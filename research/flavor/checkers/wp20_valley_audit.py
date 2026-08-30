#!/usr/bin/env python3
"""WP20: per-valley physical16 audit of the WP15b viable minima
(WP19 residual, marici.Figueiredo). Measures for EVERY stored viable
minimum (full theta stored; no re-fitting): chi2 recheck; physical16
sheet distance; WP14b inheritance K/rho_v/identity; detC support;
per-observable phi-sensitivity (sigma units); CKM angles + systematic
small-integer combo scan (a scan, NOT a map); chi2(phi) profiles for
class representatives (bowl vs trench).
Reads: results/wp15b_dense_orbit*.json,
       results/wp15b_dense_class_reduction.json,
       results/wp19b_valley_coverage.json
Writes: results/wp20_valley_audit.json
"""
import glob, json, math, sys
from collections import defaultdict
import numpy as np
from scipy.optimize import least_squares
sys.path.insert(0, "checkers")
import wp7_ensemble as wp7
from wp18a_branch_derivation import ROOT_A, ROOT_B
from wp18_branch_resolved_fibers import physical16
np.seterr(all="ignore")
WINDOWS = [22.5, 45.0, 67.5, 90.0]

def sheet_images():
    mu, md = 85, 234
    ps, slot = wp7.paper_phase_edge(mu, md)
    return {n: physical16(*wp7.build_texture(mu, md, ps, slot, np.array(r)))
            for n, r in (("small_cos_pos", ROOT_A), ("large_cos_neg", ROOT_B))}
IMG = sheet_images()

def build(member, pe, log_mags, phi):
    return wp7.build_texture(member[0], member[1], pe[0], (pe[1], pe[2]),
                             np.concatenate([log_mags, [phi]]))

def sheet_distance(Yu, Yd):
    img = physical16(Yu, Yd)
    return {n: float(np.max(np.abs(img - ref) / np.maximum(np.abs(ref), 1e-12)))
            for n, ref in IMG.items()}

def prod_delta(ev):
    return abs((ev[0]-ev[1]) * (ev[0]-ev[2]) * (ev[1]-ev[2]))

def invariants(Yu, Yd, phi):
    Hu = Yu @ Yu.conj().T; Hd = Yd @ Yd.conj().T
    su2, Uu = np.linalg.eigh(Hu); sd2, Ud = np.linalg.eigh(Hd)
    V = Uu.conj().T @ Ud
    J = (V[0,1]*V[1,2]*V[0,2].conj()*V[1,1].conj()).imag
    Du, Dd = prod_delta(su2), prod_delta(sd2)
    C = Hu @ Hd - Hd @ Hu
    detC = np.trace(C @ C @ C) / 3.0
    K = detC / (2j * math.sin(phi))
    rho = (K.real**2) / (Du**2 * Dd**2)
    err = abs(J**2 - rho*math.sin(phi)**2) / max(J**2, 1e-300)
    return {"J": float(J), "Du": float(Du), "Dd": float(Dd),
            "K_real": float(K.real),
            "K_imag_over_K": float(abs(K.imag)/max(abs(K), 1e-300)),
            "rho_v": float(rho), "identity_rel_err": float(err)}

def detC_at(member, pe, log_mags, phi):
    Yu, Yd = build(member, pe, log_mags, phi)
    Hu = Yu @ Yu.conj().T; Hd = Yd @ Yd.conj().T
    C = Hu @ Hd - Hd @ Hu
    return np.trace(C @ C @ C) / 3.0

def support_check(member, pe, log_mags):
    a1 = detC_at(member, pe, log_mags, math.pi/2) / 2j
    d0 = detC_at(member, pe, log_mags, 0.0)
    d4 = detC_at(member, pe, log_mags, math.pi/4)
    s = max(abs(a1), 1e-300)
    return {"a1_imag_over_a1": float(abs(a1.imag)/s),
            "detC0_rel": float(abs(d0)/s),
            "detC_pi4_consistency_rel": float(abs(d4 - 2j*a1*math.sin(math.pi/4))/s)}

def angles(Yu, Yd):
    su2, Uu = np.linalg.eigh(Yu @ Yu.conj().T)
    sd2, Ud = np.linalg.eigh(Yd @ Yd.conj().T)
    V = Uu.conj().T @ Ud
    def ang(num, den):
        r = -num/den
        a = math.degrees(math.atan2(r.imag, r.real)) % 360.0
        return a if a <= 180.0 else 360.0 - a
    return (ang(V[2,0]*V[2,2].conj(), V[0,0]*V[0,2].conj()),
            ang(V[1,0]*V[1,2].conj(), V[2,0]*V[2,2].conj()),
            ang(V[0,0]*V[0,2].conj(), V[1,0]*V[1,2].conj()))

def fold_deg(x):
    x = math.fmod(x, 180.0)
    if x < 0: x += 180.0
    return min(x, 180.0 - x)

COMBOS = {f"{a}a{b:+d}b{c:+d}g{k:+d}q": (a,b,c,k)
          for a in range(-2,3) for b in range(-2,3)
          for c in range(-2,3) for k in range(-2,3) if (a,b,c)!=(0,0,0)}

def best_combos(phi_deg, alpha, beta, gamma, top=3):
    res = sorted((abs(phi_deg - fold_deg(a*alpha+b*beta+c*gamma+k*90.0)), n)
                 for n,(a,b,c,k) in COMBOS.items())
    return [{"distance_deg": round(d,4), "combo": n} for d,n in res[:top]]

