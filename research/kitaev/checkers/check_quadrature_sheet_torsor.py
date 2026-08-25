#!/usr/bin/env python3
"""Exact C2 sheet action on a trace plus spin-two quadrature packet."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
OUT = K / "results" / "quadrature-sheet-torsor.json"


def reduced_zero(matrix: sp.Matrix, c: sp.Symbol, s: sp.Symbol) -> bool:
    """Check every entry modulo c^2+s^2-1."""
    basis = sp.groebner([c**2 + s**2 - 1], c, s)
    return all(basis.reduce(sp.expand(entry))[1] == 0 for entry in matrix)


def main() -> None:
    c, s = sp.symbols("c s", real=True)
    identity = sp.eye(2)

    # c=cos(2 theta), s=sin(2 theta). Q is the normalized spin-two form.
    Q = sp.Matrix([[c, s], [s, -c]])
    # This reflection swaps the +1 and -1 eigenquadratures of Q.
    R = sp.Matrix([[-s, c], [c, s]])

    assert reduced_zero(Q**2 - identity, c, s)
    assert reduced_zero(R.T * R - identity, c, s)
    assert reduced_zero(R**2 - identity, c, s)
    assert reduced_zero(R.T * Q * R + Q, c, s)
    assert reduced_zero(R * Q + Q * R, c, s)
    assert sp.trace(Q) == 0

    E_plus = identity + Q
    E_minus = identity - Q
    assert reduced_zero(E_plus * E_minus, c, s)
    assert E_plus + E_minus == 2 * identity
    assert sp.trace(E_plus) == sp.trace(E_minus) == 2
    assert reduced_zero(sp.Matrix([[E_plus.det()]]), c, s)
    assert reduced_zero(sp.Matrix([[E_minus.det()]]), c, s)
    assert reduced_zero(R.T * E_plus * R - E_minus, c, s)

    # Concrete exact specialization theta=0 exhibits ranks and null lines.
    q0 = sp.diag(1, -1)
    r0 = sp.Matrix([[0, 1], [1, 0]])
    ep0, em0 = identity + q0, identity - q0
    assert ep0.rank() == em0.rank() == 1
    assert (ep0 + em0).rank() == 2
    assert ep0.nullspace() == [sp.Matrix([0, 1])]
    assert em0.nullspace() == [sp.Matrix([1, 0])]
    assert r0.T * q0 * r0 == -q0

    # Deliberate failure: repeating the same sheet form retains one null line.
    bad_sum = ep0 + ep0
    assert bad_sum.rank() == 1
    assert bad_sum.nullspace() == ep0.nullspace()

    # A torsor origin bit labels +/-; it cannot reconstruct x=(A,B).
    origin_map = sp.Matrix([[1, 0]])
    assert origin_map.rank() == 1
    assert len(origin_map.nullspace()) == 1

    result = {
        "schema": "marici.kitaev.quadrature-sheet-torsor.v1",
        "exact_ring": "Q[c,s]/(c^2+s^2-1)",
        "forms": {
            "trace_matrix": [[1, 0], [0, 1]],
            "spin_two_matrix": [["c", "s"], ["s", "-c"]],
            "spin_two_trace": 0,
            "spin_two_square": "I modulo c^2+s^2=1",
        },
        "sheet_action": {
            "matrix": [["-s", "c"], ["c", "s"]],
            "orthogonal": True,
            "involution": True,
            "preserves_trace": True,
            "flips_spin_two": True,
            "criterion": "R^T Q R=-Q, equivalently RQ=-QR for an orthogonal involution",
            "geometric_classification": "reflection across an axis bisecting the two eigenquadrature axes of Q; identity and -I do not flip Q",
        },
        "sheet_energies": {
            "E_plus": "I+Q",
            "E_minus": "I-Q",
            "each_eigenvalues": [0, 2],
            "each_rank": 1,
            "null_lines_complementary": True,
            "product": "E_plus E_minus=0",
            "sum": "2I",
            "sum_rank": 2,
        },
        "typing": {
            "torsor_origin_bits": 1,
            "linear_amplitude_coordinates": 2,
            "origin_bit_reconstructs_amplitude": False,
            "meaning": "the bit labels which complementary quadrature is called plus; it supplies no missing real amplitude coordinate",
        },
        "composition": {
            "C2_displacement_law": "epsilon(D o C)=epsilon(D)+epsilon(C) mod 2",
            "representation_law": "rho(D o C)=rho(D)rho(C)",
            "required_coherence": "the spin-two sign character chi obeys chi(D o C)=chi(D)chi(C)",
        },
        "deliberate_falsifier": {
            "bad_pair": ["I+Q", "I+Q"],
            "theta_zero_bad_sum_rank": 1,
            "shared_null_direction": [0, 1],
            "failure": "same-sign sheets do not complete the norm",
        },
        "source_authority_boundary": {
            "D_S3_authorizes_Fourier_Tate_action": False,
            "must_be_derived": ["actual sheet displacement g_C", "lambda", "theta", "endpoint and Mellin normalization", "completion stability"],
        },
        "verdict": "An orthogonal C2 sheet involution exchanges the two semidefinite quadrature energies precisely when it anticommutes with the normalized spin-two form. Then the sheets have complementary null lines and sum to the positive-definite form 2|psi|^2. One torsor bit labels the sheets but cannot reconstruct the two real amplitude coordinates.",
    }
    checker = Path(__file__)
    result["checker_sha256"] = hashlib.sha256(checker.read_bytes()).hexdigest()
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
