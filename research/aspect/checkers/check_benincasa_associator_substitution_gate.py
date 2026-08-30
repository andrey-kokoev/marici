#!/usr/bin/env python3
"""Refuse associator promotion when a source packet contains ranks but no maps."""
import json
from pathlib import Path

A = Path(__file__).resolve().parent.parent
P = json.loads((A / "contracts" / "benincasa-associator-substitution.v1.json").read_text())
R = A / "results" / "benincasa_associator_substitution_gate.json"

def main():
    sub = P["associator_substitution"]
    required = [
        "coefficient_ring", "domain_bases", "codomain_bases",
        "integral_or_polynomial_maps", "edge_types",
        "specialization_rule", "source_digest"
    ]
    missing = [k for k in required if sub.get(k) in (None, [], {})]
    contexts = {x["id"]: x for x in P["observed_contexts"]}
    separation = (
        contexts["generic_all_odd_mod_2"]["lower_quotient_defect_rank"] == 59
        and contexts["even_coordinate_mod_2"]["lower_quotient_defect_rank"] == 304
        and contexts["generic_all_odd_mod_2"]["kernel_rank"]
        == contexts["even_coordinate_mod_2"]["kernel_rank"] == 53
    )
    substitutable = not missing
    checks = {
        "context_rank_separation_recorded": separation,
        "missing_fields_detected": len(missing) == len(required),
        "rank_summary_not_promoted_to_map": not substitutable
    }
    out = {
        "schema": "marici.aspect.benincasa-associator-substitution-gate-result.v1",
        "passed": all(checks.values()),
        "checks": checks,
        "substitutable": substitutable,
        "missing_fields": missing,
        "verdict": "blocked_missing_source_matrices",
        "next_admission": "supply all missing fields without changing the associator schema"
    }
    R.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, sort_keys=True))
    raise SystemExit(0 if out["passed"] else 1)

if __name__ == "__main__":
    main()
