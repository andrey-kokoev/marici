"""WP14 exact census: perfect matchings, determinant phase membership, and
the strong-CP chart question over the whole carrier groupoid
(marici.Figueiredo).

Residue of the brief's fifth work package, lifted from the four worked
textures (WP5, results/wp5_matching_reality.json) to (a) every viable
one-cycle nine-link topology with the phase on each cycle edge in turn
(the WP13 6552-support / 18-orbit / 80-case class) and (b) the 61 fitted
WP9 carrier-groupoid vertices, which all lie over ONE physical flavor
point (WP10, ev-000000001463 line).

Per (support, phase-edge) case, pure combinatorics (no floats, no sympy):

  * enumerate the perfect matchings of the Yu and Yd bipartite graphs
    (row set Q = {0,1,2}, column sets u^c / d^c);
  * det Y_sector = sum over matchings of sign(pi) * (product of edge
    magnitudes); the phase edge multiplies its monomial by z = e^{i phi}
    IFF the phase edge belongs to that matching;
  * phase_in_det := phase edge occurs in ANY perfect matching of its
    sector;
  * if not phase_in_det: det(Yu Yd) is a real monomial times a sign, so
    arg det(Yu Yd) in {0, pi} structurally -- the paper's "route to real
    det" (App. V) holds for this chart;
  * if phase_in_det: det of the phase sector is A + z B (or z A alone if
    every matching uses the phase edge), so arg det depends on phi (and
    on magnitudes when A, B both nonzero).

Typing caution recorded in the output: arg det(Yu Yd) is NOT invariant
under the U(1)^3 part of the weak-basis group; the physical combination
is theta-bar = theta + arg det(Yu Yd).  This census measures the
CHART-COMBINATORIAL property "the loop phase can avoid every determinant
matching".  It says nothing by itself about spontaneous CP, radiative
stability, or a solution of strong CP.

Falsifier #4 of the brief: does the phase-avoidance property survive
allowed chart changes?  Decisive test: the 61 fitted charts all sit over
one physical point.  If phase-avoidance is mixed across them, the
property types as CHART data, not physical data.

Structural criterion audit: for these unicyclic supports, an edge is in
no perfect matching iff deleting its endpoints leaves no perfect
matching (definition, brute-forced); we additionally record the Dulmage-
Mendelsohn style invariant n_matchings per sector and cross-tabulate
phase membership against WP13's zero-dichotomy orbits.

Regression gate: the four WP5 worked textures must reproduce
results/wp5_matching_reality.json phase-membership booleans.

Output: research/flavor/results/wp14_matching_determinant_census.json
"""
import json
import time
from itertools import permutations

SLOTS = [(i, j) for i in range(3) for j in range(3)]


def slots_of(mask):
    return [s for k, s in enumerate(SLOTS) if mask & (1 << k)]


def perfect_matchings(mask):
    """All permutations pi (tuple, pi[row] = col) with every (i, pi(i))
    in the support; each with its sign."""
    cols = [[j for (i, j) in slots_of(mask) if i == r] for r in range(3)]
    out = []
    for pi in permutations(range(3)):
        if all(pi[r] in cols[r] for r in range(3)):
            # sign of permutation
            inv = sum(1 for a in range(3) for b in range(a + 1, 3)
                      if pi[a] > pi[b])
            out.append((pi, -1 if inv % 2 else 1))
    return out


def has_perfect_matching(mask):
    return bool(perfect_matchings(mask))


def edges_of(mask_u, mask_d):
    eu = [(i, 3 + j) for (i, j) in slots_of(mask_u)]
    ed = [(i, 6 + j) for (i, j) in slots_of(mask_d)]
    return eu, ed


def unique_cycle_edges(mask_u, mask_d):
    """Cycle edges (frozensets of node pairs) if connected 9-edge 9-node,
    else None.  Same construction as WP13."""
    eu, ed = edges_of(mask_u, mask_d)
    adj = {v: [] for v in range(9)}
    all_edges = []
    for (a, b) in eu + ed:
        adj[a].append(b)
        adj[b].append(a)
        all_edges.append((a, b))
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
    parent = {0: None}
    tree_edges = set()
    order = [0]
    for v in order:
        for w in adj[v]:
            if w not in parent:
                parent[w] = v
                tree_edges.add(frozenset((v, w)))
                order.append(w)
    edge_set = {frozenset(e) for e in all_edges}
    non_tree = [e for e in edge_set if e not in tree_edges]
    assert len(non_tree) == 1
    (extra,) = non_tree
    a, b = tuple(extra)

    def path_to_root(x):
        p = []
        while x is not None:
            p.append(x)
            x = parent[x]
        return p

    pa = path_to_root(a)
    pb = path_to_root(b)
    sa = set(pa)
    lca = next(x for x in pb if x in sa)
    seg_a = pa[:pa.index(lca) + 1]
    seg_b = pb[:pb.index(lca) + 1]
    cyc = [frozenset((seg_a[t], seg_a[t + 1])) for t in range(len(seg_a) - 1)]
    cyc += [frozenset((seg_b[t], seg_b[t + 1])) for t in range(len(seg_b) - 1)]
    cyc.append(extra)
    return set(cyc)


