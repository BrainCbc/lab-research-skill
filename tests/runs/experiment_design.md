# Test Run — Experiment Design
**Fixture:** tests/fixtures/experiment.json（置信度加权融合提升多模态情绪识别鲁棒性；识别不可靠模态并降权）

**Claim→Evidence map:**
| Claim | 类型 | 所需证据 |
|---|---|---|
| 置信度加权融合提升鲁棒性 | mechanism + performance | w/o 置信度加权的 ablation（E2，参照 P030）；多模态噪声 stress test |
| 能识别不可靠模态并降权 | mechanism | 置信度分数与模态真实可靠性（人工标注/合成噪声）的相关性；降权前后的权重分布可视化（E2） |

**Ablation plan:**
1. w/o confidence 模块（等权融合对照）
2. w/o 模态级改为样本级置信度（验证粒度选择的必要性）
3. 置信度替换为随机权重（排除"加权本身"的安慰剂效应）

**Hold-out / split design:** 跨被试 split（E3，参照 P035）；普通随机 split 仅作对照，不得作为泛化证据。

**Stress tests:** 单模态 dropout（模拟传感器失效）；模态内高斯噪声分级；跨被试分布漂移子集。

**Falsification experiment:** 若置信度分数与合成噪声水平无单调相关性，或随机权重达到相近性能，则"置信度机制有效"被证伪。同时检查确认偏差：置信度是否只是复述分类器自身输出（boundaries.md DNA-05 注意事项），需独立校准曲线。
