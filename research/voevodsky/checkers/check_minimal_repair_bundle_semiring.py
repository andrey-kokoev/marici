from __future__ import annotations

import json
from typing import FrozenSet


Bundle = FrozenSet[str]
Antichain = FrozenSet[Bundle]


def minimize(bundles: set[Bundle]) -> Antichain:
    return frozenset(bundle for bundle in bundles if not any(other < bundle for other in bundles))


def alternative(left: Antichain, right: Antichain) -> Antichain:
    return minimize(set(left | right))


def conjunction(left: Antichain, right: Antichain) -> Antichain:
    return minimize({a | b for a in left for b in right})


def main() -> None:
    proof = frozenset({frozenset({"filler"})})
    operational = frozenset({frozenset({"constructor", "faults"})})
    obligation = alternative(proof, operational)
    assert obligation == frozenset({frozenset({"filler"}), frozenset({"constructor", "faults"})})
    assert frozenset({"filler", "constructor", "faults"}) not in obligation

    second = frozenset({frozenset({"descent"}), frozenset({"completion", "comparison"})})
    composite = conjunction(obligation, second)
    expected = frozenset({
        frozenset({"filler", "descent"}),
        frozenset({"filler", "completion", "comparison"}),
        frozenset({"constructor", "faults", "descent"}),
        frozenset({"constructor", "faults", "completion", "comparison"}),
    })
    assert composite == expected

    third = frozenset({frozenset({"source"}), frozenset({"typed_target", "map"})})
    assert conjunction(conjunction(obligation, second), third) == conjunction(obligation, conjunction(second, third))
    assert alternative(alternative(obligation, second), third) == alternative(obligation, alternative(second, third))
    assert conjunction(obligation, alternative(second, third)) == alternative(conjunction(obligation, second), conjunction(obligation, third))
    assert alternative(obligation, obligation) == obligation

    # Subsumption removes a more expensive superset repair.
    with_superset = minimize({frozenset({"filler"}), frozenset({"filler", "higher"})})
    assert with_superset == frozenset({frozenset({"filler"})})

    result = {
        "schema": "marici.voevodsky.minimal-repair-bundle-semiring.v1",
        "status": "alternative_backend_repair_algebra_verified",
        "minimal_repair_bundles": [sorted(bundle) for bundle in sorted(obligation, key=lambda item: (len(item), sorted(item)))],
        "flat_union_rejected": True,
        "alternative_operation_idempotent": True,
        "conjunction_operation_associative": True,
        "alternative_operation_associative": True,
        "distributive": True,
        "subsumption_minimization": True,
        "backend_selection_by_cardinality_authorized": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
