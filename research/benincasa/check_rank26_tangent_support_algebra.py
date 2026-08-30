"""Generated tangent-connection algebra on supported source closures."""

import hashlib
import json
from concurrent.futures import ProcessPoolExecutor

import check_rank26_tangent_support_closure as support

base = support.cyclic.base


def multiply(left, right):
    size = len(left)
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for k, value in enumerate(left[i]):
            if value:
                for j, other in enumerate(right[k]):
                    if other:
                        result[i][j] = (result[i][j] + value * other) % base.PRIME
    return result


def flatten(matrix):
    return [value for row in matrix for value in row]


def nullspace(matrix):
    rows = [list(row) for row in matrix]
    width = len(rows[0]) if rows else 0
    pivots, rank = [], 0
    for column in range(width):
        selected = next((r for r in range(rank, len(rows)) if rows[r][column]), None)
        if selected is None:
            continue
        rows[rank], rows[selected] = rows[selected], rows[rank]
        inverse = pow(rows[rank][column], base.PRIME - 2, base.PRIME)
        rows[rank] = [value * inverse % base.PRIME for value in rows[rank]]
        for r in range(len(rows)):
            if r != rank and rows[r][column]:
                scale = rows[r][column]
                rows[r] = [
                    (left - scale * right) % base.PRIME
                    for left, right in zip(rows[r], rows[rank])
                ]
        pivots.append(column)
        rank += 1
        if rank == len(rows):
            break
    free = [column for column in range(width) if column not in pivots]
    basis = []
    for column in free:
        vector = [0] * width
        vector[column] = 1
        for r, pivot in enumerate(pivots):
            vector[pivot] = (-rows[r][column]) % base.PRIME
        basis.append(vector)
    return basis


def trace_pair(left, right):
    size = len(left)
    return sum(
        left[i][j] * right[j][i]
        for i in range(size) for j in range(size)
    ) % base.PRIME


def trace_radical_certificate(algebra_basis, generators):
    gram = [
        [trace_pair(left, right) for right in algebra_basis]
        for left in algebra_basis
    ]
    radical_coordinates = nullspace(gram)
    size = len(generators[0])
    image_span = {}
    for coordinates in radical_coordinates:
        radical = [[0] * size for _ in range(size)]
        for coefficient, matrix in zip(coordinates, algebra_basis):
            if not coefficient:
                continue
            for i in range(size):
                for j in range(size):
                    radical[i][j] = (
                        radical[i][j] + coefficient * matrix[i][j]
                    ) % base.PRIME
        for column in range(size):
            vector = {row: radical[row][column] for row in range(size)
                      if radical[row][column]}
            base.add_pivot(vector, image_span)
    invariance_failures = 0
    image_basis = list(image_span.values())
    for generator in generators:
        for vector in image_basis:
            dense = [vector.get(i, 0) for i in range(size)]
            image = {
                i: sum(generator[i][j] * dense[j] for j in range(size)) % base.PRIME
                for i in range(size)
            }
            image = {i: value for i, value in image.items() if value}
            if base.reduce_row(image, image_span):
                invariance_failures += 1
    certificate = {
        "trace_pairing_radical_dimension": len(radical_coordinates),
        "trace_radical_image_dimension": len(image_span),
        "trace_radical_image_invariance_failures": invariance_failures,
    }
    return certificate, image_span


def case_algebra(item):
    name, (point, tangents) = item[:2]
    return_private = len(item) > 2 and item[2]
    presentation, span, _, record = support.tangent_closure_data(point, tangents)
    pivots = sorted(span, reverse=True)
    basis = [span[pivot] for pivot in pivots]
    position = {pivot: index for index, pivot in enumerate(pivots)}

    def coordinates(vector):
        row = dict(vector)
        out = [0] * len(basis)
        while row:
            active = [column for column in row if column in span]
            if not active:
                raise AssertionError(f"tangent connection escaped {name}: {sorted(row)[:8]}")
            pivot = max(active)
            coefficient = row[pivot]
            out[position[pivot]] = coefficient
            for column, value in span[pivot].items():
                base.add_value(row, column, -coefficient * value)
        return out

    matrices = []
    for tangent in tangents:
        matrix = [[0] * len(basis) for _ in basis]
        for source_index, vector in enumerate(basis):
            image = support.linear_image(presentation, vector, tangent)
            for target_index, value in enumerate(coordinates(image)):
                matrix[target_index][source_index] = value
        matrices.append(matrix)

    size = len(basis)
    identity = [[int(i == j) for j in range(size)] for i in range(size)]
    algebra_pivots, algebra_basis, frontier = {}, [], [identity]
    while frontier and len(algebra_basis) < size * size:
        candidate = frontier.pop()
        row = {i: value for i, value in enumerate(flatten(candidate)) if value}
        before = len(algebra_pivots)
        base.add_pivot(row, algebra_pivots)
        if len(algebra_pivots) == before:
            continue
        algebra_basis.append(candidate)
        frontier.extend(multiply(candidate, generator) for generator in matrices)

    digest = hashlib.sha256(
        json.dumps(matrices, separators=(",", ":")).encode()
    ).hexdigest()
    record = {
        "support": name,
        "point": list(point),
        "tangent_closure_rank": size,
        "generated_algebra_dimension": len(algebra_basis),
        "full_matrix_algebra_dimension": size * size,
        "absolutely_irreducible_at_tested_fiber": len(algebra_basis) == size * size,
        "tangent_connection_matrices_sha256": digest,
        "closure_record": record,
    }
    invariant_ambient = None
    if len(algebra_basis) < size * size:
        certificate, invariant_coordinates = trace_radical_certificate(
            algebra_basis, matrices
        )
        invariant_ambient = {}
        invariant_vectors = []
        for coordinates in invariant_coordinates.values():
            vector = {}
            for index, coefficient in coordinates.items():
                for column, value in basis[index].items():
                    base.add_value(vector, column, coefficient * value)
            invariant_vectors.append(vector)
            base.add_pivot(dict(vector), invariant_ambient)
        source_vector = support.cyclic.source_row(presentation)
        certificate["ambient_image_rank"] = len(invariant_ambient)
        certificate["ambient_pivot_labels"] = [
            presentation["ordered_columns"][pivot]
            for pivot in sorted(invariant_ambient, reverse=True)
        ]
        certificate["literal_source_in_invariant_plane"] = not bool(
            base.reduce_row(source_vector, invariant_ambient)
        )
        record["proper_algebra_certificate"] = certificate
    if return_private:
        return record, presentation, invariant_ambient, span
    return record


def main():
    items = list(support.CASES.items())
    with ProcessPoolExecutor(max_workers=4) as pool:
        records = list(pool.map(case_algebra, items))
    all_full = all(record["absolutely_irreducible_at_tested_fiber"] for record in records)
    print(json.dumps({
        "schema": "marici.benincasa.rank26-tangent-support-algebra.v1",
        "field": base.PRIME,
        "records": records,
        "all_tested_algebras_full": all_full,
        "status": (
            "all tested supported tangent closures generate their full matrix algebras"
            if all_full else
            "at least one supported tangent closure has a proper generated algebra"
        ),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
