"""Exact support obstructions for three WP7 numerically inviable orbits.

The representative masks are (84,119).  The up texture is anti-diagonal,
so its left Gram matrix is diagonal.  The down support forces one
off-diagonal entry of its left Gram matrix to vanish.  Consequently, in
the up-mass basis the physical data must obey

    (V diag(y_d^2,y_s^2,y_b^2) V^dagger)_{ij}=0

for some distinct row pair i,j (permutations only move the pair).  Exact
rational triangle bounds from the Tab. S2 central data exclude all three
pairs, without fitting texture parameters.  Orbits 8 and 12 force
orthogonal isolated left singular vectors in the two sectors, hence an
exact CKM zero.
"""
import json
from fractions import Fraction as F
from pathlib import Path

import sympy as sp


def slots(mask):
    return [(i, j) for i in range(3) for j in range(3)
            if mask & (1 << (3 * i + j))]


mu, md = 84, 119
assert slots(mu) == [(0, 2), (1, 1), (2, 0)]
assert slots(md) == [(0, 0), (0, 1), (0, 2),
                     (1, 1), (1, 2), (2, 0)]

u02, u11, u20 = sp.symbols("u02 u11 u20", nonzero=True)
a, b, c, d, e, f = sp.symbols("a b c d e f", nonzero=True)
Yu = sp.Matrix([[0, 0, u02], [0, u11, 0], [u20, 0, 0]])
Yd = sp.Matrix([[a, b, c], [0, d, e], [f, 0, 0]])
Hu = sp.simplify(Yu * Yu.conjugate().T)
Hd = sp.simplify(Yd * Yd.conjugate().T)
assert all(Hu[i, j] == 0 for i in range(3) for j in range(3) if i != j)
assert Hd[1, 2] == 0 and Hd[2, 1] == 0

# Conservative exact bounds.  For each row pair the b-column term is
# bounded below and the d,s columns above.  Vtb >= .99 follows already
# from the quoted Vub,Vcb central values; all unspecified CKM magnitudes
# are bounded by 1.  These deliberately loose bounds still separate.
yd, ys, yb = F(154, 10_000_000), F(306, 1_000_000), F(163, 10_000)
Vus, Vub, Vcb = F(22517, 100_000), F(3763, 1_000_000), F(4189, 100_000)
Vcd, Vtd, Vts, Vtb_lo = (F(22503, 100_000), F(863, 100_000),
                          F(4117, 100_000), F(99, 100))

bounds = {
    "uc": yb*yb*Vub*Vcb - ys*ys*Vus - yd*yd*Vcd,
    "ut": yb*yb*Vub*Vtb_lo - ys*ys*Vus*Vts - yd*yd*Vtd,
    "ct": yb*yb*Vcb*Vtb_lo - ys*ys*Vts - yd*yd*Vcd*Vtd,
}
assert all(value > 0 for value in bounds.values())


def symbolic_gram(mask, prefix):
    entries = {slot: sp.Symbol(f"{prefix}{slot[0]}{slot[1]}", nonzero=True)
               for slot in slots(mask)}
    matrix = sp.Matrix(3, 3, lambda i, j: entries.get((i, j), 0))
    return sp.simplify(matrix * matrix.conjugate().T)


def isolated_rows(gram):
    return [i for i in range(3)
            if all(gram[i, j] == 0 and gram[j, i] == 0
                   for j in range(3) if j != i)]


forced_ckm_zeros = {}
for orbit, masks in {8: (85, 118), 12: (85, 220)}.items():
    hu = symbolic_gram(masks[0], f"u{orbit}_")
    hd = symbolic_gram(masks[1], f"d{orbit}_")
    iu, id_ = isolated_rows(hu), isolated_rows(hd)
    assert len(iu) == len(id_) == 1 and iu[0] != id_[0]
    forced_ckm_zeros[str(orbit)] = {
        "masks": {"u": masks[0], "d": masks[1]},
        "isolated_up_gauge_row": iu[0],
        "isolated_down_gauge_row": id_[0],
        "overlap": 0,
        "consequence": "one CKM entry vanishes exactly after mass ordering",
    }

# The six quoted off-diagonal CKM magnitudes are strictly positive; the
# three diagonal entries are positive by row normalization and these strict
# sum-of-squares bounds.  Thus the central matrix has no zero entry.
assert all(x > 0 for x in [Vus, Vub, Vcb, Vcd, Vtd, Vts])
assert Vus*Vus + Vub*Vub < 1
assert Vcd*Vcd + Vcb*Vcb < 1
assert Vtd*Vtd + Vts*Vts < 1

out = {
    "status": "proved_scoped",
    "scope": "support representatives and S3^3 orbits 1, 8, and 12",
    "masks": {"u": mu, "d": md},
    "up_gram_diagonal": True,
    "down_gram_forced_zero_pair": [1, 2],
    "physical_constraint": "some off-diagonal of V diag(yd^2,ys^2,yb^2) V^dagger vanishes",
    "central_data_triangle_lower_bounds": {
        key: {"exact": f"{value.numerator}/{value.denominator}",
              "decimal": float(value)} for key, value in bounds.items()
    },
    "all_three_pairs_excluded": True,
    "forced_ckm_zero_orbits": forced_ckm_zeros,
    "all_measured_ckm_entries_nonzero": True,
    "conclusion": "orbits 1, 8, and 12 cannot reproduce the Tab. S2 central flavor point; their WP7 failures are structural, not optimizer budget",
}
target = Path("research/flavor/results/wp10_orbit1_exact_obstruction.json")
target.parent.mkdir(parents=True, exist_ok=True)
target.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(json.dumps(out, indent=2))
