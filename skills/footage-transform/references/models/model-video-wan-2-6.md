# Wan 2.6 - Video Generation

> **Currency (Jun 2026):** Current open-source generation (Alibaba, Dec 2025). The major open-weights option, with native audio. See [`model-currency-2026-06.md`](model-currency-2026-06.md).

---

## Quick Reference

| Attribute | Value |
|---|---|
| **Current Version** | Wan 2.6 (Dec 2025) |
| **Model Type** | Text-to-Video, Image-to-Video (open weights) |
| **Primary Use** | Local/self-hosted generation; dialogue + lip-sync; cost-sensitive work |
| **Max Resolution** | 1080p, 24 fps |
| **Max Duration** | Up to 15 seconds |
| **Architecture** | Mixture-of-Experts, 14B params |
| **Local Requirements** | Min 24GB VRAM (RTX 4090), 64GB RAM, CUDA 12.1+ (32GB+ VRAM recommended) |
| **Key Features** | Native audio (dialogue/SFX/lip-sync), multi-shot, source-image support, open license |

---

## Overview

Wan 2.6 (Alibaba) is the most capable open-source video model of the cycle. It generates up to 15s at 1080p/24fps with native audio produced in the same pass — synchronized dialogue, sound effects, and lip movement — plus multi-shot and image-to-video support. Being open-weights, it can run locally (or via hosted APIs) for privacy, customization, and low marginal cost.

> **Tip:** Wan is the pick when you need to self-host (privacy, fine-tuning, no per-clip fees) or want strong lip-sync dialogue cheaply.

---

## When to Use This Model

- **Use Wan 2.6 for**: local/offline generation, dialogue/lip-sync, high-volume or cost-sensitive work, custom fine-tuning.
- **Consider Sora 2 / Veo 3.1 for**: top-tier fidelity, multi-shot polish, hosted convenience.
- **Consider Kling 3.0 for**: 4K and the most fluid motion.
- **Note**: quality is competitive with commercial models from ~6-12 months prior — excellent for open weights, not quite frontier.

---

## Prompting Structure

Wan accepts JSON or natural-language prompts. For dialogue, describe the visual, then the spoken line and delivery.

**Core Framework (dialogue)**: `[Visual description]. The character says "[line]" with [tone]. [Lip-sync/gesture/expression notes].`

> **Tip:** Because audio is generated with the video, specify emphasis words and gestures for better lip-sync and performance.

---

## Parameters

| Parameter | Type | Description |
|---|---|---|
| `prompt` | String | Visual (and dialogue) description. |
| `resolution` | String | up to `1080p`. |
| `duration` | Integer | up to 15 seconds. |
| `aspect_ratio` | String | e.g., `16:9`, `9:16`. |
| `seed` | Integer | Reproducibility. |
| `audio` | File/Bool | Provide an audio track or enable native audio generation. |
| `image` | Image | Source image for image-to-video. |

---

## Techniques

### Basic: Text-to-video
`"A neon-lit night market in the rain, vendors under awnings, steam rising, handheld documentary feel, 1080p."`

### Intermediate: Native dialogue + lip-sync
`"Medium shot of a fisherman on a dock at dawn. He says 'The tide's turning' with weary resolve, emphasis on 'turning'. Accurate lip-sync, breath visible in cold air."`

### Advanced: Local fine-tuning
Self-host the open weights and fine-tune (LoRA-style) on a character or style for repeatable identity across a project.

---

## Common Workflows

### 1. Cost-efficient dialogue coverage
Generate dialogue beats locally with native audio; iterate freely with no per-clip fee, then finish the hero shot on a premium model if needed.

### 2. Private/offline pipeline
Run entirely on local hardware (24GB+ VRAM) where data cannot leave the building.

---

## Troubleshooting

| Issue | Cause | Solution |
|---|---|---|
| **Out-of-memory / slow** | Under-spec hardware | Meet 24GB VRAM min; lower resolution/duration; use a hosted API. |
| **Weaker fidelity vs frontier** | Open-weights tradeoff | Use for iteration/dialogue; finish hero shots on a frontier model. |
| **Lip-sync off** | Sparse delivery direction | Specify line, emphasis, tone, and mouth/gesture notes. |

---

## Integration

- **API / local**: hosted JSON APIs (prompt, resolution, duration, aspect_ratio, seed, audio) or self-hosted weights.
- **Workflow position**: high-volume/dialogue/iteration and privacy-sensitive pipelines; pair with frontier models for finals.
- **Complementary tools**: image models for first frames; local fine-tuning for identity.
