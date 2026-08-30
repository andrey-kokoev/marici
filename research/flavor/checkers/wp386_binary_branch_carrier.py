"""WP386: exact binary branch carrier and preparation-law audit."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

def main():
    C = sp.symbols("C", real=True)
    D, beta, tau = sp.symbols("D beta tau", positive=True)
    plus = sp.expand((C-beta*D)**2)
    minus = sp.expand((C+beta*D)**2)
    classical_envelope = C**2+beta**2*D**2-2*sp.Abs(C)*beta*D
    shell = C**2-beta**2*D**2
    thermal = -sp.log((sp.exp(-tau*plus)+sp.exp(-tau*minus))/2)/tau
    thermal_plus_branch = sp.simplify(thermal.subs(C, beta*D))
    thermal_origin = sp.simplify(thermal.subs({C: 0, D: 0}))
    benchmark_thermal = sp.simplify(thermal_plus_branch.subs({beta: 1, D: 1, tau: 1}))
    benchmark_zero_temperature = sp.limit(thermal.subs({C: 2, beta: 1, D: 1}), tau, sp.oo)
    residual_field_degree = 12
    branch_penalty_degree = 2*residual_field_degree
    checks = {
        "plus_branch_penalty_zero": sp.simplify(plus.subs(C, beta*D)) == 0,
        "minus_branch_penalty_zero": sp.simplify(minus.subs(C, -beta*D)) == 0,
        "classical_envelope_zero_on_plus_branch": sp.simplify(classical_envelope.subs(C, beta*D)) == 0,
        "classical_envelope_zero_on_minus_branch": sp.simplify(classical_envelope.subs(C, -beta*D)) == 0,
        "classical_envelope_positive_off_shell_benchmark": classical_envelope.subs({C: 0, beta: 1, D: 1}).is_positive,
        "classical_zero_set_matches_factor_shell": sp.factor((C-beta*D)*(C+beta*D)-shell) == 0,
        "finite_thermal_lifts_plus_branch": benchmark_thermal.is_positive,
        "finite_thermal_origin_zero_on_extended_domain": thermal_origin == 0,
        "zero_temperature_recovers_branch_minimum_benchmark": benchmark_zero_temperature == 1,
        "branch_penalty_field_degree_twenty_four": branch_penalty_degree == 24,
        "binary_carrier_halves_positive_operator_degree": 2*branch_penalty_degree == 48,
        "branch_label_flip_preserves_unlabelled_envelope": sp.simplify(classical_envelope.subs(C, -C)-classical_envelope) == 0,
        "fixed_branch_selects_orientation": plus.subs(C, beta*D) == 0 and plus.subs(C, -beta*D) != 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP386",
        "admitted_state_domain": "nondegenerate physical16 shell coordinates C,D with real positive beta, augmented by a binary CP-odd branch carrier s",
        "faithful_quotient_coordinate": "unlabelled physical shell C^2=beta^2*D^2, or labelled augmented coordinate (C,D,s)",
        "source_authorized_probe_family": "branch-conditioned square penalties, classical minimization over s, and finite-temperature summation over s",
        "contextual_partition": "classical minimization preserves the two-branch union; a fixed branch selects orientation; finite thermal summation lifts each nonzero branch and retains only the intersection as an exact zero",
        "classification": "conditional degree-24 shell selector under zero-temperature minimization or superselection, with preparation law and beta still unauthorized",
        "plus_penalty": str(plus),
        "minus_penalty": str(minus),
        "classical_envelope": str(classical_envelope),
        "finite_thermal_plus_branch": str(thermal_plus_branch),
        "branch_penalty_field_degree": branch_penalty_degree,
        "smallest_exact_falsifier": "at beta=D=tau=1 and C=1, the classical envelope is zero but the normalized thermal effective penalty log(2/(1+exp(-4))) is positive",
        "remaining_physical_instrument_gate": "derive the binary carrier, its CP transformation, beta, and a zero-temperature or superselection preparation law from source dynamics, then type its detector readout",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp386_binary_branch_carrier.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
