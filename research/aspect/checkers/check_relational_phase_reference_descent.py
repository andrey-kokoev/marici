from __future__ import annotations

import json
from pathlib import Path


def gaussian_multiply(left, right):
    a, b = left
    c, d = right
    return (a * c - b * d, a * d + b * c)


def main() -> None:
    signal = (3, 4)
    dual_reference = (2, -1)
    gauge_group = ((1, 0), (0, 1), (-1, 0), (0, -1))

    signal_orbit = tuple(gaussian_multiply(g, signal) for g in gauge_group)
    intensity_orbit = tuple(a * a + b * b for a, b in signal_orbit)
    assert intensity_orbit == (25, 25, 25, 25)
    assert tuple(map(sum, zip(*signal_orbit))) == (0, 0)

    relative_records = tuple(
        gaussian_multiply(
            gaussian_multiply(dual_reference, (g[0], -g[1])),
            gaussian_multiply(g, signal),
        )
        for g in gauge_group
    )
    relative_record = gaussian_multiply(dual_reference, signal)
    assert relative_records == (relative_record,) * 4
    assert relative_record == (10, 5)

    # Holding the admitted reference fixed while changing the target sign is a
    # physical relative change and reverses the relational record.
    reversed_signal = (-signal[0], -signal[1])
    reversed_record = gaussian_multiply(dual_reference, reversed_signal)
    assert reversed_record == (-relative_record[0], -relative_record[1])

    # A reference declared gauge-trivial cannot cancel the signal character.
    trivial_reference = (2, 0)
    trivial_records = tuple(gaussian_multiply(trivial_reference, value) for value in signal_orbit)
    assert len(set(trivial_records)) == 4

    # Squaring a real sign signal descends under Z2 but deletes its sign.
    real_signal = 3
    assert real_signal**2 == (-real_signal) ** 2

    # A bare reference torsor has two equally admissible trivializations.
    reference_torsor = (1, -1)
    torsor_relative_records = tuple(reference * real_signal for reference in reference_torsor)
    assert torsor_relative_records == (3, -3)
    assert sum(torsor_relative_records) == 0

    result = {
        "schema": "marici.aspect.relational-phase-reference-descent.v1",
        "status": "pass",
        "signal": [*signal],
        "intensity_orbit": [str(value) for value in intensity_orbit],
        "orbit_averaged_linear_response": [0, 0],
        "dual_reference": [*dual_reference],
        "gauge_invariant_relative_record": [*relative_record],
        "target_sign_reversal_record": [*reversed_record],
        "trivial_reference_orbit_size": len(set(trivial_records)),
        "squared_sign_records": [real_signal**2, (-real_signal) ** 2],
        "unselected_reference_torsor_records": list(torsor_relative_records),
        "verdict": "A phase-sensitive optical record descends only as a relational pairing between the signal character and a source-derived dual reference. Intensity descends but loses phase; a standalone odd port and a gauge-trivial reference do not descend; an unselected reference torsor yields no canonical signed value.",
        "claim_boundary": "finite Z4 phase gauge and Z2 sign reduction with exact coherent amplitudes; reference preparation, phase drift, detector noise, and global topological obstructions are not modeled",
    }
    output = Path(__file__).parents[1] / "results" / "relational_phase_reference_descent.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
