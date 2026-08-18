"""Audit the mixed flatness equation on the weighted exceptional divisor.

This keeps the complete normal residue matrix before extracting its principal
column.  It therefore tests the typed de Rham--Cech compatibility rather than
promoting the principal column to a tangential connection block.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp


def polynomial(terms, u, v):
    return sum((sp.Rational(str(c)) * u**i * v**j for i, j, c in terms), sp.Integer(0))


def matrix_text(matrix):
    return [[sp.sstr(sp.factor(matrix[i, j])) for j in range(matrix.cols)] for i in range(matrix.rows)]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("connection", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    packet = json.loads(args.connection.read_text(encoding="utf-8"))
    u, v, e, t = sp.symbols("u v e t")
    fits = {(x["axis"], x["row"], x["col"]): x["fit"] for x in packet["entries"]}

    def entry(axis, row, col):
        fit = fits[(axis, row, col)]
        return sp.cancel(polynomial(fit["numerator"], u, v) / polynomial(fit["denominator"], u, v))

    a_u = sp.Matrix(4, 4, lambda i, j: entry("u", i, j))
    a_v = sp.Matrix(4, 4, lambda i, j: entry("v", i, j))
    substitution = {u: e, v: 2 - e + 2 * e**2 * t}
    raw_e = a_u.applyfunc(lambda x: sp.cancel(x.subs(substitution)))
    raw_e += a_v.applyfunc(lambda x: sp.cancel((-1 + 4 * e * t) * x.subs(substitution)))
    raw_t = a_v.applyfunc(lambda x: sp.cancel(2 * e**2 * x.subs(substitution)))

    weights = [0, 0, 4, 2]
    sheared_e = sp.zeros(4)
    sheared_t = sp.zeros(4)
    for i in range(4):
        for j in range(4):
            factor = e ** (weights[i] - weights[j])
            sheared_e[i, j] = sp.cancel(factor * raw_e[i, j])
            sheared_t[i, j] = sp.cancel(factor * raw_t[i, j])
        sheared_e[i, i] += sp.Rational(weights[i], 1) / e

    residue = sheared_e.applyfunc(lambda x: sp.cancel(sp.limit(e * x, e, 0)))
    tangential = sheared_t.applyfunc(lambda x: sp.cancel(sp.limit(x, e, 0)))

    # The reconstructed matrices and the committed shear use dF=A F:
    # A^S=dS S^-1+SAS^-1.  Flatness is dA-A^A=0, and its exceptional
    # 1/e coefficient is d_t R_e+[R_e,A_t|_E]=0.
    commutator = residue * tangential - tangential * residue
    mixed = (residue.diff(t) + commutator).applyfunc(sp.cancel)
    opposite_sign = (residue.diff(t) - commutator).applyfunc(sp.cancel)

    principal = sp.Matrix([residue[2, 0], residue[2, 1], residue[3, 0], residue[3, 1]])
    principal_theta_trivial_source = (principal.diff(t) + tangential * principal).applyfunc(sp.cancel)
    source_connection = tangential[:2, :2]
    target_connection = tangential[2:, 2:]
    principal_block = residue[2:, :2]
    principal_block_theta = (
        principal_block.diff(t) - target_connection * principal_block + principal_block * source_connection
    ).applyfunc(sp.cancel)

    result = {
        "schema": "marici.nima.weighted_exceptional_mixed_flatness.v1",
        "source": str(args.connection).replace("\\", "/"),
        "chart": {"u": "e", "v": "2-e+2e^2t", "weights": weights},
        "connection_convention": "dF=A F; gauge transform A^S=dS S^-1+SAS^-1",
        "normal_residue": matrix_text(residue),
        "exceptional_t_connection": matrix_text(tangential),
        "mixed_flatness_matrix": matrix_text(mixed),
        "mixed_flatness_zero": mixed == sp.zeros(4),
        "opposite_sign_matrix": matrix_text(opposite_sign),
        "principal_column": [sp.sstr(sp.factor(x)) for x in principal],
        "principal_theta_with_trivial_source": [sp.sstr(sp.factor(x)) for x in principal_theta_trivial_source],
        "inherited_source_connection": matrix_text(source_connection),
        "inherited_target_connection": matrix_text(target_connection),
        "principal_block_morphism_defect": matrix_text(principal_block_theta),
        "principal_block_is_connection_morphism": principal_block_theta == sp.zeros(2),
        "interpretation": (
            "The full residue is horizontal by ambient flatness.  The apparent e4 defect arises only after "
            "declaring the principal source tangential connection trivial.  With the source and target blocks "
            "inherited from the full transformed connection, the complete lower-left principal block is a "
            "strict morphism of connections; no horizontal--vertical homotopy is needed at this grade."
        ),
        "allocator_claim": "seqclaim-f2e0d5f1ce1d7c5ddfc407af",
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"mixed_flatness_zero": result["mixed_flatness_zero"], "principal_block_is_connection_morphism": result["principal_block_is_connection_morphism"], "principal_theta_if_source_is_forced_trivial": result["principal_theta_with_trivial_source"]}))


if __name__ == "__main__":
    main()
