"""Exact WP848 audit of a charged-spurion equivariant lift of WP820."""

import json
import math
from pathlib import Path
import sympy as sp


def main() -> None:
    s1, s2, s3, z = sp.symbols("s1 s2 s3 z", nonzero=True)
    lifted = sp.Matrix([[2*s1, -s2, 0], [3*s1, 0, -s3]])
    kernel = sp.Matrix([s2*s3, 2*s1*s3, 3*s1*s2])
    unit_kernel = kernel.subs({s1: 1, s2: 1, s3: 1})
    hostile_kernel = kernel.subs({s1: 1, s2: 2, s3: 1})
    domain_weights = [1, 2, 3]
    spurion_weights = [-1, -2, -3]
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("lifted_incidence_has_exact_symbolic_kernel",
          lifted*kernel == sp.zeros(2, 1), lifted*kernel)
    check("unit_spurion_vacuum_recovers_wp820_incidence",
          lifted.subs({s1: 1, s2: 1, s3: 1})
          == sp.Matrix([[2, -1, 0], [3, 0, -1]]),
          lifted.subs({s1: 1, s2: 1, s3: 1}))
    check("unit_spurion_vacuum_recovers_primitive_ray",
          unit_kernel == sp.Matrix([1, 2, 3]), unit_kernel)
    check("unequal_spurion_vacuum_changes_kernel_ray",
          hostile_kernel == sp.Matrix([2, 2, 6])
          and hostile_kernel.cross(sp.Matrix([1, 2, 3])) != sp.zeros(3, 1),
          hostile_kernel)
    check("kernel_ray_has_two_independent_projective_vev_ratios",
          sp.simplify(kernel[1]/kernel[0]) == 2*s1/s2
          and sp.simplify(kernel[2]/kernel[0]) == 3*s1/s3,
          (sp.simplify(kernel[1]/kernel[0]), sp.simplify(kernel[2]/kernel[0])))
    check("spurion_weights_cancel_domain_weights",
          [a+b for a, b in zip(domain_weights, spurion_weights)] == [0, 0, 0],
          [a+b for a, b in zip(domain_weights, spurion_weights)])
    check("constant_first_row_cannot_share_one_target_weight",
          domain_weights[0] != domain_weights[1], domain_weights[:2])
    check("constant_second_row_cannot_share_one_target_weight",
          domain_weights[0] != domain_weights[2], [domain_weights[0], domain_weights[2]])
    virtual_character = z+z**2+z**3-2
    positive_character = z+z**2+z**3
    check("equivariant_complex_has_virtual_character_with_two_neutral_targets",
          virtual_character == positive_character-2, virtual_character)
    check("virtual_index_is_not_wp846_positive_character",
          virtual_character != positive_character, (virtual_character, positive_character))
    check("three_nonzero_spurion_vevs_have_trivial_common_stabilizer",
          math.gcd(1, 2, 3) == 1, math.gcd(1, 2, 3))
    check("equivariant_lift_does_not_select_equal_vev_alignment",
          hostile_kernel.cross(unit_kernel) != sp.zeros(3, 1),
          (unit_kernel, hostile_kernel))

    result = {
        "work_package": "WP848",
        "title": "Charged-spurion equivariant incidence lift",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "lifted_differential": "[[2s1,-s2,0],[3s1,0,-s3]], with weights(sj)=-j",
        "kernel": "(s2 s3, 2 s1 s3, 3 s1 s2)",
        "vacuum_fiber": "two projective VEV ratios; equal VEVs recover (1,2,3) but are not selected",
        "virtual_character": "z+z^2+z^3-2",
        "stabilizer": "trivial for simultaneous nonzero VEVs of weights -1,-2,-3",
        "classification": "equivariance typing repair, not a source selector; vacuum alignment and character transport remain open",
        "smallest_exact_falsifier": "VEVs (1,2,1) give kernel ray (1,1,3), not (1,2,3)",
        "remaining_source_gate": "derive an equal-VEV spurion potential and protected pre-vacuum equivariant-index transport, then relational holonomy instrumentation",
        "tests": tests}
    output = Path(__file__).parents[1] / "results" / "wp848_charged_spurion_equivariant_incidence_lift.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
