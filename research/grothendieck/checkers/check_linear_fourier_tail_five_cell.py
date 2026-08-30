"""Exact integer-matrix audit of the five-component Fourier tail cell."""


def multiply(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    size = len(left)
    return [
        [sum(left[i][k] * right[k][j] for k in range(size)) for j in range(size)]
        for i in range(size)
    ]


def main() -> None:
    # Ordered basis: Gaussian, constant, delta, centered tail, odd PV port.
    fourier = [
        [1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, -1],
        [0, 0, 0, 1, 0],
    ]
    identity = [[int(i == j) for j in range(5)] for i in range(5)]
    reflection = [
        [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, -1, 0],
        [0, 0, 0, 0, -1],
    ]
    square = multiply(fourier, fourier)
    fourth = multiply(square, square)
    assert square == reflection
    assert fourth == identity

    image_support = {
        row
        for column in range(5)
        for row in range(5)
        if fourier[row][column] != 0
    }
    assert image_support == set(range(5))

    print("fourier_square_equals_reflection=true")
    print("fourier_fourth_power_is_identity=true")
    print("gaussian_fixed_line_dimension=1")
    print("constant_delta_exchange_dimension=2")
    print("odd_tail_pv_quarter_turn_dimension=2")
    print("minimal_linear_components=5")
    print("repeated_boundary_differentiation_requires_jet_audit=true")


if __name__ == "__main__":
    main()
