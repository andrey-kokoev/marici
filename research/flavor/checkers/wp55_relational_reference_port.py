#!/usr/bin/env python3
"""WP55: exact groupoid typing of a flavor reference port."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/flavor/results/wp55_relational_reference_port.json"


def dagger(a: sp.Matrix) -> sp.Matrix:
    return a.conjugate().T


def relative_readout(h: sp.Matrix, r: sp.Matrix) -> sp.Expr:
    return sp.simplify((dagger(r) * h * r)[0])


def main() -> None:
    h = sp.diag(1, 4, 9)
    q = sp.Matrix([[sp.Rational(3, 5), sp.Rational(4, 5), 0],
                   [-sp.Rational(4, 5), sp.Rational(3, 5), 0], [0, 0, 1]])
    h_q = sp.simplify(q * h * dagger(q))
    r = sp.Matrix([1, 0, 0])
    r_q = q * r

    original = relative_readout(h, r)
    state_only_rotated = relative_readout(h_q, r)
    pair_rotated = relative_readout(h_q, r_q)

    # A nontrivial element of the stabilizer of the reference ray.
    s = sp.diag(1, -1, 1)
    stabilizer_residual = sp.simplify(s * r - r)
    stabilizer_invariance = sp.simplify(relative_readout(s * h * dagger(s), r) - original)

    gates = {
        "weak_basis_related_states_have_same_spectrum": h.charpoly().as_expr() == h_q.charpoly().as_expr(),
        "fixed_reference_readout_fails_original_quotient_descent": state_only_rotated != original,
        "simultaneous_state_reference_action_restores_descent": pair_rotated == original,
        "declared_reference_has_nontrivial_stabilizer": stabilizer_residual == sp.zeros(3, 1),
        "readout_is_invariant_under_reference_stabilizer": stabilizer_invariance == 0,
    }
    assert all(gates.values()), gates

    result = {
        "schema": "marici.flavor.relational-reference-port.v1",
        "arithmetic": "exact SymPy rational matrix algebra",
        "original_domain": "Yukawa Gram data modulo full common-left U(3)_Q",
        "extended_domain": "pairs (H,r) with a normalized Q-space reference ray r",
        "relative_readout": "O_r(H) = r^dag H r",
        "exact_values": {
            "O_r_H": str(original),
            "O_r_QHQdag": str(state_only_rotated),
            "O_Qr_QHQdag": str(pair_rotated),
        },
        "groupoids": {
            "original": "H -> Q H Q^dag; fixed-r readout does not descend",
            "relational": "(H,r) -> (Q H Q^dag,Qr); readout descends",
            "fixed_reference_gauge": "residual arrows lie in Stab(r)",
        },
        "classification": {
            "selector_on_original_physical16": False,
            "rigidifier_of_original_chart": False,
            "new_relational_experiment": True,
            "absolute_phase_recovery": False,
            "physical_instrument": "none declared for preparing or measuring a generation-space reference ray independently of the Yukawa data",
        },
        "smallest_exact_falsifier": "the same weak-basis orbit gives O_r(H)=1 and O_r(QHQ^dag)=73/25 when r is illegally held fixed",
        "gates": gates,
        "conclusion": "A reference port repairs descent only by enlarging the state and replacing the full groupoid by the relational/stabilizer groupoid; it does not select the original physical16 quotient.",
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"passed": sum(gates.values()), "total": len(gates), "output": str(OUT.relative_to(ROOT))}))


if __name__ == "__main__":
    main()
