#!/usr/bin/env python3
"""Construct the source-normalized tangential relative covector at infinity."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".tmp_sympy"))
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/infinity-gysin-tangential-relative-covector.json"

t, u = sp.symbols("t u", positive=True)
F = t**4-t**2+1
f0 = 1/sp.sqrt(F)
f2 = t**2/sp.sqrt(F)

# Endpoint-marked relative cohomology rank:
# 0 -> H0(E) -> H0({p0,pinf}) -> H1(E,D) -> H1(E) -> 0.
diagonal_h0 = sp.Matrix([[1], [1]])
reduced_endpoint_rank = 2-diagonal_h0.rank()
absolute_h1_rank = 2
relative_h1_rank = reduced_endpoint_rank+absolute_h1_rank

# Source tangential coordinate u=b/a=1/t.
# omega2 = -du/(u^2*sqrt(1-u^2+u^4)), with principal primitive 1/u.
F_infinity = sp.factor(u**4 * F.subs(t, 1/u))
omega2_u_coefficient = sp.factor(
    f2.subs(t, 1/u) * sp.diff(1/u, u)
)
principal_coefficient = sp.limit(u**2*omega2_u_coefficient, u, 0, dir="+")

# Hadamard finite-part subtraction in the source coordinate:
# integral_0^R f2 dt - R.  Convergence follows from f2-1=O(t^-2).
finite_part_decay = sp.limit(t**2*(f2-1), t, sp.oo)
f0_decay = sp.limit(t**2*f0, t, sp.oo)

checks = {
    "endpoint_reduced_rank_is_one": reduced_endpoint_rank == 1,
    "marked_relative_rank_is_three": relative_h1_rank == 3,
    "source_infinity_polynomial_is_regular": sp.expand(
        F_infinity-(1-u**2+u**4)
    ) == 0,
    "omega2_has_source_fixed_double_pole": principal_coefficient == -1,
    "omega2_subtracted_tail_is_integrable": finite_part_decay == sp.Rational(1, 2),
    "omega0_tail_is_integrable": f0_decay == 1,
}
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.infinity-gysin-tangential-relative-covector.v1",
    "marked_points": ["p0:t=0,W=+1", "pinf:u=1/t=0,W_infinity=+1"],
    "relative_exact_sequence_ranks": {
        "H0_E": 1,
        "H0_D": 2,
        "reduced_endpoint_line": reduced_endpoint_rank,
        "H1_E": absolute_h1_rank,
        "H1_E_D": relative_h1_rank,
    },
    "source_tangential_coordinate": "u=b/a=1/t",
    "infinity_quartic": sp.sstr(F_infinity),
    "omega2_in_u": sp.sstr(omega2_u_coefficient),
    "omega2_principal_double_pole_coefficient": sp.sstr(principal_coefficient),
    "finite_part_covector": {
        "omega0": "integral_0^infinity dt/sqrt(F)",
        "omega2": "limit_R_to_infinity (integral_0^R t^2 dt/sqrt(F) - R)",
        "omega2_subtracted_tail_coefficient": sp.sstr(finite_part_decay),
    },
    "normalization_source": (
        "The subtraction R=1/u is fixed by the labelled projective ratio "
        "u=b/a inherited from the compactification chart."
    ),
    "ordinary_H1_functional_without_tangent": False,
    "tangential_marked_relative_covector_defined": True,
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
print("relative rank", relative_h1_rank)
print("omega2 principal coefficient", principal_coefficient)
print("subtracted-tail coefficient", finite_part_decay)
print(OUT)
