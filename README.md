# Ecommerce Ops AI Workflow Kit

A small public demo for turning routine ecommerce operations work into a reusable AI workflow.

The project uses simulated orders, inventory, and customer-service tickets to generate a weekly SKU risk report. It is designed as a transferable proof of work for business process automation roles: identify repeated tasks, define reliable inputs, generate a draft report, keep human review boundaries explicit, and verify the logic with tests.

## What It Shows

- Business workflow decomposition across orders, inventory, and support tickets.
- A reusable `SKILL.md` for an AI assistant to run an ecommerce operations review.
- A Python CLI that produces a Markdown weekly risk report.
- Simulated CSV inputs and a generated sample report.
- Unit tests for the core risk-scoring and report-output behavior.
- Clear boundaries: AI output is a draft and must not replace stock, refund, customer promise, or owner-assignment decisions.

## Project Structure

```text
ecommerce-ops-ai-workflow-kit/
  ecom_ops/report.py
  scripts/ecom_ops_report.py
  skills/ecommerce-ops-review/SKILL.md
  examples/orders.csv
  examples/inventory.csv
  examples/tickets.csv
  examples/weekly-ops-report.md
  tests/test_ecom_ops_report.py
```

## Run The Demo

```bash
python scripts/ecom_ops_report.py \
  --orders examples/orders.csv \
  --inventory examples/inventory.csv \
  --tickets examples/tickets.csv \
  --output examples/weekly-ops-report.md
```

## Run Tests

```bash
python -m unittest discover -s tests
```

Current test coverage checks:

- summary metrics such as order count, revenue, refund count, and late shipments;
- SKU risk levels and recommended action tags;
- Markdown report sections and human-review boundary language.

## Why This Matters

Many operations teams repeat the same weekly work: collect data, identify abnormal SKUs, summarize risks, assign follow-up, and document what needs human confirmation. This repo shows how that work can be standardized into a lightweight AI-assisted workflow without pretending the AI has final business authority.

## Data Boundary

All data in this repository is simulated. The project does not contain real customer data, real merchant data, private platform exports, or any employer-internal materials.

