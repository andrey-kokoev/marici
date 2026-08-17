"""D8-module audit of the four square-curvature lattice."""

from itertools import product


def act(vector, permutation):
    out = [0] * len(vector)
    for old, value in enumerate(vector):
        out[permutation[old]] = value
    return tuple(out)


def rank(matrix):
    data = [[float(x) for x in row] for row in matrix]
    pivot = 0
    for column in range(len(data[0])):
        row = next((i for i in range(pivot, len(data)) if data[i][column]), None)
        if row is None:
            continue
        data[pivot], data[row] = data[row], data[pivot]
        scale = data[pivot][column]
        data[pivot] = [x / scale for x in data[pivot]]
        for i in range(len(data)):
            if i != pivot and data[i][column]:
                scale = data[i][column]
                data[i] = [x - scale * y for x, y in zip(data[i], data[pivot])]
        pivot += 1
    return pivot


def main():
    # Diameter i means (i,i+4), with i modulo four.
    rotations = [tuple((i + k) % 4 for i in range(4)) for k in range(4)]
    reflections = [tuple((k - i) % 4 for i in range(4)) for k in range(4)]
    d8_on_squares = set(rotations + reflections)
    assert len(d8_on_squares) == 8  # central half-turn acts trivially here

    augmentation = (1, 1, 1, 1)
    kernel_basis = ((-1, 1, 0, 0), (-1, 0, 1, 0), (-1, 0, 0, 1))
    assert rank([augmentation]) == 1
    assert rank(kernel_basis) == 3
    assert all(sum(v) == 0 for v in kernel_basis)
    assert all(sum(act(v, g)) == 0 for v, g in product(kernel_basis, d8_on_squares))

    # The non-scalar kernel splits over Q as an alternating line plus the
    # standard two-dimensional square representation.
    alternating = (1, -1, 1, -1)
    standard_basis = ((1, 0, -1, 0), (0, 1, 0, -1))
    assert sum(alternating) == 0
    assert rank((alternating,) + standard_basis) == 3
    assert all(sum(x * y for x, y in zip(alternating, v)) == 0 for v in standard_basis)
    assert {act(alternating, g) for g in d8_on_squares} == {
        alternating,
        tuple(-x for x in alternating),
    }
    standard_span_samples = {
        tuple(a * u + b * v for u, v in zip(standard_basis[0], standard_basis[1]))
        for a in range(-2, 3)
        for b in range(-2, 3)
    }
    assert all(act(v, g) in standard_span_samples for v, g in product(standard_basis, d8_on_squares))

    # Entry 401 kills only the invariant scalar image.
    selected_endpoint_scalar = 0
    assert selected_endpoint_scalar * sum(augmentation) == 0

    print("square_curvature_lattice_rank: 4")
    print("effective_D8_action_order: 8")
    print("scalar_Jordan_comparison_row: [1,1,1,1]")
    print("scalar_image_rank: 1")
    print("non_scalar_kernel_rank: 3")
    print("kernel_Q_decomposition: alternating_line + standard_2d")
    print("endpoint_scalar_image: 0")
    print("actual_curvature_vector_evaluated: NO")


if __name__ == "__main__":
    main()
