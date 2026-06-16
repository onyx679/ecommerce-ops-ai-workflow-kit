---
name: ecommerce-ops-review
description: Use when reviewing ecommerce operations data such as orders, inventory, refunds, shipping delays, customer-service tickets, SKU risk, weekly ops reports, or action queues.
---

# Ecommerce Ops Review

Use this skill to turn routine ecommerce operations inputs into a draft weekly risk review. Treat all outputs as decision support, not final business decisions.

## Required Inputs

- Orders: `order_id`, `date`, `sku`, `units`, `revenue`, `refund`, `ship_days`, `channel`
- Inventory: `sku`, `on_hand`, `reorder_point`, `lead_time_days`
- Tickets: `ticket_id`, `date`, `sku`, `topic`, `sentiment`, `status`

If any required field is missing, stop and ask for the source export or mark the section as incomplete.

## Workflow

1. Load orders, inventory, and tickets.
2. Summarize order count, gross revenue, refunds, and late shipments.
3. Group risk signals by SKU.
4. Flag low stock when `on_hand <= reorder_point`.
5. Flag refund, late-shipping, and open negative-ticket signals.
6. Produce a SKU risk table and an action queue.
7. Mark all recommendations as drafts requiring owner verification.

## Risk Rules

| Signal | Score |
|---|---:|
| Low stock | 2 |
| Open negative ticket | 2 |
| Refund order | 1 |
| Late shipment | 1 |

Risk levels:

- `high`: score >= 4
- `medium`: score >= 2
- `low`: score < 2

## Recommended Actions

- Low stock -> replenishment
- Refund order -> refund review
- Late shipment -> shipping follow-up
- Open negative ticket -> customer recovery

## Output Standard

The report must include:

- summary metrics;
- SKU risk table;
- action queue sorted by risk;
- explicit human-review boundary.

Never claim the AI has confirmed inventory, customer compensation, refund liability, or final owner assignments.
