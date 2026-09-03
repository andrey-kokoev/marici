from __future__ import annotations

import json
from pathlib import Path


SIGNATURE = Path("research/voevodsky/coherence-pyramid-computad-signature.json")


def main() -> None:
    data = json.loads(SIGNATURE.read_text(encoding="utf-8"))
    object_sorts = set(data["object_sorts"])
    generators = data["one_generators"]

    for name, generator in generators.items():
        assert generator["source_sort"] in object_sorts, name
        assert generator["target_sort"] in object_sorts, name
        assert generator["variance"] in {"under", "over", "vertical", "comparison"}, name
        assert generator["required_certificates"], name

    assert {generator["variance"] for generator in generators.values()} == {
        "under", "over", "vertical", "comparison"
    }

    required_certificate_sorts = {
        "joint_amalgamation",
        "pullback_exactness",
        "completion",
        "mixed_square",
    }
    assert required_certificate_sorts <= set(data["certificate_sorts"])

    required_cells = {
        "form_preservation_cell",
        "kernel_compatibility_cell",
        "beck_chevalley_candidate",
        "completion_comparison_cell",
    }
    assert required_cells <= set(data["two_generators"])

    required_refusals = {
        "under_embedding_without_form_preservation",
        "over_quotient_without_kernel_identification",
        "green_pushout_without_joint_amalgamation",
        "pairwise_certificate_without_full_completion",
        "closed_form_identity_from_core_equality_only",
        "completion_without_radical_and_coercivity_control",
    }
    assert required_refusals <= set(data["constructor_refusals"])

    result = {
        "schema": "marici.voevodsky.coherence-pyramid-computad-signature-check.v1",
        "status": "typed_generator_signature_verified",
        "object_sort_count": len(object_sorts),
        "one_generator_count": len(generators),
        "certificate_sort_count": len(data["certificate_sorts"]),
        "two_generator_count": len(data["two_generators"]),
        "constructor_refusal_count": len(data["constructor_refusals"]),
        "variance_classes": sorted(generator["variance"] for generator in generators.values()),
        "category_claimed": False,
        "next_gate": "finite-to-closed completion interface, then partial composition",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
