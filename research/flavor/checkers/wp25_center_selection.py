"""WP25: cluster-center selection - what fixes the five phase-cluster values?

At every viable minimum, J^2 = rho_v sin^2(phi) with rho_v = (a1/(DuDd))^2,
so the folded phase is fixed by the level-set value L = a1/(DuDd) through
sin(phi) = |J|/L. The cluster centers are therefore selected by the discrete
set of L values the magnitude sector realizes. This checker:

  A. recomputes per-minimum factors (wp21d2 logic) plus |J| and L;
  B. tests |J| constancy across clusters and the pointwise arcsin law;
  C. relation search among the five centers with a random-quintuple null;
  D. rigid-pair focus (clusters 1,2): phi_1+phi_2 vs pi/2, factor comparison;
  E. L ladder: log-spacings, ratios, recognition against mass ratios.

Reads: results/wp20_valley_audit.json,
       results/wp21e_universal_factorization.json
Writes: results/wp25_center_selection.json
Run: ../.venv/Scripts/python checkers/wp25_center_selection.py
"""
import json, math, collections, itertools
import numpy as np

SLOTS = [(i, j) for i in range(3) for j in range(3)]

def mask_slots(mask):
    return [s for k, s in enumerate(SLOTS) if mask & (1 << k)]

def tex_key(mu, md, pe):
    return f"{mu}_{md}_{pe[0]}{pe[1]}{pe[2]}"

def blocks_of(mask):
    cols = collections.defaultdict(set)
    for i, j in mask_slots(mask):
        cols[j].add(i)
    parent = list(range(3))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for rows in cols.values():
        rows = list(rows)
        for r in rows[1:]:
            parent[find(rows[0])] = find(r)
    comp = {}
    for i in range(3):
        comp.setdefault(find(i), []).append(i)
    return sorted(comp.values(), key=len)

def factor_rows(recs, fac, centers):
    import re as _re
    def cluster_of(phi):
        return min(range(len(centers)), key=lambda i: abs(phi - centers[i]))
    rows = []
    for r in recs:
        mu, md = r["member"]; pe = r["phase_edge"]
        key = tex_key(mu, md, pe)
        f = fac.get(key)
        if not f or "factorization_type" not in f:
            continue
        us, ds = mask_slots(mu), mask_slots(md)
        mags = np.exp(np.array(r["log_mags"]))
        phi = r["phi_raw"]
        Yu = np.zeros((3, 3), complex); Yd = np.zeros((3, 3), complex)
        val = {}
        for (i, j), m in zip(us, mags[:len(us)]):
            Yu[i, j] = m * (np.exp(1j*phi) if pe[0] == "u" and (i, j) == (pe[1], pe[2]) else 1)
            val[f"u{i}{j}"] = m
        for (i, j), m in zip(ds, mags[len(us):]):
            Yd[i, j] = m * (np.exp(1j*phi) if pe[0] == "d" and (i, j) == (pe[1], pe[2]) else 1)
            val[f"d{i}{j}"] = m
        Hu, Hd = Yu @ Yu.conj().T, Yd @ Yd.conj().T
        def vand(H):
            ev = np.linalg.eigvalsh(H)
            return abs((ev[0]-ev[1])*(ev[0]-ev[2])*(ev[1]-ev[2]))
        Du, Dd = vand(Hu), vand(Hd)
        M_val = 1.0
        for facstr in _re.findall(r"[ud]\d\d(?:\*\*\d+)?", f["monomial_M"]):
            m = _re.fullmatch(r"([ud]\d\d)(?:\*\*(\d+))?", facstr)
            M_val *= val[m.group(1)] ** int(m.group(2) or 1)
        sec = f["decomposed_sector"]
        H, Do = (Hu, Dd) if sec == "u" else (Hd, Du)
        a1 = math.sqrt(r["rho_v"]) * Du * Dd
        if f["factorization_type"] == "block21":
            bl = blocks_of(mu if sec == "u" else md)
            sing = [b[0] for b in bl if len(b) == 1][0]
            i, j = [b for b in bl if len(b) == 2][0]
            tr = (H[i, i] + H[j, j]).real
            det = (H[i, i]*H[j, j] - H[i, j]*H[j, i]).real
            s0 = H[sing, sing].real
            chi_s = s0*s0 - tr*s0 + det
            gap = math.sqrt(abs(tr*tr - 4*det))
        else:
            g = {(0,1): (H[0,0]-H[1,1]).real, (0,2): (H[0,0]-H[2,2]).real, (1,2): (H[1,1]-H[2,2]).real}
            S = {tuple(x) for x in f["gap_subset_dividing_B"]}
            remaining = [x for x in ((0,1),(0,2),(1,2)) if x not in S]
            gap = 1.0
            for x in remaining:
                gap *= abs(g[x])
            chi_s = 1.0
            for x in S:
                chi_s *= abs(g[x])
        L = a1 / (Du * Dd)
        rows.append(dict(key=key, cluster=cluster_of(r["phi_folded_deg"]),
                         phi_deg=r["phi_folded_deg"], chi2=r["chi2_stored"],
                         type=f["factorization_type"], sector=sec,
                         lnL=math.log(L), L=L, J=abs(r["J"]),
                         lnJ=math.log(abs(r["J"])),
                         lnM=math.log(M_val), lngap=math.log(gap),
                         lnDo=math.log(Do), lnchi=math.log(abs(chi_s))))
    return rows

