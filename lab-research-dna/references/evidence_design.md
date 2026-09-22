# Evidence Design（E1~E5）+ 硬规则 + 泛化检查清单

> DNA-10 是 `FIELD_COMMON`：以下为高水平实验设计的领域通用原则，在本组语料中反复出现，不宣称为课题组独有。

## E1 — Performance claim → broad comparative evidence
多数据集/多站点/多设备 + 强 baseline 比较；若声称 generality，单一数据集通常不足。

## E2 — Mechanism claim → component ablation + mechanism visualization
- P031：IIM/CIM/ILAA/GLAA 全 ablation + feature distribution / gradient trajectory 支撑机制。
- P030：移除 confidence score，验证 TCP-driven fusion 的真实贡献。
- P044：SPL / graph / domain 组件变体 + 训练行为验证机制。
- 每个被声称的机制组件都必须有"移除后退化"的证据。

## E3 — Generalization claim → setting-matched hold-out
- unseen-site DG 必须真正无目标域数据（P039）。
- target-accessible DA 与 target-unseen DG 不能互相替代（P044 vs P039）。
- cross-subject / cross-device claim 必须用 subject / device 级 split，而非普通随机切分。

## E4 — Restoration claim → reconstruction quality + downstream utility
恢复类工作不能只报 PSNR/SSIM；P029 同时检查去噪图像的识别精度，证明身份信息被保留。

## E5 — Interpretability / biomarker claim → localization + task relevance
显著脑区/子网络、confidence time slice、saliency map 能支撑"模型关注了哪里"，但不能自动升级为因果 biomarker 结论。

## 硬规则
1. 任何 Innovation Generator 输出必须同时给出 `Required Evidence`：至少一个能区分新机制与更弱替代解释的实验。
2. 禁止用 target-visible 证据支撑 target-unseen claim。
3. 机制 claim 没有 ablation → 证据不足，claim 必须降级。

## 泛化检查清单（Generalization Claim Check 逐项核验）
- [ ] 训练时是否见过 target 数据？
- [ ] target labels 是否可用？
- [ ] 是否允许共享原始数据/特征（隐私约束）？
- [ ] split 是否为 subject-independent / site-held-out / device-held-out？
- [ ] 有无 distribution shift vs 普通 random split 的对照？
- [ ] personalization 是全局共享表示上的局部适配，还是完全独立模型？
- [ ] 目标是单一全局模型还是每站点个性化模型？
