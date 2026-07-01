# {SHOW} - {Name} - Character Sheet

---

## Identity

> **Descriptor block** - paste verbatim into every downstream prompt:
>
> {50-80 words. Face structure, hair color and texture, skin tone with hex, body build,
> distinctive marks, default wardrobe note. Hex-pinned. Do not paraphrase downstream.
> Example: "Mid-30s man, lean build, sharp jaw, close-cropped dark brown hair, pale
> olive skin (#D4B896), faint scar above left brow. Default: slate-grey wool peacoat
> (#4A4E57), charcoal trousers, white shirt open at collar."}

### Hero reference

- Front anchor: `assets/char/{name}/char-{name}-id-front.png`
- 3/4 left: `assets/char/{name}/char-{name}-id-3q-l.png`
- 3/4 right: `assets/char/{name}/char-{name}-id-3q-r.png`
- Side left: `assets/char/{name}/char-{name}-id-side-l.png`
- Back: `assets/char/{name}/char-{name}-id-back.png`

Example (show: sbw, character: eli):
- `assets/char/eli/char-eli-id-front.png`
- `assets/char/eli/char-eli-id-3q-l.png`

### Turnaround set

- Front: `assets/char/{name}/char-{name}-turn-front.png`
- Side left: `assets/char/{name}/char-{name}-turn-side-l.png`
- Side right: `assets/char/{name}/char-{name}-turn-side-r.png`
- Back: `assets/char/{name}/char-{name}-turn-back.png`
- 3/4 left: `assets/char/{name}/char-{name}-turn-3q-l.png`
- 3/4 right: `assets/char/{name}/char-{name}-turn-3q-r.png`

Example:
- `assets/char/eli/char-eli-turn-front.png`
- `assets/char/eli/char-eli-turn-side-l.png`

### Reference lock

- **Method:** Reference images only / Reference + LoRA *(circle one)*
- **LoRA trigger word:** {trigger word, or N/A}
- **Reference count:** {N} images
- **Reference strength:** {0.0-1.0}

---

## Wardrobe

### {Costume name - e.g., Day 1}

- **Silhouette:** {silhouette description - e.g., slim-cut single-breasted, mid-calf}
- **Primary hex:** `#{RRGGBB}`
- **Secondary hex:** `#{RRGGBB}` *(if applicable)*
- **State:** clean / soiled / wet / torn *(circle one)*
- **Notes:** {garment names, materials, key construction details}
- **Images:**
  - `assets/char/{name}/char-{name}-fit-day1.png`
  - Example: `assets/char/eli/char-eli-fit-day1.png`

### {Costume name - e.g., Day 2 (wet)}

- **Silhouette:** {silhouette description}
- **Primary hex:** `#{RRGGBB}`
- **State:** wet
- **Notes:** {description of wet/soiled variations from Day 1 base; denoise value used}
- **Images:**
  - `assets/char/{name}/char-{name}-fit-{label}.png`
  - Example: `assets/char/eli/char-eli-fit-day2-wet.png`

*(Add a section for each additional costume state)*

---

## Makeup & Hair

### {State name - e.g., Clean}

- **Hair:** {color, texture, length, style}
- **Skin:** {baseline tone, coverage notes, any permanent marks}
- **Images:**
  - `assets/char/{name}/char-{name}-hmu-clean.png`
  - Example: `assets/char/eli/char-eli-hmu-clean.png`

### {State name - e.g., Wound 01}

- **Injury spec:**
  - Position: {anatomical location - e.g., right cheekbone}
  - Side: {left / right}
  - Size: {dimensions - e.g., 3 cm laceration}
  - Hex: `#{RRGGBB}` - e.g., fresh blood `#C0392B`, bruise `#4A235A`
- **Stage:** fresh / sutured / healing / healed *(circle one)*
- **Derived from:** {base state - e.g., Clean; denoise ~0.20}
- **Images:**
  - `assets/char/{name}/char-{name}-hmu-wound-01.png`
  - Example: `assets/char/eli/char-eli-hmu-wound-01.png`

### {State name - e.g., Aged}

- **Aging notes:** {description - e.g., 15 years added; deepened nasolabial folds,
  silver at temples, skin texture coarsened}
- **Derived from:** {base state; denoise value used}
- **Images:**
  - `assets/char/{name}/char-{name}-hmu-aged.png`
  - Example: `assets/char/eli/char-eli-hmu-aged.png`

*(Add sections for additional HMU states: wet, soiled, etc.)*

---

## Reference notes

- **Reference images total:** {N}
- **Reference strength:** {0.0-1.0} (range across sessions: {min}-{max})
- **Model:** {name and version}
- **LoRA:** {name / version, or N/A}
- **Currency check:** {date verified against model-currency-{month}.md}
- **Consistency notes:** {known drift points, model weaknesses, watch items}
