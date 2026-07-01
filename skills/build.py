#!/usr/bin/env python3
"""Build standalone, installable .skill packages from this repo.

The library's `context/` directory is the single source of truth. Each skill
bundles COPIES of the context files it needs into its own `references/` folder so
the packaged `.skill` zip is fully self-contained (no `../../context/` paths that
would break once shared/installed).

Usage:
    python skills/build.py          # sync references + package into skills/dist/
    python skills/build.py --sync   # only copy context files into references/
    python skills/build.py --zip    # only (re)build the .skill zips
"""
from __future__ import annotations
import argparse, shutil, zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CTX = REPO / "context"
SKILLS = REPO / "skills"
DIST = SKILLS / "dist"

MANIFEST = {
    "project-context": [
        ("reference-visual-film-directors.md", "references/reference-visual-film-directors.md"),
        ("reference-visual-cinematographers.md", "references/reference-visual-cinematographers.md"),
        ("reference-visual-commercial-directors.md", "references/reference-visual-commercial-directors.md"),
        ("reference-visual-photographers.md", "references/reference-visual-photographers.md"),
        ("reference-film-movements.md", "references/reference-film-movements.md"),
        ("guide-lens-language.md", "references/guide-lens-language.md"),
        ("guide-visual-structure.md", "references/guide-visual-structure.md"),
        ("guide-color-story.md", "references/guide-color-story.md"),
        ("guide-creative-approaches.md", "references/guide-creative-approaches.md"),
    ],
    "shot-prompt": [
        ("guide-prompting-framework.md", "references/guide-prompting-framework.md"),
        ("reference-film-grammar.md", "references/reference-film-grammar.md"),
        ("guide-shot-selection.md", "references/guide-shot-selection.md"),
        ("guide-lens-language.md", "references/guide-lens-language.md"),
        ("guide-continuity-rules.md", "references/guide-continuity-rules.md"),
        ("guide-sequence-construction.md", "references/guide-sequence-construction.md"),
        ("guide-visual-structure.md", "references/guide-visual-structure.md"),
        ("guide-color-story.md", "references/guide-color-story.md"),
        ("guide-creative-approaches.md", "references/guide-creative-approaches.md"),
        ("guide-ai-generation-strategy.md", "references/guide-ai-generation-strategy.md"),
        ("model-currency-2026-06.md", "references/model-currency-2026-06.md"),
        ("model-image-flux-pro.md", "references/models/model-image-flux-pro.md"),
        ("model-image-gemini-flash.md", "references/models/model-image-gemini-flash.md"),
        ("model-image-midjourney-v7.md", "references/models/model-image-midjourney-v7.md"),
        ("model-image-seedream-4.md", "references/models/model-image-seedream-4.md"),
        ("model-image-luma-uni-1.md", "references/models/model-image-luma-uni-1.md"),
        ("model-video-seedance-pro.md", "references/models/model-video-seedance-pro.md"),
        ("model-video-runway-gen4-turbo.md", "references/models/model-video-runway-gen4-turbo.md"),
        ("model-video-google-veo-3-1.md", "references/models/model-video-google-veo-3-1.md"),
        ("model-video-luma-ray3.md", "references/models/model-video-luma-ray3.md"),
        ("model-editing-flux-kontext.md", "references/models/model-editing-flux-kontext.md"),
        ("model-video-kling-3.md", "references/models/model-video-kling-3.md"),
        ("model-video-sora-2.md", "references/models/model-video-sora-2.md"),
        ("model-video-wan-2-6.md", "references/models/model-video-wan-2-6.md"),
        ("guide-asset-reference.md", "references/guide-asset-reference.md"),
        ("guide-image-editing.md", "references/guide-image-editing.md"),
    ],
    "sequence-design": [
        ("guide-sequence-construction.md", "references/guide-sequence-construction.md"),
        ("guide-continuity-rules.md", "references/guide-continuity-rules.md"),
        ("guide-visual-structure.md", "references/guide-visual-structure.md"),
        ("guide-shot-selection.md", "references/guide-shot-selection.md"),
        ("guide-lens-language.md", "references/guide-lens-language.md"),
        ("guide-asset-reference.md", "references/guide-asset-reference.md"),
    ],
    "footage-transform": [
        ("guide-footage-transformation.md", "references/guide-footage-transformation.md"),
        ("guide-ai-generation-strategy.md", "references/guide-ai-generation-strategy.md"),
        ("reference-film-grammar.md", "references/reference-film-grammar.md"),
        ("guide-lens-language.md", "references/guide-lens-language.md"),
        ("model-currency-2026-06.md", "references/model-currency-2026-06.md"),
        ("model-video-seedance-pro.md", "references/models/model-video-seedance-pro.md"),
        ("model-video-runway-gen4-turbo.md", "references/models/model-video-runway-gen4-turbo.md"),
        ("model-video-kling-3.md", "references/models/model-video-kling-3.md"),
        ("model-video-wan-2-6.md", "references/models/model-video-wan-2-6.md"),
        ("model-video-google-veo-3-1.md", "references/models/model-video-google-veo-3-1.md"),
    ],
    "model-docs": [
        ("model-currency-2026-06.md", "references/model-currency-2026-06.md"),
        ("model-image-flux-pro.md", "references/example-model-doc.md"),
        ("guide-ai-generation-strategy.md", "references/guide-ai-generation-strategy.md"),
    ],
    "image-edit": [
        ("guide-image-editing.md", "references/guide-image-editing.md"),
        ("guide-asset-reference.md", "references/guide-asset-reference.md"),
        ("guide-ai-generation-strategy.md", "references/guide-ai-generation-strategy.md"),
        ("guide-footage-transformation.md", "references/guide-footage-transformation.md"),
        ("model-currency-2026-06.md", "references/model-currency-2026-06.md"),
        ("model-editing-flux-kontext.md", "references/models/model-editing-flux-kontext.md"),
        ("model-image-gemini-flash.md", "references/models/model-image-gemini-flash.md"),
        ("model-image-seedream-4.md", "references/models/model-image-seedream-4.md"),
        ("model-image-luma-uni-1.md", "references/models/model-image-luma-uni-1.md"),
        ("model-image-flux-pro.md", "references/models/model-image-flux-pro.md"),
    ],
    "character-sheet": [
        ("reference-craft-character.md", "references/reference-craft-character.md"),
        ("guide-character-consistency.md", "references/guide-character-consistency.md"),
        ("guide-turnaround-sheets.md", "references/guide-turnaround-sheets.md"),
        ("guide-asset-reference.md", "references/guide-asset-reference.md"),
        ("guide-image-editing.md", "references/guide-image-editing.md"),
        ("model-currency-2026-06.md", "references/model-currency-2026-06.md"),
        ("model-editing-flux-kontext.md", "references/models/model-editing-flux-kontext.md"),
        ("model-image-gemini-flash.md", "references/models/model-image-gemini-flash.md"),
        ("model-image-seedream-4.md", "references/models/model-image-seedream-4.md"),
        ("model-image-flux-pro.md", "references/models/model-image-flux-pro.md"),
    ],
    "prop-turntable": [
        ("reference-craft-artdept.md", "references/reference-craft-artdept.md"),
        ("guide-prop-turntable.md", "references/guide-prop-turntable.md"),
        ("guide-asset-reference.md", "references/guide-asset-reference.md"),
        ("guide-image-editing.md", "references/guide-image-editing.md"),
        ("model-currency-2026-06.md", "references/model-currency-2026-06.md"),
        ("model-editing-flux-kontext.md", "references/models/model-editing-flux-kontext.md"),
        ("model-image-gemini-flash.md", "references/models/model-image-gemini-flash.md"),
        ("model-image-seedream-4.md", "references/models/model-image-seedream-4.md"),
        ("model-image-flux-pro.md", "references/models/model-image-flux-pro.md"),
    ],
    "location-pack": [
        ("reference-craft-artdept.md", "references/reference-craft-artdept.md"),
        ("guide-location-pack.md", "references/guide-location-pack.md"),
        ("guide-asset-reference.md", "references/guide-asset-reference.md"),
        ("guide-image-editing.md", "references/guide-image-editing.md"),
        ("model-currency-2026-06.md", "references/model-currency-2026-06.md"),
        ("model-editing-flux-kontext.md", "references/models/model-editing-flux-kontext.md"),
        ("model-image-gemini-flash.md", "references/models/model-image-gemini-flash.md"),
        ("model-image-seedream-4.md", "references/models/model-image-seedream-4.md"),
        ("model-image-flux-pro.md", "references/models/model-image-flux-pro.md"),
    ],
    "art-direction": [
        ("reference-craft-artdept.md", "references/reference-craft-artdept.md"),
        ("guide-art-direction.md", "references/guide-art-direction.md"),
        ("guide-asset-reference.md", "references/guide-asset-reference.md"),
        ("guide-color-story.md", "references/guide-color-story.md"),
        ("guide-image-editing.md", "references/guide-image-editing.md"),
        ("model-currency-2026-06.md", "references/model-currency-2026-06.md"),
        ("model-editing-flux-kontext.md", "references/models/model-editing-flux-kontext.md"),
        ("model-image-gemini-flash.md", "references/models/model-image-gemini-flash.md"),
        ("model-image-seedream-4.md", "references/models/model-image-seedream-4.md"),
        ("model-image-flux-pro.md", "references/models/model-image-flux-pro.md"),
    ],
}

