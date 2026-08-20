"""Local phase-identifiability audit for the viable oriented flavor ensemble.

At each deduplicated viable minimum compute the standardized 17x10 observable
Jacobian with respect to nine log magnitudes and the loop phase. Project the
phase column away from the magnitude-column span. The squared residual norm is
the profile/Schur phase information: physical readout sensitivity that cannot
be reproduced by infinitesimal magnitude retuning.
"""
import json
import math
import sys
from pathlib import Path

import numpy as np
from scipy.stats import pearsonr, spearmanr

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from wp7_ensemble import build_texture, observables17, SIGMA  # noqa: E402

ROOT = HERE.parents[0]
RESULTS = ROOT / "results"


def standardized_observables(theta, mu, md, phase_edge):
    Yu, Yd = build_texture(mu, md, phase_edge[0],
                           tuple(phase_edge[1:]), theta)
    return observables17(Yu, Yd)/SIGMA


def local_information(record, step_scale=1.0):
    mu, md = record["member"]
    theta = np.array(record["log_mags"]+[record["phi"]], dtype=float)
    phase_edge = record["phase_edge"]
    base = standardized_observables(theta, mu, md, phase_edge)
    jac = np.empty((17, 10))
    for j in range(10):
        h = step_scale*(2e-6 if j < 9 else 1e-6)
        plus, minus = theta.copy(), theta.copy()
        plus[j] += h; minus[j] -= h
        jac[:, j] = (
            standardized_observables(plus, mu, md, phase_edge) -
            standardized_observables(minus, mu, md, phase_edge)
        )/(2*h)
    jm, jp = jac[:, :9], jac[:, 9]
    coeff, *_ = np.linalg.lstsq(jm, jp, rcond=1e-10)
    profiled = jp-jm@coeff
    singular = np.linalg.svd(jac, compute_uv=False)
    return {
        "phase_column_information": float(jp@jp),
        "profiled_phase_information": float(profiled@profiled),
        "profiled_fraction": float((profiled@profiled)/(jp@jp))
            if jp@jp > 0 else 0.0,
        "jacobian_rank": int(np.linalg.matrix_rank(jac, tol=1e-7)),
        "smallest_singular_value": float(singular[-1]),
        "largest_singular_value": float(singular[0]),
        "condition_number": float(singular[0]/singular[-1])
            if singular[-1] > 0 else math.inf,
        "finite_difference_base_norm": float(np.linalg.norm(base)),
    }


records = []
orig = json.loads((RESULTS / "wp7_ensemble.json").read_text())
for orbit in orig["orbits"]:
    for m in orbit["viable_minima"]:
        records.append({"orientation": "original",
                        "orbit": orbit["orbit_index"], **m})
for orbit in range(18):
    path = RESULTS / f"wp10_sector_swapped_orbit{orbit}_pilot.json"
    if not path.exists():
        continue
    packet = json.loads(path.read_text())
    for m in packet["viable_minima"]:
        records.append({"orientation": "sector_swapped",
                        "orbit": orbit, **m})

# Remove symmetry/search copies using the same strict key as the cycle audit.
dedup = {}
for rec in records:
    key = (rec["orientation"], rec["orbit"], round(rec["phi_folded"], 6),
           round(rec["chi2"], 6))
    dedup.setdefault(key, rec)
records = list(dedup.values())

for i, rec in enumerate(records):
    primary = local_information(rec)
    refined = local_information(rec, step_scale=0.5)
    denom = max(primary["profiled_phase_information"],
                refined["profiled_phase_information"], 1e-300)
    primary["step_refinement_relative_difference"] = abs(
        primary["profiled_phase_information"] -
        refined["profiled_phase_information"])/denom
    rec.update(primary)

phi = np.array([r["phi_folded"] for r in records])
info = np.array([r["profiled_phase_information"] for r in records])
fraction = np.array([r["profiled_fraction"] for r in records])
step_error = np.array(
    [r["step_refinement_relative_difference"] for r in records])
log_info = np.log10(np.maximum(info, 1e-300))

pear = pearsonr(phi, log_info)
spear = spearmanr(phi, log_info)

# Within-oriented-orbit fixed effects.
keys = sorted({(r["orientation"], r["orbit"]) for r in records})
p0, i0 = np.empty_like(phi), np.empty_like(log_info)
group_summary = []
for key in keys:
    idx = np.array([(r["orientation"], r["orbit"]) == key for r in records])
    p0[idx] = phi[idx]-phi[idx].mean()
    i0[idx] = log_info[idx]-log_info[idx].mean()
    group_summary.append({
        "orientation": key[0], "orbit": key[1], "count": int(idx.sum()),
        "phi_mean": float(phi[idx].mean()),
        "log10_profiled_information_mean": float(log_info[idx].mean()),
        "profiled_fraction_median": float(np.median(fraction[idx])),
    })
within = pearsonr(p0, i0)

quantiles = np.quantile(phi, [0, .25, .5, .75, 1])
phase_bins = []
for k in range(4):
    sel = ((phi >= quantiles[k]) &
           (phi <= quantiles[k+1] if k == 3 else phi < quantiles[k+1]))
    phase_bins.append({
        "phi_interval": [float(quantiles[k]), float(quantiles[k+1])],
        "count": int(sel.sum()),
        "profiled_information_median": float(np.median(info[sel])),
        "profiled_fraction_median": float(np.median(fraction[sel])),
        "full_rank_fraction": float(np.mean(
            np.array([r["jacobian_rank"] for r in records])[sel] == 10)),
    })

out = {
    "schema": "marici.flavor.local_phase_identifiability.v1",
    "status": "finite_difference_profile_jacobian_audit",
    "sample_count": len(records),
    "definition":
        "squared norm of phase observable derivative after orthogonal projection off nine log-magnitude derivatives",
    "global_phi_log_information_pearson":
        {"statistic": float(pear.statistic), "pvalue": float(pear.pvalue)},
    "global_phi_log_information_spearman":
        {"statistic": float(spear.statistic), "pvalue": float(spear.pvalue)},
    "within_oriented_orbit_pearson":
        {"statistic": float(within.statistic), "pvalue": float(within.pvalue)},
    "rank10_fraction": float(np.mean(
        [r["jacobian_rank"] == 10 for r in records])),
    "profiled_fraction_quantiles":
        [float(x) for x in np.quantile(fraction, [0, .25, .5, .75, 1])],
    "step_refinement_relative_difference_quantiles":
        [float(x) for x in np.quantile(step_error, [0, .25, .5, .75, 1])],
    "phase_quartile_summary": phase_bins,
    "group_summary": group_summary,
    "records": records,
}
(RESULTS / "wp10_local_phase_identifiability.json").write_text(
    json.dumps(out, indent=2)+"\n", encoding="utf-8")
print(json.dumps({k:v for k,v in out.items()
                  if k not in ("records", "group_summary")}, indent=2))
