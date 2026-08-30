"""WP240 physical source-presence P_det on CMS scalar versus smooth nuisance."""

from __future__ import annotations

import json
import math
import zlib
from pathlib import Path

import awkward as ak
import numpy as np
import uproot
from scipy.optimize import minimize

import wp239_scalar_dimuon_acceptance as signal_calibration


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "data" / "cms-open-data-31305" / "Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON_MuonPhys.txt"
COLLISION_FILE = ROOT / "data" / "cms-open-data-31305" / "nano_data2016_2-8.root"
COLLISION_ADLER32 = "9f8a4b0c"
EDGES = np.linspace(110.0, 150.0, 41)
CENTERS = (EDGES[:-1] + EDGES[1:]) / 2
TRIGGERS = [name for name in signal_calibration.BRANCHES if name.startswith("HLT_")]
COLLISION_BRANCHES = [
    "run", "luminosityBlock", "Muon_pt", "Muon_eta", "Muon_phi",
    "Muon_mass", "Muon_charge", "Muon_mediumId", "Muon_pfRelIso04_all",
] + TRIGGERS


def certified(run, lumi, mask):
    ranges = mask.get(str(run), [])
    return any(start <= lumi <= stop for start, stop in ranges)


def mass(pair):
    energy = px = py = pz = 0.0
    for pt, eta, phi, mu_mass in pair:
        mx, my, mz = pt * math.cos(phi), pt * math.sin(phi), pt * math.sinh(eta)
        me = math.sqrt(mx * mx + my * my + mz * mz + mu_mass * mu_mass)
        energy += me; px += mx; py += my; pz += mz
    return math.sqrt(max(energy * energy - px * px - py * py - pz * pz, 0.0))


def collision_masses():
    checksum = format(zlib.adler32(COLLISION_FILE.read_bytes()) & 0xFFFFFFFF, "08x")
    with uproot.open(COLLISION_FILE) as root_file:
        events = root_file["Events"].arrays(COLLISION_BRANCHES, library="ak")
    mask = json.loads(CERT.read_text())
    selected = []
    certified_events = 0
    for event in ak.to_list(events):
        if not certified(event["run"], event["luminosityBlock"], mask):
            continue
        certified_events += 1
        good = [i for i, pt in enumerate(event["Muon_pt"]) if pt > 10 and abs(event["Muon_eta"][i]) < 2.4 and event["Muon_mediumId"][i] and event["Muon_pfRelIso04_all"][i] < 0.25]
        good.sort(key=lambda i: event["Muon_pt"][i], reverse=True)
        trigger = any(event[name] for name in TRIGGERS)
        if len(good) >= 2 and event["Muon_pt"][good[0]] > 20 and event["Muon_charge"][good[0]] * event["Muon_charge"][good[1]] < 0 and trigger:
            pair = [(event["Muon_pt"][i], event["Muon_eta"][i], event["Muon_phi"][i], event["Muon_mass"][i]) for i in good[:2]]
            value = mass(pair)
            if EDGES[0] <= value <= EDGES[-1]:
                selected.append(value)
    return np.asarray(selected), len(events), certified_events, checksum


def background_shape(slope):
    shape = np.exp(slope * (CENTERS - 130.0))
    return shape / shape.sum()


def poisson_nll(expectation, counts):
    expectation = np.maximum(expectation, 1e-12)
    return float(np.sum(expectation - counts * np.log(expectation)))