EXCLUDE_NAMES = {".DS_Store"}
EXCLUDE_SUFFIXES = (".skill",)
EXCLUDE_RELPATHS = {"references/models/model-currency-2026-06.md"}


def sync():
    for skill, pairs in MANIFEST.items():
        for src_rel, dst_rel in pairs:
            dst = SKILLS / skill / dst_rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(CTX / src_rel, dst)
            print("sync  %s: %s -> %s" % (skill, src_rel, dst_rel))


def is_packable(path, root):
    if path.name in EXCLUDE_NAMES:
        return False
    if path.suffix in EXCLUDE_SUFFIXES:
        return False
    if any(part.startswith(".fuse_hidden") for part in path.parts):
        return False
    if path.relative_to(root).as_posix() in EXCLUDE_RELPATHS:
        return False
    return True


def zip_skills():
    DIST.mkdir(parents=True, exist_ok=True)
    for skill in MANIFEST:
        root = SKILLS / skill
        out = DIST / (skill + ".skill")
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
            for p in sorted(root.rglob("*")):
                if p.is_file() and is_packable(p, root):
                    z.write(p, p.relative_to(root))
        print("zip   %s  (%d bytes)" % (out.relative_to(REPO), out.stat().st_size))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--sync", action="store_true")
    ap.add_argument("--zip", action="store_true")
    a = ap.parse_args()
    do_all = not (a.sync or a.zip)
    if a.sync or do_all:
        sync()
    if a.zip or do_all:
        zip_skills()
