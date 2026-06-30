# Deep Recursive Questioning Framework

This document provides an advanced framework for guiding an LLM to extract visual style preferences
from a user through a series of deep, recursive, conversational questions. The goal is to translate
vague, emotional language into a structured visual profile, grounded in the comprehensive reference
library and mapped to the six-layer prompting framework.

## The Core Principle: From Abstract to Concrete, Mapped to the Six Layers

The framework is designed to move the conversation from the abstract (the emotional core of the project)
to the concrete (specific technical choices and auteur references), with each phase of the conversation
directly informing a layer of the six-layer prompting framework.

### Phase 1: The Emotional Core (Informs Layer 1: Subject & Narrative)

#### Goal

To understand the fundamental feeling and narrative intent of the project.

#### Initial Question

"Before we talk about visuals, let's talk about feeling. When someone watches
this, what is the single, dominant emotion we want them to feel?"

#### Recursive Questions

- "Is that a quiet, internal feeling, or a loud, external one?"
- "Is it a simple feeling, or a complex, contradictory one?"
- "If that feeling had a texture, would it be rough or smooth?"
- "If it had a temperature, would it be warm or cold?"
- "What is the core narrative idea? Is it a story of triumph, tragedy, or something else?"

### Phase 2: The World of the Story (Informs Layer 1: Setting & Atmosphere)

#### Goal

To define the reality level and atmospheric qualities of the project.

#### Initial Question

"Now let's talk about the world of the story. Is this a world that feels like our own, or is it a
heightened, stylized version of reality?"

#### Recursive Questions

- "Is it a world of dreams and nightmares, or a world of gritty realism?"
- "Is it a world of the past, the present, or the future?"
- "Is it a world of order and control, or a world of chaos and chance?"
- "Is it a world of beauty and harmony, or a world of ugliness and discord?"
- "What does this world smell like? What does it sound like?"

### Phase 3: The Visual Language (Informs Layers 2, 3, 4, 5)

#### Goal

To translate the emotional core and world of the story into specific visual elements.

#### Initial Question

"Now that we have a sense of the feeling and the world, let's start to translate that into a visual
language. Let's start with color. Do you see this world as being vibrant and colorful, or more muted
and monochromatic?"

#### Recursive Questions (for each technical dimension)

##### Color (Layer 4)

- "Are the colors warm or cool?"
- "Are the colors saturated or desaturated?"
- "Are the colors naturalistic or artificial?"
- "Is there a dominant color?"

##### Lighting (Layer 4)

- "Is the lighting bright and even, or dark and shadowy?"
- "Is it hard or soft?"
- "Natural or artificial?"
- "Is there a particular time of day you envision?"

##### Composition (Layer 2)

- "Are the compositions balanced and symmetrical, or unbalanced and asymmetrical?"
- "Are they clean and simple, or cluttered and complex?"
- "Do they feel open or claustrophobic?"

##### Movement (Layer 3)

- "Is the camera still and observational, or is it constantly moving?"
- "Is the movement smooth and graceful, or rough and chaotic?"
- "Is it motivated by the characters, or does it have a life of its own?"

##### Optics (Layer 5)

- "Do the images feel clean and sharp, or soft and dreamy?"
- "Is there a particular texture or grain you envision?"

### Phase 4: Auteur Influence (Informs Layer 6: Editing & Pacing)

#### Goal

To use specific artists as a shorthand for complex visual ideas and to understand
the desired editing style.

#### Initial Question

"Now that we have a strong sense of the visual language, it can be helpful to use other artists as a
reference. Is there a particular director, cinematographer, or photographer whose work resonates
with what you're trying to achieve?"

#### Recursive Questions

- "What is it about their work that you're drawn to? Is it their use of color, their lighting,
  their camera movement, their editing, or something else?"
- "Are there any specific films, music videos, or photographs of theirs that you have in mind?"
- "In terms of editing, do you see this as being fast-paced and energetic, or slow and contemplative?"
- "Are there any artists whose work you want to actively avoid?"

## The Output: The Project Visual Profile

After the conversation, the LLM should synthesize all the user's responses and the mapped references
into a structured markdown document titled "Project Visual Profile." This document should be a
comprehensive summary of the project's visual DNA, organized by the six-layer framework, and ready to
inform the shot generation process.