def canonical_form(mask_u, mask_d):
    eu = sorted(slots_of(mask_u))
    ed = sorted(slots_of(mask_d))
    best = None
    for pq in permutations(range(3)):
        for pu in permutations(range(3)):
            ru = tuple(sorted((pq[i], pu[j]) for (i, j) in eu))
            for pd in permutations(range(3)):
                rd = tuple(sorted((pq[i], pd[j]) for (i, j) in ed))
                for swap in (False, True):
                    enc = (rd, ru) if swap else (ru, rd)
                    if best is None or enc < best:
                        best = enc
    return best


def decode_cycle_edge(e):
    a, b = tuple(e)
    q = a if a <= 2 else b
    other = b if a <= 2 else a
    assert q <= 2 and other >= 3, f"bad edge {e}"
    if other <= 5:
        return "u", (q, other - 3)
    return "d", (q, other - 6)


def analyze_case(mask_u, mask_d, phase_sector, phase_slot):
    """Matching structure + phase membership for one (support, phase) case."""
    mu = perfect_matchings(mask_u)
    md = perfect_matchings(mask_d)
    assert mu and md, "support must be full rank in both sectors"
    pm = mu if phase_sector == "u" else md
    q, j = phase_slot
    in_any = any(pi[q] == j for pi, _ in pm)
    in_all = all(pi[q] == j for pi, _ in pm)
    # det sign coherence: all phase-free matchings contribute a single
    # real sign each; det(Yu Yd) structural arg in {0, pi} iff the phase
    # edge is in no matching of its sector.
    return {
        "n_matchings_u": len(mu),
        "n_matchings_d": len(md),
        "phase_in_any_matching": in_any,
        "phase_in_all_matchings": in_all,
        "real_det_structural": not in_any,
        "det_phase_form": (
            "real_monomial" if not in_any
            else "z_times_monomial" if in_all and len(pm) == 1
            else "A_plus_zB"
        ),
    }


