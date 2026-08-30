import json
from pathlib import Path

import sympy as sp


def main() -> None:
    i = sp.I
    w = sp.diag(1, -1, i)
    identity = sp.eye(3)

    yu = identity + 2 * w + w**2
    yd = 2 * identity - w + 3 * w**2
    hu = sp.simplify(yu * yu.conjugate().T)
    hd = sp.simplify(yd * yd.conjugate().T)
    commutator = sp.simplify(hu * hd - hd * hu)
    cp_invariant = sp.simplify(sp.trace(commutator**3))

    mixed_hu = sp.diag(1, 2, 4)
    mixed_hd = sp.Matrix([[2, 1, i], [1, 3, 1], [-i, 1, 5]])
    mixed_commutator = sp.simplify(mixed_hu * mixed_hd - mixed_hd * mixed_hu)
    mixed_cp = sp.simplify(sp.trace(mixed_commutator**3))
    leading_minors = [mixed_hd[:n, :n].det() for n in (1, 2, 3)]

    checks = {
        "holonomy_unitary": sp.simplify(w * w.conjugate().T) == identity,
        "holonomy_normal": sp.simplify(w * w.conjugate().T - w.conjugate().T * w) == sp.zeros(3),
        "yu_is_holonomy_polynomial": yu == identity + 2 * w + w**2,
        "yd_is_holonomy_polynomial": yd == 2 * identity - w + 3 * w**2,
        "single_holonomy_grams_commute": commutator == sp.zeros(3),
        "single_holonomy_cp_zero": cp_invariant == 0,
        "mixed_hd_leading_minors": leading_minors == [2, 5, 20],
        "mixed_hd_positive_definite": all(value > 0 for value in leading_minors),
        "mixed_comparator_noncommuting": mixed_commutator != sp.zeros(3),
        "mixed_comparator_cp_nonzero": mixed_cp == -36 * i,
        "second_noncommuting_source_required": mixed_cp != 0 and cp_invariant == 0,
        "physical_instrument_open": True,
    }

    result = {
        "work_package": "WP943",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "single_holonomy": {
            "spectrum": ["1", "-1", "i"],
            "gram_commutator_rank": commutator.rank(),
            "cp_invariant": str(cp_invariant),
        },
        "mixed_comparator": {
            "hd_leading_principal_minors": [int(value) for value in leading_minors],
            "gram_commutator_rank": mixed_commutator.rank(),
            "cp_invariant": str(mixed_cp),
        },
        "classification": "proper commuting physical16 selector, experimentally wrong",
        "smallest_exact_falsifier": "positive mixed comparator has Tr([Hu,Hd]^3)=-36*i",
        "remaining_gate": "two noncommuting source-related family operators with fixed relative orientation and calibrated holonomy instrument",
    }

    expected_path = Path(__file__).parents[1] / "results" / "wp943_single_holonomy_physical16_commuting_no_go.json"
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    assert result == expected
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
