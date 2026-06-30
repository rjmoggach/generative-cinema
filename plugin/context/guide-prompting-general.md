# Generative AI Prompting Guide

**Objective**: This guide provides a universal set of principles and strategies for prompting any generative model effectively. It is designed to complement the specific model context files and help artists create high-quality visuals.

---

## The Core Philosophy: Be a Director, Not a Search Engine

Effective prompting is less like typing a search query and more like directing a film. Your goal is to give the AI a clear, vivid, and technically precise set of instructions. **Do not just list keywords; build a scene.**

## Universal Prompting Framework

Regardless of the model, a strong prompt contains several layers of information. Think of building your prompt in this order of importance:

1.  **Style & Medium (The "How")**: Define the overall aesthetic first. This has the most significant impact on the final look.
    *   **Medium**: `cinematic film still`, `wildlife documentary photo`, `oil painting`
    *   **Style**: `in the style of 1970s science fiction`, `Art Nouveau`, `cyberpunk`

2.  **Core Concept (The "What")**: Describe the main subject and action.
    *   **Subject**: `a lone astronaut`, `a majestic lion`, `a futuristic cityscape`
    *   **Action**: `standing on a desolate red planet`, `roaring on the Serengeti`, `gleaming at night`

3.  **Technical Details (The "Execution")**: Add specifics about the virtual camera, lighting, and composition. This is crucial for achieving a professional, non-generic look.
    *   **Lighting**: `harsh, direct sunlight casting long shadows`, `golden hour`, `neon-drenched`
    *   **Composition**: `wide shot`, `extreme close-up`, `rule of thirds`
    *   **Camera**: `shot on 35mm film`, `85mm lens`, `anamorphic lens flare`

4.  **Context & Mood (The "Where" and "Why")**: Describe the setting and the feeling you want to evoke.
    *   **Setting**: `with two moons in the sky`, `during a thunderstorm`
    *   **Mood**: `a sense of profound isolation and wonder`, `energetic and chaotic`

### Example Breakdown

`"Cinematic film still in the style of 1970s science fiction, a lone astronaut stands on a desolate red planet with two moons in the sky. The lighting is harsh and direct, casting long shadows. Wide shot, rule of thirds composition, shot on 35mm film with anamorphic lens flare. The mood is one of profound isolation and wonder."`

---

## Key Strategies for Success

### 1. Front-Load Critical Information

Models pay more attention to words at the beginning of the prompt. Place your most important instructions first.

-   **For a stylized image**: Start with the style. `"Impressionist oil painting of a..."`
-   **For a photorealistic image**: Start with the medium. `"Photorealistic portrait of a..."`

### 2. Use Specific, Evocative Language

Avoid generic terms. The more specific your words, the better the result.

-   **Instead of**: `A sad man`
-   **Use**: `A man with a somber expression, his face etched with weariness`

-   **Instead of**: `A nice car`
-   **Use**: `A pristine, cherry-red 1965 Ford Mustang convertible`

### 3. Master Positive Phrasing

Describe what you **want** to see, not what you **don’t** want to see. This is a universal rule, even for models that support negative prompts.

-   **Instead of**: `A room with no furniture`
-   **Use**: `An empty, spacious room with bare walls`

> **Note:** When a model supports negative prompts (like Midjourney or Seedream), use them as a *refinement tool* to remove specific artifacts (e.g., `--no blurry, text, watermark`), not as the primary way to define your scene.

### 4. Iterate and Refine

Your first prompt is rarely your last. Think of prompting as a conversation.

1.  Start with a simple prompt to get a baseline.
2.  Identify what works and what doesn’t.
3.  Add or change one element at a time to see how it affects the output.
4.  Use a fixed `seed` (if supported) to test prompt variations while keeping the base composition the same.

---

## Troubleshooting Common Prompting Issues

| Issue | Common Cause | Solution |
|---|---|---|
| **Generic, "AI-looking" Images** | The prompt was too simple or lacked technical details. | Add details about the camera, lens, lighting, and film stock. Specify a clear artistic style or reference. |
| **Inconsistent Characters** | The model is generating a different person in each image. | Use the model's character consistency feature if available (e.g., Midjourney's Omni Reference). If not, be extremely detailed and consistent in your character descriptions. |
| **Ignoring Part of the Prompt** | The prompt is too long, complex, or has conflicting terms. | Simplify the prompt. Focus on one core idea. Ensure your keywords don't contradict each other (e.g., "minimalist" and "highly detailed"). |
| **Unwanted Elements Appear** | The model has strong training data biases. | Use the model’s negative prompt feature if it has one. If not, try to guide the model away from the unwanted element by being more specific about the desired elements. |

---

## Final Checklist for a Great Prompt

Before you hit "generate," ask yourself:

-   [ ] **Is my style/medium defined first?**
-   [ ] **Is my core concept (subject + action) clear?**
-   [ ] **Have I included technical details (lighting, camera)?**
-   [ ] **Is my language specific and evocative?**
-   [ ] **Am I using positive phrasing?**
