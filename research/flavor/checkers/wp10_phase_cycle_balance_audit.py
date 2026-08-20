"""Exploratory phase-versus-cycle-modulus audit for the oriented WP10 ensemble.

For each viable fitted texture, order the unique graph cycle and compute
rho = |log(prod even edge moduli / prod odd edge moduli)|.
For the zero-diagonal six-link support rho=0 is exactly the source critical
locus proved by wp10_zero_diagonal_gram_discriminant.py.  For other supports
rho is only a source-defined cycle-balance coordinate, not yet a proved Gram
wall.  This audit therefore tests correlation without promoting rho to a
universal carrier distance.
"""
import json
import math
from pathlib import Path

import numpy as np
from scipy.stats import pearsonr, spearmanr

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
SLOTS = [(i, j) for i in range(3) for j in range(3)]


def mask_slots(mask):
    return [s for k, s in enumerate(SLOTS) if mask & (1 << k)]


def ordered_cycle(mu, md):
    edges = []
    adj = {n: [] for n in range(9)}
    for sec, mask, offset in (("u", mu, 3), ("d", md, 6)):
        for i, j in mask_slots(mask):
            idx = len(edges)
            edges.append((sec, i, j, i, offset+j))
            adj[i].append(idx)
            adj[offset+j].append(idx)
    degree = {n: len(adj[n]) for n in adj}
    alive_edges = set(range(len(edges)))
    queue = [n for n, d in degree.items() if d == 1]
    while queue:
        node = queue.pop()
        incident = [e for e in adj[node] if e in alive_edges]
        if not incident:
            continue
        e = incident[0]
        alive_edges.remove(e)
        *_, a, b = edges[e]
        other = b if node == a else a
        degree[other] -= 1
        if degree[other] == 1:
            queue.append(other)
    assert alive_edges
    start = min(alive_edges)
    order = []
    current_edge = start
    current_node = edges[start][3]
    while True:
        order.append(current_edge)
        *_, a, b = edges[current_edge]
        next_node = b if current_node == a else a
        choices = [e for e in adj[next_node]
                   if e in alive_edges and e != current_edge]
        assert len(choices) == 1
        nxt = choices[0]
        if nxt == start:
            break
        current_node, current_edge = next_node, nxt
    assert len(order) == len(alive_edges)
    return [(edges[e][0], edges[e][1], edges[e][2]) for e in order]


def cycle_balance(record):
    mu, md = record["member"]
    us, ds = mask_slots(mu), mask_slots(md)
    keys = [("u", *s) for s in us] + [("d", *s) for s in ds]
    logs = dict(zip(keys, record["log_mags"]))
    cyc = ordered_cycle(mu, md)
    signed = sum((1 if k % 2 == 0 else -1)*logs[edge]
                 for k, edge in enumerate(cyc))
    return abs(signed), len(cyc)


samples = []
orig = json.loads((RESULTS / "wp7_ensemble.json").read_text())
for orbit in orig["orbits"]:
    for m in orbit["viable_minima"]:
        rho, length = cycle_balance(m)
        samples.append({"orientation": "original", "orbit": orbit["orbit_index"],
                        "phi": m["phi_folded"], "rho": rho,
                        "cycle_length": length, "chi2": m["chi2"]})

for orbit in range(18):
    path = RESULTS / f"wp10_sector_swapped_orbit{orbit}_pilot.json"
    if not path.exists():
        continue
    rec = json.loads(path.read_text())
    for m in rec["viable_minima"]:
        rho, length = cycle_balance(m)
        samples.append({"orientation": "sector_swapped", "orbit": orbit,
                        "phi": m["phi_folded"], "rho": rho,
                        "cycle_length": length, "chi2": m["chi2"]})

# Remove symmetry/search copies before inference. The rounded tuple is much
# tighter than the physical fit tolerances and preserves distinct minima.
raw_sample_count = len(samples)
dedup = {}
for sample in samples:
    key = (sample["orientation"], sample["orbit"],
           round(sample["phi"], 6), round(sample["rho"], 6),
           round(sample["chi2"], 6))
    dedup.setdefault(key, sample)
samples = list(dedup.values())

phi = np.array([s["phi"] for s in samples])
rho = np.array([s["rho"] for s in samples])
assert len(samples) >= 10 and np.all(np.isfinite(phi)) and np.all(np.isfinite(rho))
pear = pearsonr(phi, rho)
spear = spearmanr(phi, rho)

