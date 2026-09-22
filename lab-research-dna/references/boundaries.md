# Exceptions & Boundaries（反例与边界，全部能力共用）

## 全局边界
- 无外部对照组：`lab-recurring` ≠ `lab-unique`，禁止声称独有或普适。
- Stage 2 中 MEDIUM / MEDIUM-HIGH 的边是分析性 genealogy hypothesis，不升级为作者声明。
- 44 篇内无 confirmed conference→journal direct-version pair，不得虚构版本关系。
- 技术名词（GNN / Transformer / attention / contrastive）本身不构成 Research DNA。
- 本 skill 覆盖范围限于 44 篇语料的任务家族（脑网络/多模态/多站点/生物特征/病理组学）；超出时标注`外推`并降 confidence。

## Pattern-specific 注意事项
- **Disentanglement（DNA-04/M1）：** 必须有任务相关/nuisance 的可验证定义，否则是无法证伪的命名。
- **Confidence / self-paced（DNA-05/M2）：** 需独立 calibration、ablation 或学习轨迹证据，防止确认偏差。
- **Prior（DNA-07/M4）：** 先验可能引入 bias，需证明增益非额外参数所致。
- **Graph / high-order（DNA-06/M3）：** 关系结构须有领域语义，不能因"图模型更先进"而用。
- **Assumption relaxation（DNA-02）：** 更难的 setting 只有引入新学习问题时才是创新；纯换数据集不是。
- **Cross-line transfer（DNA-08/M6）：** 强证据桥接数量有限，不可假设任意线间可迁。

## 研究线边界
- RL1：P015 是平行表示分支，不接入动态主干。
- RL3：DG / DA / FL 由 target visibility 与 privacy 区分，不写优劣关系。
- RL5：P034（EEG biometric）与 P028→P041（EEG-visual decoding）任务不同，不合并。
- RL6：cross-device/privacy、quality restoration、安全攻防是互补分支，非单链。
- RL7：明确前身多在 44 篇之外，不可过度构造线内继承。

## 重要反例速查
- P039（DG）vs P044（DA）：target assumption 不同的平行路线，非前后继。
- P015 vs RL1 主干：平行分支。
- P031 vs P034 的 disentanglement：跨任务概念并行，非版本关系。
- Satellites（P001/P011/P019/P021/P032/P037）：不用于证明统一 genealogy。
