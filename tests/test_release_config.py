from __future__ import annotations

import unittest
from pathlib import Path

import tomllib

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RELEASE_WORKFLOW = PROJECT_ROOT / ".github" / "workflows" / "release.yml"
TESTS_WORKFLOW = PROJECT_ROOT / ".github" / "workflows" / "tests.yml"


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

    def test_pypi_metadata_points_to_the_public_product(self) -> None:
        pyproject = tomllib.loads(
            (PROJECT_ROOT / "pyproject.toml").read_text(encoding="utf-8")
        )
        project = pyproject["project"]

        self.assertEqual(project.get("license"), "MIT")
        authors = project.get("authors", [{}])
        self.assertEqual(authors[0].get("name"), "codex2026-user")
        self.assertEqual(authors[0].get("email"), "1066536086@qq.com")
        self.assertIn("markdown", project.get("keywords", []))
        urls = project.get("urls", {})
        self.assertEqual(
            urls.get("Homepage"),
            "https://codex2026-user.github.io/md2docx-cn/",
        )
        self.assertEqual(
            urls.get("Source"),
            "https://github.com/codex2026-user/md2docx-cn",
        )

    def test_tests_workflow_checks_lint(self) -> None:
        workflow = TESTS_WORKFLOW.read_text(encoding="utf-8")

        self.assertIn('python -m pip install -e ".[dev]"', workflow)
        self.assertIn("python -m ruff check .", workflow)


if __name__ == "__main__":
    unittest.main()
