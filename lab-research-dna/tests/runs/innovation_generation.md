# Test Run — Innovation Generation
**Fixture:** tests/fixtures/innovation.json（RL6 掌纹，移动端部署）

## Hypothesis 1 — 跨设备+低质量联合退化下的身份保持恢复
- **Closest predecessors:** P012（跨设备生成/域迁移）、P029（噪声抑制+身份保持）
- **Existing capability:** P012 处理跨设备差异，P029 处理低质量恢复并保持身份特征，但两者独立。
- **Unresolved limitation:** 移动端真实场景是跨设备与低质量同时出现；P012 假设输入质量足够，P029 假设单设备分布。
- **New setting & relaxed assumption:** 放宽"退化因素单一"的隐含假设 → 跨设备 × 低质量联合退化（G7）。
- **New gap:** G7（Data-imperfection gap）：联合退化下的身份信息保持未被建模。
- **Core insight:** 把"设备域"与"质量退化"解耦为两个正交的 nuisance 因素，分别建模后再联合恢复（DNA-03 + DNA-04）。
- **Why not module stacking:** 改变 problem formulation（从单退化 → 联合退化），不是把两个模型拼接。
- **Required mechanism change:** 双分支解耦（设备分支/质量分支）+ 身份一致性约束。
- **Required evidence:** 跨设备×噪声分级联合 stress test（E3）；w/o 任一分支的 ablation（E2）；恢复后识别精度（E4）。
- **Falsification risk:** 若联合退化下身份信息已不可恢复（信息论下界），则方向证伪；需先做可恢复性预实验。
- **Confidence:** Medium

## Hypothesis 2 — 隐私约束下跨设备个性化的小样本适配
- **Closest predecessors:** P031（隐私联邦+解耦）、P012（跨设备）
- **Existing capability:** P031 做多站点个性化联邦；P012 做跨设备迁移但无隐私约束。
- **Unresolved limitation:** 新设备上线时只有极少样本，且不能上传原始数据（G2：隐私约束 + 小样本）。
- **New setting & relaxed assumption:** 放宽"新设备有充足数据"的假设 → few-shot 跨设备 + 联邦隐私。
- **New gap:** G2（Assumption-relaxation gap）。
- **Core insight:** 用 P031 的 identity/context 解耦思想，只传输身份相关原型做 few-shot 适配（DNA-08 跨线迁移抽象机制）。
- **Why not module stacking:** 迁移的是"解耦后只传任务相关成分"的机制逻辑，重做 few-shot 适配对象与证据。
- **Required mechanism change:** 原型级联邦适配协议 + 小样本校准。
- **Required evidence:** 新设备 few-shot（1/5-shot）跨设备协议（E3）；隐私泄露探针实验；w/o 解耦的对照（E2）。
- **Falsification risk:** 若原型传输仍泄露可重建的身份信息，则隐私 claim 证伪。
- **Confidence:** Medium-Low（跨线迁移，DNA-08 为 MEDIUM-HIGH 假设）

## Hypothesis 3 — 质量感知的自适应采集反馈
- **Closest predecessors:** P029（质量恢复）、P017（超分辨）
- **Existing capability:** 已能对低质量图像做恢复。
- **Unresolved limitation:** 恢复是事后补救；采集端不知道当前图像是否"足够好"（G4：可靠性未被显式建模）。
- **New setting & relaxed assumption:** 把"采集质量不可控"显式化 → 质量感知的采集-识别闭环。
- **New gap:** G4（Reliability gap）：图像质量置信度未进入识别决策。
- **Core insight:** 用质量分数做识别置信度门控：低质量时触发重采或降权（DNA-05）。
- **Why not module stacking:** 改变的是系统问题定义（单次识别 → 采集-识别闭环），新增决策机制。
- **Required mechanism change:** 质量-身份联合置信度估计 + 门控策略。
- **Required evidence:** 门控前后的端到端识别率对比；质量分数校准曲线（E2，防止确认偏差，见 boundaries.md）。
- **Falsification risk:** 若质量分数与识别失败无相关性，则机制无效。
- **Confidence:** Medium
