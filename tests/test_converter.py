import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from docx import Document


def converter_api():
    try:
        from md2docx_cn.converter import convert_markdown, parse_markdown
    except ImportError as exc:
        raise AssertionError(f"converter API is not implemented: {exc}") from exc
    return convert_markdown, parse_markdown


class ConverterTests(unittest.TestCase):
    def test_parse_markdown_recognizes_common_article_blocks(self):
        _, parse_markdown = converter_api()
        blocks = parse_markdown(
            "# 示例标题\n\n正文第一段。\n\n## 方法\n\n- 项目一\n- 项目二\n"
        )

        self.assertEqual(
            [(block.kind, block.text, block.level) for block in blocks],
            [
                ("heading", "示例标题", 1),
                ("paragraph", "正文第一段。", 0),
                ("heading", "方法", 2),
                ("bullet", "项目一", 0),
                ("bullet", "项目二", 0),
            ],
        )

    def test_convert_markdown_creates_a_readable_word_document(self):
        convert_markdown, _ = converter_api()
        with TemporaryDirectory() as directory:
            temp_dir = Path(directory)
            source = temp_dir / "article.md"
            output = temp_dir / "article.docx"
            source.write_text(
                "# 示例标题\n\n这是正文。\n\n- 第一项\n", encoding="utf-8"
            )

            result = convert_markdown(source, output, author="测试作者")

            self.assertEqual(result, output)
            self.assertTrue(output.exists())
            document = Document(output)
            self.assertEqual(
                [p.text for p in document.paragraphs if p.text],
                ["示例标题", "这是正文。", "第一项"],
            )
            self.assertEqual(document.core_properties.author, "测试作者")
            self.assertEqual(document.styles["Normal"].font.name, "SimSun")

    def test_parse_markdown_recognizes_numbered_steps_and_quotes(self):
        _, parse_markdown = converter_api()

        blocks = parse_markdown("1. 打开文件\n2. 执行转换\n\n> 适合中文文章。")

        self.assertEqual(
            [(block.kind, block.text) for block in blocks],
            [
                ("numbered", "打开文件"),
                ("numbered", "执行转换"),
                ("quote", "适合中文文章。"),
            ],
        )

    def test_convert_markdown_rejects_missing_source(self):
        convert_markdown, _ = converter_api()
        with TemporaryDirectory() as directory:
            temp_dir = Path(directory)
            with self.assertRaisesRegex(FileNotFoundError, "Markdown source not found"):
                convert_markdown(temp_dir / "missing.md", temp_dir / "out.docx")


if __name__ == "__main__":
    unittest.main()
