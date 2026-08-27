from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    mirror_return, internal_survival, mirror_absorption = sp.symbols(
        "m eta alpha", positive=True
    )
    round_trip = mirror_return * internal_survival
    transmitted_power = 1 - mirror_return**2 - mirror_absorption

    two_port_jacobian = sp.Matrix(
        [
            [sp.diff(round_trip, parameter) for parameter in (mirror_return, internal_survival, mirror_absorption)],
            [sp.diff(transmitted_power, parameter) for parameter in (mirror_return, internal_survival, mirror_absorption)],
        ]
    )
    assert two_port_jacobian.rank() == 2
    assert two_port_jacobian.nullspace()[0] != sp.zeros(3, 1)

    three_port_jacobian = two_port_jacobian.col_join(sp.Matrix([[0, 0, 1]]))
    assert sp.simplify(three_port_jacobian.det()) == 2 * mirror_return**2
    assert three_port_jacobian.rank() == 3

    m_true = sp.Rational(4, 5)
    eta_true = sp.Rational(3, 4)
    alpha_true = sp.Rational(11, 100)
    rho_record = m_true * eta_true
    transmission_record = 1 - m_true**2 - alpha_true
    absorption_record = alpha_true
    assert (rho_record, transmission_record, absorption_record) == (
        sp.Rational(3, 5),
        sp.Rational(1, 4),
        sp.Rational(11, 100),
    )

    recovered_mirror = sp.sqrt(1 - transmission_record - absorption_record)
    recovered_survival = sp.simplify(rho_record / recovered_mirror)
    assert recovered_mirror == m_true
    assert recovered_survival == eta_true

    # Without the absorption record, distinct physical decompositions reproduce
    # the same round-trip and transmitted-power records.
    hostile_mirror = sp.Rational(7, 10)
    hostile_survival = sp.simplify(rho_record / hostile_mirror)
    hostile_absorption = sp.simplify(1 - hostile_mirror**2 - transmission_record)
    assert hostile_survival == sp.Rational(6, 7)
    assert hostile_absorption == sp.Rational(13, 50)
    assert hostile_mirror * hostile_survival == rho_record
    assert 1 - hostile_mirror**2 - hostile_absorption == transmission_record
    assert hostile_absorption != absorption_record

    # Measuring total nonreturn determines m, but not the partition into useful
    # transmission and parasitic absorption.
    total_deficit = 1 - m_true**2
    assert total_deficit == transmission_record + absorption_record == sp.Rational(9, 25)

    result = {
        "schema": "marici.aspect.cavity-energy-channel-attribution.v1",
        "status": "pass",
        "records": {
            "round_trip": str(rho_record),
            "transmitted_power": str(transmission_record),
            "absorbed_power": str(absorption_record),
            "total_mirror_deficit": str(total_deficit),
        },
        "round_trip_plus_transmission_rank": 2,
        "full_energy_channel_rank": 3,
        "full_jacobian_determinant": str(2 * mirror_return**2),
        "recovered_parameters": {
            "mirror_return": str(recovered_mirror),
            "internal_survival": str(recovered_survival),
            "mirror_absorption": str(absorption_record),
        },
        "two_port_alias": {
            "mirror_return": str(hostile_mirror),
            "internal_survival": str(hostile_survival),
            "mirror_absorption": str(hostile_absorption),
        },
        "verdict": "Round-trip survival plus one transmitted-power port cannot attribute parasitic mirror absorption. A separately calibrated absorption or reflected-power channel raises the three-parameter energy-balance map to full rank on the positive chamber. Total nonreturn recovers mirror return but still cannot partition useful transmission from absorption.",
        "claim_boundary": "single scalar mode, normalized incident power, complete accounting into reflection, transmission, and mirror absorption, positive amplitude chamber; no scatter outside the collection aperture or detector calibration uncertainty",
    }
    output = Path(__file__).parents[1] / "results" / "cavity_energy_channel_attribution.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
