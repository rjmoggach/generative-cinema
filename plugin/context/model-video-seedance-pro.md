# Seedance Pro - Video Generation

> **Currency (Jun 2026):** Current generation is **Seedance 2.5** (announced Jun 2026 - 30s single-pass generation). Multi-shot technique below still applies. See [`model-currency-2026-06.md`](model-currency-2026-06.md).

---

## Quick Reference

| Attribute | Value |
|---|---|
| **Current Version** | 2.5 (see currency note above); 2.x grammar throughout |
| **Model Type** | Text-to-Video, Image-to-Video, **Video-to-Video** |
| **Primary Use** | Cinematic multi-shot narrative; footage transformation / VFX |
| **Max Resolution** | 1080p |
| **Max Duration** | 30s single-pass (2.5); 4–15s typical for v2v transforms |
| **Key Features** | Multi-shot sequences, character consistency, complex camera moves, video-to-video transformation |

---

## Overview

Seedance 1.0 Pro is a state-of-the-art video generation model from ByteDance. It excels at creating high-definition (1080p) videos from both text and image prompts. Its key strengths are its advanced semantic understanding, strong prompt adherence, and a unique ability to generate coherent, multi-shot narrative sequences. The model produces videos with smooth motion and can adapt to a wide variety of cinematic and artistic styles.

> **Warning:** Seedance does **not** support negative prompts. Your prompt must focus on describing what you want to see.

---

## When to Use This Model

Seedance is the premier choice for creating **short, cinematic, narrative-driven video clips**. It is particularly powerful for generating sequences with multiple shots or complex camera movements.

- **Use Seedance for**: Storyboarding, creating short film clips, animating characters with consistent identity, and producing dynamic, multi-shot sequences.
- **Consider other models for**: Generating videos longer than 10 seconds, or for simple, single-shot animations where narrative is not a priority.

---

## Prompting Structure

Seedance prompts are built around **motion**. The core of the prompt should describe the subject, its actions, and the camera work.

**Core Framework**: `[Subject] [Movement/Action] in [Scene], [Camera/Lens], [Style]`

```
+----------------+---------------------+----------------+----------------------+
| Subject        | Movement/Action     | Scene/Style    | Camera               |
+----------------+---------------------+----------------+----------------------+
| "A lone astronaut" | "walks vigorously"  | "on Mars,     | "the camera slowly    |
|                |                     | cinematic style" | pushes in"           |
+----------------+---------------------+----------------+----------------------+
```

> **Tip:** Always include adverbs of degree (e.g., `quickly`, `slowly`, `vigorously`) to control the intensity of the motion. The model does not infer this.

---

## Parameters

Parameters are appended to the end of the text prompt using `--` syntax.

| Parameter | Syntax | Values | Default | Purpose |
|---|---|---|---|---|
| Resolution | `--rs` | `480p`, `1080p` | Varies | Sets the video resolution. |
| Duration | `--dur` | `5`, `10` | Varies | Sets the video length in seconds. |
| Fixed Camera | `--cf` | `true`, `false` | `false` | Locks camera position. Set to `false` for moving shots. |

---

## Techniques

### Basic: Simple Motion

Start with a clear subject and a single, well-defined action.

- **Good**: `"A car driving down a street."`
- **Better**: `"A vintage red convertible driving quickly down a rain-slicked city street at night."`

### Intermediate: Multi-Action Sequences

Describe a series of continuous actions for a single subject.

- **Prompt**: `"A woman picks up a glass from the table, takes a sip, and then places it back down, all in one smooth motion."`

### Advanced: Multi-Shot Narrative

This is Seedance's standout feature. Use the phrase **"shot switch"** or **"cut to"** to explicitly signal a transition between scenes. The model will maintain character and style consistency.

- **Prompt**: `"Close-up of a detective's determined face, cinematic lighting. Shot switch. A low-angle shot of him entering a dark, abandoned factory. Shot switch. The camera follows him as he discovers a single, muddy footprint on the concrete floor."`

---

## Video-to-Video (footage transformation)

