# Test Run — Genealogy Matching
**Fixture:** tests/fixtures/genealogy.json（缺失模态多模态脑疾病诊断：部分被试缺 fMRI 只有 sMRI）

**Research line:** RL2（多模态脑疾病诊断与融合）主线；缺失模态分支。

**Branch & setting assumptions:**
- modality availability = incomplete（部分被试缺失 fMRI）
- task = 脑疾病诊断（AD/癫痫类，参照 P036）

**Closest predecessors:**
- P036（缺失模态 adjacent-aware 恢复，HIGH 相关：直接前作候选）
- P023（区域异质性 + 解耦，MEDIUM-HIGH genealogy hypothesis：机制参照）
- P006（多模态时空融合，MEDIUM：早期融合基线）

**Relation nature:** P036 为最近直接前作（同分支）；P023/P006 为机制/基线参照。Stage 2 MEDIUM 边已按规则标注为分析性假设。

**Warnings:**
- 缺失模式（随机缺失 vs 整模态缺失 vs 被试级缺失）必须在 problem 定义中明确，不同缺失模式对应不同方法家族（DNA-13 boundary）。
- 不得把 P036 写成"已解决缺失模态"，其恢复机制在高缺失率下的边界即新 gap 来源（G2）。
