"""WP29: is the rigid-cluster lnM freeze an exact mass-data syzygy?

WP28 showed lnM is frozen BETWEEN classes in rigid clusters (cluster 2: 1.3e-3,
cluster 1: 0.079) while the constituent edge logs disperse by e^1..e^3. The one
monomial weak-basis invariant per sector is |det Y| = product of the three
Yukawa couplings, so the decisive question: is lnM determined by the
mass-pinned det data alone (exact syzygy, freeze = fit tolerance), or is it an
approximate collective flat direction?

  A. enumerate perfect matchings per sector for all 755 classes; det term count;
  B. numerical floor: per-minimum ln|det Y_u|, ln|det Y_d| from fitted edges;
     per-cluster regression lnM ~ a*lndet_u + b*lndet_d + c over class means;
     residual between-class std vs the det floor (between-class std of the
     lndet's themselves, which measures fit tolerance on mass data);
  C. exact algebra: for classes with single-matching dets in both sectors,
     test whether the M exponent vector is a rational combination of the two
     det exponent vectors; report coefficients when exact;
  D. verdict per cluster: det-determined (residual ~ floor) or not.

Reads: results/wp20_valley_audit.json,
       results/wp21e_universal_factorization.json
Writes: results/wp29_monomial_syzygy.json
Run: ../.venv/Scripts/python checkers/wp29_monomial_syzygy.py
"""
import json, math, collections, os, re, sys, itertools
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wp25_center_selection import mask_slots, tex_key, factor_rows

CENTERS = [23.15067360649863, 43.17287913134288, 46.907137936455435,
           68.38801847180338, 89.57230686320408]

def matchings(mask):
    slots = set(mask_slots(mask))
    out = []
    for p in itertools.permutations(range(3)):
        if all((i, p[i]) in slots for i in range(3)):
            sign = 1 if (p in [(0,1,2),(1,2,0),(2,0,1)]) else -1
            out.append((p, sign))
    return out

def parse_M(mstr):
    vec = collections.Counter()
    for f in re.findall(r"[ud]\d\d(?:\*\*\d+)?", mstr):
        m = re.fullmatch(r"([ud])(\d)(\d)(?:\*\*(\d+))?", f)
        vec[("ud".index(m.group(1)), int(m.group(2)), int(m.group(3)))] += int(m.group(4) or 1)
    return vec

