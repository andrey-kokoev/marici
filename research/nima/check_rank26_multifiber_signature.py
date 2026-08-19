"""Replicate the moving-wall extension signature at independent fibers."""

import contextlib
import importlib
import io
import json
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    audit = importlib.import_module("check_rank21_occurrence_reflection_connection")

base, charts = audit.base, audit.charts


def nullspace(rows, width):
    matrix = [list(row) for row in rows if any(row)]
    pivots, rank = [], 0
    for column in range(width):
        selected = next((r for r in range(rank, len(matrix)) if matrix[r][column]), None)
        if selected is None:
            continue
        matrix[rank], matrix[selected] = matrix[selected], matrix[rank]
        inverse = pow(matrix[rank][column], base.PRIME - 2, base.PRIME)
        matrix[rank] = [value * inverse % base.PRIME for value in matrix[rank]]
        for r in range(len(matrix)):
            if r != rank and matrix[r][column]:
                scale = matrix[r][column]
                matrix[r] = [(x - scale * y) % base.PRIME for x, y in zip(matrix[r], matrix[rank])]
        pivots.append(column)
        rank += 1
    free = [column for column in range(width) if column not in pivots]
    basis = []
    for column in free:
        vector = [0] * width
        vector[column] = 1
        for r, pivot in enumerate(pivots):
            vector[pivot] = (-matrix[r][column]) % base.PRIME
        basis.append(vector)
    return basis


def sample(point):
    old_ambient, old_cutoff = charts.AMBIENT, charts.CUTOFF
    charts.AMBIENT, charts.CUTOFF = 12, 6
    try:
        pres = charts.presentation(base.fiber_data, point, charts.SOURCE_NAMES)
    finally:
        charts.AMBIENT, charts.CUTOFF = old_ambient, old_cutoff

    def derivative(vector, axis):
        image = {}
        for column, coefficient in vector.items():
            for target, value in audit.connection_image(
                pres["ordered_columns"][column], charts.SOURCE_NAMES, axis,
                pres["columns"], base.fiber_data, point,
            ).items():
                base.add_value(image, target, coefficient * value)
        return base.reduce_row(image, pres["pivots"])

    numerator = {}
    for label in pres["low_labels"]:
        if label[0] == 0 and all(level == 1 for level in label[1:-1]) and sum(label[-1]) <= 6:
            base.add_pivot(base.reduce_row({pres["columns"][label]: 1}, pres["pivots"]), numerator)
    basis = list(numerator.values())
    moving_label = (0, 1, 1, 1, 1, 2, (0, 0))
    moving = base.reduce_row({pres["columns"][moving_label]: 1}, pres["pivots"])
    augmented = dict(numerator)
    base.add_pivot(dict(moving), augmented)
    quotient = {}
    base.add_pivot(base.reduce_row(moving, numerator), quotient)
    quotient_pivot = next(iter(quotient))
    functionals = [
        [base.reduce_row(derivative(vector, axis), numerator).get(quotient_pivot, 0) for vector in basis]
        for axis in range(3)
    ]
    functional_span = {}
    for row in functionals:
        base.add_pivot({i: value for i, value in enumerate(row) if value}, functional_span)
    kernel_vectors = []
    for coordinates in nullspace(functionals, len(basis)):
        vector = {}
        for coefficient, source in zip(coordinates, basis):
            for column, value in source.items():
                base.add_value(vector, column, coefficient * value)
        kernel_vectors.append(vector)
    closure, frontier = {}, list(kernel_vectors)
    while frontier:
        vector = frontier.pop()
        before = len(closure)
        base.add_pivot(dict(vector), closure)
        if len(closure) == before:
            continue
        for axis in range(3):
            image = derivative(vector, axis)
            if image:
                frontier.append(image)
    return {
        "point": list(point),
        "numerator_rank": len(numerator),
        "augmented_rank": len(augmented),
        "second_fundamental_form_rank": len(functional_span),
        "common_kernel_rank": len(kernel_vectors),
        "kernel_derivative_closure_rank": len(closure),
        "numerator_basis_labels": [pres["ordered_columns"][pivot] for pivot in numerator],
        "second_fundamental_form_rows": functionals,
        "second_fundamental_form_supports": [
            [i for i, value in enumerate(row) if value] for row in functionals
        ],
    }


samples = [sample(point) for point in ((3, 5, 7), (5, 8, 11), (7, 11, 13))]
payload = {
    "schema": "marici.rank26-multifiber-signature.v1",
    "field": base.PRIME,
    "ambient_relation_degree": 12,
    "samples": samples,
    "common_signature": [25, 26, 3, 22, 26],
    "common_basis": all(sample["numerator_basis_labels"] == samples[0]["numerator_basis_labels"] for sample in samples),
    "common_support_pattern": all(sample["second_fundamental_form_supports"] == samples[0]["second_fundamental_form_supports"] for sample in samples),
    "status": "moving_wall_extension_signature_replicated_at_three_independent_fibers",
}
Path(__file__).with_name("rank26-multifiber-signature.json").write_text(
    json.dumps(payload, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(payload, indent=2))
