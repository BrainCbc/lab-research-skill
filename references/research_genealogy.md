# Stage 2 — Research Genealogy

## 1. Research Forest 总览

这 44 篇论文更适合表示为 **Research Forest**，而不是单一线性时间轴。当前识别出 7 条主研究线、6 篇 satellite，以及若干跨线方法桥接。

### RL1 Dynamic Functional Brain Network Representation and Spatio-Temporal Modeling

从动态/加权脑网络的表示出发，逐步把跨时间窗拓扑演化、长程依赖、神经异质性、结构/功能先验、置信度和高阶关系显式纳入模型。

- **P003 → P020 | EXTENDS | HIGH**：P003 已把动态脑网络的拓扑与时间变化联合表示作为核心问题；P020 进一步指出“独立窗口学习”无法捕获跨窗口高阶拓扑演化，并显式建模 topology evolution。
- **P020 → P022 | REFINES | HIGH**：P022 在动态脑网络基础上把问题进一步细化为神经节点的时空异质性与异质活动的时间传播机制；P022 的参考文献明确包含 P020。
- **P020 → P024 | REFINES | MEDIUM-HIGH**：P024 将 P020 一类跨窗口时空建模进一步聚焦到 long-interval temporal interactions，强调远距离时间窗之间的交互。
- **P020 → P025 | REFINES | HIGH**：P025 从脑区级动态交互推进到跨时间窗显式 topological evolution，并加入疾病相关/冗余约束；参考文献中包含 P020。
- **P020 → P026 | REFRAMES | MEDIUM-HIGH**：P026 不再只追求时空表征能力，而把“纯数据驱动、缺少结构/功能先验与可解释性”作为新的瓶颈。
- **P020 → P030 | REFINES | HIGH**：P030 延续动态脑网络跨窗口时空卷积，但进一步用 TCP confidence 对窗口预测进行可靠性加权，处理多窗口融合与不确定性。
- **P024 → P040 | GENERALIZES | MEDIUM-HIGH**：P040 将跨窗口关系从普通图上的时空交互推进到高阶 hypergraph attention，并继续强调跨窗口先验。
- **P025 → P040 | GENERALIZES | MEDIUM-HIGH**：P025 强调时空拓扑演化，P040 进一步用超图表达普通图难以充分刻画的复杂高阶时空拓扑。
- **P026 → P040 | COMBINES | MEDIUM**：P026 将功能/结构先验引入动态脑网络；P040 同样把“缺少跨窗口先验”列为限制，体现先验约束思路向高阶时空建模的延续。
- **P015 → P020 | PARALLEL_BRANCH | MEDIUM**：P015 针对加权边与层级节点关系提出一般脑网络表示；P020 面向动态网络时空演化。二者属于表示层面的平行分支，不构成直接前后继。

### RL2 Multi-Modal Brain Disease Diagnosis and Fusion

从多模态互补信息融合，演化到拓扑/时空联合建模、判别与可解释融合、区域异质性、类别不平衡以及不完整模态恢复。

- **P002 → P006 | GENERALIZES | MEDIUM-HIGH**：P002 关注多模态互补、高阶关系与判别融合；P006 将融合对象推进到多模态脑网络，并显式联合动态图的时空拓扑。
- **P002 → P014 | REFINES | MEDIUM-HIGH**：P014 延续多模态融合，但把 gap 明确转向共同空间中的判别结构与 biomarker interpretability。
- **P006 → P023 | REFINES | HIGH**：P023 延续多模态脑网络融合，进一步把 regional heterogeneity 和 disease-irrelevant information 解耦作为核心问题。
- **P010 → P023 | REFINES | MEDIUM**：P010 已从简单特征融合推进到双模态脑网络内部拓扑/社区结构；P023 进一步显式建模跨模态区域异质性。
- **P014 → P036 | GENERALIZES | HIGH**：P036 将完整多模态诊断推进到 missing modality 场景，并从邻域语义与缺失模态潜在信息恢复角度处理不完整数据；其参考文献包含 P014。
- **P002 → P036 | GENERALIZES | MEDIUM**：P002 代表完整多模态互补融合基线问题；P036 把问题设定扩展到模态缺失并要求恢复分布一致特征。
- **P009 → P036 | PARALLEL_ROBUSTNESS | MEDIUM**：P009 处理类别不平衡与模态异质性，P036 处理缺失模态；二者体现多模态脑诊断从“融合”向现实数据缺陷鲁棒性的平行扩展。

