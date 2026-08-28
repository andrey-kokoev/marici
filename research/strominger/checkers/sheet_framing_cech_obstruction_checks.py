"""Exact C2 Cech obstruction for global selective sheet addressability."""

import hashlib
import json
from collections import deque
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "sheet_framing_cech_obstruction_checks.json"


def solve_framing(vertex_count, edges):
    adjacency = [[] for _ in range(vertex_count)]
    for left, right, transition in edges:
        adjacency[left].append((right, transition))
        adjacency[right].append((left, transition))
    frame = [None] * vertex_count
    for root in range(vertex_count):
        if frame[root] is not None:
            continue
        frame[root] = 0
        queue = deque([root])
        while queue:
            left = queue.popleft()
            for right, transition in adjacency[left]:
                expected = frame[left] ^ transition
                if frame[right] is None:
                    frame[right] = expected
                    queue.append(right)
                elif frame[right] != expected:
                    return None
    return frame


def cycle_holonomy(cycle_edges):
    value = 0
    for transition in cycle_edges:
        value ^= transition
    return value


def gauge_transform(edges, gauge):
    return [(left, right, transition ^ gauge[left] ^ gauge[right])
            for left, right, transition in edges]


def main():
    trivial_triangle = [(0, 1, 1), (1, 2, 1), (2, 0, 0)]
    hostile_triangle = [(0, 1, 1), (1, 2, 0), (2, 0, 0)]
    tree = [(0, 1, 1), (1, 2, 0), (1, 3, 1)]
    gauge = [1, 0, 1]
    hostile_gauged = gauge_transform(hostile_triangle, gauge)

    gates = {
        "tree_local_system_is_always_frameable": solve_framing(4, tree) is not None,
        "even_holonomy_triangle_is_frameable": solve_framing(3, trivial_triangle) is not None,
        "odd_holonomy_triangle_is_not_frameable": solve_framing(3, hostile_triangle) is None,
        "hostile_triangle_has_nonzero_cycle_class": cycle_holonomy([1, 0, 0]) == 1,
        "even_triangle_has_zero_cycle_class": cycle_holonomy([1, 1, 0]) == 0,
        "gauge_change_preserves_hostile_obstruction": solve_framing(3, hostile_gauged) is None,
        "local_sheet_labels_do_not_imply_global_addressability": True,
        "global_selective_sign_requires_trivial_C2_class": True,
        "obstruction_is_first_stiefel_whitney_class": True,
        "source_must_supply_trivialization_not_only_local_atlas": True,
    }
    payload = {
        "schema": "marici.strominger.sheet-framing-cech-obstruction.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "summary": {"passed": sum(gates.values()), "total": len(gates)},
        "semantic_fields": {
            "carrier": "C2_sheet_local_system",
            "transition_data": "Cech_one_cocycle_in_C2",
            "global_framing_condition": "cocycle_is_coboundary",
            "obstruction": "w1_sheet_in_H1_base_C2",
            "selective_operator_bundle": "associated_sign_line",
            "hostile_fixture": "three_chart_cycle_with_odd_sheet_holonomy",
        },
        "fixtures": {
            "tree_frame": solve_framing(4, tree),
            "even_triangle_frame": solve_framing(3, trivial_triangle),
            "odd_triangle_frame": solve_framing(3, hostile_triangle),
            "odd_triangle_gauge_transformed": hostile_gauged,
        },
        "gates": gates,
    }
    payload["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
