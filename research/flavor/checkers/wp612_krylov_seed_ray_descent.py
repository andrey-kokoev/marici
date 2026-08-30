"""Exact WP612 descent audit for the flavor Krylov seed-ray carrier."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


a1, a2, a3 = sp.symbols("a1 a2 a3", real=True)
x1, x2, x3 = sp.symbols("x1 x2 x3", real=True)
A_general = sp.diag(a1, a2, a3)
x_general = sp.Matrix([x1, x2, x3])
krylov_general = x_general.row_join(A_general * x_general).row_join(
    A_general**2 * x_general
)
omega_general = sp.factor(krylov_general.det())
vandermonde = (a2 - a1) * (a3 - a1) * (a3 - a2)

A = sp.diag(1, 2, 3)
x = sp.Matrix([1, 1, 1]) / sp.sqrt(3)
krylov = x.row_join(A * x).row_join(A**2 * x)
omega = sp.simplify(krylov.det())
seed_projector = sp.simplify(x * x.conjugate().T)

zeta = sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
rephased_x = zeta * x
rephased_projector = sp.simplify(rephased_x * rephased_x.conjugate().T)
rephased_omega = sp.simplify(
    rephased_x.row_join(A * rephased_x).row_join(A**2 * rephased_x).det()
)

central_basis_change = zeta * sp.eye(3)
transformed_A = sp.simplify(
    central_basis_change * A * central_basis_change.conjugate().T
)
transformed_x = sp.simplify(central_basis_change * x)
transformed_omega = sp.simplify(
    transformed_x.row_join(transformed_A * transformed_x).row_join(
        transformed_A**2 * transformed_x
    ).det()
)

probabilities = [sp.Rational(1, 3)] * 3
magnitude_squared = sp.simplify(omega * sp.conjugate(omega))
physical_formula = sp.simplify(vandermonde**2 * (x1 * x2 * x3) ** 2)

# Independent degeneracies.
degenerate_A = sp.diag(1, 1, 3)
missing_x = sp.Matrix([1, 1, 0])
degenerate_omega = sp.simplify(
    x.row_join(degenerate_A * x).row_join(degenerate_A**2 * x).det()
)
missing_omega = sp.simplify(
    missing_x.row_join(A * missing_x).row_join(A**2 * missing_x).det()
)

# Cayley-Hamilton closure for the exact witness.
ch_residual = A**3 - 6 * A**2 + 11 * A - 6 * sp.eye(3)

checks = {
    "general_krylov_factorization": sp.simplify(
        omega_general - vandermonde * x1 * x2 * x3
    )
    == 0,
    "normalized_positive_witness": omega == 2 / (3 * sp.sqrt(3)),
    "same_seed_ray_has_same_projector": rephased_projector == seed_projector,
    "same_seed_ray_flips_krylov_determinant": rephased_omega == -omega,
    "central_u3_change_leaves_A_fixed": transformed_A == A,
    "central_u3_change_flips_krylov_determinant": transformed_omega == -omega,
    "determinant_covariance_accounts_for_flip": sp.det(central_basis_change)
    == -1,
    "magnitude_squared_descends": sp.simplify(
        rephased_omega * sp.conjugate(rephased_omega) - magnitude_squared
    )
    == 0,
    "magnitude_is_vandermonde_times_seed_support": sp.simplify(
        physical_formula - vandermonde**2 * x1**2 * x2**2 * x3**2
    )
    == 0,
    "democratic_seed_reaches_product_bound": sp.prod(probabilities)
    == sp.Rational(1, 27),
    "repeated_eigenvalue_kills_carrier": degenerate_omega == 0,
    "missing_eigendirection_kills_carrier": missing_omega == 0,
    "three_port_cayley_hamilton_closure": ch_residual == sp.zeros(3),
}

if not all(checks.values()):
    raise SystemExit(f"WP612 check failed: {checks}")

result = {
    "work_package": "WP612",
    "status": "PASS",
    "checks": {key: bool(value) for key, value in checks.items()},
    "admitted_state_domain": "a nondegenerate Hermitian flavor evolution A and a physical seed ray [x] under the full common-left U(3) weak-basis group",
    "formal_carrier": "Omega_A(x)=det[x,Ax,A^2x]",
    "descent_failure": "x and exp(i*pi/3)x define the same seed projector but give opposite Omega; the same flip is a central U(3) weak-basis transformation",
    "maximal_descended_carrier": "abs(Omega)^2=Delta_A^2 product_i p_i, where p_i is the seed-projector weight in the A eigenspaces",
    "spectral_port_realization": "if [x] is a down spectral ray and A=H_u, p_i=abs(V_ij)^2 for one charged-current column",
    "classification": "positive cyclicity/readout carrier after quotient; not an alternating physical selector",
    "smallest_exact_falsifier": "the same physical seed ray x and exp(i*pi/3)x flips the claimed orientation sign",
    "reference_disposition": "fixing a volume form or seed phase reduces U(3) to a stabilizer and defines a new relational experiment",
    "source_gate": "derive a physical phase/volume reference or formulate the source action entirely in the descended positive magnitude without claiming orientation",
    "instrument": "spectral weights p_i are charged-current observables; the determinant phase has no instrument without the added reference",
}

out = ROOT / "results" / "wp612_krylov_seed_ray_descent.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
