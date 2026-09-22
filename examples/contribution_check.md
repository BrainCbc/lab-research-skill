# Example — Contribution Check

**输入：** 某多站点脑疾病诊断工作声称的贡献：
1. "首次将对比学习用于多站点脑网络域适应"
2. "在三个站点上精度超过现有方法"
3. "提出了样本-站点双层异质性建模"

**最近前作：** P008（多中心多层不确定性 DA）、P044（统一图 DA，sample/site 双层异质性 + SPL）。

## Skill 输出

| # | Claim | Delta 分析 | 判定 |
|---|---|---|---|
| 1 | 首次用对比学习做多站点域适应 | 技术组合声明；P044 已有对比学习组件，"首次"需文献检索支撑，语料内不成立 | Weak — 改写或删除 |
| 2 | 三站点精度更高 | 仅 performance delta，无 mechanism / setting 变化；需检查是否为调参或划分所致 | Weak as stated — 需补 E2 证明增益来源 |
| 3 | 样本-站点双层异质性建模 | P044 已做 sample/site 双层；若本工作拆解到更细粒度（如 class/prototype 级，DNA-03），则构成增量，否则与 P044 重叠 | Conditional — 需明确与 P044 的拆解差异 |

**Weak claims:** #1（"首次"无依据）、#2（无机制支撑的精度 claim）。
**Suggested reframing:** 把 #3 收紧为"在 P044 的 sample/site 双层基础上，进一步拆解到 class-level 结构异质性（DNA-03），并证明该层级需要独立的对齐机制"；#2 降级为支撑性证据而非核心贡献。
