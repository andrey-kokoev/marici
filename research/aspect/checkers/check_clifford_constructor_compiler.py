from __future__ import annotations

import importlib.util
import json
from copy import deepcopy
from pathlib import Path


ROOT = Path(__file__).parents[1]
TOOL = ROOT / "tools" / "clifford_constructor_compiler.py"
SPEC = importlib.util.spec_from_file_location("clifford_constructor_compiler", TOOL)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def load(name):
    path = ROOT / "contracts" / name
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    fixture = MODULE.compile_contract(load("clifford_constructor_compiler_fixture.json"))
    assert fixture["existing_effect_rank"] == 1
    assert fixture["behavioral_kernel_dimension"] == 2
    assert fixture["rival_differences_in_existing_kernel"]["plus_vs_minus"]
    assert fixture["first_algebraically_transverse_candidate"] == "X_analyzer"
    assert fixture["first_eligible_source_authorized_effect"] == "X_analyzer"
    x_report = next(item for item in fixture["candidates"] if item["name"] == "X_analyzer")
    response = x_report["generated_effects"][0]["responses"][0]
    assert response == {
        "rival_difference": "plus_vs_minus",
        "pairing": "1",
        "sign": "positive",
        "magnitude_class": "unit",
    }
    wrong_locus = next(
        item
        for item in fixture["candidates"]
        if item["name"] == "wrong_locus_X_analyzer"
    )
    assert wrong_locus["algebraically_transverse"]
    assert wrong_locus["distinguishes_rival"]
    assert not wrong_locus["eligible_source_authorized_effect"]
    assert wrong_locus["failed_gates"] == ["authority_locus_matches"]

    malformed = deepcopy(load("clifford_constructor_compiler_fixture.json"))
    malformed["rival_differences"][0]["vector"] = ["1", "0"]
    try:
        MODULE.compile_contract(malformed)
    except ValueError as error:
        assert str(error) == "rival_differences[0].vector must have exactly 3 coordinates"
    else:
        raise AssertionError("dimension-invalid rival difference was accepted")

    moving = MODULE.compile_contract(load("moving_flagged_barrier_rivals.json"))
    assert moving["existing_effect_rank"] == 1
    assert moving["behavioral_kernel_dimension"] == 1
    assert moving["behavioral_kernel_basis"] == [["1", "0"]]
    assert moving["rival_differences_in_existing_kernel"][
        "moving_barrier_vs_tangent_native_endpoint_mode"
    ]
    assert moving["first_algebraically_transverse_candidate"] == (
        "canonical_rigged_transpose_boundary_return"
    )
    assert moving["first_eligible_source_authorized_effect"] is None

    rigged = next(
        item
        for item in moving["candidates"]
        if item["name"] == "canonical_rigged_transpose_boundary_return"
    )
    assert rigged["algebraically_transverse"]
    assert rigged["distinguishes_rival"]
    assert not rigged["eligible_source_authorized_effect"]
    assert set(rigged["failed_gates"]) == {
        "executable",
        "perturbation",
        "completion_stable",
        "authority_locus_matches",
    }

    reciprocal = next(
        item
        for item in moving["candidates"]
        if item["name"] == "ordered_inverse_derivative_reciprocal_port"
    )
    assert reciprocal["algebraically_transverse"]
    assert not reciprocal["eligible_source_authorized_effect"]
    assert set(reciprocal["failed_gates"]) == {
        "completion_stable",
        "authority_locus_matches",
    }

    fitted = next(
        item for item in moving["candidates"] if item["name"] == "fitted_reverse_incidence"
    )
    assert fitted["algebraically_transverse"]
    assert not fitted["eligible_source_authorized_effect"]
    assert set(fitted["failed_gates"]) == {"source_authorized", "completion_stable"}

    (ROOT / "results" / "clifford_constructor_compiler_fixture.json").write_text(
        json.dumps(fixture, indent=2) + "\n", encoding="utf-8"
    )
    (ROOT / "results" / "moving_flagged_barrier_clifford_audit.json").write_text(
        json.dumps(moving, indent=2) + "\n", encoding="utf-8"
    )
    summary = {
        "schema": "marici.aspect.clifford-constructor-compiler-check.v1",
        "status": "pass",
        "generic_fixture_first_eligible_effect": fixture[
            "first_eligible_source_authorized_effect"
        ],
        "moving_barrier_existing_kernel_dimension": moving[
            "behavioral_kernel_dimension"
        ],
        "moving_barrier_first_algebraically_transverse_candidate": moving[
            "first_algebraically_transverse_candidate"
        ],
        "moving_barrier_first_eligible_source_authorized_effect": moving[
            "first_eligible_source_authorized_effect"
        ],
        "verdict": "The compiler finds an eligible X effect in the generic Clifford fixture. On the source-typed moving-barrier audit, the canonical rigged transpose is the first algebraically transverse candidate, but no candidate passes source authority, executable perturbation, same-locus, calibration, and completion gates together.",
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
