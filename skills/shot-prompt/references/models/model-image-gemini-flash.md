# Gemini Flash - Image Generation

> **Currency (Jun 2026):** Current generation is **Nano Banana 2 (Gemini 3.1 Flash Image)** - default since Feb 2026 - plus **Nano Banana Pro (Gemini 3 Pro Image)** for hero/text work. Technique below still applies. See [`model-currency-2026-06.md`](model-currency-2026-06.md).

---

## Quick Reference

| Attribute | Value |
|---|---|
| **Current Version** | 2.5 Flash Image |
| **Model Type** | Text-to-Image, Multi-Modal Editing |
| **Primary Use** | Conversational image creation, text rendering |
| **Max Resolution** | High-resolution via API |
| **Interface** | API, Google AI Studio |
| **Key Features** | Conversational editing, strong text rendering, multi-image composition |

---

## Overview

Gemini 2.5 Flash Image (also known as Nano Banana) is a powerful and versatile image generation model from Google. It is designed for conversational and multi-modal interaction, allowing users to create and edit images using a combination of text and image inputs. Its core strength lies in its deep language understanding, which enables it to interpret detailed, narrative prompts to produce coherent and high-quality images.

> **Tip:** Think of prompting Gemini like you are describing a scene to a human artist. Narrative paragraphs work better than keyword lists.

---

## When to Use This Model

Gemini is the ideal choice for tasks that require **strong language understanding, conversational editing, or reliable text rendering** within an image.

- **Use Gemini for**: Creating images with specific text, iterative refinement (e.g., "now change the car to red"), or composing scenes from multiple reference images.
- **Consider Midjourney for**: More artistic and stylized outputs.
- **Consider FLUX.1 Pro for**: Faster generation of high-resolution commercial assets.

---

## Prompting Structure

The fundamental principle for prompting Gemini is to **describe the scene, not just list keywords**. A narrative, descriptive paragraph will almost always produce a better result.

**Core Framework**: `[A detailed, narrative description of the scene, including subject, action, style, and context]`

```
+--------------------------------------------------------------------+
| Narrative Prompt                                                   |
+--------------------------------------------------------------------+
| "A photorealistic wide shot of a lone astronaut standing on the     |
| surface of Mars. The landscape is a vast, rocky desert under a     |
| thin, pinkish sky. The astronaut is looking towards a distant      |
| mountain range, and the sun is low on the horizon, casting long    |
| shadows. The mood is one of quiet contemplation and solitude."      |
+--------------------------------------------------------------------+
```

---

## Parameters

Control over Gemini image generation is primarily managed through the descriptive prompt and API settings.

| Parameter | Type | Description |
|---|---|---|
| `prompt` | String | The descriptive, narrative text prompt. |
| `images` | List[File] | A list of input images for editing or composition. |
| `aspect_ratio` | String | Defines the output image dimensions (e.g., `16:9`, `1:1`). |
| `negative_prompt` | String | A description of what to avoid in the image. |

---

## Techniques

### Basic: Accurate Text in Images

Gemini has strong text rendering capabilities. Clearly state the text, its style, and its placement.

- **Prompt**: `"Create a birthday cake with the text 'Happy Birthday, Alex!' written in elegant blue icing."`

### Intermediate: Conversational Editing

The model is designed for a chat-based workflow. You can provide an initial prompt and then make sequential edits.

1.  **User**: `"A blue sports car parked on a city street."`
2.  **Gemini**: [Generates image]
3.  **User**: `"Great. Now, turn this car into a convertible."`
4.  **Gemini**: [Generates updated image]

### Advanced: Multi-Image Composition

Provide multiple images as input and describe how to combine them.

- **Workflow**: Upload an image of a cat and an image of a library.
- **Prompt**: `"Using the two provided images, place the cat from the first image onto the stack of books in the second image. Make sure to match the lighting and style of the library."`

---

## Common Workflows

### 1. Creating Illustrated Recipes

Leverage Gemini's ability to interleave text and images to generate steps for a recipe or tutorial.

- **Prompt**: `"Create a visual guide for making a pizza. Step 1: Show a ball of dough. Step 2: Show the dough being rolled out. Step 3: Show tomato sauce being spread on the dough."`

### 2. Product Mockups with Text

Generate product shots that include specific branding or text.

- **Prompt**: `"A professional product shot of a white coffee mug with the logo 'The Morning Brew' printed on the side."`

---

## Troubleshooting

| Issue | Cause | Solution |
|---|---|---|
| **Output is too literal or lacks creativity** | The prompt was a list of keywords rather than a descriptive scene. | Rewrite the prompt as a narrative paragraph. Describe the atmosphere, mood, and story you want to convey. |
| **Edits affect the wrong part of the image** | The prompt was not specific enough about the subject of the edit. | Be very specific in your instructions. Instead of "change it", say "change the red car in the foreground". |
| **Inconsistent style during editing** | The model did not fully capture the style of the original image. | Add a phrase like "...while maintaining the original photorealistic style" to your editing prompt. |

---

## Integration

- **API Example (Python)**:
    ```python
    import google.generativeai as genai

    model = genai.GenerativeModel("gemini-2.5-flash-image")
    response = model.generate_content(
        "A photorealistic image of a majestic lion on the Serengeti plains, golden hour lighting, 8k"
    )
    ```
- **Workflow Position**: Extremely versatile. Can be used for initial brainstorming, iterative development, and final asset creation, especially when text is involved.
- **Complementary Tools**: Can be used to generate base images that are then animated with a video model like Seedance or refined with a specialized editing tool.
