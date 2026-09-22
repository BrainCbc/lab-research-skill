# Method Logic（M1~M6，高层方法逻辑）

> 只保留"为什么这样设计"的方法逻辑，禁止退化为技术名词列表（GNN/Transformer/attention 本身不是 DNA）。

## M1 — Explicit decomposition（显式拆解）
把混杂因素拆成可学习成分：identity/context（P031）、identity-related / identity-invariant bias（P034）、regional heterogeneity + disease-irrelevant（P023）。关键不是"用了 disentanglement"，而是先定义哪些信息应保留、哪些应隔离，并给出可验证的分离证据。

## M2 — Reliability-aware selection / weighting（可靠性感知）
对 target sample、pseudo-label、modality、time window、hard sample 估计 reliability，用于 weighting / self-paced / active selection。代表：P001、P007、P012、P018、P030、P043、P044。注意：confidence 需独立依据与校准，防止自训练确认偏差。

## M3 — Relational / topological modeling（关系/拓扑建模）
关系结构从 high-order sample relations、brain graph、community、spatio-temporal topology 推进到 hypergraph。代表：P002、P006、P020、P040、P004、P021。关系结构必须有领域语义，能捕获平铺特征无法表达的信息。

## M4 — Prior-guided representation（先验引导表示）
用 cognitive / structural-functional / temporal-similarity / semantic-saliency prior 约束纯数据驱动表示。代表：P009、P026、P040、P041。先验须有独立依据，需实验证明增益非额外参数所致。

## M5 — Setting-specific adaptation family（设定决定的方法家族）
多站点方法不能脱离 setting 选择：federated / personalized、DG、DA 对 target visibility、privacy、model personalization 的假设不同。代表：P007、P039、P042、P044。先填 setting 再选家族。

## M6 — Cross-line mechanism transfer（跨线机制迁移）
已观察到的强桥接：confidence-aware（P018→P030）、spatio-temporal graph（P006→P020）。强迁移保留机制逻辑并重做任务对象与证据，不复制网络结构；证据有限，不可假设任意线间可迁。

## 组合决策规则
- 先由 gap 类型定主逻辑（G1→M1/M4，G2→M5+setting，G3→M1，G4→M2，G5→M3，G6→M4，G7→M2/M5）。
- 一个 hypothesis 只用一个主逻辑 + 至多一个辅助逻辑；多逻辑叠加必须能分别 ablation。
