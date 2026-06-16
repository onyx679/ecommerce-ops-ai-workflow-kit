# Evidence Matrix

This file maps public claims about the project to verifiable repository evidence and safe wording boundaries.

## Claim Matrix

| Claim | Evidence | Safe wording | Boundary |
|---|---|---|---|
| The project is a public ecommerce operations workflow demo. | `README.md`, `README.zh-CN.md`, public GitHub repository | Public demo using simulated ecommerce operations data | Do not describe it as a real merchant project. |
| The workflow uses orders, inventory, and customer-service tickets. | `examples/orders.csv`, `examples/inventory.csv`, `examples/tickets.csv` | Simulated order, inventory, and ticket inputs | Do not claim real customer, merchant, or platform export data. |
| The project includes an AI Skill. | `skills/ecommerce-ops-review/SKILL.md` | One reusable AI Skill for ecommerce operations review | Do not claim it is installed in a company environment. |
| The project includes a Python CLI. | `scripts/ecom_ops_report.py`, `ecom_ops/report.py` | Python CLI generates a Markdown weekly risk report | Do not claim production deployment. |
| The project includes evidence validation. | `scripts/verify_evidence.py`, `ecom_ops/evidence.py`, `tests/test_evidence_validation.py` | Evidence validator checks local claim references and safe wording boundaries | Do not treat validation as proof of real merchant adoption. |
| The project generates a sample report. | `examples/weekly-ops-report.md` | Script-generated Markdown sample report | Treat output as a draft, not final operating instruction. |
| The project has unit tests and public CI. | `tests/test_ecom_ops_report.py`, `.github/workflows/test.yml`, [GitHub Actions workflow](https://github.com/onyx679/ecommerce-ops-ai-workflow-kit/actions/workflows/test.yml) | Two unit tests verify summary metrics, SKU risk, actions, and report boundaries; the public GitHub Actions test workflow is available | Do not imply production deployment or external adoption. |
| The project has a release. | `v0.1.3` GitHub release | Public `v0.1.3` release | Do not imply external adoption or review. |
| The project has a public portfolio page. | `docs/index.html`, GitHub Pages | Public bilingual portfolio page with verification links | Do not imply real merchant adoption or customer data use. |

## Human Review Boundary

AI output is limited to draft preparation and risk surfacing. A human owner must confirm:

- inventory availability and replenishment decisions;
- refund liability and customer compensation;
- customer promises and response wording;
- action owners and deadlines;
- any real business data before use.

## Resume-Safe Summary

> Built a public ecommerce operations workflow demo using simulated orders, inventory, and support-ticket data. The project includes one AI Skill, two Python CLIs, sample CSV inputs, a generated Markdown weekly risk report, bilingual README files, unit tests, a public GitHub Actions test workflow, an evidence matrix with validation, a GitHub Pages portfolio page, and a public `v0.1.3` release. AI output is treated as draft decision support and requires human review.

## Do Not Claim

- Real merchant adoption.
- Real customer data analysis.
- Production deployment.
- Real-user adoption or external acceptance.
- External community acceptance.
- Revenue, refund, stock, or customer-service decisions made by AI.
