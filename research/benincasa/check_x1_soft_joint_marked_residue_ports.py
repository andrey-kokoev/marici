"""Joint cohomological marked-residue observer on the X1-soft deletion image."""

import json
from itertools import product
from math import comb

import check_rank26_tangent_support_algebra as algebra

base = algebra.base
P = base.PRIME


def poly_add(target, source, scale=1):
    for degree, coefficient in source.items():
        value = (target.get(degree, 0) + scale * coefficient) % P
        if value:
            target[degree] = value
        else:
            target.pop(degree, None)


def poly_mul(left, right):
    result = {}
    for i, x in left.items():
        for j, y in right.items():
            poly_add(result, {i + j: x * y})
    return result


def affine_power(linear, constant, power):
    return {
        degree: comb(power, degree) * pow(linear, degree, P)
        * pow(constant, power - degree, P) % P
        for degree in range(power + 1)
    }


def substitute(polynomial, substitution):
    # substitution=((a_linear,a_constant),(b_linear,b_constant)).
    result = {}
    for (i, j), coefficient in polynomial.items():
        term = poly_mul(
            affine_power(*substitution[0], i),
            affine_power(*substitution[1], j),
        )
        poly_add(result, term, coefficient)
    return result


def univariate_presentation(k, q, ambient=14, cutoff=6):
    gamma, k_depth, q_depth = 5, 2, 2
    q_count = len(q)
    low_labels = [
        (0, *levels, degree)
        for levels in product(range(1, 2), repeat=q_count)
        for degree in range(cutoff + 1)
    ]
    low_set = set(low_labels)
    ordered = list(low_labels)
    for k_pole in range(k_depth + 1):
        for levels in product(range(1, q_depth + 1), repeat=q_count):
            for degree in range(ambient + 5):
                label = (k_pole, *levels, degree)
                if label not in low_set:
                    ordered.append(label)
    columns = {label: index for index, label in enumerate(ordered)}
    pivots = {}
    kd = {degree - 1: degree * coefficient % P
          for degree, coefficient in k.items() if degree}
    qd = [
        {degree - 1: degree * coefficient % P
         for degree, coefficient in polynomial.items() if degree}
        for polynomial in q
    ]

    for k_pole in range(k_depth):
        for levels in product(range(1, q_depth + 1), repeat=q_count):
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

    k_degree = max(k)
    for k_pole in range(k_depth):
        for levels in product(range(1, q_depth + 1), repeat=q_count):
            for degree in range(ambient - k_degree + 1):
                row = {columns[(k_pole, *levels, degree)]: 1}
                for shift, coefficient in k.items():
                    base.add_value(
                        row, columns[(k_pole + 1, *levels, degree + shift)],
                        -coefficient,
                    )
                base.add_pivot(row, pivots)

    for index, polynomial in enumerate(q):
        q_degree = max(polynomial)
        for k_pole in range(k_depth + 1):
            for levels in product(range(1, q_depth + 1), repeat=q_count):
                if levels[index] == q_depth:
                    continue
                raised = list(levels)
                raised[index] += 1
                for degree in range(ambient - q_degree + 1):
                    row = {columns[(k_pole, *levels, degree)]: 1}
                    for shift, coefficient in polynomial.items():
                        base.add_value(
                            row, columns[(k_pole, *raised, degree + shift)],
                            -coefficient,
                        )
                    base.add_pivot(row, pivots)
    return {"ordered": ordered, "columns": columns, "pivots": pivots,
            "q_count": q_count}


def reduce_polynomial(polynomial, target):
    levels = (1,) * target["q_count"]
    row = {}
    for degree, coefficient in polynomial.items():
        base.add_value(row, target["columns"][(0, *levels, degree)], coefficient)
    return base.reduce_row(row, target["pivots"])


WALLS = {
    "g1": ((1, 0), (0, 8)),       # b=8, t=a
    "g2": ((0, 5), (1, 0)),       # a=5, t=b
    "g3": ((1, 0), (-1, -5)),     # a=t, b=-t-5
    "g23": ((1, 0), (0, 0)),      # b=0, t=a
    "g31": ((0, 3), (1, 0)),      # a=3, t=b
}


