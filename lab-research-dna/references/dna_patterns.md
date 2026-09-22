# DNA Patterns（13 条，Stage 3 冻结知识）

> 引用任一条 DNA 时必须同时给出：Pattern ID、specificity、confidence、boundary。
> specificity 含义：`LAB_RECURRING_NOT_PROVEN_UNIQUE` = 语料内跨线反复出现，但无外部对照组，不可声称为本组独有；
> `FIELD_COMMON*` = 领域通用策略，本组出现频繁但非独有；`RESEARCH_LINE_SPECIFIC` = 只在指定研究线成立。

---

## DNA-01 — 把"被忽略的因素"升级为显式建模对象
- **Category:** Research Strategy / Gap Construction
- **Specificity:** `LAB_RECURRING_NOT_PROVEN_UNIQUE` | **Confidence:** HIGH | **Recurrence:** High
- **Supporting lines:** RL1, RL2, RL3, RL4, RL5, RL6, RL7
- **Representative papers:** P020（跨窗 topology evolution）, P023（regional heterogeneity）, P026（先验/可解释）, P031（联邦下外部因素漂移）, P041（前景/背景感知不对称）, P044（sample/site 异质性）, P004（TIL-肿瘤空间交互）
- **Pattern:** 高频研究起点不是"换更强网络"，而是指出现有方法忽略了某个决定性因素（结构、异质性来源、先验、缺失信息、语义不对称），把它变成可建模对象。
- **Mechanism:** 先定位现有方法的盲区，再用专门的表示、约束或学习机制让该因素进入优化过程，形成 problem→mechanism 的直接对应。
- **Boundary:** 适合已有方法总体有效、但存在明确未建模因素的连续研究线；不适合仅凭技术流行度找"未被考虑"的伪 gap。
- **Counterexamples:** P032, P037
- **Potential use:** 新 idea 评审时优先问"现有方法具体忽略了什么、为什么导致失败、如何显式化"，而不是先选模块。

## DNA-02 — 通过提高现实约束或放宽理想假设来升级研究问题
- **Category:** Research Evolution
- **Specificity:** `FIELD_COMMON_STRONG_LAB_RECURRENCE`（领域常见，本组高频）| **Confidence:** HIGH | **Recurrence:** High
- **Supporting lines:** RL2, RL3, RL4, RL5, RL6
- **Representative papers:** P036（完整模态→缺失模态）, P039（target-unseen DG）, P042（隐私约束个性化联邦）, P043（跨被试睡眠）, P031（联邦+设备漂移）, P029（低质量掌纹）
- **Pattern:** 后续工作把原有 setting 推向更困难、更接近真实应用的条件。
- **Mechanism:** 保持任务目标连续，修改数据可用性/目标域可见性/隐私/质量/主体/模态条件，使旧方法的隐含假设失效。
- **Boundary:** 领域通用推进方式，非本组独有；只有新 setting 带来新的科学/学习问题时才构成强创新，单纯换数据集不算。
- **Counterexamples:** P021, P032
- **Potential use:** 对最近前作列出其成立所需假设，逐项测试能否在更现实条件下放宽，生成"下一步"候选。

## DNA-03 — 把异质性拆解到具体来源和层级
- **Category:** Problem Formulation / Method Design
- **Specificity:** `LAB_RECURRING_NOT_PROVEN_UNIQUE` | **Confidence:** HIGH | **Recurrence:** Medium-high
- **Supporting lines:** RL2, RL3, RL4, RL6
- **Representative papers:** P008（center/feature/label 三层不确定性）, P023（regional heterogeneity）, P031（identity/context 解耦）, P043（temporal/sample 双层不确定性）, P044（sample/site 双层）
- **Pattern:** "heterogeneity" 不停留在总括名词，被拆成 center/feature/label、regional、identity/context、intra-/inter-client、temporal/sample、sample/site 等来源或层级。
- **Mechanism:** 先拆分异质性来源，再为不同来源配置对齐/解耦/聚合/选择/可信度机制，避免一个统一 loss 承担所有矛盾。
- **Boundary:** 只有当不同来源有不同生成机制或需不同处理策略时才值得拆分；无证据的过度分解只增加复杂度。
- **Counterexamples:** P004, P005, P040
- **Potential use:** 新任务出现域差异时，先问它来自哪里、发生在哪一层、是否需要分治。

