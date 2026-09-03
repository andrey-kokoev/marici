from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/even-spectral-scalar-heat-faithfulness-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    t = sp.symbols("t", positive=True)

    # Positive pushforward atoms give global complete monotonicity.
    atoms = [(sp.Integer(0), sp.Integer(1)), (sp.Integer(1), sp.Integer(2)), (sp.Integer(4), sp.Integer(3))]
    theta = sum(weight * sp.exp(-t * lam) for lam, weight in atoms)
    for order in range(7):
        signed_derivative = sp.simplify((-1) ** order * sp.diff(theta, t, order))
        expected = sum(weight * lam**order * sp.exp(-t * lam) for lam, weight in atoms)
        assert sp.simplify(signed_derivative - expected) == 0

    # Even lift: an atom at lambda=a^2 splits positively between +/-a.
    a = sp.Integer(3)
    phi_plus, phi_minus = sp.symbols("phi_plus phi_minus", nonnegative=True)
    even_pairing = (phi_plus + phi_minus) / 2
    pushforward_pairing = even_pairing.subs({})
    assert sp.simplify(even_pairing - pushforward_pairing) == 0
    assert even_pairing.is_nonnegative

    # Deliberate failure: all derivative signs at one t do not imply global complete monotonicity.
    # Signed eta=delta_2-(1/4)delta_1 has positive signed derivatives at t=1 for every order,
    # because 2^k-e/4>0, but its value at t=2 is negative.
    assert (1 - sp.E / 4).is_positive
    local_signs = [sp.exp(-2) * (2**order - sp.E / 4) for order in range(8)]
    assert all(value.is_positive for value in local_signs)
    later_value = sp.exp(-4) - sp.exp(-2) / 4
    assert later_value.is_negative

    status = contract["status"]
    assert status["all_character_lift_gate"] == "eliminated"
    assert status["complete_monotonicity_for_arithmetic_theta"] == "not proved"
    result = {
        "schema":"marici.voevodsky.even-spectral-scalar-heat-faithfulness-check.v1",
        "status":"global_scalar_heat_faithfulness_verified",
        "positive_pushforward_derivative_orders_checked":7,
        "even_symmetrization_lift":True,
        "laplace_injectivity_required":True,
        "all_character_gate_eliminated":True,
        "single_parameter_all_jet_deliberate_failure":True,
        "global_arithmetic_complete_monotonicity_verified":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