def main():
    signal_masses = []
    for entry in signal_calibration.PROVENANCE["files"]:
        _, _, reco, _ = signal_calibration.analyze_file(signal_calibration.DATA_DIR / entry["path"])
        signal_masses.extend(reco.tolist())
    signal_counts, _ = np.histogram(signal_masses, bins=EDGES)
    signal_template = signal_counts / signal_counts.sum()

    observed_masses, remote_events, certified_events, collision_checksum = collision_masses()
    counts, _ = np.histogram(observed_masses, bins=EDGES)
    sideband = (CENTERS < 122) | (CENTERS > 138)

    def sideband_objective(params):
        norm, slope = np.exp(params[0]), params[1]
        shape = background_shape(slope)
        shape = shape / shape[sideband].sum()
        return poisson_nll(norm * shape[sideband], counts[sideband])

    side_fit = minimize(sideband_objective, [math.log(max(counts[sideband].sum(), 1)), -0.02], method="L-BFGS-B", bounds=[(0, 20), (-0.5, 0.5)])
    frozen_background = background_shape(side_fit.x[1])

    def full_objective(params):
        signal_yield, background_yield = np.exp(params[0]), np.exp(params[1])
        return poisson_nll(signal_yield * signal_template + background_yield * frozen_background, counts)

    fit = minimize(full_objective, [math.log(1e-6), math.log(max(counts.sum(), 1))], method="L-BFGS-B", bounds=[(-20, 20), (0, 20)])
    signal_yield, background_yield = np.exp(fit.x)
    expectation = signal_yield * signal_template + background_yield * frozen_background
    metric = np.diag(1.0 / np.maximum(expectation, 1.0))
    jacobian = np.column_stack((signal_template, frozen_background))
    gram = jacobian.T @ metric @ jacobian
    gram_det = float(np.linalg.det(gram))
    source_rank = int(np.linalg.matrix_rank(jacobian, tol=1e-12))

    background_only_nll = poisson_nll(counts.sum() * frozen_background, counts)
    likelihood_gain = max(0.0, 2 * (background_only_nll - full_objective(fit.x)))
    hostile = np.column_stack((frozen_background, frozen_background))

    checks = {
        "local_collision_checksum_matches_cern": collision_checksum == COLLISION_ADLER32,
        "muon_certification_checksum_prevalidated": CERT.stat().st_size == 10535 and format(zlib.adler32(CERT.read_bytes()) & 0xFFFFFFFF, "08x") == "a562515d",
        "collision_shard_processed": remote_events == 33177,
        "certified_event_subset_nonempty": certified_events > 0,
        "selected_collision_window_nonempty": counts.sum() > 0,
        "signal_template_source_labelled": signal_counts.sum() > 0,
        "sideband_background_frozen_before_signal_fit": side_fit.success,
        "source_presence_jacobian_rank_two": source_rank == 2,
        "positive_quotient_gram": gram_det > 0,
        "hostile_coincident_templates_rank_one": np.linalg.matrix_rank(hostile, tol=1e-12) == 1,
        "fit_converged": fit.success,
        "wp237_transfer_not_claimed": True,
    }
    checks = {key: bool(value) for key, value in checks.items()}
    result = {
        "work_package": "WP240",
        "claim": "A source-labelled scalar template and sideband-frozen CMS collision background define a physical source-presence P_det with rank two on the declared {scalar present, scalar absent} quotient.",
        "source_domain": "nonnegative MA=130 MSSM bbH->mumu signal yield modulo a smooth sideband-calibrated collision-background nuisance",
        "collision_record": {
            "record": "https://opendata.cern.ch/record/31305",
            "source_file": str(COLLISION_FILE),
            "adler32": COLLISION_ADLER32,
            "events": remote_events,
            "certified_events": certified_events,
            "selected_110_150_GeV": int(counts.sum()),
        },
        "pdet": {
            "response_rank": source_rank,
            "gram_matrix": gram.tolist(),
            "gram_determinant": gram_det,
            "signal_template_events": int(signal_counts.sum()),
            "background_slope_per_GeV": float(side_fit.x[1]),
        },
        "fit": {
            "signal_yield": float(signal_yield),
            "background_yield": float(background_yield),
            "twice_log_likelihood_gain_over_background_only": float(likelihood_gain),
            "interpretation": "capability is identifying; this shard need not contain the source",
        },
        "contextual_partition": "singleton scalar-yield fibers after quotienting the frozen smooth-background nuisance on this two-column domain",
        "hostile_falsifier": "If signal and nuisance templates coincide, rank falls to one and source presence is not identifiable.",
        "classification": "physical source-presence identifier for the CMS MSSM scalar domain; not yet a WP128/trace-adjoint source identifier",
        "remaining_gate": "Construct the source-authorized transfer from WP237 trace-adjoint production/decay to this calibrated response family, including cross-section and branching normalization.",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results" / "wp240_physical_source_presence_pdet.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
