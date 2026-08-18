"""Retain the literal three-q pivot certificate and test the source top class."""

from __future__ import annotations

import argparse
import json

from physical_single_q_twisted_derham_calibration import Q_POLYNOMIALS
from physical_top_twisted_derham_calibration import PRIME, add_pivot
from physical_two_q_twisted_derham_calibration import filtered_presentation


def quotient_reduce(vector: dict[int, int], pivots: dict[int, dict[int, int]]) -> dict[int, int]:
    result = {column: value % PRIME for column, value in vector.items() if value % PRIME}
    for pivot in sorted(pivots, reverse=True):
        coefficient = result.get(pivot, 0)
        if not coefficient:
            continue
        for column, value in pivots[pivot].items():
            next_value = (result.get(column, 0) - coefficient * value) % PRIME
            if next_value:
                result[column] = next_value
            else:
                result.pop(column, None)
    assert not (set(result) & set(pivots))
    return result


def span_rank(vectors: list[dict[int, int]]) -> int:
    basis: dict[int, dict[int, int]] = {}
    for vector in vectors:
        add_pivot(dict(vector), basis)
    return len(basis)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--gamma", type=int, default=5)
    parser.add_argument("--ambient", type=int, default=9)
    parser.add_argument("--cutoff", type=int, default=5)
    args = parser.parse_args()

    names = ("g1", "g2", "G12")
    ordered, columns, low_labels, pivots = filtered_presentation(
        tuple(Q_POLYNOMIALS[name] for name in names),
        k_depth=2,
        q_depth=2,
        ambient_degree=args.ambient,
        cutoff_degree=args.cutoff,
        gamma=args.gamma % PRIME,
    )
    del ordered

    reduced_low = {
        label: quotient_reduce({columns[label]: 1}, pivots) for label in low_labels
    }
    full_rank = span_rank(list(reduced_low.values()))
    proper_face_vectors = [
        vector
        for label, vector in reduced_low.items()
        if 0 in label[1:4]
    ]
    proper_face_rank = span_rank(proper_face_vectors)

    source_label = (0, 1, 1, 1, (0, 0, 0))
    source_vector = reduced_low[source_label]
    source_augmented_rank = span_rank(proper_face_vectors + [source_vector])

    assert full_rank == 21
    assert proper_face_rank == 20
    assert source_augmented_rank == 21

    print(
        json.dumps(
            {
                "schema": "marici.physical-three-q-source-top-projection.v1",
                "prime": PRIME,
                "kinematics": [2, 3, 4],
                "gamma": args.gamma,
                "ambient_degree": args.ambient,
                "cutoff_degree": args.cutoff,
                "quotient_rank": full_rank,
                "proper_face_span_rank": proper_face_rank,
                "proper_top_quotient_rank": full_rank - proper_face_rank,
                "source_label": [0, 1, 1, 1, [0, 0, 0]],
                "source_reduced_support_size": len(source_vector),
                "rank_after_adjoining_source": source_augmented_rank,
                "source_occupies_proper_top_line": True,
                "canonical_T7_lift_selected": False,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
