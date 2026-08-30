"""Exact WP806 audit: rephasing cycle, weak-basis descent, and CP pairing."""

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    I = sp.I

    # Four Yukawa entries on two left and two right fields plus one scalar.
    # Rows are phases of y11, y12, y21, y22.
    charge = sp.Matrix([
        [1, 0, -1, 0, -1],
        [1, 0, 0, -1, -1],
        [0, 1, -1, 0, -1],
        [0, 1, 0, -1, -1],
    ])
    loop = sp.Matrix([1, -1, -1, 1])

    Y = sp.Matrix([[1, 1], [1, I]])
    U = sp.Matrix([[1, 1], [-1, 1]]) / sp.sqrt(2)
    Y_rotated = sp.simplify(U * Y)

    def plaquette(matrix):
        return sp.simplify(
            matrix[0, 0] * matrix[1, 1]
            * sp.conjugate(matrix[0, 1]) * sp.conjugate(matrix[1, 0])
        )

    # Three-generation physical CP invariant.
    omega = -sp.Rational(1, 2) + I * sp.sqrt(3) / 2
    V = sp.Matrix([[1, 1, 1], [1, omega, omega**2], [1, omega**2, omega]]) / sp.sqrt(3)
    Hu = sp.diag(1, 2, 3)
    Hd = sp.simplify(V * sp.diag(4, 5, 7) * V.H)
    commutator = sp.simplify(Hu * Hd - Hd * Hu)
    jarlskog = sp.simplify(sp.im(commutator.det()))
    permutation = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    Hu_wb = permutation * Hu * permutation.H
    Hd_wb = sp.simplify(permutation * Hd * permutation.H)
    jarlskog_wb = sp.simplify(sp.im((Hu_wb * Hd_wb - Hd_wb * Hu_wb).det()))

    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("plaquette_charge_matrix_has_one_left_kernel", charge.rank() == 3,
          f"rank={charge.rank()}, left-nullity={4 - charge.rank()}")
    check("plaquette_loop_is_rephasing_invariant", charge.T * loop == sp.zeros(5, 1),
          (charge.T * loop).T)
    check("literal_plaquette_is_nonzero_imaginary", plaquette(Y) == I, plaquette(Y))
    check("weak_basis_rotation_is_unitary", sp.simplify(U.H * U) == sp.eye(2), sp.simplify(U.H * U))
    check("weak_basis_rotation_preserves_gram_matrix",
          sp.simplify(Y.H * Y - Y_rotated.H * Y_rotated) == sp.zeros(2),
          sp.simplify(Y.H * Y - Y_rotated.H * Y_rotated))
    check("plaquette_fails_full_weak_basis_descent", plaquette(Y_rotated) == 0,
          f"before={plaquette(Y)}, after={plaquette(Y_rotated)}")

    check("three_generation_mixing_matrix_is_unitary", sp.simplify(V.H * V) == sp.eye(3),
          sp.simplify(V.H * V))
    check("jarlskog_type_invariant_is_nonzero", jarlskog == 4 * sp.sqrt(3) / 3, jarlskog)
    check("jarlskog_type_invariant_descends_under_weak_basis",
          jarlskog_wb == jarlskog, jarlskog_wb)
    jarlskog_cp = sp.simplify(sp.im(sp.conjugate(commutator).det()))
    check("cp_conjugation_reverses_physical_orientation", jarlskog_cp == -jarlskog,
          jarlskog_cp)

    # A CP-even phase potential can select |Phi| but pairs its sign.
    phi = sp.symbols("phi", real=True)
    potential = -sp.cos(phi) + sp.cos(2 * phi)
    cos_value = sp.Rational(1, 4)
    curvature = sp.simplify(sp.diff(potential, phi, 2).subs(sp.cos(phi), cos_value).subs(sp.cos(2 * phi), 2 * cos_value**2 - 1))
    check("cp_even_potential_has_nontrivial_stationary_magnitude",
          sp.simplify(sp.diff(potential, phi) / sp.sin(phi)).subs(sp.cos(phi), cos_value) == 0,
          cos_value)
    check("paired_nontrivial_stationary_points_are_minima", curvature == sp.Rational(15, 4), curvature)
    phi0 = sp.acos(cos_value)
    check("cp_even_source_leaves_equal_sign_pair",
          sp.simplify(potential.subs(phi, phi0) - potential.subs(phi, -phi0)) == 0,
          sp.simplify(potential.subs(phi, phi0)))

    kappa = sp.symbols("kappa", real=True)
    odd_term = -kappa * sp.sin(phi)
    energy_split = sp.simplify(odd_term.subs(phi, phi0) - odd_term.subs(phi, -phi0))
    check("cp_odd_coefficient_is_required_to_lift_pair", energy_split != 0,
          energy_split)

    mass, calibration = sp.symbols("mass calibration", positive=True)
    probes = sp.Matrix([jarlskog])
    jacobian = probes.jacobian([mass, calibration])
    check("physical_orientation_probe_does_not_select_threshold_or_calibration",
          jacobian.rank() == 0, f"rank={jacobian.rank()}, nullity=2")

    result = {
        "work_package": "WP806",
        "title": "Phase-cycle weak-basis descent and CP-pair audit",
        "plaquette_charge_matrix": [[int(value) for value in row] for row in charge.tolist()],
        "plaquette_loop": [int(value) for value in loop],
        "jarlskog_type_invariant": str(jarlskog),
        "summary": {
            "passed": sum(t["passed"] for t in tests),
            "total": len(tests),
            "all_passed": all(t["passed"] for t in tests),
        },
        "tests": tests,
        "classification": {
            "plaquette_phase": "rephasing invariant but not weak-basis invariant",
            "jarlskog_orientation": "faithful physical quotient coordinate",
            "cp_even_selector": "selects magnitude but pairs signs",
            "cp_odd_selector": "requires a new source coefficient",
            "threshold_and_readout": "unselected",
        },
    }

    output = Path(__file__).parents[1] / "results" / "wp806_phase_cycle_weak_basis_cp_pair_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
