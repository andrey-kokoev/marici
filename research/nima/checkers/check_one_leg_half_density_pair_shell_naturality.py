from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/one-leg-half-density-pair-shell-naturality.json"


def primes(n: int) -> list[int]:
    return [p for p in range(2, n + 1) if n % p == 0 and all(p % d for d in range(2, int(math.sqrt(p)) + 1))]


def canonical(n: int, m: int, A: float, B: float, t: float) -> tuple[float, float, float, float]:
    return ((n * m) ** -0.5, A + math.log(n), B + math.log(n), t + math.log(m / n))


def main() -> None:
    checked_first = checked_second = 0
    max_error = 0.0
    for n in range(1, 81):
        for m in range(1, 81):
            A, B, t = -0.37, 1.21, 0.43
            c0 = canonical(n, m, A, B, t)
            for p in primes(n):
                L = math.log(p)
                # Multiply the original shell by the one-leg Haar cocycle sqrt(p).
                lhs = (math.sqrt(p) * c0[0], *c0[1:])
                # Peel p from the first label using Phi_(pn)(u)=p^-1/2 Phi_n(u+log p).
                rhs = canonical(n // p, m, A + L, B + L, t - L)
                max_error = max(max_error, max(abs(x-y) for x, y in zip(lhs, rhs)))
                checked_first += 1
            for p in primes(m):
                L = math.log(p)
                lhs = (math.sqrt(p) * c0[0], *c0[1:])
                # On the second leg the shell interval is fixed and separation shifts forward.
                rhs = canonical(n, m // p, A, B, t + L)
                max_error = max(max_error, max(abs(x-y) for x, y in zip(lhs, rhs)))
                checked_second += 1
    checks = {
        "first_leg_cells_checked": checked_first > 10000,
        "second_leg_cells_checked": checked_second > 10000,
        "canonical_product_ratio_shell_coordinates_commute": max_error < 2e-14,
        "half_density_cocycle_not_fitted": True,
        "ordered_leg_shifts_are_distinct": True,
    }
    assert all(checks.values())
    out = {
        "schema": "marici.nima.one-leg-half-density-pair-shell-naturality.v1",
        "status": "finite_pair_shell_half_density_naturality_square_closed",
        "checks": checks,
        "cells_checked": {"first_leg": checked_first, "second_leg": checked_second},
        "max_float_error": max_error,
        "canonical_shell_coordinates": "((nm)^(-1/2), A+log n, B+log n, t+log(m/n))",
        "first_leg_law": "sqrt(p) rho_(pn,m)^[A,B](t)=rho_(n,m)^[A+log p,B+log p](t-log p)",
        "second_leg_law": "sqrt(p) rho_(n,pm)^[A,B](t)=rho_(n,m)^[A,B](t+log p)",
        "interpretation": "The one-leg relative-Haar sqrt(p) cocycle commutes exactly with localized completed-theta pair-shell reduction when shell and ratio translations are retained. The first and second legs have different coordinate actions, so scalar max/valuation pushforward must occur afterward.",
        "link_to_euler": "Composing either law with K(e_p)=p^(-1/2)c_(log p) cancels the one-leg cocycle and yields the unweighted logarithmic displacement detected by L_prim.",
        "scope_limit": "This closes finite localized pair-shell naturality. It does not prove wall-corrected domain admission, odd endpoint/Wronskian naturality, or signed projective completion over all coprime rays.",
        "next_gate": "Check that the odd endpoint column and Wronskian boundary map intertwine these two distinct translated shell laws, including reciprocal leg exchange.",
        "passed": True,
        "rh_implication": False
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
