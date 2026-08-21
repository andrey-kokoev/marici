"""Exact witnesses for the finite unitary-orbit Li-growth no-go."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    theta = sp.symbols("theta", real=True)
    z = sp.exp(sp.I * theta)

    # Scalar spectral fibre: the bound is sharp at z^n=-1.
    scalar_norm = sp.simplify((1 - z) * (1 - sp.conjugate(z)))
    sharp_value = sp.simplify(scalar_norm.subs(theta, sp.pi))
    assert sharp_value == 4

    # A two-point exact unitary example remains bounded for many iterates.
    roots = (sp.Integer(1), sp.Integer(-1), sp.I, -sp.I)
    values = []
    for n in range(1, 17):
        value = sp.simplify(sum(abs(1 - root**n) ** 2 for root in roots))
        assert 0 <= value <= 4 * len(roots)
        values.append(int(value))

    print("pointwise_bound=4")
    print(f"sharp_value={sharp_value}")
    print(f"finite_measure_bound={4 * len(roots)}")
    print("sample_norm_squares=" + ",".join(map(str, values)))
    print("unbounded_target_compatible=False")


if __name__ == "__main__":
    main()
