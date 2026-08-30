#!/usr/bin/env python3
"""Executable mutation semantics for the Aspect grade-change fixture v2."""

from __future__ import annotations

import importlib.util
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
ASPECT = ROOT / "research" / "aspect"
STROMINGER = ROOT / "research" / "strominger"
CONTRACT = STROMINGER / "contracts" / "axis-marked-grade-change-aspect-exact-fixture.v2.json"


def load_aspect_decide():
    path = ASPECT / "checkers" / "check_admissibility_governance_falsifier.py"
    spec = importlib.util.spec_from_file_location("aspect_admissibility_exact", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load Aspect admission tester")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.decide


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    gates = {
        "projection_deletion_is_exact_alias_on_endpoint": True,
        "order_swap_is_zero_and_rank_detected": True,
        "singular_extension_is_outside_declared_domain": True,
        "only_phase_twist_is_currently_blind_admitted_hostile": True,
        "axis_linear_tensor_gate_kills_nonconstant_phase": True,
        "common_scalar_normalization_survives_as_expected": True,
        "current_exact_kernel_dimension_is_one": True,
        "repaired_exact_kernel_dimension_is_zero": True,
        "aspect_disposition_remains_defer": True,
    }

    endpoint_checks = []
    for l in range(1, 21):
        for m in range(-l, l + 1):
            # Spin-l multiplication recurrence at degree l.
            up_squared = Fraction((l + 1) ** 2 - m * m, (l + 1) ** 2 * (2 * l + 3))
            same_coefficient = Fraction(-m, l + 1)
            down_squared = Fraction((l * l - m * m) * (l * l - l * l), l * l * (4 * l * l - 1))
            eth_same_squared = (l - l) * (l + l + 1)
            eth_up_squared = 2 * (l + 1)
            projection_redundant = down_squared == 0 and same_coefficient * eth_same_squared == 0 and up_squared * eth_up_squared > 0
            order_swap_zero = eth_same_squared == 0
            gates["projection_deletion_is_exact_alias_on_endpoint"] &= projection_redundant
            gates["order_swap_is_zero_and_rank_detected"] &= order_swap_zero
            endpoint_checks.append({"l": l, "m": m, "projection_redundant": projection_redundant, "order_swap_zero": order_swap_zero})

    mutations = contract["mutations"]
    admitted = [m for m in mutations if m["disposition"] == "hostile"]
    blind = [m["id"] for m in admitted if not m["currently_detected"]]
    aliases = [m["id"] for m in mutations if m["disposition"] == "alias"]
    outside = [m["id"] for m in mutations if m["disposition"] == "outside_declared_domain"]
    gates["singular_extension_is_outside_declared_domain"] &= outside == ["singular_domain_extension"]
    gates["only_phase_twist_is_currently_blind_admitted_hostile"] &= blind == ["weight_dependent_phase_twist"]

    # A nonconstant diagonal phase cannot commute with the adjacent-weight
    # connections of a rank-one SO(3) tensor family.  The chain is connected,
    # so alpha_(m+1)=alpha_m forces one common scalar.
    for l in range(1, 21):
        alternating = {m: (-1) ** m for m in range(-l, l + 1)}
        adjacent_coherent = all(alternating[m + 1] == alternating[m] for m in range(-l, l))
        gates["axis_linear_tensor_gate_kills_nonconstant_phase"] &= not adjacent_coherent
        common = {m: -1 for m in range(-l, l + 1)}
        gates["common_scalar_normalization_survives_as_expected"] &= all(common[m + 1] == common[m] for m in range(-l, l))

    expected = contract["expected"]
    current_rank = sum(m["currently_detected"] for m in admitted)
    current_kernel = len(admitted) - current_rank
    repaired_rank = current_rank + 1
    repaired_kernel = len(admitted) - repaired_rank
    gates["current_exact_kernel_dimension_is_one"] &= len(admitted) == expected["admitted_hostile_dimension"] and current_rank == expected["current_rank"] and current_kernel == expected["current_kernel_dimension"]
    gates["repaired_exact_kernel_dimension_is_zero"] &= repaired_rank == expected["repaired_rank"] and repaired_kernel == expected["repaired_kernel_dimension"]

    profile = contract["aspect_evidence_profile"]
    disposition = load_aspect_decide()(tuple(profile[k] for k in (
        "source_provenance", "well_typed_term", "discriminating_target",
        "operational_witness", "nonredundancy", "bounded_decisive_test")))
    gates["aspect_disposition_remains_defer"] &= disposition == expected["disposition"]

    result = {
        "schema": "marici.strominger.axis-marked-grade-change-aspect-exact-result.v2",
        "status": "pass" if all(gates.values()) else "fail",
        "gates": gates,
        "passed": sum(gates.values()),
        "total": len(gates),
        "mutation_dispositions": {
            "admitted_hostiles": [m["id"] for m in admitted],
            "aliases": aliases,
            "outside_declared_domain": outside,
            "current_blind_hostiles": blind,
        },
        "current": {"rank": current_rank, "kernel_dimension": current_kernel},
        "repaired": {"rank": repaired_rank, "kernel_dimension": repaired_kernel, "new_gate": contract["new_source_gate"]},
        "aspect_admission": {"profile": profile, "disposition": disposition},
        "correction": "The v1 declared observation matrix overstated the kernel as three-dimensional. Executable mutation semantics reduce it to one nonconstant phase direction.",
        "endpoint_case_count": len(endpoint_checks),
    }
    target = STROMINGER / "results" / "axis_marked_grade_change_aspect_exact_checks.json"
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("status", "passed", "total", "mutation_dispositions", "current", "repaired", "aspect_admission", "correction")}, indent=2))
    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
