from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest


def cli_main():
    try:
        from md2docx_cn.cli import main
    except ImportError as exc:
        raise AssertionError(f"CLI is not implemented: {exc}") from exc
    return main


class CliTests(unittest.TestCase):
    def test_cli_converts_markdown_and_reports_output(self):
        main = cli_main()
        with TemporaryDirectory() as directory:
            temp_dir = Path(directory)
            source = temp_dir / "input.md"
            output = temp_dir / "output.docx"
            source.write_text("# 标题\n\n正文", encoding="utf-8")
            stdout = StringIO()

            with redirect_stdout(stdout):
                exit_code = main(
                    [str(source), "-o", str(output), "--author", "作者"]
                )

            self.assertEqual(exit_code, 0)
            self.assertTrue(output.exists())
            self.assertIn(str(output), stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
