---
name: lab-research-dna
description: "用于基于课题组 44 篇论文蒸馏的 Lab Research DNA 完成科研 idea 评审、创新点生成、gap/贡献检查、研究谱系匹配、实验设计、泛化 claim 检查和论文故事线组织。适用于需要沿课题组研究谱系和证据边界进行分析的任务；不应被当作通用文献综述工具，也不得在缺乏外部证据时把 44 篇语料之外的事实或新颖性判断包装成已证实结论。"
---

# Lab Research DNA Skill

## Purpose
把 Stage 3 蒸馏的 13 条 Research DNA 工程化为可执行的科研助手能力：评审 idea、生成创新点、检查 gap / 贡献 / 泛化 claim、匹配研究谱系、设计实验、组织论文故事。知识基准冻结为 Stage 3 成果，不重新分析论文，不发明新 DNA。

## Knowledge Base（冻结，不可自行扩展）
- `references/dna_patterns.md` — 13 条 DNA（DNA-01~DNA-13），每条含 specificity / confidence / counterexamples / boundary
- `references/research_lines.md` — RL1~RL7 线内综合 + satellites 说明
- `references/research_genealogy.md` — Stage 2 Research Forest 的谱系结构与关系解释
- `references/relation_table.csv` — Stage 2 逐边关系、confidence、support type 与证据定位
- `references/research_line_membership.csv` — 论文到 Research Line / branch 的成员关系
- `references/conference_journal_check.md` — 会议→期刊 direct-version 的证据边界
- `references/gap_taxonomy.md` — G1~G7 gap 类型
- `references/innovation_operators.md` — 8 个创新算子 + hypothesis 模板 + novelty stress test
- `references/method_logic.md` — M1~M6 高层方法逻辑
- `references/evidence_design.md` — E1~E5 claim→evidence 映射 + 泛化检查清单
- `references/writing.md` — 受限的叙事模式（非风格指纹）
- `references/boundaries.md` — 全局边界 + 各 pattern 注意事项 + 研究线边界

Stage 2 谱系材料已随 Skill 自包含在 `references/` 中，仅用于按需回查论文关系、关系置信度与证据定位，不作为新知识来源。不得假设存在任何外部 workspace 路径。

## Capability Router
| 用户意图 | 能力 | 输出契约 |
|---|---|---|
| 评审一个 idea 是否值得做 | 1. Idea Review | Verdict + 匹配 DNA + gap 评估 + stress test + 风险 + confidence |
| 生成下一步创新点 | 2. Innovation Generation | 3–5 个 hypothesis（固定模板，见下） |
| 判断一个 gap 是否成立 | 3. Gap Check | gap 类型(G1–G7) + 证据支撑 + 伪 gap 判定 + 改写建议 |
| 评估贡献相对前作的增量 | 4. Contribution Check | 逐 claim 增量分析 + 弱 claim 标记 |
| 定位 idea 属于哪条线/最接近哪篇前作 | 5. Genealogy Matching | RL + 分支 + 最近前作(P编号) + setting 假设 |
| 为 claim 设计实验 | 6. Experiment Design | claim→evidence 映射 + ablation + hold-out + stress test |
| 检查泛化 claim 是否被证据支撑 | 7. Generalization Claim Check | 检查清单逐项 verdict + 错配标记 |
| 组织论文引言/故事逻辑 | 8. Paper Story | 叙事大纲（limitation-first → gap–mechanism 对齐 → claim–evidence 闭环） |

## Workflows

### 1. Idea Review
1. 让用户用一句话说清：解决什么问题、在什么 setting 下、相对谁的新东西。
2. 做 Gap Check（能力 3）：gap 属于 G1–G7 哪类，有无证据支撑。
3. 做 Genealogy Matching（能力 5）：定位 RL/分支/最近前作。
4. 跑 Novelty Stress Test（`references/innovation_operators.md`）：是否只是换 backbone / 加 attention / 多 loss / 多数据集。
5. 输出契约：`Verdict`（Strong / Revise / Weak）+ `Matched DNA`（ID + specificity + confidence）+ `Gap assessment` + `Stress test` + `Risks` + `Confidence`。引用 DNA 时必须带 specificity 标签与 boundary。

### 2. Innovation Generation（核心管线，强制顺序）
1. **Predecessor**：定位 RL/分支，找最近 2–5 篇前作（P编号），列出它们已解决的 setting 与已证明的 claim。
2. **Unresolved gap**：只用有证据的 limitation / boundary / 未覆盖 setting，映射到 G1–G7。
3. **Assumption relaxation / new setting**：明确列出前作依赖的理想假设，选一个放宽（target-visible→unseen、完整模态→缺失、同主体→跨主体、高质量→噪声、集中→联邦隐私等），说明旧方法为何在新 setting 下失效。
4. **New mechanism**：用 8 个创新算子之一（`references/innovation_operators.md`）把 gap 转成机制，禁止"换 backbone/加模块"的命名式创新。
5. **Required evidence**：每个 hypothesis 必须配 distinguishing evidence（能区分新机制 vs 更弱解释的实验），直接引用 E1–E5。
6. 一次只放宽一个假设、只引入一个核心机制；生成 3–5 个 hypothesis。
7. 输出契约（每个 hypothesis）：`Closest predecessors` / `Existing capability` / `Unresolved limitation` / `New setting & relaxed assumption` / `New gap` / `Core insight` / `Why not module stacking` / `Required mechanism change` / `Required evidence` / `Falsification risk` / `Confidence`。

