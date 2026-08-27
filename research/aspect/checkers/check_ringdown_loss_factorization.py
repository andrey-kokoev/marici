from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    mirror_return, internal_survival = sp.symbols("m eta", positive=True)
    round_trip = mirror_return * internal_survival
    input_amplitude = sp.Rational(1)
    steady_record = input_amplitude / (1 - round_trip * input_amplitude)
    ringdown_ratio = round_trip

    steady_ringdown_jacobian = sp.Matrix(
        [
            [sp.diff(steady_record, mirror_return), sp.diff(steady_record, internal_survival)],
            [sp.diff(ringdown_ratio, mirror_return), sp.diff(ringdown_ratio, internal_survival)],
        ]
    )
    assert sp.simplify(steady_ringdown_jacobian.det()) == 0
    assert steady_ringdown_jacobian.rank() == 1

    m_true = sp.Rational(9, 10)
    eta_true = sp.Rational(4, 5)
    rho_true = m_true * eta_true
    assert rho_true == sp.Rational(18, 25)
    ringdown_trace = tuple(rho_true**n for n in range(5))
    assert ringdown_trace == (
        1,
        sp.Rational(18, 25),
        sp.Rational(324, 625),
        sp.Rational(5832, 15625),
        sp.Rational(104976, 390625),
    )

    # A lossless calibrated mirror leakage port adds a function of m alone.
    leakage = 1 - mirror_return**2
    augmented_jacobian = sp.Matrix(
        [
            [sp.diff(round_trip, mirror_return), sp.diff(round_trip, internal_survival)],
            [sp.diff(leakage, mirror_return), sp.diff(leakage, internal_survival)],
        ]
    )
    assert sp.simplify(augmented_jacobian.det()) == 2 * mirror_return**2
    assert augmented_jacobian.rank() == 2
    leakage_true = sp.simplify(1 - m_true**2)
    assert leakage_true == sp.Rational(19, 100)
    recovered_mirror = sp.sqrt(1 - leakage_true)
    recovered_survival = sp.simplify(rho_true / recovered_mirror)
    assert recovered_mirror == m_true
    assert recovered_survival == eta_true

    # A nonexponential trace is a model-fault syndrome even though an exact
    # exponential trace adds no static factorization rank.
    faulty_trace = (1, rho_true, rho_true**2 + sp.Rational(1, 100), rho_true**3)
    faulty_ratios = tuple(sp.simplify(faulty_trace[k + 1] / faulty_trace[k]) for k in range(3))
    assert len(set(faulty_ratios)) == 3

    result = {
        "schema": "marici.aspect.ringdown-loss-factorization.v1",
        "status": "pass",
        "true_parameters": {"mirror_return": str(m_true), "internal_survival": str(eta_true)},
        "round_trip_product": str(rho_true),
        "ringdown_trace": [str(value) for value in ringdown_trace],
        "steady_plus_ringdown_rank": 1,
        "calibrated_leakage_record": str(leakage_true),
        "product_plus_leakage_rank": 2,
        "recovered_parameters": [str(recovered_mirror), str(recovered_survival)],
        "faulty_ringdown_ratios": [str(value) for value in faulty_ratios],
        "verdict": "Ideal single-mode ringdown repeats the steady-state round-trip product and does not separate mirror return from internal survival. It adds temporal model-fault detection. A calibrated lossless mirror-leakage port raises parameter rank to two and recovers both factors on the positive chamber.",
        "claim_boundary": "single-mode scalar cavity, known time step, positive amplitudes, lossless mirror relation for the leakage port; no mode mixing, detector convolution, or unknown input coupling",
    }
    output = Path(__file__).parents[1] / "results" / "ringdown_loss_factorization.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
