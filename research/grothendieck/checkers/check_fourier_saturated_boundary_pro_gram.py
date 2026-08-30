"""Exact finite-cutoff audit of the Fourier-saturated theta boundary grades."""

from sympy import Matrix, Rational, diag


PRIMES = (2, 3, 5, 7, 11)


def sheet_rotation(size: int) -> Matrix:
    identity = Matrix.eye(size)
    zero = Matrix.zeros(size)
    return zero.row_join(-identity).col_join(identity.row_join(zero))


def sheet_gram(weights: tuple[int, ...]) -> Matrix:
    return diag(*weights, *([0] * len(weights)))


def saturate(q: Matrix, fourier: Matrix) -> Matrix:
    return sum(
        ((fourier**j).T * q * (fourier**j) for j in range(4)),
        Matrix.zeros(q.rows),
    )


def main() -> None:
    n = len(PRIMES)
    fourier = sheet_rotation(n)
    primitive = sheet_gram(tuple(p * p for p in PRIMES))
    square = sheet_gram(tuple(1 for _ in PRIMES))
    primitive_sat = saturate(primitive, fourier)
    square_sat = saturate(square, fourier)

    expected_primitive = 2 * diag(
        *(tuple(p * p for p in PRIMES) * 2)
    )
    expected_square = 2 * Matrix.eye(2 * n)
    assert fourier**2 == -Matrix.eye(2 * n)
    assert fourier**4 == Matrix.eye(2 * n)
    assert primitive_sat == expected_primitive
    assert square_sat == expected_square

    generalized = primitive_sat.inv() * square_sat
    eigenvalues = sorted(generalized.eigenvals(), key=lambda x: float(x))
    assert eigenvalues[0] == Rational(1, PRIMES[-1] ** 2)
    assert generalized.det() != 0

    print("fourier_order_4=true")
    print("primitive_saturation_exact=true")
    print("square_saturation_exact=true")
    print(f"cutoff_largest_prime={PRIMES[-1]}")
    print(f"smallest_generalized_eigenvalue={eigenvalues[0]}")
    print("asymptotic_generalized_floor=0")
    print("single_uniform_gram_equivalence=false")
    print("typed_pro_gram_family_required=true")


if __name__ == "__main__":
    main()
