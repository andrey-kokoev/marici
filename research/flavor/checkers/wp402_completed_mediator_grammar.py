"""WP402: exact completion audit for nonlinear, width, and extra-pole terms."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

def main():
    c, omega = sp.symbols("c omega", real=True)
    M2, J0, J1, J2, Q2 = sp.symbols("M2 J0 J1 J2 Q2", real=True)
    G0, G1 = sp.symbols("Gamma0 Gamma1", real=True)
    numerator = J0+J1*c+J2*c**2
    dispersive = M2+c+Q2*c**2-omega**2
    width = G0+G1*c
    dynamic = numerator/(dispersive-sp.I*omega*width)
    static = sp.factor(dynamic.subs(omega, 0))
    static_parameters = (M2, J0, J1, J2, Q2)
    contexts = (0, 1, 2, 3)
    static_records = sp.Matrix([static.subs(c, point) for point in contexts])
    baseline = {M2: 1, J0: 1, J1: 2, J2: 0, Q2: 0}
    static_jacobian = sp.simplify(static_records.jacobian(static_parameters).subs(baseline))
    static_kernel = static_jacobian.nullspace()

    imag_response = sp.simplify(sp.im(dynamic))
    width_baseline = baseline | {G0: 1, G1: 1}
    dynamic_points = ((0, 2), (1, 2))
    absorptive_records = sp.Matrix([imag_response.subs({c: cp, omega: op}) for cp, op in dynamic_points])
    width_jacobian = sp.simplify(absorptive_records.jacobian((G0, G1)).subs(width_baseline))

    R2, MX2 = sp.symbols("R2 MX2", real=True)
    extra = R2/(MX2+c-omega**2)
    completed = dynamic+extra
    checks = {
        "static_limit_is_real_rational_response": sp.simplify(static-numerator/(M2+c+Q2*c**2)) == 0,
        "finite_width_exactly_invisible_statically": not static.has(G0) and not static.has(G1),
        "four_static_contexts_have_rank_four": static_jacobian.rank() == 4,
        "five_static_parameters_leave_one_kernel": len(static_kernel) == 1,
        "static_kernel_is_nonzero": static_kernel[0] != sp.zeros(5, 1),
        "two_absorptive_contexts_identify_two_width_coefficients": width_jacobian.rank() == 2,
        "width_jacobian_determinant_nonzero": width_jacobian.det() != 0,
        "zero_frequency_absorptive_response_vanishes": imag_response.subs(omega, 0) == 0,
        "extra_pole_deletes_at_zero_residue": completed.subs(R2, 0) == dynamic,
        "extra_mass_is_blind_at_zero_residue": sp.diff(completed, MX2).subs(R2, 0) == 0,
        "nonzero_extra_residue_changes_response": sp.diff(completed, R2) == 1/(MX2+c-omega**2),
        "wp400_recovered_when_completion_deleted": sp.simplify(static.subs({J2: 0, Q2: 0})-(J0+J1*c)/(M2+c)) == 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP402",
        "admitted_state_domain": "one finite-width mediator with quadratic context corrections, plus one optional extra pole, away from declared pole singularities",
        "faithful_quotient_coordinate": "the completed source packet (M2,J0,J1,J2,Q2,Gamma0,Gamma1,R2,MX2) modulo the exact zero-residue mass fiber",
        "source_authorized_probe_family": "four static displacements, two absorptive dynamic readouts, and an extra-pole spectral response",
        "contextual_partition": "static data leave a nonlinear-correction kernel and are completely blind to width; absorptive contexts identify affine width; an extra pole mass remains blind at zero residue",
        "classification": "completion audit and minimal probe separation, not yet an executed physical calibration",
        "static_response": str(static),
        "static_jacobian_rank": static_jacobian.rank(),
        "static_kernel": str(static_kernel[0]),
        "width_jacobian": str(width_jacobian),
        "width_jacobian_determinant": str(sp.factor(width_jacobian.det())),
        "smallest_exact_falsifier": "all static displacement contexts have zero derivative with respect to Gamma0 and Gamma1, so no static withheld test can validate finite-width completion",
        "remaining_physical_instrument_gate": "add calibrated absorptive line-shape contexts and nonzero-residue extra-pole searches to the pole/displacement instrument before reserving a no-refit test",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp402_completed_mediator_grammar.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
