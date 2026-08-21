from __future__ import annotations

import tomllib
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RELEASE_WORKFLOW = PROJECT_ROOT / ".github" / "workflows" / "release.yml"


class ReleaseConfigurationTests(unittest.TestCase):
    def test_project_version_is_next_public_release(self) -> None:
        pyproject = tomllib.loads(
            (PROJECT_ROOT / "pyproject.toml").read_text(encoding="utf-8")
        )

        self.assertEqual(pyproject["project"]["version"], "0.1.1")

    def test_release_workflow_builds_and_publishes_tagged_packages(self) -> None:
        self.assertTrue(RELEASE_WORKFLOW.exists(), "release workflow is missing")
        workflow = RELEASE_WORKFLOW.read_text(encoding="utf-8")

        self.assertIn('tags: ["v*"]', workflow)
        self.assertIn("contents: write", workflow)
        self.assertIn("python -m build", workflow)
        self.assertIn("gh release create", workflow)


if __name__ == "__main__":
    unittest.main()
