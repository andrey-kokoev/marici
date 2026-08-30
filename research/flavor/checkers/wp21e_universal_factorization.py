#!/usr/bin/env python3
"""WP21e: universal a1 factorization certificate over all 755 unique
viable nine-link textures.

Census findings (WP21c v2 + divisibility extension):
  * detC support is {z^+1, z^-1} everywhere (WP16 theorem, rechecked).
  * a1 = M * B with M the monomial gcd.
  * Exactly one sector is row-sharing decomposable in this ensemble:
      - (2+1) blocks: Du_sec = sqrt(disc_b) * |chi_b(s)| exactly, where
        chi_b is the char poly of the 2x2 block and s the singleton
        diagonal entry (its eigenvalue). B is ALWAYS divisible by
        chi_b(s): B = +/-chi_b(s) * W with W a +/-1-coefficient
        alternating quadratic form in the OTHER sector's squared
        magnitudes (1, 2 or 3 terms).
      - diagonal (3 blocks): D_sec = |g01 g02 g12| with gap polys
        g_ab = H_aa - H_bb; B = +/- product of a subset of the gaps
        (possibly times a residual W; recorded if present).
  * Hence universally:  a1/(Du Dd) = M * W / (sqrt(disc_b) * D_other)
    (2+1 case)   or   M * W / (prod remaining gaps * D_other)
    (diagonal case).

This checker certifies each step per texture, symbolically where
feasible, and numerically at one random exact-rational point.

Reads: results/wp15b_dense_orbit*.json
Writes: results/wp21e_universal_factorization.json
"""
import glob, json, math, random
import sympy as sp

z = sp.symbols("z")
lam = sp.symbols("lam")


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


def blocks_of(mask):
    import collections
    cols = collections.defaultdict(set)
    for bit in range(9):
        if mask >> bit & 1:
            i, j = divmod(bit, 3)
            cols[j].add(i)
    parent = list(range(3))
    def find(x):
        while parent[x] != x: parent[x] = parent[parent[x]]; x = parent[x]
        return x
    for rows in cols.values():
        rows = list(rows)
        for r in rows[1:]:
            parent[find(rows[0])] = find(r)
    comp = {}
    for i in range(3):
        comp.setdefault(find(i), []).append(i)
    return sorted(comp.values(), key=len)


