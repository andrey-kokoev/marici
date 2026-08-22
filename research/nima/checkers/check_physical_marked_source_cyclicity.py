#!/usr/bin/env python3
"""Multiprime cyclicity audit for the calibrated rank-21 marked packet."""
import hashlib
import json
import sys
from pathlib import Path


def main():
    root = Path(__file__).resolve().parents[3]
    sys.path.insert(0, str(root / "research/benincasa"))
    import physical_four_mark_residue_twisted_derham as model

    replications = []
    for prime in (32003, 32009, 65521):
        model.PRIME = prime
        census = model.unsplit_union_census(5, 10, 5)
        assert census["relative_union_dimension"] == 21
        assert census["unsplit_source_nonzero"]
        assert census["unsplit_source_first_jet_rank"] == 3
        assert census["unsplit_source_horizontal_saturation_rank"] == 21
        replications.append({"prime": prime, **census})

    result = {
        "schema": "marici.nima.physical_marked_source_cyclicity.v1",
        "passed": True,
        "kinematics": [2, 3, 4],
        "gamma": 5,
        "ambient_degree": 10,
        "cutoff_degree": 5,
        "physical_numerator": "q_g23+q_g31",
        "replications": replications,
        "stable_rank": 21,
        "first_jet_rank": 3,
        "horizontal_source_orbit_rank": 21,
        "interpretation": "the literal unsplit physical numerator is cyclic in the calibrated rank-21 marked-relative packet",
        "scope": "three-prime finite-field replication at one generic fiber and the predeclared calibrated cutoff; not a characteristic-zero global connection theorem",
    }
    output = root / "research/nima/results/physical_marked_source_cyclicity.json"
    payload = output.read_text(encoding="utf-8")
    assert json.loads(payload) == result
    print(json.dumps({"passed": True, "source_orbit_rank": 21,
                      "sha256": hashlib.sha256(payload.encode()).hexdigest().upper()}))


if __name__ == "__main__":
    main()
