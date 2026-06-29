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
shared material (model docs, film grammar, framework, reference tables). To keep
things DRY while still shipping self-contained skills, each skill's `references/`
holds *generated copies* synced from `context/` by the build script — you edit
`context/`, then rebuild.

```
python skills/build.py          # sync references from context/ + package to skills/dist/
python skills/build.py --sync   # only refresh the bundled copies
python skills/build.py --zip    # only rebuild the .skill zips
```

`skills/dist/*.skill` are the installable/shareable packages. What each skill
bundles is declared in the `MANIFEST` in `build.py`.

## The three skills

| Skill | Replaces (Custom GPT) | Does | Produces |
|---|---|---|---|
| `project-context/` | Project Context Assistant | Guided visual-DNA interview | `project-context-<show-code>.md` |
| `shot-prompt/` | Shot Assistant | Six-layer, model-optimized prompt generation | Copy-paste shot prompts |
| `model-docs/` | Model Context Generator | Research + write/refresh a model doc | `model-<type>-<name>.md` + currency sync |

## Pipeline

```
project-context  ->  (project-context-<show>.md)  ->  shot-prompt  ->  prompts
        model-docs keeps context/model-*.md current for both
```

1. Run **project-context** once per project to lock the look.
2. Run **shot-prompt** per shot/sequence; it loads the context file and a target
   model's bundled doc, then emits model-optimized prompts.
3. Run **model-docs** whenever a model is added or its facts age; it also updates
   the currency snapshot. After editing `context/`, run `build.py` to re-sync.

## Why skills (vs. the Custom GPT prompts)

- Progressive disclosure: only the relevant reference loads into context.
- Portable + self-contained: no ChatGPT upload steps, no broken relative paths.
- Auto-triggering: descriptions are written to trigger on natural phrasing.

The original `prompts/system-prompt-*.md` files remain valid for ChatGPT Custom
GPT deployment; these skills are the agent-native equivalent.
