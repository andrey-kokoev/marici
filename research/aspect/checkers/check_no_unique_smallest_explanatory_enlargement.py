from __future__ import annotations

import json
from pathlib import Path


def record(port, history):
    first, second = history
    if port == "base":
        return ()
    if port == "A":
        return (first,)
    if port == "B":
        return (second,)
    if port == "AB":
        return (first, second)
    raise ValueError(port)


def distinguishes(port, left, right):
    return record(port, left) != record(port, right)


def refines(left_port, right_port, histories):
    # left_port refines right_port when equality under left implies equality
    # under right for every pair of histories.
    for left in histories:
        for right in histories:
            if record(left_port, left) == record(left_port, right):
                if record(right_port, left) != record(right_port, right):
                    return False
    return True


def main() -> None:
    histories = ((0, 0), (0, 1), (1, 0), (1, 1))
    ports = ("base", "A", "B", "AB")
    target_pair = ((0, 0), (1, 1))

    sufficient = tuple(
        port for port in ports if distinguishes(port, target_pair[0], target_pair[1])
    )
    assert sufficient == ("A", "B", "AB")

    assert not refines("A", "B", histories)
    assert not refines("B", "A", histories)
    assert refines("AB", "A", histories)
    assert refines("AB", "B", histories)

    minimal_sufficient = tuple(
        port
        for port in sufficient
        if not any(
            other != port
            and other in sufficient
            and refines(port, other, histories)
            and not refines(other, port, histories)
            for other in sufficient
        )
    )
    assert minimal_sufficient == ("A", "B")

    a_neighbor_pair = ((0, 0), (1, 0))
    b_neighbor_pair = ((0, 0), (0, 1))
    assert distinguishes("A", *a_neighbor_pair)
    assert not distinguishes("B", *a_neighbor_pair)
    assert distinguishes("B", *b_neighbor_pair)
    assert not distinguishes("A", *b_neighbor_pair)

    unique_smallest_exists = len(minimal_sufficient) == 1
    assert not unique_smallest_exists

    result = {
        "schema": "marici.aspect.no-unique-smallest-explanatory-enlargement.v1",
        "status": "pass",
        "histories": ["".join(map(str, history)) for history in histories],
        "target_pair": ["00", "11"],
        "sufficient_ports": list(sufficient),
        "minimal_sufficient_ports": list(minimal_sufficient),
        "A_refines_B": refines("A", "B", histories),
        "B_refines_A": refines("B", "A", histories),
        "AB_refines_A": refines("AB", "A", histories),
        "AB_refines_B": refines("AB", "B", histories),
        "unique_smallest_enlargement_exists": unique_smallest_exists,
        "A_only_neighbor_distinction": ["00", "10"],
        "B_only_neighbor_distinction": ["00", "01"],
        "verdict": "Ports A and B are incomparable minimal sufficient extensions for distinguishing 00 from 11. Each fails a neighboring distinction that the other resolves, while AB is sufficient but nonminimal. Explanatory enlargement is a sufficiency frontier indexed by future questions, not necessarily one smallest object.",
        "claim_boundary": "finite admitted port poset with deterministic bit-valued records; establishes nonuniqueness in this model rather than every physical theory",
    }
    output = Path(__file__).parents[1] / "results" / "no_unique_smallest_explanatory_enlargement.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
