"""Ensure the generated upload ZIP includes only the expected public payload."""
import json
import unittest
import zipfile

from scripts.build_plugin import REQUIRED, ROOT, build, validate


class PluginArchiveTests(unittest.TestCase):
    def test_plugin_metadata_can_be_validated(self):
        plugin = validate()
        self.assertEqual(plugin["name"], "agent-interrogation")
        self.assertEqual(plugin["license"], "MIT")

    def test_generated_zip_contents_and_crc(self):
        path = build()
        self.assertTrue(path.is_file())
        with zipfile.ZipFile(path) as archive:
            self.assertCountEqual(archive.namelist(), REQUIRED)
            self.assertIsNone(archive.testzip())
            self.assertEqual(
                archive.read("skills/interrogation/SKILL.md"),
                (ROOT / "interrogation/SKILL.md").read_bytes(),
            )
            manifest = json.loads(archive.read("plugin.json"))
            self.assertEqual(manifest["name"], "agent-interrogation")

    def test_no_secrets_or_dev_files_in_upload(self):
        self.assertNotIn(".env", REQUIRED)
        self.assertNotIn("tests/test_plugin_archive.py", REQUIRED)
        self.assertNotIn("scripts/build_plugin.py", REQUIRED)
        self.assertTrue(all(not path.startswith("/") and ".." not in path.split("/") for path in REQUIRED))


if __name__ == "__main__":
    unittest.main()
