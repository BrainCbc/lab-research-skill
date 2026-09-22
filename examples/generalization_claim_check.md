# Example — Generalization Claim Check

**输入 claim：** "我们的方法在未见过的站点上泛化能力很好。"
**实验设置：** 训练时用了目标站点的无标签数据做域对齐，测试集是该站点的有标签数据。

## Skill 输出

**Checklist verdict:**
- [x] 训练时是否见过 target 数据？—— 见过（无标签目标域数据用于对齐）→ **target-accessible**
- [ ] target labels 是否可用？—— 不可用（无监督 DA）
- [ ] split 是否为 site-held-out？—— 否，目标站点参与了训练

**Mismatch flags:**
- 🔴 Claim 声称"未见过的站点"（target-unseen），证据实际是 target-accessible DA setting。根据 DNA-12 / E3，两者不可互换（P039 vs P044 边界）。
- 该 setting 下的正确方法家族是 DA（参照 P044），不是 DG（P039）。

**Downgraded claim（改写为证据实际支撑的版本）：**
"我们的方法在目标站点无标签数据可用的域适应 setting 下，相比基线提升了跨站点精度；尚未验证在目标站点完全不可见（DG）条件下的泛化。"
