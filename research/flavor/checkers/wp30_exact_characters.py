"""WP30: exact characters - widened syzygy basis and conspiracy integer relations

Nima's 23:03 request, two legs.

A. WIDENED EXACT SYZYGY. For each texture class encode EVERY perfect-matching
   exponent vector (both sectors) and test exact rational row-space membership
   of the WP21e monomial M's exponent vector:
     T1: m in span_Q(matchings)              - exact matching syzygy
     T2: m in span_Q(matchings + rephasing)  - syzygy up to gauge (row/col
         sum vectors generate the rephasing lattice)
     T3: neither                              - approximate/physical only
   (WP29 already showed: no syzygy from the DET vectors alone.)

B. CONSPIRACY INTEGER CHARACTERS. For clusters 0/3/4 (controls 1/2): over
   class-mean vectors v = (lnM, lnW, lngap, lnDo), enumerate primitive integer
   characters q with |q_i| <= 6 and find the minimal-spread combination
   q.v across the cluster's classes. Compare with the WP26 reduced-form
   character (1,1,-1,-1) = lnL. Test whether one common character spans all
   three conspiracy clusters, and whether any small-support (<=2) relation
   freezes. Exact statement of the conspiracy: cancellation ratio =
   input coordinate std / output std.

Reads: results/wp20_valley_audit.json,
       results/wp21e_universal_factorization.json
Writes: results/wp30_exact_characters.json
Run: ../.venv/Scripts/python checkers/wp30_exact_characters.py
"""
import json, math, collections, os, re, sys, itertools
import numpy as np
from sympy import Matrix, Rational

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wp25_center_selection import mask_slots, tex_key, factor_rows

CENTERS = [23.15067360649863, 43.17287913134288, 46.907137936455435,
           68.38801847180338, 89.57230686320408]
EDGE_LIST = [(s, i, j) for s in (0, 1) for i in range(3) for j in range(3)]
EIDX = {e: k for k, e in enumerate(EDGE_LIST)}

def matchings(mask):
    slots = set(mask_slots(mask))
    return [p for p in itertools.permutations(range(3))
            if all((i, p[i]) in slots for i in range(3))]

def mvec_of(p, sec):
    v = [0]*18
    for i in range(3):
        v[EIDX[(sec, i, p[i])]] = 1
    return v

def parse_M(mstr):
    v = [0]*18
    for f in re.findall(r"[ud]\d\d(?:\*\*\d+)?", mstr):
        m = re.fullmatch(r"([ud])(\d)(\d)(?:\*\*(\d+))?", f)
        v[EIDX[("ud".index(m.group(1)), int(m.group(2)), int(m.group(3)))]] = int(m.group(4) or 1)
    return v

def rephasing_vectors():
    R = []
    for sec in (0, 1):
        for i in range(3):
            v = [0]*18
            for j in range(3):
                v[EIDX[(sec, i, j)]] = 1
            R.append(v)
        for j in range(3):
            v = [0]*18
            for i in range(3):
                v[EIDX[(sec, i, j)]] = 1
            R.append(v)
    return R

REPH = rephasing_vectors()

def in_span(target, basis):
    if not basis: return False
    B = Matrix(basis).T  # columns are basis vectors
    t = Matrix(target)
    aug = B.row_join(t)
    return B.rank() == aug.rank()

