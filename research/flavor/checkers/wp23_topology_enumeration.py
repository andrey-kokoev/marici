#!/usr/bin/env python3
"""WP23a: topology-general enumeration of the WP22 a1 classification
over ALL connected one-cycle nine-link textures, not just the 755
viable ones.

A nine-link texture pair (mask_u, mask_d) has 9 nonzero entries total
across the two 3x3 Yukawa matrices. Entry 1054 hypothesis:
both sectors full-rank (perfect matching each); only such
topologies are enumerated here. The bipartite graph on the 9 field
nodes (3 Q rows, 3 u cols, 3 d cols) then has V = 9, E = 9, hence
b1 = 1 iff connected. Splits (k, 9-k) for k in {3,4,5,6}.

The phase edge is placed canonically on the first (sorted) edge of the
unique cycle; node rephasings make tree placement gauge and cycle
placement equivalent up to the chart groupoid, so one canonical
placement per topology suffices for the structural classification
(per-texture phase-placement robustness is a separate question).

For each topology the WP22 analyze() is run symbolically and the
predicted class recorded. Off-ensemble textures may have no decomposed
sector, or both sectors decomposed; these are recorded as boundary
classes, not silently dropped.

Sanity anchor: split census must reproduce
  (3,6)=2106, (4,5)=8019, (5,4)=8019, (6,3)=2106  (total 20250).

Writes: results/wp23_topology_enumeration.json
"""
import sys, os, json, collections, itertools

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wp22_w_identification import analyze, mask_slots, cycle_nodes, SLOTS

MASKS_BY_POP = collections.defaultdict(list)
for m in range(512):
    MASKS_BY_POP[bin(m).count("1")].append(m)


def has_perfect_matching(slots):
    """Bipartite PM on 3+3: some permutation sigma with all (i,sigma(i)) in slots."""
    import itertools as _it
    S = set(slots)
    return any(all((i, s[i]) in S for i in range(3))
               for s in _it.permutations(range(3)))


def connected(mu, md):
    parent = {n: n for n in
              [("Q", i) for i in range(3)] + [("u", j) for j in range(3)]
              + [("d", j) for j in range(3)]}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    def union(a, b):
        parent[find(a)] = find(b)
    for i, j in mask_slots(mu):
        union(("Q", i), ("u", j))
    for i, j in mask_slots(md):
        union(("Q", i), ("d", j))
    return len({find(n) for n in parent}) == 1


def canonical_phase_edge(mu, md):
    cyc = cycle_nodes(mu, md)
    edges = []
    for i, j in mask_slots(mu):
        if ("Q", i) in cyc and ("u", j) in cyc:
            edges.append(("u", i, j))
    for i, j in mask_slots(md):
        if ("Q", i) in cyc and ("d", j) in cyc:
            edges.append(("d", i, j))
    edges.sort()
    return edges[0] if edges else None, len(edges)


def enumerate_topologies():
    tops = []
    unfiltered = collections.Counter()
    for k in (3, 4, 5, 6):
        for mu in MASKS_BY_POP[k]:
            for md in MASKS_BY_POP[9 - k]:
                if connected(mu, md):
                    unfiltered[k] += 1
                    if not (has_perfect_matching(mask_slots(mu))
                            and has_perfect_matching(mask_slots(md))):
                        continue
                    pe, nce = canonical_phase_edge(mu, md)
                    tops.append((mu, md, pe, nce, k))
    return tops, unfiltered


def _disjoint_pair_count(slots):
    colsets = collections.defaultdict(set)
    for i, j in slots:
        colsets[i].add(j)
    return sum(1 for i in range(3) for j in range(i + 1, 3)
               if not (colsets[i] & colsets[j]))


