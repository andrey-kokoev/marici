#!/usr/bin/env python3
"""WP23d: phase-placement independence audit. The WP22/WP23a
classification used one canonical cycle-edge phase placement per
topology. Rephasing moves the phase around the unique cycle (tree
placements are gauge), so the class labels should be invariant under
which cycle edge carries z; signs may flip. This checker runs the full
WP22 analysis for EVERY cycle-edge placement on every full-rank
one-cycle topology and records per-topology label sets.

Expected: each topology has exactly one class label across all its
cycle-edge placements (detC_zero included). Any topology with two
different non-zero classes, or mixed zero/nonzero, is an anomaly that
breaks the classification's chart-groupoid covariance.

Writes: results/wp23d_phase_placement_audit.json
"""
import sys, os, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wp22_w_identification import analyze, mask_slots, cycle_nodes
from wp23_topology_enumeration import enumerate_topologies


def all_phase_edges(mu, md):
    cyc = cycle_nodes(mu, md)
    edges = []
    for i, j in mask_slots(mu):
        if ("Q", i) in cyc and ("u", j) in cyc:
            edges.append(("u", i, j))
    for i, j in mask_slots(md):
        if ("Q", i) in cyc and ("d", j) in cyc:
            edges.append(("d", i, j))
    return sorted(edges)


def worker(arg):
    mu, md, _pe, _nce, k = arg
    name = f"{mu}_{md}"
    labels = {}
    for pe in all_phase_edges(mu, md):
        try:
            r = analyze(mu, md, pe)
        except Exception as e:
            r = {"error": f"{type(e).__name__}: {e}"}
        lab = r.get("class", r.get("anomaly", "ERROR"))
        labels[f"{pe[0]}{pe[1]}{pe[2]}"] = lab
    return name, {"split": k, "labels": labels,
                  "distinct": sorted(set(labels.values()))}


def main():
    tops, _unf = enumerate_topologies()
    print("topologies:", len(tops), flush=True)
    from multiprocessing import Pool
    census = {}
    anomalies = []
    label_pair_counts = collections.Counter()
    done = 0
    with Pool(processes=8) as pool:
        for name, r in pool.imap_unordered(worker, tops, chunksize=8):
            census[name] = r
            if len(r["distinct"]) != 1:
                anomalies.append(name)
                label_pair_counts[tuple(r["distinct"])] += 1
            done += 1
            if done % 500 == 0:
                print(f"{done}/{len(tops)} anomalies={len(anomalies)}", flush=True)
    out = {
        "purpose": "WP23d phase-placement independence of the a1 class "
                   "labels across all cycle-edge placements",
        "n_topologies": len(census),
        "n_label_consistent": len(census) - len(anomalies),
        "n_anomalies": len(anomalies),
        "anomaly_label_sets": {str(k): v for k, v in label_pair_counts.items()},
        "anomalies": sorted(anomalies),
        "census": census,
    }
    with open("results/wp23d_phase_placement_audit.json", "w",
              encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print(f"consistent {len(census)-len(anomalies)}/{len(census)}; "
          f"anomalies {len(anomalies)}; label sets: {dict(label_pair_counts)}")


if __name__ == "__main__":
    main()
