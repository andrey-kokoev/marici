#!/usr/bin/env python3
"""Validate the proposed SCC probe-semantics schema delta without admission."""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).parents[3]
base_path = ROOT / "research/aspect/scc/contract.v1.json"
delta_path = ROOT / "research/aspect/contracts/scc-probe-semantics-delta.v1.json"
base = json.loads(base_path.read_text(encoding="utf-8"))
delta = json.loads(delta_path.read_text(encoding="utf-8"))
base_sha = hashlib.sha256(base_path.read_bytes()).hexdigest()

required_sections = {
    "configuration_domain",
    "constraint_presheaf",
    "interaction_classification",
    "optional_additive_specialization",
    "continuation_interface",
    "rewrite_certificate",
    "authority_and_boundary",
}
required_checks = {
    "probe-domain-downward-closure",
    "probe-restriction-functoriality",
    "probe-matching-map-typing",
    "probe-continuation-interface-faithfulness",
    "probe-rewrite-naturality",
    "probe-source-digest",
}
base_text = json.dumps(base, sort_keys=True)

checks = {
    "base_digest_matches": base_sha == delta["base_contract"]["sha256"],
    "base_schema_matches": base["schema"] == delta["base_contract"]["schema"],
    "delta_is_not_admitted": delta["status"] == "proposed_not_admitted",
    "extension_is_opt_in": delta["compatibility"]["mode"] == "opt_in_extension",
    "legacy_absence_does_not_mean_zero": "must_not_mean_zero_defect" in delta["compatibility"]["forbidden_promotion"],
    "all_required_sections_present": set(delta["required_sections"]) == required_sections,
    "all_required_registry_checks_present": set(delta["registry_check_kinds"]) == required_checks,
    "probe_configuration_stage_follows_ports": delta["stage_insertions"][0] == {"stage": "probe_configuration", "after": "ports"},
    "rewrite_certificate_follows_dynamic_coherence": delta["stage_insertions"][1] == {"stage": "probe_rewrite_certificate", "after": "dynamic_coherence"},
    "current_contract_has_no_configuration_domain": "configuration_domain" not in base_text,
    "current_contract_has_no_restriction_maps": "restriction_maps" not in base_text,
    "current_contract_has_no_naturality_checks": "naturality" not in base_text,
    "current_contract_has_generic_residual_output_only": "residuals" in base["outputs"] and "residual_kind" not in base_text,
    "live_contract_unchanged_nonclaim_present": "live SCC contract unchanged" in delta["nonclaims"],
    "live_registry_unchanged_nonclaim_present": "live SCC registry unchanged" in delta["nonclaims"],
}
assert all(checks.values()), checks

result = {
    "schema": "marici.aspect.scc-probe-semantics-delta-check.v1",
    "status": "passed",
    "checks": checks,
    "base_sha256": base_sha,
    "required_section_count": len(required_sections),
    "required_registry_check_count": len(required_checks),
    "claim_boundary": "Schema delta validation only; no live SCC mutation or admission."
}
output = ROOT / "research/aspect/results/scc_probe_semantics_delta.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks)}, sort_keys=True))
