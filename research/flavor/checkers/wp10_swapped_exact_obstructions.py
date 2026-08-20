"""Exact physical exclusions for swapped WP10 orientations 1, 8, and 12.

Sector exchange is not a physical quotient, so these are separate certificates
from the original-orientation obstruction.  Swapped orbit 1 makes the down
Gram diagonal and forces an off-diagonal zero in the up Gram.  In the
down-mass basis this requires an off-diagonal entry of
V^dagger diag(y_u^2,y_c^2,y_t^2) V to vanish.  Conservative exact triangle
bounds exclude all three column pairs.  Swapped 8 and 12 retain mutually
orthogonal isolated left singular vectors and hence force an exact CKM zero.
"""
import json
from fractions import Fraction as F
from pathlib import Path

import sympy as sp


def slots(mask):
    return [(i, j) for i in range(3) for j in range(3)
            if mask & (1 << (3 * i + j))]


def symbolic_gram(mask, prefix):
    entries = {slot: sp.Symbol(f"{prefix}{slot[0]}{slot[1]}", nonzero=True)
               for slot in slots(mask)}
    matrix = sp.Matrix(3, 3, lambda i, j: entries.get((i, j), 0))
    return sp.simplify(matrix * matrix.conjugate().T)


def isolated_rows(gram):
    return [i for i in range(3)
            if all(gram[i, j] == 0 and gram[j, i] == 0
                   for j in range(3) if j != i)]


mu, md = 119, 84
Hu = symbolic_gram(mu, "u1s_")
Hd = symbolic_gram(md, "d1s_")
assert all(Hd[i, j] == 0 for i in range(3) for j in range(3) if i != j)
assert Hu[1, 2] == 0 and Hu[2, 1] == 0

# Tab. S2 central values, represented exactly as the printed decimals.
yu, yc, yt = F(704, 100_000_000), F(356, 100_000), F(967, 1000)
Vtd, Vts, Vtb_lo = F(863, 100_000), F(4117, 100_000), F(99, 100)

# For each column pair, lower-bound the top contribution and upper-bound
# each lighter contribution by its full squared Yukawa (|V_ij V_ik| <= 1).
bounds = {
    "ds": yt*yt*Vtd*Vts - yc*yc - yu*yu,
    "db": yt*yt*Vtd*Vtb_lo - yc*yc - yu*yu,
    "sb": yt*yt*Vts*Vtb_lo - yc*yc - yu*yu,
}
assert all(value > 0 for value in bounds.values())

forced_ckm_zeros = {}
for orbit, masks in {8: (118, 85), 12: (220, 85)}.items():
    hu = symbolic_gram(masks[0], f"u{orbit}s_")
    hd = symbolic_gram(masks[1], f"d{orbit}s_")
    iu, id_ = isolated_rows(hu), isolated_rows(hd)
    assert len(iu) == len(id_) == 1 and iu[0] != id_[0]
    forced_ckm_zeros[str(orbit)] = {
        "masks": {"u": masks[0], "d": masks[1]},
        "isolated_up_gauge_row": iu[0],
        "isolated_down_gauge_row": id_[0],
        "overlap": 0,
        "consequence": "one CKM entry vanishes exactly after mass ordering",
    }

out = {
    "status": "proved",
    "scope": "sector-swapped S3^3 orientations 1, 8, and 12",
    "orbit_1_masks": {"u": mu, "d": md},
    "down_gram_diagonal": True,
    "up_gram_forced_zero_pair": [1, 2],
    "physical_constraint":
        "some off-diagonal of V^dagger diag(yu^2,yc^2,yt^2) V vanishes",
    "central_data_triangle_lower_bounds": {
        key: {"exact": f"{value.numerator}/{value.denominator}",
              "decimal": float(value)}
        for key, value in bounds.items()
    },
    "all_three_column_pairs_excluded": True,
    "forced_ckm_zero_orbits": forced_ckm_zeros,
    "conclusion":
        "swapped orientations 1, 8, and 12 cannot reproduce the Tab. S2 central flavor point",
}
target = Path("research/flavor/results/wp10_swapped_exact_obstructions.json")
target.parent.mkdir(parents=True, exist_ok=True)
target.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(json.dumps(out, indent=2))
