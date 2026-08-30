"""Consolidate the exact total-energy Rees typing falsifier."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load(name):
    return json.loads((HERE / name).read_text())


def main():
    complete = {
        ambient: load(
            f"rank26-total-energy-rees-source-comparison-a{ambient}-p32003.json"
        )
        for ambient in (8, 10, 12, 14)
    }
    assert [complete[a]["support_excess"] for a in complete] == [8, 12, 16, 20]
    assert [
        complete[a]["elementary_length_census"] for a in complete
    ] == [
        {"length_1": 4, "length_2": 4, "length_at_least_3": 0},
        {"length_1": 5, "length_2": 7, "length_at_least_3": 0},
        {"length_1": 9, "length_2": 7, "length_at_least_3": 0},
        {"length_1": 13, "length_2": 6, "length_at_least_3": 1},
    ]
    for packet in complete.values():
        assert packet["degree_bound_checks_passed"] == packet["raw_relation_count"]
        assert list(
            packet["tangent_source_closure"]["multiplication_image_ranks"].values()
        ) == [7, 7, 7]

    replication = load(
        "rank26-total-energy-rees-source-comparison-a12-p32009-point-3-5-m8.json"
    )
    for key in (
        "cokernel_dimensions",
        "support_excess",
        "elementary_length_census",
        "relation_ranks",
    ):
        assert replication[key] == complete[12][key]
    assert replication["field"] == 32009
    assert replication["point"] == [3, 5, -8]

    relative = {
        ambient: load(f"rank26-total-energy-relative-low-rees-a{ambient}-p32003.json")
        for ambient in (12, 14)
    }
    for packet in relative.values():
        assert packet["low_rees_dimensions"] == {"T1": 7, "T2": 14, "T3": 26}
        assert packet["first_differences"] == [7, 12]
        assert packet["generic_low_rank"] == 25
        assert packet["affine_through_order_three"] is False

    result = {
        "schema": "marici.benincasa.rank26-total-energy-rees-typing-falsifier.v1",
        "full_cokernel_support_excess_by_ambient": {
            str(a): complete[a]["support_excess"] for a in complete
        },
        "full_cokernel_cutoff_stable": False,
        "source_multiplication_ranks": [7, 7, 7],
        "independent_prime_point_replication": True,
        "relative_low_rees_dimensions_at_ambient_12_and_14": [7, 14, 26],
        "relative_low_generic_rank": 25,
        "relative_low_is_complete_rank26_module": False,
        "conclusion": (
            "neither the full Laurent cokernel nor the static low relative chart "
            "is the source-cyclic rank-26 total-energy nearby object"
        ),
        "next_object": "Rees lattice of the source-cyclic rank-26 submodule",
    }
    output = HERE / "rank26-total-energy-rees-typing-falsifier.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
