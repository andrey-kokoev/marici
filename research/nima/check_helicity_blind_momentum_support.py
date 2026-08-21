#!/usr/bin/env python3
"""Exact two-bin audit of helicity-blind phase-space support for Bell readout."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "research" / "nima" / "results" / "helicity-blind-momentum-support.json"


def main() -> None:
    r1, s1, r2, s2, w1, w2 = sp.symbols(
        "r1 s1 r2 s2 w1 w2", real=True, positive=True
    )
    sqrt2 = sp.sqrt(2)
    I2 = sp.eye(2)
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    settings_a = {"A1": -sx, "A2": sy}
    settings_b = {"B1": (-sx + sy) / sqrt2, "B2": (-sx - sy) / sqrt2}

    def rho(r: sp.Symbol, s: sp.Symbol) -> sp.Matrix:
        ket = sp.Matrix([r, 0, 0, s])
        return sp.simplify(ket * ket.T / (r**2 + s**2))

    bins = [(w1, rho(r1, s1)), (w2, rho(r2, s2))]
    total_weight = w1 + w2

    tables = {}
    normalization_residuals = {}
    alice_no_signalling = []
    bob_no_signalling = []
    signs = (-1, 1)
    for aname, A in settings_a.items():
        for bname, B in settings_b.items():
            table = {}
            for a in signs:
                EA = (I2 + a * A) / 2
                for b in signs:
                    EB = (I2 + b * B) / 2
                    value = sum(
                        weight * sp.trace(state * sp.kronecker_product(EA, EB))
                        for weight, state in bins
                    ) / total_weight
                    table[f"{a},{b}"] = sp.factor(sp.simplify(value))
            tables[f"{aname},{bname}"] = table
            normalization_residuals[f"{aname},{bname}"] = sp.simplify(sum(table.values()) - 1)

    for aname in settings_a:
        for a in signs:
            left = sum(tables[f"{aname},B1"][f"{a},{b}"] for b in signs)
            right = sum(tables[f"{aname},B2"][f"{a},{b}"] for b in signs)
            alice_no_signalling.append(sp.simplify(left - right))
    for bname in settings_b:
        for b in signs:
            left = sum(tables[f"A1,{bname}"][f"{a},{b}"] for a in signs)
            right = sum(tables[f"A2,{bname}"][f"{a},{b}"] for a in signs)
            bob_no_signalling.append(sp.simplify(left - right))

    assert all(value == 0 for value in normalization_residuals.values())
    assert all(value == 0 for value in alice_no_signalling + bob_no_signalling)

    bell1 = 4 * sqrt2 * r1 * s1 / (r1**2 + s1**2)
    bell2 = 4 * sqrt2 * r2 * s2 / (r2**2 + s2**2)
    bell_mixture = sp.factor((w1 * bell1 + w2 * bell2) / total_weight)
    tsirelson_slack = sp.factor(2 * sqrt2 - bell_mixture)
    expected_slack = sp.factor(
        2
        * sqrt2
        * (
            w1 * (r1 - s1) ** 2 / (r1**2 + s1**2)
            + w2 * (r2 - s2) ** 2 / (r2**2 + s2**2)
        )
        / total_weight
    )
    assert sp.simplify(tsirelson_slack - expected_slack) == 0

    result = {
        "schema": "marici.helicity-blind-momentum-support.v1",
        "strength": "exact two-bin support theorem",
        "source_typing": (
            "Sinha-Zahed fixes momenta and treats helicities at those momenta as qubits; "
            "the tested extension is a positive helicity-blind union of two momentum bins."
        ),
        "normalization_residuals": {k: str(v) for k, v in normalization_residuals.items()},
        "alice_no_signalling_residuals": [str(v) for v in alice_no_signalling],
        "bob_no_signalling_residuals": [str(v) for v in bob_no_signalling],
        "bell_mixture": str(bell_mixture),
        "tsirelson_slack": str(tsirelson_slack),
        "positive_slack_decomposition": str(expected_slack),
        "support_condition": (
            "Each nonnegative momentum-bin weight multiplies the identity on the helicity "
            "fiber and is independent of analyzer setting and outcome."
        ),
        "conclusion": (
            "Helicity-blind base support preserves normalized no-signalling and the Tsirelson "
            "bound under positive bin mixing. This supplies a canonical theoretical support "
            "class for the source packet, but not a loophole-free model of a real detector."
        ),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["content_sha256"] = hashlib.sha256(canonical).hexdigest().upper()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "normalization": True,
        "no_signalling": True,
        "tsirelson_positive_slack": True,
        "sha256": result["content_sha256"],
    }))


if __name__ == "__main__":
    main()
