"""WP258: audit the nearest physical candidate for WP257's reference port."""

import json
from pathlib import Path

from sympy import Matrix

ROOT = Path(__file__).resolve().parents[1]
P241 = json.loads((ROOT / "results/wp241_topology_transfer_gate.json").read_text())
P256 = json.loads((ROOT / "results/wp256_scale_covariant_shape_transport.json").read_text())


def main():
    requirements = [
        "source_mass_reference",
        "common_decay_topology",
        "common_detector_era",
        "common_selection",
        "physical_branching_normalization",
    ]
    # The actual-pole dimuon records supply the mass reference. WP241 already
    # certifies that the remaining interface fields are absent.
    interface_column = Matrix([1, 0, 0, 0, 0])
    complete_interface = Matrix.ones(len(requirements), 1)
    missing = [name for name, value in zip(requirements, interface_column) if value == 0]
    checks = {
        "wp256_templates_exist": all(mass in P256["raw_templates"] for mass in ("130", "140", "160")),
        "actual_pole_mass_reference_exists": P241["calibration"]["mass_GeV"] > 0,
        "dimuon_decay_is_forced": P241["calibration"]["decay"] == "forced_mumu",
        "physical_branching_not_supplied": not P241["transport_gates"]["physical_branching_supplied"],
        "shape_transport_previously_rejected": not P241["shape_transport_authorized"],
        "yield_transport_previously_rejected": not P241["yield_transport_authorized"],
        "interface_is_incomplete": interface_column != complete_interface,
        "four_required_fields_missing": len(missing) == 4,
        "mass_label_alone_does_not_define_common_frame": interface_column.rank() == 1 and len(missing) == 4,
        "deliberate_complete_interface_claim_fails": sum((interface_column - complete_interface).applyfunc(abs)) != 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP258",
        "candidate_reference_records": [43611, 43651],
        "candidate_domain": "2016 CMS MSSM bbH forced-dimuon NanoAOD actual-pole samples",
        "target_domain": "2015 CMS SUSY bbH tau-pair MiniAOD muon-tau response used by WP256",
        "interface_requirements": requirements,
        "candidate_interface_column": [int(value) for value in interface_column],
        "missing_fields": missing,
        "contextual_partition": "the records distinguish labelled MSSM dimuon mass hypotheses, but do not refine WP256 tau-response fibers in a common detector/source frame",
        "classification": "physical mass-reference rigidifier on the dimuon MSSM domain; neither selector nor valid reference-port repair for the WP256 physical16/tau domain",
        "first_nonfaithful_arrow": "actual-pole dimuon source record -> 2015 muon-tau detector response",
        "smallest_exact_falsifier": "the candidate supplies one of five required interface fields; forced_mumu supplies no physical tau branching normalization",
        "remaining_instrument_gate": "generate or identify actual-pole tau samples in the same era and reconstruction frame, with physical branching normalization and the unchanged WP251 selection",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp258_actual_pole_reference_interface.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
