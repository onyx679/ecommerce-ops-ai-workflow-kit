from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class OpsInputs:
    orders: list[dict[str, str]]
    inventory: list[dict[str, str]]
    tickets: list[dict[str, str]]


@dataclass
class OpsReport:
    summary: dict[str, Any]
    sku_rows: dict[str, dict[str, Any]]

    def write_markdown(self, output_path: Path) -> None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        lines = [
            "# Ecommerce Ops Weekly Risk Report",
            "",
            "> AI output is a draft. Confirm stock, refunds, customer promises, and owner assignments before execution.",
            "",
            "## Summary",
            "",
            f"- Orders: {self.summary['order_count']}",
            f"- Gross revenue: {self.summary['gross_revenue']:.2f}",
            f"- Refund orders: {self.summary['refund_count']}",
            f"- Late shipments: {self.summary['late_shipments']}",
            "",
            "## SKU Risk Table",
            "",
            "| SKU | Risk | Revenue | Refunds | Late shipments | Open negative tickets | Stock | Actions |",
            "|---|---:|---:|---:|---:|---:|---:|---|",
        ]

        for sku, row in sorted(self.sku_rows.items()):
            actions = ", ".join(row["recommended_actions"]) or "monitor"
            lines.append(
                f"| {sku} | {row['risk_level']} | {row['revenue']:.2f} | "
                f"{row['refunds']} | {row['late_shipments']} | {row['open_negative_tickets']} | "
                f"{row['on_hand']} | {actions} |"
            )

        lines.extend(["", "## Action Queue", ""])
        for sku, row in sorted(
            self.sku_rows.items(),
            key=lambda item: (_risk_rank(item[1]["risk_level"]), item[0]),
            reverse=True,
        ):
            if row["risk_level"] == "low":
                continue
            actions = ", ".join(row["recommended_actions"])
            lines.append(f"- **{sku}** ({row['risk_level']}): {actions}. Owner must verify source data.")

        output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def load_inputs(orders_path: Path, inventory_path: Path, tickets_path: Path) -> OpsInputs:
    return OpsInputs(
        orders=_read_csv(orders_path),
        inventory=_read_csv(inventory_path),
        tickets=_read_csv(tickets_path),
    )


def build_report(inputs: OpsInputs) -> OpsReport:
    sku_rows: dict[str, dict[str, Any]] = {}
    inventory_by_sku = {row["sku"]: row for row in inputs.inventory}

    for order in inputs.orders:
        sku = order["sku"]
        row = _ensure_sku_row(sku_rows, sku, inventory_by_sku)
        revenue = float(order["revenue"])
        row["orders"] += 1
        row["units"] += int(order["units"])
        row["revenue"] += revenue
        if order["refund"].strip().lower() == "true":
            row["refunds"] += 1
        if int(order["ship_days"]) > 3:
            row["late_shipments"] += 1

    for ticket in inputs.tickets:
        sku = ticket["sku"]
        row = _ensure_sku_row(sku_rows, sku, inventory_by_sku)
        row["tickets"] += 1
        if ticket["status"] == "open" and ticket["sentiment"] == "negative":
            row["open_negative_tickets"] += 1
        if ticket["topic"] == "late-shipping":
            row["late_shipping_tickets"] += 1

    for sku, row in sku_rows.items():
        row["recommended_actions"] = _recommend_actions(row)
        row["risk_level"] = _risk_level(row)

    summary = {
        "order_count": len(inputs.orders),
        "gross_revenue": round(sum(float(row["revenue"]) for row in inputs.orders), 2),
        "refund_count": sum(1 for row in inputs.orders if row["refund"].strip().lower() == "true"),
        "late_shipments": sum(1 for row in inputs.orders if int(row["ship_days"]) > 3),
    }
    return OpsReport(summary=summary, sku_rows=sku_rows)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build an ecommerce operations weekly risk report.")
    parser.add_argument("--orders", type=Path, required=True)
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--tickets", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)

    report = build_report(load_inputs(args.orders, args.inventory, args.tickets))
    report.write_markdown(args.output)
    return 0


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def _ensure_sku_row(
    sku_rows: dict[str, dict[str, Any]],
    sku: str,
    inventory_by_sku: dict[str, dict[str, str]],
) -> dict[str, Any]:
    if sku not in sku_rows:
        inventory = inventory_by_sku.get(sku, {})
        sku_rows[sku] = {
            "orders": 0,
            "units": 0,
            "revenue": 0.0,
            "refunds": 0,
            "late_shipments": 0,
            "tickets": 0,
            "open_negative_tickets": 0,
            "late_shipping_tickets": 0,
            "on_hand": int(inventory.get("on_hand", 0) or 0),
            "reorder_point": int(inventory.get("reorder_point", 0) or 0),
        }
    return sku_rows[sku]


def _recommend_actions(row: dict[str, Any]) -> list[str]:
    actions: list[str] = []
    if row["on_hand"] <= row["reorder_point"]:
        actions.append("replenishment")
    if row["refunds"] > 0:
        actions.append("refund review")
    if row["late_shipments"] > 0 or row["late_shipping_tickets"] > 0:
        actions.append("shipping follow-up")
    if row["open_negative_tickets"] > 0:
        actions.append("customer recovery")
    return actions


def _risk_level(row: dict[str, Any]) -> str:
    score = 0
    if row["on_hand"] <= row["reorder_point"]:
        score += 2
    if row["refunds"] > 0:
        score += 1
    if row["late_shipments"] > 0:
        score += 1
    if row["open_negative_tickets"] > 0:
        score += 2
    if score >= 4:
        return "high"
    if score >= 2:
        return "medium"
    return "low"


def _risk_rank(level: str) -> int:
    return {"low": 1, "medium": 2, "high": 3}[level]


if __name__ == "__main__":
    raise SystemExit(main())

