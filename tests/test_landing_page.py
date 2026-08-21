from __future__ import annotations

import unittest
from html.parser import HTMLParser
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
LANDING_PAGE = PROJECT_ROOT / "docs" / "index.html"
PAGES_WORKFLOW = PROJECT_ROOT / ".github" / "workflows" / "pages.yml"


class VisibleTextCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        text = data.strip()
        if text:
            self.parts.append(text)


class LandingPageTests(unittest.TestCase):
    def test_landing_page_has_complete_conversion_path(self) -> None:
        self.assertTrue(LANDING_PAGE.exists(), "landing page is missing")
        html = LANDING_PAGE.read_text(encoding="utf-8")

        self.assertIn("中文 Markdown 一键转 Word", html)
        self.assertIn("releases/latest", html)
        self.assertIn("issues/new?template=custom-template.yml", html)
        self.assertIn("mailto:1066536086@qq.com", html)
        self.assertIn('property="og:image"', html)
        self.assertIn('name="viewport"', html)

        visible_text = VisibleTextCollector()
        visible_text.feed(html)
        self.assertIn("99 元", " ".join(visible_text.parts))

    def test_landing_page_local_assets_exist(self) -> None:
        for asset in ("styles.css", "word-preview.png", "og.png"):
            with self.subTest(asset=asset):
                self.assertTrue((PROJECT_ROOT / "docs" / asset).exists())

    def test_pages_workflow_uses_official_deployment_actions(self) -> None:
        self.assertTrue(PAGES_WORKFLOW.exists(), "Pages workflow is missing")
        workflow = PAGES_WORKFLOW.read_text(encoding="utf-8")

        self.assertIn("pages: write", workflow)
        self.assertIn("id-token: write", workflow)
        self.assertIn("actions/configure-pages@v5", workflow)
        self.assertIn("actions/upload-pages-artifact@v4", workflow)
        self.assertIn("actions/deploy-pages@v4", workflow)


if __name__ == "__main__":
    unittest.main()
