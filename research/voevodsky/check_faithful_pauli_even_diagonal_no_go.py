#!/usr/bin/env python3
"""Exact matrix audit: the raw even mismatch survives in the full Pauli linking Gram."""
import argparse
import json
from pathlib import Path
import sympy as s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--output",
        default="research/voevodsky/results/faithful_pauli_even_diagonal_no_go.json",
    )
    args = ap.parse_args()

    a, b, c, h, A, B, C, K = s.symbols(
        "a b c h A B C K", real=True
    )
    I = s.I
    Gwin = s.Matrix([[a, c + I*h], [c - I*h, b]])
    Gtheta = s.Matrix([[A, C + I*K], [C - I*K, B]])
    X = s.Matrix([[0, 1], [1, 0]])
    Y = s.Matrix([[0, I], [-I, 0]])
    R = X.row_join(Y)
    Pwin = s.simplify(R.conjugate().T * Gwin * R)
    Ptheta = s.simplify(R.conjugate().T * Gtheta * R)

    checks = {
        "xx_block_is_XGX": Pwin[:2, :2] == X * Gwin * X,
        "raw_even_entry_survives_at_xx_22": s.simplify(Pwin[1, 1] - a) == 0,
        "theta_even_entry_survives_at_xx_22": s.simplify(Ptheta[1, 1] - A) == 0,
        "entry_defect_is_raw_even_defect": s.simplify((Ptheta-Pwin)[1, 1]-(A-a)) == 0,
        "exact_retraction": s.simplify(X * Pwin[:2, :2] * X - Gwin) == s.zeros(2),
        "summed_frame_erases_cross_term": s.simplify(X*Gwin*X + Y*Gwin*Y - 2*s.diag(b, a)) == s.zeros(2),
    }
    assert all(checks.values())

    out = {
        "schema": "marici.voevodsky.faithful-pauli-even-diagonal-no-go.v1",
        "passed": True,
        "checks": checks,
        "ordered_output_coordinates": ["X:e1", "X:e2", "Y:e1", "Y:e2"],
        "witness_entry_zero_based": [1, 1],
        "witness_identity": "(Gamma_theta-Gamma_win)[X:e2,X:e2]=A-a",
        "analytic_input": "a=G_win(e1,e1)<1<=A=H_theta(e1,e1)",
        "conclusion": "the full faithful Pauli linking Grams are unequal",
        "boundary": "the summed frame identity remains a valid lossy coercivity statement",
        "rh_proved": False,
    }
    Path(args.output).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"passed": True, "checks": len(checks), "witness": out["witness_identity"]}))


if __name__ == "__main__":
    main()
