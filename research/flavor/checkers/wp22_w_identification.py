#!/usr/bin/env python3
"""WP22: identification of W and the complete structural classification
of the first-harmonic amplitude a1 on the viable ensemble.

WP21e showed a1 = M * chi_b(s) * W universally (755/755). WP22
identifies W and certifies the full classification per texture:

  * diagonal decomposed sector (73): B = +- g01 g02 g12
    (full gap product = +- D_sec).
  * block21, 4-cycle, singleton off cycle (398): B = +- chi_b(s).
  * block21, 4-cycle, singleton off cycle, connected sector has
    exactly 2 leaf columns and none attaches to the singleton row
    (50): B = +- chi_b(s) * [(Y+tY)_ll - (Y+tY)_l'l'],
    the two leaf-column norm difference of the connected sector.
  * block21, 6-cycle, singleton on cycle (234):
    B = +- chi_b(s) * [H_ii - H_jj], where {i,j} are the two Q-rows
    touched by the decomposed sector's cycle edges.

The checker computes the graph data per texture, constructs the
predicted F by this rule, and verifies B = +-F symbolically.

Reads: results/wp15b_dense_orbit*.json
Writes: results/wp22_w_identification.json
"""
import glob, json, collections, itertools
import sympy as sp

z = sp.symbols("z")
lam = sp.symbols("lam")
SLOTS = [(i, j) for i in range(3) for j in range(3)]


def mask_slots(mask):
    return [s for k, s in enumerate(SLOTS) if mask & (1 << k)]


def texture_sym(mask, prefix):
    entries = []
    for bit in range(9):
        if mask >> bit & 1:
            i, j = divmod(bit, 3)
            entries.append((i, j, sp.symbols(f"{prefix}{i}{j}", positive=True)))
    M = sp.zeros(3)
    for i, j, s in entries:
        M[i, j] = s
    return M, entries


def sector_data(Y):
    Yc = Y.conjugate()
    for i in range(3):
        for j in range(3):
            Yc[i, j] = Yc[i, j].subs(sp.conjugate(z), 1 / z)
    return Y * Yc.T


def blocks_of(slots):
    cols = collections.defaultdict(set)
    for i, j in slots:
        cols[j].add(i)
    parent = list(range(3))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    for rows in cols.values():
        rows = list(rows)
        for r in rows[1:]:
            parent[find(rows[0])] = find(r)
    comp = {}
    for i in range(3):
        comp.setdefault(find(i), []).append(i)
    return sorted(comp.values(), key=len)


def cycle_nodes(mu, md):
    adj = collections.defaultdict(set)
    for i, j in mask_slots(mu):
        adj[('Q', i)].add(('u', j)); adj[('u', j)].add(('Q', i))
    for i, j in mask_slots(md):
        adj[('Q', i)].add(('d', j)); adj[('d', j)].add(('Q', i))
    removed, stack = set(), [n for n in adj if len(adj[n]) == 1]
    adj2 = {n: set(s) for n, s in adj.items()}
    while stack:
        n = stack.pop()
        if n in removed:
            continue
        removed.add(n)
        for m in adj2[n]:
            adj2[m].discard(n)
            if len(adj2[m]) == 1:
                stack.append(m)
    return {n for n in adj if n not in removed}


