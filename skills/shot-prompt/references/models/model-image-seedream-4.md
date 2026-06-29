# Seedream - v4.0

> **Currency (Jun 2026):** Current generation is **Seedream 5.0 Lite** (Apr 2026; v5 adds Chain-of-Thought reasoning + web search before generating). Technique below still applies. See [`model-currency-2026-06.md`](model-currency-2026-06.md).

---

## Quick Reference

| Attribute | Value |
|---|---|
| **Current Version** | 4.0 (doubao-seedream-4-0-250828) |
| **Model Type** | Text-to-Image, Image Editing |
| **Primary Use** | Ultra high-resolution, knowledge-based image generation |
| **Max Resolution** | 4K (4096px) Native |
| **Interface** | API, Doubao App |
| **Key Features** | 4K native output, unified editing/generation, strong reasoning |

---

## Overview

Seedream 4.0 is the latest-generation image creation model from ByteDance. It features a unified architecture that integrates both image generation and editing, allowing it to handle complex multi-modal tasks with high fidelity. The model is known for its exceptional prompt adherence, aesthetic quality, and its unique ability to generate stunning images at a native 4K resolution. It also possesses strong reasoning capabilities and can leverage rich knowledge to create accurate visuals like professional charts and illustrations.

> **Tip:** Seedream supports negative prompts. Use them to refine your output and remove unwanted artifacts.

---

## When to Use This Model

Seedream 4.0 is the best choice when **maximum resolution and detail** are required, or when the image requires **complex reasoning or knowledge** (e.g., creating a diagram).

- **Use Seedream for**: Final print-quality assets, detailed architectural renders, scientific illustrations, and when you need the highest possible native resolution.
- **Consider Midjourney for**: More artistic and stylized outputs where creative interpretation is desired.
- **Consider FLUX.1 Pro for**: Faster generation if 4K native resolution is not a strict requirement.

---

## Prompting Structure

Seedream responds best to clear, descriptive language. The order of words matters, with critical style and subject tokens having more influence when placed at the beginning of the prompt.

**Core Framework**: `[Style & Medium] of a [Subject Description], [Environmental Context], [Technical Details] --no [Negative Prompt]`

```
+--------------------------+--------------------------+-----------------------+
| Style & Medium           | Subject & Context        | Technical & Negative  |
+--------------------------+--------------------------+-----------------------+
| "Ultra-realistic 4K photo" | "of a majestic eagle      | "85mm lens, --no blurry |
|                          | soaring over a mountain  | background, no        |
|                          | range at sunset"        | cartoonish features"  |
+--------------------------+--------------------------+-----------------------+
```

---

## Parameters

Control in Seedream is achieved through a combination of descriptive text, negative prompts, and reference images. API parameters may vary by provider.

| Control Method | Syntax | Purpose |
|---|---|---|
| Text Prompt | Natural language description | Defines the core content and style of the image. |
| Negative Prompt | `--no [text]` or API parameter | Excludes unwanted elements (e.g., `no blurry background`). |
| Reference Image | Image file(s) | Provides a strong reference for style, pose, or character consistency. |

---

## Techniques

### Basic: Leveraging 4K Native Resolution

To get the most out of Seedream, explicitly ask for high resolution and detail in your prompt.

- **Prompt**: `"An ultra-realistic, highly detailed, 4K photograph of a dewdrop on a spider web, macro photography."`

### Intermediate: Knowledge-Based Generation

Seedream can create images based on its internal knowledge. You can ask it to generate diagrams, charts, or illustrations of complex concepts.

- **Prompt**: `"A professional infographic showing the process of photosynthesis, in a clean, minimalist style, with clear labels for sunlight, water, and carbon dioxide."`

### Advanced: Multi-Image Composition

Because of its unified architecture, Seedream can understand and combine multiple images with a high degree of coherence.

- **Workflow**: Provide two images (e.g., a person and a location).
- **Prompt**: `"Using the two provided images, place the person from the first image into the cafe from the second image. Ensure the lighting on the person matches the cafe environment."`

---

## Common Workflows

### 1. Creating Print-Quality Artwork

Generate assets at their final required resolution, minimizing the need for upscaling.

- **Prompt**: `"A 4K, hyper-detailed fantasy illustration of a dragon perched on a castle, suitable for a large poster print."`

### 2. Scientific and Technical Illustration

Use the model’s reasoning capabilities to create accurate and clear visuals for educational or technical content.

- **Prompt**: `"A clear, labeled diagram of the human heart, showing the four chambers and major arteries, medical illustration style."`

---

## Troubleshooting

| Issue | Cause | Solution |
|---|---|---|
| **Ambiguous or Unfocused Output** | The prompt is too vague or contains conflicting ideas. | Simplify the prompt to focus on a single, clear concept. Break complex scenes into smaller, more manageable descriptions. |
| **Unwanted AI Artifacts** | Common issue with all generative models (e.g., extra fingers, strange textures). | Use a detailed negative prompt to exclude common artifacts. Example: `--no blurry, noisy, jpeg artifacts, extra limbs, malformed hands.` |
| **Style Overrides Content** | A very strong style reference may dominate the prompt. | Adjust the weight of the reference image if the API allows, or use a more descriptive text prompt to reinforce the desired content. |

---

## Integration

- **API Example**: API access is typically provided through platforms like BytePlus. The specific implementation will vary.
- **Workflow Position**: Seedream is a powerhouse for producing final, high-resolution assets. Its unified editing and generation capabilities can reduce the need for multiple tools in a pipeline.
- **Complementary Tools**: For video projects, assets generated with Seedream 4.0 can be used as high-quality initial frames for a video generation model like **Seedance Pro**.
