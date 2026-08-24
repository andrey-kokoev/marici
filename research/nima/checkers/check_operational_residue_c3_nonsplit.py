"""Exact C3 attack on the operational-residue conjecture over F_3."""

from __future__ import annotations

import json
from itertools import product
from pathlib import Path


P = 3


def add(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((x + y) % P for x, y in zip(a, b))


def scale(c: int, a: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((c * x) % P for x in a)


def shift(a: tuple[int, int, int]) -> tuple[int, int, int]:
    return (a[2], a[0], a[1])


def delta(a: tuple[int, int, int]) -> tuple[int, int, int]:
    return add(shift(a), scale(-1, a))


def epsilon(a: tuple[int, int, int]) -> int:
    return sum(a) % P


def soft_gysin(a: tuple[int, int, int]) -> tuple[int, int, int]:
    return a


def span(vectors: list[tuple[int, ...]]) -> set[tuple[int, ...]]:
    if not vectors:
        return {()}
    zero = (0,) * len(vectors[0])
    result = {zero}
    for vector in vectors:
        result = {
            add(existing, scale(coefficient, vector))
            for existing in result
            for coefficient in range(P)
        }
    return result


def main() -> None:
    ambient = list(product(range(P), repeat=3))
    ideal = {a for a in ambient if epsilon(a) == 0}
    invariants = {a for a in ambient if shift(a) == a}
    norm = (1, 1, 1)

    assert len(ambient) == 27
    assert len(ideal) == 9
    assert invariants == span([norm])
    assert invariants <= ideal
    assert all(epsilon(a) == 0 for a in invariants)

    # An equivariant section k -> A would require an invariant augmentation-one vector.
    equivariant_section_candidates = {a for a in invariants if epsilon(a) == 1}
    assert not equivariant_section_candidates

    delta_ideal = {delta(a) for a in ideal}
    assert len(delta_ideal) == 3
    assert delta_ideal <= ideal
    tate_quotient_cardinality = len(ideal) // len(delta_ideal)
    assert tate_quotient_cardinality == 3

    # G_soft = identity preserves the filtration and differential exactly.
    assert all(soft_gysin(a) in ideal for a in ideal)
    assert all(delta(soft_gysin(a)) == soft_gysin(delta(a)) for a in ambient)
    assert all(epsilon(soft_gysin(a)) == epsilon(a) for a in ambient)

    # A labelled endpoint readout detects a kernel vector, while scalar sewing kills it.
    witness = (1, -1 % P, 0)
    assert witness in ideal
    assert witness not in delta_ideal
    assert soft_gysin(witness) == witness
    assert witness[0] == 1
    assert epsilon(witness) == 0

    result = {
        "status": "PASS",
        "field": "F_3",
        "ambient_cardinality": len(ambient),
        "augmentation_ideal_dimension": 2,
        "invariant_dimension": 1,
        "invariants_contained_in_augmentation_ideal": True,
        "equivariant_section_exists": False,
        "delta_ideal_dimension": 1,
        "tate_quotient_dimension": 1,
        "soft_gysin": "identity on F_3[C_3]",
        "induced_tate_map": "identity",
        "scalar_augmentation_on_residue": 0,
        "labelled_readout_on_witness": 1,
        "conclusion": (
            "The source-resolved result is a nonsplit C3-module extension. "
            "The canonical soft Gysin transports the nonzero Tate residue, "
            "while ordinary scalar sewing annihilates it."
        ),
    }

    output = Path(__file__).parents[1] / "results" / "operational-residue-c3-nonsplit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
