"""Compiler for the 3+2+1 bivariant closure double category."""
import json
from pathlib import Path

root=Path(__file__).resolve().parents[3]
contract=json.loads((root/"research/strominger/contracts/bivariant-closure-double-category.v1.json").read_text())
def classify(x):
    if not x["vertical_admitted"]: return "unauthorized_vertical"
    if not x["horizontal_admitted"]: return "missing_horizontal"
    if not x["both_composites_defined"]: return "domain_mismatch"
    if x.get("comparison")=="identity": return "strict"
    if x.get("ambient")=="Z" and x.get("comparison_typed_over")=="Q": return "rational_only"
    if x.get("comparison_typed_over"): return "typed_cell"
    return "domain_mismatch"
records=[{"id":x["id"],"expected":x["expected"],"actual":classify(x)} for x in contract["fixtures"]]
passed=all(x["expected"]==x["actual"] for x in records)
result={"schema":"marici.checker_results.v1","checker":"bivariant_closure_double_category_checks.py",
 "passed":passed,"architecture":"3 base towers + 2 variance-separated closure towers + 1 mixed-square tower",
 "records":records,
 "hostile_gate":"contravariant invariance never supplies covariant authority; pairwise valid boundaries never fit their own comparison cell",
 "prediction":"pasting mixed squares requires a further modification/3-cell level"}
(root/"research/strominger/results/bivariant_closure_double_category.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if passed else 1)
