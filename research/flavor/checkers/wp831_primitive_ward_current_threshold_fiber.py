"""Exact WP831 audit of the primitive Ward-current threshold fiber."""

import json
from math import gcd
from pathlib import Path
import sympy as sp


def main() -> None:
    B = sp.Matrix([[2, -1, 0], [3, 0, -1]])
    q = sp.Matrix([1, 2, 3])
    e_high = sp.symbols("e_high", positive=True, real=True)
    r = sp.symbols("r", positive=True, integer=True)
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    nullspace = B.nullspace()
    check("incidence_has_one_dimensional_current_kernel",
          B.rank() == 2 and len(nullspace) == 1, nullspace)
    check("primitive_current_is_exact_kernel_generator",
          B*q == sp.zeros(2, 1)
          and gcd(gcd(abs(int(q[0])), abs(int(q[1]))), abs(int(q[2]))) == 1,
          q)
    anomaly = sum(component**3 for component in q)
    check("oriented_inflow_fixes_current_orientation",
          anomaly == 36 and sum((-component)**3 for component in q) == -36,
          anomaly)
    check("primitive_current_fixes_unit_portal_charge_contrast",
          q[2]-q[1] == 1, q[2]-q[1])

    base_index = sp.expand(q.dot(q))
    check("base_ward_spectral_index_is_fourteen", base_index == 14, base_index)
    check("vectorlike_pair_preserves_linear_and_cubic_anomaly",
          r+(-r) == 0 and sp.expand(r**3+(-r)**3) == 0,
          (r+(-r), sp.expand(r**3+(-r)**3)))
    high_index = base_index+2*r**2
    check("vectorlike_pair_changes_current_spectral_index",
          sp.simplify(high_index-base_index-2*r**2) == 0, high_index)

    e_low = sp.sqrt(high_index/base_index)*e_high
    response_high = sp.expand(high_index*e_high**2)
    response_low = sp.simplify(base_index*e_low**2)
    check("ward_response_continuity_allows_coupling_rematching",
          sp.simplify(response_low-response_high) == 0,
          (response_high, response_low))
    check("unit_vectorlike_threshold_changes_portal_magnitude",
          sp.simplify(e_low.subs(r, 1)-sp.sqrt(sp.Rational(8, 7))*e_high) == 0
          and sp.simplify(e_low.subs(r, 1)-e_high) != 0,
          e_low.subs(r, 1))

    e = sp.symbols("e", positive=True, real=True)
    response = base_index*e**2
    check("fixed_spectrum_current_record_is_injective_for_positive_coupling",
          sp.diff(response, e) > 0, sp.diff(response, e))
    hostile_e = sp.sqrt(sp.Rational(7, 8))
    check("open_spectrum_current_record_has_exact_source_fiber",
          base_index*1**2 == (base_index+2)*hostile_e**2,
          (base_index, (base_index+2)*hostile_e**2))

    result = {
        "work_package": "WP831",
        "title": "Primitive Ward-current threshold fiber",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "admitted_state_domain": "WP820 rank-one integer current kernel with oriented cubic inflow, positive gauge coupling, and anomaly-neutral vectorlike threshold completions",
        "faithful_quotient_coordinate": "primitive oriented current q=(1,2,3) plus the full active spectral index and positive coupling",
        "source_authorized_probe_family": "the unique primitive-current two-point response C=S e^2, conditional on a complete active spectrum",
        "contextual_partition": {
            "fixed_spectrum": "C is injective in e>0",
            "open_threshold_completion": "C identifies products S e^2 and collapses distinct spectrum/coupling packets",
        },
        "classification": {
            "channel_selection": "the primitive oriented kernel selects one linear conserved-current channel",
            "portal_sign": "the oriented charge contrast is positive and primitive",
            "portal_magnitude": "not selected; current normalization reads e only after the full spectral index is fixed",
            "threshold_survival": "fails numerically: Ward-response continuity permits e_low=sqrt(S_high/S_low)e_high",
            "rg_basin": "not supplied by current uniqueness",
            "physical_readout": "formal current-correlator probe; calibrated momentum, production, spectral subtraction, and detector response remain absent",
            "selector_or_rigidifier": "current-channel selector and charge rigidifier, neither a coupling-magnitude nor physical16 selector",
        },
        "smallest_exact_falsifier": {
            "base_packet": {"spectral_index": "14", "coupling": "1"},
            "vectorlike_completed_packet": {"spectral_index": "16", "coupling": "sqrt(7/8)"},
            "common_current_record": "14",
        },
        "remaining_source_gate": "the same constructor must forbid or fix every anomaly-neutral spectral completion, derive its masses and interacting RG basin, and realize the primitive-current correlator in one calibrated physical16 instrument",
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp831_primitive_ward_current_threshold_fiber.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
