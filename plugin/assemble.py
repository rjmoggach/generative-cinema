#!/usr/bin/env python3
"""Assemble the generative-cinema plugin from the repo's canonical sources.

The repo root holds the source of truth: `context/` (the library) and
`skills/*/SKILL.md` (the four skills, with bundled `references/`). This script
regenerates the plugin's single shared library and repoints every skill reference
at `${CLAUDE_PLUGIN_ROOT}/context/...` so there is no per-skill duplication.

Authored-by-hand (not touched here): plugin/.claude-plugin/plugin.json,
plugin/agents/*.md, plugin/README.md.

Usage:
    python plugin/assemble.py             # sync context/ + skills/, then validate
    python plugin/assemble.py --package   # also build the .plugin archive
"""
from __future__ import annotations
import argparse, json, re, shutil, sys, zipfile
from pathlib import Path

PLUGIN = Path(__file__).resolve().parent
REPO = PLUGIN.parent
CTX_SRC = REPO / "context"
SKILLS_SRC = REPO / "skills"
CTX_OUT = PLUGIN / "context"
SKILLS_OUT = PLUGIN / "skills"

SKILLS = ["project-context", "sequence-design", "shot-prompt", "model-docs"]

# Helper files that live only inside the source skills' references/ (not in context/).
# Copied into the shared plugin context/ under the SAME basename the SKILL.md uses.
HELPERS = [
    SKILLS_SRC / "project-context/references/questioning-framework.md",
    SKILLS_SRC / "project-context/references/output-template.md",
    SKILLS_SRC / "shot-prompt/references/model-layer-priority.md",
    SKILLS_SRC / "shot-prompt/references/output-examples.md",
    SKILLS_SRC / "model-docs/references/model-doc-template.md",
    SKILLS_SRC / "model-docs/references/example-model-doc.md",
]

# Rewrite any markdown ref into the shared plugin context, dropping subdirs.
#   ](references/models/foo.md)  ->  ](${CLAUDE_PLUGIN_ROOT}/context/foo.md)
#   ](references/foo.md)         ->  ](${CLAUDE_PLUGIN_ROOT}/context/foo.md)
#   ](references/models/)        ->  ](${CLAUDE_PLUGIN_ROOT}/context/)
LINK_RE = re.compile(r"\]\(references/(?:models/)?([^)]*)\)")
ROOT = "${CLAUDE_PLUGIN_ROOT}/context/"


def repoint(md: str) -> str:
    return LINK_RE.sub(lambda m: "](" + ROOT + m.group(1) + ")", md)


def sync_context():
    CTX_OUT.mkdir(parents=True, exist_ok=True)
    for f in sorted(CTX_SRC.glob("*.md")):
        shutil.copyfile(f, CTX_OUT / f.name)
    for h in HELPERS:
        if not h.exists():
            sys.exit(f"missing helper source: {h}")
        shutil.copyfile(h, CTX_OUT / h.name)
    print(f"context/: {len(list(CTX_OUT.glob('*.md')))} files")


def sync_skills():
    for name in SKILLS:
        src = SKILLS_SRC / name / "SKILL.md"
        out_dir = SKILLS_OUT / name
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "SKILL.md").write_text(repoint(src.read_text(encoding="utf-8")), encoding="utf-8")
        print(f"skill: {name}")


def validate():
    ok = True
    # plugin.json
    pj = PLUGIN / ".claude-plugin" / "plugin.json"
    try:
        meta = json.load(open(pj))
        assert re.fullmatch(r"[a-z0-9-]+", meta["name"]), "name not kebab-case"
    except Exception as e:
        print("FAIL plugin.json:", e); ok = False
    # skills present + links resolve inside the package
    for name in SKILLS:
        sk = SKILLS_OUT / name / "SKILL.md"
        if not sk.exists():
            print("FAIL missing skill:", name); ok = False; continue
        for ref in re.findall(r"\]\((\$\{CLAUDE_PLUGIN_ROOT\}/[^)]+)\)", sk.read_text(encoding="utf-8")):
            rel = ref.replace("${CLAUDE_PLUGIN_ROOT}/", "")
            target = PLUGIN / rel
            # a bare directory ref (…/context/) is fine
            if rel.endswith("/"):
                continue
            if not target.exists():
                print(f"FAIL {name}: missing {rel}"); ok = False
        # no stale references/ paths left
        if "](references/" in sk.read_text(encoding="utf-8"):
            print(f"FAIL {name}: stale references/ path remains"); ok = False
    # agents parse
    for a in sorted((PLUGIN / "agents").glob("*.md")):
        t = a.read_text(encoding="utf-8")
        if not t.startswith("---"):
            print("FAIL agent frontmatter:", a.name); ok = False
    print("VALIDATE: OK" if ok else "VALIDATE: ERRORS")
    return ok


def package():
    tmp = Path("/tmp/generative-cinema.plugin")
    if tmp.exists():
        tmp.unlink()
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(PLUGIN.rglob("*")):
            if p.is_file() and p.name != "assemble.py" and not p.name.endswith(".plugin"):
                if any(part.startswith(".fuse_hidden") for part in p.parts):
                    continue
                z.write(p, p.relative_to(PLUGIN))
    out_dir = Path("/sessions/confident-funny-curie/mnt/outputs")
    dest = out_dir / "generative-cinema.plugin"
    shutil.copyfile(tmp, dest)
    print(f"packaged: {dest} ({dest.stat().st_size} bytes)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--package", action="store_true")
    a = ap.parse_args()
    sync_context()
    sync_skills()
    ok = validate()
    if a.package and ok:
        package()
    sys.exit(0 if ok else 1)
