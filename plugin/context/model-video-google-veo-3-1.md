# Google Veo 3.1 - Video Generation

> **Currency (Jun 2026):** **Veo 3.1 remains current** (family: 3.1 / 3.1 Fast / 3.1 Lite). No Veo 4 yet - this doc is largely accurate. See [`model-currency-2026-06.md`](model-currency-2026-06.md).

---

## Quick Reference

| Attribute | Value |
|---|---|
| **Current Version** | 3.1 (October 2025) |
| **Model Type** | Text-to-Video, Image-to-Video |
| **Primary Use** | High-fidelity video with synchronized audio |
| **Max Resolution** | 1080p |
| **Max Duration** | 8 seconds (API), 60+ seconds (Flow with Extend) |
| **Framerate** | 24 FPS |
| **API Endpoint** | `veo-3.1-generate-preview` (Vertex AI) |
| **Key Feature** | Native audio generation (dialogue, SFX, music) |

---

## Overview

Google Veo 3.1 is a state-of-the-art video generation model that excels in creating realistic, high-fidelity video with synchronized, AI-generated audio. It builds upon its predecessor, Veo 3, with significantly stronger prompt adherence, enhanced realism, and richer audio capabilities, including dialogue, sound effects, and ambient noise.

Veo 3.1 is designed for professional and enterprise workflows, offering granular control over scene composition and narrative flow. It is available through Google's Flow, the Gemini API, and Vertex AI, making it accessible for a wide range of applications from creative experimentation to large-scale production.

> **Note:** Veo 3.1 is currently in preview status. API limits and capabilities may evolve.

---

## When to Use This Model

Veo 3.1 is the ideal choice when **synchronized audio and video are required in a single generation**. Its native audio capabilities make it unique among video generation models.

- **Use Veo 3.1 for**: Projects requiring dialogue, sound effects, or ambient audio synchronized with video; narrative storytelling; marketing videos with voiceovers.
- **Consider Seedance Pro for**: Multi-shot cinematic sequences without audio requirements.
- **Consider Runway Gen-4 for**: Faster iteration and character consistency workflows.
- **Consider Luma Ray3 for**: HDR output and advanced physics simulation.

**Veo 3.1's Unique Strength**: Only model that natively generates audio (dialogue, SFX, music) synchronized with video content.

---

## Prompting Structure

Veo 3.1 prompts should be highly descriptive and can include explicit audio cues. The model understands complex narrative and cinematic language.

**Core Framework**: `[Scene Description]. [Action]. [Audio Description]. [Cinematic Style].`

```
+---------------------+--------------------+---------------------+--------------------+
| Scene Description   | Action             | Audio Description   | Cinematic Style    |
+---------------------+--------------------+---------------------+--------------------+
| "A robot walks in   | "stopping to look  | "Birds chirping,    | "Cinematic wide    |
| a lush forest"      | at a stream"       | water flowing,      | angle, golden hour |
|                     |                    | dialogue: 'Hello'"  | lighting"          |
+---------------------+--------------------+---------------------+--------------------+
```

---

## Parameters

Veo 3.1 is controlled via API parameters. Audio generation is enabled by default.

| Parameter | Type | Values | Default | Purpose |
|---|---|---|---|---|
| `prompt` | string | Text description | (required) | Describes video and audio content |
| `reference_images` | array | Image URLs | [] | "Ingredients" for style/character consistency |
| `start_frame` | string | Image URL | null | Starting frame for Frames-to-Video |
| `end_frame` | string | Image URL | null | Ending frame for Frames-to-Video |
| `duration_seconds` | integer | 4, 6, 8 | 8 | Video length in seconds |
| `resolution` | string | "720p", "1080p" | "1080p" | Output resolution |
| `include_audio` | boolean | true, false | true | Generate synchronized audio |

---

## Techniques

### Basic: Audio-Synchronized Video

Explicitly describe both visual and audio elements in your prompt for best results.

- **Prompt**: `"A woman stands in a quiet library. She whispers, 'It's so peaceful here.' The sound of pages turning in the background. Soft, warm lighting."`
- **Expected Output**: Video with synchronized whispered dialogue and ambient page-turning sounds.

