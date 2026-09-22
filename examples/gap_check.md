# Example — Gap Check

**输入 gap 声称：** "现有睡眠分期方法没有用 Transformer，我们用 Transformer 来做多导睡眠分期。"

## Skill 输出

**Gap type:** 未分类（无法映射到 G1–G7）。

**Evidence support:** 无。前作 P043 已处理 heterogeneous multi-modal 睡眠数据的跨被试漂移与可信融合；"没用 Transformer"是技术选型描述，不是失败条件。

**Pseudo-gap verdict:** 是伪 gap。属于"换 backbone"类型：problem / assumption / mechanism / evidence 均未变化。

**Reformulation（按 DNA-01 句式）：**
"现有方法（P043 等）能够处理多模态睡眠数据的跨被试漂移，但忽略了睡眠阶段转移的长程时间依赖在注意力建模中的显式约束，导致 N1/N2 易混淆阶段的边界判定不稳定；我们把阶段转移先验显式建模为转移约束。"
→ 映射到 G1（被忽略因素：阶段转移结构）+ G6（先验），需补充混淆矩阵证据（E2/E5）。
