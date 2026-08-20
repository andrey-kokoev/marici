"""Phase-aware invariant Jacobians for the four remaining viable classes.

One sector is anti-diagonal and fixes a diagonal Gram basis. For the other
six-link sector use the rephasing-invariant coordinates
  three Gram diagonals,
  three squared off-diagonal magnitudes,
  Im(H01 H12 H20).
Together with the three diagonal-sector Gram eigenvalues this is a square
10-coordinate map from nine positive edge magnitudes and the loop phase.
"""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
SLOTS = [(i, j) for i in range(3) for j in range(3)]


def slots(mask):
    return [s for k, s in enumerate(SLOTS) if mask & (1 << k)]


def unique_cycle(mu, md):
    edges, adj = [], {n: [] for n in range(9)}
    for sec, mask, off in (("u", mu, 3), ("d", md, 6)):
        for i, j in slots(mask):
            idx = len(edges)
            edges.append((sec, i, j, i, off+j))
            adj[i].append(idx); adj[off+j].append(idx)
    alive, deg = set(range(9)), {n: len(adj[n]) for n in adj}
    queue = [n for n in adj if deg[n] == 1]
    while queue:
        n = queue.pop()
        inc = [e for e in adj[n] if e in alive]
        if not inc:
            continue
        e = inc[0]; alive.remove(e)
        a, b = edges[e][3:]; m = b if n == a else a
        deg[m] -= 1
        if deg[m] == 1: queue.append(m)
    return [edges[e][:3] for e in sorted(alive)]


def phase_edge(mu, md):
    cyc = unique_cycle(mu, md)
    downs = sorted((i, j) for sec, i, j in cyc if sec == "d")
    if downs:
        return ("d", *downs[0])
    ups = sorted((i, j) for sec, i, j in cyc if sec == "u")
    return ("u", *ups[0])


def phase_derivative(expr, c, s):
    return sp.diff(expr, c)*(-s) + sp.diff(expr, s)*c


def invariant_map(mu, md):
    mags = sp.symbols("m0:9", positive=True)
    c, s = sp.symbols("c s", real=True)
    keys = [("u", *slot) for slot in slots(mu)] + [
            ("d", *slot) for slot in slots(md)]
    assert len(keys) == 9
    p_edge = phase_edge(mu, md)
    Yu, Yd = sp.zeros(3), sp.zeros(3)
    for mag, key in zip(mags, keys):
        val = mag*(c+sp.I*s) if key == p_edge else mag
        sector, i, j = key
        (Yu if sector == "u" else Yd)[i, j] = val
    Hu = sp.simplify(Yu*Yu.conjugate().T)
    Hd = sp.simplify(Yd*Yd.conjugate().T)
    # Identify the anti-diagonal sector by its three edges.
    base, moving = (Hu, Hd) if len(slots(mu)) == 3 else (Hd, Hu)
    coords = [sp.re(base[i, i]) for i in range(3)]
    coords += [sp.re(moving[i, i]) for i in range(3)]
    coords += [sp.expand_complex(moving[i,j]*sp.conjugate(moving[i,j]))
               for i, j in ((0,1), (0,2), (1,2))]
    triple = sp.expand_complex(moving[0,1]*moving[1,2]*moving[2,0])
    coords.append(sp.im(triple))
    coords = [sp.simplify(x) for x in coords]
    jac = sp.zeros(10, 10)
    for i, expr in enumerate(coords):
        for j, mag in enumerate(mags):
            jac[i,j] = sp.diff(expr, mag)
        jac[i,9] = phase_derivative(expr, c, s)
    det = sp.factor(jac.det())
    # Reduce powers of c using c^2=1-s^2 for a compact unit-circle form.
    reduced = sp.factor(sp.rem(
        sp.Poly(det, c), sp.Poly(c**2+s**2-1, c)).as_expr())
    return {
        "phase_edge": p_edge,
        "coordinates": [str(x) for x in coords],
        "jacobian_determinant": str(det),
        "unit_circle_reduced_jacobian": str(reduced),
        "identically_zero": det == 0,
    }


cases = [
    ("original", 0, 84, 95),
    ("original", 2, 84, 221),
    ("sector_swapped", 0, 95, 84),
    ("sector_swapped", 2, 221, 84),
]
records = []
for orientation, orbit, mu, md in cases:
    result = invariant_map(mu, md)
    records.append({"orientation": orientation, "orbit": orbit,
                    "masks": {"u": mu, "d": md}, **result})

out = {
    "schema": "marici.flavor.phase_aware_invariant_jacobians.v1",
    "status": "complete_symbolic_jacobian_audit",
    "coordinate_contract":
        "3 base Gram diagonals + 3 moving Gram diagonals + 3 offdiagonal norms + Im(H01 H12 H20)",
    "case_count": len(records),
    "generic_full_rank_count": sum(not r["identically_zero"] for r in records),
    "records": records,
}
(RESULTS / "wp10_phase_aware_invariant_jacobians.json").write_text(
    json.dumps(out, indent=2)+"\n", encoding="utf-8")
print(json.dumps({**out, "records": [
    {k:v for k,v in r.items() if k != "coordinates"} for r in records]}, indent=2))