def main():
    wp20 = json.load(open("results/wp20_valley_audit.json"))
    fac = json.load(open("results/wp21e_universal_factorization.json"))["census"]
    recs = wp20["records"]

    phis = sorted(r["phi_folded_deg"] for r in recs)
    centers, cur = [], [phis[0]]
    for p in phis[1:]:
        if p - cur[-1] > 1.5:
            centers.append(sum(cur) / len(cur)); cur = [p]
        else:
            cur.append(p)
    centers.append(sum(cur) / len(cur))

    rows = factor_rows(recs, fac, centers)
    by_cluster = collections.defaultdict(list)
    for x in rows:
        by_cluster[x["cluster"]].append(x)

    # B. |J| constancy and the arcsin law
    cl_summary = {}
    for ci in sorted(by_cluster):
        xs = by_cluster[ci]
        cl_summary[ci] = dict(
            center=centers[ci], n=len(xs),
            mean_lnJ=float(np.mean([x["lnJ"] for x in xs])),
            std_lnJ=float(np.std([x["lnJ"] for x in xs])),
            mean_lnL=float(np.mean([x["lnL"] for x in xs])),
            std_lnL=float(np.std([x["lnL"] for x in xs])),
            types=dict(collections.Counter(x["type"] for x in xs)),
            sectors=dict(collections.Counter(x["sector"] for x in xs)))
    dev = [abs(x["J"] - x["L"]*math.sin(math.radians(x["phi_deg"])))/x["J"] for x in rows]
    arcsin_max_rel = max(dev)
    Jmeans = [cl_summary[ci]["mean_lnJ"] for ci in sorted(cl_summary)]
    J_between_std = float(np.std(Jmeans))

    # C. relation search with null
    Cs = [centers[i] for i in sorted(cl_summary)]
    targets = {"pi/2": 90.0, "pi/4": 45.0, "pi/8": 22.5, "3pi/8": 67.5, "pi": 180.0}
    best = min(recs, key=lambda r: r["chi2_stored"])
    import wp7_ensemble as wp7
    Yu_b, Yd_b = wp7.build_texture(best["member"][0], best["member"][1],
                                   best["phase_edge"][0],
                                   (best["phase_edge"][1], best["phase_edge"][2]),
                                   np.array(best["log_mags"] + [best["phi_raw"]]))
    obs = wp7.observables17(Yu_b, Yd_b)
    alpha, beta, gamma = float(obs[12]), float(obs[13]), float(obs[14])
    targets.update({"alpha": alpha, "beta": beta, "gamma": gamma})
    hits = []
    coeffs = [-2, -1, -0.5, 0.5, 1, 2]
    n_trials = 0
    for k in (1, 2, 3):
        for idxs in itertools.combinations(range(5), k):
            for cs in itertools.product(coeffs, repeat=k):
                v = sum(c*Cs[i] for c, i in zip(cs, idxs))
                for tname, tv in targets.items():
                    n_trials += 1
                    res = abs(v - tv)
                    if res < 0.15:
                        hits.append(dict(combo=[(c, i) for c, i in zip(cs, idxs)],
                                         value=v, target=tname, residual=res))
    hits.sort(key=lambda h: h["residual"])
    rng = np.random.default_rng(20260823)
    null_counts = []
    for _ in range(200):
        rq = sorted(rng.uniform(20, 90, 5))
        cnt = 0
        for k in (1, 2, 3):
            for idxs in itertools.combinations(range(5), k):
                for cs in itertools.product(coeffs, repeat=k):
                    v = sum(c*rq[i] for c, i in zip(cs, idxs))
                    for tv in targets.values():
                        if abs(v - tv) < 0.15:
                            cnt += 1
        null_counts.append(cnt)
    null_mean = float(np.mean(null_counts))

    # D. rigid pair (clusters 1, 2)
    rigid = {}
    for ci in (1, 2):
        xs = by_cluster[ci]
        rigid[ci] = dict(center=centers[ci], n=len(xs),
                         mean_lnM=float(np.mean([x["lnM"] for x in xs])),
                         mean_lngap=float(np.mean([x["lngap"] for x in xs])),
                         mean_lnDo=float(np.mean([x["lnDo"] for x in xs])),
                         mean_lnchi=float(np.mean([x["lnchi"] for x in xs])),
                         std_lnL=float(np.std([x["lnL"] for x in xs])))
    sum12 = centers[1] + centers[2]
    phi_std = {ci: float(np.std([x["phi_deg"] for x in by_cluster[ci]])) for ci in (1, 2)}

    # E. L ladder
    Ls = [math.exp(cl_summary[ci]["mean_lnL"]) for ci in sorted(cl_summary)]
    ladder = dict(L_values=Ls,
                  log_spacings=[cl_summary[i+1]["mean_lnL"] - cl_summary[i]["mean_lnL"]
                                for i in range(4)],
                  ratios=[Ls[i+1]/Ls[i] for i in range(4)],
                  sin_centers=[math.sin(math.radians(c)) for c in Cs])
    su2, _ = np.linalg.eigh(Yu_b @ Yu_b.conj().T)
    sd2, _ = np.linalg.eigh(Yd_b @ Yd_b.conj().T)
    yu, yc, yt = np.sqrt(su2); yd, ys, yb = np.sqrt(sd2)
    mass_cands = {"yc/yu": yc/yu, "yt/yc": yt/yc, "yb/ys": yb/ys, "ys/yd": ys/yd,
                  "yb/yd": yb/yd, "yt/yu": yt/yu, "sqrt(yt/yc)": math.sqrt(yt/yc),
                  "sqrt(yb/ys)": math.sqrt(yb/ys), "sqrt(yc/yu)": math.sqrt(yc/yu)}
    ladder_recog = {}
    for li, lr in enumerate(ladder["ratios"]):
        best_c = min(mass_cands.items(), key=lambda kv: abs(math.log(kv[1]/lr)))
        ladder_recog[f"L{li+1}/L{li}"] = dict(ratio=lr, nearest=best_c[0],
                                               nearest_val=best_c[1],
                                               log_dev=abs(math.log(best_c[1]/lr)))

    out = dict(
        purpose="WP25 cluster-center selection audit",
        centers=Cs, best_fit_ckm=dict(alpha=alpha, beta=beta, gamma=gamma),
        B_arcsin_law_max_rel_dev=arcsin_max_rel,
        B_lnJ_between_cluster_std=J_between_std,
        B_cluster_summary={str(k): v for k, v in cl_summary.items()},
        C_relation_hits=hits[:15], C_n_trials=n_trials,
        C_null_mean_hits=null_mean, C_n_hits=len(hits),
        D_rigid_pair={str(k): v for k, v in rigid.items()}, D_sum12_deg=sum12,
        D_sum12_residual_vs_90=abs(sum12 - 90.0),
        D_within_cluster_phi_std={str(k): v for k, v in phi_std.items()},
        E_ladder=ladder, E_ladder_recognition=ladder_recog)
    json.dump(out, open("results/wp25_center_selection.json", "w"), indent=1)
    print("centers:", [round(c, 4) for c in Cs])
    print("CKM best-fit: alpha=%.3f beta=%.3f gamma=%.3f" % (alpha, beta, gamma))
    print("arcsin law max rel dev: %.3e" % arcsin_max_rel)
    print("lnJ between-cluster std: %.4f" % J_between_std)
    for ci in sorted(cl_summary):
        s = cl_summary[ci]
        print(f"cluster {ci}: phi={s['center']:.4f} n={s['n']} lnJ={s['mean_lnJ']:.4f}+-{s['std_lnJ']:.4f} "
              f"lnL={s['mean_lnL']:.4f}+-{s['std_lnL']:.4f} types={s['types']} sec={s['sectors']}")
    print(f"rigid pair sum: {sum12:.4f} deg, residual vs 90: {abs(sum12-90):.4f}, "
          f"within-cluster phi std: {phi_std}")
    print(f"relation hits (<0.15 deg): {len(hits)} over {n_trials} trials; null mean {null_mean:.1f}")
    for h in hits[:8]:
        print("  ", h["combo"], "=", round(h["value"], 4), "~", h["target"], f"res={h['residual']:.4f}")
    print("L ladder ratios:", [round(r, 4) for r in ladder["ratios"]])
    print("L recognition:", {k: (v["nearest"], round(v["log_dev"], 4)) for k, v in ladder_recog.items()})

if __name__ == "__main__":
    main()
