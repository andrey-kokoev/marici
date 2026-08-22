"""Audit the source typing of the first-jet graph-principal filler.

This checker distinguishes source subspaces before applying Theta.  It tests
whether the raw free-row parity block and the supported graph-kernel block are
actually the same object, rather than merely having the same Theta image.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "benincasa"))
import physical_four_mark_residue_twisted_derham as m

AMBIENT = int(os.environ.get("MARICI_AMBIENT_DEGREE", "12"))
CUTOFF = int(os.environ.get("MARICI_CUTOFF_DEGREE", "6"))
P = m.PRIME
GAMMA = (P - 1) // 2
RESULTS = ROOT / "research" / "nima" / "results"
OUT = RESULTS / f"physical_theta_graph_typing_audit_p{P}_a{AMBIENT}_c{CUTOFF}.json"
SIMPLE_MONOMIALS = ((1, 1), (1, 0), (0, 1), (0, 0), (2, 0), (0, 2))
JET_MULTIPLIERS = ((0, 0), (1, 0), (0, 1))


def add_scaled(target, source, scalar=1):
    for column, value in source.items():
        m.add_value(target, column, scalar * value)


def rank(rows):
    pivots = {}
    for row in rows:
        m.add_pivot(dict(row), pivots)
    return len(pivots)


def apply_rows(vector, rows):
    result = {}
    for source, coefficient in vector.items():
        add_scaled(result, rows[source], coefficient)
    return result


def main():
    _, columns, quotient_pivots, free = m.presentation(
        (), GAMMA, AMBIENT, CUTOFF, minimum_q_level=0
    )
    labels = {column: label for label, column in columns.items()}
    assert len(free) == 9

    normal_path = RESULTS / (
        f"physical_half_twist_normal_jet_defect_p{P}_a{AMBIENT}_c{CUTOFF}.json"
    )
    normal = json.loads(normal_path.read_text(encoding="utf-8"))
    assert normal["passed"] and normal["kernel_is_graph_of_jet_to_simple_reduction"]

    simple_vectors = [
        m.quotient_coordinates((0, monomial), columns, quotient_pivots, free)
        for monomial in SIMPLE_MONOMIALS
    ]
    k1 = {(2, 0): 198, (0, 2): 378, (0, 0): -47520}
    jet_vectors = []
    for multiplier in JET_MULTIPLIERS:
        vector = {}
        for exponent, coefficient in k1.items():
            monomial = (exponent[0] + multiplier[0], exponent[1] + multiplier[1])
            add_scaled(
                vector,
                m.quotient_coordinates((1, monomial), columns, quotient_pivots, free),
                coefficient,
            )
        jet_vectors.append(vector)

    reductions = [
        {int(index): int(value) for index, value in row.items()}
        for row in normal["jet_to_simple_reduction_matrix"]
    ]
    graph_vectors = []
    for jet, reduction in zip(jet_vectors, reductions):
        graph = dict(jet)
        for simple_index, coefficient in reduction.items():
            add_scaled(graph, simple_vectors[simple_index], -coefficient)
        graph_vectors.append(graph)

    kernel_vectors = []
    label_to_free = {labels[column]: column for column in free}
    for relation in normal["kernel_representatives"]:
        kernel_vectors.append({
            label_to_free[(item["label"][0], tuple(item["label"][1]))]: item["coefficient"]
            for item in relation
        })
    assert rank(graph_vectors) == rank(kernel_vectors) == rank(graph_vectors + kernel_vectors) == 3

    # The raw rows carrying Theta are the seventh and ninth free rows.  Their
    # common parity is a property of this raw quotient basis, not of the graph
    # relations obtained after subtracting their simple reductions.
    raw_p02 = [{free[index]: 1} for index in (6, 8)]
    graph_p02 = [graph_vectors[index] for index in (0, 2)]
    combined_rank = rank(raw_p02 + graph_p02)

    parity_support = []
    for graph in graph_p02:
        parity_support.append(sorted({
            tuple(power % 2 for power in labels[column][-1]) for column in graph
        }))

    theta_images = []
    for axis in (0, 1):
        axis_path = RESULTS / (
            f"physical_moving_localization_horizontality_p{P}_a{AMBIENT}_"
            f"c{CUTOFF}_axes{axis}.json"
        )
        axis_packet = json.loads(axis_path.read_text(encoding="utf-8"))["axes"][0]
        rows = [
            {int(column): int(value) for column, value in row.items()}
            for row in axis_packet["mixed_curvature_rows"]
        ]
        # rows are ordered by free basis rather than by ambient column id.
        raw_index_vectors = [{6: 1}, {8: 1}]
        free_to_index = {column: index for index, column in enumerate(free)}
        simple_index_vectors = [
            {free_to_index[column]: value for column, value in vector.items()}
            for vector in simple_vectors
        ]
        jet_index_vectors = [
            {free_to_index[column]: value for column, value in vector.items()}
            for vector in jet_vectors
        ]
        graph_index_vectors = [
            {free_to_index[column]: value for column, value in graph.items()}
            for graph in graph_vectors
        ]
        raw_images = [apply_rows(vector, rows) for vector in raw_index_vectors]
        simple_images = [apply_rows(vector, rows) for vector in simple_index_vectors]
        jet_images = [apply_rows(vector, rows) for vector in jet_index_vectors]
        graph_images_all = [apply_rows(vector, rows) for vector in graph_index_vectors]
        graph_images_p02 = [graph_images_all[index] for index in (0, 2)]
        factorization_residuals = list(simple_images)
        for jet_image, graph_image in zip(jet_images, graph_images_all):
            residual = dict(jet_image)
            add_scaled(residual, graph_image, -1)
            factorization_residuals.append(residual)
        theta_images.append({
            "axis": axis,
            "raw_images": raw_images,
            "graph_images_all": graph_images_all,
            "graph_images_p02": graph_images_p02,
            "graph_boundary_rank": rank(graph_images_all),
            "equation58_simple_image_rank": rank(simple_images),
            "theta_equals_graph_boundary_times_projection": not any(factorization_residuals),
            "graph_projection_factorization_residual_rank": rank(factorization_residuals),
            "graph_projection_factorization_residuals": factorization_residuals,
            "graph_nonzero_generator_indices": [
                index for index, image in enumerate(graph_images_all) if image
            ],
            "raw_and_graph_p02_images_agree_labelwise": raw_images == graph_images_p02,
        })

    packet = {
        "schema": "marici.physical-theta-graph-typing-audit.v1",
        "prime": P,
        "ambient": AMBIENT,
        "cutoff": CUTOFF,
        "raw_parity_block_rank": rank(raw_p02),
        "supported_graph_block_rank": rank(graph_p02),
        "combined_rank": combined_rank,
        "intersection_dimension": 4 - combined_rank,
        "raw_and_graph_blocks_are_equal": combined_rank == 2,
        "supported_graph_block_is_in_localization_kernel": (
            rank(graph_vectors + kernel_vectors) == 3
        ),
        "graph_generator_parity_supports": parity_support,
        "graph_block_is_single_parity_eigenspace": all(len(support) == 1 for support in parity_support),
        "theta_image_comparison": theta_images,
        "prior_rowwise_graph_identification_fails": (
            combined_rank > 2
            and all(not item["raw_and_graph_p02_images_agree_labelwise"] for item in theta_images)
        ),
        "prior_graph_factorization_fails": all(
            not item["theta_equals_graph_boundary_times_projection"]
            for item in theta_images
        ),
        "corrected_smallest_predeclared_supported_cell": "full graph kernel J_3",
        "p02_disposition": (
            "invalid as previously certified: raw parity rows and literal graph generators were conflated"
        ),
        "scope": "finite-field finite-cutoff source-typing audit",
    }
    packet["passed"] = (
        packet["supported_graph_block_is_in_localization_kernel"]
        and not packet["raw_and_graph_blocks_are_equal"]
        and not packet["graph_block_is_single_parity_eigenspace"]
        and packet["prior_rowwise_graph_identification_fails"]
        and packet["prior_graph_factorization_fails"]
    )
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    if not packet["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
