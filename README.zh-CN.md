# 电商运营 AI 工作流套件

[![test](https://github.com/onyx679/ecommerce-ops-ai-workflow-kit/actions/workflows/test.yml/badge.svg)](https://github.com/onyx679/ecommerce-ops-ai-workflow-kit/actions/workflows/test.yml)

这是一个公开 demo，用于展示如何把电商运营中的重复工作拆解为可复用的 AI 工作流。

项目使用模拟订单、库存和客服工单数据，生成一份 SKU 维度的周度风险报告。它适合作为业务流程提效岗位的可迁移作品：识别重复任务、定义可靠输入、生成报告草稿、保留人工审核边界，并用测试验证核心逻辑。

作品页：https://onyx679.github.io/ecommerce-ops-ai-workflow-kit/

## 展示能力

- 将订单、库存、客服反馈三类资料拆成标准输入。
- 编写可复用 `SKILL.md`，指导 AI 助手执行电商运营风险复盘。
- 用 Python CLI 生成 Markdown 周报。
- 提供模拟 CSV 输入和脚本生成的样例输出。
- 用单元测试和 GitHub Actions 测试工作流验证风险评分和报告生成行为。
- 明确边界：AI 输出只是草稿，不能替代库存、退款、客户承诺和责任人分配等人工决策。

## 项目结构

```text
ecommerce-ops-ai-workflow-kit/
  EVIDENCE.md
  ecom_ops/report.py
  scripts/ecom_ops_report.py
  skills/ecommerce-ops-review/SKILL.md
  examples/orders.csv
  examples/inventory.csv
  examples/tickets.csv
  examples/weekly-ops-report.md
  tests/test_ecom_ops_report.py
```

## 运行示例

```bash
python scripts/ecom_ops_report.py ^
  --orders examples/orders.csv ^
  --inventory examples/inventory.csv ^
  --tickets examples/tickets.csv ^
  --output examples/weekly-ops-report.md
```

## 运行测试

```bash
python -m unittest discover -s tests
```

GitHub Actions 测试 workflow：https://github.com/onyx679/ecommerce-ops-ai-workflow-kit/actions/workflows/test.yml

当前测试覆盖：

- 订单数、收入、退款数、发货延迟数等摘要指标；
- SKU 风险等级和建议行动标签；
- Markdown 报告结构和人工审核边界说明。

## 为什么有价值

很多运营团队每周都会重复做类似工作：汇总数据、识别异常 SKU、整理风险、分配跟进行动、记录待人工确认事项。这个项目展示如何把这类工作标准化为轻量 AI 辅助流程，同时不让 AI 冒充最终业务决策者。

## 数据边界

本仓库所有数据均为模拟数据，不包含真实客户数据、真实商家数据、平台私有导出或任何雇主内部资料。

## 证据和安全表述

见 [EVIDENCE.md](./EVIDENCE.md)，其中包含 claim 证据矩阵、人工审核边界、简历安全表述，以及不应声称的内容。

## 核查链接

- 作品页：https://onyx679.github.io/ecommerce-ops-ai-workflow-kit/
- Release：https://github.com/onyx679/ecommerce-ops-ai-workflow-kit/releases/tag/v0.1.1
- 测试 workflow：https://github.com/onyx679/ecommerce-ops-ai-workflow-kit/actions/workflows/test.yml
- AI Skill：https://github.com/onyx679/ecommerce-ops-ai-workflow-kit/blob/main/skills/ecommerce-ops-review/SKILL.md
- 生成报告：https://github.com/onyx679/ecommerce-ops-ai-workflow-kit/blob/main/examples/weekly-ops-report.md
- 证据矩阵：https://github.com/onyx679/ecommerce-ops-ai-workflow-kit/blob/main/EVIDENCE.md
