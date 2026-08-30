#!/usr/bin/env python3
"""Freeze the minimal graph whose bridge Cut returns two triangle loops."""

import json
from pathlib import Path


def components(vertices, edges):
    adjacency = {vertex: set() for vertex in vertices}
    for left, right in edges:
        adjacency[left].add(right)
        adjacency[right].add(left)
    unseen = set(vertices)
    result = []
    while unseen:
        seed = min(unseen)
        stack = [seed]
        block = set()
        while stack:
            current = stack.pop()
            if current in block:
                continue
            block.add(current)
            unseen.discard(current)
            stack.extend(adjacency[current] - block)
        result.append(sorted(block))
    return result


def loop_rank(vertices, edges, component_count=1):
    return len(edges) - len(vertices) + component_count


def main() -> None:
    vertices = [1, 2, 3, 4, 5, 6]
    left_edges = [(1, 2), (2, 3), (3, 1)]
    right_edges = [(4, 5), (5, 6), (6, 4)]
    bridge = (3, 4)
    edges = left_edges + [bridge] + right_edges
    cut_edges = [edge for edge in edges if edge != bridge]
    blocks = components(vertices, cut_edges)

    checks = {
        "graph_is_connected": components(vertices, edges) == [vertices],
        "bridge_deletion_has_two_components": blocks == [[1, 2, 3], [4, 5, 6]],
        "left_component_is_triangle": set(left_edges) == {(1, 2), (2, 3), (3, 1)},
        "right_component_is_triangle": set(right_edges) == {(4, 5), (5, 6), (6, 4)},
        "total_loop_rank_is_two": loop_rank(vertices, edges) == 2,
        "each_cut_component_has_loop_rank_one": (
            loop_rank(blocks[0], left_edges) == 1 and loop_rank(blocks[1], right_edges) == 1
        ),
        "bridge_is_unique_cut_interface": len(edges) - len(cut_edges) == 1,
        "six_vertices_are_minimal_for_two_vertex_disjoint_triangles": len(vertices) == 2 * 3,
        "seven_edges_are_minimal_after_connecting_them": len(edges) == 3 + 3 + 1,
    }
    packet = {
        "schema": "marici.minimal-double-triangle-cut-source.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "graph": {
            "vertices": vertices,
            "edges": [list(edge) for edge in edges],
            "left_triangle": [1, 2, 3],
            "right_triangle": [4, 5, 6],
            "bridge_cut": list(bridge),
            "loop_rank": 2,
        },
        "resolved_interface_occurrences": ["y_34,+", "y_34,-"],
        "partial_energies": {
            "left": "X1+X2+X3+y_34,+",
            "right": "X4+X5+X6+y_34,-",
            "physical_diagonal": "y_34,+=y_34,-=y_34",
        },
        "source_acquisition_target": (
            "complete canonical/OFPT integrand, labelled denominator terms, i-epsilon contour, and bridge-Cut factorization "
            "for the six-site seven-edge double-triangle graph"
        ),
        "not_yet_claimed": "no coefficient-torsor sewing map follows from this graph census alone",
        "checks": checks,
    }
    out = Path(__file__).with_name("minimal-double-triangle-cut-source.json")
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
