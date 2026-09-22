# Lab Research DNA Skill v1.0.1

把课题组 44 篇论文的 Stage 3 蒸馏成果（13 条 Research DNA）工程化为可执行的科研助手技能。

## 知识来源（冻结）
- Stage 3 `lab_research_dna.md / .json`（13 条 DNA：DNA-01~DNA-13）
- 配套：research_strategy / gap_patterns / innovation_patterns / method_patterns / evidence_patterns / generalization_patterns / writing_patterns / exceptions_and_boundaries
- Stage 2 谱系材料已打包进 `references/`，仅用于按需回查关系、confidence 与证据定位，不引入新知识。

本 skill 不重新分析论文、不发明新 DNA。引用 DNA 时必须带 specificity 标签（`LAB_RECURRING_NOT_PROVEN_UNIQUE` / `FIELD_COMMON*` / `RESEARCH_LINE_SPECIFIC`），禁止把组内复现模式说成独有或普适。

## 安装（Codex）

### 方式 A：用户级全局安装
把整个 `lab-research-dna/` 文件夹放到：

```text
~/.agents/skills/lab-research-dna/
```

Windows 对应：

```text
C:\Users\<你的用户名>\.agents\skills\lab-research-dna\
```

确保最终存在：

```text
~/.agents/skills/lab-research-dna/SKILL.md
```

### 方式 B：仓库级安装
若只希望该 Skill 在某个项目仓库内生效，放到：

```text
<repo>/.agents/skills/lab-research-dna/
```

### 从 GitHub clone 到全局 Skill 目录

```bash
git clone https://github.com/BrainCbc/lab-research-skill.git ~/.agents/skills/lab-research-dna
```

Skill 为自包含版本，不依赖 Muse workspace 或其他绝对路径。安装/更新后若 Codex 未立即显示，重启 Codex。

## 使用
触发语示例：
- "帮我评审一下这个 idea" → Idea Review
- "基于 RL1 生成几个创新点" → Innovation Generation
- "这个 gap 成立吗" → Gap Check
- "我们的贡献相对 P044 增量够吗" → Contribution Check
- "这个工作最接近哪篇前作" → Genealogy Matching
- "ablation 怎么做" → Experiment Design
- "我们能 claim 未见站点的泛化吗" → Generalization Claim Check
- "帮我组织引言逻辑" → Paper Story

8 个能力的完整工作流与输出契约见 `SKILL.md`；示例见 `examples/`（每能力一个）。可在 Codex 中显式调用 `$lab-research-dna`，也可让 Codex 根据 `description` 自动选择。

## 测试
```bash
cd lab-research-dna
python3 tests/test_structure.py   # 结构/引用完整性测试
python3 tests/test_contracts.py   # 输出契约测试（基于 tests/runs/ 的实际执行记录）
```
`tests/fixtures/` 为测试输入，`tests/runs/` 为各能力在 fixture 上的实际执行输出（已随包交付，可复核）。

## 维护
- **知识冻结**：`references/` 内容对应 Stage 3 v1.0，默认不改。如需更新（新增论文/修正 DNA），同步更新 `references/dna_patterns.md`、`examples/` 相关用例，并在本文件记录版本号与变更。
- **版本记录**：
  - v1.0.1（2026-09-22）：GitHub/Codex 发布修订；Skill 名称改为 `lab-research-dna`，移除 Muse 临时绝对路径，打包 Stage 2 谱系核心文件，增强自包含性。
  - v1.0.0（2026-09-22）：首版，13 条 DNA，8 能力，测试通过。

## 目录结构
```
lab-research-dna/
├── SKILL.md               # 能力路由 + 工作流 + 输出契约 + 全局规则
├── README.md              # 本文件
├── references/            # 按需加载的知识文件
│   ├── dna_patterns.md
│   ├── research_lines.md
│   ├── research_genealogy.md
│   ├── relation_table.csv
│   ├── research_line_membership.csv
│   ├── conference_journal_check.md
│   ├── gap_taxonomy.md
│   ├── innovation_operators.md
│   ├── method_logic.md
│   ├── evidence_design.md
│   ├── writing.md
│   └── boundaries.md
├── examples/              # 8 个能力的完整示例
└── tests/
    ├── test_structure.py
    ├── test_contracts.py
    ├── fixtures/
    └── runs/
```
