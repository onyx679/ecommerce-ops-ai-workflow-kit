# Transfer Case: Ecommerce Operations to AI Workflow BP Work

This note explains why an ecommerce operations demo is relevant to AI workflow BP work. It is not presented as vehicle-domain experience. It is operating-method evidence: repeated business work can be converted into structured inputs, reusable AI instructions, generated reports, and human-review checkpoints.

中文说明：这份说明解释为什么电商运营 demo 能作为 AI 流程提效岗位的迁移证据。它不是汽车领域经历，也不声称使用真实店铺数据；它证明的是流程拆解、字段标准化、报告生成、行动项整理和人工审核边界设计能力。

## 1. Repeated Work Pattern

Weekly ecommerce operations reviews often repeat the same steps:

- collect order, inventory, and support-ticket records;
- identify abnormal SKUs, refunds, late shipments, and unresolved negative feedback;
- summarize risks and draft follow-up actions;
- ask a human operator to confirm replenishment, refund, customer promise, and owner assignment decisions.

This is similar to other business-process roles where the work is document-heavy, field-driven, and review-sensitive.

## 2. Skillization Method

The demo turns that repeated work into:

1. standard CSV inputs for orders, inventory, and tickets;
2. a reusable `SKILL.md` that defines the task, required inputs, outputs, and review boundaries;
3. a Python CLI that generates a Markdown weekly risk report;
4. tests that verify summary metrics, SKU risk logic, and boundary language;
5. an evidence matrix that separates safe claims from claims that should not be made.

## 3. Transferable Capability

For an AI BP / workflow automation role, this demonstrates:

- extracting structured fields from messy repeated work;
- defining what AI can draft and what humans must decide;
- producing a reviewable report instead of a vague chat answer;
- validating workflow logic with tests;
- documenting claim boundaries before the work is shown publicly.

## 4. What It Does Not Claim

- It is not a real merchant project.
- It does not use real customer records, merchant data, or platform exports.
- It does not prove ecommerce revenue, profit, refund, or customer-service outcomes.
- It does not replace human ownership of inventory, refund, customer promise, or action-owner decisions.

## 5. Reviewer Route

Reviewers can inspect:

- Skill: `skills/ecommerce-ops-review/SKILL.md`
- CLI logic: `ecom_ops/report.py`
- Simulated inputs: `examples/orders.csv`, `examples/inventory.csv`, `examples/tickets.csv`
- Generated report: `examples/weekly-ops-report.md`
- Tests: `tests/test_ecom_ops_report.py`
- Evidence matrix: `EVIDENCE.md`
