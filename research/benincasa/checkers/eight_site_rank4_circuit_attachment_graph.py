"""Build the typed occurrence-to-minimal-circuit support attachment graph.

Equal circuit nodes mean equal source-labelled linear dependences, up to the
unique primitive global sign.  The graph records support incidence only.  It
does not assign residue orientations or a physical current differential.
"""

import collections
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "results" / "eight-site-rank4-labelled-expansion.json"
TARGET = ROOT / "results" / "eight-site-rank4-circuit-attachment-graph.json"


def circuit_key(occurrence: dict, circuit: dict) -> tuple[str, int]:
    pairs = sorted(
        (label, int(coefficient))
        for label, coefficient in zip(occurrence["labels"], circuit["coefficients"])
        if coefficient
    )
    sign = 1
    if pairs[0][1] < 0:
        sign = -1
        pairs = [(label, -coefficient) for label, coefficient in pairs]
    return "|".join(f"{coefficient:+d}*{label}" for label, coefficient in pairs), sign


def main() -> None:
    source = json.loads(SOURCE.read_text())
    occurrences = source["occurrences"]
    attachments = []
    circuit_groups = collections.defaultdict(list)
    adjacency = collections.defaultdict(set)

    for occurrence in occurrences:
        occurrence_node = f"occurrence:{occurrence['occurrence_id']}"
        for circuit_index, circuit in enumerate(occurrence["labelled_circuits"]):
            key, canonicalization_sign = circuit_key(occurrence, circuit)
            circuit_node = f"circuit:{key}"
            attachment = {
                "occurrence_id": occurrence["occurrence_id"],
                "source_orbit_key": occurrence["source_orbit_key"],
                "cyclic_shift": occurrence["cyclic_shift"],
                "circuit_index": circuit_index,
                "circuit_key": key,
                "canonicalization_sign": canonicalization_sign,
                "regulator_sign_class": circuit["positive_regulator_cone_sign"],
            }
            attachments.append(attachment)
            circuit_groups[key].append(attachment)
            adjacency[occurrence_node].add(circuit_node)
            adjacency[circuit_node].add(occurrence_node)

    components = []
    visited = set()
    for node in sorted(adjacency):
        if node in visited:
            continue
        stack = [node]
        visited.add(node)
        nodes = []
        while stack:
            current = stack.pop()
            nodes.append(current)
            for neighbor in adjacency[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        occurrence_ids = sorted(item.removeprefix("occurrence:") for item in nodes if item.startswith("occurrence:"))
        circuit_keys = sorted(item.removeprefix("circuit:") for item in nodes if item.startswith("circuit:"))
        components.append({
            "occurrence_ids": occurrence_ids,
            "circuit_keys": circuit_keys,
            "occurrence_count": len(occurrence_ids),
            "circuit_count": len(circuit_keys),
        })

    components.sort(key=lambda item: item["occurrence_ids"][0])
    occurrence_component = {
        occurrence_id: component_index
        for component_index, component in enumerate(components)
        for occurrence_id in component["occurrence_ids"]
    }
    orbit_rotation_lookup = {
        (item["source_orbit_key"], item["cyclic_shift"]): item["occurrence_id"]
        for item in occurrences
    }
    one_step_exchanges_components = all(
        occurrence_component[item["occurrence_id"]]
        != occurrence_component[orbit_rotation_lookup[(item["source_orbit_key"], (item["cyclic_shift"] + 1) % 8)]]
        for item in occurrences
    )
    two_steps_preserve_components = all(
        occurrence_component[item["occurrence_id"]]
        == occurrence_component[orbit_rotation_lookup[(item["source_orbit_key"], (item["cyclic_shift"] + 2) % 8)]]
        for item in occurrences
    )

    multiplicities = collections.Counter(len(group) for group in circuit_groups.values())
    private = [key for key, group in circuit_groups.items() if len(group) == 1]
    private_mixed = [
        key for key in private
        if circuit_groups[key][0]["regulator_sign_class"] == "mixed"
    ]
    edge_count = len(attachments)
    vertex_count = len(occurrences) + len(circuit_groups)
    checks = {
        "occurrence_count": len(occurrences),
        "circuit_key_count": len(circuit_groups),
        "attachment_count": edge_count,
        "component_count": len(components),
        "component_shapes": [
            [component["occurrence_count"], component["circuit_count"]]
            for component in components
        ],
        "graph_cycle_rank": edge_count - vertex_count + len(components),
        "circuit_attachment_multiplicity_distribution": {
            str(key): value for key, value in sorted(multiplicities.items())
        },
        "private_circuit_count": len(private),
        "private_mixed_circuit_count": len(private_mixed),
        "one_step_cyclic_rotation_exchanges_components": one_step_exchanges_components,
        "two_step_cyclic_rotation_preserves_components": two_steps_preserve_components,
    }
    assert checks["occurrence_count"] == 288
    assert checks["circuit_key_count"] == 182
    assert checks["attachment_count"] == 1520
    assert checks["component_count"] == 2
    assert checks["component_shapes"] == [[144, 91], [144, 91]]
    assert checks["graph_cycle_rank"] == 1052
    assert checks["private_circuit_count"] == 32
    assert checks["private_mixed_circuit_count"] == 32
    assert one_step_exchanges_components
    assert two_steps_preserve_components

    output = {
        "schema": "marici.eight_site_rank4_circuit_attachment_graph.v1",
        "scope": {
            "included": "equality classes of primitive labelled minimal circuits and occurrence attachments",
            "excluded": "residue orientation, sewn Cech differential, and physical-current map",
        },
        "checks": checks,
        "components": components,
        "private_circuit_keys": sorted(private),
        "private_mixed_circuit_keys": sorted(private_mixed),
        "circuit_groups": {
            key: group for key, group in sorted(circuit_groups.items())
        },
    }
    TARGET.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(checks, sort_keys=True))


if __name__ == "__main__":
    main()
