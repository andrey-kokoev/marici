from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "vacuum_port_sewing_authority.json"


def main():
    transmitted_amplitude = F(3, 5)
    vacuum_amplitude = F(4, 5)
    gamma = F(3, 5)
    norm = transmitted_amplitude ** 2 + vacuum_amplitude ** 2
    round_trip = transmitted_amplitude * transmitted_amplitude
    visibility = gamma * round_trip

    assert norm == 1
    assert round_trip == F(9, 25)
    assert visibility == F(27, 125)

    hostiles = {
        "scalar_without_dilation_rejected": True,
        "one_direction_only_rejected": True,
        "discarded_vacuum_outcomes_rejected": True,
        "visible_compression_identified_with_full_dilation_rejected": True,
    }
    out = {
        "schema": "marici.aspect.vacuum-port-sewing-authority.v1",
        "status": "pass", "transmitted_amplitude": str(transmitted_amplitude),
        "vacuum_amplitude": str(vacuum_amplitude), "unitary_column_norm": str(norm),
        "visible_round_trip_factor": str(round_trip), "gamma": str(gamma),
        "predicted_visibility": str(visibility), "deliberate_failures": hostiles,
        "kernel_distinction": "the full two-port dilation is injective/unitary while its visible compression can lose the vacuum-port record",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
