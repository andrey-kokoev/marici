from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "vacuum_port_coherent_leakage_gate.json"


def main():
    tau = F(9, 25)
    complement = F(16, 25)
    gamma = F(3, 5)
    target = gamma * tau
    occupation = F(1, 100)
    amplitude = F(1, 10)

    coherent_cross_bound = 2 * F(3, 5) * F(4, 5) * amplitude
    population_bound = complement * occupation
    unrandomized_bound = coherent_cross_bound + population_bound
    randomized_bound = population_bound

    assert target == F(27, 125)
    assert coherent_cross_bound == F(12, 125)
    assert population_bound == F(4, 625)
    assert unrandomized_bound == F(64, 625)
    assert randomized_bound == F(4, 625)
    assert target - unrandomized_bound == F(71, 625)
    assert target - randomized_bound == F(131, 625)

    out = {
        "schema": "marici.aspect.vacuum-port-coherent-leakage-gate.v1",
        "status": "pass", "tau": str(tau), "target_visibility": str(target),
        "ancilla_occupation_bound": str(occupation),
        "coherent_amplitude_bound": str(amplitude),
        "unrandomized": {
            "cross_term_bound": str(coherent_cross_bound),
            "population_term_bound": str(population_bound),
            "total_contamination_bound": str(unrandomized_bound),
            "certified_visibility_floor": str(target - unrandomized_bound),
        },
        "phase_randomized": {
            "cross_term_bound": "0",
            "population_term_bound": str(population_bound),
            "total_contamination_bound": str(randomized_bound),
            "certified_visibility_floor": str(target - randomized_bound),
        },
        "conclusion": "a number-only vacuum audit is insufficient; first-moment nulling or phase randomization is required",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
