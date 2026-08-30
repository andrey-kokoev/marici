#!/usr/bin/env python3
"""Exact audit of the two-amplitude photon Bell packet of arXiv:2212.10213v3."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "research" / "nima" / "results" / "photon-bell-source-packet.json"


def main() -> None:
    r, s = sp.symbols("r s", real=True)
    den = r**2 + s**2
    sqrt2 = sp.sqrt(2)
    I2 = sp.eye(2)
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])

    # Sinha-Zahed/CGLMP MES settings, arXiv:2212.10213v3 eqs. (6)-(13).
    settings = {
        "A1": -sx,
        "A2": sy,
        "B1": (-sx + sy) / sqrt2,
        "B2": (-sx - sy) / sqrt2,
    }
    ket = sp.Matrix([r, 0, 0, s])
    rho = sp.simplify(ket * ket.T / den)

    def expectation(left: sp.Matrix, right: sp.Matrix) -> sp.Expr:
        return sp.simplify(sp.trace(rho * sp.kronecker_product(left, right)))

    # This sign convention reproduces the source's eq. (13).
    bell = sp.simplify(
        expectation(settings["A1"], settings["B1"])
        + expectation(settings["A1"], settings["B2"])
        - expectation(settings["A2"], settings["B1"])
        + expectation(settings["A2"], settings["B2"])
    )
    expected_bell = sp.simplify(4 * sqrt2 * r * s / den)

    probabilities = {}
    normalization_residuals = {}
    no_signalling_residuals = []
    signs = (-1, 1)
    for aname in ("A1", "A2"):
        for bname in ("B1", "B2"):
            table = {}
            for a in signs:
                pa = (I2 + a * settings[aname]) / 2
                for b in signs:
                    pb = (I2 + b * settings[bname]) / 2
                    value = sp.simplify(sp.trace(rho * sp.kronecker_product(pa, pb)))
                    table[f"{a},{b}"] = str(value)
            probabilities[f"{aname},{bname}"] = table
            normalization_residuals[f"{aname},{bname}"] = str(
                sp.simplify(sum(sp.sympify(v) for v in table.values()) - 1)
            )

    # Alice marginals are independent of Bob's choice and vice versa.
    for aname in ("A1", "A2"):
        for a in signs:
            m1 = sum(sp.sympify(probabilities[f"{aname},B1"][f"{a},{b}"]) for b in signs)
            m2 = sum(sp.sympify(probabilities[f"{aname},B2"][f"{a},{b}"]) for b in signs)
            no_signalling_residuals.append(str(sp.simplify(m1 - m2)))
    for bname in ("B1", "B2"):
        for b in signs:
            m1 = sum(sp.sympify(probabilities[f"A1,{bname}"][f"{a},{b}"]) for a in signs)
            m2 = sum(sp.sympify(probabilities[f"A2,{bname}"][f"{a},{b}"]) for a in signs)
            no_signalling_residuals.append(str(sp.simplify(m1 - m2)))

    assert sp.simplify(sp.trace(rho) - 1) == 0
    assert all(v == "0" for v in normalization_residuals.values())
    assert all(v == "0" for v in no_signalling_residuals)
    assert sp.simplify(bell - expected_bell) == 0

    # |4 sqrt(2) r s/(r^2+s^2)| <= 2 sqrt(2) follows from
    # (|r|-|s|)^2 >= 0. Record the exact polynomial slack for r,s >= 0.
    tsirelson_slack_numerator = sp.expand(2 * sqrt2 * den - 4 * sqrt2 * r * s)
    assert sp.simplify(tsirelson_slack_numerator - 2 * sqrt2 * (r - s) ** 2) == 0

    result = {
        "schema": "marici.photon-bell-source-packet.v1",
        "strength": "exact source-formula audit",
        "source": {
            "title": "Bell inequalities in 2-2 scattering",
            "authors": ["Aninda Sinha", "Ahmadullah Zahed"],
            "version": "arXiv:2212.10213v3",
            "doi": "10.1103/PhysRevD.108.025015",
            "equations": [6, 8, 9, 10, 11, 13],
        },
        "specialization": "fixed incoming ++ photons; low-energy outgoing state N(Phi1|00>+Phi2|11>); Phi1=r and Phi2=s real",
        "state_trace_residual": str(sp.simplify(sp.trace(rho) - 1)),
        "joint_probabilities": probabilities,
        "normalization_residuals": normalization_residuals,
        "no_signalling_residuals": no_signalling_residuals,
        "bell_expression": str(bell),
        "source_equation_13_specialization": str(expected_bell),
        "tsirelson_slack_numerator": str(tsirelson_slack_numerator),
        "tsirelson_factorization": str(2 * sqrt2 * (r - s) ** 2),
        "maximal_at": "r=s!=0",
        "gate_vector": [True, True, True, True, True, True],
        "marici_comparison_status": (
            "The external source packet types the Bell experiment and exact quantum bound. "
            "It is not yet derived from the Marici transmutation/relative-totalization maps."
        ),
        "next_falsifier": (
            "Construct the map from the Ward-reduced two-open-pair scattering object to the "
            "positive helicity density object, and test whether its projector effects and "
            "Born pairing commute with physical Cut."
        ),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["content_sha256"] = hashlib.sha256(canonical).hexdigest().upper()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"bell": str(bell), "sha256": result["content_sha256"]}))


if __name__ == "__main__":
    main()