def main():
    point = (0, 3, 5)
    tangents = ((0, 1, 0), (0, 0, 1))
    _, presentation, deleted_image, _ = algebra.case_algebra(
        ("X1_soft", (point, tangents), True)
    )
    k, all_q = base.fiber_data(*point)
    names = list(algebra.support.cyclic.charts.SOURCE_NAMES)

    targets = {}
    constant_units = {}
    for wall_name, substitution in WALLS.items():
        restricted_k = substitute(k, substitution)
        retained = []
        units = {}
        for name in names:
            if name == wall_name:
                continue
            restricted = substitute(all_q[name], substitution)
            if set(restricted) <= {0}:
                units[name] = restricted.get(0, 0)
            else:
                retained.append(restricted)
        assert all(value % P for value in units.values())
        targets[wall_name] = univariate_presentation(restricted_k, retained)
        constant_units[wall_name] = units

    offsets, total_width = {}, 0
    for name, target in targets.items():
        offsets[name] = total_width
        total_width += len(target["ordered"])

    invariant_pivots = sorted(deleted_image, reverse=True)
    invariant_basis = [deleted_image[pivot] for pivot in invariant_pivots]
    joint_rows = []
    wall_rows = {name: [] for name in WALLS}
    port_spans = {name: {} for name in WALLS}
    unsupported = 0
    for vector in invariant_basis:
        joined = {}
        for wall_name, substitution in WALLS.items():
            numerator = {}
            for column, coefficient in vector.items():
                label = presentation["ordered_columns"][column]
                k_pole, *rest = label
                exponent = rest.pop()
                levels = rest
                if k_pole != 0 or any(level != 1 for level in levels):
                    unsupported += 1
                    continue
                poly_add(numerator, substitute({exponent: coefficient}, substitution))
            reduced = reduce_polynomial(numerator, targets[wall_name])
            wall_rows[wall_name].append(dict(reduced))
            base.add_pivot(dict(reduced), port_spans[wall_name])
            offset = offsets[wall_name]
            for column, coefficient in reduced.items():
                base.add_value(joined, offset + column, coefficient)
        joint_rows.append(joined)

    joint_span = {}
    for row in joint_rows:
        base.add_pivot(dict(row), joint_span)

    # Restrict both tangent connection matrices to the deletion basis.
    invariant_position = {pivot: index for index, pivot in enumerate(invariant_pivots)}

    def invariant_coordinates(vector):
        row = dict(vector)
        coordinates = [0] * len(invariant_basis)
        while row:
            active = [column for column in row if column in deleted_image]
            if not active:
                raise AssertionError(f"tangent image escaped deletion module: {sorted(row)[:8]}")
            pivot = max(active)
            coefficient = row[pivot]
            coordinates[invariant_position[pivot]] = coefficient
            for column, value in deleted_image[pivot].items():
                base.add_value(row, column, -coefficient * value)
        return coordinates

    tangent_matrices = []
    for tangent in tangents:
        matrix = [[0] * len(invariant_basis) for _ in invariant_basis]
        for source_index, vector in enumerate(invariant_basis):
            image = algebra.support.linear_image(presentation, vector, tangent)
            for target_index, value in enumerate(invariant_coordinates(image)):
                matrix[target_index][source_index] = value
        tangent_matrices.append(matrix)

    def score_closure(observer_rows):
        observed_coordinates = sorted({column for row in observer_rows for column in row})
        initial_covectors = [
            {index: observer_rows[index].get(column, 0)
             for index in range(len(invariant_basis))
             if observer_rows[index].get(column, 0)}
            for column in observed_coordinates
        ]
        score_span, frontier = {}, [(row, 0) for row in initial_covectors if row]
        cumulative_by_depth = {}
        while frontier:
            covector, depth = frontier.pop(0)
            before = len(score_span)
            base.add_pivot(dict(covector), score_span)
            if len(score_span) == before:
                continue
            cumulative_by_depth[depth] = len(score_span)
            dense = [covector.get(index, 0) for index in range(len(invariant_basis))]
            for matrix in tangent_matrices:
                image = {
                    column: sum(dense[row] * matrix[row][column]
                                for row in range(len(invariant_basis))) % P
                    for column in range(len(invariant_basis))
                }
                image = {column: value for column, value in image.items() if value}
                if image:
                    frontier.append((image, depth + 1))
        return score_span, cumulative_by_depth

    score_span, cumulative_by_depth = score_closure(joint_rows)
    per_port_score = {}
    for name, rows in wall_rows.items():
        span, cumulative = score_closure(rows)
        per_port_score[name] = {
            "closure_rank": len(span),
            "cumulative_rank_by_depth": cumulative,
        }
    result = {
        "schema": "marici.benincasa.x1-soft-joint-marked-residue-ports.v1",
        "field": P,
        "point": list(point),
        "deleted_module_rank": len(deleted_image),
        "individual_port_ranks": {
            name: len(span) for name, span in port_spans.items()
        },
        "joint_port_rank": len(joint_span),
        "score_closure_rank_on_deleted_module": len(score_span),
        "score_cumulative_rank_by_depth": cumulative_by_depth,
        "individual_port_score_closures": per_port_score,
        "unsupported_term_count": unsupported,
        "constant_wall_units": constant_units,
        "joint_faithfulness": len(joint_span) == len(deleted_image) and unsupported == 0,
        "score_completed_faithfulness": (
            len(score_span) == len(deleted_image) and unsupported == 0
        ),
    }
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