## DNA-04 — 保护任务相关信号，同时隔离 nuisance 信息
- **Category:** Representation Strategy
- **Specificity:** `LAB_RECURRING_NOT_PROVEN_UNIQUE` | **Confidence:** HIGH | **Recurrence:** Medium-high
- **Supporting lines:** RL2, RL3, RL5, RL6, RL7
- **Representative papers:** P005（显著特征选择）, P023（disease-irrelevant 信息解耦）, P031（identity/context 解耦）, P034（EEG 身份解耦）, P041（前景/背景）, P044
- **Pattern:** 把性能瓶颈重写为"有用信号与干扰信息混杂"：重要特征被冗余特征、上下文、身份无关偏差、背景、疾病无关信息污染。
- **Mechanism:** 通过特征选择、解耦、显著性、权重或结构约束保留 task-related component，抑制 nuisance component。
- **Boundary:** 必须能说明"任务相关"与"nuisance"的可观测/可验证代理；否则 disentanglement 易沦为命名创新。
- **Counterexamples:** P024, P025, P040
- **Potential use:** 检查当前表示是否把任务因子与场景/个体/背景/噪声混在一起，并要求可验证的分离证据。

## DNA-05 — 用置信度、难度或质量控制"谁先学、谁更可信、谁贡献更大"
- **Category:** Learning Strategy
- **Specificity:** `LAB_RECURRING_NOT_PROVEN_UNIQUE` | **Confidence:** HIGH | **Recurrence:** High
- **Supporting lines:** RL1, RL3, RL4, RL6
- **Representative papers:** P001（target sample reweighting）, P007（self-paced 跨站点迁移）, P012（self-paced CycleGAN）, P018（modality TCP）, P030（window TCP）, P043（SPL）, P044（SPL 样本难度）
- **Pattern:** 当伪标签/时间窗/模态/样本/跨域数据可靠性不一致时，用 reweighting、confidence regression、self-paced、quality score、active selection，而非等权处理。
- **Mechanism:** 显式估计可靠性/难度，转为训练顺序、融合权重、样本权重或标注优先级，减少错误信息累积。
- **Boundary:** 可靠性分数需有独立依据并经 ablation/可视化验证；若 confidence 只是模型自身无校准输出，可能放大确认偏差。
- **Counterexamples:** P026, P040
- **Potential use:** 面对 noisy / pseudo-labeled / multi-window / multi-modal 数据时优先检查"等权假设"是否合理。

## DNA-06 — 优先利用关系结构，而不是只做平铺特征融合
- **Category:** Method Design
- **Specificity:** `FIELD_COMMON_STRONG_LAB_EMPHASIS`（领域常见，本组有明显方法学强调）| **Confidence:** HIGH | **Recurrence:** High
- **Supporting lines:** RL1, RL2, RL7
- **Representative papers:** P002（高阶样本关系）, P006（时空拓扑融合）, P020（跨窗 topology evolution）, P040（hypergraph）, P004（WSI 空间交互）, P021（图结构感知对比）
- **Pattern:** 把样本/脑区/时间窗/patch 的关系结构作为主要信息源，从普通图推进到拓扑演化、社区、多尺度、超图高阶关系。
- **Mechanism:** 把实体间关系编码为图/拓扑/高阶结构，学习交互与组织方式，而非拼接独立特征。
- **Boundary:** 图结构本身不是创新；必须证明关系结构对应任务机制、能捕获平铺特征无法表达的信息。
- **Counterexamples:** P031, P038
- **Potential use:** 当对象间存在明确交互/拓扑/时空组织时，检查是否应把"关系"提升为一等建模对象。

