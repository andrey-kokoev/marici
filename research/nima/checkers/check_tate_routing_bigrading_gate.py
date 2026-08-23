"""Exact grading census for the two missing eight-cone routing bits.

This does not assert a source-to-target map.  It tests the candidate grading
forced by the full-log signed rays against the literal Boolean/Tor grading.
"""

from collections import Counter
from itertools import product
import json


PAIRS = ((0, 1), (0, 2), (1, 2))


def main() -> None:
    source_rows = [
        (signs, pair)
        for signs in product((1, -1), repeat=3)
        for pair in PAIRS
    ]
    source_degree = Counter(
        sum(signs[axis] == -1 for axis in pair)
        for signs, pair in source_rows
    )
    assert source_degree == Counter({0: 6, 1: 12, 2: 6})

    # Six road/sheet bases, two missing-state types (size two or full size
    # three), and two conductor Tor grades.
    target_rows = [
        (base, missing_extra, tor)
        for base in range(6)
        for missing_extra in (0, 1)
        for tor in (0, 1)
    ]
    target_degree = Counter(
        missing_extra + tor for _, missing_extra, tor in target_rows
    )
    assert target_degree == Counter({0: 6, 1: 12, 2: 6})
    assert source_degree == target_degree

    # After a base (pair, remaining sheet) <-> (road, sheet) identification,
    # every base contains four rows. Degree zero and two have unique targets;
    # the two degree-one source rows may still be exchanged between
    # (small, Tor1) and (full, Tor0).
    per_base_degree_counts = Counter(
        sum(sign == -1 for sign in pair_signs)
        for pair_signs in product((1, -1), repeat=2)
    )
    assert per_base_degree_counts == Counter({0: 1, 1: 2, 2: 1})
    independent_middle_swaps_before_symmetry = 2**6
    d3_transported_middle_swaps = 2
    assert independent_middle_swaps_before_symmetry == 64

    packet = {
        "claim": (
            "The contracted-negative-ray grading and literal "
            "(Boolean-excess plus Tor) grading have the identical census "
            "(6,12,6).  Conditional on a base identification, grading fixes "
            "the degree-zero and degree-two routes and leaves only a binary "
            "exchange of the two degree-one decorations."
        ),
        "status": "proved_scoped_conditional_reduction",
        "source_degree_census": dict(sorted(source_degree.items())),
        "target_degree_census": dict(sorted(target_degree.items())),
        "per_base_degree_census": dict(sorted(per_base_degree_counts.items())),
        "unconstrained_per_base_middle_swaps": independent_middle_swaps_before_symmetry,
        "d3_transported_global_middle_choices": d3_transported_middle_swaps,
        "not_proved": (
            "The grading itself does not identify the road/sheet base and "
            "does not choose which mixed contracted-sign orientation maps "
            "to (small Boolean, Tor1) versus (full Boolean, Tor0)."
        ),
        "next_test": (
            "Construct the ordered occurrence-line/excess-Gysin comparison "
            "which identifies one source sign flip with the flip-normal "
            "direction and the other with the Cartier-Tor direction; then "
            "audit reflection and the six-short-facet global boundary."
        ),
    }
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