def detc_zero_predicate(mu, md):
    """Certified rule (WP23a): detC == 0 identically iff
    (decomposed sector diagonal AND connected-sector disjoint pairs >= 1)
    or (decomposed sector block21 AND connected-sector disjoint pairs >= 2)."""
    from wp22_w_identification import blocks_of
    us, ds = mask_slots(mu), mask_slots(md)
    bu, bd = blocks_of(us), blocks_of(ds)
    sec = "u" if len(bu) >= 2 else "d"
    bl = bu if sec == "u" else bd
    con = ds if sec == "u" else us
    n = _disjoint_pair_count(con)
    if len(bl) == 3:
        return n >= 1
    return n >= 2


def worker(arg):
    mu, md, pe, nce, k = arg
    name = f"{mu}_{md}"
    if pe is None:
        return name, {"split": k, "anomaly": "no_cycle_edge"}, nce
    try:
        r = analyze(mu, md, pe)
    except Exception as e:
        r = {"error": f"{type(e).__name__}: {e}"}
    r["split"] = k
    return name, r, nce


def main():
    tops, unfiltered = enumerate_topologies()
    split_counts = collections.Counter(t[4] for t in tops)
    expected = {3: 2106, 4: 8019, 5: 8019, 6: 2106}
    anchor_ok = dict(unfiltered) == expected
    print("unfiltered connected:", dict(sorted(unfiltered.items())),
          "anchor ok:", anchor_ok, flush=True)
    print("full-rank topologies:", len(tops), "splits:",
          dict(sorted(split_counts.items())), flush=True)

    from multiprocessing import Pool
    census, class_counts, anomalies = {}, collections.Counter(), []
    nce_counts = collections.Counter()
    done = 0
    with Pool(processes=8) as pool:
        for name, r, nce in pool.imap_unordered(worker, tops, chunksize=16):
            census[name] = r
            nce_counts[nce] += 1
            class_counts[r.get("class", r.get("anomaly", "ERROR"))] += 1
            if "error" in r or "anomaly" in r:
                anomalies.append(name)
            done += 1
            if done % 1000 == 0:
                print(f"{done}/{len(tops)}", flush=True)
    verified = sum(1 for r in census.values() if "sign" in r)
    # detC_zero structural rule cross-tab (certified iff on this census)
    pred_tab = collections.Counter()
    for name, r in census.items():
        mu, md = map(int, name.split("_"))
        pred = detc_zero_predicate(mu, md)
        actual = r.get("anomaly") == "detC_zero"
        pred_tab[(pred, actual)] += 1
    zero_rule_ok = set(pred_tab) <= {(True, True), (False, False)}
    out = {
        "purpose": "WP23a topology-general enumeration of the WP22 a1 "
                   "classification over all connected one-cycle nine-link "
                   "textures (canonical cycle phase placement)",
        "n_topologies": len(census),
        "split_counts_unfiltered_connected": dict(sorted(unfiltered.items())),
        "split_counts": dict(sorted(split_counts.items())),
        "split_anchor_expected": expected,
        "rank_filter": "both sectors have a perfect matching (entry 1054 hypothesis)",
        "split_anchor_ok": anchor_ok,
        "cycle_edge_counts": dict(sorted(nce_counts.items())),
        "n_verified": verified,
        "class_counts": dict(class_counts),
        "anomalies": sorted(anomalies),
        "detc_zero_rule": "detC==0 iff (diag sector AND connected-sector "
                          "disjoint row pairs >= 1) or (block21 sector AND "
                          "connected-sector disjoint row pairs >= 2)",
        "detc_zero_rule_crosstab": {str(k): v for k, v in sorted(pred_tab.items())},
        "detc_zero_rule_ok": zero_rule_ok,
        "census": census,
    }
    with open("results/wp23_topology_enumeration.json", "w",
              encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print("classes:", dict(class_counts))
    print("detC_zero rule crosstab:", dict(pred_tab), "ok:", zero_rule_ok)
    print(f"verified {verified}/{len(census)}; anomalies: {len(anomalies)}")
    print("-> results/wp23_topology_enumeration.json")


if __name__ == "__main__":
    main()
