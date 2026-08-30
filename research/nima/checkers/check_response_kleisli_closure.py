"""Exact audit of compositional closure for value/residue responses."""

from __future__ import annotations

import itertools
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/response-kleisli-closure.json"


@dataclass(frozen=True)
class Response:
    kind: str
    value: int | None
    residue: tuple[str, ...]


def value(x: int) -> Response:
    return Response("value", x, ())


def qualified(x: int, label: str) -> Response:
    return Response("qualified", x, (label,))


def obstruction(label: str) -> Response:
    return Response("obstruction", None, (label,))


def bind(response: Response, operation: Callable[[int], Response]) -> Response:
    if response.kind == "obstruction":
        return response
    assert response.value is not None
    following = operation(response.value)
    residues = response.residue + following.residue
    if following.kind == "obstruction":
        return Response("obstruction", None, residues)
    assert following.value is not None
    return Response("qualified" if residues else "value", following.value, residues)


operations: tuple[Callable[[int], Response], ...] = (
    lambda x: value(x + 1),
    lambda x: qualified(2 * x, "qualified-step"),
    lambda _x: obstruction("blocked-step"),
)
initial = (value(2), qualified(2, "prior"), obstruction("prior-block"))

associativity_checks = 0
for response, first, second in itertools.product(initial, operations, operations):
    left = bind(bind(response, first), second)
    right = bind(response, lambda x, f=first, g=second: bind(f(x), g))
    associativity_checks += 1
    assert left == right

all_composites = tuple(
    bind(response, operation)
    for response, operation in itertools.product(initial, operations)
)

forward_trace = ("restriction", "boundary")
reverse_trace = ("boundary", "restriction")

gates = {
    "three_cases_are_closed_under_composition": all(
        response.kind in {"value", "qualified", "obstruction"}
        for response in all_composites
    ),
    "composition_is_associative": associativity_checks == 27,
    "obstruction_preserves_prior_residue": bind(
        qualified(1, "prior"), lambda _x: obstruction("later")
    ).residue == ("prior", "later"),
    "qualified_composition_accumulates_ordered_residue": bind(
        qualified(1, "first"), lambda x: qualified(x, "second")
    ).residue == ("first", "second"),
    "none_none_is_not_created": all(
        response.value is not None or response.residue
        for response in all_composites
    ),
    "unordered_payload_forgets_path_order": (
        forward_trace != reverse_trace and set(forward_trace) == set(reverse_trace)
    ),
}
assert all(gates.values()), gates

result = {
    "schema": "marici.nima.response-kleisli-closure.v1",
    "associativity_checks": associativity_checks,
    "gates": gates,
    "conclusion": (
        "The three response cases are closed and associative under Kleisli-like "
        "composition when residues are ordered typed traces. No fourth top-level "
        "case is forced, but a flat unordered residue loses composition data; "
        "alternative path comparisons require higher coherence inside R."
    ),
}
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))
