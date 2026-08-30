from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "five_empty_bin_reset_candidate.json"


def predecessor_spread_after_empty_bins(k):
    # Ready/dead detector model: dead mass contracts by 16/25 per empty bin;
    # the next photon click response differs by 9/25 times the residual mass.
    return F(9, 25) * F(16, 25) ** k


def main():
    tolerance = F(1, 20)
    spreads = {k: predecessor_spread_after_empty_bins(k) for k in range(7)}
    passing = [k for k, value in spreads.items() if value <= tolerance]
    minimum = min(passing)
    assert spreads[4] > tolerance
    assert spreads[5] <= tolerance
    assert minimum == 5
    out = {
        "schema": "marici.aspect.five-empty-bin-reset-candidate.v1",
        "status": "pass",
        "source_model": "finite ready/dead photodetector with dead-state retention 16/25 per empty bin",
        "qualification_tolerance": str(tolerance),
        "predecessor_spread_by_empty_bins": {str(k): str(v) for k, v in spreads.items()},
        "four_bin_spread": str(spreads[4]),
        "five_bin_spread": str(spreads[5]),
        "minimum_passing_empty_bins": minimum,
        "candidate_reset": "five consecutive empty recovery bins before the target photon probe",
        "scope": "exact for the admitted two-state detector model; the sixteen-cell physical qualification remains required for the apparatus",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
