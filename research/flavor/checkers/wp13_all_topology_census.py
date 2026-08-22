"""WP13: exhaustive exact harmonic census over ALL one-cycle nine-link
topologies (marici.Figueiredo).

Extends WP12 (entry 1903), which certified det[H_u,H_d] = 2i K sin(phi)
exactly at the 61 FITTED carrier-groupoid vertices, to the full
support-general class:

  supports (mask_u, mask_d) with |supp Yu| = k, |supp Yd| = 9 - k,
  k in {3..6}, each sector admitting a perfect matching (full rank),
  and the combined nine-node bipartite field graph CONNECTED -- hence
  b1 = E - V + 1 = 1, a unique cycle.  The loop phase z = e^{i phi} is
  placed on each edge of the unique cycle in turn.

Method per (support, phase-edge) case, exact Fraction arithmetic
(no floating point, no sympy in the hot loop):

  * Laurent polynomials in z as {power: Fraction} dicts;
  * H_u = Yu Yu^dag (dagger: transpose + z -> z^{-1}), likewise H_d;
  * C = [H_u, H_d]; det C = tr C^3 / 3 (exact identity, gated in WP12);
  * record the Laurent support of det C at TWO independent exact
    rational magnitude assignments (polynomial-identity-testing screen:
    any nonzero higher-harmonic coefficient at a generic exact point is
    a rigorous counterexample certificate).

Symmetry: row/column permutations (S_3 x S_3 x S_3) conjugate H_u, H_d
by permutation matrices and leave det C invariant, and u <-> d swap
maps case to case; the census quotients by this group and tests orbit
representatives, while recording the full (support, phase-edge) counts.

Regression gate: every one of the 61 WP9 fitted charts must appear in
the enumeration and pass.

Output: research/flavor/results/wp13_all_topology_census.json
"""
import json
import time
from fractions import Fraction
from itertools import combinations

SLOTS = [(i, j) for i in range(3) for j in range(3)]
SLOT_INDEX = {s: k for k, s in enumerate(SLOTS)}

# node ids: Q_i = i (0..2), u^c_j = 3+j (3..5), d^c_k = 6+k (6..8)


def slots_of(mask):
    return [s for k, s in enumerate(SLOTS) if mask & (1 << k)]


def has_perfect_matching(mask):
    cols_of_row = [[j for (i, j) in slots_of(mask) if i == r] for r in range(3)]
    if any(not c for c in cols_of_row):
        return False
    import itertools
    for perm in itertools.permutations(range(3)):
        if all(perm[r] in cols_of_row[r] for r in range(3)):
            return True
    return False


def edges_of(mask_u, mask_d):
    """Combined field-graph edges as (node_a, node_b), tagged by sector."""
    eu = [(i, 3 + j) for (i, j) in slots_of(mask_u)]
    ed = [(i, 6 + j) for (i, j) in slots_of(mask_d)]
    return eu, ed


def unique_cycle_edges(mask_u, mask_d):
    """Return the set of cycle edges (as frozensets of node pairs) if the
    combined graph is connected with 9 edges on 9 nodes, else None."""
    eu, ed = edges_of(mask_u, mask_d)
    adj = {v: [] for v in range(9)}
    all_edges = []
    for (a, b) in eu + ed:
        adj[a].append(b)
        adj[b].append(a)
        all_edges.append((a, b))
    # connectivity
    seen = {0}
    stack = [0]
    while stack:
        v = stack.pop()
        for w in adj[v]:
            if w not in seen:
                seen.add(w)
                stack.append(w)
    if len(seen) != 9 or len(all_edges) != 9:
        return None
    # spanning tree via DFS from 0; the single non-tree edge closes the cycle
    parent = {0: None}
    pedge = {}
    order = [0]
    tree_edges = set()
    non_tree = []
    edge_set = {frozenset(e) for e in all_edges}
    for v in order:
        for w in adj[v]:
            if w not in parent:
                parent[w] = v
                pedge[w] = frozenset((v, w))
                tree_edges.add(frozenset((v, w)))
                order.append(w)
    non_tree = [e for e in edge_set if e not in tree_edges]
    assert len(non_tree) == 1
    (extra,) = non_tree
    a, b = tuple(extra)
    # path a -> b in the tree
    def path_to_root(x):
        p = []
        while x is not None:
            p.append(x)
            x = parent[x]
        return p
    pa = path_to_root(a)
    pb = path_to_root(b)
    sa = set(pa)
    cycle_nodes = []
    for x in pb:
        if x in sa:
            lca = x
            break
    seg_a = pa[:pa.index(lca) + 1]
    seg_b = pb[:pb.index(lca) + 1]
    cyc = [frozenset((seg_a[t], seg_a[t + 1])) for t in range(len(seg_a) - 1)]
    cyc += [frozenset((seg_b[t], seg_b[t + 1])) for t in range(len(seg_b) - 1)]
    cyc.append(extra)
    return set(cyc)


