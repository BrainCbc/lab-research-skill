#!/usr/bin/env python3
"""结构/引用完整性测试：不依赖任何第三方库。"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
failures = []


def check(cond, msg):
    if not cond:
        failures.append(msg)
    print(("PASS " if cond else "FAIL ") + msg)


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()


# 1. 必需文件
for rel in ["SKILL.md", "README.md"]:
    check(os.path.isfile(os.path.join(ROOT, rel)), f"必需文件存在: {rel}")

# 2. references/ 8 个知识文件
REFS = ["dna_patterns.md", "research_lines.md", "research_genealogy.md",
        "relation_table.csv", "research_line_membership.csv",
        "conference_journal_check.md", "gap_taxonomy.md",
        "innovation_operators.md", "method_logic.md", "evidence_design.md",
        "writing.md", "boundaries.md"]
for r in REFS:
    check(os.path.isfile(os.path.join(ROOT, "references", r)), f"reference 存在: {r}")

# 3. examples/ 8 个能力示例
EXS = ["idea_review.md", "innovation_generation.md", "gap_check.md",
       "contribution_check.md", "genealogy_matching.md",
       "experiment_design.md", "generalization_claim_check.md", "paper_story.md"]
for e in EXS:
    check(os.path.isfile(os.path.join(ROOT, "examples", e)), f"example 存在: {e}")

# 4. frontmatter
skill = read("SKILL.md")
m = re.match(r"^---\n(.*?)\n---\n", skill, re.S)
check(m is not None, "SKILL.md 有 frontmatter")
if m:
    fm = m.group(1)
    check('name: lab-research-dna' in fm or 'name: "lab-research-dna"' in fm,
          'frontmatter name 为 lab-research-dna')
    check("description:" in fm and len(fm.split("description:")[1].strip()) > 10,
          "frontmatter description 非空且有触发信息")


# 4b. GitHub/Codex 发布自包含性
check(os.path.basename(ROOT) == "lab-research-dna", "Skill 目录名为 lab-research-dna")
check("workspace/stage4_input" not in skill and "~/workspace/" not in skill,
      "SKILL.md 不依赖 Muse 临时 workspace 绝对路径")
readme = read("README.md")
check(".agents/skills/lab-research-dna" in readme,
      "README 包含 Codex .agents/skills 安装路径")
check("$lab-research-dna" in readme,
      "README 包含显式调用 $lab-research-dna")

# 5. 8 个能力在 SKILL.md 中齐全
for cap in ["Idea Review", "Innovation Generation", "Gap Check",
            "Contribution Check", "Genealogy Matching", "Experiment Design",
            "Generalization Claim Check", "Paper Story"]:
    check(cap in skill, f"SKILL.md 包含能力: {cap}")

# 6. SKILL.md 引用的 references 文件都存在
for ref in re.findall(r"references/([\w\-]+\.md)", skill):
    check(os.path.isfile(os.path.join(ROOT, "references", ref)),
          f"SKILL.md 引用的 reference 可解析: {ref}")

# 7. DNA 13 条齐全，每条有 specificity/confidence/boundary/counterexamples
dna = read("references/dna_patterns.md")
for i in range(1, 14):
    pid = f"DNA-{i:02d}"
    check(pid in dna, f"dna_patterns.md 包含 {pid}")
for field in ["Specificity", "Confidence", "Boundary", "Counterexamples"]:
    check(dna.count(field) >= 13, f"dna_patterns.md 每条含 {field}（≥13 处）")

# 8. specificity 标签齐全且无"独有"误述
for tag in ["LAB_RECURRING_NOT_PROVEN_UNIQUE", "FIELD_COMMON",
            "RESEARCH_LINE_SPECIFIC", "LAB_RECURRING_HYPOTHESIS"]:
    check(tag in dna, f"dna_patterns.md 含 specificity 标签 {tag}")
check("独有" not in dna or "不可声称为本组独有" in dna or "不宣称" in dna,
      "dna_patterns.md 未把 lab-recurring 包装成独有")

# 9. Innovation Generation 管线五段齐全
for kw in ["Predecessor", "Unresolved gap", "Assumption relaxation",
           "New mechanism", "Required evidence"]:
    check(kw in skill, f"SKILL.md 创新管线含: {kw}")

# 10. 全局硬规则存在
for kw in ["MEDIUM", "P039", "P044", "target-visible", "lab-recurring"]:
    check(kw in skill, f"SKILL.md 全局规则提及: {kw}")

print()
if failures:
    print(f"{len(failures)} 项失败")
    sys.exit(1)
print("结构测试全部通过")
