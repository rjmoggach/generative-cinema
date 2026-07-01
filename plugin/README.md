# generative-cinema

A flexible plugin for getting **cinematic, model-optimized prompts** for generative
image/video — at any level of structure. Ask for a great one-off still prompt, the
next shot from a still, a sequence's coverage, a shot within a sequence, or the
full project → sequence → shot chain. The plugin pairs a production *workflow*
(skills) with a *crew* you can talk to (agents), backed by one shared film-grammar
+ craft + model library.

You are the **Creative Director**: you set the brief and approve. The crew does the work.

## Flexible entry — work at whatever level you have

| You want… | Ask | Who handles it |
|---|---|---|
| A great one-off still prompt | "great prompt for X" | `cinematographer` (or `shot-prompt`) |
| A shot from a still | "next shot from this still" | `cinematographer` |
| A scene's coverage / shot list | "break down this scene" | `first-ad` (or `sequence-design`) |
| A shot within a sequence | "give me the next shot" | `cinematographer` |
| To transform a clip you already have | "add X to this video / swap the world" | `cinematographer` (or `footage-transform`) |
| To edit a still you already have | "change this image to X / swap the background" | `image-edit` |
| A whole project's look first | "define the look" | `project-context` |
| The full chain | start at project, flow down | the crew, in order |

No project context is required for a one-off — only load a show bible when you want
every output locked to the same look.

## Skills (seven)

| Skill | Does | Produces |
|---|---|---|
| `project-context` | Visual-DNA interview (the look) | `project-context-{show-code}.md` |
| `sequence-design` | Plan coverage, staging, intensity arc | a numbered shot list |
| `shot-prompt` | Six-layer, model-optimized prompts | copy-paste shot prompts |
| `footage-transform` | Video-to-video: preserve a real clip, change one thing | copy-paste v2v prompts |
| `image-edit` | Image-to-image: preserve a real still, change one thing | copy-paste i2i prompts |
| `character-sheet` | Build a persistent character reference: hero identity, turnaround, wardrobe + HMU states | `char-{show}-{name}.md` + `assets/char/{name}/` |
| `model-docs` | Research + write/refresh a model doc | `model-{type}-{name}.md` |

## Agents (the crew you talk to)

Crew personas that apply the skills' craft with a role's judgment and voice.

| Agent | Role | What you ask for |
|---|---|---|
| `director` | Director | "Direct this scene", "your take", "director's notes" — intent, approach, coverage calls (you brief it as Creative Director) |
| `cinematographer` | DP | "Give me the next shot", "a great prompt for this still" — hands back a finished, model-optimized prompt |
| `first-ad` | 1st AD | "Break down this scene", "build a shot list" — an ordered coverage plan |
| `script-supervisor` | Continuity | "Does this cut together?" — audits screen direction, eyelines, the line, look consistency |
| `researcher` | Research | "Research model X" — isolated web research feeding `model-docs` |
| `casting-director` | Art dept | "Lock a character's identity" — hero portrait, multi-angle bundle, locked descriptor block |
| `costume-designer` | Art dept | "Build the turnaround / wardrobe continuity" — character model sheet + wardrobe states |
| `makeup-hair` | Art dept | "Lock the HMU states" — clean/aged/wounded/wet state references per character |

Typical flow: you brief the **Director** → the **1st AD** breaks down coverage →
the **DP** hands back each shot's prompt → the **Script Supervisor** checks it cuts
together. Or skip straight to the **DP** for a single shot or one-off still.

## Shared library (`context/`)

One copy of the knowledge base — craft guides (`guide-*.md`), film grammar and
visual references (`reference-*.md`), creative references (`reference-craft-*.md`),
per-model docs (`model-*.md`), the currency snapshot, and skill helper files. Every
skill and agent reads it via `${CLAUDE_PLUGIN_ROOT}/context/...`, so there is no
per-skill duplication. Character-pipeline additions: `guide-character-consistency.md`,
`guide-turnaround-sheets.md`, `reference-craft-character.md`, and the typed asset
naming taxonomy in `guide-asset-reference.md` (`assets/{type}/{name}/`).

## How it's built

Assembled from the repository's canonical sources:

```
python plugin/assemble.py            # populate plugin/context + transform skill paths, validate
python plugin/assemble.py --package  # also build the .plugin (in /tmp, copied to outputs)
```

`context/` and `skills/*/SKILL.md` at the repo root are the editable source of
truth; `assemble.py` regenerates `plugin/context/` and `plugin/skills/` with paths
repointed to `${CLAUDE_PLUGIN_ROOT}`. Agents, `plugin.json`, and this README are
authored directly under `plugin/`. The committed `plugin/` is the complete,
self-contained plugin — nothing needs building to install.

## Install

**Cowork:** download the latest [`generative-cinema.plugin`](https://github.com/rjmoggach/generative-cinema/releases/latest/download/generative-cinema.plugin) from Releases, open it in chat, and press install.

**Claude Code (from this repo as a marketplace):**

```
/plugin marketplace add rjmoggach/generative-cinema
/plugin install generative-cinema@generative-cinema
```

Or from a local clone: `/plugin marketplace add ./generative-cinema` then the same
install. Skills are namespaced (e.g., `generative-cinema:shot-prompt`); the crew
agents become available to the main agent.
