# Model Currency Snapshot — June 2026

This file tracks the **current generation** of each documented model and the newer
releases that have appeared since the individual `model-*.md` docs were written.
The per-model docs still describe valid prompting *technique*; treat this file as
the authority on **which version is current** and **what changed**. Re-verify
quarterly — this space moves fast.

> **How to use**: When recommending or documenting a model, check this table first.
> If a doc's "Current Version" row disagrees with this file, this file wins.

---

## Image Generation

| Doc | Version at doc-writing | Current (Jun 2026) | What changed |
|---|---|---|---|
| `model-image-flux-pro.md` | FLUX.1 Pro 1.1 (Nov 2024) | **FLUX.2 Pro** (Nov 25 2025); `[flex]`, `[dev]`, `[klein]` variants (Klein Jan 2026) | 32B params, Mistral-3 24B VLM + rectified-flow transformer. Stronger photorealism, typography, multi-image reference, character consistency. Up to 4MP. |
| `model-image-gemini-flash.md` | Gemini 2.5 Flash Image ("Nano Banana") | **Nano Banana 2 = Gemini 3.1 Flash Image** (Feb 26 2026, now default); **Nano Banana Pro = Gemini 3 Pro Image** for hero/text work | 512px–4K, faster, better subject consistency and instruction following. Pro tier does advanced reasoning + high-fidelity text rendering. |
| `model-image-midjourney-v7.md` | v7 (2025) | **v8.1** (default Jun 10 2026); v8.0 alpha Mar 2026 | ~4–5× faster, better prompt adherence + small-detail retention, native HD 2K (no upscale), Draft mode, `--preview`. |
| `model-image-seedream-4.md` | 4.0 (Aug 2025) | **Seedream 5.0 Lite** (Apr 9 2026); v5 Lite (Feb 24 2026); 4.5 (Dec 2025) | v5 adds Chain-of-Thought reasoning + real-time web search before generating; 4K; higher consistency/fidelity. |

## Video Generation

| Doc | Version at doc-writing | Current (Jun 2026) | What changed |
|---|---|---|---|
| `model-video-seedance-pro.md` | Seedance 1.0 Pro | **Seedance 2.5** (announced Jun 23 2026); 2.0 prior | 2.5 generates 30s in a single pass (vs 10s). Multi-shot strengths retained. |
| `model-video-runway-gen4-turbo.md` | Gen-4 Turbo (Apr 2025) | **Gen-4.5** (Dec 2025) | Revamped motion engine: more lifelike physics, object interaction, camera moves; SOTA motion quality + prompt adherence. Still strongest end-to-end production UI (motion brush, director mode). |
| `model-video-google-veo-3-1.md` | Veo 3.1 (Oct 2025) | **Veo 3.1** still current — family is 3.1 / 3.1 Fast / 3.1 Lite | No Veo 4 as of Jun 2026. Lite is most cost-effective (720p/1080p, 4/6/8s). This doc is largely accurate. |
| `model-video-luma-ray3.md` | Ray3 (Sep 2025) | **Ray3.2** (Jun 9 2026, now with API); Ray3.14 (Jan 26 2026) | Ray3.2: up to 16 keyframes/clip for frame-level direction, native HDR + 16-bit EXR export (composites in Resolve/Nuke), full API. Ray3.14 added native 1080p, 4× faster/3× cheaper (drops char-ref + audio). |

## Image Editing

| Doc | Version at doc-writing | Current (Jun 2026) | What changed |
|---|---|---|---|
| `model-editing-flux-kontext.md` | Kontext 1.0 (Max/Pro/Dev) | Kontext still available; **FLUX.2** now unifies generation + in-context editing + multi-ref natively | For new work, evaluate FLUX.2 editing and Nano Banana 2 (excellent conversational editor) alongside Kontext. |

---

## Coverage Gaps — Models referenced but NOT yet documented

The prompting framework (`guide-prompting-framework.*`, `docs/04-six-layer-framework.md`)
gives model-specific advice for these, but the library has **no `model-*.md` doc** for them.
Priority candidates for new docs (use the `model-docs` skill):

| Model | Status (Jun 2026) | Why document it |
|---|---|---|
| **Kling 3.0** | Released Feb 5 2026 (Kuaishou) | Only model with native 4K output; ~$0.50/clip. Framework already cites "Kling 2.5". |
| **OpenAI Sora 2 / Sora 2 Pro** | Current | Multi-shot storytelling leader; framework cites it but no doc exists. |
| **Wan 2.6** | Current | Only major open-source option (24GB+ VRAM); good for local/uncensored dialogue work. Framework cites "Wan 2.5". |

---

## Maintenance

- Update this file when a documented model ships a new major version.
- When you write/refresh a full `model-*.md`, sync its "Current Version" row here.
- Convert relative dates to absolute (e.g., "last month" → "May 2026").
