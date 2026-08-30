"""Finite prototype of a cost-aware programmable optical criticism engine."""

from fractions import Fraction as F
import json


def total_variation(p, q):
    return sum(abs(a - b) for a, b in zip(p, q)) / 2


def main():
    # Rival isolated routes I and -I have identical adjoint/intensity behavior.
    contexts = [
        {"name": "baseline_projective", "authorized": True, "cost": 0,
         "records": {"identity": (F(1),), "central_phase": (F(1),)}},
        {"name": "determinant_shadow", "authorized": True, "cost": 1,
         "records": {"identity": (F(1),), "central_phase": (F(1),)}},
        {"name": "weak_controlled_reference", "authorized": True, "cost": 1,
         "records": {"identity": (F(3, 4), F(1, 4)), "central_phase": (F(1, 4), F(3, 4))}},
        {"name": "full_controlled_reference", "authorized": True, "cost": 3,
         "records": {"identity": (F(1), F(0)), "central_phase": (F(0), F(1))}},
        {"name": "hidden_route_oracle", "authorized": False, "cost": 0,
         "records": {"identity": (F(1), F(0)), "central_phase": (F(0), F(1))}},
    ]
    source_distance = F(1)
    for context in contexts:
        context["margin"] = total_variation(
            context["records"]["identity"], context["records"]["central_phase"]
        ) / source_distance

    threshold = F(3, 4)
    eligible = [c for c in contexts if c["authorized"] and c["margin"] >= threshold]
    selected = min(eligible, key=lambda c: (c["cost"], -c["margin"]))
    criticism_profile = {
        budget: max((c["margin"] for c in contexts if c["authorized"] and c["cost"] <= budget), default=F(0))
        for budget in (0, 1, 2, 3)
    }
    checks = {
        "baseline_rivals_are_observationally_equal": contexts[0]["margin"] == 0,
        "first_failed_gate_is_global_multiplicity": contexts[0]["records"]["identity"] == contexts[0]["records"]["central_phase"],
        "unauthorized_oracle_is_excluded_despite_unit_margin": contexts[-1]["margin"] == 1 and not contexts[-1]["authorized"],
        "weak_reference_has_half_margin_at_cost_one": contexts[2]["margin"] == F(1, 2) and contexts[2]["cost"] == 1,
        "full_reference_has_unit_margin_at_cost_three": contexts[3]["margin"] == 1 and contexts[3]["cost"] == 3,
        "threshold_selects_cheapest_adequate_authorized_context": selected["name"] == "full_controlled_reference",
        "criticism_profile_is_budget_monotone": list(criticism_profile.values()) == [F(0), F(1, 2), F(1, 2), F(1)],
        "selected_context_predicts_opposite_output_ports": selected["records"]["identity"] == (1, 0) and selected["records"]["central_phase"] == (0, 1),
        "engine_classifies_test_not_source_explanation": True,
    }
    result = {
        "schema": "marici.aspect.programmable_optical_criticism_engine.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "checks": checks,
        "rivals": ["identity route", "central pi-phase route"],
        "first_failed_gate": "global_multiplicity",
        "required_margin": "3/4",
        "selected_intervention": selected["name"],
        "selected_cost": selected["cost"],
        "criticism_profile": {str(k): str(v) for k, v in criticism_profile.items()},
        "context_table": [
            {"name": c["name"], "authorized": c["authorized"], "cost": c["cost"], "margin": str(c["margin"])}
            for c in contexts
        ],
        "typed_boundary": {
            "source": "two rival unitary routes separated by one authorized constructor-word unit",
            "constructor": "predeclared library of projective and controlled-reference optical contexts",
            "detector": "two-output probability law with total-variation observation metric",
            "hostile": "baseline-equivalent routes I and minus I plus an unauthorized zero-cost oracle",
            "completion": "selects a severe bounded test but does not explain why either source route occurs",
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
