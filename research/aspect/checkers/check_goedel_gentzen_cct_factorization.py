#!/usr/bin/env python3
"""Finite diagnostic model for the proposed Gödel–Gentzen CCT factorization.

This checks only the finite interface and a deliberate failure case. It is not a
proof of either source theorem or of an unbounded CCT realization.
"""

from __future__ import annotations

import json
from pathlib import Path


def strict_descent(edges: list[tuple[str, str]], rank: dict[str, int]) -> tuple[bool, list[dict[str, object]]]:
    checks = [
        {"source": source, "target": target, "source_rank": rank[source], "target_rank": rank[target], "strict": rank[target] < rank[source]}
        for source, target in edges
    ]
    return all(bool(check["strict"]) for check in checks), checks


def main() -> None:
    lower_probe = {"g": "unresolved", "zero_eq_zero": "proved"}
    meta_probe = {"g": "certified_under_external_assumption", "zero_eq_zero": "proved"}
    forward_translation = {"g": "g", "zero_eq_zero": "zero_eq_zero"}
    reflection_map: dict[str, str] = {}

    rank = {"D3": 3, "D2": 2, "D1": 1, "NF": 0}
    reduction_edges = [("D3", "D2"), ("D2", "D1"), ("D1", "NF")]
    descent_passed, descent_checks = strict_descent(reduction_edges, rank)

    bad_rank = {"A": 1, "B": 0}
    bad_edges = [("A", "B"), ("B", "A")]
    bad_passed, bad_checks = strict_descent(bad_edges, bad_rank)

    operations = {
        "resolve_foundation": {"pressure": 2, "dependencies": set(), "rank_target": 2},
        "resolve_probe": {"pressure": 9, "dependencies": {"resolve_foundation"}, "rank_target": 1},
        "normalize_residue": {"pressure": 4, "dependencies": set(), "rank_target": 2},
    }
    completed: set[str] = set()
    admissible = {
        name for name, operation in operations.items()
        if operation["dependencies"] <= completed
    }
    selected = max(admissible, key=lambda name: operations[name]["pressure"])

    assertions = {
        "lower_rung_probe_is_not_total": lower_probe["g"] == "unresolved",
        "meta_rung_adds_certificate": meta_probe[forward_translation["g"]] == "certified_under_external_assumption",
        "certificate_does_not_descend": "g" not in reflection_map,
        "gentzen_like_finite_rank_strictly_descends": descent_passed,
        "deliberate_cycle_is_rejected": not bad_passed,
        "pressure_selects_only_among_admissible_operations": selected == "normalize_residue",
        "higher_pressure_cannot_override_dependencies": "resolve_probe" not in admissible,
        "resolution_order_contains_no_time_coordinate": all("time" not in operation for operation in operations.values()),
    }
    passed = all(assertions.values())

    result = {
        "schema": "marici.aspect.goedel-gentzen-cct-finite-diagnostic.v1",
        "status": "passed" if passed else "failed",
        "strength": "finite_diagnostic_model_only",
        "assertions": assertions,
        "lower_probe": lower_probe,
        "meta_probe": meta_probe,
        "forward_translation": forward_translation,
        "reflection_map": reflection_map,
        "descent_checks": descent_checks,
        "deliberate_failure_checks": bad_checks,
        "pressure_scheduler": {
            "admissible": sorted(admissible),
            "selected": selected,
            "blocked_higher_pressure_operation": "resolve_probe",
            "ordering_kind": "typed_dependency_and_rank_order_only",
        },
        "claim_boundary": [
            "does_not_prove_goedel_incompleteness",
            "does_not_prove_gentzen_consistency",
            "does_not_construct_epsilon_0_well_foundedness",
            "does_not_construct_a_source_derived_CCT_functor",
        ],
    }

    output = Path(__file__).resolve().parents[1] / "results" / "goedel_gentzen_cct_factorization.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "assertions": assertions}, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
