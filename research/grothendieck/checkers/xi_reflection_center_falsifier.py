"""Exact hostile test for shifting the completed-zeta reflection center."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    c, z, delta = sp.symbols("c z delta", real=True)
    s = c + sp.I * z
    reflected = 1 - s
    same_line_reversal = c - sp.I * z
    residual = sp.expand(reflected - same_line_reversal)
    shifted_residual = sp.expand(residual.subs(c, sp.Rational(1, 2) + delta))
    unique_center = sp.solve(sp.Eq(residual, 0), c)

    assert residual == 1 - 2 * c
    assert shifted_residual == -2 * delta
    assert unique_center == [sp.Rational(1, 2)]
    assert residual.subs(c, sp.Rational(1, 2)) == 0

    print(f"reflection_line_residual={residual}")
    print(f"shifted_center_residual={shifted_residual}")
    print(f"unique_invariant_center={unique_center[0]}")
    print("nonzero_shift_preserves_centered_reversal=False")
    print("deliberate_failure_exhibited=True")


if __name__ == "__main__":
    main()
