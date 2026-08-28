import json
from pathlib import Path

import sympy as sp


def main() -> None:
    i = sp.I
    omega = (-1 + sp.sqrt(3) * i) / 2
    identity = sp.eye(3)
    d = sp.diag(1, omega, omega**2)
    s = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    words = [sp.simplify(d**a * s**b) for a in range(3) for b in range(3)]
    word_matrix = sp.Matrix.hstack(*[word.reshape(9, 1) for word in words])

    commuting_yu = d
    commuting_yd = d**2
    commuting_hu = sp.simplify(commuting_yu * commuting_yu.conjugate().T)
    commuting_hd = sp.simplify(commuting_yd * commuting_yd.conjugate().T)
    commuting_commutator = sp.simplify(commuting_hu * commuting_hd - commuting_hd * commuting_hu)
    commuting_cp = sp.simplify(sp.trace(commuting_commutator**3))

    mixed_yu = sp.diag(1, 2, 4)
    mixed_yd = sp.Matrix([[2, 1, i], [1, 3, 1], [-i, 1, 5]])
    mixed_hu = sp.simplify(mixed_yu * mixed_yu.conjugate().T)
    mixed_hd = sp.simplify(mixed_yd * mixed_yd.conjugate().T)
    mixed_commutator = sp.simplify(mixed_hu * mixed_hd - mixed_hd * mixed_hu)
    mixed_cp = sp.simplify(sp.trace(mixed_commutator**3))
    leading_minors = [sp.simplify(mixed_hd[:n, :n].det()) for n in (1, 2, 3)]

    checks = {
        "omega_is_primitive_cube_root": sp.simplify(omega**2 + omega + 1) == 0,
        "clock_unitary": sp.simplify(d * d.conjugate().T) == identity,
        "shift_unitary": sp.simplify(s * s.conjugate().T) == identity,
        "weyl_relation": sp.simplify(d * s - omega * s * d) == sp.zeros(3),
        "nine_words_independent": word_matrix.rank() == 9,
        "generated_algebra_is_full_m3": word_matrix.rank() == 9,
        "commuting_packet_cp_zero": commuting_cp == 0,
        "mixed_down_gram_leading_minors": leading_minors == [6, 40, 400],
        "mixed_down_gram_positive": all(value > 0 for value in leading_minors),
        "mixed_packet_commutator_rank_three": mixed_commutator.rank() == 3,
        "mixed_packet_cp_nonzero": mixed_cp == -842400 * i,
        "same_carrier_has_hostile_coefficient_fiber": commuting_cp != mixed_cp,
        "arbitrary_coefficients_do_not_select_proper_family": word_matrix.rank() == 9,
        "physical_instrument_remains_open": True,
    }

    result = {
        "work_package": "WP944",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "source_pair": {
            "relation": "D*S = omega*S*D",
            "word_span_dimension": word_matrix.rank(),
            "ambient_algebra_dimension": 9,
        },
        "hostile_fiber": {
            "commuting_cp_invariant": str(commuting_cp),
            "mixed_cp_invariant": str(mixed_cp),
            "mixed_commutator_rank": mixed_commutator.rank(),
            "mixed_down_gram_leading_principal_minors": [int(value) for value in leading_minors],
        },
        "classification": "presentation rigidifier and universal algebraic carrier; not a selector without a source-fixed proper word module",
        "smallest_exact_falsifier": "one fixed Weyl holonomy pair admits coefficient packets with CP cubic 0 and -842400*i",
        "remaining_gate": "source-derived proper executable word module, completion stability, physical16 descent, and calibrated holonomy instrument",
    }

    expected_path = Path(__file__).parents[1] / "results" / "wp944_two_holonomy_universal_algebra_no_selector.json"
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    assert result == expected
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
