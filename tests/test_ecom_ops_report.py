import tempfile
import unittest
from pathlib import Path

from ecom_ops.report import build_report, load_inputs


ROOT = Path(__file__).resolve().parents[1]


class EcommerceOpsReportTest(unittest.TestCase):
    def test_build_report_scores_sku_risks_from_orders_inventory_and_tickets(self):
        inputs = load_inputs(
            ROOT / "examples" / "orders.csv",
            ROOT / "examples" / "inventory.csv",
            ROOT / "examples" / "tickets.csv",
        )

        report = build_report(inputs)

        self.assertEqual(report.summary["order_count"], 8)
        self.assertEqual(report.summary["gross_revenue"], 1897.0)
        self.assertEqual(report.summary["refund_count"], 2)
        self.assertEqual(report.summary["late_shipments"], 4)

        sku_d = report.sku_rows["SKU-D"]
        self.assertEqual(sku_d["risk_level"], "high")
        self.assertIn("replenishment", sku_d["recommended_actions"])
        self.assertIn("shipping follow-up", sku_d["recommended_actions"])

        sku_b = report.sku_rows["SKU-B"]
        self.assertEqual(sku_b["risk_level"], "high")
        self.assertIn("refund review", sku_b["recommended_actions"])

    def test_markdown_output_contains_decision_boundary_and_action_queue(self):
        inputs = load_inputs(
            ROOT / "examples" / "orders.csv",
            ROOT / "examples" / "inventory.csv",
            ROOT / "examples" / "tickets.csv",
        )
        report = build_report(inputs)

        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "weekly-ops-report.md"
            report.write_markdown(output)
            markdown = output.read_text(encoding="utf-8")

        self.assertIn("# Ecommerce Ops Weekly Risk Report", markdown)
        self.assertIn("## Action Queue", markdown)
        self.assertIn("AI output is a draft", markdown)
        self.assertIn("SKU-D", markdown)
        self.assertIn("SKU-B", markdown)


if __name__ == "__main__":
    unittest.main()