Seedance 2.x can take a clip the user already has as the **base** and transform it —
add a VFX element, swap the environment, drop in a photoreal creature, sync a camera
move to a spoken line. For the model-agnostic craft (preserve-then-change, lighting
integration, timed moves, duration budget), see
[`guide-footage-transformation.md`](guide-footage-transformation.md). The
Seedance-specific *syntax* is below.

### Input declarations

The source clip is the **base, not a style reference**. Declare it on one line:

```
@source: Original <clip name> — <who/what is in it>. Preserve <identity, face,
wardrobe, performance, framing, camera and motion> exactly; <the one thing to change>.
```

When a transformation needs a real texture the model keeps faking (an animal's fur, a
specific material), add a **second input** as a texture-only reference:

```
@creature: Reference photo of a real <animal> — <fur / face / anatomy notes>.
Appearance and texture reference only; ignore the photo's background and lighting,
do not use it for the environment.
```

### Specs line

One compact line, always carrying the source-matching constraints:

```
Photoreal. <aspect, default 16:9>. <duration — match the source clip>s. <look/grade>.
NON-IP — generic <creature/design>, not based on any brand or character.
<SFX only | SFX and source dialogue only>.
```

- **Match the source runtime by default.** Extend only when a payoff needs room, and say why.
- **NON-IP guardrail** belongs in the specs line whenever a creature, armor, vehicle, or
  character design is added — generic, never a branded character. It also tends to
  generate more reliably than a trademarked design.
- **Audio:** `SFX only` for added effects; `SFX and source dialogue only` when the source
  talk track must survive (e.g. a zoom synced to a spoken line).

### Scene action + SFX

Describe **continuous camera movement** (the source is one take), not cuts. Lead with the
shot/lens and "same framing as the source," then the preserved performance, then the
transformation, then any timed move; close with the lock-down clause. End with a specific,
ordered, **behavioral** SFX line (not "fire" but "a soft whoomph as it catches, then a low
steady flame roar and crackle, occasional ember pop").

### Seedance 2.x input limits

Images ≤ 9; videos ≤ 3 items, total ≤ 15s; audio ≤ 3 MP3s, total ≤ 15s; total mixed
inputs ≤ 12; generation duration 4–15s. A source clip plus a texture-reference photo fits
easily. If a request needs more inputs than allowed, flag it and say what to prioritize.

> **No negative prompts.** As with all Seedance work, describe what you want, not what to avoid.

---

## Common Workflows

### 1. Animating a Still Image (Image-to-Video)

Provide a starting image and describe the motion that should begin from that frame.

- **Workflow**: Generate a high-quality character portrait in Midjourney or Seedream.
- **Prompt**: `(With the portrait as input) "The person in the image slowly turns their head to the left and smiles, subtle motion."`

### 2. Creating a Cinematic Long Take

Combine multiple camera movements to create a single, unbroken shot.

- **Prompt**: `"The camera starts on a close-up of a key in a door, then pulls back to reveal a man opening it, follows him into a room, and finally pans across the room to a window showing a cityscape at night."`

---

## Troubleshooting

| Issue | Cause | Solution |
|---|---|---|
| **Motion is static or weak** | The prompt lacks adverbs of degree or strong action verbs. | Add adverbs like `quickly`, `vigorously`, `gently` to describe the motion. Use dynamic verbs. |
| **Camera is not moving** | The `--cf` parameter was set to `true`, or no camera movement was described. | Ensure `--cf` is `false` and include explicit camera movement commands in the prompt (e.g., `pan left`, `zoom in`). |
| **I2V prompt fails** | The text prompt contradicts the content of the source image. | Ensure the prompt describes an action that logically follows from the image. Do not try to change the subject or background in an I2V prompt. |

---

## Integration

- **API Example**: API access is typically provided through platforms like BytePlus. The specific implementation will vary.
- **Workflow Position**: Seedance is a powerful tool for generating final video clips for creative projects, social media, and storyboarding.
- **Complementary Tools**: Use a high-quality image generation model like **Seedream 4.0** or **Midjourney** to create a starting frame for I2V generation, giving you more control over the initial scene composition.
