"""Exact WP586 ambiguity of a D4-only score as a portal tangent."""

import json
from pathlib import Path

import sympy as sp

c, d, alpha = sp.symbols("c d alpha", real=True)
a, b, e = sp.symbols("a b e", real=True)

amplitude = a + c * b + d * e
weight = sp.expand(amplitude**2)
d4_partial = sp.diff(weight, c)
portal_tangent = sp.simplify(sp.diff(weight, c) + alpha * sp.diff(weight, d))

base = {a: 1, b: 1, e: 1, c: 0, d: 0}
hostile = {
    "d4_only": sp.simplify(d4_partial.subs(base)),
    "aligned_completion": sp.simplify(portal_tangent.subs({**base, alpha: 1})),
    "cancelling_completion": sp.simplify(portal_tangent.subs({**base, alpha: -1})),
}

checks = {
    "weight_is_quadratic": sp.Poly(weight, c, d).total_degree() == 2,
    "portal_tangent_contains_unfixed_completion": sp.diff(portal_tangent, alpha)
    == 2 * e * amplitude,
    "d4_only_hostile_response_is_two": hostile["d4_only"] == 2,
    "aligned_completion_response_is_four": hostile["aligned_completion"] == 4,
    "cancelling_completion_response_is_zero": hostile["cancelling_completion"] == 0,
    "same_d4_component_in_all_completions": sp.diff(c + alpha * d, c) == 1,
}

if not all(checks.values()):
    raise SystemExit(f"WP586 check failed: {checks}")

checks = {key: bool(value) for key, value in checks.items()}
result = {
    "work_package": "WP586",
    "status": "PASS",
    "checks": checks,
    "generator_grammar": "M=a+c*b+d*e with c=D4 and d one omitted correlated generator coordinate",
    "d4_partial": sp.sstr(d4_partial),
    "portal_tangent": sp.sstr(portal_tangent),
    "hostile_responses": {key: sp.sstr(value) for key, value in hostile.items()},
    "classification": "D4 score is an executable source partial derivative but neither a portal tangent nor an instrument",
    "smallest_exact_falsifier": "at M=1+c+d, alpha=1 gives response 4 and alpha=-1 gives response 0 although both have dc/dq=1",
    "remaining_gate": "derive the full portal tangent in (D3,D4,CT1,CT2,CT3,widths,branching fractions,heavy-state amplitudes) before detector transport",
}

out = Path(__file__).resolve().parents[1] / "results" / "wp586_d4_score_portal_tangent_ambiguity.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
