# Test Run — Contribution Check
**Fixture:** tests/fixtures/contribution.json（超图睡眠分期；前作 P043）

| # | Claim | Delta 分析 | 判定 |
|---|---|---|---|
| 1 | 首次将超图用于睡眠分期 | 技术"首次"声明；语料内 P040 已用超图（脑网络），跨任务"首次"需外部文献检索，语料内不成立；且超图本身不是 DNA（boundaries.md） | Weak — 删除或改写为机制 claim |
| 2 | 三数据集超现有方法 2% | 纯 performance delta，无 mechanism/setting 变化说明 | Weak as stated — 需 E2 证明增益来源 |
| 3 | 模态-被试双层不确定性建模 | P043 已有 modality/subject/temporal/sample 不确定性；若"双层"是其子集，则与 P043 重叠；需明确新增的层级或不同的不确定性处理机制（DNA-03） | Conditional — 收紧为与 P043 的差异点 |

**Weak claims:** #1、#2。
**Suggested reframing:** 将 #1 改写为"把睡眠阶段间的转移结构建模为超边，显式表达高阶阶段依赖（DNA-06，需证明平铺特征无法表达该信息）"；#3 收紧为"在 P043 的不确定性框架上，新增 __ 层级并证明需要独立机制"；#2 降级为支撑证据。