## DNA-07 — 当纯数据驱动建模达到瓶颈时，引入先验与可解释约束
- **Category:** Method Design / Interpretability
- **Specificity:** `LAB_RECURRING_NOT_PROVEN_UNIQUE` | **Confidence:** MEDIUM-HIGH | **Recurrence:** Medium
- **Supporting lines:** RL1, RL2, RL5
- **Representative papers:** P009（cognitive-driven ordinal preservation）, P014（判别+可解释 ROI）, P026（结构/功能先验）, P040（跨窗先验）, P041（semantic-prior gating）
- **Pattern:** 部分工作明确把"纯数据驱动、缺先验、难解释"作为新 gap，引入认知/结构-功能/时间相似性/语义显著性先验。
- **Mechanism:** 让先验参与表示构造、注意、约束或分组，使搜索空间与领域结构一致，提高解释性/稳定性。
- **Boundary:** 先验须有独立依据，需实验证明增益非额外参数所致；非所有研究线的稳定模式。
- **Counterexamples:** P020, P024, P031
- **Potential use:** 模型已高性能但解释弱/数据效率差时，寻找结构/功能/认知/语义先验作为下一层创新。

## DNA-08 — 跨研究线迁移抽象机制，而不是照搬整套模型
- **Category:** Research Strategy / Knowledge Transfer
- **Specificity:** `LAB_RECURRING_HYPOTHESIS`（中等置信跨线迁移假设，样本较少）| **Confidence:** MEDIUM-HIGH | **Recurrence:** Low-medium
- **Supporting lines:** BRIDGE, RL1, RL4, RL5, RL6
- **Representative papers:** P018→P030（confidence-aware 跨线）, P006→P020（spatio-temporal graph 跨线）, P031/P034（disentanglement 概念并行）
- **Pattern:** 把已验证的抽象机制迁移到新问题，保留"机制解决哪类失败"的逻辑，重新定义输入对象、约束与证据，而非复制模型。
- **Mechanism:** 迁移的是失败机制的抽象解法，不是网络结构。
- **Boundary:** 强证据桥接数量有限，不能假设每条线都能互相迁移；概念并行不等于版本继承。
- **Counterexamples:** P004, P032, P037
- **Potential use:** 要求在新任务中重新定义失败模式与验证实验，优先迁移"为什么有效"。

## DNA-09 — 研究演化更像"分支专化"，而不是单一路线逐篇叠加
- **Category:** Research Evolution / Genealogy
- **Specificity:** `LAB_RECURRING_NOT_PROVEN_UNIQUE` | **Confidence:** HIGH | **Recurrence:** High
- **Supporting lines:** RL2, RL3, RL4, RL6
- **Representative papers:** P039/P044/P042（多站点三路线）, P012/P031（掌纹跨设备两路线）, P017/P029（质量恢复）, P036（缺失模态）
- **Pattern:** 同一大问题按不同假设/失败模式分叉为互补分支（DG/DA/FL、跨设备/质量恢复/安全），而非强行排成"前作+新模块"单链。
- **Mechanism:** 围绕稳定的大问题建立多个互补分支，各分支针对不同现实条件或证据目标优化。
- **Boundary:** corpus-level 谱系结论；MEDIUM/MEDIUM-HIGH 边仍是分析性假设，不代表作者声明。
- **Counterexamples:** P028, P041（相对线性）
- **Potential use:** 新 idea 先定位"哪条分支/哪个 setting"，再谈方法创新；不要问"接哪一篇"。

## DNA-10 — Claim 的扩大通常伴随 Evidence scope 的扩大
- **Category:** Evidence Design
- **Specificity:** `FIELD_COMMON`（通用高水平实验原则，不作组内 DNA）| **Confidence:** HIGH | **Recurrence:** High
- **Supporting lines:** RL1, RL2, RL3, RL4, RL6
- **Representative papers:** P031（ablation 全移除）, P039（多站点 DG 对比+显著性）, P044（多组件 ablation）, P036（恢复质量+下游 AUC）, P029（PSNR/SSIM+识别精度）
- **Pattern:** 声称跨域/鲁棒/机制有效/可信时，增加多站点-多设备-多数据集、消融、可视化、特征分布或下游任务证据，而非只报单一 accuracy。
- **Mechanism:** 每个核心 claim 映射到能区分该 claim 与更弱解释的实验。
- **Boundary:** 通用原则，不可包装成课题组独有风格；具体论文证据强度仍需逐篇核验。
- **Counterexamples:** 语料内无明确反例记录；典型误用即反例——把通用实验原则包装成"本组独有风格"（已用 `FIELD_COMMON` 标记防范）。
- **Potential use:** 生成创新点时同步生成"什么实验能证伪或区分它"，避免创新与证据脱节。

