# {SHOW} - {Name} - Prop Sheet

---

## Hero

> **Descriptor block** — paste verbatim into every downstream prompt:
>
> {40-70 words. Object class, overall form, primary material and finish with hex,
> secondary material if relevant, key identifying marks (engraving, logo, wear, patina),
> scale cue (length/weight class), and any critical proportional note. Hex-pinned.
> Example: "Lever-action rifle, 24-inch octagonal barrel, case-hardened steel
> (#3D3D3A), walnut stock (#7B4F2E) with cheekpiece, brass trigger guard (#B5A642),
> faint wear at the lever loop. Approximately 100 cm overall."}

- **Hero anchor:** `assets/prop/{name}/prop-{name}-hero.png`
- **Material:** {primary material — e.g., case-hardened steel `#3D3D3A`}
- **Finish:** {surface finish — e.g., matte blued, high-polish, oiled walnut}
- **Secondary material:** {if applicable — e.g., walnut stock `#7B4F2E`}
- **Scale cue:** {approximate length, height, or weight class}
- **Prop class:** hero / dressing / action *(circle one)*

Example (show: sbw, prop: revolver):
- `assets/prop/revolver/prop-revolver-hero.png`

---

## Orthographic ring

- Front: `assets/prop/{name}/prop-{name}-ortho-front.png`
- Back: `assets/prop/{name}/prop-{name}-ortho-back.png`
- Side left: `assets/prop/{name}/prop-{name}-ortho-side-l.png`
- Side right: `assets/prop/{name}/prop-{name}-ortho-side-r.png`
- Top: `assets/prop/{name}/prop-{name}-ortho-top.png`
- Bottom: `assets/prop/{name}/prop-{name}-ortho-bottom.png` *(include only if relevant)*

Example (prop: revolver):
- `assets/prop/revolver/prop-revolver-ortho-front.png`
- `assets/prop/revolver/prop-revolver-ortho-side-l.png`

**Alignment notes:** {camera distance, lens length, any axis alignment note — held
constant across the ring}

---

## Details

### {Detail name — e.g., Barrel inscription}

- **Image:** `assets/prop/{name}/prop-{name}-detail-01.png`
- **Derived from:** {ortho view this was cropped/enlarged from — e.g., ortho-front}
- **What it shows:** {feature and production reason — e.g., maker's mark, legible in
  close-up insert}

### {Detail name — e.g., Clasp mechanism}

- **Image:** `assets/prop/{name}/prop-{name}-detail-02.png`
- **Derived from:** {source ortho view}
- **What it shows:** {feature and production reason}

Example (prop: revolver):
- `assets/prop/revolver/prop-revolver-detail-01.png`

*(Add a section for each additional detail)*

---

## State variants

### {State name — e.g., Pristine}

- **Image:** `assets/prop/{name}/prop-{name}-hero.png` *(the base anchor)*
- **Notes:** {clean/unused condition — e.g., no wear, factory finish}

### {State name — e.g., Aged}

- **Image:** `assets/prop/{name}/prop-{name}-hero-aged.png`
- **Derived from:** {base state; denoise value used — e.g., pristine hero; denoise ~0.20}
- **Notes:** {description of aging — e.g., oxidised barrel, stock wear at grip}

### {State name — e.g., Damaged}

- **Image:** `assets/prop/{name}/prop-{name}-hero-damaged.png`
- **Derived from:** {base state; denoise value}
- **Notes:** {damage spec — e.g., cracked stock, bent trigger guard; position + hex}

### {State name — e.g., Wet}

- **Image:** `assets/prop/{name}/prop-{name}-hero-wet.png`
- **Derived from:** {base state; denoise value}
- **Notes:** {wet/soiled variation notes}

Example (prop: revolver):
- `assets/prop/revolver/prop-revolver-hero-aged.png`
- `assets/prop/revolver/prop-revolver-hero-damaged.png`

*(Add a section for each additional state)*

---

## Multiples

*(Complete this section only if instances of this prop appear together in the same
frame — e.g., a pair of handcuffs, a rack of matching rifles.)*

### {Multiple label — e.g., Instance A}

- **Image:** `assets/prop/{name}/prop-{name}-hero.png` *(same anchor; same ref strength)*
- **Notes:** {any positional or staging note for this instance}

### {Multiple label — e.g., Instance B}

- **Image:** `assets/prop/{name}/prop-{name}-hero.png`
- **Notes:** {staging note}

*All multiples must be derived from the same hero anchor at the same reference strength
to read as identical objects rather than variants.*

---

## Reference notes

- **Reference images total:** {N}
- **Reference strength:** {0.0-1.0} (range across sessions: {min}-{max})
- **Model:** {name and version — e.g., FLUX.1 Kontext, 2026-06}
- **Currency check:** {date verified against model-currency-{month}.md}
- **Consistency notes:** {known drift points, model weaknesses, watch items — e.g.,
  specular highlights on barrel blow out above strength 0.75; composite logo in post}
