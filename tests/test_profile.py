import unittest
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).parents[1]
README = ROOT / "README.md"
HERO = ROOT / "assets" / "ai-systems-lab.gif"


class ProfileContractTest(unittest.TestCase):
    def test_readme_contains_identity_and_sections(self):
        self.assertTrue(README.exists(), "README.md must exist")
        text = README.read_text(encoding="utf-8")
        required = [
            "AI SYSTEMS LAB",
            "SYSTEM PROFILE",
            "CURRENT SIGNALS",
            "PROJECT MATRIX",
            "TECH STACK",
            "https://github.com/aiis2/datell",
            "https://github.com/aiis2/risk-agent",
            "https://github.com/aiis2/frontend-design-report",
        ]
        self.assertTrue(all(item in text for item in required))

    def test_hero_is_repository_hosted_and_bounded(self):
        self.assertTrue(HERO.exists(), "animated hero must exist")
        self.assertLess(HERO.stat().st_size, 5_000_000)
        with Image.open(HERO) as image:
            self.assertEqual(image.size, (1200, 420))
            self.assertTrue(image.is_animated)


if __name__ == "__main__":
    unittest.main()