# Separate within-support motion from between-support stratification.
group_keys = sorted({(s["orientation"], s["orbit"]) for s in samples})
phi_within = np.empty_like(phi)
rho_within = np.empty_like(rho)
group_means = []
for key in group_keys:
    idx = np.array([(s["orientation"], s["orbit"]) == key for s in samples])
    phi_within[idx] = phi[idx]-phi[idx].mean()
    rho_within[idx] = rho[idx]-rho[idx].mean()
    group_means.append((float(phi[idx].mean()), float(rho[idx].mean()), int(idx.sum())))
within_pear = pearsonr(phi_within, rho_within)
between_pear = pearsonr([g[0] for g in group_means],
                        [g[1] for g in group_means])

# Orbit-preserving permutation test for the within-group statistic.
rng = np.random.default_rng(20260820)
observed = abs(float(within_pear.statistic))
extreme = 0
permutations = 10000
for _ in range(permutations):
    shuffled = rho_within.copy()
    for key in group_keys:
        idx = np.flatnonzero([(s["orientation"], s["orbit"]) == key
                             for s in samples])
        shuffled[idx] = rng.permutation(shuffled[idx])
    stat = abs(float(pearsonr(phi_within, shuffled).statistic))
    extreme += stat >= observed
permutation_p = (extreme+1)/(permutations+1)

quantiles = np.quantile(rho, [0, .25, .5, .75, 1])
bins = []
for k in range(4):
    if k == 3:
        sel = (rho >= quantiles[k]) & (rho <= quantiles[k+1])
    else:
        sel = (rho >= quantiles[k]) & (rho < quantiles[k+1])
    bins.append({
        "rho_interval": [float(quantiles[k]), float(quantiles[k+1])],
        "count": int(sel.sum()),
        "phi_mean": float(phi[sel].mean()),
        "phi_std": float(phi[sel].std()),
    })

canonical = np.array([math.pi/8, math.pi/4, 3*math.pi/8, math.pi/2])
nearest = np.argmin(abs(phi[:, None]-canonical[None, :]), axis=1)
cluster_by_bin = []
for k in range(4):
    if k == 3:
        sel = (rho >= quantiles[k]) & (rho <= quantiles[k+1])
    else:
        sel = (rho >= quantiles[k]) & (rho < quantiles[k+1])
    counts = [int(np.sum(nearest[sel] == j)) for j in range(4)]
    cluster_by_bin.append(counts)

out = {
    "schema": "marici.flavor.phase_cycle_balance_audit.v1",
    "status": "exploratory_source_coordinate_audit",
    "raw_sample_count": raw_sample_count,
    "sample_count": len(samples),
    "orientation_counts": {
        key: sum(s["orientation"] == key for s in samples)
        for key in ("original", "sector_swapped")
    },
    "rho_definition":
        "absolute alternating sum of log edge moduli around the unique cycle",
    "typing_caution":
        "rho=0 is a proved Gram critical wall only for the six-link zero-diagonal support; elsewhere rho is a source coordinate",
    "pearson_phi_rho": {"statistic": float(pear.statistic), "pvalue": float(pear.pvalue)},
    "spearman_phi_rho": {"statistic": float(spear.statistic), "pvalue": float(spear.pvalue)},
    "orbit_fixed_effect_pearson": {
        "statistic": float(within_pear.statistic),
        "parametric_pvalue": float(within_pear.pvalue),
        "orbit_preserving_permutation_pvalue": permutation_p,
        "permutations": permutations,
    },
    "between_orbit_mean_pearson": {
        "statistic": float(between_pear.statistic),
        "pvalue": float(between_pear.pvalue),
        "group_count": len(group_means),
    },
    "rho_quartile_phase_summary": bins,
    "nearest_nominal_phase_counts_by_rho_quartile": cluster_by_bin,
    "nominal_phases": ["pi/8", "pi/4", "3pi/8", "pi/2"],
    "samples": samples,
}
(RESULTS / "wp10_phase_cycle_balance_audit.json").write_text(
    json.dumps(out, indent=2)+"\n", encoding="utf-8")
print(json.dumps({k: v for k, v in out.items() if k != "samples"}, indent=2))
