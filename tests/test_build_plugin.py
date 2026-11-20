#!/usr/bin/env python3
"""Regression tests for the plugin packager; standard library only."""
import runpy
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
builder = runpy.run_path(str(ROOT / "scripts" / "build_plugin.py"))
parse_frontmatter = builder["parse_frontmatter"]
validate = builder["validate"]


class FrontmatterTests(unittest.TestCase):
    def test_lf(self):
        header = parse_frontmatter(b'---\nname: interrogation\ndescription: test\n---\nBody')
        self.assertIn("name: interrogation", header)

    def test_crlf_windows_checkout(self):
        header = parse_frontmatter(b'---\r\nname: interrogation\r\ndescription: test\r\n---\r\nBody')
        self.assertIn("description: test", header)

    def test_utf8_bom_and_crlf(self):
        header = parse_frontmatter(b'\xef\xbb\xbf---\r\nname: interrogation\r\n---\r\n')
        self.assertIn("name: interrogation", header)

    def test_missing_frontmatter(self):
        with self.assertRaisesRegex(ValueError, "missing YAML frontmatter"):
            parse_frontmatter(b"# Skill description\n")

    def test_real_repository_checkout(self):
        info = validate()
        self.assertEqual(info["name"], "agent-interrogation")


if __name__ == "__main__":
    unittest.main()
