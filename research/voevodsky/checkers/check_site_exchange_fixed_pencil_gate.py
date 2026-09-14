#!/usr/bin/env python3
"""Show that an abstract A1^3 character does not select a labelled odd line."""
import json
from pathlib import Path
import sympy as sp

R = Path(__file__).resolve().parents[3]
G = -2 * sp.eye(3)
S12 = sp.Matrix([[0,1,0],[1,0,0],[0,0,1]])
S13 = sp.Matrix([[0,0,1],[0,1,0],[1,0,0]])
S23 = sp.Matrix([[1,0,0],[0,0,1],[0,1,0]])
involutions = [S12,S13,S23]
odd = [sp.Matrix([1,-1,0]), sp.Matrix([1,0,-1]), sp.Matrix([0,1,-1])]
checks = {
    "three_distinct_isometric_involutions": len({tuple(S) for S in involutions}) == 3 and all(S.T*G*S == G and S*S == sp.eye(3) for S in involutions),
    "three_distinct_odd_lines": len({tuple(v) for v in odd}) == 3,
    "each_candidate_is_odd": all(involutions[i]*odd[i] == -odd[i] for i in range(3)),
    "each_odd_eigenspace_rank_one": all((S+sp.eye(3)).rank() == 2 for S in involutions),
    "each_candidate_square_minus_four": all((v.T*G*v)[0] == -4 for v in odd),
}
assert all(checks.values()), checks
out = {
    "schema": "marici.voevodsky.site-exchange-fixed-pencil-gate.v1",
    "passed": True,
    "fixed_pencil_integral_action_constructed": False,
    "candidate_odd_generators": [[int(q) for q in v] for v in odd],
    "countermodel": "three distinct coordinate-swap isometries of A1^3 have the same abstract involution type and different odd lines",
    "surviving": "v_alg is odd in the displayed de Rham coordinate exchange",
    "first_missing_map": "integral comparison from the site-exchanged reflection pencil back to the fixed pencil",
    "checks": checks,
}
p = R / "research/voevodsky/results/site_exchange_fixed_pencil_gate.json"
p.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({"passed": True, "candidate_odd_lines": 3, "v_alg_integral_line_selected": False}))
