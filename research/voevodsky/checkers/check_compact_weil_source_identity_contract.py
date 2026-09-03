from __future__ import annotations

import json
from pathlib import Path


REQUIRED = {
    "source_locator",
    "test_space",
    "fourier_convention",
    "quadratic_form_normalization",
    "archimedean_term",
    "prime_translation_terms",
    "polar_endpoint_terms",
    "zero_extension_convention",
    "dirichlet_comparison_map",
}


def missing_fields(candidate: dict) -> list[str]:
    return sorted(REQUIRED - candidate.keys())


def main() -> None:
    contract_path = Path("research/voevodsky/compact-weil-source-identity-contract.json")
    contract = json.loads(contract_path.read_text(encoding="utf-8"))
    assert set(contract["required"]) == REQUIRED

    gaussian_fixture = {
        "source_locator": "research/grothendieck/explicit-two-variable-weil-heat-source-formula.md",
        "test_space": "shifted_spectral_gaussian",
        "fourier_convention": {},
        "quadratic_form_normalization": {},
        "archimedean_term": {},
        "prime_translation_terms": {},
        "polar_endpoint_terms": {},
    }
    missing = missing_fields(gaussian_fixture)
    assert missing == ["dirichlet_comparison_map", "zero_extension_convention"]
    assert gaussian_fixture["test_space"] != "compact_logarithmic_support"

    result = {
        "schema": "marici.voevodsky.compact-weil-source-contract-check.v1",
        "status": "source_identity_contract_verified_uninstantiated",
        "required_fields": sorted(REQUIRED),
        "gaussian_fixture_missing_fields": missing,
        "gaussian_fixture_wrong_test_space": True,
        "authoritative_instance_materialized": False,
        "matrix_assembly_authorized": False,
        "acceptance_test": "all required fields plus compact_logarithmic_support test space and source locator",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
