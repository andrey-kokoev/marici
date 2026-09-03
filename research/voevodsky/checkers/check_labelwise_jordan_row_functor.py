from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/labelwise-jordan-row-functor-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    J1 = sp.diag(1, -1)
    J2 = sp.Matrix([[0, 1], [1, 0]])
    J1p = sp.diag(1, 0)
    J1m = sp.diag(0, 1)
    J2p = sp.Rational(1, 2) * sp.Matrix([[1, 1], [1, 1]])
    J2m = sp.Rational(1, 2) * sp.Matrix([[1, -1], [-1, 1]])
    assert J1 == J1p - J1m and J2 == J2p - J2m

    total = J1 + J2
    total_abs = sp.sqrt(2) * sp.eye(2)  # total**2 = 2I
    total_p = (total + total_abs) / 2
    total_m = (total_abs - total) / 2
    assert total**2 == 2 * sp.eye(2)
    assert total_p != J1p + J2p
    assert total_m != J1m + J2m

    x, y = sp.symbols("x y", real=True)
    f = sp.Matrix([x, y])
    source_form = sp.expand((f.T * total * f)[0])
    labelled_difference = sp.expand((f.T * (J1p + J2p) * f)[0] - (f.T * (J1m + J2m) * f)[0])
    assert sp.simplify(source_form - labelled_difference) == 0

    # Cutoff extension appends label blocks instead of rotating old sign coordinates.
    plus_stage_1 = J1p
    plus_stage_2 = sp.diag(J1p, J2p)
    minus_stage_1 = J1m
    minus_stage_2 = sp.diag(J1m, J2m)
    assert plus_stage_2[:2, :2] == plus_stage_1
    assert minus_stage_2[:2, :2] == minus_stage_1

    status = contract["status"]
    assert status["tail_control"] == "not supplied"
    result = {
        "schema":"marici.voevodsky.labelwise-jordan-row-functor-check.v1",
        "status":"labelwise_functorial_repair_verified",
        "global_sum_positive_part_nonadditive":True,
        "global_sum_negative_part_nonadditive":True,
        "labelwise_quadratic_identity":True,
        "cutoff_append_coherence":True,
        "tail_control_supplied":False,
        "global_observer_contraction_supplied":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
