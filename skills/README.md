# Skills

Agent Skills built as an evolution of this context library. They package the
knowledge that powered the Custom GPT system prompts into portable,
progressively-disclosed skills usable by any skill-aware agent (Claude / Cowork).

Each skill is a **self-contained package**: a `SKILL.md` (YAML frontmatter +
instructions) plus a `references/` folder that bundles every file it needs. A
packaged `.skill` has no external path dependencies, so it works once shared or
installed.

## Source of truth vs. packages

The library's `context/` directory is the **single source of truth** for the
shared material (model docs, film grammar, craft guides, reference tables). To
keep things DRY while still shipping self-contained skills, each skill's
`references/` holds *generated copies* synced from `context/` by the build
script — you edit `context/`, then rebuild.

```
python skills/build.py          # sync references from context/ + package to skills/dist/
python skills/build.py --sync   # only refresh the bundled copies
python skills/build.py --zip    # only rebuild the .skill zips
```

`skills/dist/*.skill` are the installable/shareable packages. What each skill
bundles is declared in the `MANIFEST` in `build.py`.

## The four skills

| Skill | Level | Does | Produces |
|---|---|---|---|
| `project-context/` | Project | Guided visual-DNA interview | `project-context-<show-code>.md` |
| `sequence-design/` | Scene | Plan coverage, staging, intensity arc | A numbered shot list |
| `shot-prompt/` | Shot | Six-layer, model-optimized prompt generation | Copy-paste shot prompts |
| `model-docs/` | Library | Research + write/refresh a model doc | `model-<type>-<name>.md` + currency sync |

## Pipeline

```
project-context  ->  sequence-design  ->  shot-prompt  ->  prompts
   (the look)         (the scene plan)     (each shot)
        model-docs keeps context/model-*.md current for all of them
```

1. **project-context** once per project to lock the look.
2. **sequence-design** per scene to plan coverage, screen direction, intensity arc.
3. **shot-prompt** per shot to emit model-optimized prompts from that plan.
4. **model-docs** whenever a model is added or its facts age (also updates the
   currency snapshot). After editing `context/`, run `build.py` to re-sync.

## Craft guides (in `context/`, bundled per skill)

Decision-support guides (heuristic format: Decision / Use when / Because / Prompt
translation / Watch-outs / Anchors):

- `guide-shot-selection`, `guide-lens-language`, `guide-continuity-rules`,
  `guide-sequence-construction` (shot + scene craft)
- `guide-visual-structure`, `guide-color-story`, `guide-creative-approaches`
  (visual structure, color, authorial voice)
- `guide-ai-generation-strategy` (craft under current model limits)

## Why skills (vs. the Custom GPT prompts)

- Progressive disclosure: only the relevant reference loads into context.
- Portable + self-contained: no ChatGPT upload steps, no broken relative paths.
- Auto-triggering: descriptions are written to trigger on natural phrasing.

The original `prompts/system-prompt-*.md` files remain valid for ChatGPT Custom
GPT deployment; these skills are the agent-native equivalent.
