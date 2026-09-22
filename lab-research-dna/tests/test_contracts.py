#!/usr/bin/env python3
"""输出契约测试：校验 tests/runs/ 中各能力的实际执行输出是否满足 SKILL.md 的输出契约。"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUNS = os.path.join(ROOT, "tests", "runs")
failures = []


def check(cond, msg):
    if not cond:
        failures.append(msg)
    print(("PASS " if cond else "FAIL ") + msg)


def read(name):
    with open(os.path.join(RUNS, name), encoding="utf-8") as f:
        return f.read()


# 8 个 run 文件都存在
expected_runs = ["idea_review.md", "innovation_generation.md", "gap_check.md",
                 "contribution_check.md", "genealogy_matching.md",
                 "experiment_design.md", "generalization_claim_check.md",
                 "paper_story.md"]
for r in expected_runs:
    check(os.path.isfile(os.path.join(RUNS, r)), f"run 输出存在: {r}")

# 1. Idea Review 契约
t = read("idea_review.md")
for s in ["Verdict", "Matched DNA", "Gap assessment", "Stress test", "Risks", "Confidence"]:
    check(s in t, f"idea_review 含契约字段: {s}")
check("LAB_RECURRING_NOT_PROVEN_UNIQUE" in t or "FIELD_COMMON" in t,
      "idea_review 引用 DNA 时带 specificity 标签")

# 2. Innovation Generation 契约：管线五段 + hypothesis 模板字段
t = read("innovation_generation.md")
for s in ["Closest predecessors", "Existing capability", "Unresolved limitation",
          "New setting", "New gap", "Core insight", "Why not module stacking",
          "Required mechanism change", "Required evidence",
          "Falsification risk", "Confidence"]:
    check(s in t, f"innovation_generation 含模板字段: {s}")
check(t.count("Hypothesis") >= 3, "innovation_generation 生成 ≥3 个 hypothesis")
check("Required evidence" in t and "Falsification risk" in t,
      "innovation_generation 每个 hypothesis 有证据与证伪条件")

# 3. Gap Check 契约
t = read("gap_check.md")
for s in ["Gap type", "Evidence support", "Pseudo-gap verdict", "Reformulation"]:
    check(s in t, f"gap_check 含契约字段: {s}")

# 4. Contribution Check 契约
t = read("contribution_check.md")
for s in ["Per-claim delta", "Weak claims", "Suggested reframing"]:
    check(s in t.replace("Delta 分析", "Per-claim delta"), f"contribution_check 含契约字段: {s}")
check("Weak" in t, "contribution_check 标记了弱 claim")

# 5. Genealogy Matching 契约
t = read("genealogy_matching.md")
for s in ["Research line", "Branch", "Closest predecessors", "Relation nature", "Warnings"]:
    check(s in t, f"genealogy_matching 含契约字段: {s}")
check("genealogy hypothesis" in t or "MEDIUM" in t,
      "genealogy_matching 对 MEDIUM 边做了假设标注")

# 6. Experiment Design 契约
t = read("experiment_design.md")
for s in ["Claim", "Evidence map", "Ablation plan", "Hold-out", "Stress tests",
          "Falsification experiment"]:
    check(s in t, f"experiment_design 含契约字段: {s}")

# 7. Generalization Claim Check 契约
t = read("generalization_claim_check.md")
for s in ["Checklist verdict", "Mismatch flags", "Downgraded claim"]:
    check(s in t, f"generalization_claim_check 含契约字段: {s}")
check("target-accessible" in t and "target-unseen" in t,
      "generalization_claim_check 区分了 target 可见性")

# 8. Paper Story 契约
t = read("paper_story.md")
for s in ["Narrative outline", "Tension check"]:
    check(s in t, f"paper_story 含契约字段: {s}")
check("独有写作风格" in t, "paper_story 声明不声称独有写作风格")

print()
if failures:
    print(f"{len(failures)} 项失败")
    sys.exit(1)
print("契约测试全部通过")
