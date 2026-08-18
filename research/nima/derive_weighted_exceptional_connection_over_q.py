"""Pull the reconstructed Q-connection to the weighted exceptional chart."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp


def rational(text: str) -> sp.Rational:
    return sp.Rational(text)


def polynomial(terms: list[list[object]], u: sp.Symbol, v: sp.Symbol):
    return sum((rational(str(c)) * u**i * v**j for i, j, c in terms), sp.Integer(0))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("connection", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    packet = json.loads(args.connection.read_text(encoding="utf-8"))
    u, v, e, t = sp.symbols("u v e t")
    entries = {(x["axis"], x["row"], x["col"]): x["fit"] for x in packet["entries"]}

    def expression(axis: str, row: int, col: int):
        fit = entries[(axis, row, col)]
        return sp.cancel(polynomial(fit["numerator"], u, v) / polynomial(fit["denominator"], u, v))

    av = sp.Matrix(4, 4, lambda i, j: expression("v", i, j))
    substitution = {u: e, v: 2 - e + 2 * e**2 * t}
    raw_t = av.applyfunc(lambda x: sp.cancel(2 * e**2 * x.subs(substitution)))
    weights = [0, 0, 4, 2]
    sheared_t = sp.Matrix(
        4,
        4,
        lambda i, j: sp.cancel(e ** (weights[i] - weights[j]) * raw_t[i, j]),
    )
    exceptional_t = sheared_t.applyfunc(lambda x: sp.cancel(sp.limit(x, e, 0)))

    residues = {}
    ell = sp.Matrix([0, 1, 0, -3])
    ell_connection_action = exceptional_t * ell
    ell_horizontal = sp.Matrix.hstack(ell, ell_connection_action).rank() <= 1
    horizontal_closure_basis = sp.Matrix.hstack(ell, ell_connection_action).columnspace()
    for label, point in (("plus", 1), ("minus", -1)):
        residue = exceptional_t.applyfunc(
            lambda x: sp.cancel(sp.limit((t - point) * x, t, point))
        )
        if residue * residue != residue:
            raise AssertionError(f"residue at {point} is not idempotent")
        action = residue * ell
        augmented_rank = residue.row_join(action).rank()
        residues[label] = {
            "point": point,
            "matrix": [[sp.sstr(residue[i, j]) for j in range(4)] for i in range(4)],
            "rank": residue.rank(),
            "characteristic_polynomial": sp.sstr(sp.factor(residue.charpoly().as_expr())),
            "ell_action": [sp.sstr(x) for x in action],
            "ell_invariant": augmented_rank == residue.rank() and sp.Matrix.hstack(ell, action).rank() <= 1,
            "ell_eigenvalue": (
                sp.sstr(next(action[i] / ell[i] for i in range(4) if ell[i] != 0))
                if sp.Matrix.hstack(ell, action).rank() <= 1
                else None
            ),
            "residue_idempotent": True,
            "local_monodromy": "identity_4",
            "local_monodromy_reason": "exp(-2*pi*i*R)=I for an idempotent R with eigenvalues 0 and 1",
        }

    result = {
        "schema": "marici.nima.weighted_exceptional_connection_Q.v1",
        "source": str(args.connection).replace("\\", "/"),
        "chart": {"u": "e", "v": "2-e+2*e^2*t", "weights": weights},
        "connection_convention": "dF + A F = 0; local monodromy exp(-2*pi*i*Res(A))",
        "exceptional_t_connection": [
            [sp.sstr(exceptional_t[i, j]) for j in range(4)] for i in range(4)
        ],
        "constant_exceptional_line": {
            "generator": [sp.sstr(x) for x in ell],
            "connection_action": [sp.sstr(x) for x in ell_connection_action],
            "horizontal": ell_horizontal,
            "minimum_horizontal_closure_rank": len(horizontal_closure_basis),
            "minimum_horizontal_closure_basis": [
                [sp.sstr(x) for x in vector] for vector in horizontal_closure_basis
            ],
        },
        "residues": residues,
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"residues": residues}))


if __name__ == "__main__":
    main()
