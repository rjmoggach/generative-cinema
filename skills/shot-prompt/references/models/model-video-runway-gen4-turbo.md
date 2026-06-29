# Runway Gen-4 Turbo - Video Generation

> **Currency (Jun 2026):** Current generation is **Gen-4.5** (Dec 2025 - revamped motion engine, SOTA motion quality/prompt adherence). Workflow below still applies. See [`model-currency-2026-06.md`](model-currency-2026-06.md).

---

## Quick Reference

| Attribute | Value |
|---|---|
| **Current Version** | 4.0 Turbo (April 2025) |
| **Model Type** | Text-to-Video, Image-to-Video |
| **Primary Use** | Rapid iteration, character consistency |
| **Max Resolution** | 720p (1280x720), 4K with upscaler |
| **Max Duration** | 10 seconds |
| **Generation Speed** | ~30 seconds for 10-second clip |
| **API Cost** | 5 credits/sec ($0.05/sec) |
| **Key Feature** | Fast generation with character locking |

---

## Overview

Runway Gen-4 Turbo is a state-of-the-art generative video model designed for speed, consistency, and high-fidelity output. It represents a significant leap from Gen-3 Alpha, focusing on production-ready quality and API accessibility.

Gen-4 Turbo can generate 10-second video clips in as little as 30 seconds, making it ideal for rapid prototyping and iteration. Its core strength lies in maintaining character, object, and location consistency across scenes, driven by a single reference image or a detailed text prompt. The model is trained on a massive multimodal dataset, enabling it to understand and execute complex cinematic language and physical interactions.

> **Note:** Gen-4 Turbo generates at 720p natively. Use Runway's upscaling model for 4K output.

---

## When to Use This Model

Runway Gen-4 Turbo is the best choice when **fast iteration and character consistency** are priorities, especially in production workflows requiring rapid feedback.

- **Use Runway Gen-4 for**: Rapid prototyping, storyboarding, character animation with consistency, VFX element generation, iterative creative development.
- **Consider Seedance Pro for**: Multi-shot narrative sequences with cinematic camera control.
- **Consider Veo 3.1 for**: Projects requiring synchronized audio generation.
- **Consider Luma Ray3 for**: HDR output and advanced physics simulation.

**Runway's Unique Strength**: Fastest generation time (~30s for 10s video) with excellent character locking from single reference images.

---

## Prompting Structure

Gen-4 Turbo prompts should clearly define shot type, subject, action, environment, and cinematic style.

**Core Framework**: `[Shot Type] of [Subject], [Action]. [Scene Description]. [Cinematic Style].`

```
+----------------+---------------------+------------------------+---------------------+
| Shot Type      | Subject & Action    | Scene Description      | Cinematic Style     |
+----------------+---------------------+------------------------+---------------------+
| "Close-up shot | of a detective,     | in a dark, rain-soaked | Cinematic, 35mm     |
| "              | looking up          | alley                  | film, moody lighting|
+----------------+---------------------+------------------------+---------------------+
```

---

## Parameters

Gen-4 Turbo is controlled via API parameters with fine-grained motion control.

| Parameter | Type | Values | Default | Purpose |
|---|---|---|---|---|
| `prompt` | string | Text description | (required) | Describes the desired video content |
| `image_uri` | string | Image URL | null | Source image for I2V or character reference |
| `motion_strength` | integer | 1-10 | 5 | Controls amount of motion (higher = more dynamic) |
| `seed` | integer | Any integer | random | Ensures generation consistency |
| `aspect_ratio` | string | "16:9", "9:16", "1:1" | "16:9" | Output video aspect ratio |
| `duration_seconds` | integer | 5, 10 | 5 | Video length in seconds |

---

## Techniques

### Basic: Text-to-Video with Camera Control

Use explicit camera movement commands for precise cinematography.

- **Prompt**: `"Wide angle shot of a futuristic car driving through a neon-lit city at night, rain on the streets. Camera slowly pushes in. Cinematic, moody lighting, high contrast."`
- **Expected Output**: Video starting wide and gradually moving closer to the car with cinematic motion.

### Intermediate: Character Locking with Reference Image

