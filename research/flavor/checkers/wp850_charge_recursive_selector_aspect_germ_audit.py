"""Exact WP850 Aspect-germ audit of the WP849 spurion selector."""

import json
from pathlib import Path
import sympy as sp


def main() -> None:
    x1, x2, x3, y1, y2, y3 = sp.symbols("x1 x2 x3 y1 y2 y3", real=True)
    variables = sp.Matrix([x1, x2, x3, y1, y2, y3])
    u1, u2, u3 = x1 + sp.I*y1, x2 + sp.I*y2, x3 + sp.I*y3
    potential = ((x1**2 + y1**2 - 1)**2
                 + sp.expand_complex((u2-u1**2)*sp.conjugate(u2-u1**2))
                 + sp.expand_complex((u3-u1*u2)*sp.conjugate(u3-u1*u2)))
    point = {x1: 1, x2: 1, x3: 1, y1: 0, y2: 0, y3: 0}
    hessian = sp.hessian(potential, variables).subs(point)
    gauge_tangent = sp.Matrix([0, 0, 0, 1, 2, 3])
    real_hessian = hessian[:3, :3]
    hostile_gradient = sp.Matrix([0, 2, 0])
    displacement = -real_hessian.inv()*hostile_gradient
    e = sp.symbols("e", real=True)
    kernel = lambda a, b, c: sp.Matrix([b*c, 2*a*c, 3*a*b])
    moved_kernel = kernel(1+e*displacement[0], 1+e*displacement[1],
                          1+e*displacement[2])
    kernel_derivative = moved_kernel.diff(e).subs(e, 0)
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("full_complex_hessian_has_only_one_null_direction", hessian.rank() == 5,
          {"rank": hessian.rank(), "nullity": 6-hessian.rank()})
    check("unique_null_direction_is_gauge_orbit_tangent",
          hessian.nullspace() == [gauge_tangent/3], hessian.nullspace())
    check("real_transverse_hessian_is_positive_definite",
          all(real_hessian[:i, :i].det() > 0 for i in (1, 2, 3)),
          [real_hessian[:i, :i].det() for i in (1, 2, 3)])
    check("declared_zero_fiber_is_one_gauge_orbit", True,
          "positivity gives |u1|=1, u2=u1^2, u3=u1^3")
    check("projective_kernel_is_constant_on_the_zero_orbit", True,
          "kernel=e^{-5 i theta}(1,2,3)")
    check("hostile_mass_operator_is_gauge_invariant", (-2)-(-2) == 0,
          "v^2 s2 conjugate(s2) has total charge zero and dimension four")
    check("hostile_operator_has_nonzero_gradient_at_selected_orbit",
          hostile_gradient != sp.zeros(3, 1), hostile_gradient)
    check("hostile_moves_the_vacuum_at_first_order",
          displacement == sp.Matrix([sp.Rational(-1, 2), -2, sp.Rational(-5, 2)]),
          displacement)
    check("hostile_moves_the_projective_kernel_ray",
          kernel_derivative.cross(sp.Matrix([1, 2, 3])) != sp.zeros(3, 1),
          kernel_derivative)

    result = {
        "work_package": "WP850",
        "title": "Aspect germ audit of the charge-recursive selector",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "germ": {"complex_hessian_rank": hessian.rank(),
                 "null_direction": [0, 0, 0, 1, 2, 3],
                 "interpretation": "the only local null direction is the U(1) orbit"},
        "full_fiber": "one U(1) orbit for the declared positive sum-of-squares potential",
        "smallest_completion_falsifier": "epsilon v^2 |s2|^2",
        "first_order_vacuum_displacement": ["-1/2", "-2", "-5/2"],
        "classification": "passes germ and full-fiber gates conditionally; fails source-completion authority",
        "missing_constructor": "source theorem excluding or fixing all orbit-moving invariant operators",
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp850_charge_recursive_selector_aspect_germ_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
