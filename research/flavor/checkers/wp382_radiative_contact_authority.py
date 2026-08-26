"""WP382: exact one-loop authority audit for a radiative flavor contact."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

def main():
    F = sp.symbols("F", real=True)
    M2, mu2, g = sp.symbols("M2 mu2 g", positive=True)
    n = sp.symbols("n", positive=True, integer=True)
    sigma = sp.symbols("sigma", real=True)
    c, t = sp.symbols("c t", real=True)
    x = M2 + g*F
    loop = sigma*n*x**2*(sp.log(x/mu2)-sp.Rational(3, 2))/(64*sp.pi**2)
    curvature = sp.factor(sp.diff(loop, F, 2).subs(F, 0))
    expected = sigma*n*g**2*sp.log(M2/mu2)/(32*sp.pi**2)
    total_curvature = sp.factor(c + curvature)
    shifted = sp.expand_log(curvature.subs(mu2, mu2*sp.exp(2*t)), force=True)
    scale_shift = sp.simplify(shifted-curvature)
    beta_c = sigma*n*g**2/(16*sp.pi**2)
    running_total = sp.simplify(
        (c + beta_c*t) + shifted - total_curvature
    )
    scalar_below = sp.simplify(curvature.subs({sigma: 1, mu2: M2/sp.exp(2)}))
    scalar_above = sp.simplify(curvature.subs({sigma: 1, mu2: M2*sp.exp(2)}))
    matching = sp.simplify(curvature.subs(mu2, M2))
    finite_shift = sp.symbols("delta_c", real=True)

    checks = {
        "one_loop_curvature_exact": sp.simplify(curvature-expected) == 0,
        "scalar_below_scale_positive": scalar_below.is_positive,
        "scalar_above_scale_negative": scalar_above.is_negative,
        "minimal_subtraction_matching_curvature_zero": matching == 0,
        "fermion_statistics_reverses_sign": sp.simplify(curvature.subs(sigma, -1)+curvature.subs(sigma, 1)) == 0,
        "scale_shift_exact": sp.simplify(scale_shift + sigma*n*g**2*t/(16*sp.pi**2)) == 0,
        "counterterm_running_restores_scale_invariance": running_total == 0,
        "finite_counterterm_changes_curvature": sp.simplify((total_curvature+finite_shift)-total_curvature) == finite_shift,
        "positive_finite_shift_can_reverse_hostile_benchmark": (total_curvature.subs({sigma: 1, n: 1, g: 1, M2: 1, mu2: sp.exp(2), c: 1})).is_positive,
        "zero_boundary_does_not_survive_scale_change": sp.simplify(scalar_below-scalar_above) != 0,
        "deleting_source_coupling_kills_loop_contact": curvature.subs(g, 0) == 0,
        "boson_fermion_pair_can_cancel": sp.simplify(curvature.subs(sigma, 1)+curvature.subs(sigma, -1)) == 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP382",
        "admitted_state_domain": "one-loop modes with affine invariant mass-squared M2+gF on the nondegenerate physical16 residual stratum, plus a local F-squared counterterm",
        "faithful_quotient_coordinate": "WP378 weak-basis-invariant shell residual F",
        "source_authorized_probe_family": "Coleman-Weinberg Hessian, scale transport, statistics reversal, deletion, and finite-counterterm shifts",
        "contextual_partition": "fixed microscopic spectrum determines running, while renormalization boundary conditions label inequivalent local contact curvatures",
        "classification": "radiative dynamics generates and transports a contact but does not select its sign or finite value without a source-authorized renormalization condition",
        "one_loop_curvature": str(curvature),
        "total_curvature": str(total_curvature),
        "scale_shift": str(scale_shift),
        "counterterm_beta": str(beta_c),
        "hostile_scalar_curvatures": {"below_threshold": str(scalar_below), "above_threshold": str(scalar_above)},
        "smallest_exact_falsifier": "the same scalar source gives opposite curvature signs at mu2=M2/exp(2) and mu2=M2*exp(2), while its curvature vanishes at mu2=M2",
        "remaining_physical_instrument_gate": "freeze a physical subtraction observable or UV boundary condition that fixes the finite F-squared coefficient, then show positivity and ensemble survival in detector units",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp382_radiative_contact_authority.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
