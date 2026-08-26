"""WP349: exact no-go for democratic projector-coefficient selection."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    a_u, b_u, a_d, b_d = sp.symbols("a_u b_u a_d b_d", real=True)
    identity = sp.eye(3)
    p = sp.diag(1, 0, 0)
    q = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2), 0],
                   [sp.Rational(1, 2), sp.Rational(1, 2), 0],
                   [0, 0, 0]])
    vector_r = sp.Matrix([1, sp.I, 1])
    r = sp.simplify(vector_r * vector_r.conjugate().T / 3)
    democratic_sum = sp.simplify(p + q + r)
    yukawa_up = a_u * identity + b_u * democratic_sum
    yukawa_down = a_d * identity + b_d * democratic_sum
    hu = sp.simplify(yukawa_up * yukawa_up.conjugate().T)
    hd = sp.simplify(yukawa_down * yukawa_down.conjugate().T)
    commutator = sp.simplify(hu * hd - hd * hu)
    cp_odd = sp.simplify(sp.trace(commutator**3))
    coefficient_vector = sp.Matrix(sp.symbols("c1:4"))
    swap_12 = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    swap_23 = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    invariant_solution = sp.linsolve(
        list((swap_12 - sp.eye(3)) * coefficient_vector) + list((swap_23 - sp.eye(3)) * coefficient_vector),
        list(coefficient_vector),
    )
    checks = {
        "permutation_invariant_coefficients_are_democratic": invariant_solution == {(coefficient_vector[2], coefficient_vector[2], coefficient_vector[2])},
        "democratic_sum_is_hermitian": democratic_sum == democratic_sum.conjugate().T,
        "sector_lifts_commute_with_same_hermitian": sp.simplify(yukawa_up * democratic_sum - democratic_sum * yukawa_up) == sp.zeros(3) and sp.simplify(yukawa_down * democratic_sum - democratic_sum * yukawa_down) == sp.zeros(3),
        "sector_hermitians_commute_identically": commutator == sp.zeros(3),
        "cp_odd_invariant_vanishes_identically": cp_odd == 0,
        "democratic_sum_has_full_rank": democratic_sum.det() != 0,
        "projector_geometry_alone_does_not_restore_mixing": p * q != q * p and commutator == sp.zeros(3),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP349",
        "admitted_state_domain": "the WP326 three-projector geometry with a common S3 permutation symmetry imposed on projector-channel coefficients in both sectors",
        "faithful_quotient_coordinate": "relative sector mixing and CP invariants on physical16",
        "source_operation": "projector-channel permutation symmetry restricts each coefficient vector to the democratic ray, giving Y_f=a_f I+b_f(P+Q+R)",
        "invariant_coefficient_space": str(invariant_solution),
        "democratic_sum": [[str(value) for value in row] for row in democratic_sum.tolist()],
        "commutator": [[str(value) for value in row] for row in commutator.tolist()],
        "cp_odd_invariant": str(cp_odd),
        "contextual_partition": "all democratic coefficient choices share zero relative commutator even though the underlying projectors do not commute pairwise",
        "classification": "a genuine symmetry rigidifier of coefficient directions that eliminates generic mixing; it is not a viable physical16 selector",
        "smallest_exact_falsifier": "both sector Hermitians are polynomials in the same matrix P+Q+R, so their commutator vanishes for every democratic coefficient choice",
        "remaining_physical_instrument_gate": "derive a source principle selecting distinct nonparallel sector coefficient vectors without fitting them, while preserving the three-projector complex geometry and stable matching",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp349_democratic_projector_symmetry_no_go.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
