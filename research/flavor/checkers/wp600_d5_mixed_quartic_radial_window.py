"""Exact WP600 D5 inequivalent-doublet mixed-quartic window."""

import json
from pathlib import Path

import sympy as sp


x, y, u, v = sp.symbols("x y u v", real=True)
variables = (x, y, u, v)
C = sp.diag(1, -1)


def rotation(angle):
    return sp.Matrix(
        [
            [sp.cos(angle), -sp.sin(angle)],
            [sp.sin(angle), sp.cos(angle)],
        ]
    )


def mixed_quartic_invariants(order, weight_phi, weight_psi):
    generator_angle = 2 * sp.pi / order
    generators = (
        sp.diag(
            rotation(weight_phi * generator_angle),
            rotation(weight_psi * generator_angle),
        ),
        sp.diag(C, C),
    )
    monomials = [
        x**a * y**b * u**c * v**d
        for a in range(3)
        for b in range(3)
        for c in range(3)
        for d in range(3)
        if a + b == 2 and c + d == 2
    ]
    coefficients = sp.symbols(f"c0:{len(monomials)}")
    generic = sum(
        coefficient * monomial
        for coefficient, monomial in zip(coefficients, monomials)
    )
    equations = []
    source_vector = sp.Matrix(variables)
    for generator in generators:
        transformed = generator * source_vector
        substitution = {
            variable: transformed[index]
            for index, variable in enumerate(variables)
        }
        difference = sp.Poly(
            sp.expand_trig(
                sp.expand(generic.subs(substitution, simultaneous=True) - generic)
            ),
            *variables,
        )
        equations.extend(difference.coeffs())
    matrix, _ = sp.linear_eq_to_matrix(equations, coefficients)
    nullspace = matrix.nullspace()
    basis = [
        sp.factor(
            sum(vector[index] * monomials[index] for index in range(len(monomials)))
        )
        for vector in nullspace
    ]
    return nullspace, basis


d5_nullspace, d5_basis = mixed_quartic_invariants(5, 1, 2)
d4_nullspace, _ = mixed_quartic_invariants(4, 1, 1)
radial_product = (x**2 + y**2) * (u**2 + v**2)

z_phi = x + sp.I * y
z_psi = u + sp.I * v
anisotropy_phi = sp.expand(sp.re(z_phi**5))
anisotropy_psi = sp.expand(sp.re(z_psi**5))
d5_rotation = sp.diag(rotation(2 * sp.pi / 5), rotation(4 * sp.pi / 5))
d5_cp = sp.diag(C, C)
source_vector = sp.Matrix(variables)


def polynomial_is_invariant(polynomial, generator):
    transformed = generator * source_vector
    substitution = {
        variable: transformed[index]
        for index, variable in enumerate(variables)
    }
    return sp.trigsimp(
        sp.expand_trig(
            sp.expand(polynomial.subs(substitution, simultaneous=True) - polynomial)
        )
    ) == 0


vacuum_phi = sp.Matrix([1, 0])
vacuum_psi = sp.Matrix([sp.cos(sp.pi / 5), sp.sin(sp.pi / 5)])
phi_cp_stabilizers = []
psi_cp_stabilizers = []
common_cp_stabilizers = []
for power in range(5):
    cp_phi = rotation(2 * sp.pi * power / 5) * C
    cp_psi = rotation(4 * sp.pi * power / 5) * C
    phi_fixed = sp.simplify(cp_phi * vacuum_phi - vacuum_phi) == sp.zeros(2, 1)
    psi_fixed = sp.simplify(cp_psi * vacuum_psi - vacuum_psi) == sp.zeros(2, 1)
    if phi_fixed:
        phi_cp_stabilizers.append(power)
    if psi_fixed:
        psi_cp_stabilizers.append(power)
    if phi_fixed and psi_fixed:
        common_cp_stabilizers.append(power)

checks = {
    "d5_weight_one_and_two_mixed_quartic_dimension_is_one": len(d5_nullspace)
    == 1,
    "unique_d5_mixed_quartic_is_radial_product": sp.simplify(
        d5_basis[0] - radial_product
    )
    == 0,
    "identical_d4_doublets_have_extra_mixed_quartics": len(d4_nullspace) == 3,
    "weight_one_quintic_anisotropy_is_d5_invariant": polynomial_is_invariant(
        anisotropy_phi, d5_rotation
    )
    and polynomial_is_invariant(anisotropy_phi, d5_cp),
    "weight_two_quintic_anisotropy_is_d5_invariant": polynomial_is_invariant(
        anisotropy_psi, d5_rotation
    )
    and polynomial_is_invariant(anisotropy_psi, d5_cp),
    "axis_vacuum_has_only_cp_power_zero": phi_cp_stabilizers == [0],
    "off_axis_vacuum_has_only_cp_power_three": psi_cp_stabilizers == [3],
    "candidate_pair_has_no_common_generalized_cp": common_cp_stabilizers == [],
}

if not all(checks.values()):
    raise SystemExit(f"WP600 check failed: {checks}")

result = {
    "work_package": "WP600",
    "status": "PASS",
    "checks": {key: bool(value) for key, value in checks.items()},
    "domain": "two inequivalent faithful real D5 doublets of rotation weights one and two; complete renormalizable mixed bidegree-(2,2) grammar",
    "mixed_quartic_basis": [str(item) for item in d5_basis],
    "representation_criterion": "for irreducible orthogonal V and W with one invariant metric each, angle-moving mixed quartics are absent when Sym^2(V) and Sym^2(W) share no nontrivial irreducible channel",
    "cp_witness": "the pair theta_phi=0 and theta_psi=pi/5 has individual generalized-CP stabilizer powers 0 and 3, with empty common intersection",
    "classification": "quartic-only representation window, not a complete renormalizable architecture: bidegree-(2,2) cross-couplings are radial",
    "smallest_exact_falsifier": "the symmetry-allowed cubic Re(z_phi*z_psi^2) lies outside the bidegree-(2,2) census and moves the candidate",
    "remaining_selector_gate": "derive the degree-five operators and their opposite relative sign from one microscopic source rather than choosing the sign from the desired CP result",
    "completion_gate": "enumerate all mixed invariants through the source cutoff and prove radiative closure after the degree-five mediators are included",
    "stability_gate": "a quintic angular operator is only an EFT term; derive the stabilizing higher-degree completion or keep the bounded cutoff domain explicit",
    "instrument_gate": "derive the portal to a calibrated physical16 CP-odd coordinate and threshold records for the mediators generating the quintic operators",
}

out = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "wp600_d5_mixed_quartic_radial_window.json"
)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