def main():
    wp20 = json.load(open("results/wp20_valley_audit.json"))
    fac = json.load(open("results/wp21e_universal_factorization.json"))["census"]
    recs = [r for r in wp20["records"]
            if fac.get(tex_key(*r["member"], r["phase_edge"]), {}).get("factorization_type")]
    rows = factor_rows(wp20["records"], fac, CENTERS)
    lnM_by_key = collections.defaultdict(list)
    cluster_by_key = {}
    for row in rows:
        lnM_by_key[row["key"]].append(row["lnM"])
        cluster_by_key[row["key"]] = row["cluster"]

    # A + per-class det data
    cls = {}
    for r in recs:
        mu, md = r["member"]; pe = r["phase_edge"]
        key = tex_key(mu, md, pe)
        if key in cls: continue
        mu_, md_ = matchings(mu), matchings(md)
        cls[key] = dict(member=[mu, md], phase_edge=pe,
                        M=fac[key]["monomial_M"], Mvec=parse_M(fac[key]["monomial_M"]),
                        matchings_u=[[list(p), s] for p, s in mu_],
                        matchings_d=[[list(p), s] for p, s in md_])
    term_counts = collections.Counter((len(c["matchings_u"]), len(c["matchings_d"]))
                                      for c in cls.values())

    # B. per-minimum lndet from fitted edges
    lndet = collections.defaultdict(lambda: [[], []])  # key -> [lndet_u list, lndet_d list]
    for r in recs:
        mu, md = r["member"]; pe = r["phase_edge"]
        key = tex_key(mu, md, pe)
        if key not in cls: continue
        us, ds = mask_slots(mu), mask_slots(md)
        logs = r["log_mags"]
        lu = dict(zip(us, logs[:len(us)])); ld = dict(zip(ds, logs[len(us):]))
        for sec, slots_d, mlist, out_i in (("u", lu, cls[key]["matchings_u"], 0),
                                           ("d", ld, cls[key]["matchings_d"], 1)):
            terms = [sum(slots_d[(i, p[i])] for i in range(3)) for p, s in mlist]
            if len(terms) == 1:
                val = terms[0]
            else:  # two terms with opposite signs: log|exp(a)-exp(b)|
                a, b = sorted(terms, reverse=True)
                val = a + math.log(-math.expm1(b - a))
            lndet[key][out_i].append(val)

    # per-cluster regression over class means
    per_cluster = {}
    for cl in range(5):
        keys = [k for k in cls if cluster_by_key.get(k) == cl and lndet[k][0]]
        X, Y = [], []
        for k in keys:
            X.append([np.mean(lndet[k][0]), np.mean(lndet[k][1]), 1.0])
            Y.append(np.mean(lnM_by_key[k]))
        X, Y = np.array(X), np.array(Y)
        coef, *_ = np.linalg.lstsq(X, Y, rcond=None)
        resid = Y - X @ coef
        floor_u = float(np.std(X[:, 0])); floor_d = float(np.std(X[:, 1]))
        per_cluster[str(cl)] = dict(
            n_classes=len(keys), coef=[float(c) for c in coef],
            lnM_between_std=float(np.std(Y)),
            resid_between_std=float(np.std(resid)),
            floor_lndet_u=floor_u, floor_lndet_d=floor_d,
            resid_over_floor=float(np.std(resid) / max(floor_u, floor_d, 1e-12)))

    # C. exact algebra for single-single classes
    exact = []
    for key, c in cls.items():
        if len(c["matchings_u"]) == 1 and len(c["matchings_d"]) == 1:
            du = collections.Counter({(0, i, c["matchings_u"][0][0][i]): 1 for i in range(3)})
            dd = collections.Counter({(1, i, c["matchings_d"][0][0][i]): 1 for i in range(3)})
            mv = c["Mvec"]
            au = {e: mv[e] for e in du if mv.get(e)}
            ad = {e: mv[e] for e in dd if mv.get(e)}
            au_vals = set(au.values()); ad_vals = set(ad.values())
            ok = (len(au) == 3 and len(au_vals) == 1 and len(ad) == 3 and len(ad_vals) == 1
                  and all(mv[e] == 0 for e in mv if e not in du and e not in dd))
            if ok:
                exact.append(dict(key=key, cluster=cluster_by_key.get(key),
                                  a_u=au_vals.pop(), a_d=ad_vals.pop()))
    exact_by_cluster = collections.Counter(e["cluster"] for e in exact)

    # det_u anchor census: does the unique det_u matching pass through (2,2)?
    anchor = collections.Counter()
    for key, c in cls.items():
        if len(c["matchings_u"]) == 1:
            p = c["matchings_u"][0][0]
            anchor[(cluster_by_key.get(key), p[2] == 2)] += 1
    anchor_table = {f"{cl}|{thr}": n for (cl, thr), n in sorted(anchor.items())}
    cl1_diag = sum(n for (cl, thr), n in anchor.items() if cl == 1 and thr)
    cl1_tot = sum(n for (cl, thr), n in anchor.items() if cl == 1)

    c2, c1 = per_cluster["2"], per_cluster["1"]
    consp = [per_cluster[str(c)] for c in (0, 3, 4)]
    gates = {
        "G1_matchings_enumerated": dict(
            value={str(k): v for k, v in sorted(term_counts.items())},
            passed=len(cls) == 755 and all(1 <= a <= 2 and 1 <= b <= 2
                                           for (a, b) in term_counts)),
        "G2_cluster2_at_mass_floor": dict(
            value=dict(lnM_between_std=c2["lnM_between_std"],
                       floor_lndet_u=c2["floor_lndet_u"],
                       resid_over_floor=c2["resid_over_floor"]),
            passed=c2["resid_over_floor"] < 3.0 and c2["lnM_between_std"] < 5 * c2["floor_lndet_u"]),
        "G3_conspiracy_not_det_determined": dict(
            value=[round(c["resid_over_floor"], 1) for c in consp],
            passed=all(c["resid_over_floor"] > 5.0 for c in consp)),
        "G4_no_exact_monomial_syzygy": dict(
            value=dict(n_exact=len(exact), n_single_single=sum(
                v for (a, b), v in term_counts.items() if a == 1 and b == 1)),
            passed=len(exact) == 0),
        "G5_cluster1_det_u_diagonal_anchor": dict(
            value=dict(det_u_through_22=cl1_diag, total=cl1_tot),
            passed=cl1_tot > 0 and cl1_diag == cl1_tot),
    }
    out = dict(purpose=__doc__.strip().splitlines()[0],
               n_classes=len(cls), det_term_counts={str(k): v for k, v in sorted(term_counts.items())},
               per_cluster=per_cluster, exact_syzygy_classes=exact,
               det_u_anchor_census=anchor_table,
               gates=gates, gates_passed=sum(g["passed"] for g in gates.values()),
               interpretation=(
                   "No exact monomial syzygy anywhere: 0/731 single-single classes "
                   "have the M exponent vector in span(det_u, det_d). The cluster-2 "
                   "lnM freeze (1.3e-3) sits AT the mass-data fit-tolerance floor "
                   "(det_u floor 1.1e-3): the monomial is pinned as tightly as the "
                   "masses themselves, but NOT through det values (regression "
                   "residual 8.7e-4 barely below raw 1.3e-3, coefficients "
                   "non-integer) - it behaves like physical data without being "
                   "reducible to det data. Cluster 1 is structurally different: "
                   "all 27 classes are diagonal-up textures with det_u = "
                   "u00*u11*u22 through the y_t-CENTRAL anchor edge, det_u frozen "
                   "to 7.3e-10 between classes, while lnM spreads 0.079 - an "
                   "intermediate freeze far above the mass floor, unexplained by "
                   "det data. Conspiracy clusters: lnM spreads 3.8..9.9, "
                   "18..10456x the floor - no determination. Net: the rigid "
                   "freeze is a property of the viable fitted set per cluster, "
                   "not a monomial identity."))
    json.dump(out, open("results/wp29_monomial_syzygy.json", "w"), indent=1)
    print(json.dumps(dict(term_counts={str(k): v for k, v in sorted(term_counts.items())},
                          per_cluster=per_cluster,
                          n_exact=len(exact), exact_by_cluster=dict(exact_by_cluster),
                          gates={k: v["passed"] for k, v in gates.items()}), indent=1))

if __name__ == "__main__":
    main()
