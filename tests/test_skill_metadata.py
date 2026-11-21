"""Parse the skill's YAML with a real parser during release checks."""

import unittest

import yaml

from scripts.build_plugin import ROOT, parse_frontmatter


SKILL_DIRS = ("interrogation", "skills/interrogation")


class SkillMetadataTests(unittest.TestCase):
    def test_skill_frontmatter_is_valid_yaml(self):
        for skill_dir in SKILL_DIRS:
            path = ROOT / skill_dir / "SKILL.md"
            with self.subTest(path=path.relative_to(ROOT)):
                header = parse_frontmatter(path.read_bytes())
                metadata = yaml.safe_load(header)
                self.assertIsInstance(metadata, dict)
                mapping = yaml.compose(header, Loader=yaml.SafeLoader)
                self.assertEqual(len(mapping.value), len(metadata), "Repeated frontmatter key")
                self.assertEqual(metadata.get("name"), "interrogation")
                description = metadata.get("description")
                self.assertIsInstance(description, str)
                self.assertTrue(description.strip())

    def test_codex_metadata_requires_explicit_invocation(self):
        for skill_dir in SKILL_DIRS:
            path = ROOT / skill_dir / "agents" / "openai.yaml"
            with self.subTest(path=path.relative_to(ROOT)):
                metadata = yaml.safe_load(path.read_text(encoding="utf-8"))
                self.assertIsInstance(metadata, dict)
                policy = metadata.get("policy")
                self.assertIsInstance(policy, dict)
                self.assertIs(policy.get("allow_implicit_invocation"), False)