def phi_sensitivity(member, pe, log_mags, phi, h=0.02):
    def obs_at(p):
        Yu, Yd = build(member, pe, log_mags, p)
        o = wp7.observables17(Yu, Yd)
        return np.where(np.isfinite(o), o, np.nan)
    sig = (obs_at(phi+h)-obs_at(phi-h))/(2.0*h)/wp7.SIGMA
    names = [n for n,_,_ in wp7.OBS17]
    return [{"observable": names[i], "d_obs_d_phi_sigma": float(sig[i])}
            for i in np.argsort(-np.abs(sig))[:3]]

def chi2_of(member, pe, theta):
    Yu, Yd = wp7.build_texture(member[0], member[1], pe[0], (pe[1], pe[2]), theta)
    o = wp7.observables17(Yu, Yd)
    o = np.where(np.isfinite(o), o, 1.0e6)
    return float(np.sum(((o - wp7.CENTRAL)/wp7.SIGMA)**2))

def profile(member, pe, log_mags, phi0):
    out = {}
    for dg in (-6,-4,-2,-1,0,1,2,4,6):
        p = phi0 + math.radians(dg)
        def resid(m9):
            Yu, Yd = wp7.build_texture(member[0], member[1], pe[0], (pe[1], pe[2]),
                                       np.concatenate([m9, [p]]))
            o = wp7.observables17(Yu, Yd)
            o = np.where(np.isfinite(o), o, 1.0e6)
            return (o - wp7.CENTRAL)/wp7.SIGMA
        try:
            sol = least_squares(resid, np.array(log_mags), method="lm",
                                ftol=1e-12, xtol=1e-12, gtol=1e-12, max_nfev=800)
            out[str(dg)] = float(2.0*sol.cost)
        except Exception:
            out[str(dg)] = None
    return out

def main():
    w19b = json.load(open("results/wp19b_valley_coverage.json"))
    pinned_of = {int(k): (v.get("pinned_deg") or []) for k,v in w19b["per_orbit"].items()}
    w15 = json.load(open("results/wp15b_dense_class_reduction.json"))
    dominant = [c for c in w15["class_table"] if c["chi2_min"] < 4.0]
    records, rep_idx = [], {}
    for path in sorted(glob.glob("results/wp15b_dense_orbit*.json")):
        d = json.load(open(path)); oi = d["orbit_index"]
        for half in d["s3_orbits"]:
            for m in half["member_results"]:
                member = tuple(m["member"])
                for v in m["viable_minima"]:
                    if v["chi2"] >= 4.0: continue
                    pe = v["phase_edge"]; lm = np.array(v["log_mags"]); phi = float(v["phi"])
                    pf = math.degrees(wp7.fold_phi(phi))
                    Yu, Yd = build(member, pe, lm, phi)
                    inv = invariants(Yu, Yd, phi)
                    a,b,g = angles(Yu, Yd)
                    sd = sheet_distance(Yu, Yd); sheet = min(sd, key=sd.get)
                    dp = min((abs(pf-p) for p in pinned_of.get(oi, [])), default=None)
                    records.append({
                        "orbit": oi, "member": list(member), "phase_edge": pe,
                        "chi2_stored": v["chi2"],
                        "chi2_recomputed": chi2_of(member, pe, np.concatenate([lm,[phi]])),
                        "phi_folded_deg": pf,
                        "valley_kind": ("exact" if dp is not None and dp <= 0.3 else "extra"),
                        "sheet": sheet, "sheet_rel_distance": sd[sheet],
                        "J": inv["J"], "rho_v": inv["rho_v"],
                        "identity_rel_err": inv["identity_rel_err"],
                        "K_imag_over_K": inv["K_imag_over_K"],
                        "support": support_check(member, pe, lm),
                        "ut_angles_deg": {"alpha": a, "beta": b, "gamma": g},
                        "window_distance_deg": min(abs(pf-w) for w in WINDOWS),
                        "best_combos": best_combos(pf, a, b, g),
                        "phi_sensitivity_top3": phi_sensitivity(member, pe, lm, phi),
                        "log_mags": lm.tolist(), "phi_raw": phi})
                    idx = len(records)-1
                    for c in dominant:
                        if (c["orbit_index"] == oi
                                and abs(math.degrees(c["phi_folded"]) - pf) < 0.5
                                and abs(c["chi2_min"] - v["chi2"]) < 0.5):
                            rep_idx.setdefault((oi, round(pf,1)), idx)
    prof = {f"orbit{oi}|phi{pdeg}": {"record_index": idx,
                "profile_chi2": profile(tuple(records[idx]["member"]),
                                        records[idx]["phase_edge"],
                                        records[idx]["log_mags"],
                                        records[idx]["phi_raw"])}
            for (oi,pdeg), idx in sorted(rep_idx.items())}
    ident_max = max(r["identity_rel_err"] for r in records)
    sup_max = max(max(r["support"]["detC0_rel"], r["support"]["detC_pi4_consistency_rel"])
                  for r in records)
    sheets, kinds = defaultdict(int), defaultdict(int)
    for r in records:
        sheets[r["sheet"]] += 1; kinds[r["valley_kind"]] += 1
    out = {"purpose": "WP20 per-valley physical16 audit of all stored WP15b viable minima (WP19 residual)",
           "n_minima_audited": len(records),
           "sheet_counts": dict(sheets), "valley_kind_counts": dict(kinds),
           "inheritance_identity_max_rel_err": ident_max,
           "support_check_max_rel": sup_max,
           "records": records, "class_profiles": prof}
    dest = "results/wp20_valley_audit.json"
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print(f"audited {len(records)} minima; sheets {dict(sheets)}; kinds {dict(kinds)}")
    print(f"identity max rel err {ident_max:.2e}; support max rel {sup_max:.2e}")
    print("profiles:", len(prof)); print("->", dest)

if __name__ == "__main__":
    main()
