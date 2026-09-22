# Test Run — Generalization Claim Check
**Fixture:** tests/fixtures/generalization.json（claim 未见设备泛化好；实际用了目标设备无标签数据做对齐）

**Checklist verdict:**
- [x] 训练时是否见过 target 数据？—— 见过（目标设备无标签数据参与对齐）→ **target-accessible**
- [ ] target labels 是否可用？—— 不可用
- [x] split 是否为 device-held-out？—— 否，目标设备参与训练

**Mismatch flags:**
- 🔴 Claim"没见过的采集设备"（target-unseen）与 setting（target-accessible 对齐）错配。根据 DNA-12（`RESEARCH_LINE_SPECIFIC`，RL3）与 E3，DA 与 DG 不可互换。
- 若方法含设备特异性适配组件，其在新设备上的行为未经验证。

**Downgraded claim:**
"在目标设备无标签数据可用的无监督域适应 setting 下，跨设备识别精度相比基线提升 X%；在目标设备完全不可见条件下的泛化尚未验证。"