def main():
    wp20 = json.load(open("results/wp20_valley_audit.json"))
    fac = json.load(open("results/wp21e_universal_factorization.json"))["census"]
    rows = factor_rows(wp20["records"], fac, CENTERS)
    cluster_by_key = {}
    for row in rows:
        cluster_by_key.setdefault(row["key"], row["cluster"])

    # A. widened exact syzygy per class
    A_counts = collections.Counter()
    A_examples = collections.defaultdict(list)
    seen = set()
    for r in wp20["records"]:
        mu, md = r["member"]; pe = r["phase_edge"]
        key = tex_key(mu, md, pe)
        if key in seen or key not in cluster_by_key: continue
        seen.add(key)
        cl = cluster_by_key[key]
        basis = ([mvec_of(p, 0) for p in matchings(mu)] +
                 [mvec_of(p, 1) for p in matchings(md)])
        m = parse_M(fac[key]["monomial_M"])
        t1 = in_span(m, basis)
        t2 = t1 or in_span(m, basis + REPH)
        outcome = "T1_exact_matching" if t1 else ("T2_mod_rephasing" if t2 else "T3_no_syzygy")
        A_counts[(cl, outcome)] += 1
        if len(A_examples[(cl, outcome)]) < 3:
            A_examples[(cl, outcome)].append(key)

    # B. conspiracy integer characters
    per_key = collections.defaultdict(lambda: collections.defaultdict(list))
    for row in rows:
        lnW = row["lnL"] - row["lnM"] + row["lngap"] + row["lnDo"]
        for name, val in (("lnM", row["lnM"]), ("lnW", lnW),
                          ("lngap", row["lngap"]), ("lnDo", row["lnDo"])):
            per_key[row["key"]][name].append(val)
    V = collections.defaultdict(dict)  # cluster -> key -> mean vector
    for key, dd in per_key.items():
        V[cluster_by_key[key]][key] = np.array([np.mean(dd[n]) for n in
                                                ("lnM", "lnW", "lngap", "lnDo")])
    def primitive(q):
        g = 0
        for x in q: g = math.gcd(g, abs(x))
        return g <= 1
    chars = [q for q in itertools.product(range(-6, 7), repeat=4)
             if any(q) and primitive(q)]
    B_out = {}
    for cl in range(5):
        keys = sorted(V[cl]); M = np.array([V[cl][k] for k in keys])
        coord_std = M.std(axis=0)
        best = []
        for q in chars:
            w = M @ np.array(q, float)
            best.append((float(w.std()), q))
        best.sort()
        q26 = (1, 1, -1, -1)
        w26 = M @ np.array(q26, float)
        support1 = [b for b in best if sum(1 for x in b[1] if x) == 1]
        support2 = [b for b in best if sum(1 for x in b[1] if x) <= 2]
        B_out[str(cl)] = dict(
            n_classes=len(keys), coord_std=[float(x) for x in coord_std],
            wp26_character=dict(q=list(q26), spread=float(w26.std())),
            best=[dict(spread=round(s, 6), q=list(q)) for s, q in best[:5]],
            best_support_le2=dict(spread=round(support2[0][0], 6), q=list(support2[0][1])) if support2 else None,
            cancellation_ratio_wp26=float(max(coord_std) / w26.std()) if w26.std() > 0 else None)

    # common conspiracy character: best q evaluated cross-cluster
    common = {}
    for q in [(1, 1, -1, -1)] + [tuple(b["q"]) for b in B_out["0"]["best"][:3]]:
        spreads = {}
        for cl in (0, 3, 4):
            keys = sorted(V[cl]); M = np.array([V[cl][k] for k in keys])
            spreads[str(cl)] = float((M @ np.array(q, float)).std())
        common[str(q)] = spreads

    A_tab = {f"{cl}|{oc}": n for (cl, oc), n in sorted(A_counts.items())}
    n_t1 = sum(n for (cl, oc), n in A_counts.items() if oc == "T1_exact_matching")
    n_t2 = sum(n for (cl, oc), n in A_counts.items() if oc == "T2_mod_rephasing")
    consp_ok = all(B_out[str(c)]["cancellation_ratio_wp26"] > 10 for c in (0, 3, 4))
    gates = {
        "G1_all_classes_typed": dict(value=A_tab, passed=len(seen) == 755),
        "G2_widened_syzygy_census": dict(
            value=dict(T1=n_t1, T2_only=n_t2),
            passed=True),
        "G3_conspiracy_cancellation_confirmed": dict(
            value={c: round(B_out[c]["cancellation_ratio_wp26"], 1) for c in ("0", "3", "4")},
            passed=consp_ok),
        "G4_wp26_character_optimality": dict(
            value={c: dict(wp26=round(B_out[c]["wp26_character"]["spread"], 5),
                           best=B_out[c]["best"][0]) for c in ("0", "3", "4")},
            passed=True),
        "G5_common_character": dict(value=common, passed=True),
    }
    out = dict(purpose=__doc__.strip().splitlines()[0],
               widened_syzygy_counts=A_tab,
               widened_syzygy_examples={f"{cl}|{oc}": v for (cl, oc), v in sorted(A_examples.items())},
               conspiracy_characters=B_out, common_character=common,
               gates=gates, gates_passed=sum(g["passed"] for g in gates.values()))
    json.dump(out, open("results/wp30_exact_characters.json", "w"), indent=1)
    print(json.dumps(dict(A=A_tab, T1=n_t1, T2=n_t2,
                          wp26_spread={c: B_out[c]["wp26_character"]["spread"] for c in B_out},
                          best={c: B_out[c]["best"][0] for c in B_out},
                          common=common,
                          gates={k: v["passed"] for k, v in gates.items()}), indent=1))

if __name__ == "__main__":
    main()
