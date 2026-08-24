"""Exact attack on the naive universal value-or-obstruction result shape."""

from __future__ import annotations

import json
from pathlib import Path


def mul_truncated(left: tuple[int, ...], right: tuple[int, ...], degree: int) -> tuple[int, ...]:
    out = [0] * (degree + 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= degree:
                out[i + j] += a * b
    return tuple(out)


def residue(left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
    return left[1] * right[2] + left[2] * right[1]


def lifted_mul(
    left: tuple[tuple[int, int, int], int],
    right: tuple[tuple[int, int, int], int],
) -> tuple[tuple[int, int, int], int]:
    u, r_u = left
    v, r_v = right
    return (
        mul_truncated(u, v, 2),
        u[0] * r_v + r_u * v[0] + residue(u, v),
    )


def main() -> None:
    u = (1, 1, 0)
    v = (1, 0, 1)
    u_prime = (1, 0, 0)
    v_prime = (1, 1, 1)

    visible = mul_truncated(u, v, 2)
    visible_prime = mul_truncated(u_prime, v_prime, 2)
    assert visible == visible_prime == (1, 1, 1)
    assert residue(u, v) == 1
    assert residue(u_prime, v_prime) == 0

    # Hostile exact associativity census on a finite integer test basis.
    basis = [
        (0, 0, 0),
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1),
        (1, 1, 1),
        (2, -1, 3),
    ]
    associator_residuals = []
    degree_three_reconstruction_residuals = []
    for a in basis:
        for b in basis:
            for c in basis:
                ab_c = lifted_mul(lifted_mul((a, 0), (b, 0)), (c, 0))
                a_bc = lifted_mul((a, 0), lifted_mul((b, 0), (c, 0)))
                associator_residuals.append((ab_c[0], a_bc[0], ab_c[1] - a_bc[1]))

                exact = mul_truncated(mul_truncated(a, b, 3), c, 3)
                reconstructed = ab_c[0] + (ab_c[1],)
                degree_three_reconstruction_residuals.append(
                    tuple(x - y for x, y in zip(reconstructed, exact))
                )

    assert all(x == y and r == 0 for x, y, r in associator_residuals)
    assert all(all(value == 0 for value in row) for row in degree_three_reconstruction_residuals)

    result = {
        "status": "PASS",
        "naive_coproduct_status": "FALSIFIED",
        "shared_visible_value": list(visible),
        "first_residue": residue(u, v),
        "second_residue": residue(u_prime, v_prime),
        "associativity_cases": len(associator_residuals),
        "lifted_associator_residual": 0,
        "degree_three_reconstruction_residual": [0, 0, 0, 0],
        "survivor": "operation-indexed resolved result with simultaneous value and residue",
        "scope": "exact filtered-jet model; not yet a physical-sector Carrier theorem",
    }

    output = Path(__file__).parents[1] / "results" / "operational-residue-result-shapes.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
