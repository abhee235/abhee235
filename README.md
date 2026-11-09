<img src="assets/banner.svg" width="100%" alt="A terminal window. whoami prints Abhishek Kumar Singh. cat mission.txt prints: I build developer tools that run on your own machine. Kuchu, a small white robot, stands in the corner of the terminal.">

This year I've shipped an AI app builder that needs no cloud, a desktop for Linux servers that installs nothing on the server, and a desk pet that shows what Claude Code is doing. All three are open source under the MIT license.

<img src="https://img.shields.io/badge/TypeScript-1E1A33?style=for-the-badge&logo=typescript&logoColor=F5B14C" alt="TypeScript"> <img src="https://img.shields.io/badge/Rust-1E1A33?style=for-the-badge&logo=rust&logoColor=F5B14C" alt="Rust"> <img src="https://img.shields.io/badge/Python-1E1A33?style=for-the-badge&logo=python&logoColor=F5B14C" alt="Python"> <img src="https://img.shields.io/badge/C%23-1E1A33?style=for-the-badge&logo=dotnet&logoColor=F5B14C" alt="C#"> <img src="https://img.shields.io/badge/React-1E1A33?style=for-the-badge&logo=react&logoColor=45C7B7" alt="React"> <img src="https://img.shields.io/badge/Node.js-1E1A33?style=for-the-badge&logo=nodedotjs&logoColor=45C7B7" alt="Node.js"> <img src="https://img.shields.io/badge/Electron-1E1A33?style=for-the-badge&logo=electron&logoColor=45C7B7" alt="Electron"> <img src="https://img.shields.io/badge/Tauri-1E1A33?style=for-the-badge&logo=tauri&logoColor=45C7B7" alt="Tauri"> <img src="https://img.shields.io/badge/Ollama-1E1A33?style=for-the-badge&logo=ollama&logoColor=FF7A90" alt="Ollama"> <img src="https://img.shields.io/badge/Docker-1E1A33?style=for-the-badge&logo=docker&logoColor=FF7A90" alt="Docker"> <img src="https://img.shields.io/badge/Linux-1E1A33?style=for-the-badge&logo=linux&logoColor=FF7A90" alt="Linux"> <img src="https://img.shields.io/badge/GitHub_Actions-1E1A33?style=for-the-badge&logo=githubactions&logoColor=FF7A90" alt="GitHub Actions">

## `~/projects`

<a href="https://appbuilder.sh"><img align="right" width="400" src="assets/cascade.webp" alt="Cascade building a bike accessories store, with the chat on the left and a live preview on the right"></a>

### [Cascade](https://github.com/abhee235/cascade-ai)

Build real apps from a prompt, right on your own machine. Describe what you want, and an agent writes the code, runs it in a sandboxed container and shows you a live preview. Use local Ollama models or bring your own key, in the desktop app or in VS Code.

<sub>Built with TypeScript, Electron, Docker, Ollama and MCP</sub>

[Website](https://appbuilder.sh) &nbsp; [Download](https://appbuilder.sh/#download) &nbsp; [Code](https://github.com/abhee235/cascade-ai)

<br clear="all">

<a href="https://headlessos.com"><img align="right" width="400" src="assets/headlessos.webp" alt="HeadlessOS showing a server dashboard with CPU, memory, disks and network on a desktop with a dock"></a>

### [HeadlessOS](https://github.com/abhee235/headlessos)

A Windows-like desktop for headless Linux servers. Files, Docker, processes and a terminal, all over plain SSH with nothing installed on the server. Its AI agents pick from a fixed list of actions, and anything that changes the server waits for your approval.

<sub>Built with TypeScript, React, Fastify, Electron and SSH</sub>

[Website](https://headlessos.com) &nbsp; [Download](https://headlessos.com/download) &nbsp; [Code](https://github.com/abhee235/headlessos)

<br clear="all">

<a href="https://abhee235.github.io/kuchu/"><img align="right" width="400" src="assets/kuchu.webp" alt="Kuchu, a small robot desk pet, beside a card asking whether to allow an edit in Claude Code"></a>

### [Kuchu](https://github.com/abhee235/kuchu)

A desk pet for Claude Code. It thinks, works, waves when a session needs you and hops when one is done. Its card shows what's happening and lets you answer permission requests right there. On the Microsoft Store, with macOS in preview.

<sub>Built with Rust, Tauri and TypeScript</sub>

[Website](https://abhee235.github.io/kuchu/) &nbsp; [Microsoft Store](https://apps.microsoft.com/detail/9NNK1Q800R84) &nbsp; [Code](https://github.com/abhee235/kuchu)

<br clear="all">

**Also worth a look:** [neural-nets](https://github.com/abhee235/neural-nets), a build-it-yourself course on transformers and GPT-style models in TypeScript with no ML libraries, and [floorplan-ai](https://github.com/abhee235/floorplan-ai), which turns floor plans and briefs into editable 3D office models with a traceable bill of materials.

## `~/stats`

<img src="assets/stats.svg" width="100%" alt="1,856 contributions in the last year, across 171 active days, with a best streak of 17 days. Per month: Dec 2025 52, Jan 2026 61, Feb 2026 8, Mar 2026 24, Apr 2026 124, May 2026 29, Jun 2026 79, Jul 2026 250, Aug 2026 211, Sep 2026 163, Oct 2026 565, Nov 2026 287. Code by language in public repos: TypeScript 80.0%, JavaScript 5.5%, Python 3.7%, Rust 2.1%, C# 1.6%, Other 7.2%.">

## `~/principles.ts`

```ts
const principles = {
  localFirst: "If it can run on your machine, it should. No account, no telemetry.",
  safeAgents: "Sandboxes, typed actions, approvals and audit logs, not just a model with a shell.",
  shipIt: "Installers, docs, websites and release pipelines are part of the work.",
};
```