### Intermediate: Frames-to-Video Narrative Control

Use start and end frames to create precise narrative transitions.

- **Workflow**: Generate two keyframes (opening and closing shots) in Midjourney or FLUX
- **Prompt**: `"Transition from the first frame to the second frame. A detective walks from the dark alley into the bright street. Footsteps echo, city ambience grows louder. Film noir style."`
- **Result**: Smooth transition between your two frames with appropriate audio.

### Advanced: Multi-Image Character Consistency

Provide multiple reference images of the same character to maintain consistency across generations.

- **Workflow**: Upload 3-4 images of your character in different poses/lighting
- **Prompt**: `"The character from the reference images runs through a rainy street, shouting 'Wait!' Splashing water, heavy rain sounds. Handheld camera, dramatic lighting."`
- **Result**: Your character appears consistently, with synchronized dialogue and sound effects.

---

## Common Workflows

### 1. Creating Dialogue-Driven Narrative Clips

Leverage Veo 3.1's unique audio generation for character-driven stories.

- **Prompt**: `"Close-up of a young woman's face, tears streaming down. She says, 'I can't do this anymore.' Soft piano music plays in the background. Cinematic, shallow depth of field, 85mm lens."`

### 2. Extended Sequences with Scene Extension

Create longer videos by using the Extend feature to chain 8-second clips.

**Clip 1** (8s):
- **Prompt**: `"A spaceship approaches a distant planet. Engine hum, radio static. Wide shot, space cinematography."`

**Clip 2** (Extend from Clip 1):
- **Prompt**: `"The spaceship enters the planet's atmosphere. Turbulence sounds, alarms beeping. Camera follows the ship's descent."`

### 3. Music Video Generation

Generate visuals synchronized with specific musical styles or moods.

- **Prompt**: `"A dancer spins in a neon-lit room, movements flowing with an upbeat electronic music track. Bass drops, synthesizers. Dynamic camera movements, vibrant colors."`

---

## Troubleshooting

| Issue | Cause | Solution |
|---|---|---|
| **Audio has artifacts or distortion** | Audio description too complex or conflicting with visual content. | Simplify audio cues. Be specific (e.g., "soft piano" instead of "orchestral symphony with complex harmonies"). |
| **Dialogue not generated** | Prompt lacks explicit dialogue cues. | Use quotation marks for dialogue: `She says, "Hello there."` Place dialogue cues early in the prompt. |
| **Limited to 8 seconds** | API constraint for single-generation duration. | Use "Extend" feature in Google Flow to chain clips, or stitch multiple 8s clips in post-production. |
| **Character inconsistency** | Single reference image insufficient. | Provide 3-4 reference images of the same character in `reference_images` array. Be detailed in character description. |
| **Preview API limitations** | Veo 3.1 is in preview status. | Some prompts may not be supported. Check official documentation for current capabilities and limits. |

---

## Integration

- **API Example (Python)**:
    ```python
    import vertexai
    from vertexai.preview.vision_models import VideoGenerationModel

    vertexai.init(project="YOUR_PROJECT_ID", location="us-central1")

    model = VideoGenerationModel.from_pretrained("veo-3.1-generate-preview")

    response = model.generate_videos(
        prompt="A robot walks in a lush forest, birds chirping, stream flowing nearby. Cinematic, wide-angle shot.",
        duration_seconds=8,
        resolution="1080p",
        include_audio=True
    )
    ```

- **Workflow Position**: Ideal for final asset generation when synchronized audio is required. Use after concept development in faster models like Seedance or Runway for previsualization.
- **Complementary Tools**: Generate keyframes with Midjourney v7 or FLUX.1 Pro, then animate with Veo 3.1. Use reference images for character consistency.

---

## References

- Google. (2025, October 15). *Introducing Veo 3.1 and advanced capabilities in Flow*. https://blog.google/technology/ai/veo-updates-flow/
- Google Cloud. (2025). *Veo 3.1 Documentation*. https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/veo/3-1-generate
