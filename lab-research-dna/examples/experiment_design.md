# Example — Experiment Design

**输入 claims：** "我们的方法通过解耦身份与环境因素，在跨设备掌纹识别上更鲁棒，且去噪后的图像仍保留身份信息。"

## Skill 输出

**Claim→Evidence map:**
| Claim | 类型 | 所需证据 |
|---|---|---|
| 解耦身份/环境 | mechanism | 移除解耦模块的 ablation，身份/环境成分可视化（E2） |
| 跨设备更鲁棒 | generalization | device-held-out split，多设备交叉对比（E3）；不得只用随机 split |
| 去噪保留身份信息 | restoration | PSNR/SSIM + 去噪后识别精度（E4，参照 P029） |

**Ablation plan:**
1. w/o 解耦模块（验证 M1 机制）
2. w/o 环境分支（验证 nuisance 隔离的必要性）
3. 替换为简单特征拼接（弱替代解释对照）

**Hold-out / split design:** 按设备划分 train/test（如 P012/P031 的跨设备协议）；补充跨设备 + 低质量双重 stress test。

**Stress tests:** 高斯噪声分级（参照 P029 Table V）、缺失设备数据（G7）、光照变化子集。

**Falsification experiment:** 若"解耦后"的环境成分仍能预测身份（探针分类器精度显著高于随机），则解耦机制被证伪。
