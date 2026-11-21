"""Portable skill metadata and distribution consistency tests.

PyYAML is a dev-only dependency; plugin installation has no Python runtime dependency.
"""
import unittest
from pathlib import Path

import yaml

from scripts.build_plugin import ROOT, parse_frontmatter


class SkillIntegrityTests(unittest.TestCase):
    def test_both_skill_frontmatters_are_valid_yaml(self):
        for path in ("interrogation/SKILL.md", "skills/interrogation/SKILL.md"):
            with self.subTest(path=path):
                raw = (ROOT / path).read_bytes()
                data = yaml.safe_load(parse_frontmatter(raw))
                self.assertIsInstance(data, dict)
                self.assertEqual(data.get("name"), "interrogation")
                self.assertIsInstance(data.get("description"), str)
                self.assertTrue(data["description"].strip())

    def test_both_skill_copies_are_identical(self):
        self.assertEqual(
            (ROOT / "interrogation/SKILL.md").read_bytes(),
            (ROOT / "skills/interrogation/SKILL.md").read_bytes(),
        )
        self.assertEqual(
            (ROOT / "interrogation/agents/openai.yaml").read_bytes(),
            (ROOT / "skills/interrogation/agents/openai.yaml").read_bytes(),
        )

    def test_codex_metadata_yaml(self):
        path = ROOT / "interrogation/agents/openai.yaml"
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        self.assertIsInstance(data, dict)
        self.assertTrue(data["interface"]["display_name"].strip())
        self.assertTrue(data["interface"]["default_prompt"].strip())
        self.assertIs(data["policy"]["allow_implicit_invocation"], False)

    def test_approval_gate_in_skill(self):
        skill = (ROOT / "interrogation/SKILL.md").read_text(encoding="utf-8")
        for marker in ("INTERROGATION_LOCKED", "AWAITING_APPROVAL", "mode=auto", "Light", "Standard", "Deep"):
            with self.subTest(marker=marker):
                self.assertIn(marker, skill)
        self.assertIn("Утверждаю ТЗ, приступай к реализации", skill)

    def test_invalid_yaml_is_rejected(self):
        with self.assertRaises(yaml.YAMLError):
            yaml.safe_load("name: [invalid yaml")


if __name__ == "__main__":
    unittest.main()
