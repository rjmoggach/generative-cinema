# Generative AI Context Library

**Version**: 0.2.0
**Updated**: 2026-06-29

A model-agnostic library of context for effective image and video prompting —
film-grammar references, decision-support craft guides, per-model docs, and a set
of installable agent skills that turn it all into a working pipeline.

---

## What's inside

```
context/      Knowledge the system reasons over (model docs, film grammar,
              craft guides, currency snapshot, visual references)
skills/       Agent skills (self-contained, installable) + build script
docs/         Setup and workflow guides
prompts/      Custom GPT system prompts + templates (legacy ChatGPT path)
knowledge-base/  Primary-source film texts (Arijon, Mascelli, etc.)
```

---

## The skills pipeline (recommended)

Four self-contained skills under `skills/` (see `skills/README.md`). Build/refresh
installable `.skill` packages with `python skills/build.py`.

```
project-context  ->  sequence-design  ->  shot-prompt  ->  prompts
   (the look)         (the scene plan)     (each shot)
        model-docs keeps the model docs current for all of them
```

| Skill | Level | Does |
|---|---|---|
| `project-context` | Project | Guided visual-DNA interview -> `project-context-<show-code>.md` |
| `sequence-design` | Scene | Plan coverage, staging, screen direction, intensity arc -> shot list |
| `shot-prompt` | Shot | Six-layer, model-optimized prompts honoring the project look |
| `model-docs` | Library | Research + write/refresh a model doc; sync currency |

---

## Models (12)

Always check `context/model-currency-2026-06.md` for the current version before
quoting specs — this space moves monthly.

### Image (4)

- **FLUX.2** (Pro/Flex/Dev/Klein) - fast, high-res, strong typography + reference.
- **Nano Banana 2 / Pro** (Gemini 3.1 / 3 Image) - conversational editing, text rendering.
- **Midjourney v8.1** - artistic/stylized, native HD 2K, Omni Reference.
- **Seedream 5** - ultra high-res (4K), reasons + web-searches before generating.

### Video (7)

- **Seedance 2.5** - cinematic multi-shot; up to 30s single-pass.
- **Runway Gen-4.5** - fast iteration, strong character lock, best production UI.
- **Veo 3.1** - native audio + JSON prompting.
- **Luma Ray3.2** - 16-bit HDR/EXR, frame-level keyframes for VFX.
- **Kling 3.0** - native 4K, most fluid motion, Motion Control/Brush.
- **Sora 2 / 2 Pro** - multi-shot storytelling, physics, native dialogue (API sunset Sep 24 2026).
- **Wan 2.6** - open-weights, native audio/lip-sync, self-hostable.

### Editing (1)

- **FLUX.1 Kontext** (and FLUX.2 unified editing) - iterative editing, consistency.

---

## Cinematic craft guides

Decision-support guides in `context/` (format: Decision / Use when / Because /
Prompt translation / Watch-outs / Anchors). They turn the taxonomy into judgment:

- `guide-shot-selection`, `guide-lens-language`, `guide-continuity-rules`, `guide-sequence-construction`
- `guide-visual-structure` (contrast/affinity), `guide-color-story`, `guide-creative-approaches`
- `guide-ai-generation-strategy` (craft under current model limits)

Plus the foundations: `guide-prompting-framework.md` (six-layer framework),
`reference-film-grammar.md`, `reference-film-movements.md`, and the
`reference-visual-*` style anchors (directors, cinematographers, commercial
directors, photographers).

---

## Model selection (quick guide)

| Need | Reach for | Alternative |
|---|---|---|
| Max resolution still | Seedream 5 | FLUX.2 |
| Fast, clean high-res still | FLUX.2 | Seedream 5 |
| Artistic/stylized still | Midjourney v8.1 | FLUX.2 |
| Text in image / conversational edit | Nano Banana 2 | FLUX.1 Kontext |
| Native 4K video / fluid motion | Kling 3.0 | Luma Ray3.2 |
| Multi-shot storytelling | Sora 2 | Seedance 2.5 |
| Video with audio/dialogue | Veo 3.1 | Wan 2.6 / Sora 2 |
| Fast char-consistent coverage | Runway Gen-4.5 | Kling 3.0 |
| HDR / VFX elements | Luma Ray3.2 | - |
| Open-source / local / private | Wan 2.6 | - |
| Image editing | FLUX.1 Kontext | Nano Banana 2 |

---

## Universal prompting principles

1. **Front-load style**: `"Cinematic photo of..."` (not `"...cinematic style"`).
2. **Be specific**: `"1967 red Mustang convertible"` (not `"nice car"`).
3. **Positive phrasing**: describe what you want, not what you don't.
4. **Layer information**: Style -> Subject -> Technical -> Context.
5. **Iterate**: start simple, change one element at a time.

See `context/guide-prompting-general.md` and `context/guide-prompting-framework.md`.

---

## Legacy: Custom GPT deployment

The `prompts/system-prompt-*.md` files remain valid for ChatGPT Custom GPT
setups; `docs/01-setup-custom-gpt.md` covers deployment. The `skills/` are the
agent-native equivalent and are preferred for Claude / Cowork.

---

## Maintenance

- **Refresh model facts**: `model-docs` skill; update `context/model-currency-2026-06.md`.
- **Add craft content**: follow the heuristic format; wire into `skills/build.py` MANIFEST; rebuild.
- **Rebuild skill packages**: `python skills/build.py`.
- **Log changes**: `CHANGELOG.md`.
- **File naming**: `model-<type>-<name>.md`, `guide-*.md`, `reference-*.md` (kebab-case).
