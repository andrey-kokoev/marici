"""Exact U(3) central-kernel audit for two adjoint flavor Higgs fields."""

import json
from pathlib import Path

import sympy as sp


I = sp.I
identity = sp.eye(3)
basis = [
    identity,
    sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
    sp.Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]]),
    sp.diag(1, -1, 0),
    sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
    sp.Matrix([[0, 0, -I], [0, 0, 0], [I, 0, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, -I], [0, I, 0]]),
    sp.diag(1, 1, -2),
]

A = sp.diag(0, 1, 3)
D = sp.Matrix([[2, 1, 1], [1, -1, 1], [1, 1, 0]])


def commutator(left, right):
    return left * right - right * left


def pairing(left, right):
    total = sp.zeros(3)
    for background in (A, D):
        total += commutator(left, background).conjugate().T * commutator(right, background)
    return sp.simplify(sp.trace(total))


mass_gram = sp.Matrix([[pairing(left, right) for right in basis] for left in basis])
su3_gram = mass_gram[1:, 1:]
u3_rank = mass_gram.rank()
su3_rank = su3_gram.rank()
su3_determinant = sp.factor(su3_gram.det())

scale, g_f = sp.symbols("f g_F", positive=True, real=True)
scaled_gram = g_f**2 * scale**2 * mass_gram

checks = {
    "identity_commutes_with_both_adjoints": commutator(identity, A) == sp.zeros(3) and commutator(identity, D) == sp.zeros(3),
    "central_mass_row_and_column_vanish": mass_gram[0, :] == sp.zeros(1, 9) and mass_gram[:, 0] == sp.zeros(9, 1),
    "generic_U3_mass_gram_has_rank_eight": u3_rank == 8,
    "generic_SU3_restriction_has_rank_eight": su3_rank == 8,
    "generic_SU3_determinant_is_nonzero": su3_determinant != 0,
    "U3_kernel_dimension_is_exactly_one": 9 - u3_rank == 1,
    "absolute_nonzero_spectrum_scales_with_gf_squared_f_squared": sp.diff(scaled_gram[1, 1], g_f) != 0 and sp.diff(scaled_gram[1, 1], scale) != 0,
    "normalized_shape_does_not_fix_absolute_scale": {g_f, scale}.issubset(scaled_gram.free_symbols),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP433",
    "title": "Two-adjoint gauge-clock obstruction",
    "benchmark_A": str(A),
    "benchmark_D": str(D),
    "U3_mass_gram_rank": u3_rank,
    "SU3_mass_gram_rank": su3_rank,
    "U3_kernel_dimension": 9 - u3_rank,
    "SU3_determinant": str(su3_determinant),
    "classification": "two conjugation adjoints generically Higgs SU(3)_Q but cannot Higgs the central U(1) or fix the absolute gauge-mass scale",
    "smallest_exact_falsifier": "a full-rank U(3) commutator mass Gram constructed only from adjoint backgrounds",
    "remaining_gate": "center-charged completion or SU(3)-only theory, anomaly cancellation, portal, and independent authority for g_F f/v",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).parents[1] / "results" / "wp433_two_adjoint_gauge_clock_obstruction.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
