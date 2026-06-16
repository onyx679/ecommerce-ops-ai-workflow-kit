# Ecommerce Ops AI Workflow Kit

[![test](https://github.com/onyx679/ecommerce-ops-ai-workflow-kit/actions/workflows/test.yml/badge.svg)](https://github.com/onyx679/ecommerce-ops-ai-workflow-kit/actions/workflows/test.yml)

A small public demo for turning routine ecommerce operations work into a reusable AI workflow.

The project uses simulated orders, inventory, and customer-service tickets to generate a weekly SKU risk report. It is designed as a transferable proof of work for business process automation roles: identify repeated tasks, define reliable inputs, generate a draft report, keep human review boundaries explicit, and verify the logic with tests.

Portfolio page: https://onyx679.github.io/ecommerce-ops-ai-workflow-kit/

Transfer case: [Ecommerce Operations to AI Workflow BP Work](./docs/transfer-case.md)

## What It Shows

- Business workflow decomposition across orders, inventory, and support tickets.
- A reusable `SKILL.md` for an AI assistant to run an ecommerce operations review.
- A Python CLI that produces a Markdown weekly risk report.
- A verification CLI that checks the public claim-to-evidence matrix.
- Simulated CSV inputs and a generated sample report.
- Unit tests and a GitHub Actions test workflow for the core risk-scoring and report-output behavior.
- Clear boundaries: AI output is a draft and must not replace stock, refund, customer promise, or owner-assignment decisions.

## Project Structure

```text
ecommerce-ops-ai-workflow-kit/
  EVIDENCE.md
  ecom_ops/report.py
  ecom_ops/evidence.py
  scripts/ecom_ops_report.py
  scripts/verify_evidence.py
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

## Verify Evidence Matrix

```bash
python scripts/verify_evidence.py
```

This checks that local evidence references in `EVIDENCE.md` exist and that key safety boundaries remain present.

GitHub Actions test workflow: https://github.com/onyx679/ecommerce-ops-ai-workflow-kit/actions/workflows/test.yml

Current test coverage checks:

- summary metrics such as order count, revenue, refund count, and late shipments;
- SKU risk levels and recommended action tags;
- Markdown report sections and human-review boundary language.
- evidence-matrix references and safe wording boundaries.

## Why This Matters

Many operations teams repeat the same weekly work: collect data, identify abnormal SKUs, summarize risks, assign follow-up, and document what needs human confirmation. This repo shows how that work can be standardized into a lightweight AI-assisted workflow without pretending the AI has final business authority.

## Transfer Case

See [docs/transfer-case.md](./docs/transfer-case.md) for a reviewer-friendly explanation of why this ecommerce operations demo is relevant to AI workflow BP work. It frames the project as transferable operating-method evidence rather than vehicle-domain experience or real merchant performance.

## Data Boundary

All data in this repository is simulated. The project does not contain real customer data, real merchant data, private platform exports, or any employer-internal materials.

## Evidence And Safe Wording

See [EVIDENCE.md](./EVIDENCE.md) for the claim matrix, human-review boundary, resume-safe summary, and claims that should not be made.

## Verification Links

- Portfolio page: https://onyx679.github.io/ecommerce-ops-ai-workflow-kit/
- Release: https://github.com/onyx679/ecommerce-ops-ai-workflow-kit/releases/tag/v0.1.3
- Transfer case: https://github.com/onyx679/ecommerce-ops-ai-workflow-kit/blob/main/docs/transfer-case.md
- Test workflow: https://github.com/onyx679/ecommerce-ops-ai-workflow-kit/actions/workflows/test.yml
- AI Skill: https://github.com/onyx679/ecommerce-ops-ai-workflow-kit/blob/main/skills/ecommerce-ops-review/SKILL.md
- Generated report: https://github.com/onyx679/ecommerce-ops-ai-workflow-kit/blob/main/examples/weekly-ops-report.md
- Evidence matrix: https://github.com/onyx679/ecommerce-ops-ai-workflow-kit/blob/main/EVIDENCE.md
