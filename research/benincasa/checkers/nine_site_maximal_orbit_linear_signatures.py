"""Uniform exact linear signature census for all 480 maximal C9 source orbits."""

import collections
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "results" / "nine-site-full-source-inventory.json"
CONTOUR = ROOT / "results" / "nine-site-canonical-contour-packet.json"
TARGET = ROOT / "results" / "nine-site-maximal-orbit-linear-signatures.json"
N = 9


def parse_region(label: str) -> set[int] | None:
    if not label.startswith("g_"):
        return None
    return {int(character) - 1 for character in label[2:]}


def wall_row(label: str) -> list[Fraction]:
    x = [Fraction(0) for _ in range(N)]
    y = [Fraction(0) for _ in range(N)]
    region = parse_region(label)
    if region is not None:
        for site in region:
            x[site] = Fraction(1)
        for edge in range(N):
            if (edge in region) != ((edge + 1) % N in region):
                y[edge] = Fraction(1)
    else:
        assert label.startswith("G_minus_e")
        edge = int(label.removeprefix("G_minus_e")[0]) - 1
        x = [Fraction(1) for _ in range(N)]
        y[edge] = Fraction(2)
    return y + x


def rref(rows: list[list[Fraction]], pivot_limit: int) -> tuple[list[list[Fraction]], list[int], int]:
    matrix = [row[:] for row in rows]
    row_index = 0
    pivots = []
    for column in range(pivot_limit):
        pivot = next((index for index in range(row_index, len(matrix)) if matrix[index][column]), None)
        if pivot is None:
            continue
        matrix[row_index], matrix[pivot] = matrix[pivot], matrix[row_index]
        scale = matrix[row_index][column]
        matrix[row_index] = [value / scale for value in matrix[row_index]]
        for target in range(len(matrix)):
            if target == row_index or not matrix[target][column]:
                continue
            factor = matrix[target][column]
            matrix[target] = [left - factor * right for left, right in zip(matrix[target], matrix[row_index])]
        pivots.append(column)
        row_index += 1
    return matrix, pivots, row_index


def rank(rows: list[list[Fraction]]) -> int:
    if not rows:
        return 0
    _, pivots, _ = rref(rows, len(rows[0]))
    return len(pivots)


def rational_vector(values: list[Fraction]) -> list[str]:
    return [str(value) for value in values]


def main() -> None:
    inventory = json.loads(INVENTORY.read_text())
    contour = json.loads(CONTOUR.read_text())
    top = inventory["top_orbits"]
    facets = {item["label"]: item for item in contour["facets"]}
    vertices = contour["vertices"]
    records = []

    for orbit in top:
        labels = [str(value) for value in orbit["representative"]]
        rows = [wall_row(label) for label in labels]
        matrix, pivots, y_rank = rref(rows, N)
        free_edges = [edge for edge in range(N) if edge not in pivots]
        base_relations = [row[N:] for row in matrix[y_rank:] if any(row[N:])]
        base_rank = rank(base_relations)

        face_indices = sorted(set.intersection(*(set(facets[label]["zero_vertex_indices"]) for label in labels)))
        multiplicities = collections.Counter(vertices[index]["edge"] for index in face_indices)
        doubled = sorted(edge for edge, count in multiplicities.items() if count == 2)
        singleton = sorted(edge for edge, count in multiplicities.items() if count == 1)
        higher = sorted((edge, count) for edge, count in multiplicities.items() if count > 2)
        transported_free = [edge + 1 for edge in free_edges]
        visible = doubled == transported_free and not higher

        connected = sorted(label for label in labels if label.startswith("g_"))
        spanning = sorted(label for label in labels if label.startswith("G_minus_e"))
        support_incidence = {
            "connected_region_labels": connected,
            "spanning_subgraph_labels": spanning,
            "connected_region_count": len(connected),
            "spanning_subgraph_count": len(spanning),
            "face_vertex_count": len(face_indices),
            "doubled_face_edges": doubled,
            "singleton_face_edges": singleton,
            "higher_multiplicity_face_edges": higher,
        }
        linear_fold_input_type = {
            "wall_normal_rank": y_rank,
            "free_routing_dimension": len(free_edges),
            "base_relation_rank": base_rank,
            "companion_equation_count": 5 if len(free_edges) == 4 else None,
            "jacobian_shape": [5, 4] if len(free_edges) == 4 else None,
            "fold_rank_type_status": "pending_exact_companion_minors",
        }
        exact_signature = {
            "routing_visibility": visible,
            "linear_fold_input_type": linear_fold_input_type,
            "stabilizer_order": orbit["stabilizer_order"],
            "physical_support_incidence": support_incidence,
        }
        records.append({
            "canonical_key": orbit["canonical_key"],
            "labels": labels,
            "stabilizer_order": orbit["stabilizer_order"],
            "orbit_size": orbit["orbit_size"],
            "enumerated_source_multiplicity": orbit["enumerated_source_multiplicity"],
            "wall_normal_pivot_edges": [edge + 1 for edge in pivots],
            "free_routing_edges": transported_free,
            "base_relations": [rational_vector(row) for row in base_relations],
            "routing_visibility": visible,
            "linear_fold_input_type": linear_fold_input_type,
            "physical_support_incidence": support_incidence,
            "exact_linear_signature": exact_signature,
        })

    encoded = [json.dumps(item["exact_linear_signature"], sort_keys=True, separators=(",", ":")) for item in records]
    counts = collections.Counter(encoded)
    signature_ids = {signature: f"linear-signature-{index:03d}" for index, signature in enumerate(sorted(counts))}
    for record, signature in zip(records, encoded):
        record["linear_signature_id"] = signature_ids[signature]
    partition = [
        {
            "linear_signature_id": signature_ids[signature],
            "count": count,
            "signature": json.loads(signature),
            "canonical_keys": [record["canonical_key"] for record, encoded_signature in zip(records, encoded) if encoded_signature == signature],
        }
        for signature, count in sorted(counts.items(), key=lambda item: signature_ids[item[0]])
    ]
    checks = {
        "maximal_orbit_count": len(records),
        "linear_signature_count": len(partition),
        "wall_normal_rank_distribution": dict(collections.Counter(str(item["linear_fold_input_type"]["wall_normal_rank"]) for item in records)),
        "free_routing_dimension_distribution": dict(collections.Counter(str(item["linear_fold_input_type"]["free_routing_dimension"]) for item in records)),
        "base_relation_rank_distribution": dict(collections.Counter(str(item["linear_fold_input_type"]["base_relation_rank"]) for item in records)),
        "routing_visibility_distribution": dict(collections.Counter(str(item["routing_visibility"]).lower() for item in records)),
        "stabilizer_distribution": dict(collections.Counter(str(item["stabilizer_order"]) for item in records)),
        "all_face_vertex_counts_ten": all(item["physical_support_incidence"]["face_vertex_count"] == 10 for item in records),
        "all_edge_multiplicities_one_or_two": all(not item["physical_support_incidence"]["higher_multiplicity_face_edges"] for item in records),
    }
    assert checks["maximal_orbit_count"] == 480
    packet = {
        "schema": "marici.nine_site_maximal_orbit_linear_signatures.v1",
        "scope": {
            "completed": "uniform exact wall-normal, routing-visibility, stabilizer, and physical-support-incidence census",
            "pending": "exact companion maximal-minor calculation needed to replace linear_fold_input_type with fold rank/type",
        },
        "checks": checks,
        "partition": partition,
        "records": records,
    }
    TARGET.write_text(json.dumps(packet, indent=2) + "\n")
    print(json.dumps(checks, sort_keys=True))


if __name__ == "__main__":
    main()
