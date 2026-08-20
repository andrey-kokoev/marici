#!/usr/bin/env python3
"""Exact local monodromy complexes for Entry 1120's residue matrices."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/benincasa/results/rank12-u0-v2-exact-quotient-residues.json"
OUTPUT = ROOT / "research/benincasa/results/rank12-u0-v2-residue-monodromy-complex.json"
s = sp.symbols("s")
f = s**2 + 6 * s + 1
alpha = -3 + 2 * sp.sqrt(2)


def parse_matrix(rows):
    return sp.Matrix([[sp.sympify(x, locals={"s": s}) for x in row] for row in rows])


def reduce_f(x):
    return sp.rem(sp.cancel(x).as_numer_denom()[0], f, s) / sp.rem(
        sp.cancel(x).as_numer_denom()[1], f, s
    )


def reduce_matrix(m):
    return m.applyfunc(lambda x: sp.cancel(reduce_f(x)))


def quotient_rank(m):
    """Rank over Q[s]/(f), evaluated at one exact algebraic embedding."""
    return m.subs(s, alpha).applyfunc(sp.simplify).rank()


packet = json.loads(SOURCE.read_text(encoding="utf-8"))
residues = {row["divisor"]: parse_matrix(row["matrix"]) for row in packet["residues"]}

out = []
for divisor in ("s", "s-1", "s+1"):
    R = residues[divisor]
    # Every rational residue is semisimple with integral spectrum, hence exp(2 pi i R)=I.
    assert R.is_diagonalizable()
    assert all(ev.is_integer for ev in R.eigenvals())
    out.append(
        {
            "divisor": divisor,
            "residue_semisimple": True,
            "local_monodromy": "I_4",
            "rank_T_minus_I": 0,
            "invariant_rank": 4,
            "coinvariant_rank": 4,
        }
    )

R = residues["s^2+6s+1"]
P_minus = reduce_matrix(4 * R**2)
P_zero = reduce_matrix(sp.eye(4) - P_minus)
N_zero = reduce_matrix(R * P_zero)

# Source-fixed marked Cousin maps from Entry 851, restricted to the quotient
# basis (Omega111, Omega101, Omega110, e5).
res_walls = sp.Matrix(
    [
        [-1, 0, 0, 0],  # t1
        [0, -1, 0, 0],  # g1
        [1, 0, 0, 0],   # t2
        [0, 0, 1, 0],   # g2
    ]
)
res_top = sp.Matrix([[1, 0, 1, 0]])
kummer_generator = sp.Matrix([-(s + 7) / 4, 1, 0, 0])
kummer_wall_image = reduce_matrix(res_walls * kummer_generator)

assert reduce_matrix(P_minus**2 - P_minus) == sp.zeros(4)
assert reduce_matrix(P_zero**2 - P_zero) == sp.zeros(4)
assert reduce_matrix(P_minus * P_zero) == sp.zeros(4)
assert quotient_rank(P_minus) == 1
assert quotient_rank(P_zero) == 3
assert quotient_rank(N_zero) == 0
assert reduce_matrix(N_zero**2) == sp.zeros(4)
assert reduce_matrix(P_minus * kummer_generator - kummer_generator) == sp.zeros(4, 1)
assert quotient_rank(kummer_wall_image) == 1
assert reduce_matrix(res_top * kummer_wall_image) == sp.zeros(1, 1)

# On the Kummer line T=-1, so T-I is invertible.  The rank-three
# zero-residue sector is semisimple and has identity monodromy.
out.append(
    {
        "divisor": "s^2+6s+1",
        "field": "Q[s]/(s^2+6s+1)",
        "kummer_projector": [[str(reduce_f(x)) for x in row] for row in P_minus.tolist()],
        "unipotent_projector": [[str(reduce_f(x)) for x in row] for row in P_zero.tolist()],
        "nilpotent_logarithm": [[str(reduce_f(x)) for x in row] for row in N_zero.tolist()],
        "kummer_rank": 1,
        "zero_residue_rank": 3,
        "nilpotent_rank": 0,
        "nilpotent_square_zero": True,
        "rank_T_minus_I": 1,
        "invariant_rank": 3,
        "coinvariant_rank": 3,
        "monodromy_description": "(-1) on the Kummer line; identity on the rank-three zero-residue sector",
        "kummer_generator": [str(reduce_f(x)) for x in kummer_generator],
        "stacked_wall_basis": ["t1", "g1", "t2", "g2"],
        "stacked_wall_image": [str(reduce_f(x)) for x in kummer_wall_image],
        "top_residue_of_wall_image": ["0"],
        "wall_coherence": "The W1 and W2 top residues cancel under Res_top=(1,0,1,0).",
    }
)

result = {
    "schema": "marici.benincasa.rank12_u0_v2_residue_monodromy_complex.v1",
    "status": "passed",
    "connection_basis": packet["basis"],
    "local_complexes": out,
    "conclusion": "Only the quadratic marked collision has nontrivial local monodromy. Its Kummer line maps nontrivially into the source-fixed two-wall Cousin complex and its two top residues cancel exactly.",
}
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"schema": result["schema"], "status": "passed", "local_complexes": out}, default=str))
