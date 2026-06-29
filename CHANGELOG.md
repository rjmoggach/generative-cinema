# Changelog

All notable changes to the Generative AI Context Library will be documented in this file.

## v0.2 - 2026-06-29

### Model currency refresh (June 2026)

- Added `context/model-currency-2026-06.md` as the single source of truth for current model versions.
- Added a currency callout to each of the 9 original model docs (FLUX.2, Nano Banana 2, Midjourney v8.1, Seedream 5, Seedance 2.5, Runway Gen-4.5, Veo 3.1, Luma Ray3.2).

### New model docs (12 models total)

- `model-video-kling-3.md` - Kling 3.0 (native 4K, fluid motion, Motion Control/Brush).
- `model-video-sora-2.md` - Sora 2 / 2 Pro (multi-shot storytelling, native dialogue; API sunset Sep 24 2026).
- `model-video-wan-2-6.md` - Wan 2.6 (open-weights, native audio/lip-sync, self-hostable).

### Cinematic craft guides (decision-support)

Heuristic-format guides (Decision / Use when / Because / Prompt translation / Watch-outs / Anchors):

- `guide-shot-selection.md`, `guide-lens-language.md`, `guide-continuity-rules.md`, `guide-sequence-construction.md` (P0).
- `guide-visual-structure.md`, `guide-color-story.md`, `guide-creative-approaches.md` (P1).
- `guide-ai-generation-strategy.md` (P2 - craft under current model limits).
- See `CRAFT-EXPANSION-PROPOSAL.md` for the roadmap.

### Agent skills (`skills/`)

Evolved the Custom GPT prompts into self-contained, progressively-disclosed skills:

- `project-context` (visual DNA interview), `sequence-design` (scene/coverage planning), `shot-prompt` (six-layer prompt generation), `model-docs` (document/refresh a model).
- `skills/build.py` syncs `context/` into each skill's bundled `references/` and packages installable `.skill` files to `skills/dist/` (git-ignored).
- Pipeline: project-context -> sequence-design -> shot-prompt -> prompts.

## v0.1 - 2025-11-07

### Initial Release

**9 Production-Ready Models:**
- Image Generation (4): FLUX.1 Pro, Gemini Flash, Midjourney v7, Seedream 4.0
- Video Generation (4): Seedance Pro, Runway Gen-4 Turbo, Google Veo 3.1, Luma Ray3
- Image Editing (1): FLUX.1 Kontext

**Show Context System:**
- Meta-generator for creating show context documents (20 essential questions)
- Template for manual creation
- Complete example: luxury automotive commercial

**Custom GPT Integration:**
- Meta-generator for system prompts
- Generic template for quick setup
- Complete deployment guide

**Documentation:**
- 9 model documentation files (consistent template structure)
- Setup guide for Custom GPT deployment
- Common workflow examples
- Model selection decision guide
- Universal prompting principles

**Process Tools:**
- Meta-generator for show contexts
- Meta-generator for system prompts
- Model documentation template
- All files follow `meta-generator-[TYPE]-[SUBTYPE].md` naming convention

**File Structure:**
- `context/` - 9 model documentation files
- `docs/` - Setup guides, workflows, model selection
- `prompts/` - 7 meta-generators and templates
