from __future__ import annotations

import json
from pathlib import Path


REGISTRY = Path("research/voevodsky/coherence-pyramid-overlay-registry-v3.json")


def main() -> None:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    analytic = json.loads(Path(registry["analytic_fragment_registry"]).read_text(encoding="utf-8"))
    evidence = [json.loads(Path(path).read_text(encoding="utf-8")) for path in registry["evidence"]]
    assert len(evidence) == 15
    assert all(item["passed"] is True for item in evidence)
    assert analytic["global_scope"]["analytic_fragment_verified"] is True
    assert analytic["global_scope"]["full_cross_sector_equipment"] is False

    indexing = registry["indexing_structure"]
    assert indexing["total_shape"] == "bisimplicial computad-valued diagram"
    assert "certificate-sector naturality" in indexing["mixed_horns"]

    levels = registry["representation_levels"]
    assert levels.index("ordered_loop_probe") < levels.index("horn_filler")
    assert levels.index("horn_filler") < levels.index("certificate-natural_global_section")

    loop = registry["kitaev_associator_loop"]
    assert loop["exact_value"] == "-1/8"
    assert "globally nonfaithful" in loop["coordinate_strength"]
    assert "positive multiplicative commutative" in loop["rival_exclusion_strength"]
    assert loop["observable_robustness"] == {"gap": "1/8", "contamination_fraction": "1/9", "minimum_negative_mass": "1/8", "minimum_total_variation": "5/4"}
    assert loop["physical_constructor_status"] == "not authorized"
    assert loop["global_gluing_status"] == "not verified"

    nonpromotions = registry["required_nonpromotions"]
    assert len(nonpromotions) == 7
    assert all(value is False for value in nonpromotions.values())

    probe = registry["probe_contract"]
    all_fields = set().union(*(set(values) for values in probe.values()))
    assert len(all_fields) == sum(len(values) for values in probe.values())
    assert {"joint_faithfulness_certificate", "mixed_horn_coverage", "process_robustness_lower_bound"} <= all_fields

    status = registry["global_status"]
    assert status["overlay_schema_verified"] is True
    assert status["cross_sector_global_section_verified"] is False
    assert status["full_coherence_pyramid_equipment_verified"] is False

    result = {
        "schema": "marici.voevodsky.coherence-pyramid-overlay-registry-check.v3",
        "status": "bisimplicial_partial_representation_registry_verified",
        "evidence_documents_passed": len(evidence),
        "analytic_and_partial_layers_separated": True,
        "certificate_sector_mixed_horns_recorded": True,
        "probe_coordinate_coverage_implementation_rival_modalities_separated": True,
        "Kitaev_loop_exact_strength_preserved": True,
        "seven_nonpromotion_gates_enforced": True,
        "cross_sector_global_section_verified": False,
        "full_coherence_pyramid_equipment_verified": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
