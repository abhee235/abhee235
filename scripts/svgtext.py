"""Draws text as vector paths, so it looks the same on every device.

Images in a README can't load web fonts, and system fonts differ per OS.
Martian Mono is under the SIL Open Font License, see fonts/OFL.txt.
"""
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

FONTS = {w: TTFont(Path(__file__).parent / "fonts" / f"martian-{w}.woff") for w in (400, 700)}


def width(text_value, size):
    return len(text_value) * 0.7 * size  # Martian Mono is monospaced at 700/1000 units


def text(value, x, y, size, fill, weight=400, anchor="start", element_id=None):
    font = FONTS[weight]
    glyphs, cmap = font.getGlyphSet(), font.getBestCmap()
    scale = size / font["head"].unitsPerEm
    x -= {"start": 0, "middle": width(value, size) / 2, "end": width(value, size)}[anchor]
    pen = SVGPathPen(glyphs, ntos=lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
    for ch in value:
        name = cmap.get(ord(ch), ".notdef")
        glyphs[name].draw(TransformPen(pen, (scale, 0, 0, -scale, x, y)))
        x += glyphs[name].width * scale
    attr = f' id="{element_id}"' if element_id else ""
    return f'<path{attr} fill="{fill}" d="{pen.getCommands()}"/>'
