#!/usr/bin/env python3
"""Assemble the generative-cinema plugin from the repo's canonical sources.

The repo root holds the source of truth: `context/` (the library) and
`skills/*/SKILL.md` (the seven skills, with bundled `references/`). This script
regenerates the plugin's single shared library and repoints every skill reference
at `${CLAUDE_PLUGIN_ROOT}/context/...` so there is no per-skill duplication.

Authored by hand (not touched here): plugin/.claude-plugin/plugin.json,
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

SKILLS = ["project-context", "sequence-design", "shot-prompt", "model-docs", "footage-transform", "image-edit", "character-sheet"]

HELPERS = [
    SKILLS_SRC / "project-context/references/questioning-framework.md",
    SKILLS_SRC / "project-context/references/output-template.md",
    SKILLS_SRC / "shot-prompt/references/model-layer-priority.md",
    SKILLS_SRC / "shot-prompt/references/output-examples.md",
    SKILLS_SRC / "model-docs/references/model-doc-template.md",
    SKILLS_SRC / "model-docs/references/example-model-doc.md",
    SKILLS_SRC / "character-sheet/references/character-template.md",
]

LINK_RE = re.compile(r"\]\(references/(?:models/)?([^)]*)\)")
ROOT = "${CLAUDE_PLUGIN_ROOT}/context/"
AGENT_REQUIRED = {"name", "description", "model", "color", "tools"}


def repoint(md):
    return LINK_RE.sub(lambda m: "](" + ROOT + m.group(1) + ")", md)


def sync_context():
    CTX_OUT.mkdir(parents=True, exist_ok=True)
    for f in sorted(CTX_SRC.glob("*.md")):
        shutil.copyfile(f, CTX_OUT / f.name)
    for h in HELPERS:
        if not h.exists():
            sys.exit("missing helper source: %s" % h)
        shutil.copyfile(h, CTX_OUT / h.name)
    print("context/: %d files" % len(list(CTX_OUT.glob("*.md"))))


def sync_skills():
    for name in SKILLS:
        src = SKILLS_SRC / name / "SKILL.md"
        out_dir = SKILLS_OUT / name
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "SKILL.md").write_text(repoint(src.read_text(encoding="utf-8")), encoding="utf-8")
        print("skill: %s" % name)


def validate():
    ok = True
    pj = PLUGIN / ".claude-plugin" / "plugin.json"
    try:
        meta = json.load(open(pj))
        assert re.fullmatch(r"[a-z0-9-]+", meta["name"]), "name not kebab-case"
    except Exception as e:
        print("FAIL plugin.json:", e); ok = False
    for name in SKILLS:
        sk = SKILLS_OUT / name / "SKILL.md"
        if not sk.exists():
            print("FAIL missing skill:", name); ok = False; continue
        body = sk.read_text(encoding="utf-8")
        for ref in re.findall(r"\]\((\$\{CLAUDE_PLUGIN_ROOT\}/[^)]+)\)", body):
            rel = ref.replace("${CLAUDE_PLUGIN_ROOT}/", "")
            if rel.endswith("/"):
                continue
            if not (PLUGIN / rel).exists():
                print("FAIL %s: missing %s" % (name, rel)); ok = False
        if "](references/" in body:
            print("FAIL %s: stale references/ path remains" % name); ok = False
    # agents: frontmatter must be strict-YAML-parseable (no raw <example> tags)
    # with the required keys. The plugin loader parses this as strict YAML.
    for a in sorted((PLUGIN / "agents").glob("*.md")):
        m = re.match(r"---\n(.*?)\n---\n", a.read_text(encoding="utf-8"), re.S)
        if not m:
            print("FAIL agent (no frontmatter):", a.name); ok = False; continue
        keys = set()
        for line in m.group(1).splitlines():
            if not line.strip() or line[0] in " \t":
                continue
            if line.lstrip().startswith("<") or ":" not in line.split("#")[0]:
                print("FAIL %s: non-YAML frontmatter line: %r" % (a.name, line)); ok = False
            else:
                keys.add(line.split(":", 1)[0].strip())
        missing = AGENT_REQUIRED - keys
        if missing:
            print("FAIL %s: missing keys %s" % (a.name, sorted(missing))); ok = False
    print("VALIDATE: OK" if ok else "VALIDATE: ERRORS")
    return ok


def package():
    dest = REPO / "generative-cinema.plugin"
    if dest.exists():
        dest.unlink()
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(PLUGIN.rglob("*")):
            if p.is_file() and p.name != "assemble.py" and not p.name.endswith(".plugin"):
                if any(part.startswith(".fuse_hidden") for part in p.parts):
                    continue
                z.write(p, p.relative_to(PLUGIN))
    print("packaged: %s (%d bytes)" % (dest, dest.stat().st_size))


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
