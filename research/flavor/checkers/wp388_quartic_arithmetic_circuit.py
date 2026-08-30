"""WP388: exact quartic arithmetic-circuit completion and authority audit."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

def main():
    x, y, r, t, z, w = sp.symbols("x y r t z w", real=True)
    a, b, c = sp.symbols("a b c", positive=True)
    g1, g2, g3 = z-x*y, w-z*r, w-t
    potential = sp.expand(a*g1**2+b*g2**2+c*g3**2)
    solution = {z: x*y, w: x*y*r, t: x*y*r}
    aux_hessian = sp.simplify(sp.hessian(potential, (z, w)).subs(solution))
    aux_det = sp.factor(aux_hessian.det())
    aux_trace = sp.factor(sp.trace(aux_hessian))
    wrong_final = sp.expand(a*g1**2+b*g2**2+c*(w+t)**2)
    hostile = {x: 1, y: 2, r: 3, t: 6, z: 2, w: 6}
    deleted_final = sp.expand(a*g1**2+b*g2**2)
    checks = {
        "compiled_solution_zero": potential.subs(solution) == 0,
        "gate_equations_imply_target": sp.factor(g3.subs({z: x*y, w: x*y*r})) == x*y*r-t,
        "auxiliary_hessian_determinant_positive": aux_det.is_positive,
        "auxiliary_hessian_trace_positive": aux_trace.is_positive,
        "auxiliary_hessian_positive_definite": aux_hessian[0, 0].is_positive and aux_det.is_positive,
        "maximum_gate_penalty_degree_four": sp.Poly(potential, x, y, r, t, z, w).total_degree() == 4,
        "hostile_correct_circuit_zero": potential.subs(hostile) == 0,
        "hostile_wrong_final_gate_nonzero": wrong_final.subs(hostile).is_positive,
        "deleting_final_gate_blinds_target": not deleted_final.has(t),
        "deleted_gate_accepts_wrong_target": deleted_final.subs({x: 1, y: 2, r: 3, t: -99, z: 2, w: 6}) == 0,
        "wrong_sign_circuit_selects_different_shell": wrong_final.subs({z: x*y, w: x*y*r, t: -x*y*r}) == 0,
        "positive_weights_make_zero_require_each_gate": all(weight.is_positive for weight in (a, b, c)),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP388",
        "admitted_state_domain": "real arithmetic inputs and auxiliary gate variables with strictly positive gate-penalty weights",
        "faithful_quotient_coordinate": "the projected input relation t=x*y*r; flavor descent additionally requires an equivariant circuit from fundamental fields",
        "source_authorized_probe_family": "positive multiplication-gate constraints and their auxiliary Hessian",
        "contextual_partition": "each frozen circuit has a faithful zero-set projection to its compiled polynomial relation; different final gates define different selected shells",
        "classification": "quartic locality compiler and presentation rigidifier, not independent selector authority",
        "compiled_potential": str(potential),
        "auxiliary_hessian": str(aux_hessian),
        "auxiliary_hessian_determinant": str(aux_det),
        "maximum_polynomial_degree": 4,
        "smallest_exact_falsifier": "the correct and sign-flipped final gates are both positive quartic circuits but select t=x*y*r and t=-x*y*r respectively",
        "remaining_physical_instrument_gate": "derive one equivariant gate graph, representations, positive weights, and beta from microscopic flavor dynamics rather than compiling the desired shell",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp388_quartic_arithmetic_circuit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
