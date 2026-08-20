from __future__ import annotations

import argparse
import json
import sys
from itertools import product
from pathlib import Path

sys.path.insert(0, str(Path(__file__).with_name(".tmp_sympy")))
import sympy as sp


aa, bb, rho, lam = sp.symbols("aa bb rho lam")


def geometry():
    x = rho * lam
    y = lam
    z = sp.Integer(1)
    E = x + y + z
    h = x**2 + y**2 - z**2
    F = x**2 * aa**4 - h * aa**2 * bb**2 + y**2 * bb**4
    ga = h * (x**2 + E**2) - 2 * x**2 * (y**2 + E**2)
    gb = h * (y**2 + E**2) - 2 * y**2 * (x**2 + E**2)
    H = z**2 * ((E**2 - y**2) * (E**2 - x**2) + E**2 * z**2)
    K = sp.expand(F + ga * aa**2 + gb * bb**2 + H)

    # q=y12+E and c=y12=q-E.  K1 is dK_general/dq at q=0.
    K1 = sp.expand(
        2 * E * (x**2 - y**2 + z**2) * aa**2
        + 2 * E * (y**2 - x**2 + z**2) * bb**2
        - 2 * E * z**2 * (2 * E**2 - x**2 - y**2 + z**2)
    )
    return x, y, z, E, K, K1


X, Y, Z, E, K, K1 = geometry()
KA = sp.diff(K, aa)
KB = sp.diff(K, bb)
KL = sp.diff(K, lam)
K1L = sp.diff(K1, lam)

simple = [aa * bb, aa, None, bb, None, None, sp.Integer(1), aa**2, bb**2]
double = [None, None, -sp.Rational(1, 2) * aa * K1, None,
          -sp.Rational(1, 2) * bb * K1, -sp.Rational(1, 2) * K1,
          None, None, None]

blocks = {
    "oo": [0],
    "oe": [1, 2],
    "eo": [3, 4],
    "ee": [5, 6, 7, 8],
}
parities = {"oo": (1, 1), "oe": (1, 0), "eo": (0, 1), "ee": (0, 0)}


def monomials(max_degree: int, parity: tuple[int, int]):
    result = []
    for i in range(max_degree + 1):
        for j in range(max_degree + 1 - i):
            if i % 2 == parity[0] and j % 2 == parity[1]:
                result.append(aa**i * bb**j)
    return result


def vector_field(prefix: str, max_degree: int, target_parity: tuple[int, int]):
    pa, pb = target_parity
    mons_a = monomials(max_degree, (1 - pa, pb))
    mons_b = monomials(max_degree, (pa, 1 - pb))
    ca = sp.symbols(f"{prefix}a0:{len(mons_a)}")
    cb = sp.symbols(f"{prefix}b0:{len(mons_b)}")
    va = sum((c * m for c, m in zip(ca, mons_a)), sp.Integer(0))
    vb = sum((c * m for c, m in zip(cb, mons_b)), sp.Integer(0))
    return va, vb, list(ca) + list(cb)


def exact_numerator(Va, Vb, exponent):
    # d((-Vb da + Va db)/K^exponent), cleared to K^(exponent+1).
    return sp.expand((sp.diff(Va, aa) + sp.diff(Vb, bb)) * K
                     - exponent * (Va * KA + Vb * KB))


def derivative_terms(index: int):
    if simple[index] is not None:
        return sp.Integer(0), sp.expand(-sp.Rational(1, 2) * simple[index] * KL)
    n = double[index]
    # n/K^(3/2), with n=-P*K1/2.
    return sp.expand(-sp.Rational(3, 2) * n * KL), sp.diff(n, lam)


def solve_target(block_name: str, target: int, degree_u: int, degree_v: int,
                 numeric: bool, verbose: bool = True):
    indices = blocks[block_name]
    target_parity = parities[block_name]
    coeffs = sp.symbols(f"c0:{len(indices)}")
    V_a, V_b, v_unknowns = vector_field("v", degree_v, target_parity)
    t5, t3 = derivative_terms(target)
    if simple[target] is not None:
        u_unknowns = []
        lhs = t3
        for coeff, index in zip(coeffs, indices):
            if simple[index] is not None:
                lhs -= coeff * simple[index] * K
            else:
                lhs -= coeff * double[index]
        rhs = exact_numerator(V_a, V_b, sp.Rational(1, 2))
    else:
        U_a, U_b, u_unknowns = vector_field("u", degree_u, target_parity)
        lhs = t5 + t3 * K
        for coeff, index in zip(coeffs, indices):
            if simple[index] is not None:
                lhs -= coeff * simple[index] * K**2
            else:
                lhs -= coeff * double[index] * K
        rhs = exact_numerator(U_a, U_b, sp.Rational(3, 2))
        rhs += exact_numerator(V_a, V_b, sp.Rational(1, 2)) * K
    identity = sp.Poly(sp.expand(lhs - rhs), aa, bb)
    equations = list(identity.coeffs())
    unknowns = list(coeffs) + u_unknowns + v_unknowns
    if numeric:
        equations = [eq.subs({rho: 2, lam: 3}) for eq in equations]
    matrix, vector = sp.linear_eq_to_matrix(equations, unknowns)
    if verbose:
        print(json.dumps({
            "block": block_name,
            "target": target + 1,
            "degree_u": degree_u,
            "degree_v": degree_v,
            "equations": matrix.rows,
            "unknowns": matrix.cols,
            "rank": matrix.rank() if numeric else None,
            "augmented_rank": matrix.row_join(vector).rank() if numeric else None,
        }))
    solution = sp.linsolve((matrix, vector), unknowns)
    item = next(iter(solution))
    connection = [sp.factor(item[i]) for i in range(len(coeffs))]
    if verbose:
        print("CONNECTION", target + 1, connection)
    return connection, item, unknowns, sp.expand(identity.as_expr())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("block", choices=blocks)
    parser.add_argument("target", type=int, help="one-based e-index")
    parser.add_argument("--degree-u", type=int, default=7)
    parser.add_argument("--degree-v", type=int, default=3)
    parser.add_argument("--symbolic", action="store_true")
    args = parser.parse_args()
    solve_target(args.block, args.target - 1, args.degree_u, args.degree_v,
                 not args.symbolic)


if __name__ == "__main__":
    main()
