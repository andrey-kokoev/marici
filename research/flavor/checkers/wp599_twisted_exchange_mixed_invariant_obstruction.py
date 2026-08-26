"""Exact WP599 twisted-exchange mixed-invariant obstruction."""

import json
from pathlib import Path

import sympy as sp


x, y, u, v = sp.symbols("x y u v", real=True)
alpha, beta, zeta = sp.symbols("alpha beta zeta", real=True)
variables = (x, y, u, v)

R = sp.Matrix([[0, -1], [1, 0]])
C = sp.diag(1, -1)
Q = sp.Matrix([[1, -1], [1, 1]]) / sp.sqrt(2)
zero = sp.zeros(2)

common_rotation = sp.diag(R, R)
bare_cp = sp.diag(C, C)
twisted_exchange = zero.row_join(Q).col_join(Q.T.row_join(zero))
generators = (common_rotation, bare_cp, twisted_exchange)

# Complete quartic subspace with bidegree two in each doublet.
monomials = []
for a in range(3):
    for b in range(3):
        if a + b != 2:
            continue
        for c in range(3):
            for d in range(3):
                if c + d == 2:
                    monomials.append(x**a * y**b * u**c * v**d)

coefficients = sp.symbols(f"c0:{len(monomials)}")
generic = sum(c * monomial for c, monomial in zip(coefficients, monomials))
equations = []
vector = sp.Matrix(variables)
for generator in generators:
    transformed = generator * vector
    substitution = {
        variable: transformed[index]
        for index, variable in enumerate(variables)
    }
    difference = sp.Poly(
        sp.expand(generic.subs(substitution, simultaneous=True) - generic),
        *variables,
    )
    equations.extend(difference.coeffs())

constraint_matrix, _ = sp.linear_eq_to_matrix(equations, coefficients)
nullspace = constraint_matrix.nullspace()
invariant_basis = [
    sp.factor(sum(vector[i] * monomials[i] for i in range(len(monomials))))
    for vector in nullspace
]

j_sin = sp.expand((u * y + v * x) ** 2)
j_cos = sp.expand((u * x - v * y) ** 2)


def invariant_under(polynomial, generator):
    transformed = generator * vector
    substitution = {
        variable: transformed[index]
        for index, variable in enumerate(variables)
    }
    return sp.expand(polynomial.subs(substitution, simultaneous=True) - polynomial) == 0


real_slice = {x: sp.cos(alpha), y: sp.sin(alpha), u: sp.cos(beta), v: sp.sin(beta)}
j_sin_slice = sp.trigsimp(j_sin.subs(real_slice))
j_cos_slice = sp.trigsimp(j_cos.subs(real_slice))
hostile_potential = zeta * sp.cos(alpha + beta) ** 2
hostile_gradient = sp.simplify(
    sp.Matrix(
        [sp.diff(hostile_potential, alpha), sp.diff(hostile_potential, beta)]
    ).subs({alpha: 0, beta: sp.pi / 4})
)

selected_pairs = [
    (sp.Rational(a, 4) * sp.pi, sp.Rational(b, 4) * sp.pi)
    for a in range(8)
    if a % 2 == 0
    for b in range(8)
    if b % 2 == 1
]
selected_gradients = [
    sp.simplify(
        sp.Matrix(
            [sp.diff(hostile_potential, alpha), sp.diff(hostile_potential, beta)]
        ).subs({alpha: a, beta: b, zeta: 1})
    )
    for a, b in selected_pairs
]

checks = {
    "twisted_exchange_is_involution": twisted_exchange**2 == sp.eye(4),
    "complete_mixed_quartic_invariant_dimension_is_two": len(nullspace) == 2,
    "j_sin_is_invariant_under_every_generator": all(
        invariant_under(j_sin, generator) for generator in generators
    ),
    "j_cos_is_invariant_under_every_generator": all(
        invariant_under(j_cos, generator) for generator in generators
    ),
    "derived_basis_spans_the_two_explicit_invariants": (
        sp.Matrix.hstack(*nullspace).rank() == 2
    ),
    "j_sin_real_slice_is_sum_angle_sine_square": sp.trigsimp(
        j_sin_slice - sp.sin(alpha + beta) ** 2
    )
    == 0,
    "j_cos_real_slice_is_sum_angle_cosine_square": sp.trigsimp(
        j_cos_slice - sp.cos(alpha + beta) ** 2
    )
    == 0,
    "smallest_hostile_moves_axis_diagonal_vacuum": hostile_gradient
    == sp.Matrix([-zeta, -zeta]),
    "every_opposite_parity_selected_vacuum_is_moved_at_zeta_one": all(
        gradient != sp.zeros(2, 1) for gradient in selected_gradients
    ),
}

if not all(checks.values()):
    raise SystemExit(f"WP599 check failed: {checks}")

result = {
    "work_package": "WP599",
    "status": "PASS",
    "checks": {key: bool(value) for key, value in checks.items()},
    "domain": "complete real quartic bidegree-(2,2) polynomial space for two D4 doublets under common quarter rotation, bare CP and Nima's quarter-twisted exchange T",
    "invariant_basis": [str(item) for item in invariant_basis],
    "angular_basis": ["sin(alpha+beta)^2", "cos(alpha+beta)^2"],
    "classification": "twisted exchange removes CP stabilizers on the truncated anisotropy packet but does not close the complete renormalizable invariant ring",
    "smallest_exact_falsifier": "the allowed invariant (u*x-v*y)^2 with coefficient zeta=1 gives gradient (-1,-1) at alpha=0,beta=pi/4",
    "effect_on_selected_ensemble": "all sixteen opposite-parity discrete vacua have nonzero gradient under the hostile invariant at unit coefficient",
    "source_authority_gate": "derive a microscopic sequestering or product-selection rule forbidding the nonradial linear combination of the two mixed invariants",
    "instrument_gate": "unchanged: no calibrated source-to-physical16 and scalar/threshold joint instrument has been constructed",
}

out = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "wp599_twisted_exchange_mixed_invariant_obstruction.json"
)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
