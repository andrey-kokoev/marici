#!/usr/bin/env python3
"""WP21c: census of the a1 Vandermonde cancellation over all unique
nine-link textures present in the WP15b viable minima.

For each unique (mask_u, mask_d, phase_edge) among stored viable
minima (chi2 < 4), extract symbolic a1 (support {+-1} confirmed),
factor it as M * B with M the monomial gcd, and test whether the
alternating bracket B is absorbed by Vandermonde factors:
    Du^2 / B^2 polynomial?   Dd^2 / B^2 polynomial?
    (Du^2 * Dd^2) / B^2 polynomial?
(Du^2, Dd^2 are the discriminants of the Hu / Hd characteristic
polynomials, hence polynomials in the squared edge magnitudes.)

Method (WP21c v2, fixes the v1 PolynomialError bug): v1 divided with
squared generators (s**2) via sp.div, which raises PolynomialError
("contains an element of the set of generators") for every texture --
a mechanical artifact, not a scientific result. v2 instead computes
q = sp.cancel(D2 / B**2) and declares absorption iff sp.Poly(q, *mags)
builds without error (q is then a polynomial in the raw magnitudes).

A parity pre-check records whether B is even in every variable (as
expected when the loop edges carry odd total degree in a1 and M
strips exactly one power of each); textures failing it are flagged as
oddballs, not forced.

Numerical confirmation per texture: at a random exact-rational
positive point, report |a1|/(Du Dd) and |a1|.

Reads: results/wp15b_dense_orbit*.json
Writes: results/wp21c_a1_cancellation_census.json
"""
import glob, json, math, random
import sympy as sp

z = sp.symbols("z")


def texture_sym(mask, phase_sector, phase_slot, prefix):
    """Build symbolic Y with distinct magnitude symbols; phase edge * z."""
    syms = {}
    entries = []
    for bit in range(9):
        if mask >> bit & 1:
            i, j = divmod(bit, 3)
            s = sp.symbols(f"{prefix}{i}{j}", positive=True)
            entries.append((i, j, s))
    M = sp.zeros(3)
    for i, j, s in entries:
        M[i, j] = s * z if (prefix == phase_sector and (i, j) == phase_slot) else s
    return M, entries


def sector_data(Y):
    Yc = Y.conjugate()
    for i in range(3):
        for j in range(3):
            Yc[i, j] = Yc[i, j].subs(sp.conjugate(z), 1 / z)
    return Y * Yc.T


def discriminant3(H, lam):
    ch = sp.Poly(H.charpoly(lam).as_expr(), lam)
    return sp.expand(sp.discriminant(ch, lam))


def quotient_is_polynomial(D2, B, mags):
    """Return (flag, cofactor_str): True iff cancel(D2/B**2) is a polynomial."""
    q = sp.cancel(D2 / B**2)
    try:
        sp.Poly(q, *mags)
    except Exception:
        return False, None
    s = str(q)
    return True, (s if len(s) <= 300 else s[:300] + "...<truncated>")


