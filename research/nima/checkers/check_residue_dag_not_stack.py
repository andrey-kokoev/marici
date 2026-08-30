"""Exact diamond test: residue resolution is a DAG, not canonically a stack."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/residue-dag-not-stack.json"

nodes = ("restrict", "gysin", "transport", "specialize", "coherence")
dependencies = {
    ("restrict", "gysin"),
    ("transport", "specialize"),
    ("gysin", "coherence"),
    ("specialize", "coherence"),
}


def respects(order: tuple[str, ...], edges: set[tuple[str, str]]) -> bool:
    position = {node: index for index, node in enumerate(order)}
    return all(position[left] < position[right] for left, right in edges)


construction_orders = tuple(
    order for order in itertools.permutations(nodes) if respects(order, dependencies)
)
repair_dependencies = {(right, left) for left, right in dependencies}
repair_orders = tuple(
    order for order in itertools.permutations(nodes) if respects(order, repair_dependencies)
)

left_stack = ("restrict", "gysin", "coherence")
right_stack = ("transport", "specialize", "coherence")

gates = {
    "diamond_has_six_linear_extensions": len(construction_orders) == 6,
    "repair_has_six_reverse_extensions": len(repair_orders) == 6,
    "coherence_waits_for_both_branches": all(
        order[-1] == "coherence" for order in construction_orders
    ),
    "coherence_repairs_before_both_branches": all(
        order[0] == "coherence" for order in repair_orders
    ),
    "neither_branch_stack_contains_full_residue": (
        set(left_stack) != set(nodes) and set(right_stack) != set(nodes)
    ),
    "lifo_requires_arbitrary_linear_extension": len(construction_orders) > 1,
}
assert all(gates.values()), gates

result = {
    "schema": "marici.nima.residue-dag-not-stack.v1",
    "nodes": nodes,
    "dependencies": sorted([list(edge) for edge in dependencies]),
    "construction_linear_extensions": len(construction_orders),
    "repair_linear_extensions": len(repair_orders),
    "gates": gates,
    "conclusion": (
        "A diamond coherence residue has a canonical dependency DAG but six "
        "valid stack linearizations. LIFO is valid only after an arbitrary "
        "linear extension; resolution is intrinsically partial-order driven."
    ),
}
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))