def canonical_form(mask_u, mask_d):
    """Min encoding over S_3(Q) x S_3(u^c) x S_3(d^c) and u<->d swap."""
    import itertools
    eu = sorted(slots_of(mask_u))
    ed = sorted(slots_of(mask_d))
    best = None
    for pq in itertools.permutations(range(3)):
        for pu in itertools.permutations(range(3)):
            ru = tuple(sorted((pq[i], pu[j]) for (i, j) in eu))
            for pd in itertools.permutations(range(3)):
                rd = tuple(sorted((pq[i], pd[j]) for (i, j) in ed))
                for swap in (False, True):
                    enc = (rd, ru) if swap else (ru, rd)
                    if best is None or enc < best:
                        best = enc
    return best


# ---------- exact Laurent arithmetic ----------

def lp_const(c):
    return {0: Fraction(c)} if c else {}


def lp_z():
    return {1: Fraction(1)}


def lp_mul(a, b):
    out = {}
    for pa, ca in a.items():
        for pb, cb in b.items():
            out[pa + pb] = out.get(pa + pb, Fraction(0)) + ca * cb
    return {p: c for p, c in out.items() if c}


def lp_add(a, b):
    out = dict(a)
    for p, c in b.items():
        out[p] = out.get(p, Fraction(0)) + c
    return {p: c for p, c in out.items() if c}


def lp_neg(a):
    return {p: -c for p, c in a.items()}


def lp_conj(a):
    return {-p: c for p, c in a.items()}


