# Kling 3.0 - Video Generation

> **Currency (Jun 2026):** Current generation, released by Kuaishou Feb 5 2026. The only major model with native 4K output. See [`model-currency-2026-06.md`](model-currency-2026-06.md).

---

## Quick Reference

| Attribute | Value |
|---|---|
| **Current Version** | Kling 3.0 / 3.0 Pro (Feb 2026) |
| **Model Type** | Text-to-Video, Image-to-Video |
| **Primary Use** | Fluid character/athletic motion; native 4K output |
| **Max Resolution** | 4K (3.0); Pro tier 1080p, up to 48 fps |
| **Max Duration** | 5-10s per clip; extendable up to ~3 min |
| **Cost** | ~$0.075/s (3.0) via API; ~$0.70 for a 5s 1080p clip with audio |
| **Key Features** | Native 4K, Motion Control, Motion Brush, optional built-in audio |

---

## Overview

Kling 3.0 (Kuaishou) is a high-fidelity video model known for the most fluid human and athletic motion in the field and for being the only major 2026 model with native 4K output. It supports text-to-video and image-to-video, clip extension up to roughly three minutes, and directorial controls that set it apart: Motion Control and Motion Brush.

> **Tip:** Reach for Kling when believable *movement* (sports, dance, action, physical performance) is the priority.

### Version note

Kling 3.0 is current as of June 2026; the lineup also includes Kling O1 and a dedicated Motion Control tier. Verify per-tier limits against the currency file.

---

## When to Use This Model

- **Use Kling 3.0 for**: athletic/character motion fidelity, native 4K finals, and shots where you need to direct motion precisely.
- **Consider Sora 2 for**: multi-shot storytelling and spatial consistency across angles.
- **Consider Runway Gen-4.5 for**: fastest production UI and character lock across coverage.
- **Consider Wan 2.6 for**: open-source/local or dialogue with native audio at low cost.

---

## Prompting Structure

Kling responds to a detailed visual description followed by camera and motion direction, then quality markers.

**Core Framework**: `[Subject + detailed appearance] [action/motion], [camera movement], [lighting/atmosphere], [style], [quality markers]`

> **Tip:** Match clip duration to the action. If the move takes 5s, request 5s, not 10 — padding invites loops and drift.

---

## Parameters

| Parameter | Type | Description |
|---|---|---|
| `prompt` | String | Visual + motion description. |
| `mode` | Enum | `standard` or `pro` (pro = higher fidelity/resolution). |
| `resolution` | String | Up to `4k` on 3.0; `1080p` on Pro. |
| `duration` | Integer | 5 or 10 seconds (extendable). |
| `motion_brush` | Mask/Path | Draw a motion path the model follows. |
| `motion_control` | Video ref | Extract a motion pattern from a reference clip and apply to a new subject. |
| `audio` | Bool | Optional built-in audio generation. |

---

## Techniques

### Basic: Clear subject and motion
- **Good**: `"A sprinter exploding out of the blocks on a wet track."`
- **Better**: `"Low-angle tracking shot of a sprinter exploding out of the blocks on a rain-slicked track, water spraying, muscles taut, stadium lights flaring, slow-motion, cinematic."`

### Intermediate: Motion Brush for directed movement
Draw the path of a specific element (a falling leaf, a turning head) so motion follows your intent rather than the model's guess.

### Advanced: Motion Control transfer
Upload a reference clip of a movement (a dance, a fight beat) and apply that motion pattern to a different character or creature for repeatable, art-directed action.

---

## Common Workflows

### 1. Hero action shot at 4K
Generate a strong keyframe (FLUX.2 / Midjourney), drive image-to-video in Pro/4K, direct the key movement with Motion Brush.

### 2. Repeatable choreography
Capture or generate one motion reference, then use Motion Control to apply it across multiple characters for a consistent sequence.

---

## Troubleshooting

| Issue | Cause | Solution |
|---|---|---|
| **Looping or drift in long clips** | Duration exceeds the action | Shorten duration; extend only if needed. |
| **Motion ignores intent** | Under-specified movement | Use Motion Brush or Motion Control rather than text alone. |
| **Identity drift** | Long generation, no anchor | Drive from a reference image; hold appearance cues. |

---

## Integration

- **API**: per-second billing (~$0.075/s for 3.0); JSON request with prompt, mode, resolution, duration, optional motion controls and audio.
- **Workflow position**: motion-heavy coverage and 4K hero shots; feed keyframes from an image model.
- **Complementary tools**: image models for keyframes; an editor for cutting Kling coverage into a sequence.
