"""Compare the total-energy normal staircase with an off-support control."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SUPPORT = HERE / "streamed-covariant-source-jet-rank-d2-a16-k4-q4-4-4-2-2-p32003-point-2-3-m5.json"
CONTROL = HERE / "streamed-covariant-source-jet-rank-d2-a16-k4-q4-4-4-2-2-p32003-point-2-3-m4.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def main() -> None:
    support = json.loads(SUPPORT.read_text())
    control = json.loads(CONTROL.read_text())
    fixed = [
        "field", "maximum_jet_depth", "target_ambient", "target_K_depth",
        "target_q_depths", "target_column_count", "target_relation_count",
        "words_per_exact_depth", "derivative_axes", "ordered_word_labels",
        "rank_engine_sha256",
    ]
    for key in fixed:
        assert support[key] == control[key], key
    assert sum(support["point"]) == 0
    assert sum(control["point"]) != 0
    assert support["cumulative_quotient_rank"] == 3
    assert control["cumulative_quotient_rank"] == 3

    result = {
        "schema": "marici.benincasa.total-energy-normal-staircase-control.v1",
        "normal_coordinate": "E_T=X1+X2+X3",
        "word_basis": support["ordered_word_labels"],
        "support": {
            "point": support["point"],
            "E_T": 0,
            "rank": support["cumulative_quotient_rank"],
            "relation_rank": support["rank_engine_result"]["relation_ranks"][0],
            "sha256": digest(SUPPORT),
        },
        "control": {
            "point": control["point"],
            "E_T": sum(control["point"]),
            "rank": control["cumulative_quotient_rank"],
            "relation_rank": control["rank_engine_result"]["relation_ranks"][0],
            "sha256": digest(CONTROL),
        },
        "rank_excess_at_total_energy": 0,
        "classification": (
            "the second ordinary normal source grade survives, but its rank is "
            "generic differential growth rather than a total-energy-supported excess"
        ),
        "nearby_cycle_inference_authorized": False,
        "next_typed_gate": (
            "apply the independently source-derived oriented g3 Kummer functional "
            "and then construct the full localization comparison"
        ),
    }
    output = HERE / "total-energy-normal-staircase-control.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
