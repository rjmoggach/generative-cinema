# The Six-Layer Framework for Cinematic AI Video Generation

This framework integrates the principles of classical film grammar from Arijon and Spottiswoode 
with modern AI video generation techniques. It provides a comprehensive structure for crafting 
prompts that cover the entire gamut of cinematic possibility.

---

## Layer 1: Subject, Action, and Narrative Intent

This layer defines the core narrative of the shot. It answers the questions: **Who? What? Why?**

| Category | Description | Examples |
|---|---|---|
| **Subject** | The main character, object, or focus of the shot. | `a seasoned detective`, `a futuristic cityscape`, `a lone wolf` |
| **Action** | The primary activity or movement occurring in the shot. | `investigating a crime scene`, `shimmering in the heat haze`, `howling at the moon` |
| **Narrative Intent** | The underlying purpose or emotion of the shot. | `conveying a sense of dread`, `establishing a feeling of awe`, `expressing profound loneliness` |
| **Dialogue Staging** | For scenes with dialogue, specify the staging. | `two-player face-to-face`, `three-player triangle`, `telephone conversation with opposed diagonals` |

---

## Layer 2: Shot Composition and Framing

This layer defines the visual composition of the shot, including distance, angle, and arrangement of elements. It answers the question: **How is the scene framed?**

| Category | Description | Examples |
|---|---|---|
| **Shot Distance** | The perceived distance between the camera and the subject. | `Extreme Long Shot (ELS)`, `Medium Shot (MS)`, `Big Close Up (BCU)` |
| **Camera Angle** | The vertical angle of the camera relative to the subject. | `Low Angle`, `High Angle`, `Dutch Angle`, `Bird's Eye View` |
| **Compositional Principles** | The arrangement of elements within the frame. | `Triangle Principle`, `Rule of Thirds`, `Symmetrical Composition`, `Diagonal Composition` |
| **Framing Precision** | Specific framing instructions. | `Cutting height under the waist`, `Headroom for subject`, `Negative space to the left` |

---

## Layer 3: Camera Dynamics and Movement

This layer defines how the camera moves through space, adding energy and perspective. It answers the question: **How does the camera move?**

| Category | Description | Examples |
|---|---|---|
| **Basic Movements** | Fundamental camera movements. | `Tracking Shot`, `Pan`, `Tilt`, `Dolly`, `Crane` |
| **Combination Movements** | Complex movements combining multiple techniques. | `Dolly Zoom (Vertigo Effect)`, `Circular Tracking`, `Arc Shot` |
| **Focus Manipulation** | Directing attention by changing focus. | `Rack Focus`, `Deep Focus`, `Shallow Focus`, `Soft Focus` |
| **Movement Quality** | The style and speed of the movement. | `Slow and deliberate`, `Handheld and chaotic`, `Smooth Steadicam glide` |

---

## Layer 4: Lighting, Color, and Atmosphere

This layer defines the visual mood and tone of the shot through light, color, and environmental effects. It answers the question: **What is the visual mood?**

| Category | Description | Examples |
|---|---|---|
| **Lighting Styles** | The overall lighting setup. | `High Key`, `Low Key`, `Chiaroscuro`, `Rembrandt Lighting`, `Three-Point Lighting` |
| **Time of Day** | The time of day, which dictates natural light quality. | `Golden Hour`, `Blue Hour`, `Midday Sun`, `Twilight` |
| **Color Theory** | The use of color to create mood and meaning. | `Monochromatic`, `Saturated`, `Desaturated`, `Teal and Orange` |
| **Atmospheric Effects** | Environmental elements that add texture and mood. | `Volumetric Fog`, `Heavy Rain`, `Lens Flares`, `Film Grain`, `Dust Particles` |

---

## Layer 5: Technical Specifications and Lens Choice

This layer defines the specific technical parameters of the virtual camera and lens, influencing the final look and feel. It answers the question: **What camera and lens are we using?**

| Category | Description | Examples |
|---|---|---|
| **Lens Type** | The focal length of the virtual lens. | `35mm Wide Angle`, `50mm Natural Perspective`, `85mm Portrait`, `Macro`, `Anamorphic` |
| **Optical Characteristics** | The specific visual properties of the lens. | `Shallow Depth of Field`, `Deep Depth of Field`, `Bokeh`, `Lens Flares`, `Fisheye Distortion` |
| **Film Stock/Format** | The type of film or digital format being simulated. | `35mm film grain`, `Kodak Portra color palette`, `IMAX quality`, `Vintage 1970s film stock` |
| **Resolution/Quality** | The desired output quality. | `8k resolution`, `ultra high quality`, `professional cinematography` |

---

## Layer 6: Editing, Pacing, and Transitions

This layer defines the temporal aspects of the shot, including its duration, rhythm, and relationship to other shots. It answers the question: **How does this shot fit into the sequence?**

| Category | Description | Examples |
|---|---|---|
| **Pacing and Rhythm** | The speed and flow of the shot. | `Slow motion (120fps)`, `Fast motion (time lapse)`, `Energetic pacing`, `Contemplative rhythm` |
| **Editing Techniques** | How the shot is cut and combined with others. | `Parallel Editing`, `Match Cut`, `Jump Cut`, `Insert Shot`, `Cutaway` |
| **Transitions** | How the shot begins and ends. | `Straight Cut`, `Fade In/Out`, `Dissolve`, `Wipe`, `L-Cut/J-Cut` |
| **Montage Theory** | The conceptual effect of shot juxtaposition. | `Rhythmical Montage`, `Implicational Montage`, `Ideological Montage` |

