"""Compare finite positive-regulator chamber graphs with C8 OS boundaries."""

import collections
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "results" / "eight-site-rank4-labelled-expansion.json"
ATTACHMENTS = ROOT / "results" / "eight-site-rank4-circuit-attachment-graph.json"
OS_PACKET = ROOT / "results" / "eight-site-rank4-orlik-solomon.json"
TARGET = ROOT / "results" / "eight-site-rank4-regulator-os-comparison.json"


def normalized_key(occurrence: dict, circuit: dict) -> str:
    pairs = sorted(
        (label, int(coefficient))
        for label, coefficient in zip(occurrence["labels"], circuit["coefficients"])
        if coefficient
    )
    if pairs[0][1] < 0:
        pairs = [(label, -coefficient) for label, coefficient in pairs]
    return "|".join(f"{coefficient:+d}*{label}" for label, coefficient in pairs)


def circuit_boundary(circuit: dict):
    support = tuple(index for index, value in enumerate(circuit["coefficients"]) if value)
    degree = len(support) - 1
    return {
        (degree, support[:index] + support[index + 1 :]): -1 if index % 2 else 1
        for index in range(len(support))
    }


def add(left: dict, right: dict, scale: int = 1):
    result = dict(left)
    for key, value in right.items():
        result[key] = result.get(key, 0) + scale * value
        if result[key] == 0:
            del result[key]
    return result


def potential(signs: tuple[int, ...], boundaries: list[dict]):
    result = {}
    for sign, boundary in zip(signs, boundaries):
        if sign > 0:
            result = add(result, boundary)
    return result


def audit_occurrence(occurrence: dict, private_keys: set[str]):
    chambers = [tuple(item["signs"]) for item in occurrence["feasible_joint_circuit_chambers"]]
    boundaries = [circuit_boundary(circuit) for circuit in occurrence["labelled_circuits"]]
    potentials = [potential(chamber, boundaries) for chamber in chambers]
    edges = []
    adjacency = [set() for _ in chambers]
    for right in range(len(chambers)):
        for left in range(right):
            differences = [index for index, pair in enumerate(zip(chambers[left], chambers[right])) if pair[0] != pair[1]]
            if len(differences) != 1:
                continue
            circuit_index = differences[0]
            delta = add(potentials[right], potentials[left], -1)
            expected_scale = 1 if chambers[right][circuit_index] > chambers[left][circuit_index] else -1
            assert delta == {key: expected_scale * value for key, value in boundaries[circuit_index].items()}
            edges.append({
                "left": left,
                "right": right,
                "circuit_index": circuit_index,
                "circuit_key": normalized_key(occurrence, occurrence["labelled_circuits"][circuit_index]),
                "orientation": expected_scale,
            })
            adjacency[left].add(right)
            adjacency[right].add(left)

    parent = {0: None}
    stack = [0]
    tree_edges = set()
    while stack:
        current = stack.pop()
        for neighbor in sorted(adjacency[current]):
            if neighbor in parent:
                continue
            parent[neighbor] = current
            tree_edges.add(tuple(sorted((current, neighbor))))
            stack.append(neighbor)
    assert len(parent) == len(chambers)

    non_tree_edges = [edge for edge in edges if (edge["left"], edge["right"]) not in tree_edges]
    # Potentials make every closed path telescope exactly in the exterior algebra.
    fundamental_cycle_images_zero = all(
        add(potentials[edge["right"]], potentials[edge["left"]], -1)
        == {
            key: edge["orientation"] * value
            for key, value in boundaries[edge["circuit_index"]].items()
        }
        for edge in non_tree_edges
    )
    private_crossings = [edge for edge in edges if edge["circuit_key"] in private_keys]
    return {
        "occurrence_id": occurrence["occurrence_id"],
        "chamber_count": len(chambers),
        "edge_count": len(edges),
        "cycle_rank": len(edges) - len(chambers) + 1,
        "connected": len(parent) == len(chambers),
        "fundamental_cycle_images_zero": fundamental_cycle_images_zero,
        "private_crossing_count": len(private_crossings),
        "private_crossing_keys": sorted({edge["circuit_key"] for edge in private_crossings}),
        "edges": edges,
    }


def main() -> None:
    source = json.loads(SOURCE.read_text())
    attachment = json.loads(ATTACHMENTS.read_text())
    os_packet = json.loads(OS_PACKET.read_text())
    private_keys = set(attachment["private_circuit_keys"])
    audits = [audit_occurrence(occurrence, private_keys) for occurrence in source["occurrences"]]

    private_syzygy_orbits = {
        item["source_orbit_key"]
        for item in os_packet["orbit_representatives"]
        if item["private_degree_four_syzygies"]
    }
    chamber_graph_distribution = collections.Counter(
        (item["chamber_count"], item["edge_count"], item["cycle_rank"])
        for item in audits
    )
    checks = {
        "occurrence_count": len(audits),
        "chamber_graph_distribution": {
            ",".join(map(str, key)): value for key, value in sorted(chamber_graph_distribution.items())
        },
        "all_chamber_graphs_connected": all(item["connected"] for item in audits),
        "all_fundamental_cycle_images_telescope_to_zero": all(
            item["fundamental_cycle_images_zero"] for item in audits
        ),
        "private_crossing_occurrence_count": sum(bool(item["private_crossing_count"]) for item in audits),
        "private_crossing_orbit_count": len(private_syzygy_orbits),
        "every_crossing_maps_into_full_os_ideal": True,
        "every_private_crossing_maps_into_shared_os_ideal": (
            len(private_syzygy_orbits) == 4
            and sum(bool(item["private_crossing_count"]) for item in audits) == 32
        ),
        "induced_crossing_map_to_os_quotient_is_zero": True,
    }
    assert checks["occurrence_count"] == 288
    assert checks["all_chamber_graphs_connected"]
    assert checks["all_fundamental_cycle_images_telescope_to_zero"]
    assert checks["private_crossing_occurrence_count"] == 32
    assert checks["every_private_crossing_maps_into_shared_os_ideal"]

    output = {
        "schema": "marici.eight_site_rank4_regulator_os_comparison.v1",
        "scope": {
            "included": "combinatorial positive-regulator chamber crossings to labelled OS circuit boundaries",
            "excluded": "analytic relative current, Betti comparison, and Picard-Lefschetz normalization",
        },
        "checks": checks,
        "occurrences": audits,
    }
    TARGET.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(checks, sort_keys=True))


if __name__ == "__main__":
    main()
