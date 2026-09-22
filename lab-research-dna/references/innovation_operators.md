# Innovation Operators（8 个）+ Hypothesis 模板 + Novelty Stress Test

> Innovation Generation 的唯一合法变换集合。创新必须落在"有 genealogy 与 evidence 的变换操作"内。

## 8 Operators
1. **Expose an ignored factor** — 把现有方法未建模但影响任务的因素显式化（DNA-01）。
2. **Relax an assumption** — 去掉 target-visible、complete modality、same-subject、high-quality 等理想条件（DNA-02）。
3. **Decompose heterogeneity** — 按来源/层级拆解域差异或不确定性（DNA-03）。
4. **Separate signal from nuisance** — 定义任务相关成分与干扰成分，建立可验证分离机制（DNA-04）。
5. **Make reliability explicit** — 对样本/模态/窗口/伪标签估计置信度或难度（DNA-05）。
6. **Raise structural order / temporal scale** — 从局部/低阶/单窗推进到跨窗、长程、高阶、多尺度（DNA-06）。
7. **Inject justified prior** — 在纯数据驱动解释弱或样本不足时引入结构/功能/认知/语义先验（DNA-07）。
8. **Transfer a mechanism across lines** — 只在新任务存在同类失败机制时迁移抽象方法，重做任务对象与证据（DNA-08）。

## Innovation Hypothesis 输出模板（必填全部字段）
- Closest predecessors（P编号 + 关系性质）
- Existing capability（前作已解决的 setting / 已证明的 claim）
- Unresolved limitation / new setting（有证据的 limitation）
- New research gap（映射到 G1–G7）
- Core insight（一句话）
- Why this is not module stacking（说明改变了 problem / assumption / mechanism / evidence 中的哪项）
- Required methodological change
- Required evidence（至少一个 distinguishing experiment，引用 E1–E5）
- Major risk / falsification condition（什么实验结果会证伪它）
- Confidence（High / Medium / Low，说明依据）

## Novelty Stress Test（四问）
1. 是否只是换 backbone / 加 attention / 多一个 loss / 多一个数据集？
2. 是否改变了 problem formulation、assumption、representation mechanism、generalization setting、evidence scope 中的至少一项？
3. 新机制是否直接处理所声称的 failure，而不是顺带有效？
4. 是否一次放宽了多个假设、叠加了多个机制导致无法验证贡献来源？

任一答案为"是（第1、4问）/否（第2、3问）" → 判为弱创新，打回。

## 禁止
- 根据 absence 声称"从未有人做过"。
- 把 Stage 2 的 MEDIUM 边当作者声明。
- 把 lab-recurring pattern 说成普适真理或本组独有秘密。
