from __future__ import annotations

import json
from pathlib import Path


def hamming(left, right):
    return sum(a != b for a, b in zip(left, right))


def nearest(received, codebook):
    distances = {label: hamming(received, codeword) for label, codeword in codebook.items()}
    minimum = min(distances.values())
    candidates = tuple(label for label, distance in distances.items() if distance == minimum)
    return minimum, candidates


def main() -> None:
    codebook = {"alpha": "0000", "beta": "1111"}
    minimum_distance = hamming(codebook["alpha"], codebook["beta"])
    assert minimum_distance == 4
    authorized_correction_radius = (minimum_distance - 1) // 2
    assert authorized_correction_radius == 1

    one_flip = "0001"
    two_flip = "0011"
    three_flip = "0111"
    assert nearest(one_flip, codebook) == (1, ("alpha",))
    assert nearest(two_flip, codebook) == (2, ("alpha", "beta"))
    assert nearest(three_flip, codebook) == (1, ("beta",))

    # If three_flip originated as alpha, unrestricted nearest-neighbor decoding
    # returns a confident but false beta assignment.
    true_origin_three_flip = "alpha"
    decoded_three_flip = nearest(three_flip, codebook)[1][0]
    assert decoded_three_flip != true_origin_three_flip

    # An exact detector copy preserves the complete codeword. Coding cannot
    # distinguish source multiplicity from downstream duplication.
    copied_records = (codebook["alpha"], codebook["alpha"])
    assert all(nearest(record, codebook) == (0, ("alpha",)) for record in copied_records)
    assert len(copied_records) == 2

    result = {
        "schema": "marici.aspect.optical-pilot-code-distance.v1",
        "status": "pass",
        "codebook": codebook,
        "minimum_distance": minimum_distance,
        "authorized_correction_radius": authorized_correction_radius,
        "one_flip_decode": {"received": one_flip, "distance": 1, "state": "corrected_alpha"},
        "two_flip_decode": {"received": two_flip, "distance": 2, "state": "ambiguous"},
        "three_flip_decode": {
            "received": three_flip,
            "nearest": decoded_three_flip,
            "true_origin": true_origin_three_flip,
            "state": "false_correction_if_radius_ignored",
        },
        "exact_copy_records": list(copied_records),
        "exact_copy_multiplicity_resolved": False,
        "verdict": "A distance-four optical pilot code corrects one symbol error, must retain a two-error tie as ambiguous, and can falsely relabel a three-error alpha record as beta if nearest-neighbor decoding is used outside its authorized radius. Exact downstream copies preserve the entire code and remain multiplicity-ambiguous. Coding repairs transport corruption, not detector-copy provenance.",
        "claim_boundary": "two fixed binary four-symbol pilots with substitution errors and exact decoding; no erasure channel, soft likelihoods, synchronization loss, code-dependent source back-action, or larger codebook",
    }
    output = Path(__file__).parents[1] / "results" / "optical_pilot_code_distance.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
