#!/usr/bin/env python3
"""Soft expansion of the primary T-phi-phi Ward endpoint difference."""

import json
from pathlib import Path

import sympy as sp


eps, kappa = sp.symbols("eps kappa")
kx, ky, kz, nx, ny, nz = sp.symbols("kx ky kz nx ny nz", real=True)
k = sp.symbols("k", positive=True)
F0, Fp = sp.symbols("F0 Fp")

kvec = sp.Matrix([kx, ky, kz])
nvec = sp.Matrix([nx, ny, nz])
kn = sp.expand(kvec.dot(nvec))

# First radial Taylor grade F(|k+eps*n|)=F(k)+eps*F'(k)*(k.n)/k.
F_shift = F0 + eps * Fp * kn / k
k3 = -kvec - eps * nvec
ward_target = sp.expand(-kappa * (kvec * F_shift + k3 * F0))
first_grade = sp.simplify(ward_target.diff(eps).subs(eps, 0))
expected = sp.simplify(-kappa * (kvec * Fp * kn / k - nvec * F0))
assert sp.simplify(first_grade - expected) == sp.zeros(3, 1)
assert ward_target.subs(eps, 0) == sp.zeros(3, 1)

# Symmetric soft stress-tensor lift. Its contraction with n is the first Ward
# grade. For radial F this matrix is symmetric.
soft_tensor = sp.simplify(-kappa * (Fp / k * (kvec * kvec.T) - F0 * sp.eye(3)))
assert sp.simplify(soft_tensor * nvec - first_grade) == sp.zeros(3, 1)
assert soft_tensor == soft_tensor.T

# TT projection relative to the soft direction removes the isotropic F0 term.
# Impose n.n=1 only after expanding the projector identities.
pi = sp.eye(3) - nvec * nvec.T


def unit_reduce(expression):
    return sp.simplify(expression.subs(nx**2 + ny**2 + nz**2, 1))


transverse = sp.expand(pi * soft_tensor * pi)
tt = sp.expand(transverse - pi * sp.trace(transverse) / 2)
isotropic_tensor = kappa * F0 * sp.eye(3)
isotropic_transverse = sp.expand(pi * isotropic_tensor * pi)
isotropic_tt = sp.expand(isotropic_transverse - pi * sp.trace(isotropic_transverse) / 2)

# Verify the isotropic TT piece modulo n.n=1 by polynomial reduction.
nn = nx**2 + ny**2 + nz**2
for value in isotropic_tt:
    _, remainder = sp.div(sp.Poly(sp.expand(value), nx, ny, nz), sp.Poly(nn - 1, nx, ny, nz))
    assert remainder.as_expr() == 0

# At a fixed physical frame n=z and hard momentum in the xz plane, the plus
# response is proportional to F' times the transverse hard quadrupole.
physical = {nx: 0, ny: 0, nz: 1, ky: 0}
tt_physical = sp.simplify(tt.subs(physical))
plus = sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]])
plus_response = sp.factor(sp.trace(plus.T * tt_physical) / 2)
assert plus_response == -Fp * kappa * kx**2 / (2 * k)
assert not plus_response.has(F0)

# For the source conformal scalar two-point function F(k)=k, F'=1.
conformal_response = sp.simplify(plus_response.subs({F0: k, Fp: 1}))
assert conformal_response == -kappa * kx**2 / (2 * k)

packet = {
    "schema": "marici.benincasa.soft-tensor-ward-score-recovery.v1",
    "status": "passed",
    "primary_input": "Baumann et al. equation (4.30), with equal scalar couplings",
    "ward_target": {
        "zeroth_soft_grade": "zero",
        "first_soft_grade": [str(value) for value in first_grade],
        "apparent_1_over_q_lift": "removable because the target starts at order q",
    },
    "soft_tensor": {
        "formula": [[str(value) for value in row] for row in soft_tensor.tolist()],
        "TT_depends_on": "F'(k) only",
        "isotropic_F_term_after_TT": "zero",
    },
    "physical_plus_port": {
        "generic_response": str(plus_response),
        "conformal_scalar_F_equals_k": str(conformal_response),
        "score_source": "first radial momentum score of the scalar two-point function",
        "rank": 1,
        "loss_support": "hard momentum parallel to the soft tensor direction (existing collinear Gram support)",
    },
    "classification": "soft tensor port recovered by an existing scalar score/Ward endpoint map",
    "new_carrier_support": False,
    "scope_warning": (
        "This is the universal leading soft Ward grade. Subleading soft orders "
        "and loop-specific renormalized two-point coefficients require their "
        "own source normalization."
    ),
}

output = Path(__file__).with_name("soft-tensor-ward-score-recovery.json")
output.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2, sort_keys=True))
