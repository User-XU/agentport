import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from evolve_memory import classify_text


class EvolveMemoryTests(unittest.TestCase):
    def test_routes_project_rule(self):
        route = classify_text("For this project, always run make verify before completion.")

        self.assertEqual("project_rules", route.bucket)
        self.assertTrue(route.safe_to_sync)

    def test_routes_public_memory(self):
        route = classify_text("The user prefers concise collaboration updates.")

        self.assertEqual("public_memory", route.bucket)
        self.assertTrue(route.safe_to_sync)

    def test_routes_sensitive_context_to_private(self):
        field = "_".join(("api", "key"))
        token = "sk-proj-" + "abcdefghijklmnopqrstuvwxyz"
        route = classify_text(f"{field} = '{token}'")

        self.assertEqual("private_state", route.bucket)
        self.assertFalse(route.safe_to_sync)

    def test_empty_candidate_is_discarded(self):
        route = classify_text("   ")

        self.assertEqual("discard", route.bucket)
        self.assertFalse(route.safe_to_sync)


if __name__ == "__main__":
    unittest.main()