---

## Framework Flexibility and Adaptation

**CRITICAL**: This framework is descriptive, not prescriptive. You do NOT need to use all six layers for every prompt.

### When to Use Which Layers

**Minimal Prompt (Layers 1-2 only)**: Quick iteration, simple shots, test generations

- Subject + Action + Shot/Framing
- Example: "A chef preparing sushi, Medium Close Up"

**Moderate Prompt (Layers 1-4)**: Most production work, balanced detail

- Add Camera Movement + Lighting
- Suitable for 80% of prompts

**Complex Prompt (All 6 Layers)**: Hero shots, key sequences, precise vision

- Use when exact technical control is required
- Commercial work, final deliverables

### Layer Priority by Model

| Model | Essential Layers | Optional Layers |
|-------|-----------------|-----------------|
| **Kling 2.5** | 1, 2, 3 (movement is critical) | 4, 5, 6 |
| **Sora 2 Pro** | 1, 2, 6 (multi-shot focus) | 3, 4, 5 |
| **Veo 3.1** | All layers (accepts complex JSON) | None - use all |
| **Wan 2.5** | 1 (dialogue), 2, 4 | 3, 5, 6 |

### Adaptation Guidelines

1. **Start simple, add complexity**: Begin with 2-3 layers, add more if results aren't precise enough
2. **Front-load critical details**: Most important elements in first 20 words
3. **Model-specific**: Some models ignore technical specs (Layer 5), others require them
4. **Iterate systematically**: Change ONE layer at a time to understand its effect

---

## Prompt Templates and Examples

### Template 1: Minimal (2 Layers)

```
[Layer 2: Shot Type] of [Layer 1: Subject] [Layer 1: Action]
```

**Example**: "Close Up of a barista pouring latte art"

**Use Case**: Quick tests, simple animations, iterative exploration

---

### Template 2: Moderate (4 Layers)

```
[Layer 2: Shot Type] of [Layer 1: Subject] [Layer 1: Action], [Layer 3: Camera Movement]. [Layer 4: Lighting Style] lighting, [Layer 4: Atmosphere].
```

**Example**: "Medium Shot of a cyclist racing through a forest trail, tracking shot following from the side. Golden hour lighting, dappled sunlight through trees."

**Use Case**: Standard production work, most commercial projects

---

### Template 3: Detailed (5 Layers)

```
[Layer 2: Shot Type] of [Layer 1: Subject] [Layer 1: Action] with [Layer 1: Narrative Intent]. [Layer 3: Camera Movement] using [Layer 5: Lens Type] with [Layer 5: Optical Characteristic]. [Layer 4: Lighting Style] during [Layer 4: Time of Day], [Layer 4: Color] palette.
```

**Example**: "Full Shot of a pianist performing at a grand concert hall with quiet intensity. Slow crane shot descending from above using 35mm wide-angle lens with deep depth of field. Three-point lighting during evening, warm amber palette."

**Use Case**: Key hero shots, precise aesthetic control

---

### Template 4: Complex (All 6 Layers)

```
[Layer 2: Shot/Framing] of [Layer 1: Subject] [Layer 1: Action] with [Layer 1: Narrative Intent], set in [Setting]. The scene is captured with [Layer 3: Camera Movement] using a [Layer 5: Lens Type] with [Layer 5: Optical Characteristic]. The lighting is [Layer 4: Lighting Style] during [Layer 4: Time of Day], creating a [Layer 4: Color/Atmosphere] mood. The shot has a [Layer 6: Pacing/Rhythm] and ends with a [Layer 6: Transition]. [Layer 5: Technical Specs].
```

**Example**: "Medium Shot of a seasoned detective investigating a crime scene with a sense of dread, set in a rain-soaked alley. The scene is captured with a slow dolly push-in using an 85mm Portrait lens with shallow depth of field. The lighting is Low Key during the Blue Hour, creating a desaturated and mysterious mood. The shot has a contemplative rhythm and ends with a slow dissolve. 35mm film grain, professional cinematography."

**Use Case**: Final deliverables, commercial work, maximum control

---

### Template 5: Multi-Shot Sequence (Sora/Seedance)

```
Shot 1: [Layer 2] of [Layer 1 Subject/Action]. Shot 2: [Different Layer 2] of [Layer 1 continuation]. Shot 3: [Layer 2] revealing [detail]. [Layer 4: Lighting], [Layer 5: Technical].
```

**Example**: "Shot 1: Extreme Long Shot of a lone figure walking across a desert at sunset. Shot 2: Medium Shot tracking alongside the figure, revealing weathered clothing. Shot 3: Close Up of their determined face, dust-covered. Golden hour lighting, anamorphic lens with horizontal flares, 35mm film grain."

**Use Case**: Narrative sequences, establishing + detail combinations

---

### Template 6: Dialogue Scene (Wan 2.5)

```
[Layer 2: Framing] of [Layer 1: Subject] [Layer 1: Dialogue Staging]. The character says "[dialogue]" with [emotion/tone]. [Layer 4: Lighting], [Layer 3: Camera Movement if any].
```

**Example**: "Medium Close Up of a young woman in a coffee shop, face-to-face dialogue staging. She says 'I can't believe you're leaving' with quiet devastation. Soft window light from the left, static shot."

**Use Case**: Character dialogue, emotional scenes, lip-sync requirements
