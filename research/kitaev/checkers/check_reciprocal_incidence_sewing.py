#!/usr/bin/env python3
"""Exact audit of sewing reciprocal incidence arrows."""

import hashlib
import json
from pathlib import Path

from sympy import I, Matrix, Rational, simplify


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/reciprocal-incidence-sewing.json"


def closure(p, q, U, V):
    return simplify((p * V.inv() * q * U)[0])


def typed_unsewn_compose(p_domain, q_codomain):
    if p_domain != q_codomain:
        raise ValueError("reciprocal_incidence_carriers_not_sewn")


def main():
    p = Matrix([[1, 0]])
    q = Matrix([1, 0])
    U = Matrix([[1]])

    unsewn_rejected = False
    try:
        typed_unsewn_compose("F_plus", "F_minus")
    except ValueError:
        unsewn_rejected = True
    assert unsewn_rejected

    identity = Matrix.eye(2)
    swap = Matrix([[0, 1], [1, 0]])
    k_identity = closure(p, q, U, identity)
    k_swap = closure(p, q, U, swap)
    assert k_identity == 1
    assert k_swap == 0
    assert p.rank() == q.rank() == 1

    q_orthogonal = Matrix([0, 1])
    k_orthogonal = closure(p, q_orthogonal, U, identity)
    assert k_orthogonal == 0
    assert q_orthogonal.rank() == 1

    # Coherent independent basis changes preserve the sewn scalar.
    V = Matrix([[2, 1], [1, 1]])
    G = Matrix([[1, 1], [0, 1]])
    H = Matrix([[1, 0], [1, 1]])
    original = closure(p, q, U, V)
    p_new = p * G.inv()
    q_new = H * q
    V_new = H * V * G.inv()
    transformed = closure(p_new, q_new, U, V_new)
    assert transformed == original

    # Scalar sewing phase changes the orientation but not magnitude.
    U_phase = Matrix([[I]])
    k_phase = closure(p, q, U_phase, identity)
    assert k_phase == I
    assert simplify(k_phase * k_phase.conjugate()) == 1

    # Uniformly bounded sewing maps with collapsing transversality.
    collapse = []
    for N in (2, 3, 5, 10, 20):
        eps = Rational(1, N)
        V_inv = Matrix([[eps, 1], [1, 0]])
        V_N = V_inv.inv()
        assert V_inv.det() == -1
        assert V_N.det() == -1
        kN = simplify((p * V_inv * q)[0])
        assert kN == eps
        max_entry = max(abs(value) for value in list(V_inv) + list(V_N))
        assert max_entry <= 1
        collapse.append({
            "N": N,
            "kappa": str(kN),
            "max_absolute_sewing_entry": str(max_entry),
        })

    payload = {
        "schema": "marici.kitaev.reciprocal_incidence_sewing.v1",
        "status": "pass",
        "strength": "finite sewing and completion compiler theorem",
        "unsewn_typed_composition_rejected": unsewn_rejected,
        "identity_vs_swap_hostile": {
            "same_sector_ranks": True,
            "identity_kappa": str(k_identity),
            "swap_kappa": str(k_swap),
        },
        "orthogonality_hostile_kappa": str(k_orthogonal),
        "coherent_basis_invariance": str(original) == str(transformed),
        "sheet_phase": {"kappa": str(k_phase), "magnitude_squared": "1"},
        "uniform_sewing_transversality_collapse": collapse,
        "limiting_kappa": "0",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope_exclusions": [
            "Fourier-Tate sewing derivation", "theta sheet frame",
            "signed arithmetic current", "uniform transversality",
            "conservative realization", "zero orientation", "RH"
        ],
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
