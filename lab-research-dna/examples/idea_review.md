# Example — Idea Review

**输入 idea：** "把 Mamba 换掉 Transformer，在 ADNI 上做多模态脑疾病分类，期望精度更高。"

## Skill 输出

**Verdict:** Weak

**Matched DNA:** 无。最接近的是 DNA-06（关系结构），但该 idea 未涉及任何关系结构变化。

**Gap assessment:** 未映射到 G1–G7。ADNI 上多模态融合已有 P002/P006/P023 等工作；"换 backbone"没有指出前作在何种 setting 下因何失败，不构成 G1（无被忽略因素）也不构成 G2（setting 未变）。

**Stress test:** 四问中第 1 问为"是"（仅换 backbone），第 2 问为"否"（problem / assumption / mechanism / evidence 均未变）→ 弱创新。

**Risks:** 即使精度提升，也无法区分是 Mamba 有效还是调参/数据划分所致；投稿时易被质疑 novelty。

**Confidence:** High（判定依据充分）

**改写建议（按能力 3）：** 若发现现有融合方法在"长序列多模态"上因二次复杂度无法建模跨模态长程依赖（G5），可转为"用状态空间模型显式建模跨模态长程依赖"，并要求与 Transformer 基线的显存/长度 scaling 对比（E2）。
