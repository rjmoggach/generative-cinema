# generative-wrangler

**Version**: 0.8.0 · **Updated**: 2026-07-01

A flexible plugin for getting **cinematic, model-optimized prompts** for generative
image and video — at any level of structure. Ask for a great one-off still prompt,
the next shot from a still, a scene's coverage, a shot within a sequence, an edit to
a still or clip you already have, or the full project → sequence → shot chain. It
pairs a production *workflow* (skills) with a *crew* you talk to (agents), backed by a
film-grammar + craft + model reference library.

You are the **Creative Producer**: you set the brief and approve. The crew does the work.

This repository is also a **Claude Code plugin marketplace** — the installable
plugin lives in [`plugin/`](plugin/), and the editable source it's built from lives
at the repo root (`context/`, `skills/`).

---

## Install

**Cowork:** download the latest [`generative-wrangler.plugin`](https://github.com/rjmoggach/generative-wrangler/releases/latest/download/generative-wrangler.plugin) from [Releases](https://github.com/rjmoggach/generative-wrangler/releases/latest), open it in chat, and press install.

**Claude Code:**

```
/plugin marketplace add rjmoggach/generative-wrangler
/plugin install generative-wrangler@generative-wrangler
```

Or from a local clone: `/plugin marketplace add ./generative-wrangler` then the same install.

---

## Flexible entry — work at whatever level you have

| You want… | Ask | Who handles it |
|---|---|---|
| A great one-off still prompt | "great prompt for X" | `cinematographer` (or `shot-prompt`) |
| A shot from a still | "next shot from this still" | `cinematographer` |
| A scene's coverage / shot list | "break down this scene" | `first-ad` (or `sequence-design`) |
| A shot within a sequence | "give me the next shot" | `cinematographer` |
| To transform a clip you already have | "add X to this video / swap the world" | `cinematographer` (or `footage-transform`) |
| To edit a still you already have | "change this image to X / swap the background" | `cinematographer` (or `image-edit`) |
| A whole project's look first | "define the look" | `project-context` |
| The full chain | start at project, flow down | the crew, in order |

No project context is required for a one-off — only load a show bible when you want
every output locked to the same look.

---

## The crew

Skills are the production workflow; agents are the crew you talk to, applying the
skills' craft with a role's judgment.

### Skills (the workflow)

| Skill | Level | Does |
|---|---|---|
| `project-context` | Project | Visual-DNA interview → `project-context-{show-code}.md` |
| `art-direction` | World bible / Project | PD interview → `art-bible-{show}.md`: palette, material/CMF, era, global style ref, asset index |
| `sequence-design` | Scene | Plan coverage, staging, screen direction, intensity arc → shot list |
| `shot-prompt` | Shot | Six-layer, model-optimized prompts honoring the project look |
| `footage-transform` | Shot (v2v) | Video-to-video prompts: preserve a real clip, change one thing (VFX, world swap, timed moves) |
| `image-edit` | Shot (i2i) | Image-to-image prompts: preserve a real still, change one thing (recolor, world swap, add/age, relight, compose locked refs) |
| `character-sheet` | Asset | Build a persistent character reference: hero identity, turnaround, wardrobe + HMU states |
| `prop-turntable` | Asset | Build a persistent prop reference: hero anchor, orthographic ring, detail views, state variants/multiples |
| `location-pack` | Asset | Build a location/set reference: master establishing plate, coverage, time-of-day/weather variants, continuity table |
| `model-docs` | Library | Research + write/refresh a model doc; sync currency |

### Agents (the crew)

| Agent | Role | You ask for |
|---|---|---|
| `director` | Director | Intent, approach, coverage calls, notes (you brief it as Creative Producer) |
| `production-designer` | Art dept lead | "Set the world" — the art-bible interview, then delegates to casting/costume/makeup-hair/propmaster/location-scout |
| `cinematographer` | DP | "Give me the next shot" / "a great prompt for this still" — a finished prompt |
| `first-ad` | 1st AD | "Break down this scene" — an ordered coverage shot list |
| `script-supervisor` | Continuity | "Does this cut together?" — screen direction, eyelines, the line, look consistency |
| `researcher` | Research | "Research model X" — isolated web research feeding `model-docs` |
| `casting-director` | Art dept | "Lock a character's identity" — hero portrait, multi-angle bundle, locked descriptor block |
| `costume-designer` | Art dept | "Build the turnaround / wardrobe continuity" — character model sheet + wardrobe states |
| `makeup-hair` | Art dept | "Lock the HMU states" — clean/aged/wounded/wet state references per character |
| `propmaster` | Art dept | "Build the prop turntable" — hero anchor, multi-angle ring, detail and state variants |
| `location-scout` | Art dept | "Build the location pack" — master plate, coverage, time/weather variants |

Typical flow: brief the **Director** → the **Production Designer** sets the world
and delegates to the art-dept sub-roles (**casting director** → **costume
designer** → **makeup & hair** → **propmaster** → **location scout**) → the **1st
AD** breaks down coverage → the **DP** hands back each shot's prompt → the
**Script Supervisor** checks it cuts together. Or skip straight to the **DP** for
a single shot or one-off still.

---

## Models (12)

Check `context/model-currency-2026-06.md` for the current version before quoting
specs — this space moves monthly.

**Image (4):** FLUX.2 · Nano Banana 2 / Pro (Gemini 3.1 / 3 Image) · Midjourney v8.1 · Seedream 5.
**Video (7):** Seedance 2.5 · Runway Gen-4.5 · Veo 3.1 · Luma Ray3.2 · Kling 3.0 · Sora 2 / 2 Pro (API sunset Sep 24 2026) · Wan 2.6.
**Editing (1):** FLUX.1 Kontext (and FLUX.2 unified editing).

| Need | Reach for | Alternative |
|---|---|---|
| Max resolution still | Seedream 5 | FLUX.2 |
| Fast, clean high-res still | FLUX.2 | Seedream 5 |
| Artistic / stylized still | Midjourney v8.1 | FLUX.2 |
| Text in image / conversational edit | Nano Banana 2 | FLUX.1 Kontext |
| Native 4K video / fluid motion | Kling 3.0 | Luma Ray3.2 |
| Multi-shot storytelling | Sora 2 | Seedance 2.5 |
| Video with audio / dialogue | Veo 3.1 | Wan 2.6 / Sora 2 |
| Fast char-consistent coverage | Runway Gen-4.5 | Kling 3.0 |
| HDR / VFX elements | Luma Ray3.2 | — |
| Open-source / local / private | Wan 2.6 | — |
| Image editing | FLUX.1 Kontext | Nano Banana 2 |

---

## Craft guides

Decision-support guides in `context/` (format: Decision / Use when / Because /
Prompt translation / Watch-outs / Anchors) that turn the taxonomy into judgment:
`guide-shot-selection`, `guide-lens-language`, `guide-continuity-rules`,
`guide-sequence-construction`, `guide-visual-structure` (contrast/affinity),
`guide-color-story`, `guide-creative-approaches`, `guide-ai-generation-strategy`.
Editing / asset workflow: `guide-footage-transformation` (video-to-video),
`guide-image-editing` (image-to-image), and `guide-asset-reference` (building reusable
character/prop/location anchors; typed asset naming: `assets/{type}/{name}/`, codes
`char`/`prop`/`set`/`veh`/`cam`/`light`/`style`/`fx`). Character pipeline:
`guide-character-consistency` (hero ref, descriptor block, HMU/wardrobe state libraries),
`guide-turnaround-sheets` (model-sheet views and alignment conventions), and
`reference-craft-character` (casting/costume/makeup-hair artistry with real-master anchors).
Props & locations pipeline: `guide-prop-turntable` (object multi-view conventions,
framing-the-asset rules), `guide-location-pack` (master-plate + coverage + variant
conventions, continuity table), and `reference-craft-artdept` (props + locations/sets
artistry with real-master anchors). Asset paths: `assets/prop/{name}/` (prop turntables)
and `assets/set/{name}/` (location/set packs). World bible: `guide-art-direction`
(palette/CMF, era, top-down inheritance mechanics) governs the art-bible that every
asset sheet inherits from.
Foundations: `guide-prompting-framework` (the six-layer framework),
`reference-film-grammar`, `reference-film-movements`, and the `reference-visual-*`
style anchors (directors, cinematographers, commercial directors, photographers).

---

## Repository layout

```
.claude-plugin/marketplace.json   This repo as a Claude Code marketplace → ./plugin
plugin/                           The installable generative-wrangler plugin (assembled)
  ├── .claude-plugin/plugin.json
  ├── skills/   (10)   agents/ (11)   context/ (the bundled library)
  └── assemble.py                  Builds plugin/ from the repo-root sources
context/                          Source of truth: model docs, craft guides, references
skills/                           Source skill definitions (with bundled references/)
docs/                             Setup + workflow guides
prompts/                          Legacy Custom GPT system prompts + templates
knowledge-base/                   Primary-source film texts (Arijon, Mascelli, …)
```

`context/` and `skills/` are the editable source of truth. `python plugin/assemble.py`
regenerates `plugin/context/` and `plugin/skills/` with paths repointed to
`${CLAUDE_PLUGIN_ROOT}`; the committed `plugin/` is the complete, self-contained
plugin. Use `--package` to also build the clickable `.plugin`.

---

## Maintenance

- **Refresh model facts:** `model-docs` skill (or the `researcher` agent); update `context/model-currency-2026-06.md`.
- **Add craft content:** write in the heuristic format under `context/`, wire into `skills/build.py` + `plugin/assemble.py`, rebuild.
- **Rebuild the plugin:** `python plugin/assemble.py` (add `--package` to build `generative-wrangler.plugin`). The `.plugin` is **not** committed — attach it to a GitHub Release on each version bump (`gh release create vX.Y.Z generative-wrangler.plugin`) so the Cowork download link stays current.
- **Log changes:** `CHANGELOG.md`.

---

## Legacy: Custom GPT deployment

The `prompts/system-prompt-*.md` files remain valid for ChatGPT Custom GPT setups
(`docs/01-setup-custom-gpt.md`). The plugin is the agent-native equivalent and is
preferred for Claude / Cowork.
