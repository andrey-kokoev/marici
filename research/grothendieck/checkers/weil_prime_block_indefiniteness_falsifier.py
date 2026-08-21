"""Exact two-translate obstruction to termwise positive prime factorization."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    weight = sp.symbols("w", positive=True)
    block = sp.Matrix([[0, -weight], [-weight, 0]])
    symmetric_vector = sp.Matrix([1, 1])
    antisymmetric_vector = sp.Matrix([1, -1])

    determinant = sp.factor(block.det())
    symmetric_value = sp.expand((symmetric_vector.T * block * symmetric_vector)[0])
    antisymmetric_value = sp.expand((antisymmetric_vector.T * block * antisymmetric_vector)[0])
    eigenvalues = tuple(sorted(block.eigenvals(), key=sp.default_sort_key))

    assert determinant == -weight**2
    assert symmetric_value == -2 * weight
    assert antisymmetric_value == 2 * weight
    assert set(eigenvalues) == {-weight, weight}

    print(f"local_prime_block={block.tolist()}")
    print(f"determinant={determinant}")
    print(f"symmetric_direction={symmetric_value}")
    print(f"antisymmetric_direction={antisymmetric_value}")
    print(f"eigenvalues={eigenvalues}")
    print("prime_block_positive_semidefinite=False")
    print("deliberate_failure_exhibited=True")


if __name__ == "__main__":
    main()
