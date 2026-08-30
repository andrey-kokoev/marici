import ast
import json
from pathlib import Path


root = Path(__file__).parents[1]
marici = root.parents[1]
candidate_path = marici / "research" / "benincasa" / "checkers" / "check_rank26_dual_gamma_cyclic_atlas_closure.py"
source = candidate_path.read_text(encoding="utf-8")
tree = ast.parse(source)

checks_dict = None
for node in ast.walk(tree):
    if isinstance(node, ast.Assign) and any(isinstance(target, ast.Name) and target.id == "checks" for target in node.targets):
        checks_dict = node.value
        break

assert isinstance(checks_dict, ast.Dict)
expressions = {
    key.value: ast.unparse(value)
    for key, value in zip(checks_dict.keys, checks_dict.values)
    if isinstance(key, ast.Constant) and isinstance(key.value, str)
}

epsilon_expression = expressions.get("epsilon_coordinate_returns_identically", "")
cycle_expression = expressions.get("signed_order_three_quotient_composite_is_identity", "")
line_expression = expressions.get("common_bockstein_line_returns_identically", "")

findings = {
    "epsilon_closure_is_hard_coded": epsilon_expression == "True",
    "cycle_closure_reuses_edge_identity_failures_without_composition": "edge_identity_failures" in cycle_expression and "compose" not in cycle_expression,
    "bockstein_line_closure_is_inferred_without_extracted_line_transport": "edge_identity_failures" in line_expression and "bockstein" not in line_expression.lower(),
    "charts_are_generated_from_one_base_chart": "charts = [tr.presentation(cyclic_fiber(k)" in source,
    "no_explicit_three_edge_matrix_product_is_computed": "matmul" not in source and "compose(" not in source,
}

required_repairs = [
    "derive and transport the epsilon coordinate on each edge, then compare after three steps",
    "materialize all three quotient matrices and multiply them in the declared order",
    "extract the common Bockstein line in every chart and compose its three induced scalar maps",
    "separate source-authorized cyclic generation from a claim of independent chart construction",
]

result = {
    "schema": "marici.aspect.dual-gamma-cyclic-checker-anti-fitting.v1",
    "status": "claim_gaps_detected_preexecution" if all(findings.values()) else "audit_inconclusive",
    "candidate": str(candidate_path.relative_to(marici)).replace("\\", "/"),
    "findings": findings,
    "observed_check_expressions": {
        "epsilon": epsilon_expression,
        "cycle": cycle_expression,
        "bockstein_line": line_expression,
    },
    "required_repairs": required_repairs,
    "disposition": "the current candidate may test edgewise cyclic covariance but cannot yet certify signed order-three closure on epsilon or the Bockstein line",
}

out = root / "results" / "dual_gamma_cyclic_checker_anti_fitting.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "claim_gaps_detected_preexecution" else 1)