Maintain character consistency across multiple generations using a reference image.

- **Workflow**: Upload a clear, well-lit portrait of your character as `image_uri`
- **Prompt**: `"The character walks confidently down a busy city street, looking around. Handheld camera follows from behind. Natural lighting, documentary style."`
- **Result**: Your specific character appears consistently, performing the described action.

### Advanced: Style Transfer from Reference

Apply the visual style of a reference image to generated motion.

- **Workflow**: Upload a stylized image (painting, film still, artistic photo) as `image_uri`
- **Prompt**: `"The scene transitions from day to night, figures moving through the space. Maintain the artistic style of the reference image."`
- **Result**: Video with motion that preserves the color palette, texture, and aesthetic of your reference.

---

## Common Workflows

### 1. Rapid Storyboard Iteration

Generate multiple video concepts quickly for director approval.

**Iteration 1** (Test concept):
- **Prompt**: `"Dolly zoom shot of a woman standing in a forest, looking shocked. Dramatic lighting. --seed 12345 --duration 5 --motion 6"`

**Iteration 2** (Refine with same seed):
- **Prompt**: `"Dolly zoom shot of a woman standing in a forest, looking shocked, trees swaying in wind. Dramatic lighting, golden hour. --seed 12345 --duration 5 --motion 6"`

### 2. Character Consistency Across Scenes

Create multiple shots of the same character in different environments.

**Shot 1**:
- Reference: Character portrait as `image_uri`
- **Prompt**: `"The character sits at a cafe, sipping coffee, watching people pass by. Soft morning light."`

**Shot 2**:
- Same reference image
- **Prompt**: `"The character runs through a dark alley at night, looking behind nervously. Handheld camera, streetlight shadows."`

**Result**: Same character across completely different scenes and lighting conditions.

### 3. VFX Element Generation

Create dynamic elements for compositing into live-action footage.

- **Prompt**: `"Intense flames and smoke rising dramatically, high detail, dark background. Slow motion, cinematic lighting."`
- Use green screen or dark background for easy compositing
- Upscale to 4K with Runway's upscaler

---

## Troubleshooting

| Issue | Cause | Solution |
|---|---|---|
| **Jittery or inconsistent motion** | `motion_strength` too high for the described action. | Reduce `motion_strength` to 3-5 for subtle motion, 6-8 for dynamic action. Simplify action description. |
| **Character doesn't match reference** | Reference image unclear or prompt doesn't reference the character. | Use well-lit, clear portrait. In prompt, explicitly say "the character" or "the person from the image." |
| **720p too low for final delivery** | Gen-4 Turbo native resolution is 720p. | Use Runway's `upscale_v1` model in a second API call to upscale to 4K. Plan workflow accordingly. |
| **Generation too slow** | Complex prompts or high motion strength increases processing time. | Simplify prompt, reduce motion strength, or use shorter duration (5s instead of 10s) for faster tests. |
| **Limited to 10 seconds** | API constraint for single-generation duration. | Generate multiple 10s clips and stitch in editing software. Plan shot sequence in advance. |

---

## Integration

- **API Example (Python)**:
    ```python
    import requests

    response = requests.post(
        "https://api.runwayml.com/v1/generate",
        headers={"Authorization": "Bearer YOUR_API_KEY"},
        json={
            "model": "gen4_turbo",
            "prompt": "Cinematic shot of a futuristic car driving through neon-lit city at night, rain on streets. Camera pushes in.",
            "aspect_ratio": "16:9",
            "duration_seconds": 10,
            "motion_strength": 7
        }
    )
    ```

- **Workflow Position**: Ideal for rapid prototyping, previsualization, and iterative development. Use early in workflow to test concepts before committing to slower, higher-res models.
- **Complementary Tools**: Generate keyframes with Midjourney v7 or FLUX.1 Pro for character references. Upscale with Runway's upscaler or Topaz Video AI for final delivery.

---

## References

- Runway. (2025, April 8). *Introducing Runway Gen-4*. https://runwayml.com/research/introducing-runway-gen-4
- Runway. (2025). *API Documentation - Available AI Models*. https://docs.dev.runwayml.com/guides/models/
