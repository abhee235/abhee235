"""Rebuilds assets/stats.svg from the account's public activity.

Reads only what anyone can see. If GitHub's page changes and the numbers can't be
checked, it stops with an error and the last good panel stays in place.
"""
import json
import os
import re
import sys
import urllib.request
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from svgtext import text  # noqa: E402

LOGIN = "abhee235"
ROOT = Path(__file__).parent.parent
PANEL, INK, SOFT, MUTED, GRID = "#1E1A33", "#EDE9F7", "#B7B0CE", "#8F88AA", "#3A3456"
BAR = "#C08420"
# Checked for contrast and colour-blind separation on the panel colour, in this order.
SLOTS = ["#C08420", "#9A78EE", "#E5587A", "#4F8DF0", "#1FA193"]
OTHER = "#6B6485"
SHOWN = ["TypeScript", "JavaScript", "Python", "Rust", "C#"]


def get(url, api=False):
    headers = {"User-Agent": "profile-stats"}
    token = os.environ.get("GITHUB_TOKEN")
    if api:
        headers["Accept"] = "application/vnd.github+json"
        if token:
            headers["Authorization"] = f"Bearer {token}"
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def activity():
    html = get(f"https://github.com/users/{LOGIN}/contributions")
    head = re.search(r"([\d,]+)\s+contributions?\s+in the last year", html)
    cells = re.findall(r'data-date="(\d{4}-\d{2}-\d{2})"[^>]*?id="(contribution-day-component-\d+-\d+)"', html)
    tips = dict(re.findall(r'<tool-tip[^>]*for="(contribution-day-component-\d+-\d+)"[^>]*>\s*(.*?)\s*</tool-tip>', html, re.S))
    days = {}
    for day, cell in cells:
        m = re.match(r"([\d,]+) contribution", tips.get(cell, ""))
        days[day] = int(m.group(1).replace(",", "")) if m else 0
    if not head or sum(days.values()) != int(head.group(1).replace(",", "")):
        raise SystemExit("Contribution page didn't parse cleanly, keeping the last panel.")
    return days


def best_streak(days):
    best = run = 0
    prev = None
    for day in sorted(d for d, n in days.items() if n):
        current = date.fromisoformat(day)
        run = run + 1 if prev and current - prev == timedelta(days=1) else 1
        best, prev = max(best, run), current
    return best


def languages():
    repos = json.loads(get(f"https://api.github.com/users/{LOGIN}/repos?per_page=100&type=owner", api=True))
    totals = Counter()
    for repo in repos:
        if repo["fork"] or repo["archived"]:
            continue
        totals.update(json.loads(get(f"https://api.github.com/repos/{LOGIN}/{repo['name']}/languages", api=True)))
    if not totals:
        raise SystemExit("No language data, keeping the last panel.")
    whole = sum(totals.values())
    shares = [(name, totals[name] / whole * 100) for name in SHOWN]
    return shares + [("Other", 100 - sum(s for _, s in shares))]


def months(days):
    totals = Counter()
    for day, n in days.items():
        totals[day[:7]] += n
    return sorted(totals.items())[-12:]  # The oldest month in the window is only partly covered.


def month_label(month):
    return date.fromisoformat(month + "-01").strftime("%b %Y")


def bar_path(x, base, w, h, r=4):
    """A bar with rounded top corners, anchored flat on the baseline."""
    r = min(r, h, w / 2)
    return f"M{x:.1f} {base}v{-(h - r):.1f}q0 {-r:.1f} {r:.1f} {-r:.1f}h{w - 2 * r:.1f}q{r:.1f} 0 {r:.1f} {r:.1f}v{h - r:.1f}z"


def panel(days, shares):
    total, active, best = sum(days.values()), sum(1 for n in days.values() if n), best_streak(days)
    parts = [f'<rect width="760" height="306" rx="14" fill="{PANEL}"/>']

    parts.append(text(f"{total:,}", 28, 84, 52, INK, 700))
    parts.append(text("contributions", 28, 112, 14, SOFT))
    parts.append(text("in the last year", 28, 132, 14, SOFT))
    parts.append(text(str(active), 28, 172, 22, INK, 700))
    parts.append(text("active days", 28, 192, 12, MUTED))
    parts.append(text(f"{best} days", 164, 172, 22, INK, 700))
    parts.append(text("best streak", 164, 192, 12, MUTED))

    series = months(days)
    left, base, top, slot, bar_w = 340, 170, 62, 33, 21
    peak = max(n for _, n in series)
    parts.append(text("Contributions per month", left, 38, 13, SOFT))
    parts.append(f'<path stroke="{GRID}" d="M{left} {base + .5}h{slot * 11 + bar_w}"/>')
    for i, (_, n) in enumerate(series):
        x = left + i * slot
        h = max(2, (base - top) * n / peak)
        latest = i == len(series) - 1
        opacity = ' opacity=".55"' if latest else ""  # The current month isn't finished.
        parts.append(f'<path fill="{BAR}"{opacity} d="{bar_path(x, base, bar_w, h)}"/>')
        if n == peak or latest:
            parts.append(text(str(n), x + bar_w / 2, base - h - 8, 12, INK, 700, "middle"))
    parts.append(text(month_label(series[0][0]), left, base + 20, 11, MUTED))
    end = left + (len(series) - 1) * slot + bar_w
    parts.append(text(month_label(series[-1][0]) + " so far", end, base + 20, 11, MUTED, anchor="end"))

    parts.append(text("Code by language, public repos", 28, 226, 13, SOFT))
    x, gap = 28.0, 2
    usable = 704 - gap * (len(shares) - 1)
    colors = SLOTS + [OTHER]
    for i, (_, share) in enumerate(shares):
        segment = usable * share / 100
        radius = 3 if segment > 8 else 1
        parts.append(f'<rect x="{x:.1f}" y="238" width="{segment:.1f}" height="12" rx="{radius}" fill="{colors[i]}"/>')
        x += segment + gap
    for i, (name, share) in enumerate(shares):
        lx, ly = 28 + (i % 3) * 240, 271 + (i // 3) * 21
        parts.append(f'<rect x="{lx}" y="{ly - 10}" width="10" height="10" rx="2" fill="{colors[i]}"/>')
        parts.append(text(f"{name} {share:.1f}%", lx + 18, ly, 12, SOFT))

    svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 306" role="img">' + "".join(parts) + "</svg>"
    per_month = ", ".join(f"{month_label(m)} {n}" for m, n in series)
    by_language = ", ".join(f"{name} {share:.1f}%" for name, share in shares)
    alt = (
        f"{total:,} contributions in the last year, across {active} active days, with a best streak of {best} days. "
        f"Per month: {per_month}. Code by language in public repos: {by_language}."
    )
    return svg, alt


def main():
    svg, alt = panel(activity(), languages())
    (ROOT / "assets" / "stats.svg").write_text(svg + "\n", encoding="utf-8")
    readme = ROOT / "README.md"
    if readme.exists():
        page = readme.read_text(encoding="utf-8")
        page = re.sub(r'(src="assets/stats\.svg"[^>]*alt=")[^"]*"', lambda m: f'{m.group(1)}{alt}"', page)
        readme.write_text(page, encoding="utf-8")
    print(alt)


if __name__ == "__main__":
    main()
