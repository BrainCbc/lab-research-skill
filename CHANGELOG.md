# Changelog

## v1.0.1 — 2026-09-22
- 将 Skill `name` 从 `lab_research_dna` 改为 `lab-research-dna`，与发布目录和显式调用 `$lab-research-dna` 对齐。
- 删除 Muse 构建环境的临时绝对路径依赖。
- 将 Stage 2 的 `research_genealogy.md`、`relation_table.csv`、`research_line_membership.csv`、`conference_journal_check.md` 纳入 `references/`，使 GitHub/Codex 发布包自包含。
- 更新 Codex 用户级与仓库级安装说明。
- 增强结构测试：校验 Skill 名称、目录匹配、自包含谱系文件和无外部 workspace 路径。

## v1.0.0 — 2026-09-22
- 首版：13 条 Research DNA、8 个能力、references/examples/tests。
