# FLUX.1 Kontext - Image Editing

> **Currency (Jun 2026):** Kontext still works, but **FLUX.2** now unifies generation + in-context editing, and **Nano Banana 2** is an excellent conversational editor - evaluate both for new work. See [`model-currency-2026-06.md`](model-currency-2026-06.md).

---

## Quick Reference

| Attribute | Value |
|---|---|
| **Current Version** | 1.0 (Max, Pro, Dev) |
| **Model Type** | Image Editing, Multi-Modal |
| **Primary Use** | Iterative editing, character consistency, style transfer |
| **Max Resolution** | Varies by version |
| **Speed** | Interactive (designed for conversational workflows) |
| **API Endpoint** | `https://api.bfl.ai/v1/flux/image-to-image` |

---

## Overview

FLUX.1 Kontext is a suite of generative models from Black Forest Labs that unifies image generation and in-context editing. Unlike traditional models, Kontext processes both text and image inputs to perform precise modifications, maintain character consistency, and transfer styles. It is designed for fast, iterative workflows, allowing artists to refine images conversationally without complex masking.

> **Warning:** Kontext is for editing existing images. For generating images from scratch, refer to the `flux-pro.md` documentation.

### Version Tiers

- **Max**: Maximum performance and quality.
- **Pro**: Professional-grade for production use.
- **Dev**: Open-weights version for local and consumer hardware.

---

## When to Use This Model

Kontext is the go-to model for **refining and iterating on existing images**. It excels at tasks that require preserving parts of an image while changing others.

- **Use Kontext for**: Changing an object's color, adding or removing elements, changing the background, or ensuring a character looks the same across multiple images.
- **Do not use Kontext for**: Generating initial concepts from a blank slate. Use FLUX.1 Pro for that.

---

## Prompting Structure

Kontext prompts are **instructional**, telling the model what to change in a provided image. The key is to be explicit about what to change and what to preserve.

**Core Framework**: `[Action] the [Subject] to [New State], while preserving [Elements to Keep]`

```
+----------+----------------+---------------------+-------------------------+
| Action   | Subject        | New State           | Preservation            |
+----------+----------------+---------------------+-------------------------+
| "Change" | "the blue car" | "to a vibrant red"  | "while preserving the    |
|          |                |                     | background and lighting" |
+----------+----------------+---------------------+-------------------------+
```

---

## Parameters

Kontext is controlled via the prompt and the input images. The API has specific parameters for this workflow.

| Parameter | Type | Description |
|---|---|---|
| `prompt` | String | The instructional text prompt describing the change. |
| `image` | File | The base image to be edited. |
| `style_reference` | File | (Optional) An image to use as a style guide. |
| `mask` | File | (Optional) A black and white image to define the editable region. White is editable, black is preserved. |

---

## Techniques

### Basic: Localized Edits

Make targeted changes to a specific object or region. For best results, be explicit.

- **Good**: `"Make the apple green."`
- **Better**: `"Change the color of the red apple to a bright, vibrant green, while keeping the background and lighting identical."`

### Intermediate: Character Consistency

Preserve a character's identity across different scenes. This is one of Kontext's most powerful features.

- **Prompt**: `"Place the woman from the input image into a bustling Parisian cafe, preserving her facial features, hairstyle, and expression."`
- **Expected Output**: The same character, now in a new environment.

### Advanced: Masked Editing

For maximum precision, provide a mask file. This tells the model exactly which pixels to change and which to leave untouched.

- **Workflow**: Create a black and white mask where the area you want to edit is white. Upload it with the `mask` parameter.
- **Prompt**: `"Fill the masked area with a field of wildflowers."`

---

## Common Workflows

### 1. Background Replacement

Swap the background while keeping the foreground subject perfectly intact.

- **Prompt**: `"Change the background to a dramatic, stormy sky, while keeping the person in the foreground perfectly preserved."`

### 2. Iterative Refinement

Build a complex scene step-by-step. This conversational approach is what Kontext is designed for.

1.  **Start**: `"A portrait of a man."` (Generated with FLUX.1 Pro)
2.  **Edit 1 (Kontext)**: `"Remove the hat from the man."`
3.  **Edit 2 (Kontext)**: `"Now, give him a pair of sunglasses."`
4.  **Edit 3 (Kontext)**: `"Change the setting to a sunny beach."`

---

## Troubleshooting

| Issue | Cause | Solution |
|---|---|---|
| **Unintentional Changes** | The prompt was too vague, leading the model to alter more than intended. | Be explicit about what to preserve. Use phrases like "while keeping all other aspects unchanged" or "only change the [element]". Use a mask for precision. |
| **Loss of Character Identity** | A broad prompt like "transform into a viking" implies a full replacement. | Use more precise verbs like "change clothes to viking style" and add instructions to "preserve facial features, eye color, and expression". |
| **Seams or Artifacts** | The model struggled to blend the edited region with the background. | Try a slightly different prompt, or use a feathered mask to create a smoother transition between the editable and preserved areas. |

---

## Integration

- **API Example (Python)**:
    ```python
    import requests

    with open("base_image.png", "rb") as f:
        image_data = f.read()

    response = requests.post(
        "https://api.bfl.ai/v1/flux/image-to-image",
        headers={"Authorization": "Bearer YOUR_API_KEY"},
        data={"prompt": "Change the blue car to a vibrant red"},
        files={"image": image_data}
    )
    ```
- **Workflow Position**: Use Kontext in the refinement and iteration phase of a project, after initial concepts have been generated with a text-to-image model like FLUX.1 Pro.
- **Complementary Tools**: FLUX.1 Pro for base image generation.
