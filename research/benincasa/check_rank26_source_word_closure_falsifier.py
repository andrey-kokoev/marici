"""Consolidate the replicated Gauss--Manin closure falsifier."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
FILES = {
    "strict_a12": "rank26-total-energy-source-word-closure-a12-p32003.json",
    "strict_a14": "rank26-total-energy-source-word-closure-a14-p32003.json",
    "strict_replication": "rank26-total-energy-source-word-closure-a12-p32009-point-3-5-m8.json",
    "logarithmic_a12": "rank26-total-energy-source-word-closure-log-a12-p32003.json",
}


def main():
    packets = {name: json.loads((HERE / path).read_text()) for name, path in FILES.items()}
    strict = [packets[name] for name in ("strict_a12", "strict_a14", "strict_replication")]
    assert all(packet["closure_mode"] == "strict" for packet in strict)
    assert all(packet["source_image_ranks"] == [26, 52] for packet in strict)
    assert all(packet["normal_derivative_extension_ranks"] == [25, 26] for packet in strict)
    assert all(not packet["normal_closure"] for packet in strict)
    logarithmic = packets["logarithmic_a12"]
    assert logarithmic["closure_mode"] == "logarithmic"
    assert logarithmic["normal_derivative_extension_ranks"] == [0, 25]
    assert not logarithmic["normal_closure"]
    assert strict[0]["field"] != strict[2]["field"]
    assert strict[0]["point"] != strict[2]["point"]
    result = {
        "schema": "marici.benincasa.rank26-source-word-closure-falsifier.v1",
        "status": "passed",
        "strict_extension_ranks": [25, 26],
        "logarithmic_extension_ranks": [0, 25],
        "replicated_cutoffs": [12, 14],
        "replicated_primes": [strict[0]["field"], strict[2]["field"]],
        "replicated_points": [strict[0]["point"], strict[2]["point"]],
        "classification": (
            "the stable (26,52,75) source-word census belongs to a non-horizontal "
            "primitive chart and does not define a strict or logarithmic nearby lattice"
        ),
        "inputs": FILES,
    }
    output = HERE / "rank26-source-word-closure-falsifier.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
