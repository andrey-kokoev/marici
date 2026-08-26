"""Exact rank gate for the retained-reference Higgs response."""

import json
from pathlib import Path

import sympy as sp


v0, w_h, w_j = sp.symbols("v0 w_h w_j", positive=True)

# Rows are the curvature and retained-reference tadpole readouts.  The sole
# admitted source coordinate is the quadratic deformation c.
j_one = sp.Matrix([1, v0])
w = sp.diag(w_h, w_j)
gram_one = sp.simplify((j_one.T * w * j_one)[0])

# A two-error claim can only repeat that same causal column until an independent
# source operation has been specified.  Repetition makes the kernel explicit.
j_two = sp.Matrix([[1, 1], [v0, v0]])
gram_two = sp.simplify(j_two.T * w * j_two)
kernel = j_two.nullspace()

checks = {
    "single_knob_response_rank_is_one": j_one.rank() == 1,
    "two_readouts_give_positive_one_parameter_information": gram_one == w_h + v0**2 * w_j,
    "duplicated_two_error_response_rank_is_one": j_two.rank() == 1,
    "two_error_gram_determinant_vanishes": sp.factor(gram_two.det()) == 0,
    "exact_source_story_kernel_is_difference_direction": kernel == [sp.Matrix([-1, 1])],
}

result = {
    "work_package": "WP414",
    "title": "Higgs retained-reference response-rank gate",
    "one_knob_jacobian": [str(x) for x in j_one],
    "one_knob_weighted_gram": str(gram_one),
    "putative_two_error_jacobian": [[str(x) for x in row] for row in j_two.tolist()],
    "putative_two_error_gram_determinant": str(sp.factor(gram_two.det())),
    "source_story_kernel": [[str(x) for x in vector] for vector in kernel],
    "classification": "two readouts calibrate one Higgs source direction; they do not identify two source errors",
    "smallest_falsifier": "an independently derived second source column not proportional to (1,v0)",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).parents[1] / "results" / "wp414_higgs_response_rank_gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