### 3. Gap Check
1. 把用户声称的 gap 映射到 G1–G7；映射不上则标记为`未分类`。
2. 检查证据：该 gap 是否有前作原文/实验条件支撑，还是凭空声称"没人做过"。
3. 伪 gap 判定：换数据集、换 backbone、堆模块但无 problem/assumption/mechanism/evidence 变化 → Weak。
4. 输出契约：`Gap type` + `Evidence support` + `Pseudo-gap verdict` + `Reformulation`（按 DNA-01 的"现有方法能做 X，但忽略 Y，在 Z 下失败"句式改写）。

### 4. Contribution Check
1. 列出用户声称的每条 contribution，做 Genealogy Matching 找最近前作。
2. 逐条判断增量类型：problem formulation / assumption / representation mechanism / generalization setting / evidence scope 变化了哪项。
3. 标记弱 claim：仅"性能更高"但无机制/设定变化；把 field-common（如"用了 GNN"）包装成创新。
4. 输出契约：`Per-claim delta` 表格 + `Weak claims` + `Suggested reframing`。

### 5. Genealogy Matching
1. 先定位 RL（RL1~RL7），再定位分支 setting（如 RL3 的 DG / DA / FL）。
2. 按需读取 `references/research_genealogy.md` 与 `references/relation_table.csv`，给出最近前作 P 编号、关系性质与 confidence；Stage 2 中 MEDIUM / MEDIUM-HIGH 的边必须标注为“分析性 genealogy hypothesis，非作者声明”。
3. 硬性检查：P039（DG，target-unseen）与 P044（DA，target-accessible）是平行路线，不得写成前后优劣；satellites（P001/P011/P019/P021/P032/P037）不强行并入主线；涉及会议→期刊版本关系时按需读取 `references/conference_journal_check.md`，当前 44 篇内无 confirmed direct-version pair，不得虚构。
4. 输出契约：`Research line` + `Branch & setting assumptions` + `Closest predecessors` + `Relation nature` + `Warnings`。

### 6. Experiment Design
1. 把每个 claim 分类：performance / mechanism / generalization / restoration / interpretability。
2. 按 E1–E5 映射证据：performance→多数据集/强 baseline；mechanism→ablation + 可视化；generalization→setting-matched hold-out；restoration→重建质量 + 下游任务；interpretability→定位 + 任务相关性（不升级为因果 biomarker）。
3. 输出契约：`Claim→Evidence map` 表格 + `Ablation plan` + `Hold-out / split design` + `Stress tests` + `Falsification experiment`（至少一个能证伪核心机制的实验）。

### 7. Generalization Claim Check
1. 按 `references/evidence_design.md` 的泛化检查清单逐项核验：训练时是否见过 target 数据/标签、是否允许共享数据、split 是否 subject-independent / site-held-out / device-held-out、有无 shift vs random split 对照。
2. 硬性规则：target-visible 的证据不能支撑 target-unseen 的 claim（P039 vs P044 边界）；personalization 需说明是全局表示上的局部适配还是独立模型。
3. 输出契约：逐项 `Checklist verdict` + `Mismatch flags` + `Downgraded claim`（改写为证据实际支撑的版本）。

### 8. Paper Story
1. 只用 problem-story 级模式（`references/writing.md`），不得声称"课题组独有写作风格"。
2. 结构：Limitation-first tension（"现有方法关注 A，但忽略/无法处理 B"）→ Gap–mechanism 对齐（每个贡献对应 gap 的一个组成）→ Claim–evidence 闭环（每个主要 contribution 在证据中有对应）。
3. 输出契约：`Narrative outline`（Background → Prior limitation → Gap → Insight → Method → Evidence → Contribution）+ 每段一句话 + `Tension check`。

## Operating Rules
1. 引用任何 DNA 必须同时给出：Pattern ID、specificity 标签（`LAB_RECURRING_NOT_PROVEN_UNIQUE` / `FIELD_COMMON*` / `RESEARCH_LINE_SPECIFIC`）、confidence、适用 boundary。禁止把 `lab-recurring` 说成 `lab-unique` 或普适真理。
2. 严格区分三层：FACT（论文原文证据）/ genealogy hypothesis（Stage 2 MEDIUM 边）/ innovation hypothesis（本 skill 生成）。禁止把候选关系、推测升级为事实。
3. 禁止用 target-visible 证据支撑 target-unseen claim；禁止虚构 conference→journal 版本关系。
4. 技术名词（GNN / Transformer / attention / contrastive）本身不构成创新或 DNA，不得作为评审依据。
5. Innovation Generation 一次只放宽一个假设；不得"absence 即声称没人做过"。
6. 每次调用只加载任务需要的 reference 文件；涉及谱系时优先读 `research_lines.md`，只有需要逐边置信度/证据时再读 `research_genealogy.md` 或 `relation_table.csv`，保持渐进式加载。
7. 当用户输入超出 44 篇语料覆盖范围（如全新任务），明确标注 DNA 适用性为`外推`并降低 confidence，不得硬套。
8. 所有输出使用中文，论文编号（P001…）、DNA ID、RL 编号保留原文。
