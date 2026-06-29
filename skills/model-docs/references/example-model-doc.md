# FLUX.1 Pro - Text-to-Image

> **Currency (Jun 2026):** Superseded by **FLUX.2** (Pro/Flex/Dev/Klein, Nov 2025 - 32B params; stronger photorealism, typography, multi-image reference). Technique below still applies. See [`model-currency-2026-06.md`](model-currency-2026-06.md).

---

## Quick Reference

| Attribute | Value |
|---|---|
| **Current Version** | 1.1 Pro (November 2024) |
| **Model Type** | Text-to-Image |
| **Primary Use** | High-fidelity, fast image generation |
| **Max Resolution** | 4MP (2048x2048) via `ultra` mode |
| **Speed** | ~10 seconds for a 4MP image |
| **Cost** | ~$0.06 per 4MP image |
| **API Endpoint** | `https://api.bfl.ai/v1/flux/text-to-image` |

---

## Overview

FLUX.1 Pro is a state-of-the-art text-to-image model from Black Forest Labs, built on a 12 billion parameter rectified flow transformer. It is designed for speed and high-quality output, making it a strong choice for production workflows. The latest version, 1.1 Pro, introduced significant performance gains and specialized modes for high-resolution and photorealistic generation.

> **Note:** This document focuses on the **Pro** version. For editing and multi-modal tasks, refer to the `flux-kontext.md` documentation.

### Version History

- **v1.1 (Nov 2024)**: Introduced `ultra` (4MP) and `raw` (photorealism) modes. 6x faster than v1.0.
- **v1.0 (Initial Release)**: First production-ready version.

---

## When to Use This Model

FLUX.1 Pro is the ideal choice for projects that require **fast generation of high-resolution, clean, and detailed images**. It excels in commercial art, product visualization, and architectural rendering.

- **Use FLUX.1 Pro for**: Speed, high resolution, and prompt adherence.
- **Consider Midjourney for**: Highly artistic, stylized, or aesthetic-focused results where speed is less critical.
- **Consider Gemini Flash for**: Conversational editing and complex text rendering in images.

---

## Prompting Structure

FLUX responds best to clear, descriptive sentences. The model prioritizes concepts at the beginning of the prompt.

**Core Framework**: `[Style & Medium] of a [Subject] [Action], [Context & Environment], [Technical Details]`

```
+----------------------+--------------------------+-----------------------+
| Style & Medium       | Subject & Action         | Context & Details     |
+----------------------+--------------------------+-----------------------+
| "Cinematic photo of" | "a stoic Roman general  | "at dawn, 85mm lens,   |
|                      | inspecting his troops"  | shallow depth of field" |
+----------------------+--------------------------+-----------------------+
```

---

## Parameters

Unlike other models, FLUX.1 Pro is primarily controlled via API-level settings rather than `--` parameters in the prompt itself.

| Parameter | Type | Description |
|---|---|---|
| `prompt` | String | The descriptive text prompt. |
| `mode` | Enum | Sets the generation mode. Options: `default`, `ultra`, `raw`. |
| `resolution` | String | Defines the output size (e.g., `1024x1024`, `2048x2048`). Must be compatible with the selected `mode`. |
| `num_outputs` | Integer | The number of images to generate. |

---

## Techniques

### Basic: Simple Scene Construction

Start with a clear subject and action. This is the foundation of every good prompt.

- **Good**: `"A red fox sitting in tall grass."`
- **Better**: `"Wildlife documentary photo of a red fox sitting in tall, sun-drenched grass at dawn."`

### Intermediate: Composition and Style

Add camera and style keywords to gain control over the final image. Place them early in the prompt for maximum influence.

- **Prompt**: `"Van Gogh style painting of a modern city street, with swirling brushstrokes and vibrant colors."`
- **Expected Output**: An image that strongly mimics Van Gogh's aesthetic, applied to a contemporary subject.

### Advanced: Photorealism with Technical Terms

For maximum realism, use professional photography terms. This guides the model to produce results that look like they were captured with a real camera.

- **Before**: `"Photo of a woman."`
- **After**: `"Professional headshot of a business executive, clean white background, studio lighting, 85mm lens, f/1.4, shallow depth of field."`

---

## Common Workflows

### 1. Architectural Visualization

Use `ultra` mode to generate high-resolution architectural renders. Be specific about materials, lighting, and time of day.

- **Prompt**: `"Ultra-realistic architectural render of a modern glass house in a forest, evening light filtering through the trees, interior lights on, 4K, photorealistic."`

### 2. Product Mockups

Use `raw` mode for clean, realistic product shots. Specify the background and lighting setup.

- **Prompt**: `"Professional product shot of a sleek black smartphone on a white background, studio softbox lighting, raw mode."`

---

## Troubleshooting

| Issue | Cause | Solution |
|---|---|---|
| **Vague or Generic Output** | The prompt lacks specific, descriptive language. | Replace general terms with precise descriptors (e.g., instead of "a car", use "a vintage 1967 red convertible"). |
| **Unwanted Elements Appear** | The model is guided by positive instructions, not exclusions. | Rephrase the prompt to describe what you want to see, rather than what you want to avoid. Use positive framing. |
| **Incorrect Style** | The style keyword is placed too late in the prompt. | Front-load the most critical style or artistic reference to give it higher priority in the prompt structure. |

---

## Integration

- **API Example (Python)**:
    ```python
    import requests

    response = requests.post(
        "https://api.bfl.ai/v1/flux/text-to-image",
        headers={"Authorization": "Bearer YOUR_API_KEY"},
        json={
            "prompt": "A majestic lion on the Serengeti plains, golden hour lighting, photorealistic, 8k",
            "mode": "ultra",
            "resolution": "2048x2048"
        }
    )
    ```
- **Workflow Position**: Ideal for final asset generation due to its speed and high resolution. Use it after initial concepts have been explored with faster, cheaper models if necessary.
- **Complementary Tools**: Use `flux-kontext.md` for iterative editing and refinement of images generated with FLUX.1 Pro.
