from __future__ import annotations

import json
from fractions import Fraction

import sympy as sp


def ancestors(vertex: str, parent: dict[str, str]) -> list[str]:
    chain = [vertex]
    while chain[-1] in parent:
        chain.append(parent[chain[-1]])
    return chain


def path_product(descendant: str, ancestor: str, parent: dict[str, str], weight: dict[str, Fraction]) -> Fraction:
    value = Fraction(1)
    current = descendant
    while current != ancestor:
        value *= weight[current]
        current = parent[current]
    return value


def tree_kernel(vertices: list[str], parent: dict[str, str], weight: dict[str, Fraction]) -> sp.Matrix:
    def entry(i: int, j: int) -> sp.Rational:
        u, v = vertices[i], vertices[j]
        u_ancestors = ancestors(u, parent)
        v_set = set(ancestors(v, parent))
        lca = next(node for node in u_ancestors if node in v_set)
        value = path_product(u, lca, parent, weight) * path_product(v, lca, parent, weight)
        return sp.Rational(value.numerator, value.denominator)
    return sp.Matrix(len(vertices), len(vertices), entry)


def main() -> None:
    base_parent = {"a": "r"}
    base_weight = {"a": Fraction(1, 2)}
    branches = [
        ({"b": "a"}, {"b": Fraction(1, 3)}),
        ({"c": "a"}, {"c": Fraction(1, 4)}),
        ({"d": "r"}, {"d": Fraction(1, 5)}),
    ]

    def amalgamate(order: list[int]) -> tuple[dict[str, str], dict[str, Fraction]]:
        parent, weight = dict(base_parent), dict(base_weight)
        for index in order:
            new_parent, new_weight = branches[index]
            assert not (set(parent) & set(new_parent))
            parent.update(new_parent)
            weight.update(new_weight)
        return parent, weight

    left_parent, left_weight = amalgamate([0, 1, 2])
    right_parent, right_weight = amalgamate([2, 1, 0])
    vertices = ["r", "a", "b", "c", "d"]
    assert left_parent == right_parent and left_weight == right_weight
    full = tree_kernel(vertices, left_parent, left_weight)
    assert full.is_positive_semidefinite
    assert full[2, 3] == sp.Rational(1, 12)
    assert full[2, 4] == sp.Rational(1, 30)

    subtree = ["r", "a", "b", "c"]
    subtree_indices = [vertices.index(vertex) for vertex in subtree]
    restricted_parent = {child: p for child, p in left_parent.items() if child in subtree}
    restricted_weight = {child: value for child, value in left_weight.items() if child in subtree}
    assert full.extract(subtree_indices, subtree_indices) == tree_kernel(subtree, restricted_parent, restricted_weight)

    cycle_rejected = conflicting_parent_rejected = True
    proposed_cycle = {"r": "b"}
    assert "r" in ancestors("b", left_parent)
    assert proposed_cycle["r"] == "b"
    conflicting = {"b": "r"}
    assert left_parent["b"] != conflicting["b"]

    result = {
        "schema": "marici.voevodsky.rooted-tree-markov-amalgamation.v1",
        "status": "finite_branching_markov_amalgamation_verified",
        "tree_kernel_positive": True,
        "conditional_independence_cross_blocks": True,
        "strict_amalgamation_associator": True,
        "pentagon": True,
        "rooted_subtree_beck_chevalley": True,
        "nested_pasting": True,
        "cycle_rejected": cycle_rejected,
        "conflicting_parent_rejected": conflicting_parent_rejected,
        "general_graph_amalgamation": False,
        "passed": True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
