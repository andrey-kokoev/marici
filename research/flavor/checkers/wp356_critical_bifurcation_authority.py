"""WP356: exact selector-authority audit for a pitchfork source potential."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    t = sp.symbols("t", real=True)
    r = sp.symbols("r", real=True)
    u = sp.symbols("u", real=True, positive=True)
    delta = sp.symbols("Delta", real=True, positive=True)
    m = sp.symbols("m", integer=True, positive=True)

    potential = r * t**2 / 2 + u * t**4 / 4
    stationarity = sp.factor(sp.diff(potential, t))
    broken_q = -r / u
    positive_root = sp.sqrt(-r / u)
    response_r = sp.diff(broken_q, r)
    response_u = sp.diff(broken_q, u)
    susceptibility = sp.simplify(sp.diff(positive_root, r))
    discrete_q = sp.simplify(broken_q.subs(r, -m * delta))

    second_at_zero = sp.diff(potential, t, 2).subs(t, 0)
    second_at_broken = sp.simplify(
        sp.diff(potential, t, 2).subs(t**2, broken_q)
    )

    checks = {
        "stationarity_factorizes": stationarity == t * (r + u * t**2),
        "symmetric_curvature_is_r": second_at_zero == r,
        "broken_branch_q_is_minus_r_over_u": broken_q == -r / u,
        "broken_curvature_is_positive_for_r_negative": second_at_broken == -2 * r,
        "control_response_is_nonzero": response_r == -1 / u,
        "quartic_response_is_nonzero_off_criticality": response_u == r / u**2,
        "susceptibility_has_critical_divergence": susceptibility == -1 / (2 * sp.sqrt(-r * u)),
        "discrete_branch_retains_normalization_ratio": discrete_q == delta * m / u,
        "deliberate_equal_q_hostile_pair_has_distinct_sources": (
            sp.simplify(broken_q.subs({r: -1, u: 1}) - broken_q.subs({r: -2, u: 2})) == 0
            and (-1, 1) != (-2, 2)
        ),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    result = {
        "work_package": "WP356",
        "admitted_state_domain": "stationary vacua of V(t)=r*t^2/2+u*t^4/4 with real r and u>0; optional discretization r=-m*Delta with m positive integer and Delta>0",
        "faithful_quotient_coordinate": "the CP-geometry magnitude q=t^2, a one-coordinate physical readout rather than the full physical16 quotient",
        "source_authorized_probe_family": "stationarity, stability, and coefficient interventions within the declared even-quartic source grammar",
        "contextual_partition": "r>=0 selects the symmetric vacuum q=0; r<0 selects a two-sign broken fiber with q=-r/u; discretization labels fibers by m but leaves Delta/u authoritative",
        "classification": "conditional phase selector and sign-pair rigidifier, but neither a numerical nonzero-q selector nor a full physical16 selector",
        "potential": str(potential),
        "stationarity": str(stationarity),
        "broken_q": str(broken_q),
        "response_r": str(response_r),
        "response_u": str(response_u),
        "positive_branch_susceptibility": str(susceptibility),
        "discrete_q": str(discrete_q),
        "smallest_exact_falsifier": "d q/d r=-1/u is nonzero on the broken branch, so proximity to criticality does not erase continuous source authority",
        "hostile_pair": "(r,u)=(-1,1) and (-2,2) are distinct source packets with the same q=1",
        "remaining_physical_instrument_gate": "derive and calibrate r, u, and Delta in one source/readout frame and measure the resulting physical16 displacement; the quartic grammar itself is not yet a flavor-derived action",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp356_critical_bifurcation_authority.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
