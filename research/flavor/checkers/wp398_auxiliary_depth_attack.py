"""WP398: exact auxiliary-circuit attack on effective degree bounds."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

def main():
    c, z, w = sp.symbols("c z w", real=True)
    a, b, eps = sp.symbols("a b epsilon", positive=True)
    gate1 = z-c*(c-1)
    gate2 = w-z*(c-2)
    potential = sp.expand(a*gate1**2+b*gate2**2)
    solution = {z: c*(c-1), w: c*(c-1)*(c-2)}
    eliminated_w = sp.factor(solution[w])
    aux_hessian = sp.simplify(sp.hessian(potential, (z, w)).subs(solution))
    aux_det = sp.factor(aux_hessian.det())
    aux_trace = sp.factor(sp.trace(aux_hessian))
    manifest_trace = 2*a+2*b*((c-2)**2+1)
    manifest_leading_minor = 2*a+2*b*(c-2)**2
    response = sp.Matrix([1, eps*eliminated_w])
    base = sp.Matrix([1, 0])
    withheld = response.subs(c, 3)
    joint_det = sp.factor((base*base.T+withheld*withheld.T).det())
    checks = {
        "compiled_solution_satisfies_first_gate": sp.simplify(gate1.subs(solution)) == 0,
        "compiled_solution_satisfies_second_gate": sp.simplify(gate2.subs(solution)) == 0,
        "compiled_potential_zero": sp.simplify(potential.subs(solution)) == 0,
        "effective_completion_is_wp397_cubic": eliminated_w == c*(c-1)*(c-2),
        "local_potential_maximum_degree_four": sp.Poly(potential, c, z, w).total_degree() == 4,
        "auxiliary_hessian_determinant_positive": aux_det == 4*a*b,
        "auxiliary_hessian_trace_positive": sp.simplify(aux_trace-manifest_trace) == 0 and manifest_trace.is_positive,
        "auxiliary_hessian_positive_definite": sp.simplify(aux_hessian[0, 0]-manifest_leading_minor) == 0 and manifest_leading_minor.is_positive and aux_det.is_positive,
        "compiled_response_invisible_at_three_tests": all(response.subs(c, point) == base for point in (0, 1, 2)),
        "compiled_response_rotates_at_withheld_context": withheld == sp.Matrix([1, 6*eps]),
        "compiled_withheld_joint_determinant": joint_det == 36*eps**2,
        "deleting_second_gate_leaves_output_unconstrained": not (a*gate1**2).has(w),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP398",
        "admitted_state_domain": "one real context coordinate and two real auxiliary gate variables with positive gate weights",
        "faithful_quotient_coordinate": "the eliminated projective response direction as a function of context",
        "source_authorized_probe_family": "quartic gate potential, exact elimination, auxiliary Hessian, and withheld-context wedge",
        "contextual_partition": "the constant and circuit-completed responses agree at contexts 0,1,2 and differ at context 3 despite a degree-four local gate grammar",
        "classification": "exact attack on local vertex degree as a sufficient bound on effective contextual complexity",
        "gate_potential": str(potential),
        "eliminated_output": str(eliminated_w),
        "auxiliary_hessian_determinant": str(aux_det),
        "withheld_joint_determinant": str(joint_det),
        "smallest_exact_falsifier": "two stable quadratic multiplication gates compile the cubic invisible completion while every local term remains degree at most four",
        "remaining_physical_instrument_gate": "derive bounds on auxiliary field content, circuit depth, topology, and representations from the source action, not merely a local operator-degree bound",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp398_auxiliary_depth_attack.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
