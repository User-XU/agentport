import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from init_machine import init_machine
from init_project import copy_project_template


class InitProjectTests(unittest.TestCase):
    def test_machine_init_copies_root_agent_entry(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "machine-context"
            target.mkdir()

            result = init_machine(target)

            self.assertIn(str(target / "agent-entry/instructions/agent-rules.md"), result["created"])
            self.assertTrue((target / "agent-entry/init/new-machine-agent-init.md").exists())
            self.assertTrue((target / "agent-entry/memories/MEMORY.md").exists())

    def test_project_template_creates_required_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "demo-project"
            target.mkdir()

            result = copy_project_template(target)

            self.assertIn(str(target / "AGENTS.md"), result["created"])
            self.assertTrue((target / ".agent-context/rules/project-rules.md").exists())
            self.assertTrue((target / ".agent-context/memory/PROJECT_MEMORY.md").exists())
            self.assertTrue((target / ".agent-context/private/README.md").exists())

    def test_project_template_does_not_overwrite_by_default(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "demo-project"
            target.mkdir()
            agents = target / "AGENTS.md"
            agents.write_text("custom", encoding="utf-8")

            result = copy_project_template(target)

            self.assertIn(str(agents), result["skipped"])
            self.assertEqual("custom", agents.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
