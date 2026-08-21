from __future__ import annotations

import re
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DOCS = PROJECT_ROOT / "docs"
GUIDE_URL = "https://codex2026-user.github.io/md2docx-cn/markdown-to-word.html"


class SearchAcquisitionTests(unittest.TestCase):
    def test_guide_answers_search_intent_and_links_to_product(self) -> None:
        guide = (DOCS / "markdown-to-word.html").read_text(encoding="utf-8")

        self.assertIn("Markdown 转 Word", guide)
        self.assertIn("releases/latest", guide)
        self.assertIn("word-preview.png", guide)
        self.assertIn('rel="canonical"', guide)

    def test_site_navigation_and_sitemap_include_guide(self) -> None:
        home = (DOCS / "index.html").read_text(encoding="utf-8")
        sitemap = (DOCS / "sitemap.xml").read_text(encoding="utf-8")

        self.assertIn("markdown-to-word.html", home)
        self.assertIn(GUIDE_URL, sitemap)

    def test_indexnow_key_file_is_valid(self) -> None:
        key_files = [
            path
            for path in DOCS.glob("*.txt")
            if re.fullmatch(r"[a-f0-9]{32}\.txt", path.name)
        ]

        self.assertEqual(len(key_files), 1)
        self.assertEqual(key_files[0].stem, key_files[0].read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    unittest.main()