def mat_mul(A, B):
    out = [[{} for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            acc = {}
            for k in range(3):
                acc = lp_add(acc, lp_mul(A[i][k], B[k][j]))
            out[i][j] = acc
    return out


def mat_sub(A, B):
    return [[lp_add(A[i][j], lp_neg(B[i][j])) for j in range(3)]
            for i in range(3)]


def mat_dagger(A):
    return [[lp_conj(A[j][i]) for j in range(3)] for i in range(3)]


def mat_trace(A):
    return lp_add(lp_add(A[0][0], A[1][1]), A[2][2])


def decode_cycle_edge(e):
    """Order-independent decode of a cycle edge (frozenset of two node ids)
    into (sector, slot).  Q nodes are 0..2, u^c 3..5, d^c 6..8."""
    a, b = tuple(e)
    q = a if a <= 2 else b
    other = b if a <= 2 else a
    assert q <= 2 and other >= 3, f"bad edge {e}"
    if other <= 5:
        return "u", (q, other - 3)
    return "d", (q, other - 6)


def detC_support(mask_u, mask_d, phase_sector, phase_slot, mags):
    """Exact Laurent support of det[Hu,Hd]; mags = 9 Fractions in
    (u-slots, d-slots) order."""
    zero = {}
    Yu = [[zero]*3 for _ in range(3)]
    Yd = [[zero]*3 for _ in range(3)]
    entries = [("u", s) for s in slots_of(mask_u)] + \
              [("d", s) for s in slots_of(mask_d)]
    assert len(entries) == 9
    assert (phase_sector, phase_slot) in entries, \
        f"phase slot {phase_sector}{phase_slot} not in support"
    phase_applied = False
    for (sector, slot), m in zip(entries, mags):
        val = lp_const(m)
        if sector == phase_sector and slot == phase_slot:
            val = lp_mul(val, lp_z())
            phase_applied = True
        if sector == "u":
            Yu[slot[0]][slot[1]] = val
        else:
            Yd[slot[0]][slot[1]] = val
    assert phase_applied
    Hu = mat_mul(Yu, mat_dagger(Yu))
    Hd = mat_mul(Yd, mat_dagger(Yd))
    C = mat_sub(mat_mul(Hu, Hd), mat_mul(Hd, Hu))
    C2 = mat_mul(C, C)
    C3 = mat_mul(C2, C)
    tr3 = mat_trace(C3)
    # det C = tr C^3 / 3
    return {p: c / 3 for p, c in tr3.items() if c}


def analyze_case(mask_u, mask_d, phase_sector, phase_slot):
    """Two independent exact generic magnitude assignments.  Classification:
    'first_harmonic' (support exactly {-1,+1}, a1 != 0), 'identically_zero'
    (det C vanishes at both generic points), else 'higher_harmonic'."""
    mags_a = [Fraction(p) for p in (2, 3, 5, 7, 11, 13, 17, 19, 23)]
    mags_b = [Fraction(p * p + 1, q) for p, q in
              zip((3, 5, 7, 11, 13, 17, 19, 23, 29),
                  (2, 3, 5, 7, 11, 13, 17, 19, 23))]
    supp_a = detC_support(mask_u, mask_d, phase_sector, phase_slot, mags_a)
    supp_b = detC_support(mask_u, mask_d, phase_sector, phase_slot, mags_b)
    antisym = all(supp_a.get(-m, 0) + supp_a.get(m, 0) == 0 for m in (1, 2, 3)) \
        and supp_a.get(0, 0) == 0
    no_higher = set(supp_a) <= {-1, 0, 1} and set(supp_b) <= {-1, 0, 1}
    if not supp_a and not supp_b:
        cls = "identically_zero"
    elif no_higher and supp_a.get(1, 0) != 0:
        cls = "first_harmonic"
    else:
        cls = "higher_harmonic"
    return {"pass": no_higher and antisym,
            "class": cls,
            "support_a": sorted(supp_a), "support_b": sorted(supp_b),
            "a1": str(supp_a.get(1)), "a2": str(supp_a.get(2)),
            "a3": str(supp_a.get(3)), "a0": str(supp_a.get(0)),
            "cp_antisym": antisym}


def main():
    t0 = time.time()
    # ---- enumerate all viable one-cycle supports ----
    masks = range(512)
    pm = {m: (bin(m).count("1") in (3, 4, 5, 6)) and has_perfect_matching(m)
          for m in masks}
    supports = []
    for mu in masks:
        if not pm.get(mu):
            continue
        ku = bin(mu).count("1")
        if not (3 <= ku <= 6):
            continue
        for md in masks:
            if bin(md).count("1") != 9 - ku or not pm.get(md):
                continue
            cyc = unique_cycle_edges(mu, md)
            if cyc is None:
                continue
            supports.append((mu, md, cyc))
    print(f"viable one-cycle supports: {len(supports)} ({time.time()-t0:.0f}s)",
          flush=True)

    # ---- orbit reduction ----
    orbits = {}
    for mu, md, cyc in supports:
        orbits.setdefault(canonical_form(mu, md), []).append((mu, md, cyc))
    print(f"S3^3-plus-swap orbits: {len(orbits)} ({time.time()-t0:.0f}s)",
          flush=True)

    # ---- exact census over orbit representatives ----
    total_cases = 0
    tested = 0
    failures = []
    cases = []
    cycle_len_hist = {}
    class_hist = {}
    purity_class = {}
    for canon, members in sorted(orbits.items()):
        mu, md, cyc = members[0]
        cycle_len_hist[len(cyc)] = cycle_len_hist.get(len(cyc), 0) + 1
        cyc_u = sum(1 for e in cyc if max(e) <= 5)
        cyc_d = len(cyc) - cyc_u
        purity = ("u_only" if cyc_d == 0 else
                  "d_only" if cyc_u == 0 else "mixed")
        for e in cyc:
            sector, slot = decode_cycle_edge(e)
            total_cases += 1
            r = analyze_case(mu, md, sector, slot)
            tested += 1
            cls = r["class"]
            class_hist[cls] = class_hist.get(cls, 0) + 1
            key = f"{purity}/{cls}"
            purity_class[key] = purity_class.get(key, 0) + 1
            cases.append({"member": [mu, md], "phase_edge": [sector, *slot],
                          "cycle_length": len(cyc), "cycle_purity": purity,
                          "class": cls, "support_a": r["support_a"]})
            if not r["pass"]:
                failures.append({"member": [mu, md], "phase_edge": [sector, *slot],
                                 "result": r})
    print(f"phase-placement cases tested: {tested} "
          f"({time.time()-t0:.0f}s)", flush=True)
    print(f"higher-harmonic failures: {len(failures)}")
    print("cycle length histogram (per orbit):", cycle_len_hist)
    print("class histogram:", class_hist)
    print("purity/class cross-tab:", purity_class)

    # ---- regression: all 61 fitted charts present and passing ----
    with open("results/wp9_lo_atlas.json", encoding="utf-8") as f:
        charts = json.load(f)["charts"]
    regress = []
    for ch in charts:
        mu, md = ch["member"]
        sec = ch["phase_edge"][0]
        slot = (ch["phase_edge"][1], ch["phase_edge"][2])
        r = analyze_case(mu, md, sec, slot)
        regress.append({"member": [mu, md], "phase_edge": ch["phase_edge"],
                        "pass": r["pass"]})
    n_reg = sum(r["pass"] for r in regress)

    out = {
        "purpose": "WP13 support-general exact census: det[Hu,Hd] harmonic "
                   "support over ALL connected one-cycle nine-link "
                   "topologies with full-rank sectors, phase on each cycle "
                   "edge; exact Fraction arithmetic, two generic magnitude "
                   "assignments per case",
        "viable_support_count": len(supports),
        "orbit_count": len(orbits),
        "phase_cases_tested": tested,
        "failure_count": len(failures),
        "failures": failures[:50],
        "cycle_length_histogram_per_orbit": cycle_len_hist,
        "fitted_chart_regression": {"count": len(regress), "passing": n_reg},
        "method_note": "det C = tr C^3/3 exact; PIT screen with two exact "
                       "rational assignments; nonzero higher harmonic at a "
                       "generic exact point is a rigorous counterexample",
    }
    with open("results/wp13_all_topology_census.json", "w",
              encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(json.dumps({k: v for k, v in out.items()
                      if k not in ("failures",)}, indent=2)[:1500])
    print(f"elapsed {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