### RL3 Multi-Site / Cross-Site Brain Generalization, Adaptation and Federated Learning

围绕多站点分布偏移、隐私、目标站点可见性和个体/站点异质性，形成联邦适应、主动对抗适应、域泛化、个性化联邦和图域适应等分支。

- **P007 → P042 | REFINES | HIGH**：P007 以联邦适应解决多站点异质性与隐私；P042 在同一隐私约束场景下进一步处理跨站点分布校准与个性化模型，并明确引用 P007。
- **P008 → P044 | UNIFIES | MEDIUM-HIGH**：P008 从 center/feature/label 多层不确定性做主动对抗适应；P044 将 sample-level 与 site-level heterogeneity、outliers 和图拓扑保持统一进 graph domain adaptation。
- **P007 → P039 | GENERALIZES_SETTING | MEDIUM**：P007 面向可参与训练/迁移的多站点联邦适应；P039 进一步切换为 target-unseen 的 domain generalization 假设，并处理类内跨站点结构多样性。
- **P039 → P044 | PARALLEL_SETTING | HIGH**：两篇均处理多站点分布偏移，但 P039 是无目标域数据的 DG，P044 是有目标站点参与的 DA；应视为同一大问题下互补而非前后继。

### RL4 Multi-Modal Emotion / Cross-Subject Trustworthy Physiological Recognition

从多模态情绪识别中的不确定性与动态置信度，扩展到跨个体表征对齐、情绪分布学习以及跨被试睡眠阶段的可信融合。

- **P018 → P027 | EXTENDS | MEDIUM-HIGH**：P018 系统建模多模态不确定性与动态置信度；P027 在此类鲁棒融合问题上进一步加入跨个体分布漂移与 subject-independent discriminative representation。
- **P018 → P035 | EXTENDS | HIGH**：P035 将多模态异质性问题推进到跨被试场景，联合学习 subject-independent representation 与 EEG/eye-movement common feature；其问题逻辑与 P018 的不确定融合连续。
- **P027 → P033 | BRANCHES_TO_NEW_TASK | MEDIUM-HIGH**：P033 明确引用 P027，并把多模态情绪建模从单一类别/跨个体识别拓展到 emotion distribution learning 与 label correlation。
- **P035 → P033 | BRANCHES_TO_NEW_TASK | MEDIUM-HIGH**：P033 明确引用 P035；其新增重点不是继续 subject alignment，而是异质多模态下的混合情绪分布与标签相关性。
- **P018 → P043 | CROSS_TASK_METHOD_TRANSFER | HIGH**：P043 明确引用 P018，并把动态/可信多模态融合思想迁移到跨被试睡眠阶段分类，同时加入时间与样本层不确定性。
- **P035 → P043 | GENERALIZES_TO_SLEEP | MEDIUM-HIGH**：P035 的跨被试多模态对齐与 P043 的跨被试睡眠异质模态融合具有直接问题连续性，但 P043 增加 trustworthy/dynamic uncertainty 目标。

### RL5 EEG Visual Decoding and EEG Biometrics

一支关注 EEG-视觉语义解码和对齐，另一支关注脑纹身份表征解耦；二者共享 EEG 表示学习背景但任务不同。

