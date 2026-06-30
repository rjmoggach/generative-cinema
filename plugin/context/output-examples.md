# Output Examples

Reference for formatting. Every prompt is in a code block; labels above; model
parameters below, outside the block. All examples begin with a project's Standard
Prompt Prefix (here, a "poetic Americana" show).

## Single shot

**S2-02 Master — MS, eye-level, static**

```
Cinematic poetic Americana, naturalistic soft lighting, subtle 35mm film grain, lyrical tracking movement, shot on spherical 40mm lens at f/2.8, Dante Ariola and Lance Acord influence, William Eggleston color sensibility — Eli Manning at window, contemplative, eyes toward snowfall, quiet resolve. Medium shot, eye-level, rule of thirds with slight lead room left, minimal headroom. Static framing with implied gentle push-in energy. Soft window key from left wraps cheek, negative fill right, medium-shallow depth of field. Light snow falling outside catching backlight, steam on glass, faint breath condensation. Warm tabletop practicals dim in background bokeh (#F4E4C1 warm glow). Fine 35mm grain, subtle halation on highlights, protected shadow detail.
```

**Model Parameters** (FLUX.2 / FLUX.1 Pro): resolution 3840×2160 (16:9 UHD) · seed 4217 (continuity) · CFG 7.0

## Batch / sequence

**S2-01 Establishing — LS, eye-level, static**

```
Cinematic poetic Americana, naturalistic soft lighting, subtle 35mm film grain, lyrical tracking movement, shot on spherical 40mm lens at f/2.8, Dante Ariola and Lance Acord influence, William Eggleston color sensibility — Interior New Jersey living room, morning. Eli silhouetted near picture window, soft north-light key, negative fill on room side, light snow falling outside catching backlight. Family ephemera and winter coats in soft bokeh, warm tabletop practicals dim. Clean headroom, rule-of-thirds, protected copy space right.
```

**S2-03 Coverage — CU profile, eye-level**

```
Cinematic poetic Americana, naturalistic soft lighting, subtle 35mm film grain, lyrical tracking movement, shot on spherical 40mm lens at f/2.8, Dante Ariola and Lance Acord influence, William Eggleston color sensibility — Tight profile of Eli against cool window glow, snow drifting beyond. Soft key, crisp catchlight, shadow falloff on far cheek. Subtle skin texture, gentle halation on highlights, background practicals in oval bokeh.
```

**Model Parameters** (FLUX.2): resolution 3840×2160 · seed 4217 (hold across shots for continuity)

## Veo 3.1 JSON variant

```json
{
  "scene": "Eli at the living-room window at morning, light snow outside",
  "movement": "Slow dolly push-in",
  "angle": "Eye level",
  "lens": "40mm spherical",
  "lighting": "Soft north-light window key, negative fill right",
  "atmosphere": "Snow catching backlight, steam on glass",
  "color_grading": "Warm naturalistic Americana, #F4E4C1 practicals",
  "style": "Poetic Americana, subtle 35mm grain",
  "duration": "8 seconds",
  "negative_prompt": "harsh contrast, oversaturation, lens distortion"
}
```
