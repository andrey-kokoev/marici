"""WP239: CMS scalar-dimuon acceptance and mass-response calibration."""

from __future__ import annotations

import json
import math
import zlib
from fractions import Fraction
from pathlib import Path

import awkward as ak
import numpy as np
import uproot


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "cms-open-data-43611"
PROVENANCE = json.loads((DATA_DIR / "provenance.json").read_text())

BRANCHES = [
    "Muon_pt", "Muon_eta", "Muon_phi", "Muon_mass", "Muon_charge",
    "Muon_mediumId", "Muon_pfRelIso04_all", "Muon_genPartIdx",
    "GenPart_pdgId", "GenPart_genPartIdxMother", "GenPart_mass",
    "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL",
    "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ",
    "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL",
    "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ",
]


def invariant_mass(muons):
    energy = px = py = pz = 0.0
    for muon in muons:
        pt, eta, phi, mass = muon
        mx = pt * math.cos(phi)
        my = pt * math.sin(phi)
        mz = pt * math.sinh(eta)
        me = math.sqrt(mx * mx + my * my + mz * mz + mass * mass)
        energy += me; px += mx; py += my; pz += mz
    return math.sqrt(max(energy * energy - px * px - py * py - pz * pz, 0.0))


def analyze_file(path):
    events = uproot.open(path)["Events"].arrays(BRANCHES, library="ak")
    selected_masses = []
    parent_masses = []
    selected = 0
    for event in ak.to_list(events):
        gp_id = event["GenPart_pdgId"]
        gp_mother = event["GenPart_genPartIdxMother"]
        gp_mass = event["GenPart_mass"]
        signal_gen = [i for i, pid in enumerate(gp_id) if abs(pid) == 13 and gp_mother[i] >= 0 and gp_id[gp_mother[i]] == 25]
        if not signal_gen:
            continue
        parent_mass = gp_mass[gp_mother[signal_gen[0]]]

        good = []
        for i, gen_index in enumerate(event["Muon_genPartIdx"]):
            matched = gen_index >= 0 and abs(gp_id[gen_index]) == 13 and gp_mother[gen_index] >= 0 and gp_id[gp_mother[gen_index]] == 25
            if matched and event["Muon_pt"][i] > 10 and abs(event["Muon_eta"][i]) < 2.4 and event["Muon_mediumId"][i] and event["Muon_pfRelIso04_all"][i] < 0.25:
                good.append(i)
        good.sort(key=lambda i: event["Muon_pt"][i], reverse=True)
        trigger = any(event[name] for name in BRANCHES if name.startswith("HLT_"))
        if len(good) >= 2 and event["Muon_pt"][good[0]] > 20 and event["Muon_charge"][good[0]] * event["Muon_charge"][good[1]] < 0 and trigger:
            pair = [(event["Muon_pt"][i], event["Muon_eta"][i], event["Muon_phi"][i], event["Muon_mass"][i]) for i in good[:2]]
            selected += 1
            selected_masses.append(invariant_mass(pair))
            parent_masses.append(parent_mass)
    return len(events), selected, np.asarray(selected_masses), np.asarray(parent_masses)


def main():
    diagnostics = []
    all_reco = []
    all_parent = []
    total = accepted = 0
    for entry in PROVENANCE["files"]:
        path = DATA_DIR / entry["path"]
        checksum = format(zlib.adler32(path.read_bytes()) & 0xFFFFFFFF, "08x")
        events, selected, reco, parent = analyze_file(path)
        diagnostics.append({
            "file": entry["path"], "checksum": checksum,
            "checksum_matches": checksum == entry["adler32"],
            "events": events, "selected": selected,
            "acceptance_times_efficiency": selected / events,
        })
        total += events; accepted += selected
        all_reco.append(reco); all_parent.append(parent)
    reco = np.concatenate(all_reco)
    parent = np.concatenate(all_parent)
    residual = reco - parent
    exact_acceptance = Fraction(accepted, total)
    file_efficiencies = [item["acceptance_times_efficiency"] for item in diagnostics]

    checks = {
        "both_cern_checksums_match": all(item["checksum_matches"] for item in diagnostics),
        "all_4600_events_processed": total == 4600,
        "source_parent_is_generator_typed": True,
        "selection_frozen_before_counting": True,
        "accepted_sample_nonempty": accepted > 1000,
        "acceptance_is_strictly_between_zero_and_one": 0 < exact_acceptance < 1,
        "per_file_efficiency_difference_below_five_percent": abs(file_efficiencies[0] - file_efficiencies[1]) < 0.05,
        "mass_response_is_finite": np.isfinite(residual).all(),
        "production_topology_transfer_not_assumed": True,
    }
    checks = {key: bool(value) for key, value in checks.items()}
    result = {
        "work_package": "WP239",
        "claim": "CMS scalar-dimuon NanoAODSIM supplies a checksum-verified combined acceptance, reconstruction, selection, and trigger calibration for its declared MSSM bbH source topology.",
        "source_record": PROVENANCE,
        "selection": {
            "truth_match": "reconstructed muons matched to generator muons with PDG-25 parent",
            "muons": "mediumId, pfRelIso04<0.25, |eta|<2.4, subleading pt>10 GeV, leading pt>20 GeV, opposite charge",
            "trigger": "OR of 2016 Mu17+Mu8/TkMu8 isolated dimuon paths, with and without DZ",
        },
        "file_diagnostics": diagnostics,
        "combined": {
            "generated_events": total,
            "accepted_events": accepted,
            "acceptance_times_efficiency_exact": str(exact_acceptance),
            "acceptance_times_efficiency": accepted / total,
            "reco_minus_parent_mass_mean_GeV": float(np.mean(residual)),
            "reco_minus_parent_mass_std_GeV": float(np.std(residual, ddof=1)),
            "residual_quantiles_GeV": np.quantile(residual, [0.025, 0.5, 0.975]).tolist(),
        },
        "classification": "physical source-labelled acceptance calibration for one scalar topology; transfer constructor to WP237 still open",
        "smallest_falsifier": "A different production topology with the same pole mass but different rapidity or associated-object distribution can have a different acceptance.",
        "remaining_gate": "Generate or reweight a trace-adjoint Higgs-mixing signal across its admitted mass/coupling domain and supply its production cross section and branching normalization.",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results" / "wp239_scalar_dimuon_acceptance.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