def main():
    t0 = time.time()
    # ---- enumerate all viable one-cycle supports (WP13 class) ----
    pm_cache = {}
    supports = []
    for mu in range(512):
        ku = bin(mu).count("1")
        if not (3 <= ku <= 6):
            continue
        pm_cache.setdefault(mu, perfect_matchings(mu))
        if not pm_cache[mu]:
            continue
        for md in range(512):
            if bin(md).count("1") != 9 - ku:
                continue
            pm_cache.setdefault(md, perfect_matchings(md))
            if not pm_cache[md]:
                continue
            cyc = unique_cycle_edges(mu, md)
            if cyc is None:
                continue
            supports.append((mu, md, cyc))
    print(f"viable one-cycle supports: {len(supports)} "
          f"({time.time()-t0:.0f}s)", flush=True)

    orbits = {}
    for mu, md, cyc in supports:
        orbits.setdefault(canonical_form(mu, md), []).append((mu, md, cyc))
    print(f"orbits: {len(orbits)} ({time.time()-t0:.0f}s)", flush=True)

    # ---- census A: orbit representatives, phase on each cycle edge ----
    orbit_cases = []
    class_hist = {}
    for canon, members in sorted(orbits.items()):
        mu, md, cyc = members[0]
        for e in sorted(cyc, key=lambda x: tuple(sorted(x))):
            sector, slot = decode_cycle_edge(e)
            r = analyze_case(mu, md, sector, slot)
            cls = r["det_phase_form"]
            class_hist[cls] = class_hist.get(cls, 0) + 1
            orbit_cases.append({
                "member": [mu, md], "phase_edge": [sector, *slot],
                "cycle_length": len(cyc), **r})
    print(f"orbit phase cases: {len(orbit_cases)}  classes: {class_hist}",
          flush=True)

    # ---- census B: FULL support-level counts (all 6552 supports, every
    # cycle-edge phase placement), for comparison with the paper's
    # texture census ----
    full_real = 0
    full_total = 0
    for mu, md, cyc in supports:
        mu_m = pm_cache[mu]
        md_m = pm_cache[md]
        for e in cyc:
            sector, slot = decode_cycle_edge(e)
            pm = mu_m if sector == "u" else md_m
            q, j = slot
            if not any(pi[q] == j for pi, _ in pm):
                full_real += 1
            full_total += 1
    print(f"full support-level phase cases: {full_total}, "
          f"real-det-structural: {full_real} ({time.time()-t0:.0f}s)",
          flush=True)

    # ---- census C: the 61 fitted charts (all over one physical point) ----
    with open("results/wp9_lo_atlas.json", encoding="utf-8") as f:
        charts = json.load(f)["charts"]
    fitted = []
    n_fitted_real = 0
    for ch in charts:
        mu, md = ch["member"]
        sec = ch["phase_edge"][0]
        slot = (ch["phase_edge"][1], ch["phase_edge"][2])
        r = analyze_case(mu, md, sec, slot)
        n_fitted_real += r["real_det_structural"]
        fitted.append({"orbit": ch["orbit"], "member": [mu, md],
                       "phase_edge": ch["phase_edge"], **r})
    print(f"fitted charts: {len(fitted)}, real-det-structural: "
          f"{n_fitted_real}", flush=True)

    # ---- regression vs WP5 worked textures ----
    with open("results/wp5_matching_reality.json", encoding="utf-8") as f:
        wp5 = json.load(f)["textures"]
    worked = {
        "example_I_S38": (0b100011010, 0b100111010, "u", (0, 1)),
        "example_II_S43": (0b100010101, 0b110100101, "d", (2, 2)),
        "example_III_S48": (0b100110001, 0b101010110, "d", (0, 1)),
        "pi_over_4_S53": (0b100110001, 0b110011100, "d", (1, 1)),
    }
    regress = {}
    for name, (mu, md, sec, slot) in worked.items():
        r = analyze_case(mu, md, sec, slot)
        prior = wp5[name]
        ok = (r["phase_in_any_matching"] ==
              prior["phase_edge_in_any_matching"]
              and r["n_matchings_u"] == prior["sectors"]["u"]["n_matchings"]
              and r["n_matchings_d"] == prior["sectors"]["d"]["n_matchings"])
        regress[name] = {"match": ok,
                         "phase_in_any": r["phase_in_any_matching"],
                         "prior": prior["phase_edge_in_any_matching"]}
        print(f"regress {name}: {'OK' if ok else 'MISMATCH'}", flush=True)

    # ---- cross-tabulation vs WP13 zero-dichotomy orbits ----
    zero_orbits = {(84, 119), (85, 118), (85, 220)}
    zero_cases = [c for c in orbit_cases
                  if tuple(c["member"]) in zero_orbits]
    zero_real = sum(c["real_det_structural"] for c in zero_cases)

    out = {
        "purpose": "WP14 support-general perfect-matching census: is the "
                   "loop phase able to avoid every determinant matching "
                   "(structural real det(Yu Yd)), over all one-cycle "
                   "nine-link topologies and over the 61-vertex fitted "
                   "carrier groupoid (brief WP5 residue, falsifier #4)",
        "typing_caution": "arg det(Yu Yd) is not U(3)^3 weak-basis "
                          "invariant; only theta-bar = theta + arg det is "
                          "physical.  This census measures a chart-"
                          "combinatorial property only; it does not "
                          "address spontaneous CP, radiative stability, "
                          "or strong CP itself.",
        "viable_support_count": len(supports),
        "orbit_count": len(orbits),
        "orbit_phase_cases": len(orbit_cases),
        "orbit_class_histogram": class_hist,
        "full_support_level": {
            "phase_cases": full_total,
            "real_det_structural": full_real,
            "fraction_real": f"{full_real}/{full_total}",
        },
        "fitted_charts": {
            "count": len(fitted),
            "real_det_structural": n_fitted_real,
            "uniform": n_fitted_real in (0, len(fitted)),
            "charts": fitted,
        },
        "wp5_regression": regress,
        "wp5_regression_all_match": all(v["match"] for v in regress.values()),
        "wp13_zero_orbit_cross_tab": {
            "zero_orbit_cases": len(zero_cases),
            "real_det_structural_among_them": zero_real,
        },
        "orbit_cases": orbit_cases,
    }
    with open("results/wp14_matching_determinant_census.json", "w",
              encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(json.dumps({k: v for k, v in out.items()
                      if k not in ("orbit_cases", "fitted_charts")},
                     indent=2)[:1800])
    print(f"elapsed {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main()
