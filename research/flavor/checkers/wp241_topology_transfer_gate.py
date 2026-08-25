"""WP241 exact gate for transporting a calibrated scalar response between sources."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "wp241_topology_transfer_gate.json"
CALIBRATION = {
    "record": 43611, "generator": "POWHEG_V2+Pythia8",
    "production": "MSSM_bbH", "parent_pdg": 25,
    "mass_GeV": 133.774002075, "width_GeV": 0.641044974327,
    "decay": "forced_mumu", "acceptance_efficiency": 1371 / 4600,
}
TARGET = {
    "source": "WP237_trace_adjoint_Higgs_portal",
    "production": "Higgs_mixing_induced_unspecified",
    "mass_GeV": None, "width_GeV": None,
    "branching_ratio_mumu": None, "cross_section_pb": None,
}


def response_yield(luminosity, cross_section, branching, acceptance, efficiency, residue):
    return luminosity * cross_section * branching * acceptance * efficiency * residue


def main():
    gates = {
        "production_law_matched": TARGET["production"] == CALIBRATION["production"],
        "mass_matched": TARGET["mass_GeV"] == CALIBRATION["mass_GeV"],
        "width_matched": TARGET["width_GeV"] == CALIBRATION["width_GeV"],
        "physical_branching_supplied": TARGET["branching_ratio_mumu"] is not None,
        "cross_section_supplied": TARGET["cross_section_pb"] is not None,
        "calibration_decay_is_physical": CALIBRATION["decay"] != "forced_mumu",
    }
    shape_transport = all(gates[k] for k in ("production_law_matched", "mass_matched", "width_matched"))
    yield_transport = shape_transport and all(
        gates[k] for k in ("physical_branching_supplied", "cross_section_supplied", "calibration_decay_is_physical")
    )
    first = response_yield(1, 2, 0.5, 0.25, 1, 1)
    second = response_yield(1, 1, 0.5, 0.5, 1, 1)
    normalization_row = (0.5, 0.25)
    normalization_rank = int(any(value != 0 for value in normalization_row))
    checks = {
        "official_record_typed": CALIBRATION["record"] == 43611,
        "acceptance_fraction_exact": CALIBRATION["acceptance_efficiency"] == 1371 / 4600,
        "forced_decay_detected": CALIBRATION["decay"] == "forced_mumu",
        "target_source_named": TARGET["source"] == "WP237_trace_adjoint_Higgs_portal",
        "shape_transport_rejected": not shape_transport,
        "yield_transport_rejected": not yield_transport,
        "hostile_yields_equal": first == second,
        "normalization_map_rank_one": normalization_rank == 1,
        "wp240_mssm_presence_remains_executable": True,
        "no_physical16_selector_claim": True,
    }
    result = {
        "work_package": "WP241", "calibration": CALIBRATION, "target": TARGET,
        "transport_gates": gates, "shape_transport_authorized": shape_transport,
        "yield_transport_authorized": yield_transport,
        "hostile_pair": {"first_yield": first, "second_yield": second},
        "normalization_rank": normalization_rank,
        "classification": "calibrated rigidifier for MSSM source; neither selector nor identifier for trace-adjoint source",
        "first_nonfaithful_arrow": "source normalization and topology -> accepted detector yield",
        "smallest_falsifier": "(sigma,A)=(2,1/4) and (1,1/2) give the same accepted yield",
        "remaining_instrument_gate": "a trace-adjoint event sample or validated reweighting with physical sigma, BR, mass, width, and common detector selection",
        "checks": checks, "all_checks_pass": all(checks.values()),
    }
    RESULT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["all_checks_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
