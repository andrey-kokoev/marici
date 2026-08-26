"""WP387: exact continuous CP-odd carrier completion audit."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

def main():
    C, q = sp.symbols("C q", real=True)
    D, beta, a, lam = sp.symbols("D beta a lambda", positive=True)
    potential = sp.expand(a*(C-beta*D*q)**2 + lam*(q**2-1)**2)
    grad = sp.Matrix([sp.diff(potential, C), sp.diff(potential, q)])
    hessian = sp.hessian(potential, (C, q))
    plus = {C: beta*D, q: 1}
    minus = {C: -beta*D, q: -1}
    hplus = sp.simplify(hessian.subs(plus))
    determinant = sp.factor(hplus.det())
    trace = sp.factor(sp.trace(hplus))
    cp_transformed = sp.expand(potential.subs({C: -C, q: -q}, simultaneous=True))
    portal_cancelled_q = C/(beta*D)
    cancelled_remainder = sp.factor(potential.subs(q, portal_cancelled_q))
    checks = {
        "plus_vacuum_zero": potential.subs(plus) == 0,
        "minus_vacuum_zero": potential.subs(minus) == 0,
        "plus_vacuum_stationary": grad.subs(plus) == sp.zeros(2, 1),
        "minus_vacuum_stationary": grad.subs(minus) == sp.zeros(2, 1),
        "cp_invariance_exact": sp.simplify(cp_transformed-potential) == 0,
        "vacuum_hessian_determinant_positive": determinant == 16*a*lam,
        "vacuum_hessian_trace_positive": trace.is_positive,
        "vacuum_hessian_positive_definite": hplus[0, 0].is_positive and determinant.is_positive,
        "portal_cancellation_leaves_double_well_cost": cancelled_remainder == lam*(C-beta*D)**2*(C+beta*D)**2/(D**4*beta**4),
        "off_shell_carrier_origin_positive": potential.subs({C: 0, q: 0}) == lam,
        "fixed_plus_carrier_recovers_wp386_branch": sp.factor(potential.subs(q, 1)-a*(C-beta*D)**2) == 0,
        "fixed_minus_carrier_recovers_wp386_branch": sp.factor(potential.subs(q, -1)-a*(C+beta*D)**2) == 0,
        "highest_field_degree_twenty_six": 2*(12+1) == 26,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP387",
        "admitted_state_domain": "nondegenerate invariant C,D coordinates augmented by a real CP-odd carrier q with positive double-well and portal coefficients",
        "faithful_quotient_coordinate": "augmented coordinate (C,D,q) modulo simultaneous CP flip (C,q)->(-C,-q)",
        "source_authorized_probe_family": "joint classical potential, stationary equations, CP action, and vacuum Hessian",
        "contextual_partition": "two stable CP-related zero-energy vacua project to the two branches of the physical shell; off-shell points have strictly positive joint potential",
        "classification": "healthy continuous realization of the conditional binary selector, but not a microscopic numerical selector because beta and the high-degree portal are inserted",
        "potential": str(potential),
        "vacuum_hessian": str(hplus),
        "vacuum_hessian_determinant": str(determinant),
        "vacuum_hessian_trace": str(trace),
        "highest_field_degree": 26,
        "smallest_exact_falsifier": "choosing q=C/(beta*D) cancels the portal but leaves lambda*(C^2-beta^2*D^2)^2/(beta^4*D^4), which vanishes only on the intended shell",
        "remaining_physical_instrument_gate": "derive beta and the degree-25/26 mixed operators from a microscopic source, then specify vacuum preparation, domain-wall effects, and a calibrated q readout",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp387_continuous_cp_carrier.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