def is_poly(q, mags):
    try:
        sp.Poly(q, *mags)
        return True
    except Exception:
        return False


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
    terms = [(e - 1, cc) for (e,), cc in poly.terms()]
    support = sorted(e for e, _ in terms)
    if support != [-1, 1]:
        return {"anomaly": f"support {support}"}
    a1 = sp.expand(next(cc for e, cc in terms if e == 1))
    mags = [s for _, _, s in ue] + [s for _, _, s in de]
    tms = sp.Poly(a1, *mags).terms()
    gmin = [min(m[i] for m, _ in tms) for i in range(len(mags))]
    Mn = sp.prod(s ** g for s, g in zip(mags, gmin))
    B = sp.expand(a1 / Mn)
    out = {"support": support, "monomial_M": str(Mn)}

    bu, bd = blocks_of(mu), blocks_of(md)
    out["u_blocks"] = [len(b) for b in bu]
    out["d_blocks"] = [len(b) for b in bd]
    if len(bu) >= 2 and len(bd) >= 2:
        return {**out, "anomaly": "both sectors decomposable (unexpected)"}
    if len(bu) == 1 and len(bd) == 1:
        return {**out, "anomaly": "no decomposable sector"}
    sec, H, bl = ("u", Hu, bu) if len(bu) >= 2 else ("d", Hd, bd)
    Hother = Hd if sec == "u" else Hu
    out["decomposed_sector"] = sec

    if len(bl) == 2:  # 2+1 block structure
        sing = [b[0] for b in bl if len(b) == 1][0]
        blk = [b for b in bl if len(b) == 2][0]
        Hb = H.extract(blk, blk)
        chib = sp.Poly(Hb.charpoly(lam).as_expr(), lam)
        chi_at_s = sp.expand(chib.as_expr().subs(lam, H[sing, sing]))
        # Vandermonde identity: D_sec^2 = disc_b * chi_b(s)^2
        disc_b = sp.expand(sp.discriminant(chib, lam))
        D2 = sp.expand(sp.discriminant(sp.Poly(H.charpoly(lam).as_expr(), lam), lam))
        ident = sp.expand(D2 - disc_b * chi_at_s**2)
        out["vandermonde_identity_exact"] = bool(ident == 0)
        # B divisibility
        q = sp.cancel(B / chi_at_s)
        if not is_poly(q, mags):
            return {**out, "anomaly": "B not divisible by chi_b(s)"}
        qp = sp.Poly(q, *mags)
        out["W"] = str(sp.expand(q))
        out["W_terms"] = len(qp.terms())
        coeffs = {str(cc) for _, cc in qp.terms()}
        out["W_coeffs"] = sorted(coeffs)
        out["factorization_type"] = "block21"
        out["reduced_form"] = "a1/(Du Dd) = M*W/(sqrt(disc_b)*D_other)"
        # numeric verification (retry over seeds to dodge degenerate points)
        import numpy as np
        def vand(Hn):
            ev = np.linalg.eigvalsh(Hn)
            return abs((ev[0]-ev[1]) * (ev[0]-ev[2]) * (ev[1]-ev[2]))
        zval = sp.Rational(3, 5) + sp.Rational(4, 5) * sp.I
        rel = None
        for trial in range(10):
            random.seed((hash((mu, md, pe)) & 0xFFFF) + trial)
            vals = {s: sp.Rational(random.randint(1, 9), random.randint(1, 9)) for s in mags}
            wv = float(q.subs(vals))
            gv = float(disc_b.subs(vals))
            if wv == 0 or gv <= 0:
                continue
            Hun = np.array(Hu.subs(vals).subs(z, zval).evalf(30).tolist()).astype(complex)
            Hdn = np.array(Hd.subs(vals).subs(z, zval).evalf(30).tolist()).astype(complex)
            Du, Dd = vand(Hun), vand(Hdn)
            lhs = abs(float(a1.subs(vals))) / (Du * Dd)
            if lhs == 0:
                continue
            gap = math.sqrt(gv)
            Do = Dd if sec == "u" else Du
            rhs = abs(float(Mn.subs(vals)) * wv) / (gap * Do)
            rel = abs(lhs - rhs) / lhs
            break
        out["numeric_rel_err"] = rel
    else:  # diagonal sector (3 blocks)
        gaps = {(a, b): sp.expand(H[a, a] - H[b, b]) for a, b in ((0, 1), (0, 2), (1, 2))}
        D2 = sp.expand(sp.discriminant(sp.Poly(H.charpoly(lam).as_expr(), lam), lam))
        ident = sp.expand(D2 - gaps[(0, 1)]**2 * gaps[(0, 2)]**2 * gaps[(1, 2)]**2)
        out["vandermonde_identity_exact"] = bool(ident == 0)
        # find gap subset dividing B (largest first), allow residual W
        found = None
        import itertools
        for r in (3, 2, 1):
            for S in itertools.combinations([(0, 1), (0, 2), (1, 2)], r):
                prod = sp.prod(gaps[g] for g in S)
                q = sp.cancel(B / prod)
                if is_poly(q, mags):
                    found = (S, sp.expand(q))
                    break
            if found: break
        if not found:
            return {**out, "anomaly": "no gap subset divides B"}
        S, W = found
        out["gap_subset_dividing_B"] = [list(g) for g in S]
        out["W"] = str(W)
        out["W_terms"] = len(sp.Poly(W, *mags).terms()) if W != 0 else 0
        out["factorization_type"] = "diagonal"
        remaining = [g for g in ((0, 1), (0, 2), (1, 2)) if g not in S]
        out["reduced_form"] = "a1/(Du Dd) = M*W/(prod remaining gaps * D_other)"
        import numpy as np
        def vand(Hn):
            ev = np.linalg.eigvalsh(Hn)
            return abs((ev[0]-ev[1]) * (ev[0]-ev[2]) * (ev[1]-ev[2]))
        zval = sp.Rational(3, 5) + sp.Rational(4, 5) * sp.I
        lhs = None
        for trial in range(10):
            random.seed((hash((mu, md, pe)) & 0xFFFF) + trial)
            vals = {s: sp.Rational(random.randint(1, 9), random.randint(1, 9)) for s in mags}
            if float(W.subs(vals)) == 0:
                continue
            Hun = np.array(Hu.subs(vals).subs(z, zval).evalf(30).tolist()).astype(complex)
            Hdn = np.array(Hd.subs(vals).subs(z, zval).evalf(30).tolist()).astype(complex)
            Du, Dd = vand(Hun), vand(Hdn)
            lhs = abs(float(a1.subs(vals))) / (Du * Dd)
            if lhs == 0:
                continue
            rem = 1.0
            for g in remaining:
                rem *= abs(float(gaps[g].subs(vals)))
            if rem == 0:
                continue
            break
        Do = Dd if sec == "u" else Du
        rhs = abs(float(Mn.subs(vals)) * float(W.subs(vals))) / (rem * Do)
        out["numeric_rel_err"] = (abs(lhs - rhs) / lhs) if lhs else None
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
                    key = (mu, md, tuple(v["phase_edge"]))
                    seen.setdefault(key, v["chi2"])
    print(f"unique viable textures: {len(seen)}", flush=True)
    census, anomalies = {}, []
    for k, (mu, md, pe) in enumerate(sorted(seen)):
        name = f"{mu}_{md}_{pe[0]}{pe[1]}{pe[2]}"
        try:
            r = analyze(mu, md, pe)
        except Exception as e:
            r = {"error": f"{type(e).__name__}: {e}"}
        r["min_chi2"] = seen[(mu, md, pe)]
        census[name] = r
        if "error" in r or "anomaly" in r:
            anomalies.append(name)
        if (k + 1) % 50 == 0:
            print(f"{k+1}/{len(seen)}", flush=True)
    import collections
    type_counts = collections.Counter(r.get("factorization_type") for r in census.values())
    w_counts = collections.Counter(r.get("W_terms") for r in census.values())
    ident_fail = [k for k, r in census.items() if r.get("vandermonde_identity_exact") is False]
    max_rel = max((r.get("numeric_rel_err", 0) for r in census.values()), default=None)
    out = {
        "purpose": "WP21e universal a1=M*chi_b(s)*W factorization certificate",
        "n_textures": len(census),
        "factorization_type_counts": dict(type_counts),
        "W_term_counts": dict(w_counts),
        "vandermonde_identity_failures": ident_fail,
        "numeric_rel_err_max": max_rel,
        "anomalies": anomalies,
        "census": census,
    }
    with open("results/wp21e_universal_factorization.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print("types:", dict(type_counts))
    print("W terms:", dict(w_counts))
    print("identity failures:", len(ident_fail), "max rel err:", max_rel)
    print("anomalies:", anomalies)
    print("-> results/wp21e_universal_factorization.json")


if __name__ == "__main__":
    main()