def analyze(mu, md, pe):
    Yu, ue = texture_sym(mu, "u")
    Yd, de = texture_sym(md, "d")
    for M, entries, pfx in ((Yu, ue, "u"), (Yd, de, "d")):
        for i, j, s in entries:
            if pfx == pe[0] and (i, j) == (pe[1], pe[2]):
                M[i, j] = s * z
    Hu, Hd = sector_data(Yu), sector_data(Yd)
    C = Hu * Hd - Hd * Hu
    detC = sp.expand(C.det())
    poly = sp.Poly(sp.expand(detC * z), z)
    terms = [(e - 1, cc) for (e,), cc in poly.terms() if cc != 0]
    if detC == 0:
        return {"anomaly": "detC_zero"}
    if sorted(e for e, _ in terms) != [-1, 1]:
        return {"anomaly": "support"}
    a1 = sp.expand(next(cc for e, cc in terms if e == 1))
    mags = [s for _, _, s in ue] + [s for _, _, s in de]
    tms = sp.Poly(a1, *mags).terms()
    gmin = [min(m[i] for m, _ in tms) for i in range(len(mags))]
    Mn = sp.prod(s ** g for s, g in zip(mags, gmin))
    B = sp.expand(a1 / Mn)

    uslots, dslots = mask_slots(mu), mask_slots(md)
    bu, bd = blocks_of(uslots), blocks_of(dslots)
    sec, H, bl, dec_slots, con_slots, con_pfx = (
        ("u", Hu, bu, uslots, dslots, "d") if len(bu) >= 2
        else ("d", Hd, bd, dslots, uslots, "u"))
    dec_pfx = sec
    cyc = cycle_nodes(mu, md)
    out = {"decomposed_sector": sec, "cycle_nodes": len(cyc)}

    if len(bl) == 3:  # diagonal
        g = {(a, b): sp.expand(H[a, a] - H[b, b])
             for a, b in ((0, 1), (0, 2), (1, 2))}
        F = g[(0, 1)] * g[(0, 2)] * g[(1, 2)]
        out["class"] = "diagonal"
    else:
        sing = [b[0] for b in bl if len(b) == 1][0]
        blk = [b for b in bl if len(b) == 2][0]
        Hb = H.extract(blk, blk)
        chib = sp.Poly(Hb.charpoly(lam).as_expr(), lam)
        chi_at_s = sp.expand(chib.as_expr().subs(lam, H[sing, sing]))
        con_syms = {(i, j): sp.symbols(f"{con_pfx}{i}{j}", positive=True)
                    for i, j in con_slots}
        if len(cyc) == 6:  # 6-cycle: row-norm diff of dec-cycle-touched rows
            touched = sorted({i for i, j in dec_slots
                              if ('Q', i) in cyc and (dec_pfx, j) in cyc})
            assert len(touched) == 2
            i, j = touched
            Hi = sum(s**2 for (r, cc), s in con_syms.items() if r == i)
            Hj = sum(s**2 for (r, cc), s in con_syms.items() if r == j)
            W = Hi - Hj
            out["class"] = "6cycle_row_diff"
            out["touched_rows"] = touched
        else:  # 4-cycle
            coldeg = collections.Counter(j for i, j in con_slots)
            leafcols = sorted(j for j in range(3) if coldeg.get(j, 0) == 1)
            leaf_attach = {i for i, j in con_slots if j in leafcols}
            if len(leafcols) == 2 and sing not in leaf_attach:
                l1, l2 = leafcols
                G1 = sum(s**2 for (r, cc), s in con_syms.items() if cc == l1)
                G2 = sum(s**2 for (r, cc), s in con_syms.items() if cc == l2)
                W = G1 - G2
                out["class"] = "4cycle_leafcol_diff"
                out["leaf_cols"] = leafcols
            else:
                W = sp.Integer(1)
                out["class"] = "4cycle_trivial"
        F = chi_at_s * W
    if sp.expand(B - F) == 0:
        out["sign"] = +1
    elif sp.expand(B + F) == 0:
        out["sign"] = -1
    else:
        out["anomaly"] = "B != +-F"
        out["B_minus_F"] = str(sp.expand(B - F))[:200]
    return out


def main():
    seen = {}
    for path in sorted(glob.glob("results/wp15b_dense_orbit*.json")):
        d = json.load(open(path))
        for half in d["s3_orbits"]:
            for m in half["member_results"]:
                mu, md = m["member"]
                for v in m["viable_minima"]:
                    if v["chi2"] >= 4.0:
                        continue
                    seen.setdefault((mu, md, tuple(v["phase_edge"])), v["chi2"])
    print(f"unique viable textures: {len(seen)}", flush=True)
    census, anomalies = {}, []
    class_counts = collections.Counter()
    for k, (mu, md, pe) in enumerate(sorted(seen)):
        name = f"{mu}_{md}_{pe[0]}{pe[1]}{pe[2]}"
        try:
            r = analyze(mu, md, pe)
        except Exception as e:
            r = {"error": f"{type(e).__name__}: {e}"}
        census[name] = r
        class_counts[r.get("class", "ERROR")] += 1
        if "error" in r or "anomaly" in r:
            anomalies.append(name)
        if (k + 1) % 100 == 0:
            print(f"{k+1}/{len(seen)}", flush=True)
    verified = sum(1 for r in census.values() if "sign" in r)
    out = {
        "purpose": "WP22 identification of W and complete a1 classification",
        "n_textures": len(census), "n_verified": verified,
        "class_counts": dict(class_counts),
        "anomalies": anomalies, "census": census,
    }
    with open("results/wp22_w_identification.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print("classes:", dict(class_counts))
    print(f"verified {verified}/{len(census)}; anomalies: {anomalies[:10]}")
    print("-> results/wp22_w_identification.json")


if __name__ == "__main__":
    main()
