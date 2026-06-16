import tempfile
import unittest
from pathlib import Path

from ecom_ops.evidence import render_pretty, validate_evidence_file


ROOT = Path(__file__).resolve().parents[1]


class EvidenceValidationTest(unittest.TestCase):
    def test_current_evidence_matrix_references_existing_files_and_boundaries(self):
        result = validate_evidence_file(ROOT / "EVIDENCE.md", ROOT)

        self.assertTrue(result.ok)
        self.assertIn("README.md", result.checked_references)
        self.assertIn("scripts/ecom_ops_report.py", result.checked_references)
        self.assertIn("examples/weekly-ops-report.md", result.checked_references)

    def test_missing_referenced_file_fails_validation(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            evidence = root / "EVIDENCE.md"
            evidence.write_text(
                "\n".join(
                    [
                        "`missing.md`",
                        "Do not describe it as a real merchant project.",
                        "Do not claim real customer, merchant, or platform export data.",
                        "Do not claim production deployment.",
                        "Do not imply external adoption or review.",
                        "AI output is limited to draft preparation and risk surfacing.",
                    ]
                ),
                encoding="utf-8",
            )

            result = validate_evidence_file(evidence, root)

        self.assertFalse(result.ok)
        self.assertIn("missing referenced evidence path: missing.md", result.errors)

    def test_pretty_output_reports_status(self):
        result = validate_evidence_file(ROOT / "EVIDENCE.md", ROOT)
        pretty = render_pretty(result)

        self.assertIn("STATUS: PASS", pretty)
        self.assertIn("Checked references:", pretty)


if __name__ == "__main__":
    unittest.main()
