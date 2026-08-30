from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


Matrix = list[list[F]]
STATES = ("H", "V", "D_a", "D_b", "A", "dead")
GENERATORS = ("H", "V", "D", "A")
RAY = {"H": "H", "V": "V", "D_a": "D", "D_b": "D", "A": "A", "dead": "dead"}
PROJECTOR: dict[str, Matrix] = {
    "H": [[F(1), F(0)], [F(0), F(0)]],
    "V": [[F(0), F(0)], [F(0), F(1)]],
    "D": [[F(1, 2), F(1, 2)], [F(1, 2), F(1, 2)]],
    "A": [[F(1, 2), F(-1, 2)], [F(-1, 2), F(1, 2)]],
}
SUCCESSOR = {"H": "H", "V": "V", "D": "D_a", "A": "A"}


def mm(a: Matrix, b: Matrix) -> Matrix:
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0)) for j in range(len(b[0]))] for i in range(len(a))]


def tr(a: Matrix) -> F:
    return sum((a[i][i] for i in range(len(a))), F(0))


def scale(a: Matrix, value: F) -> Matrix:
    return [[value * x for x in row] for row in a]


def analyzer_response(state: str, generator: str) -> tuple[F, str]:
    if state == "dead":
        return F(0), "dead"
    probability = tr(mm(PROJECTOR[RAY[state]], PROJECTOR[generator]))
    return (probability, SUCCESSOR[generator]) if probability else (F(0), "dead")


def canonical_partition(groups: list[list[str]]) -> tuple[tuple[str, ...], ...]:
    return tuple(sorted((tuple(sorted(group)) for group in groups), key=lambda group: group[0]))


def refine(partition: tuple[tuple[str, ...], ...]) -> tuple[tuple[str, ...], ...]:
    block_of = {state: index for index, block in enumerate(partition) for state in block}
    fibers: dict[tuple, list[str]] = {}
    for state in STATES:
        current_output = int(state != "dead")
        future = tuple((str(probability), block_of[successor]) for probability, successor in (analyzer_response(state, g) for g in GENERATORS))
        fibers.setdefault((current_output, future), []).append(state)
    return canonical_partition(list(fibers.values()))


def stabilized_partition() -> tuple[tuple[tuple[str, ...], ...], int]:
    partition = canonical_partition([[s for s in STATES if s != "dead"], ["dead"]])
    iterations = 0
    while True:
        successor = refine(partition)
        iterations += 1
        if successor == partition:
            return partition, iterations
        partition = successor


def preserves_partition(mapping: dict[str, str], partition: tuple[tuple[str, ...], ...]) -> bool:
    block_of = {state: index for index, block in enumerate(partition) for state in block}
    return all(len({block_of[mapping[state]] for state in block}) == 1 for block in partition)


def encode_matrix(a: Matrix) -> list[list[str]]:
    return [[str(x) for x in row] for row in a]


def main() -> None:
    stable, iterations = stabilized_partition()
    expected = canonical_partition([["H"], ["V"], ["D_a", "D_b"], ["A"], ["dead"]])
    assert stable == expected

    old_partition = canonical_partition([["H", "V", "D_a", "D_b", "A"], ["dead"]])
    old_block = {state: index for index, block in enumerate(old_partition) for state in block}
    stable_to_old = {"|".join(block): old_block[block[0]] for block in stable}
    assert all(old_block[state] == old_block["H"] for state in ("H", "V", "D_a", "D_b", "A"))
    assert len({block for block in stable if block != ("dead",)}) == 4

    mixed = [[F(1, 2), F(0)], [F(0), F(1, 2)]]
    h_then_d = mm(mm(PROJECTOR["D"], mm(mm(PROJECTOR["H"], mixed), PROJECTOR["H"])), PROJECTOR["D"])
    d_then_h = mm(mm(PROJECTOR["H"], mm(mm(PROJECTOR["D"], mixed), PROJECTOR["D"])), PROJECTOR["H"])
    assert tr(h_then_d) == tr(d_then_h) == F(1, 4)
    assert h_then_d != d_then_h
    downstream_h = [
        tr(mm(PROJECTOR["H"], h_then_d)) / tr(h_then_d),
        tr(mm(PROJECTOR["H"], d_then_h)) / tr(d_then_h),
    ]
    assert downstream_h == [F(1, 2), F(1)]

    horizontal_lift = scale(PROJECTOR["H"], F(1, 4))
    diagonal_lift = scale(PROJECTOR["D"], F(1, 4))
    assert tr(horizontal_lift) == tr(diagonal_lift) == F(1, 4)
    assert horizontal_lift != diagonal_lift

    good_map = {state: ("H" if state in ("D_a", "D_b") else state) for state in STATES}
    bad_map = {state: state for state in STATES}
    bad_map["D_a"] = "H"
    bad_map["D_b"] = "V"
    assert preserves_partition(good_map, stable)
    assert not preserves_partition(bad_map, stable)
    assert old_block[bad_map["D_a"]] == old_block[bad_map["D_b"]]

    result = {
        "schema": "marici.aspect.optical-stabilized-behavioral-congruence.v1",
        "status": "pass",
        "authorized_future_analyzers": list(GENERATORS),
        "stabilization_iterations": iterations,
        "old_partition": old_partition,
        "stable_partition": stable,
        "canonical_stable_to_old_downgrade": stable_to_old,
        "canonical_old_to_stable_upgrade_exists": False,
        "equal_old_scalar_probability": "1/4",
        "equal_scalar_continuations_equal": False,
        "downstream_h_conditional_probabilities": [str(x) for x in downstream_h],
        "distinct_continuation_lifts": [encode_matrix(horizontal_lift), encode_matrix(diagonal_lift)],
        "good_old_operation_preserves_stable_congruence": True,
        "hostile_label_dependent_operation_preserves_old_scalar_class": True,
        "hostile_label_dependent_operation_preserves_stable_congruence": False,
        "verdict": "Migration needs refined-congruence preservation and source-selected continuation lifts; old scalar equality supplies neither.",
        "claim_boundary": "finite exact ideal-polarization stabilized congruence",
    }
    output = Path(__file__).parents[1] / "results" / "optical_stabilized_behavioral_congruence.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