def analyze(mask_u, mask_d, phase_edge):
    Yu, ue = texture_sym(mask_u, "u", None, "u")
    Yd, de = texture_sym(mask_d, "d", None, "d")
    psec, pi, pj = phase_edge
    # re-mark phase edge
    for M, entries, pfx in ((Yu, ue, "u"), (Yd, de, "d")):
        for i, j, s in entries:
            if pfx == psec and (i, j) == (pi, pj):
                M[i, j] = s * z
    Hu = sector_data(Yu)
    Hd = sector_data(Yd)
    C = Hu * Hd - Hd * Hu
    detC = sp.expand(C.det())
    poly = sp.Poly(sp.expand(detC * z), z)
    terms = [(e - 1, c) for (e,), c in poly.terms()]
    support = sorted(e for e, _ in terms)
    if support != [-1, 1]:
        return {"support": support, "anomaly": "support not {+-1}"}
    a1 = sp.expand(next(c for e, c in terms if e == 1))
    mags = [s for _, _, s in ue] + [s for _, _, s in de]
    p = sp.Poly(a1, *mags)
    tms = p.terms()
    # monomial gcd
    gmin = [min(m[i] for m, _ in tms) for i in range(len(mags))]
    M = sp.prod(s ** g for s, g in zip(mags, gmin))
    B = sp.expand(a1 / M)
    nB = len(sp.Poly(B, *mags).terms()) if B != 0 else 0
    out = {
        "support": support,
        "monomial_M": str(M),
        "bracket_monomial_count": nB,
        "bracket_degree": int(sum(sp.Poly(B, *mags).terms()[0][0])) if nB else 0,
    }
    # parity pre-check: is B even in every variable?
    if nB:
        parities = {tuple(e % 2 for e in m) for m, _ in sp.Poly(B, *mags).terms()}
        out["bracket_even_all_vars"] = (parities == {(0,) * len(mags)})
    lam = sp.symbols("lam")
    if B == 0:
        out["anomaly"] = "zero bracket"
        return out
    D2s = {}
    for sector, H in (("u", Hu), ("d", Hd)):
        D2 = discriminant3(H, lam)
        D2s[sector] = D2
        flag, cof = quotient_is_polynomial(D2, B, mags)
        out[f"D{sector}2_over_B2_polynomial"] = flag
        if flag and cof is not None:
            out[f"D{sector}2_cofactor"] = cof
    if not (out["Du2_over_B2_polynomial"] or out["Dd2_over_B2_polynomial"]):
        # combined test: maybe B splits across the two sectors
        flag, cof = quotient_is_polynomial(D2s["u"] * D2s["d"], B, mags)
        out["Du2Dd2_over_B2_polynomial"] = flag
        if flag and cof is not None:
            out["Du2Dd2_cofactor"] = cof
    # numeric confirmation at random exact rationals
    random.seed(hash((mask_u, mask_d, psec, pi, pj)) & 0xFFFF)
    vals = {s: sp.Rational(random.randint(1, 9), random.randint(1, 9))
            for s in mags}
    import numpy as np
    zval = sp.Rational(3, 5) + sp.Rational(4, 5) * sp.I  # exact point on unit circle
    Hun = np.array(Hu.subs(vals).subs(z, zval).evalf(30).tolist()).astype(complex)
    Hdn = np.array(Hd.subs(vals).subs(z, zval).evalf(30).tolist()).astype(complex)
    def vand(H):
        ev = np.linalg.eigvalsh(H)
        return abs((ev[0]-ev[1]) * (ev[0]-ev[2]) * (ev[1]-ev[2]))
    lhs = abs(float(a1.subs(vals))) / (vand(Hun) * vand(Hdn))
    out["numeric_|a1|/(DuDd)"] = lhs
    out["numeric_|a1|"] = abs(float(a1.subs(vals)))
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
    print(f"unique viable textures: {len(seen)}")
    census = {}
    anomalies = []
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
        if not r.get("bracket_even_all_vars", True):
            anomalies.append(name + ":odd-parity")
        print(f"[{k+1}/{len(seen)}] {name}: M={r.get('monomial_M')} "
              f"Bterms={r.get('bracket_monomial_count')} "
              f"even={r.get('bracket_even_all_vars')} "
              f"Du2abs={r.get('Du2_over_B2_polynomial')} "
              f"Dd2abs={r.get('Dd2_over_B2_polynomial')} "
              f"Dcomb={r.get('Du2Dd2_over_B2_polynomial')}", flush=True)
    absorbed = sum(1 for r in census.values()
                   if r.get("Du2_over_B2_polynomial") or r.get("Dd2_over_B2_polynomial")
                   or r.get("Du2Dd2_over_B2_polynomial"))
    out = {"purpose": "WP21c v2 a1 Vandermonde-cancellation census over unique viable textures "
                      "(cancel+Poly test; v1 sp.div squared-generator bug fixed)",
           "n_textures": len(census), "n_absorbed": absorbed,
           "anomalies": anomalies, "census": census}
    with open("results/wp21c_a1_cancellation_census.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print(f"absorbed {absorbed}/{len(census)}; anomalies {anomalies}")
    print("-> results/wp21c_a1_cancellation_census.json")


if __name__ == "__main__":
    main()
