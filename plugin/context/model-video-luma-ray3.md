# Luma Ray3 - Video Generation

> **Currency (Jun 2026):** Current generation is **Ray3.2** (Jun 2026 - full API, 16 keyframes/clip, HDR + 16-bit EXR export). Technique below still applies. See [`model-currency-2026-06.md`](model-currency-2026-06.md).

---

## Quick Reference

| Attribute | Value |
|---|---|
| **Current Version** | Ray 3 (September 2025) |
| **Model Type** | Text-to-Video, Image-to-Video |
| **Primary Use** | HDR video generation, advanced physics |
| **Max Resolution** | 4K (with HiFi upscale) |
| **Max Duration** | 10 seconds |
| **Generation Speed** | 5x faster in Draft Mode |
| **API Status** | Ray 2 only (Ray 3 web UI exclusive) |
| **Key Feature** | 16-bit HDR, reasoning engine, Draft Mode |

---

## Overview

Luma Dream Machine Ray3 is the world's first "reasoning" video model, capable of understanding complex user intent and generating video with a high degree of physical and narrative coherence.

Ray3 introduces several groundbreaking features, including native 16-bit HDR generation, a rapid "Draft Mode" for iteration, and "Visual Annotation" for precise control. It is designed for professional and artistic workflows, enabling the creation of studio-grade video content directly from text and images.

> **Important:** As of November 2025, Ray3 features (HDR, Draft Mode, reasoning) are only available through the Luma web interface. The API currently supports Ray 2 models.

---

## When to Use This Model

Luma Ray3 is the best choice when **HDR output for professional color grading** or **advanced physics simulation** are required.

- **Use Luma Ray3 for**: Professional VFX workflows requiring HDR/EXR output, rapid prototyping with Draft Mode, complex physics simulations, artistic/surreal content with precise control.
- **Consider Seedance Pro for**: Multi-shot narrative sequences with standard dynamic range.
- **Consider Runway Gen-4 for**: Faster API-based iteration with character consistency.
- **Consider Veo 3.1 for**: Synchronized audio generation.

**Ray3's Unique Strengths**: Only model with native 16-bit HDR output and reasoning engine for complex physics/interactions. Draft Mode offers 5x faster iteration.

---

## Prompting Structure

Ray3 prompts benefit from descriptive, narrative language. The model's reasoning capabilities allow for complex physics and interaction descriptions.

**Core Framework**: `[Subject] [Action] in [Scene]. [Detailed Physics/Interaction]. [Cinematic Style] in [HDR/SDR].`

```
+-------------------+---------------------+------------------------+--------------------+
| Subject & Action  | Scene & Physics     | Interaction Details    | Cinematic/HDR      |
+-------------------+---------------------+------------------------+--------------------+
| "A heavy ball     | thrown forcefully   | "The ball hits a       | "Cinematic slow    |
| "                 | at a plaster wall"  | plaster wall, causing  | motion, 16-bit HDR"|
|                   |                     | cracks and crumbling"  |                    |
+-------------------+---------------------+------------------------+--------------------+
```

---

## Parameters

Ray3 advanced features are currently web UI only. API supports Ray 2 with basic parameters.

| Parameter | Type | Values | Default | Purpose |
|---|---|---|---|---|
| `prompt` | string | Text description | (required) | Describes desired video content |
| `image_url` | string | Image URL | null | Source image for I2V |
| `model` | string | "ray-2" | "ray-2" | Model version (Ray 3 not in API yet) |
| `duration` | string | "5s", "10s" | "5s" | Video length |
| `resolution` | string | "720p", "1080p" | "720p" | Output resolution |
| `loop` | boolean | true, false | false | Create seamless loop |
| `draft` | boolean | true, false | false | Use Draft Mode (web UI only) |

**Web UI Exclusive Features**:
- HDR output (16-bit EXR)
- HiFi upscaling to 4K
- Visual Annotation tool
- Extend and advanced keyframing

---

## Techniques

### Basic: Physics-Based Reasoning

Describe physical interactions in detail to leverage the reasoning engine.

- **Generic**: `"A ball hits a wall."`
- **Better**: `"A heavy metal ball is thrown forcefully at a thin plaster wall. The ball impacts the wall, causing deep cracks to spread from the point of impact. Small pieces of plaster crumble and fall to the ground. Slow motion, cinematic lighting."`
- **Result**: Realistic physics simulation with appropriate material behavior.

### Intermediate: Draft-to-HiFi Workflow

