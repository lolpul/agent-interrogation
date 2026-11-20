#!/usr/bin/env python3
"""Validate the skills-only plugin and build a minimal submission ZIP.

This performs structural checks only; behavioral checks require running an agent.
No dependencies beyond Python's standard library.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = [
    "plugin.json",
    ".codex-plugin/plugin.json",
    "skills/interrogation/SKILL.md",
    "skills/interrogation/agents/openai.yaml",
    "assets/interrogation.svg",
    "LICENSE",
]


def validate() -> dict:
    errors = []
    for path in REQUIRED:
        if not (ROOT / path).is_file():
            errors.append(f"Missing: {path}")
    if errors:
        raise ValueError("\n".join(errors))

    plugin = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
    overlay = json.loads((ROOT / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
    ext = plugin.get("extensions", {}).get("com.openai", {})
    interface = ext.get("interface", {})
    if plugin.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        errors.append("Invalid portable plugin schema declaration")
    if plugin.get("name") != "agent-interrogation":
        errors.append("Unexpected plugin identifier")
    if not re.fullmatch(r"\d+\.\d+\.\d+", plugin.get("version", "")):
        errors.append("Plugin version must be semver")
    for field in ("name", "version", "description", "author", "homepage", "repository", "license"):
        if overlay.get(field) != plugin.get(field):
            errors.append(f"Manifest field differs: {field}")
    if overlay.get("interface") != interface:
        errors.append("OpenAI presentation metadata differs between manifests")
    if overlay.get("skills") != "./skills/":
        errors.append("Codex compatibility manifest must point to ./skills/")
    for field, limit in [
        ("displayName", 30), ("shortDescription", 30),
        ("longDescription", 4000), ("developerName", 80)
    ]:
        value = interface.get(field)
        if not isinstance(value, str) or not 0 < len(value) <= limit:
            errors.append(f"Invalid interface.{field}")
    for field in ("category", "capabilities"):
        if not interface.get(field):
            errors.append(f"Missing interface.{field}")
    for icon_field in ("logo", "composerIcon"):
        value = interface.get(icon_field, "")
        if not value.startswith("./") or ".." in Path(value).parts:
            errors.append(f"Invalid {icon_field} path")
        elif not (ROOT / value[2:]).is_file():
            errors.append(f"{icon_field} file missing")
    svg = ET.parse(ROOT / "assets/interrogation.svg").getroot()
    try:
        x, y, w, h = [float(n) for n in svg.attrib["viewBox"].split()]
        if w != h or w < 48:
            errors.append("SVG viewBox must be square and at least 48px")
    except (ValueError, KeyError):
        errors.append("Invalid SVG viewBox")
    canonical = (ROOT / "interrogation/SKILL.md").read_bytes()
    distributed = (ROOT / "skills/interrogation/SKILL.md").read_bytes()
    if canonical != distributed:
        errors.append("Packaged SKILL.md is out of sync with interrogation/SKILL.md")
    if (ROOT / "interrogation/agents/openai.yaml").read_bytes() != (
        ROOT / "skills/interrogation/agents/openai.yaml"
    ).read_bytes():
        errors.append("Packaged Codex metadata differs from original")
    if not distributed.startswith(b"---\n"):
        errors.append("SKILL.md is missing YAML frontmatter")
    header = distributed.split(b"---", 2)[1].decode("utf-8", errors="replace")
    if not re.search(r"(?m)^name:\s*interrogation\s*$", header):
        errors.append("SKILL.md must declare name: interrogation")
    if not re.search(r"(?m)^description:\s*\S+", header):
        errors.append("SKILL.md must declare a description")
    if errors:
        raise ValueError("\n".join(errors))
    return plugin


def build() -> Path:
    plugin = validate()
    out = ROOT / "dist" / f"agent-interrogation-{plugin['version']}.zip"
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for relative_path in REQUIRED:
            z.write(ROOT / relative_path, arcname=relative_path)
    with zipfile.ZipFile(out) as z:
        if sorted(z.namelist()) != sorted(REQUIRED):
            raise ValueError("Archive entries do not match the package manifest")
        if z.testzip() is not None:
            raise ValueError("ZIP CRC check failed")
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Validate only; do not write a ZIP")
    args = parser.parse_args()
    try:
        info = validate()
        print(f"PASS: skill-only package {info['name']} v{info['version']}")
        if not args.check:
            print(f"Built: {build()}")
    except (ValueError, OSError, json.JSONDecodeError, ET.ParseError) as err:
        print(f"FAIL: {err}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
