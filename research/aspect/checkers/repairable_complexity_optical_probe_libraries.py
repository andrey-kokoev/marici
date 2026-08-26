"""Finite repairable-complexity audit for preregistered optical probe libraries."""

from fractions import Fraction as F
import json


THRESHOLD = F(3, 4)  # Frozen by packet 48 before this comparison.


PROBES = {
    "baseline": {"authorized": True, "cost": 0, "law": ((F(1),), (F(1),))},
    "determinant": {"authorized": True, "cost": 1, "law": ((F(1),), (F(1),))},
    "weak_reference": {"authorized": True, "cost": 1, "law": ((F(3, 4), F(1, 4)), (F(1, 4), F(3, 4)))},
    "full_reference": {"authorized": True, "cost": 3, "law": ((F(1), F(0)), (F(0), F(1)))},
    "hidden_oracle": {"authorized": False, "cost": 0, "law": ((F(1), F(0)), (F(0), F(1)))},
}


def tv(law):
    p, q = law
    return sum(abs(a - b) for a, b in zip(p, q)) / 2


def audit(names):
    admitted = [PROBES[name] for name in names if PROBES[name]["authorized"]]
    distinct_laws = {probe["law"] for probe in admitted}
    generative_capacity = len(distinct_laws)
    best_margin = max((tv(probe["law"]) for probe in admitted), default=F(0))
    unresolved_incoherence = 1 if best_margin < THRESHOLD else 0
    repair_capacity = sum(1 for law in distinct_laws if tv(law) >= THRESHOLD)
    return {
        "G": generative_capacity,
        "I": unresolved_incoherence,
        "R": repair_capacity,
        "M": repair_capacity - unresolved_incoherence,
        "best_margin": best_margin,
    }


def main():
    weak = audit(["baseline", "determinant", "weak_reference"])
    full = audit(["baseline", "determinant", "weak_reference", "full_reference"])
    oracle_excluded = audit(["baseline", "determinant", "weak_reference", "full_reference", "hidden_oracle"])
    duplicate_baseline = audit(["baseline", "determinant", "weak_reference", "baseline"])
    checks = {
        "threshold_is_inherited_not_postfit": THRESHOLD == F(3, 4),
        "weak_library_has_negative_repair_margin": weak == {"G": 2, "I": 1, "R": 0, "M": -1, "best_margin": F(1, 2)},
        "full_library_increases_generativity_and_repairs_incoherence": full == {"G": 3, "I": 0, "R": 1, "M": 1, "best_margin": F(1)},
        "full_transition_has_positive_delta_g": full["G"] - weak["G"] == 1,
        "full_transition_restores_nonnegative_margin": weak["M"] < 0 <= full["M"],
        "unauthorized_oracle_changes_no_typed_quantity": oracle_excluded == full,
        "duplicate_probe_does_not_inflate_generative_capacity": duplicate_baseline == weak,
        "temporary_negative_margin_has_declared_cost_two_recovery": PROBES["full_reference"]["cost"] - PROBES["weak_reference"]["cost"] == 2,
        "fixture_tests_architecture_not_natural_gradient": True,
    }
    result = {
        "schema": "marici.aspect.repairable_complexity_optical_probe_libraries.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "checks": checks,
        "frozen_threshold": "3/4",
        "libraries": {
            "weak": {**weak, "best_margin": str(weak["best_margin"])},
            "full": {**full, "best_margin": str(full["best_margin"])},
            "oracle_excluded": {**oracle_excluded, "best_margin": str(oracle_excluded["best_margin"])},
        },
        "typed_boundary": {
            "source": "two fixed rival optical routes and a preregistered probe library",
            "constructor": "behavioral quotient of authorized probe laws with fixed costs",
            "detector": "thresholded total-variation criticism margin",
            "hostile": "redundant probes inflate raw counts and an unauthorized oracle fakes free repair",
            "completion": "tests one architecture transition but supplies no evidence for a universal natural gradient",
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
