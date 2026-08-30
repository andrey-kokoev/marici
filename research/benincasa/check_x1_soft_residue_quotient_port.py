"""The b=0 residue port identifies the X1-soft rank-four quotient."""

import json
from itertools import product

import check_rank26_tangent_support_algebra as algebra

base = algebra.base


def wall_presentation(ambient=14, cutoff=6):
    # At X1=0, point (0,3,5), b=0:
    # K=-1024 a^2+128000.  q_g1=-8 is a unit and is removed.
    # The retained marked walls are a-5, a+5, and a-3.
    p = base.PRIME
    k = {2: (-1024) % p, 0: 128000 % p}
    q = [
        {1: 1, 0: -5 % p},
        {1: 1, 0: 5 % p},
        {1: 1, 0: -3 % p},
    ]
    gamma, k_depth, q_depth = 5, 2, 2
    low_labels = [
        (0, *levels, degree)
        for levels in product(range(1, 2), repeat=3)
        for degree in range(cutoff + 1)
    ]
    low_set = set(low_labels)
    ordered = list(low_labels)
    for k_pole in range(k_depth + 1):
        for levels in product(range(1, q_depth + 1), repeat=3):
            for degree in range(ambient + 5):
                label = (k_pole, *levels, degree)
                if label not in low_set:
                    ordered.append(label)
    columns = {label: index for index, label in enumerate(ordered)}
    pivots = {}

    kd = {degree - 1: degree * coefficient % p
          for degree, coefficient in k.items() if degree}
    qd = [
        {degree - 1: degree * coefficient % p
         for degree, coefficient in polynomial.items() if degree}
        for polynomial in q
    ]

    for k_pole in range(k_depth):
        for levels in product(range(1, q_depth + 1), repeat=3):
            if any(level == q_depth for level in levels):
                continue
            for degree in range(ambient + 1):
                row = {}
                if degree:
                    base.add_value(row, columns[(k_pole, *levels, degree - 1)], degree)
                for shift, coefficient in kd.items():
                    base.add_value(
                        row, columns[(k_pole + 1, *levels, degree + shift)],
                        (gamma - k_pole) * coefficient,
                    )
                for index, level in enumerate(levels):
                    raised = list(levels)
                    raised[index] += 1
                    for shift, coefficient in qd[index].items():
                        base.add_value(
                            row, columns[(k_pole, *raised, degree + shift)],
                            -level * coefficient,
                        )
                base.add_pivot(row, pivots)

    for k_pole in range(k_depth):
        for levels in product(range(1, q_depth + 1), repeat=3):
            for degree in range(ambient - 1):
                row = {columns[(k_pole, *levels, degree)]: 1}
                for shift, coefficient in k.items():
                    base.add_value(
                        row, columns[(k_pole + 1, *levels, degree + shift)],
                        -coefficient,
                    )
                base.add_pivot(row, pivots)

    for index, polynomial in enumerate(q):
        for k_pole in range(k_depth + 1):
            for levels in product(range(1, q_depth + 1), repeat=3):
                if levels[index] == q_depth:
                    continue
                raised = list(levels)
                raised[index] += 1
                for degree in range(ambient):
                    row = {columns[(k_pole, *levels, degree)]: 1}
                    for shift, coefficient in polynomial.items():
                        base.add_value(
                            row, columns[(k_pole, *raised, degree + shift)],
                            -coefficient,
                        )
                    base.add_pivot(row, pivots)
    return {"ordered": ordered, "columns": columns, "pivots": pivots}


def reduce_wall_polynomial(polynomial, wall):
    row = {}
    for degree, coefficient in polynomial.items():
        base.add_value(row, wall["columns"][(0, 1, 1, 1, degree)], coefficient)
    return base.reduce_row(row, wall["pivots"])


def residue_polynomial(vector, presentation):
    polynomial = {}
    unsupported = []
    for column, coefficient in vector.items():
        label = presentation["ordered_columns"][column]
        k_pole, *rest = label
        exponent = rest.pop()
        levels = rest
        if k_pole != 0 or any(level != 1 for level in levels):
            unsupported.append(label)
            continue
        # Res_b=0 P(a,b) da db / (b * other walls) keeps P(a,0) da.
        if exponent[1] == 0:
            base.add_value(polynomial, exponent[0], coefficient)
    return polynomial, unsupported


def main():
    point = (0, 3, 5)
    tangents = ((0, 1, 0), (0, 0, 1))
    _, presentation, deleted_image, tangent_span = algebra.case_algebra(
        ("X1_soft", (point, tangents), True)
    )

    quotient = {}
    for vector in tangent_span.values():
        base.add_pivot(base.reduce_row(vector, deleted_image), quotient)

    residue_span = {}
    unsupported_count = 0
    quotient_residue_rows = []
    wall = wall_presentation()
    cohomological_residue_span = {}
    for vector in quotient.values():
        residue, unsupported = residue_polynomial(vector, presentation)
        unsupported_count += len(unsupported)
        quotient_residue_rows.append(residue)
        base.add_pivot(dict(residue), residue_span)
        base.add_pivot(reduce_wall_polynomial(residue, wall), cohomological_residue_span)

    result = {
        "schema": "marici.benincasa.x1-soft-residue-quotient-port.v1",
        "field": base.PRIME,
        "point": list(point),
        "soft_wall": "q_g23=b=0",
        "tangent_module_rank": len(tangent_span),
        "deleted_kernel_rank": len(deleted_image),
        "quotient_rank": len(quotient),
        "residue_image_rank": len(residue_span),
        "wall_cohomology_residue_rank": len(cohomological_residue_span),
        "unsupported_term_count": unsupported_count,
        "quotient_pivot_labels": [
            presentation["ordered_columns"][pivot]
            for pivot in sorted(quotient, reverse=True)
        ],
        "residue_polynomial_rows": quotient_residue_rows,
        "kernel_equals_deleted_image": (
            len(tangent_span) - len(residue_span) == len(deleted_image)
            and len(quotient) == len(residue_span) == len(cohomological_residue_span)
            and unsupported_count == 0
        ),
    }
    assert result["kernel_equals_deleted_image"]
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