- **P028 → P041 | REFINES | HIGH**：P028 建立 EEG→视觉层级神经表征；P041 明确引用 ViEEG，并把问题推进到复杂场景中的 foreground/background perceptual asymmetry 与 semantic misalignment。

### RL6 Palmprint Biometrics: Cross-Device, Robustness and Image Quality

覆盖跨设备域差异、安全攻防、超分辨/去噪、个性化联邦以及同质/异质掌纹识别，形成多个互补子分支。

- **P012 → P031 | REFRAMES | MEDIUM-HIGH**：P012 通过跨手机图像生成/域迁移缓解设备差异；P031 把同一 cross-device 问题重构为隐私保护的 personalized federated learning，并显式分解 identity/context drift。
- **P017 → P029 | EXTENDS | HIGH**：P017 针对低质量掌纹做超分辨、恢复纹理/边缘；P029 进一步针对噪声退化做掌纹内在特征驱动去噪，形成清晰的图像质量恢复子线。
- **P012 → P038 | GENERALIZES | MEDIUM**：P012 聚焦跨智能手机域差异；P038 将识别设定扩展为 homogeneous/heterogeneous palmprint recognition，并强调高效特征投影。

### RL7 Digital Pathology and Multi-Omics Cancer Analysis

围绕 WSI 与组学/临床结局联合建模，从肿瘤微环境与生存关联、特征感知多模态生存分析，发展到 WSI 多实例多任务联合预测。

- **P004 → P016 | EVOLVES_TASK_SCOPE | MEDIUM-HIGH**：P004 联合 WSI 与多组学刻画 TIL-tumor 生存关联；P016 将 WSI 建模推进到 clinical outcome 与 genomic profile 的多实例多任务联合预测。二者各自的明确 preliminary work 均在语料外。
- **P005 → P016 | EVOLVES_TASK_SCOPE | MEDIUM-HIGH**：P005 通过 feature-aware multi-modal metric learning 做生存分析；P016 把目标扩为 WSI 上的多任务 clinical/genomic joint prediction。

## 2. 跨研究线方法桥接

- **P034 ↔/→ P031 | CONCEPTUAL_PARALLEL | MEDIUM-HIGH**：P034 在 EEG biometric 中解耦 identity-related 与 identity-invariant bias；P031 在掌纹中解耦 identity/contextual features。两者同年、跨模态，属于概念并行而非版本关系。
- **P018 ↔/→ P030 | CROSS_LINE_METHOD_TRANSFER | HIGH**：P030 的参考文献明确包含 P018，并采用 true class probability (TCP) 作为窗口置信度标准，把情绪多模态中的 confidence-aware 思想迁移到动态脑网络多窗口融合。
- **P006 ↔/→ P020 | CROSS_LINE_METHOD_EVOLUTION | MEDIUM-HIGH**：P006 在多模态脑网络中联合时空图卷积；P020 将重点收缩到动态脑网络跨时间窗高阶拓扑演化，体现时空图建模从 multimodal fusion 向 temporal topology evolution 的迁移。

## 3. 关键结构性结论

1. **动态脑网络线不是简单“换 GNN”**：主线从窗口内/窗口间联合表示，逐步推进到显式拓扑演化、长间隔依赖、节点异质性、先验可解释性、置信度与高阶超图关系。
2. **多模态脑诊断线从“互补融合”走向“现实约束下的鲁棒融合”**：判别性/可解释性、区域异质性、不平衡与缺失模态逐步成为独立问题。
3. **多站点脑诊断至少存在三种不同假设路线**：隐私约束下的 federated adaptation/personalization、target-accessible domain adaptation、target-unseen domain generalization。它们不能互相替代。
4. **情绪/生理信号方向出现明显方法迁移**：confidence-aware / cross-subject alignment 从情绪识别扩展到动态脑网络或睡眠阶段等任务。
5. **掌纹方向不是单链**：跨设备、隐私联邦、图像质量、安全攻防和异质识别是相互关联但不同的问题分支。
