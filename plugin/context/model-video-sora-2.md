# Sora 2 - Video Generation

> **Currency (Jun 2026):** Current OpenAI video model (Sora 2 / Sora 2 Pro). **API caveat:** the Sora 2 API version stops accepting requests Sep 24 2026 — confirm the active endpoint before integrating. See [`model-currency-2026-06.md`](model-currency-2026-06.md).

---

## Quick Reference

| Attribute | Value |
|---|---|
| **Current Version** | Sora 2 / Sora 2 Pro |
| **Model Type** | Text-to-Video, Image-to-Video |
| **Primary Use** | Multi-shot storytelling, spatial/physics consistency, synced dialogue |
| **Max Resolution** | Pro: 720p, 1024p (1792x1024), true 1080p (1920x1080) |
| **Max Duration** | 10s, 15s, or 25s |
| **Cost** | API ~$0.30/s (720p) to ~$0.50/s (high-res); Batch tier 50% off |
| **Key Features** | Multi-shot sequences, strong world/physics model, native audio + dialogue, Cameos |

---

## Overview

Sora 2 (OpenAI) is the leading model for multi-shot storytelling: it can render an establishing shot, action, detail, and reaction within a single coherent sequence while preserving spatial relationships and plausible physics. Sora 2 Pro adds higher resolution and stronger prompt adherence. Native audio includes synchronized dialogue, and Cameos allow licensed/consented likenesses.

> **Warning:** OpenAI announced the Sora 2 API will stop accepting requests on Sep 24 2026. Check the current endpoint/version before building against it.

---

## When to Use This Model

- **Use Sora 2 for**: multi-shot sequences in one generation, spatial consistency across angles, dialogue scenes.
- **Consider Kling 3.0 for**: native 4K and the most fluid single-shot motion.
- **Consider Veo 3.1 for**: alternative audio-native generation with JSON control.
- **Consider Wan 2.6 for**: open-source/local dialogue at low cost.

---

## Prompting Structure

Sora rewards professional camera language and explicit shot ordering. Describe the sequence as a director would, beat by beat.

**Core Framework**: `Start as [establishing shot], [transition] to [medium], then [transition] to [close-up], [camera technique]. [Technical specs], [continuity note].`

> **Tip:** Be explicit about what you *want* (Sora handles positive direction better than negation). State spatial relationships you need preserved.

---

## Parameters

| Parameter | Type | Description |
|---|---|---|
| `prompt` | String | Sequence description with shot order and camera language. |
| `model` | Enum | `sora-2` or `sora-2-pro`. |
| `resolution` | String | `720p`, `1024p` (1792x1024), or `1080p` (Pro). |
| `duration` | Integer | 10, 15, or 25 seconds. |
| `input_image` | Image | Optional first-frame / reference for image-to-video. |

---

## Techniques

### Basic: Single coherent action
`"A bustling Parisian cafe at golden hour, slow push-in to a woman reading at a corner table. 35mm, warm light, shallow depth of field."`

### Intermediate: Multi-shot in one prompt
`"Establishing wide of a desert highway at dawn; cut to medium tracking alongside a lone motorcyclist; then close-up of gloved hands on the throttle. Anamorphic, consistent left-to-right travel, golden light."`

### Advanced: Dialogue with synced audio
Specify the line, tone, and staging; Sora 2 renders synchronized speech. Keep eyelines and the 180-degree axis consistent across the implied cuts.

---

## Common Workflows

### 1. One-shot sequence
Write a 3-4 beat sequence (establish -> action -> detail -> reaction) in a single prompt; let Sora maintain spatial continuity rather than generating separate clips.

### 2. Dialogue scene
Provide visual staging + the spoken line + tone; review lip-sync and eyeline consistency.

---

## Troubleshooting

| Issue | Cause | Solution |
|---|---|---|
| **Lost spatial continuity** | Too many beats or vague geography | Fewer beats; state positions and travel direction explicitly. |
| **Soft prompt adherence** | Standard tier on a complex shot | Use Sora 2 Pro for precise/high-res work. |
| **Negation ignored** | "not blurry" style phrasing | Describe the positive ("crisp, in focus"). |

---

## Integration

- **API**: per-second billing; `sora-2` / `sora-2-pro`; Batch tier halves the rate. Confirm the endpoint given the Sep 24 2026 API sunset.
- **Workflow position**: best as the multi-shot/storytelling engine; pair with single-shot specialists (Kling) for hero motion.
- **Complementary tools**: image models for first frames; an NLE to assemble beyond the max clip length.
