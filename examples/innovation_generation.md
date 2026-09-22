# Example — Innovation Generation

**输入：** RL1（动态脑网络），最近前作 P020（跨窗 topology evolution）、P030（TCP 置信度）、P040（temporal prior + hypergraph）。

## Skill 输出（3 个 hypothesis，展示 1 个完整）

### Hypothesis A — 跨被试动态演化对齐
- **Closest predecessors:** P020（跨窗演化显式建模）、P022（节点时空异质性）
- **Existing capability:** 已能建模单个被试内跨时间窗的拓扑演化（P020），P040 进一步引入时间先验与超图。
- **Unresolved limitation:** 所有工作都在单被试内建模演化；跨被试的演化轨迹存在个体差异，直接套用单被试模型会导致对齐失效（DNA-03 未覆盖"演化轨迹"这一层级的异质性）。
- **New setting & relaxed assumption:** 放宽"演化模式被试间一致"的隐含假设 → cross-subject 动态演化。
- **New gap:** G3（heterogeneity-decomposition gap）+ G5（temporal-scale gap）：演化轨迹本身的跨被试异质性未被拆解。
- **Core insight:** 把"演化轨迹"从个体特有信号中解耦出被试不变的演化原型，再做个性化残差建模。
- **Why not module stacking:** 改变的是 problem formulation（从单被试演化 → 跨被试演化对齐），不是加模块。
- **Required mechanism change:** 演化原型学习（原型轨迹字典）+ 个体残差分支；用 DNA-04 的解耦逻辑。
- **Required evidence:** (1) 跨被试 split 下的分类对比（E3）；(2) 移除原型分支的 ablation（E2）；(3) 演化原型可视化与临床一致性检查（E5 级别，不升级为 biomarker）。
- **Falsification risk:** 若跨被试演化轨迹本身噪声主导、原型无稳定性，则假设被证伪；需先做轨迹可重复性预实验。
- **Confidence:** Medium（跨被试在 RL4 有先例 P035，但 RL1 内无直接证据）

（Hypothesis B/C 略：B=长程先验的因果验证；C=窗口可靠性与演化的联合建模。）
