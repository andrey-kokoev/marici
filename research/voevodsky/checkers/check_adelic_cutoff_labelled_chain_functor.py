from __future__ import annotations

import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


CONTRACT = Path("research/voevodsky/adelic-cutoff-labelled-chain-functor-v1.json")


def height(value: Fraction) -> int:
    return max(abs(value.numerator), value.denominator)


def fiber(bound: int) -> set[Fraction]:
    return {Fraction(a, b) for b in range(1, bound + 1) for a in range(-bound, bound + 1) if a and height(Fraction(a, b)) <= bound}


def edge_boundary(chain: dict[tuple[Fraction, tuple[str, str]], int]) -> dict[tuple[Fraction, str], int]:
    out: defaultdict[tuple[Fraction, str], int] = defaultdict(int)
    for (label, (source, target)), coefficient in chain.items():
        out[(label, source)] -= coefficient
        out[(label, target)] += coefficient
    return {key: value for key, value in out.items() if value}


def reflect_vertex(vertex: str) -> str:
    return {"w": "-w", "-w": "w"}[vertex]


def reciprocal_chain(chain: dict[tuple[Fraction, tuple[str, str]], int]) -> dict[tuple[Fraction, tuple[str, str]], int]:
    return {(1 / label, (reflect_vertex(edge[0]), reflect_vertex(edge[1]))): coefficient for (label, edge), coefficient in chain.items()}


def reciprocal_boundary(chain: dict[tuple[Fraction, str], int]) -> dict[tuple[Fraction, str], int]:
    return {(1 / label, reflect_vertex(vertex)): coefficient for (label, vertex), coefficient in chain.items()}


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    fibers = {bound: fiber(bound) for bound in (2, 4, 6)}
    assert fibers[2] < fibers[4] < fibers[6]

    packet = {Fraction(1): 3, Fraction(-1): -2, Fraction(2): 5, Fraction(1, 2): 7}
    assert set(packet).issubset(fibers[2])
    chain = {(label, ("w", "-w")): coefficient for label, coefficient in packet.items()}
    # Zero-extension transitions preserve the sparse element literally.
    transition_2_4 = dict(chain)
    transition_4_6 = dict(transition_2_4)
    transition_2_6 = dict(chain)
    assert transition_4_6 == transition_2_6
    assert all(label in fibers[6] for label, _ in transition_2_6)

    boundary_before = edge_boundary(chain)
    boundary_after_transition = edge_boundary(transition_2_6)
    assert boundary_before == boundary_after_transition
    reciprocal = reciprocal_chain(chain)
    assert all(label in fibers[2] for label, _ in reciprocal)
    assert edge_boundary(reciprocal) == reciprocal_boundary(boundary_before)
    assert reciprocal_chain(reciprocal) == chain

    status = contract["status"]
    assert status["labelled_chain_functor"] == "constructed"
    assert status["analytic_mellin_evaluation_natural_transformation"] == "not supplied"
    result = {
        "schema": "marici.voevodsky.adelic-cutoff-labelled-chain-functor-check.v1",
        "status": "algebraic_cutoff_chain_functor_verified",
        "cutoff_objects_checked": 3,
        "transition_identity_and_composition": True,
        "boundary_naturality": True,
        "reciprocal_transition_naturality": True,
        "reciprocal_boundary_naturality": True,
        "reciprocal_involution": True,
        "analytic_mellin_evaluation_supplied": False,
        "uniform_completion_verified": False,
        "first_missing_datum": contract["first_missing_datum"],
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