Use Draft Mode for fast iteration, then upscale the best result.

**Step 1** - Generate drafts (web UI, Draft Mode enabled):
- Generate 5-10 variations quickly
- Each takes ~20 seconds instead of ~2 minutes
- Lower cost for experimentation

**Step 2** - Select best draft:
- Choose the version closest to your vision

**Step 3** - HiFi upscale:
- Upscale selected draft to 4K HDR
- Export as 16-bit EXR for VFX pipeline

### Advanced: Visual Annotation for Precise Control

For complex spatial instructions, use the annotation tool instead of text.

- **Workflow** (web UI only):
  1. Upload reference image
  2. Use annotation tool to draw motion paths
  3. Indicate where objects should move or appear
  4. Generate with visual guidance

- **Use case**: `"Character jumps from point A to point B"` - draw arc between points instead of describing in text

---

## Common Workflows

### 1. Professional VFX Element Generation

Create HDR elements for compositing in professional VFX workflows.

- **Prompt**: `"Intense flames and volumetric smoke rising dramatically against dark background. Complex particle motion, realistic fire physics. 16-bit HDR for professional color grading."`
- **Output**: Generate in HDR, export as EXR
- **Use in**: Nuke, After Effects, Flame for seamless compositing

### 2. Rapid Concept Exploration with Draft Mode

Quickly iterate on creative ideas before committing to high-res generation.

**Draft iterations** (5-10 variations, ~20s each):
- Variation 1: `"Surreal landscape with floating islands"`
- Variation 2: `"Surreal landscape with floating islands, waterfalls flowing upward"`
- Variation 3: `"Surreal landscape with floating islands, aurora in sky, dream-like atmosphere"`

**HiFi final**: Select best draft, upscale to 4K HDR

### 3. Physics-Heavy Action Sequences

Leverage reasoning engine for complex physical interactions.

- **Prompt**: `"A glass bottle falls from a table, tumbling through the air. It hits a hard tile floor at an angle, shattering into hundreds of pieces that scatter outward. Liquid splashes and spreads. Slow motion, sharp detail, cinematic lighting. 16-bit HDR."`
- **Result**: Realistic glass break physics with proper momentum and material behavior.

---

## Troubleshooting

| Issue | Cause | Solution |
|---|---|---|
| **Can't access HDR/Draft Mode via API** | Ray3 features not yet in public API. | Use Luma web interface for Ray3 features. API limited to Ray 2 capabilities. Check documentation for API updates. |
| **Physics don't look realistic** | Prompt lacks specific physical details. | Describe material properties ("heavy metal ball", "thin plaster"), forces ("thrown forcefully"), and expected results ("cracks spread", "pieces crumble"). |
| **Anatomy issues with characters** | Complex character poses challenging for all models. | Use reference images, Visual Annotation to guide character placement, simpler poses, or generate in parts and composite. |
| **Cost too high for exploration** | Using HiFi 4K HDR for all iterations. | Use Draft Mode for exploration (5x faster, lower cost), only upscale to HiFi for final selected versions. |
| **Need longer than 10 seconds** | Single-generation limit. | Use Extend feature (web UI) to chain clips, or generate multiple 10s clips and stitch in editing software. |

---

## Integration

- **API Example (Python)** - Ray 2 only:
    ```python
    import requests

    response = requests.post(
        "https://api.lumalabs.ai/dream-machine/v1/generations",
        headers={"Authorization": "Bearer YOUR_API_KEY"},
        json={
            "model": "ray-2",
            "prompt": "A majestic whale breaches the ocean surface in slow motion, water droplets catching sunlight. Cinematic, nature documentary style.",
            "duration": "5s",
            "resolution": "1080p"
        }
    )
    ```

> **Note:** For Ray3 features (HDR, Draft Mode, reasoning), use the Luma web interface at lumalabs.ai

- **Workflow Position**: Ideal for final professional-grade assets requiring HDR output. Use Draft Mode early for concept exploration, then HiFi upscale selected versions.
- **Complementary Tools**: Generate keyframes with Midjourney v7 or FLUX.1 Pro. Export HDR/EXR for compositing in Nuke, After Effects, or Flame.

---

## References

- Luma AI. (2025, September 18). *AI Video Generation with Ray 3 & Dream Machine*. https://lumalabs.ai/ray
- Luma AI. (2025). *Dream Machine API Documentation*. https://docs.lumalabs.ai/docs/video-generation
- Luma AI. (2025). *Dream Machine Pricing*. https://lumalabs.ai/pricing
