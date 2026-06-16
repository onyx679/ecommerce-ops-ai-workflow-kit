import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PortfolioPageTest(unittest.TestCase):
    def test_pages_default_to_english(self):
        html = (ROOT / "docs" / "index.html").read_text(encoding="utf-8")

        self.assertIn('<html lang="en">', html)
        self.assertIn('class="language-button active" data-lang="en"', html)
        self.assertIn('setLanguage("en");', html)

    def test_chinese_language_option_is_available(self):
        html = (ROOT / "docs" / "index.html").read_text(encoding="utf-8")

        self.assertIn('data-lang="zh"', html)
        self.assertIn('data-zh="一个使用模拟数据的作品集项目', html)
        self.assertIn("中文 README", html)

    def test_page_surfaces_evidence_validator_and_current_test_count(self):
        html = (ROOT / "docs" / "index.html").read_text(encoding="utf-8")

        self.assertIn("scripts/verify_evidence.py", html)
        self.assertIn("Evidence validator", html)
        self.assertIn("<div><dt>7</dt>", html)
