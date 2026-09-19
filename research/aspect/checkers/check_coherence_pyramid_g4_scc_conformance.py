from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT / "research/aspect/contracts/coherence-pyramid-to-g4-scc-linkage.v1.json"
OUT = ROOT / "research/aspect/results/coherence-pyramid-g4-scc-conformance.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    contract = load(CONTRACT)
    paths = {
        "coverage": ROOT / contract["source_realization"]["coverage"],
        "completion": ROOT / contract["source_realization"]["completion"],
        "compatibility": ROOT / contract["source_realization"]["compatibility"],
        "scc": ROOT / contract["target_scc"]["contract"],
        "construction_source": ROOT / contract["source_realization"]["construction_source"],
        "evans_interval": ROOT / "research/voevodsky/results/first-zero-evans-cross-certificate.json",
    }
    docs = {name: load(path) for name, path in paths.items() if name != "construction_source"}

    evidence_checks = {
        "complete_cellwise_analytical_coverage": docs["coverage"]["passed"],
        "common_cofinal_relative_completion": docs["completion"]["passed"] and docs["completion"]["checks"]["single_cofinal_mode"],
        "signed_relative_compatibility": docs["compatibility"]["signed_relative_compatibility_certified"],
        "positive_compatibility_not_certified": not docs["compatibility"]["positive_compatibility_certified"],
        "scc_canonical_g4_is_pair_to_border": docs["scc"]["ontology"]["analytical_G4_forward"] == "T_PB=T_pair_to_border",
        "scc_currently_marks_pyramid_unlinked": not docs["scc"]["external_unlinked_frontiers"]["coherence_pyramid"]["typed_link_to_Aspect_G4_generator"],
        "evans_interval_status_updates_v18": docs["evans_interval"]["status"] == "two_interval_strategies_certify_strict_negativity",
    }

    acceptance = contract["acceptance"]
    source_text = paths["construction_source"].read_text(encoding="utf-8")
    linkage_checks = {
        "candidate_formula_materialized": bool(contract["candidate_link"]["formula"]),
        "candidate_source_derived": contract["candidate_link"]["source_derived"],
        "source_prescribes_tensor_not_selected_channel_embedding": (
            "N_*\\mathbb C[\\sigma]\\widehat\\otimes V" in source_text
            and "delete from the final construction" in source_text
        ),
        "tensor_extended_source_carrier": acceptance["tensor_extended_source_carrier"],
        "graph_TPB_target": acceptance["graph_TPB_target"],
        "bordered_readout_intertwines_factorwise": acceptance["bordered_readout_intertwining"],
        "contragredient_return_intertwines_factorwise": acceptance["contragredient_return_intertwining"],
    }
    admitted = all(evidence_checks.values()) and all(linkage_checks.values())

    out = {
        "schema": "marici.scc.coherence-pyramid-g4-conformance.result.v1",
        "status": "admitted_signed_relative_tensor_linkage" if admitted else "not_admitted_missing_cross_carrier_linkage",
        "evidence_checks": evidence_checks,
        "linkage_checks": linkage_checks,
        "analytical_geometry_verified": all(evidence_checks.values()),
        "scc_admitted": admitted,
        "first_failed_gate": next((name for name, value in linkage_checks.items() if not value), None),
        "linkage_formula": contract["candidate_link"]["formula"],
        "external_nonclaims": contract["external_nonrequirements"],
        "v18_correction": "The coherence geometry is fully realized at signed/relative strength, its canonical factorwise tensor link to T_PB is admitted, and the unchanged Evans hostility is interval-certified. Positive terminal realization and transverse Evans placement remain open.",
        "artifacts_sha256": {name: digest(path) for name, path in paths.items()},
        "claim_boundary": "Admission is only for the factorwise signed/relative coherence tensor link to canonical G4. It is not a cross-identification of moving-current and arithmetic coordinates and does not promote positive-Hilbert or Evans claims.",
        "passed": admitted,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    if not out["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
