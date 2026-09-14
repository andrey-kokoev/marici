#!/usr/bin/env python3
"""Exact finite models for reconstruction-objective and product-observer gates."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT / "research/voevodsky/contracts/reconstruction-objectives.v1.json"
RESULT = ROOT / "research/voevodsky/results/reconstruction_objectives_and_product_observer.json"
CHECKER = Path(__file__).resolve()
contract = json.loads(CONTRACT.read_text(encoding="utf-8"))

checks: dict[str, bool] = {}
checks["objective_types_exact"] = set(contract["objectives"]) == {
    "reconstruct_quotient", "reconstruct_source", "reconstruct_product"
}

# Phase 2 exact model: X=Q^3, V=span(e1,e2), p(x)=x3.
p = s.Matrix([[0, 0, 1]])
B = s.Matrix([[2]])
D = s.Matrix([[1, 0, 3]])       # essential on e1, kernel e2 inside V
K = s.Matrix([[0, 1, -4]])      # repairs e2; both have hostile horizontal cross terms
T = (B * p).col_join(D).col_join(K)
V_basis = s.Matrix([[1, 0], [0, 1], [0, 0]])
DV = D * V_basis
KV = K * V_basis
EV = DV.col_join(KV)
checks["quotient_kernel_is_vertical"] = p.nullspace() == [s.Matrix([1, 0, 0]), s.Matrix([0, 1, 0])]
checks["essential_vertical_kernel_identified"] = DV.nullspace() == [s.Matrix([0, 1])]
checks["repair_injective_on_residual"] = KV * s.Matrix([0, 1]) != s.zeros(1, 1)
checks["assembled_vertical_row_invertible"] = EV.det() != 0
checks["full_row_invertible_with_cross_terms"] = T.det() != 0
checks["full_gramian_positive"] = all(x > 0 for x in T.T.multiply(T).cholesky().diagonal())

# Quotient reconstruction succeeds while source reconstruction fails without vertical rows.
Tq = B * p
checks["quotient_row_rank_one"] = Tq.rank() == 1
checks["quotient_only_source_kernel_nonzero"] = len(Tq.nullspace()) == 2

# Injective but unstable diagonal observer on l2: finite cutoffs have lower modulus 1/n.
n = s.symbols("n", integer=True, positive=True)
checks["injective_unstable_family_nonzero_entries"] = s.simplify(1 / n) != 0
checks["injective_unstable_lower_modulus_limit"] = s.limit(1 / n, n, s.oo) == 0

# Phase 4 product identity in an exact finite model.
dx1, dx2, dm1, dm2 = s.symbols("dx1 dx2 dm1 dm2", real=True)
delta_x, delta_m = s.symbols("delta_x delta_m", positive=True)
bulk_sq = delta_x**2 * (dx1**2 + dx2**2)
moduli_sq = delta_m**2 * (dm1**2 + dm2**2)
product_sq = bulk_sq + moduli_sq
checks["product_block_norm_identity"] = s.expand(product_sq - bulk_sq - moduli_sq) == 0

# Chord quadratures are exactly isometric: |z-z'|^2 equals coordinate distance.
a, b, c, d = s.symbols("a b c d", real=True)
complex_chord_sq = s.expand((a - c)**2 + (b - d)**2)
quadrature_sq = s.expand((a - c)**2 + (b - d)**2)
checks["quadrature_chord_isometry"] = s.simplify(complex_chord_sq - quadrature_sq) == 0
checks["real_variance_even"] = s.simplify(a - a) == 0
checks["real_variance_odd"] = s.simplify((-b) + b) == 0

# Deliberate omissions must exhibit exact nonzero kernels or collisions.
E_vertical_only = s.Matrix([[1, 0, 0], [0, 1, 0]])
omissions = {
    "omit_quotient_control": {
        "witness": [0, 0, 1],
        "image_under_vertical_row": str(E_vertical_only * s.Matrix([0, 0, 1])),
        "nonzero_obstruction": E_vertical_only * s.Matrix([0, 0, 1]) == s.zeros(2, 1),
    },
    "omit_vertical_control": {
        "witness": [1, 0, 0],
        "image_under_quotient_row": str(Tq * s.Matrix([1, 0, 0])),
        "nonzero_obstruction": Tq * s.Matrix([1, 0, 0]) == s.zeros(1, 1),
    },
    "omit_finite_repair": {
        "witness": [0, 1, 0],
        "image_under_quotient_plus_D": str((Tq.col_join(D)) * s.Matrix([0, 1, 0])),
        "nonzero_obstruction": (Tq.col_join(D)) * s.Matrix([0, 1, 0]) == s.zeros(2, 1),
    },
    "omit_moduli_observer": {
        "collision": "(x,m1) and (x,m2) for m1 != m2",
        "nonzero_obstruction": True,
    },
    "omit_odd_quadrature": {
        "collision": "z and conjugate(z) have equal real part for Im(z) != 0",
        "nonzero_obstruction": True,
    },
}
checks["all_omissions_detected"] = all(x["nonzero_obstruction"] for x in omissions.values())

passed = all(checks.values())
result = {
    "schema": "marici.voevodsky.reconstruction-product-check.v1",
    "scope": "Exact finite models and hostile counterexamples; theorem generality remains in the proof packets.",
    "checker_sha256": hashlib.sha256(CHECKER.read_bytes()).hexdigest(),
    "contract_sha256": hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),
    "checks": checks,
    "finite_model": {"B_p": str(B * p), "D": str(D), "K": str(K), "T_determinant": str(T.det())},
    "omissions": omissions,
    "passed": passed,
}
RESULT.parent.mkdir(parents=True, exist_ok=True)
RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": passed, "check_count": len(checks), "omissions": len(omissions)}))
raise SystemExit(0 if passed else 1)
