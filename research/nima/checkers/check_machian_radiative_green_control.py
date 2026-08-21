#!/usr/bin/env python3
"""Exact bounded nonlocality control for the radiative Marici--Mach conjecture."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path


def legendre_at_zero(n: int) -> Fraction:
    values = [Fraction(1), Fraction(0)]
    for ell in range(1, n):
        values.append(-Fraction(ell, ell + 1) * values[ell - 1])
    return values[n]


def eigenvalue(ell: int) -> Fraction:
    return Fraction((ell - 1) * ell * (ell + 1) * (ell + 2), 4)


def kernel_value(cosine: str, cutoff: int) -> Fraction:
    total = Fraction(0)
    for ell in range(2, cutoff + 1):
        if cosine == "minus_one":
            p = Fraction((-1) ** ell)
        elif cosine == "zero":
            p = legendre_at_zero(ell)
        else:
            raise ValueError(cosine)
        total += Fraction(2 * ell + 1) * p / eigenvalue(ell)
    return total


def main() -> None:
    cutoffs = list(range(2, 13))
    rows = []
    for cutoff in cutoffs:
        antipodal = kernel_value("minus_one", cutoff)
        orthogonal = kernel_value("zero", cutoff)
        rows.append({
            "cutoff": cutoff,
            "antipodal_kernel_without_4pi": str(antipodal),
            "orthogonal_kernel_without_4pi": str(orthogonal),
            "antipodal_nonzero": antipodal != 0,
            "orthogonal_nonzero": orthogonal != 0,
        })
    assert all(row["antipodal_nonzero"] for row in rows)
    assert all(row["orthogonal_nonzero"] for row in rows)

    result = {
        "schema": "marici.nima.machian_radiative_green_control.v1",
        "passed": True,
        "operator": "O=(1/4)D^2(D^2+2)",
        "harmonic_eigenvalue": "(l-1)l(l+1)(l+2)/4",
        "kernel": "sum_{l=2}^L (2l+1) P_l(cos gamma)/lambda_l; common 1/(4pi) omitted",
        "cutoffs": rows,
        "interpretation": (
            "Within every tested exact harmonic truncation, a source at an "
            "antipodal or orthogonal direction contributes nontrivially to "
            "the local inverse-O memory response."
        ),
        "scope": (
            "Weak relational/nonlocal radiative-gravity control only. It does "
            "not derive inertial frames, inertial mass, Einstein dynamics, or "
            "a Mach principle from the Marici Carrier."
        ),
    }
    root = Path(__file__).resolve().parents[3]
    output = root / "research/nima/results/machian-radiative-green-control.json"
    if not output.exists():
        raise AssertionError(f"missing frozen result packet: {output}")
    payload = output.read_text(encoding="utf-8")
    assert json.loads(payload) == result
    print(json.dumps({
        "passed": True,
        "cutoffs": len(cutoffs),
        "sha256": hashlib.sha256(payload.encode()).hexdigest().upper(),
    }))


if __name__ == "__main__":
    main()