## DNA-11 — RL1 动态脑网络：从窗口表示走向跨窗演化、长程、高阶、先验与置信度
- **Category:** Research-Line-Specific Pattern
- **Specificity:** `RESEARCH_LINE_SPECIFIC`（仅 RL1，不外推）| **Confidence:** HIGH | **Recurrence:** Line-wide
- **Supporting lines:** RL1
- **Representative papers:** P003（动态拓扑+时间联合表示）→ P020（显式跨窗 topology evolution）→ P022（节点异质性传播）/ P024（long-interval）/ P025（跨窗演化）/ P026（先验可解释）/ P030（TCP 置信度）→ P040（temporal prior + hypergraph）
- **Pattern:** 每一代补足上一代未表达的时间尺度、关系阶数、节点异质性、先验或窗口可靠性，而非简单扩大 GNN。
- **Mechanism:** 沿"时间尺度 × 关系阶数 × 节点异质性 × 先验 × 置信度"五轴推进。
- **Boundary:** 只适用于动态脑网络主线；P015 是平行表示分支。
- **Counterexamples:** P015
- **Potential use:** 用五轴定位未覆盖空间找新 idea。

## DNA-12 — RL3 多站点：target 可见性、隐私和个性化需求决定方法家族
- **Category:** Research-Line-Specific Pattern
- **Specificity:** `RESEARCH_LINE_SPECIFIC`（仅 RL3，不外推）| **Confidence:** HIGH | **Recurrence:** Line-wide
- **Supporting lines:** RL3
- **Representative papers:** P007（联邦适应，隐私约束）, P008（多中心多层不确定性 DA）, P039（target-unseen DG）, P044（target-accessible graph DA）, P042（个性化联邦）
- **Pattern:** 先明确 target data 是否可访问、是否允许跨站点共享、要全局还是个性化模型，再选 FL / DG / DA；路线互补不可互换。
- **Mechanism:** setting assumption 决定方法家族。
- **Boundary:** 不能把 DG 与 DA 写成先后优劣；不能用 target-visible 实验证 unseen-site claim。
- **Counterexamples:** RL3 内无明确反例；典型误用即反例——把 P039（DG）与 P044（DA）写成直接前后继，或用 target-visible 证据支撑 unseen-site claim。
- **Potential use:** 任何 multi-site idea 先填 setting 五元组（target可见性/隐私/个性化/标签/拓扑）再评估 novelty。

## DNA-13 — 多模态路线从"互补融合"转向"不完美条件下的鲁棒融合"
- **Category:** Research-Line-Specific Pattern
- **Specificity:** `RESEARCH_LINE_SPECIFIC`（RL2/RL4，不外推）| **Confidence:** HIGH | **Recurrence:** High within two lines
- **Supporting lines:** RL2, RL4
- **Representative papers:** P002（互补融合起点）→ P009（不平衡）/ P014（判别可解释）/ P023（区域异质性）/ P036（缺失模态）；P018（不确定性融合）→ P035（跨被试）/ P043（可信睡眠融合）
- **Pattern:** 当"多模态互补"不再是瓶颈后，重点转向模态不一致、主体漂移、标签结构、缺失与不确定性。
- **Mechanism:** 现实数据缺陷成为问题定义本身。
- **Boundary:** 不同任务的数据缺陷不应统一成一个"鲁棒融合"模块；缺失/异质/跨主体/不确定性需分别设计证据。
- **Counterexamples:** P010
- **Potential use:** 检查新多模态工作解决的是哪种 imperfection，并要求专门的 stress test。
