# Example — Paper Story

**输入：** problem=动态脑网络分类；gap=现有方法只在单时间窗内建模，忽略跨窗拓扑演化；method=显式跨窗演化建模+时间先验；evidence=多数据集对比 + ablation + 演化可视化。

## Skill 输出

**Narrative outline:**
1. **Background：** 动态功能脑网络（DFBN）通过滑动窗刻画脑区动态连接，已广泛用于脑疾病诊断。
2. **Prior limitation：** 现有方法聚焦单时间窗内的拓扑学习（P003 及同类），忽略了跨时间窗的拓扑演化信息（W1 句式；对应 DNA-01 / G1）。
3. **Gap：** 跨窗演化未被显式建模，导致长程动态模式丢失（G5）。
4. **Insight：** 把"演化"提升为一等建模对象，用可学习的跨窗传播机制显式表达（DNA-01）。
5. **Method：** 跨窗演化模块（对应 gap 的演化部分）+ 时间先验约束（对应可解释部分）—— 每个组件唯一对应 gap 的一个组成（W2）。
6. **Evidence：** 多数据集对比（E1）→ 移除演化模块的 ablation（E2）→ 演化轨迹可视化（E5 级别，不升级为 biomarker）。
7. **Contribution：** (a) 首次将跨窗拓扑演化显式建模；(b) 时间先验约束提升可解释性；(c) 在 X/Y 数据集上验证。每条在证据中有直接对应（W3）。

**Tension check:** ✅ limitation-first 张力成立（单窗 vs 跨窗）；✅ gap–mechanism 对齐（演化↔演化模块，先验↔先验约束）；✅ claim–evidence 闭环（每条贡献有表/图对应）。
> 注：以上为 problem-story 结构建议，不声称任何"课题组独有写作风格"。
