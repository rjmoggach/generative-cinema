# Midjourney - v7

> **Currency (Jun 2026):** Current default is **v8.1** (Jun 2026 - ~4-5x faster, native HD 2K, Draft mode, `--preview`). Parameters below still apply. See [`model-currency-2026-06.md`](model-currency-2026-06.md).

---

## Quick Reference

| Attribute | Value |
|---|---|
| **Current Version** | 7.0 (2025) |
| **Model Type** | Text-to-Image, Image-to-Image |
| **Primary Use** | Artistic and aesthetic-focused image generation |
| **Max Resolution** | High-resolution via upscalers (e.g., 4096x4096) |
| **Interface** | Discord, Web |
| **Key Features** | `–-stylize`, `–-chaos`, Omni Reference, Draft Mode |

---

## Overview

Midjourney is a premier AI image generation model known for its highly artistic and aesthetically refined outputs. It operates primarily through a Discord-based interface, using a parameter-driven approach to give users precise control over the generation process. Version 7 introduced significant improvements in prompt adherence and user workflow, including powerful tools for maintaining character consistency (`Omni Reference`) and rapid, conversational iteration (`Draft Mode`).

> **Note:** Midjourney excels at creating beautiful, often surprising results. It is less suited for tasks requiring absolute photorealism or precise control over every pixel.

---

## When to Use This Model

Midjourney is the best choice when the **artistic style and aesthetic quality** of the image are the top priorities. It is perfect for concept art, mood boards, and creating unique, stylized visuals.

- **Use Midjourney for**: Concept art, character design, abstract visuals, and when you want the AI to have some creative input.
- **Consider FLUX.1 Pro for**: Fast, high-resolution, and clean commercial images.
- **Consider Seedream 4.0 for**: Maximum resolution (4K native) and complex, knowledge-based illustrations.

---

## Prompting Structure

Midjourney prompts combine descriptive text with parameters. The structure is flexible, but this is a proven framework.

**Core Framework**: `[Image Prompts] [Text Prompt] [Parameters]`

```
+----------------+--------------------------------+--------------------------+
| Image Prompt   | Text Prompt                    | Parameters               |
+----------------+--------------------------------+--------------------------+
| [URL of image] | "A portrait of a woman, in the  | "--ar 4:5 --s 750 --v 7" |
|                | style of Art Nouveau, with a   |                          |
|                | muted color palette"            |                          |
+----------------+--------------------------------+--------------------------+
```

---

## Parameters

Parameters are added to the end of a prompt and always begin with `--`.

| Parameter | Syntax | Values | Default | Purpose |
|---|---|---|---|---|
| Aspect Ratio | `--ar` | `X:Y` | `1:1` | Sets image dimensions. |
| Stylize | `--s` | 0-1000 | 100 | Controls artistic interpretation. |
| Chaos | `--c` | 0-100 | 0 | Varies the initial image grid. |
| Negative Prompt | `--no` | `[text]` | None | Excludes specified elements. |
| Image Weight | `--iw` | 0-3 | 1 | Controls influence of an image prompt. |
| Tile | `--tile` | Flag | Creates a seamless, repeatable pattern. |
| Version | `--v` | 1-7 | 7 | Selects the model version. |
| Niji | `--niji` | Flag | Activates the anime/illustration model. |

---

## Techniques

### Basic: Controlling Style

The `--stylize` (or `--s`) parameter is your primary tool for controlling how artistic the output is. Low values are more literal; high values are more creative.

- **Low Stylize**: `A photo of a cat --s 50` (Will look very much like a standard photo).
- **High Stylize**: `A photo of a cat --s 900` (Will be a highly artistic interpretation of a cat).

### Intermediate: Character Consistency with Omni Reference

To maintain a character across multiple images, use a clear reference image and the `Omni Reference` feature.

- **Workflow**: Use an image URL as the first part of your prompt. Midjourney v7 will interpret this as an Omni Reference.
- **Prompt**: `[URL of character image] A portrait of the same person, now wearing a space helmet, cinematic lighting.`

### Advanced: Prompt Engineering with Weights

Use `::` to separate concepts in your prompt and assign them different weights. This gives you fine-grained control over the composition.

- **Prompt**: `space ship::2 interior::1` (The space ship is twice as important as the interior).
- **Prompt**: `dog:: cat::-1` (This will try to show a dog and remove any cat-like features).

---

## Common Workflows

### 1. Concept Art Exploration

Use `--chaos` to generate a wide variety of initial ideas from a single prompt.

- **Prompt**: `A futuristic cityscape, utopian architecture, flying vehicles, lush greenery --c 50`
- This will produce four initial images that are significantly different from each other, allowing for rapid exploration.

### 2. Creating Seamless Textures

Use the `--tile` parameter to create patterns for 3D models, wallpapers, or other design assets.

- **Prompt**: `Ancient stone bricks with moss growing between them, photorealistic --tile`

---

## Troubleshooting

| Issue | Cause | Solution |
|---|---|---|
| **Unwanted Elements** | The model included something you didn't want. | Use the `--no` parameter to specify what to exclude (e.g., `--no people, --no text`). |
| **Inconsistent Character** | The character's appearance changes between images. | Use the Omni Reference feature with a clear image of the character. For even more control, use the `--seed` parameter to maintain the same noise pattern. |
| **Output Too Artistic** | The `--stylize` value is too high, overriding the prompt. | Lower the `--stylize` value (e.g., `--s 100`) to make the model adhere more closely to your text prompt. |

---

## Integration

- **Interface**: Midjourney is primarily accessed via Discord bots. API access is available for enterprise customers.
- **Workflow Position**: Excellent for the initial ideation and concept art phase. The high aesthetic quality also makes it suitable for final asset generation.
- **Complementary Tools**: Use images generated in Midjourney as a starting point for video generation in models like Seedance or Runway, or for detailed editing in FLUX Kontext.
