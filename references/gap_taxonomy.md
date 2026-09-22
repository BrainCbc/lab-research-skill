# Gap Taxonomy（G1~G7）

> Gap Check 与 Innovation Generation 共用。gap 必须有前作原文或实验条件支撑；不得虚构"尚未考虑"的因素。

## G1 — Ignored-factor gap（被忽略因素）
典型形式：现有方法关注 A，但忽略 B，导致在 C 条件下失效。
代表：P020（跨窗 topology evolution）、P023（regional heterogeneity）、P026（先验/可解释）、P041（前景/背景）、P044（sample/site 异质性）。

## G2 — Assumption-relaxation gap（假设放宽）
从完整/同域/已知目标/同主体/高质量转向 missing modality、unseen site、cross-subject、cross-device、noisy data。
代表：P036、P039、P043、P031、P029。

## G3 — Heterogeneity-decomposition gap（异质性拆解）
不再把 domain shift 当单一分布差，拆到 center/feature/label、regional、identity/context、sample/site 等层级。
代表：P008、P023、P031、P044。

## G4 — Reliability / uncertainty gap（可靠性）
问题不再是"有没有信息"，而是"不同信息是否同样可信"。
代表：P001（target sample confidence）、P018（modality TCP）、P030（window TCP）、P043（temporal/sample uncertainty）、P044（sample difficulty）。

## G5 — Structure-order / temporal-scale gap（结构阶数/时间尺度）
现有表示刻画局部/单窗/低阶关系，但不能刻画 long-range、cross-window、high-order、hierarchical topology。
代表：P020、P024、P025、P040。

## G6 — Interpretability / prior gap（可解释/先验）
性能导向模型缺少领域先验或 biomarker interpretability。
代表：P014、P026、P040。

## G7 — Data-imperfection gap（数据不完美）
现实数据的 imbalance、missing modality、noise、low resolution、incomplete cross-device samples 直接成为问题定义。
代表：P009、P012、P017、P029、P036。

## 使用边界
- 所谓新 gap 若只是换数据集/换模型，不能自动视为科学问题升级。
- 不得根据 absence 直接声称"从未有人做过"。
