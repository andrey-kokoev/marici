"""Factor the physical half-twist connection defect through the killed kernel."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "benincasa"))
import physical_four_mark_residue_twisted_derham as m

NAMES = ("g1", "g2", "g3", "g23", "g31")
GAMMA = (m.PRIME - 1) // 2
AMBIENT = int(os.environ.get("MARICI_AMBIENT_DEGREE", "10"))
CUTOFF = int(os.environ.get("MARICI_CUTOFF_DEGREE", "5"))
OUT = (
    Path(__file__).resolve().parents[1]
    / "results"
    / f"physical_half_twist_normal_jet_defect_p{m.PRIME}_a{AMBIENT}_c{CUTOFF}.json"
)


def add_scaled(target, vector, scale=1):
    for column, value in vector.items():
        m.add_value(target, column, scale * value)


def normalized(row):
    if not row:
        return row
    pivot = max(row)
    inverse = pow(row[pivot], m.PRIME - 2, m.PRIME)
    return {column: value * inverse % m.PRIME for column, value in row.items()}


def main() -> None:
    a_low, a_columns, a_pivots, a_free = m.presentation((), GAMMA, AMBIENT, CUTOFF, minimum_q_level=0)
    c_low, c_columns, c_pivots, c_free = m.presentation(NAMES, GAMMA, AMBIENT, CUTOFF, minimum_q_level=0)
    a_label = {column: label for label, column in a_columns.items()}
    c_label = {column: label for label, column in c_columns.items()}

    def embedded_label(label):
        k_pole, monomial = label
        return (k_pole, 0, 0, 0, 0, 0, monomial)

    def common_quotient(vector):
        reduced = m.reduce_row(vector, c_pivots)
        return {column: reduced[column] for column in c_free if column in reduced}

    images = {}
    for column in a_free:
        images[column] = common_quotient({c_columns[embedded_label(a_label[column])]: 1})

    # Row-reduce the map while carrying source combinations.  A zero image
    # leaves a canonical computed kernel representative in absolute coordinates.
    image_pivots = {}
    lift_pivots = {}
    kernel = []
    for source_column in a_free:
        row = dict(images[source_column])
        lift = {source_column: 1}
        while row and max(row) in image_pivots:
            pivot = max(row)
            coefficient = row[pivot]
            add_scaled(row, image_pivots[pivot], -coefficient)
            add_scaled(lift, lift_pivots[pivot], -coefficient)
        if row:
            pivot = max(row)
            inverse = pow(row[pivot], m.PRIME - 2, m.PRIME)
            row = {column: value * inverse % m.PRIME for column, value in row.items()}
            lift = {column: value * inverse % m.PRIME for column, value in lift.items()}
            image_pivots[pivot] = row
            lift_pivots[pivot] = lift
        else:
            kernel.append(normalized(lift))

    def absolute_connection(vector, axis):
        image = {}
        for column, coefficient in vector.items():
            add_scaled(image, m.connection_image(a_label[column], (), GAMMA, axis, a_columns), coefficient)
        reduced = m.reduce_row(image, a_pivots)
        return {column: reduced[column] for column in a_free if column in reduced}

    def common_connection(vector, axis):
        image = {}
        for column, coefficient in vector.items():
            add_scaled(image, m.connection_image(c_label[column], NAMES, GAMMA, axis, c_columns), coefficient)
        return common_quotient(image)

    def map_absolute(vector):
        image = {}
        for column, coefficient in vector.items():
            add_scaled(image, images[column], coefficient)
        return image

    defects = [{}, {}]
    defect_by_source = [{}, {}]
    for source_column in a_free:
        for axis in range(2):
            defect = common_connection(images[source_column], axis)
            add_scaled(defect, map_absolute(absolute_connection({source_column: 1}, axis)), -1)
            defect_by_source[axis][source_column] = defect
            m.add_pivot(dict(defect), defects[axis])

    kernel_defects = [{}, {}]
    for relation in kernel:
        for axis in range(2):
            defect = {}
            for source_column, coefficient in relation.items():
                add_scaled(defect, defect_by_source[axis][source_column], coefficient)
            m.add_pivot(defect, kernel_defects[axis])

    def relation_packet(relation):
        return [
            {"label": a_label[column], "coefficient": coefficient}
            for column, coefficient in sorted(relation.items())
        ]

    parity_keys = ((0, 0), (0, 1), (1, 0), (1, 1))
    parity_packet = {}
    for parity in parity_keys:
        source_columns = [
            column for column in a_free
            if tuple(exponent % 2 for exponent in a_label[column][-1]) == parity
        ]
        parity_image = {}
        parity_defects = [{}, {}]
        for column in source_columns:
            m.add_pivot(dict(images[column]), parity_image)
            for axis in range(2):
                m.add_pivot(dict(defect_by_source[axis][column]), parity_defects[axis])
        parity_packet[str(parity)] = {
            "absolute_dimension": len(source_columns),
            "image_dimension": len(parity_image),
            "kernel_dimension": len(source_columns) - len(parity_image),
            "defect_ranks": [len(span) for span in parity_defects],
        }

    # Literal q-normal equation-(58) numerators at (X1,X2,X3)=(2,3,4):
    # K1 = 198 a^2 + 378 b^2 - 47520.  Overall -1/2 factors do not affect
    # spans.  One additional K pole represents K1/K^(3/2) relative to the
    # K^(-1/2) twist.
    k1 = {(2, 0): 198, (0, 2): 378, (0, 0): -47520}
    jet_multipliers = ((0, 0), (1, 0), (0, 1))
    jet_vectors = []
    jet_span = {}
    jet_common_images = []
    jet_defect_spans = [{}, {}]
    for multiplier in jet_multipliers:
        vector = {}
        for exponent, coefficient in k1.items():
            monomial = (exponent[0] + multiplier[0], exponent[1] + multiplier[1])
            add_scaled(
                vector,
                m.quotient_coordinates((1, monomial), a_columns, a_pivots, a_free),
                coefficient,
            )
        jet_vectors.append(vector)
        m.add_pivot(dict(vector), jet_span)
        jet_common_images.append(map_absolute(vector))
        for axis in range(2):
            defect = {}
            for source_column, coefficient in vector.items():
                add_scaled(defect, defect_by_source[axis][source_column], coefficient)
            m.add_pivot(defect, jet_defect_spans[axis])

    kernel_span = {}
    combined_kernel_jet_span = {}
    for relation in kernel:
        m.add_pivot(dict(relation), kernel_span)
        m.add_pivot(dict(relation), combined_kernel_jet_span)
    for vector in jet_vectors:
        m.add_pivot(dict(vector), combined_kernel_jet_span)

    simple_monomials = ((1, 1), (1, 0), (0, 1), (0, 0), (2, 0), (0, 2))
    simple_vectors = [
        m.quotient_coordinates((0, monomial), a_columns, a_pivots, a_free)
        for monomial in simple_monomials
    ]
    simple_span = {}
    simple_common_span = {}
    jet_common_span = {}
    equation58_span = {}
    for vector in simple_vectors:
        m.add_pivot(dict(vector), simple_span)
        m.add_pivot(map_absolute(vector), simple_common_span)
        m.add_pivot(dict(vector), equation58_span)
    for vector in jet_vectors:
        m.add_pivot(map_absolute(vector), jet_common_span)
        m.add_pivot(dict(vector), equation58_span)
    common_simple_plus_jet = {pivot: dict(row) for pivot, row in simple_common_span.items()}
    for row in jet_common_span.values():
        m.add_pivot(dict(row), common_simple_plus_jet)

    # Express each jet image uniquely in the simple-image basis.  This is the
    # explicit reduction R:J3->S6 whose graph is the localization kernel.
    simple_images = [map_absolute(vector) for vector in simple_vectors]
    coordinate_pivots = {}
    coordinate_lifts = {}
    for index, image in enumerate(simple_images):
        row = dict(image)
        lift = {index: 1}
        while row and max(row) in coordinate_pivots:
            pivot = max(row)
            coefficient = row[pivot]
            add_scaled(row, coordinate_pivots[pivot], -coefficient)
            add_scaled(lift, coordinate_lifts[pivot], -coefficient)
        pivot = max(row)
        inverse = pow(row[pivot], m.PRIME - 2, m.PRIME)
        coordinate_pivots[pivot] = {
            column: value * inverse % m.PRIME for column, value in row.items()
        }
        coordinate_lifts[pivot] = {
            column: value * inverse % m.PRIME for column, value in lift.items()
        }

    def simple_coordinates(target):
        row = dict(target)
        coordinates = {}
        while row:
            pivot = max(row)
            coefficient = row[pivot]
            if pivot not in coordinate_pivots:
                raise RuntimeError("target is outside the simple-period image")
            add_scaled(row, coordinate_pivots[pivot], -coefficient)
            add_scaled(coordinates, coordinate_lifts[pivot], coefficient)
        return coordinates

    jet_reduction_coordinates = [simple_coordinates(map_absolute(vector)) for vector in jet_vectors]
    graph_vectors = []
    graph_defect_spans = [{}, {}]
    graph_defect_packets = [[], []]
    for jet, reduction in zip(jet_vectors, jet_reduction_coordinates):
        graph = dict(jet)
        for simple_index, coefficient in reduction.items():
            add_scaled(graph, simple_vectors[simple_index], -coefficient)
        graph_vectors.append(graph)
        for axis in range(2):
            defect = {}
            for source_column, coefficient in graph.items():
                add_scaled(defect, defect_by_source[axis][source_column], coefficient)
            m.add_pivot(dict(defect), graph_defect_spans[axis])
            graph_defect_packets[axis].append(simple_coordinates(defect))
    graph_span = {}
    graph_plus_kernel = {}
    for graph in graph_vectors:
        m.add_pivot(dict(graph), graph_span)
        m.add_pivot(dict(graph), graph_plus_kernel)
    for relation in kernel:
        m.add_pivot(dict(relation), graph_plus_kernel)

    packet = {
        "schema": "marici.physical-half-twist-normal-jet-defect.v1",
        "prime": m.PRIME,
        "twist_gamma_mod_prime": GAMMA,
        "ambient": AMBIENT,
        "cutoff": CUTOFF,
        "absolute_dimension": len(a_free),
        "localization_image_dimension": len(image_pivots),
        "localization_kernel_dimension": len(kernel),
        "parity_decomposition": parity_packet,
        "kernel_representatives": [relation_packet(relation) for relation in kernel],
        "literal_k1_jet_span_dimension": len(jet_span),
        "literal_k1_jet_common_image_nonzero": [bool(image) for image in jet_common_images],
        "kernel_plus_literal_k1_jet_dimension": len(combined_kernel_jet_span),
        "literal_k1_jet_defect_ranks": [len(span) for span in jet_defect_spans],
        "simple_period_span_dimension": len(simple_span),
        "simple_period_common_image_dimension": len(simple_common_span),
        "equation58_simple_plus_jet_span_dimension": len(equation58_span),
        "jet_common_image_dimension": len(jet_common_span),
        "common_simple_plus_jet_dimension": len(common_simple_plus_jet),
        "jet_to_simple_reduction_matrix": jet_reduction_coordinates,
        "explicit_graph_dimension": len(graph_span),
        "explicit_graph_plus_kernel_dimension": len(graph_plus_kernel),
        "explicit_graph_connection_defect_ranks": [len(span) for span in graph_defect_spans],
        "explicit_graph_connection_defect_in_simple_coordinates": graph_defect_packets,
        "full_connection_defect_ranks": [len(span) for span in defects],
        "kernel_restricted_defect_ranks": [len(span) for span in kernel_defects],
    }
    packet["defect_is_detected_fully_on_killed_kernel"] = (
        packet["localization_kernel_dimension"] == 3
        and packet["full_connection_defect_ranks"] == [3, 3]
        and packet["kernel_restricted_defect_ranks"] == [3, 3]
    )
    packet["literal_k1_jets_equal_localization_kernel"] = (
        packet["literal_k1_jet_span_dimension"] == 3
        and packet["literal_k1_jet_common_image_nonzero"] == [False, False, False]
        and packet["kernel_plus_literal_k1_jet_dimension"] == 3
        and packet["literal_k1_jet_defect_ranks"] == [3, 3]
    )
    packet["kernel_is_graph_of_jet_to_simple_reduction"] = (
        packet["simple_period_span_dimension"] == 6
        and packet["simple_period_common_image_dimension"] == 6
        and packet["literal_k1_jet_span_dimension"] == 3
        and packet["jet_common_image_dimension"] == 3
        and packet["equation58_simple_plus_jet_span_dimension"] == 9
        and packet["common_simple_plus_jet_dimension"] == 6
        and packet["localization_kernel_dimension"] == 3
        and packet["explicit_graph_dimension"] == 3
        and packet["explicit_graph_plus_kernel_dimension"] == 3
        and packet["explicit_graph_connection_defect_ranks"] == [3, 3]
    )
    packet["passed"] = (
        packet["defect_is_detected_fully_on_killed_kernel"]
        and not packet["literal_k1_jets_equal_localization_kernel"]
        and packet["kernel_is_graph_of_jet_to_simple_reduction"]
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    if not packet["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
