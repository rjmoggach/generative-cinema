# generative-cinema

A cinematic context system for generative image/video work, packaged as one
installable plugin. It bundles four skills (the pipeline), a review crew of three
subagents, and the full film-grammar + craft + model reference library.

## Components

### Skills (the doers)

| Skill | Does | Produces |
|---|---|---|
| `project-context` | Visual-DNA interview (the look) | `project-context-{show-code}.md` |
| `sequence-design` | Plan coverage, staging, intensity arc | a numbered shot list |
| `shot-prompt` | Six-layer, model-optimized prompts | copy-paste shot prompts |
| `model-docs` | Research + write/refresh a model doc | `model-{type}-{name}.md` |

Pipeline: `project-context -> sequence-design -> shot-prompt -> prompts`.

### Agents (the review crew)

| Agent | Role | Job |
|---|---|---|
| `script-supervisor` | Continuity QC | Audit a shot list for screen direction, eyelines, the 180 line, palette/light/lens consistency |
| `director` | Creative review | Director's notes: does coverage serve the beat, does the intensity arc land, are moves motivated |
| `researcher` | Development | Isolated web research of a model's current specs, returned as a brief for `model-docs` |

### Shared library (`context/`)

One copy of the knowledge base — craft guides (`guide-*.md`), film grammar and
visual references (`reference-*.md`), per-model docs (`model-*.md`), the currency
snapshot, and skill helper files. Every skill and agent reads it via
`${CLAUDE_PLUGIN_ROOT}/context/...`, so there is no per-skill duplication.

## How it's built

The plugin is assembled from the repository's canonical sources:

```
python plugin/assemble.py        # populate plugin/context + transform skill paths
python plugin/assemble.py --package   # also build the .plugin (in /tmp, copied to outputs)
```

`context/` and `skills/*/SKILL.md` at the repo root remain the editable source of
truth; `assemble.py` regenerates `plugin/context/` and `plugin/skills/` with paths
repointed to `${CLAUDE_PLUGIN_ROOT}`. Agents, `plugin.json`, and this README are
authored directly under `plugin/`.

## Install

Install the produced `generative-cinema.plugin` from the Cowork plugins UI. Once
installed, the four skills auto-trigger on creative/library phrasing and the three
agents are available for review and research.
