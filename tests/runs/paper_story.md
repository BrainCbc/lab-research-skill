# Test Run — Paper Story
**Fixture:** tests/fixtures/story.json（跨被试多模态睡眠分期）

**Narrative outline:**
1. **Background：** 多模态睡眠分期依赖 EEG/眼动等多导信号，已有可信融合方法处理模态不确定性（P018、P043）。
2. **Prior limitation：** 现有可信融合在单被试内建模不确定性（P018），或虽考虑跨被试但未显式拆解"模态不可靠"与"被试漂移"两类不确定性的不同来源（W1 句式；对应 DNA-03 / G3+G4）。
3. **Gap：** 跨被试条件下两类不确定性混杂，单一置信度机制无法分别处理。
4. **Insight：** 把不确定性拆解到模态层与被试层，分别估计可信度再联合决策（DNA-03 + DNA-05）。
5. **Method：** 模态置信度分支（对应模态不可靠）+ 被试对齐分支（对应分布漂移）—— 每个组件唯一对应 gap 的一个组成（W2）。
6. **Evidence：** 跨被试 split 对比（E3）→ 双分支各自 ablation（E2）→ 不确定性分数可视化（E5 级别，不升级为因果结论）。
7. **Contribution：** (a) 模态-被试双层不确定性拆解；(b) 跨被试可信融合框架；(c) 在 X 数据集上的验证。每条在证据中有直接对应（W3）。

**Tension check:** ✅ limitation-first 张力成立（单被试内 vs 跨被试双层）；✅ gap–mechanism 对齐；✅ claim–evidence 闭环。
> 注：以上为 problem-story 结构建议，不声称任何"课题组独有写作风格"。
