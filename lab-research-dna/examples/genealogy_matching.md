# Example — Genealogy Matching

**输入：** "我们想做跨站点的 EEG 情绪识别，目标站点数据不可用，还要保护隐私。"

## Skill 输出

**Research line:** RL4（多模态情绪/跨被试可信生理识别）为主，RL3（多站点泛化/联邦）为辅。

**Branch & setting assumptions:**
- target visibility = unseen（目标站点数据不可用）→ DG 路线
- privacy = constrained（隐私保护）→ 联邦/去中心化
- 注意：unseen + 隐私约束的组合在语料内无完全对应的单篇工作（P039 是 DG 但无联邦；P007/P042 是联邦但 target 可见），属于分支交叉的新 setting，需标注`外推`。

**Closest predecessors:**
- P039（target-unseen DG，HIGH 相关；关系：setting 参照，非版本继承）
- P018（多模态 uncertainty + confidence，机制可迁移 DNA-08）
- P035（cross-subject 对齐，MEDIUM-HIGH genealogy hypothesis）
- P007（联邦适应，隐私约束参照）

**Relation nature:** setting 参照 + 机制迁移，无直接版本继承关系。

**Warnings:**
- 不得把 P039 写成"前作"，它是平行 setting 的参照，不是被改进的对象。
- 跨 RL4/RL3 的机制迁移（DNA-08）需在新任务中重做失败模式定义与证据（M6）。
- 44 篇内无 conference→journal 版本对，不虚构。
