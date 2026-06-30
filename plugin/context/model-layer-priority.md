# Model Layer Priority & Syntax Notes

Which of the six layers matter most per model, plus syntax quirks. Always confirm
the **current version** in `../../context/model-currency-2026-06.md` and read the
matching `../../context/model-*.md` for full parameters.

## Image

### FLUX.2 (was FLUX.1 Pro) — `model-image-flux-pro.md`
- Emphasize Layers 1, 2, 4. Front-load style/medium.
- API-controlled (mode, resolution), not `--` flags. Strong typography + multi-ref.
- Use for establishing stills and final high-res assets.

### Midjourney v8.1 (was v7) — `model-image-midjourney-v7.md`
- Emphasize Layers 1, 2, 4. Parameter-driven (`--ar`, `--s`, `--chaos`).
- Omni Reference for character consistency; Draft mode for fast iteration; native HD 2K.
- Best for artistic/stylized concept and keyframes.

### Seedream 5 (was 4.0) — `model-image-seedream-4.md`
- Emphasize Layers 1, 2, 4. **Supports negative prompts** (use to strip artifacts).
- 4K native; v5 reasons + web-searches before generating. Good for print/diagram fidelity.

### Nano Banana 2 / Pro (Gemini Flash family) — `model-image-gemini-flash.md`
- Narrative paragraphs over keyword lists. Best conversational editor + text rendering.
- Use for "now change X" iterative edits and text-in-image.

## Video

### Seedance 2.5 (was 1.0 Pro) — `model-video-seedance-pro.md`
- Use **all 6 layers**; excels at multi-shot sequences. **No negative prompts.**
- Describe shot switches explicitly. 2.5 supports up to 30s single-pass.

### Runway Gen-4.5 (was Gen-4 Turbo) — `model-video-runway-gen4-turbo.md`
- Emphasize Layers 1, 2, 3 — **movement is critical**. Fast, strong character lock.
- Best end-to-end production UI (motion brush, director mode). Use for coverage iteration.

### Veo 3.1 — `model-video-google-veo-3-1.md`
- Use **all 6 layers**; accepts **JSON** prompts; **native audio** (dialogue/SFX/music).
- Use when audio sync or precise control matters. Has a `negative_prompt` field.

### Luma Ray3.2 (was Ray3) — `model-video-luma-ray3.md`
- Emphasize Layer 5 (HDR, physics) + frame-level keyframes (up to 16/clip).
- 16-bit EXR/HDR export for compositing (Resolve/Nuke). Use for VFX-grade elements.

### Kling 3.0 — `model-video-kling-3.md`
- Emphasize Layers 1, 2, 3 — **most fluid motion**; native 4K. Match duration to action.
- Use Motion Brush / Motion Control to direct movement rather than text alone.

### Sora 2 / 2 Pro — `model-video-sora-2.md`
- Emphasize Layers 1, 2, 6 — **multi-shot storytelling** in one prompt; strong physics.
- Native dialogue; describe shot order + spatial continuity. (API sunsets Sep 24 2026.)

### Wan 2.6 — `model-video-wan-2-6.md`
- Use all 6 layers; **open-source**, native audio/lip-sync. Best for local/cost-sensitive dialogue.
- Specify line, emphasis, and gesture for lip-sync quality.

## Editing

### FLUX.1 Kontext / FLUX.2 editing — `model-editing-flux-kontext.md`
- Describe the change while explicitly preserving identity/features.
- For new work also consider FLUX.2 unified editing and Nano Banana 2.

## Adding more models
Use the `model-docs` skill and update `model-currency-2026-06.md`. All models the
framework references are now documented.
