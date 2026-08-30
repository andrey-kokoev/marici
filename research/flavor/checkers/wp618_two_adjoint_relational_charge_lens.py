"""Exact WP618 relational charge lens from the WP438 two-adjoint vacuum."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]

A = sp.diag(1, -1, 0)
D = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
identity = sp.eye(3)
quadratic_sum = A**2 + D**2
quadratic_traceless = sp.simplify(
    quadratic_sum - sp.trace(quadratic_sum) * identity / 3
)
H = sp.simplify(sp.Rational(3, 2) * quadratic_traceless)

r = sp.symbols("r", real=True)
X = sp.simplify(H + r * A)
eigenvalues = [sp.simplify(X[index, index]) for index in range(3)]
signed_gaps = [
    sp.simplify(eigenvalues[0] - eigenvalues[1]),
    sp.simplify(eigenvalues[1] - eigenvalues[2]),
    sp.simplify(eigenvalues[0] - eigenvalues[2]),
]
mass_squares = [sp.expand(gap**2) for gap in signed_gaps]

target_r = sp.Rational(3, 5)
hostile_r = sp.Integer(1)
target_X = sp.simplify(X.subs(r, target_r))
hostile_X = sp.simplify(X.subs(r, hostile_r))
target_gaps = sorted(abs(gap.subs(r, target_r)) for gap in signed_gaps)
hostile_gaps = sorted(abs(gap.subs(r, hostile_r)) for gap in signed_gaps)
target_normalized_gaps = [
    sp.simplify(gap / target_gaps[0]) for gap in target_gaps
]
hostile_normalized_gaps = [
    sp.simplify(gap / hostile_gaps[0]) for gap in hostile_gaps
]
target_mass_squares = sorted(
    sp.simplify(value.subs(r, target_r)) for value in mass_squares
)
target_normalized_mass_squares = [
    sp.simplify(value / target_mass_squares[0])
    for value in target_mass_squares
]

# A reference-sensitive record changes sign under global reversal of X, while
# the ordinary gauge-mass spectrum does not.
reference_pairing = sp.simplify(sp.trace(X * H))
reversed_reference_pairing = sp.simplify(sp.trace((-X) * H))
reversed_mass_squares = [
    sp.expand((-gap) ** 2) for gap in signed_gaps
]

checks = {
    "quadratic_composite_is_primitive_stabilizer":
        H == sp.diag(1, 1, -2),
    "reference_commutes_with_both_vacuum_adjoints":
        H * A - A * H == sp.zeros(3)
        and H * D - D * H == sp.zeros(3),
    "lens_is_traceless_for_every_portal_ratio": sp.trace(X) == 0,
    "target_ratio_produces_centered_target_ray":
        target_X == sp.Rational(2, 5) * sp.diag(4, 1, -5),
    "target_ratio_produces_one_two_three_gaps":
        target_normalized_gaps == [1, 2, 3],
    "hostile_ratio_produces_different_gap_geometry":
        hostile_normalized_gaps == [1, 1, 2],
    "same_vacuum_admits_continuous_portal_fiber":
        sp.diff(X, r) == A and target_X != hostile_X,
    "target_vector_mass_squares_are_one_four_nine":
        target_normalized_mass_squares == [1, 4, 9],
    "mass_spectrum_is_global_sign_blind":
        reversed_mass_squares == mass_squares,
    "reference_pairing_is_sign_sensitive":
        reference_pairing == 6 and reversed_reference_pairing == -6,
}

if not all(checks.values()):
    raise SystemExit(f"WP618 check failed: {checks}")

result = {
    "work_package": "WP618",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "the source-free WP438 embedded-Pauli two-adjoint vacuum, its quadratic stabilizer composite, and charge lenses X(r)=H+rA",
    "source_relations": {
        "A": "diag(1,-1,0)",
        "D": "embedded off-diagonal Pauli generator",
        "H": "(3/2) times the traceless part of A^2+D^2 = diag(1,1,-2)",
    },
    "normalization": "A and H use primitive integral SU(3) cocharacter normalization; overall charge scale remains quotiented",
    "lens_family": "X(r)=H+rA=diag(1+r,1-r,-2)",
    "target_portal_ratio": "3/5",
    "target_lens": ["8/5", "2/5", "-2"],
    "target_gap_ratio": [1, 2, 3],
    "hostile_portal_ratio": "1",
    "hostile_gap_ratio": [1, 1, 2],
    "contextual_partition": "the frozen two-adjoint vacuum and derived reference H leave a continuous one-parameter fiber of inequivalent charge-gap geometries indexed by r",
    "classification": "source-derived relational carrier and orientation reference; portal rigidifier conditional on r; not a numerical charge-gap selector",
    "smallest_exact_falsifier": "the same A,D,H source packet admits r=3/5 with gap ratio 1:2:3 and r=1 with gap ratio 1:1:2",
    "ordinary_physical_probe": "family-root vector mass squares proportional to (2r)^2, (3-r)^2, and (3+r)^2; at r=3/5 their ratio is 1:4:9",
    "ordinary_probe_kernel": "the vector mass spectrum is unchanged under X -> -X",
    "relational_probe": "a coherent interference record calibrated against the source-derived H port is proportional to Tr(XH)=6 and changes sign under X -> -X",
    "groupoid_change": "using H as a reference defines a relational experiment over the stabilizer of the jointly prepared A,D,H packet; it does not reveal an absolute sign of X",
    "instrument_gate": "resolve all three root-vector masses and a coherent H-referenced interference channel, while proving both arise from the same prepared two-adjoint vacuum and calibrating the portal ratio independently",
    "remaining_source_gate": "derive r=3/5 from a symmetry, representation multiplicity, or vacuum equation fixed before flavor data; otherwise the target is encoded in a free portal coefficient",
}

out = ROOT / "results" / "wp618_two_adjoint_relational_charge_lens.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
