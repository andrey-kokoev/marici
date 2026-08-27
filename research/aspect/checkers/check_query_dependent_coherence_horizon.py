from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


def main() -> None:
    per_step_phase_margin = Fraction(3, 4)
    delays = (0, 1, 2, 4, 8)
    phase_margins = {delay: per_step_phase_margin**delay for delay in delays}
    phase_inverse_gains = {delay: 1 / margin for delay, margin in phase_margins.items()}
    population_margins = {delay: Fraction(1) for delay in delays}

    assert phase_margins[0] == 1
    assert phase_margins[8] == Fraction(6561, 65536)
    assert phase_inverse_gains[8] == Fraction(65536, 6561) > 9
    assert all(population_margins[delay] == 1 for delay in delays)
    assert all(phase_margins[delay] > 0 for delay in delays)

    complete_dephasing_phase_margin = Fraction(0)
    complete_dephasing_population_margin = Fraction(1)
    assert complete_dephasing_phase_margin == 0
    assert complete_dephasing_population_margin == 1

    minimum_accepted_margin = Fraction(1, 10)
    last_accepted_delay = max(
        delay for delay in delays if phase_margins[delay] >= minimum_accepted_margin
    )
    assert last_accepted_delay == 8

    result = {
        "schema": "marici.aspect.query-dependent-coherence-horizon.v1",
        "status": "pass",
        "per_step_phase_margin": str(per_step_phase_margin),
        "phase_margins": {str(delay): str(value) for delay, value in phase_margins.items()},
        "phase_inverse_gains": {str(delay): str(value) for delay, value in phase_inverse_gains.items()},
        "population_margins": {str(delay): str(value) for delay, value in population_margins.items()},
        "finite_delay_phase_rank_survives": all(value > 0 for value in phase_margins.values()),
        "minimum_accepted_phase_margin": str(minimum_accepted_margin),
        "last_tested_delay_meeting_margin": last_accepted_delay,
        "complete_dephasing_phase_margin": str(complete_dephasing_phase_margin),
        "complete_dephasing_population_margin": str(complete_dephasing_population_margin),
        "verdict": "A stored port can preserve population questions perfectly while its phase-sensitive margin decays as (3/4)^n. Exact rank survives every finite tested delay, but inverse gain exceeds nine by step eight; coherent availability is therefore probe-family, margin, and deadline dependent.",
        "claim_boundary": "identical Markovian phase contractions and exact probes; no non-Markovian revival, drift, pulse error, loss, or finite-sample uncertainty",
    }
    output = Path(__file__).parents[1] / "results" / "query_dependent_coherence_horizon.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
