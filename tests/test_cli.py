import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PYTHON = "/opt/anaconda3/bin/python"


class CliTests(unittest.TestCase):
    def run_cli(self, *args):
        env = os.environ.copy()
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        return subprocess.run(
            [PYTHON, str(ROOT / "scripts/pacs.py"), *args],
            cwd=ROOT,
            env=env,
            text=True,
            capture_output=True,
            check=True,
        )

    def test_cli_initializes_and_audits_project(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "demo-project"
            target.mkdir()

            self.run_cli("init-project", "--target", str(target))
            result = self.run_cli("audit", "--target", str(target), "--json")

            payload = json.loads(result.stdout)
            self.assertTrue(payload["ok"])
            self.assertEqual("project", payload["mode"])

    def test_cli_routes_candidate_context(self):
        result = self.run_cli(
            "route",
            "--text",
            "For this project, always run make verify before completion.",
        )

        payload = json.loads(result.stdout)
        self.assertEqual("project_rules", payload["bucket"])
        self.assertTrue(payload["safe_to_sync"])


if __name__ == "__main__":
    unittest.main()
