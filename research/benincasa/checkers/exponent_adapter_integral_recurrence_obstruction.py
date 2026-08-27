"""Test whether identity-labelled integral transport types the quarter recurrence."""

from __future__ import annotations

import json
from pathlib import Path

from exponent_adapter_defect_filtration import analyze, row_basis


ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / "research" / "benincasa" / "results"
ORBITS = {
    "minus_i": {"resonant": (-5, 4), "regular_translate": (-1, 4)},
    "plus_i": {"resonant": (-7, 4), "regular_translate": (-3, 4)},
}


def compare(
    packet: dict,
    resonant: tuple[int, int],
    regular_translate: tuple[int, int],
) -> dict:
    prime = packet["p"]
    left = analyze(packet, resonant)
    right = analyze(packet, regular_translate)
    left_vectors = [dict(vector) for vector in left["kernel"]]
    right_vectors = [dict(vector) for vector in right["kernel"]]
    intersection = len(left_vectors) + len(right_vectors) - len(
        row_basis(left_vectors + right_vectors, prime)
    )
    return {
        "resonant_gamma": f"{resonant[0]}/{resonant[1]}",
        "regular_translate_gamma": f"{regular_translate[0]}/{regular_translate[1]}",
        "resonant_relation_dimension": len(left_vectors),
        "regular_relation_dimension": len(right_vectors),
        "intersection_dimension_in_fixed_low_basis": intersection,
        "resonant_only_dimension": len(left_vectors) - intersection,
        "regular_only_dimension": len(right_vectors) - intersection,
        "identity_label_transport_is_nested": intersection
        == min(len(left_vectors), len(right_vectors)),
        "relative_rank_defect": len(left_vectors) - len(right_vectors),
    }


def main() -> None:
    observed = {}
    for prime in (32003, 32009):
        packet = json.loads(
            (RESULTS / f"exponent_adapter_full_pencil_{prime}.json").read_text()
        )
        observed[str(prime)] = {
            name: compare(packet, **points) for name, points in ORBITS.items()
        }

    expected = {
        "minus_i": (15, 10, 5, 10, 5, 5),
        "plus_i": (17, 10, 5, 12, 5, 7),
    }
    for prime_results in observed.values():
        for name, result in prime_results.items():
            assert (
                result["resonant_relation_dimension"],
                result["regular_relation_dimension"],
                result["intersection_dimension_in_fixed_low_basis"],
                result["resonant_only_dimension"],
                result["regular_only_dimension"],
                result["relative_rank_defect"],
            ) == expected[name]
            assert not result["identity_label_transport_is_nested"]

    output = {
        "schema": "marici.benincasa.exponent_adapter_integral_recurrence_obstruction.v1",
        "status": "pass",
        "fixed_low_basis": "labelled monomials a^i b^j with i+j<=7",
        "two_prime_results": observed,
        "conclusion": (
            "Within each fixed order-four Kummer character, the resonant and "
            "regular-translate relation spaces are not nested in the fixed low "
            "basis. Identity-labelled K-shift transport is therefore not a chain "
            "map. A relative recurrence requires a source-derived map through the "
            "high exact sector and its boundary costalk; the frozen pencil packet "
            "contains fibers but no such cross-fiber map."
        ),
    }
    destination = RESULTS / "exponent_adapter_integral_recurrence_obstruction.json"
    destination.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
