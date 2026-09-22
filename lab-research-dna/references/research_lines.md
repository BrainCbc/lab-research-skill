# Research Lines（RL1~RL7 线内综合 + satellites）

> Stage 2 Research Forest 的线内蒸馏。`MEDIUM` / `MEDIUM-HIGH` 的 Stage 2 边仍视为分析性 genealogy hypothesis。

## RL1 — Dynamic Functional Brain Network Representation and Spatio-Temporal Modeling
- **演化：** P003（动态拓扑+时间联合表示）→ P020（显式跨窗 topology evolution）→ 分叉：P022（节点时空异质性传播）、P024（long-interval）、P025（跨窗演化强化）、P026（结构/功能先验+可解释）、P030（TCP 置信度）→ P040（temporal prior + hypergraph）。
- **线内模式：** 问题从"能否建动态网络"推进到"哪些时间尺度/关系阶数/异质性/先验/可靠性仍未显式建模"；方法与 gap 一一对应。
- **例外：** P015 是一般脑网络表示的平行分支，不接入 P003→P020 主干。
- **Idea 方向：** 用 DNA-11 五轴（时间尺度×关系阶数×节点异质性×先验×置信度）定位未覆盖空间。

## RL2 — Multi-Modal Brain Disease Diagnosis and Fusion
- **演化：** P002（互补+高阶判别融合）→ P006（多模态融合+时空拓扑）→ 转向现实缺陷：P009（不平衡）、P014（判别/可解释）、P023（区域异质性+disease-irrelevant 解耦）、P036（缺失模态）。
- **线内模式：** 基本融合成立后，创新来源转向数据缺陷、结构异质性、可解释性；后续问题不是"更复杂的 fusion block"，而是"哪种不完美条件未解决"。
- **例外：** P010 偏社区/拓扑结构化融合，不归鲁棒性分支。

## RL3 — Multi-Site / Cross-Site Brain Generalization, Adaptation and Federated Learning
- **演化：** P007（联邦适应+隐私）→ P008（center/feature/label 三层不确定性 DA）→ 三条互补路线：P039（target-unseen DG）、P044（target-accessible graph DA）、P042（隐私约束个性化 FL）。
- **线内模式：** 方法家族由 setting assumption 决定；异质性细化为 sample/site/class/prototype/personalization 层级。
- **关键边界：** DG/DA/FL 不构成优劣关系；P039 与 P044 是 target assumption 不同的平行路线；禁止用 target-visible 实验证 unseen-site claim。

## RL4 — Multi-Modal Emotion / Cross-Subject Trustworthy Physiological Recognition
- **演化：** P018（多模态 uncertainty + 动态 confidence）→ P027/P035（跨个体漂移、subject-independent 表示）→ P033（emotion distribution/label correlation 分叉）→ P043（可信融合迁到跨被试睡眠，含 modality/subject/temporal/sample 不确定性）。
- **线内模式：** "融合"被重写为"在跨主体和不确定性下，哪些信息值得信任、如何对齐"。

## RL5 — EEG Visual Decoding and EEG Biometrics
- **演化：** P028→P041（层级视觉神经表征 → 复杂场景 foreground/background 感知不对称 + 语义不对齐）；P034（EEG biometric 身份解耦）为独立分支。
- **线内模式：** 两分支都强调任务相关 vs 干扰信息分离，但任务目标不同，不强行合并 genealogy。

## RL6 — Palmprint Biometrics: Cross-Device, Robustness and Image Quality
- **演化：** 天然多分支：P012/P031（跨设备：生成/域迁移 vs 隐私联邦+解耦）；P017→P029（质量恢复：超分辨→噪声抑制+身份保持）；P013（攻防安全）；P038（同质/异质识别+高效投影）。
- **线内模式：** 新问题来自移动应用真实约束：设备差异、数据缺失、隐私、噪声/低分辨率、安全、异质设置。

## RL7 — Digital Pathology and Multi-Omics Cancer Analysis
- **演化：** P004（WSI 空间交互+多组学生存关联）→ P005（feature-aware metric learning 生存分析）→ P016（WSI clinical outcome + genomic 多实例多任务）。
- **线内模式：** 关注空间关系、模态互补、特征选择、任务范围扩展。
- **边界：** 明确前身多在 44 篇之外，不可过度构造线内直接继承。

## Satellites（不强行并入主线）
P001、P011、P019、P021、P032、P037。用途：识别可跨线迁移的方法思想（如 P001 的 sample reweighting/confidence、P021 的 graph structure awareness）；禁止用它们证明"全组统一路线"。
