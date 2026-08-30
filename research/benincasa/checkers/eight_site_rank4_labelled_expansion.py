"""Expand the 36 C8 rank-four cyclic orbits to 288 labelled occurrences.

This packet transports only source labels, normal arrangements, circuit data,
and regulator chambers.  It deliberately does not manufacture a physical
current or a sewn Cech differential.
"""

import importlib.util
import copy
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WALLS = ROOT / "results" / "eight-site-rank4-base-reduced-walls.json"
INVENTORY = ROOT / "results" / "eight-site-full-source-inventory.json"
TARGET = ROOT / "results" / "eight-site-rank4-labelled-expansion.json"
AUDITOR = Path(__file__).with_name("eight_site_rank4_regulator_normals.py")
N = 8


def load_auditor():
    spec = importlib.util.spec_from_file_location("rank4_regulator_normals", AUDITOR)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def rotate_index(index: int, shift: int) -> int:
    return ((index - 1 + shift) % N) + 1


def rotate_label(label: str, shift: int) -> str:
    if label.startswith("g_"):
        sites = sorted(rotate_index(int(character), shift) for character in label[2:])
        return "g_" + "".join(str(site) for site in sites)
    if label.startswith("G_minus_e"):
        edge = label.removeprefix("G_minus_e")
        left, right = int(edge[0]), int(edge[1])
        return f"G_minus_e{rotate_index(left, shift)}{rotate_index(right, shift)}"
    raise ValueError(f"unsupported label: {label}")


def rotate_vector(values: list, shift: int) -> list:
    result = [None] * N
    for index, value in enumerate(values):
        result[(index + shift) % N] = value
    return result


def rotate_packet(base: dict, shift: int) -> dict:
    packet = copy.deepcopy(base)
    packet["labels"] = [rotate_label(label, shift) for label in base["labels"]]
    packet["canonical_key"] = "|".join(sorted(packet["labels"]))
    packet["independent_labels"] = [rotate_label(label, shift) for label in base["independent_labels"]]
    packet["pivot_y_edges"] = [rotate_index(edge, shift) for edge in base["pivot_y_edges"]]
    packet["y_normal_matrix"] = [rotate_vector(row, shift) for row in base["y_normal_matrix"]]
    packet["x_coefficient_matrix"] = [rotate_vector(row, shift) for row in base["x_coefficient_matrix"]]
    packet["source_regulator_matrix"] = [
        rotate_vector(row[:N], shift) + rotate_vector(row[N:], shift)
        for row in base["source_regulator_matrix"]
    ]
    for circuit in packet["labelled_circuits"]:
        circuit["support_labels"] = [rotate_label(label, shift) for label in circuit["support_labels"]]
        circuit["external_regulator_offset_coefficients"] = rotate_vector(
            circuit["external_regulator_offset_coefficients"], shift
        )
        witnesses = circuit.get("opposite_sign_witnesses")
        if witnesses:
            witnesses["positive_offset_epsilon_X"] = rotate_vector(
                witnesses["positive_offset_epsilon_X"], shift
            )
            witnesses["negative_offset_epsilon_X"] = rotate_vector(
                witnesses["negative_offset_epsilon_X"], shift
            )
    for chamber in packet["feasible_joint_circuit_chambers"]:
        chamber["rational_witness"] = rotate_vector(chamber["rational_witness"], shift)
    return packet


def main() -> None:
    auditor = load_auditor()
    wall_records = json.loads(WALLS.read_text())["records"]
    inventory = json.loads(INVENTORY.read_text())["all_orbits"]
    inventory_by_key = {record["canonical_key"]: record for record in inventory}
    occurrences = []
    orbit_summaries = []

    for orbit_index, wall in enumerate(wall_records):
        key = wall["canonical_key"]
        source = inventory_by_key[key]
        assert source["orbit_size"] == 8
        assert source["stabilizer_order"] == 1
        assert source["enumerated_source_multiplicity"] == 8
        orbit_occurrences = []
        labels = key.split("|")
        base_packet = auditor.audit(wall)
        for shift in range(N):
            rotated_labels = sorted(rotate_label(label, shift) for label in labels)
            occurrence_key = "|".join(rotated_labels)
            packet = rotate_packet(base_packet, shift)
            assert packet["canonical_key"] == occurrence_key
            occurrence_id = f"orbit-{orbit_index:02d}-rotation-{shift}"
            packet.update({
                "occurrence_id": occurrence_id,
                "source_orbit_key": key,
                "cyclic_shift": shift,
                "source_orbit_size": source["orbit_size"],
                "source_stabilizer_order": source["stabilizer_order"],
            })
            occurrences.append(packet)
            orbit_occurrences.append(occurrence_id)
        orbit_summaries.append({
            "source_orbit_key": key,
            "reduced_pattern": wall["reduced_pattern"],
            "orbit_size": source["orbit_size"],
            "stabilizer_order": source["stabilizer_order"],
            "enumerated_source_multiplicity": source["enumerated_source_multiplicity"],
            "occurrence_ids": orbit_occurrences,
        })

    occurrence_keys = [item["canonical_key"] for item in occurrences]
    orientation_counts = {}
    chamber_count_distribution = {}
    circuit_count_distribution = {}
    for item in occurrences:
        key = str(item["pivot_orientation"])
        orientation_counts[key] = orientation_counts.get(key, 0) + 1
        chambers = str(item["feasible_joint_circuit_chamber_count"])
        chamber_count_distribution[chambers] = chamber_count_distribution.get(chambers, 0) + 1
        circuits = str(len(item["labelled_circuits"]))
        circuit_count_distribution[circuits] = circuit_count_distribution.get(circuits, 0) + 1

    checks = {
        "cyclic_orbit_count": len(orbit_summaries),
        "labelled_occurrence_count": len(occurrences),
        "unique_labelled_occurrence_count": len(set(occurrence_keys)),
        "all_orbits_free_size_eight": all(
            item["orbit_size"] == 8 and item["stabilizer_order"] == 1
            for item in orbit_summaries
        ),
        "all_normal_ranks_four": all(item["rank_y_normals"] == 4 for item in occurrences),
        "circuit_count_distribution": circuit_count_distribution,
        "feasible_chamber_count_distribution": chamber_count_distribution,
        "pivot_orientation_counts": orientation_counts,
    }
    assert checks["cyclic_orbit_count"] == 36
    assert checks["labelled_occurrence_count"] == 288
    assert checks["unique_labelled_occurrence_count"] == 288
    assert checks["all_orbits_free_size_eight"]
    assert checks["all_normal_ranks_four"]

    output = {
        "schema": "marici.eight_site_rank4_labelled_expansion.v1",
        "scope": {
            "included": "source-labelled cyclic expansion, exact normal/circuit data, positive-regulator chambers",
            "excluded": "physical-current map and sewn Cech differential",
        },
        "checks": checks,
        "orbits": orbit_summaries,
        "occurrences": occurrences,
    }
    TARGET.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(checks, sort_keys=True))


if __name__ == "__main__":
    main()
