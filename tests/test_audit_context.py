import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from audit_context import audit
from init_project import copy_project_template


class AuditContextTests(unittest.TestCase):
    def test_audit_passes_after_project_init(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "demo-project"
            target.mkdir()
            copy_project_template(target)

            result = audit(target, "project")

            self.assertTrue(result["ok"])
            self.assertEqual([], result["issues"])

    def test_audit_detects_missing_required_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)

            result = audit(target, "project")

            self.assertFalse(result["ok"])
            kinds = {issue["kind"] for issue in result["issues"]}
            self.assertIn("missing_required_file", kinds)

    def test_auto_mode_prefers_project_when_both_entries_exist(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "demo-project"
            target.mkdir()
            copy_project_template(target)
            (target / "agent-entry/instructions").mkdir(parents=True)

            result = audit(target, "auto")

            self.assertEqual("project", result["mode"])

    def test_audit_detects_possible_secret_outside_private(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "demo-project"
            target.mkdir()
            copy_project_template(target)
            field = "_".join(("api", "key"))
            token = "sk-proj-" + "abcdefghijklmnopqrstuvwxyz"
            (target / "notes.md").write_text(f"{field} = '{token}'", encoding="utf-8")

            result = audit(target, "project")

            self.assertFalse(result["ok"])
            self.assertTrue(any(issue["kind"] == "possible_secret" for issue in result["issues"]))


if __name__ == "__main__":
    unittest.main()
