from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    L = sp.Integer(1)
    operator_mass = sp.Integer(2)
    localization_bound = sp.Integer(3)
    threshold = 2 * L * (sp.exp(operator_mass + localization_bound) - 1) / sp.pi
    cutoff = int(sp.ceiling(sp.N(threshold, 50)))
    delta = sp.log(1 + (cutoff + 1) * sp.pi / (2 * L)) - operator_mass - localization_bound
    assert sp.N(delta, 50) > 0

    tail_operator_norm_bound = operator_mass
    mixing_norm_bound = operator_mass
    schur_penalty = sp.simplify(operator_mass**2 / delta)

    # Deliberate failure: one integer below the sufficient strict cutoff need not pass.
    failing_cutoff = int(sp.floor(sp.N(threshold, 50))) - 1
    failing_delta = sp.log(1 + (failing_cutoff + 1) * sp.pi / (2 * L)) - operator_mass - localization_bound
    assert sp.N(failing_delta, 50) < 0

    result = {
        "schema": "marici.voevodsky.dirichlet-tail-operator-mass.v1",
        "status": "finite_tail_cutoff_from_operator_mass_verified",
        "fixture_L": str(L),
        "fixture_operator_mass": str(operator_mass),
        "fixture_localization_bound": str(localization_bound),
        "strict_cutoff_threshold_for_N_plus_1": str(threshold),
        "certified_fixture_N": cutoff,
        "certified_tail_gap": str(delta),
        "certified_tail_gap_decimal": str(sp.N(delta, 16)),
        "tail_operator_norm_bound": str(tail_operator_norm_bound),
        "mixing_norm_bound": str(mixing_norm_bound),
        "schur_penalty_bound": str(schur_penalty),
        "deliberate_failure_N": failing_cutoff,
        "deliberate_failure_gap_decimal": str(sp.N(failing_delta, 16)),
        "scalar_symbol_used": False,
        "next_gate": "certify finite low-block ground eigenvalue above Schur penalty",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
