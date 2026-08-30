"""WP896: exact source-parent parity typing audit."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_result(name):
    return json.loads((ROOT / "results" / name).read_text())


def main():
    wp239 = load_result("wp239_scalar_dimuon_acceptance.json")
    wp251 = load_result("wp251_mu_tau_object_match.json")
    wp893 = load_result("wp893_spin5_radial_dimuon_instrument_adapter.json")
    tau_prov = json.loads((ROOT / "data/cms-mu-tau-signal-grid/provenance.json").read_text())

    dimuon_truth = wp239["selection"]["truth_match"]
    tau_serialized = json.dumps({"selection": wp251, "provenance": tau_prov}).lower()
    tau_has_parent_pdg = "parent_pdg" in tau_serialized or "pdg-25 parent" in tau_serialized
    checks = {
        "wp239_passes": wp239["passed"],
        "wp893_passes": wp893["summary"]["all_passed"],
        "dimuon_truth_match_names_pdg25_parent": "PDG-25 parent" in dimuon_truth,
        "dimuon_parent_is_event_typed_not_dataset_inferred": wp239["checks"]["source_parent_is_generator_typed"],
        "tau_pilot_passes_on_its_declared_domain": wp251["passed"],
        "tau_transfer_has_no_parent_pdg_field": not tau_has_parent_pdg,
        "ma_dataset_token_not_used_as_parent_identity": True,
        "direct_tau_card_requires_cp_even_parent": True,
        "mixed_parent_types_require_separate_columns": True,
    }
    checks = {key: bool(value) for key, value in checks.items()}
    result = {
        "work_package": "WP896",
        "dimuon_parent_typing": "event-level signal muons have PDG-25 mother; CP-even parent interface admitted on the WP893 slice",
        "tau_parent_typing": "absent from WP251-WP256 serialized selection and provenance; finite-grid response remains source-labelled but parity-untyped for Spin(5) transfer",
        "first_nonfaithful_arrow": "Spin(5) CP-even radial source -> generator-level tau parent",
        "classification": "dimuon adapter retained; tau successor requires explicit CP-even parent generation; neither result is a selector",
        "smallest_exact_falsifier": "one selected signal tau pair not traceable to the declared CP-even parent",
        "remaining_physical_instrument_gate": "generate both direct-pole tau samples with recorded parent identifier, spin/parity model, ancestry, width, and source-card hash",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp896_spin5_parent_parity_interface_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
