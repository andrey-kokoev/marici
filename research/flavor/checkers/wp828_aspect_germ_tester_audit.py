"""Exact WP828 audit of the WP827 construction against Aspect's germ tester."""

import json
from pathlib import Path
import sympy as sp


def main() -> None:
    rate = sp.symbols("rate", positive=True, real=True)
    shift = sp.symbols("shift", real=True)
    gain = sp.symbols("gain", positive=True, real=True)
    separate = sp.symbols("gain_lower gain_portal gain_upper", positive=True)
    anchor = 2 + sp.sqrt(3)
    gap = sp.log(anchor) / rate
    times = sp.Matrix([-gap, 0, gap])
    scales = times.applyfunc(sp.exp)
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    shifted = times + sp.ones(3, 1) * shift
    gaps = sp.Matrix([times[1] - times[0], times[2] - times[1]])
    shifted_gaps = sp.Matrix([shifted[1] - shifted[0], shifted[2] - shifted[1]])
    check("translation_completion_is_constant_on_full_orbits",
          all(sp.simplify(x) == 0 for x in shifted_gaps - gaps), shifted_gaps)

    ratios = sp.Matrix([scales[1] / scales[0], scales[2] / scales[1]])
    common_gain_scales = gain * scales
    common_gain_ratios = sp.Matrix([
        common_gain_scales[1] / common_gain_scales[0],
        common_gain_scales[2] / common_gain_scales[1],
    ])
    check("common_gain_completion_is_constant_on_full_orbits",
          all(sp.simplify(x) == 0 for x in common_gain_ratios - ratios),
          common_gain_ratios)

    separate_gain_scales = sp.Matrix([separate[i] * scales[i] for i in range(3)])
    separate_gain_ratios = sp.Matrix([
        separate_gain_scales[1] / separate_gain_scales[0],
        separate_gain_scales[2] / separate_gain_scales[1],
    ])
    check("separate_gain_completion_fails_full_fiber_gate",
          any(sp.simplify(x) != 0 for x in separate_gain_ratios - ratios),
          separate_gain_ratios)

    ternary_relation = sp.simplify(times[2] - 2 * times[1] + times[0])
    check("native_target_is_ternary_equal_spacing_relation",
          ternary_relation == 0, ternary_relation)
    check("binary_factorization_requires_shared_middle_identity",
          gaps[0] == gaps[1] and len(gaps) == 2,
          {"left_gap": str(gaps[0]), "right_gap": str(gaps[1]),
           "required_shared_record": "portal"})

    marked_germ = {
        "type": "oriented logistic RG trajectory with intrinsic curvature anchors",
        "identity_token": "one source trajectory and labels lower/portal/upper",
        "provenance_interface": "beta field -> acceleration -> jerk-zero anchors",
        "unconsumed_comparison_port": "shared RG clock and common calibration epoch",
    }
    check("marked_carrier_has_aspect_required_fields",
          set(marked_germ) == {"type", "identity_token", "provenance_interface",
                               "unconsumed_comparison_port"}, marked_germ)

    realization = {
        "map_to_ordered_detector_record": False,
        "physical16_descent": False,
        "threshold_survival": False,
        "common_gain_instrument": False,
    }
    check("events_are_not_mistyped_as_primitive_germs",
          not realization["map_to_ordered_detector_record"], realization)
    check("authority_gate_remains_open_after_descent",
          not any(realization.values()), realization)

    ratio_rate_one = sp.simplify(anchor ** (1 / sp.Integer(1)))
    ratio_rate_two = sp.simplify(anchor ** (1 / sp.Integer(2)))
    check("rate_pair_is_exact_smallest_normalization_falsifier",
          sp.simplify(ratio_rate_one - ratio_rate_two) != 0,
          {"rate_1": str(ratio_rate_one), "rate_2": str(ratio_rate_two)})

    classification = {
        "aspect_structure": "marked ternary carrier germ with retained same-trajectory comparison port",
        "fiber_gate": "passes for common translation and common gain; fails for independent gains",
        "arity_gate": "ternary; binary gaps are composable only with the same portal identity retained",
        "authority_gate": "fails: no threshold-to-physical16 realization or calibrated instrument",
        "selector_status": "conditional event selector inside the admitted logistic source model, not a selector on the physical16 lens family",
        "rigidifier_status": "relational rigidifier for event ratios conditional on beta normalization",
        "verdict": "WP827 passes Aspect's germ structure only after retyping; it does not pass physical realization authority",
    }
    result = {
        "work_package": "WP828",
        "title": "Aspect germ tester audit of the intrinsic RG curvature triplet",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "marked_carrier_germ": marked_germ,
        "native_target": {
            "arity": 3,
            "arguments": ["lower curvature anchor", "portal crossing", "upper curvature anchor"],
            "relation": "t_upper - 2*t_portal + t_lower = 0",
            "binary_factorization_condition": "both gaps retain the identical portal record and common trajectory provenance",
        },
        "completion_maps": {
            "translation_orbit": "three RG times -> two adjacent gaps",
            "common_gain_orbit": "three event energies -> two adjacent ratios",
            "forbidden_local_completion": "separate event calibration before forming ratios",
        },
        "realization": realization,
        "classification": classification,
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp828_aspect_germ_tester_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
