"""WP390: exact single-causal-channel rank theorem and hostile completion."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

def main():
    g1, g2, h1, h2 = sp.symbols("g1 g2 h1 h2", real=True)
    chi, eta, eps = sp.symbols("chi eta epsilon", positive=True)
    X, Y = sp.symbols("X Y", real=True)
    v, w = sp.Matrix([g1, g2]), sp.Matrix([h1, h2])
    one = sp.simplify(chi*v*v.T)
    two = sp.simplify(one+eta*w*w.T)
    one_det = sp.factor(one.det())
    two_det = sp.factor(two.det())
    wedge = g1*h2-g2*h1
    amplitude = g1*X+g2*Y
    portal = sp.expand(chi*amplitude**2)
    perturbed_det = sp.factor((one+eps*w*w.T).det())
    collinear = sp.simplify(two.subs({h1: 3*g1, h2: 3*g2}).det())
    checks = {
        "one_channel_gram_outer_product": one == sp.Matrix([[chi*g1**2, chi*g1*g2], [chi*g1*g2, chi*g2**2]]),
        "one_channel_determinant_zero": one_det == 0,
        "one_channel_portal_exact_square": sp.expand(sp.Matrix([X, Y]).T*one*sp.Matrix([X, Y]))[0] == portal,
        "wp389_saturation_forced": sp.simplify((2*chi*g1*g2)**2-4*(chi*g1**2)*(chi*g2**2)) == 0,
        "two_channel_determinant_wedge_square": sp.simplify(two_det-chi*eta*wedge**2) == 0,
        "independent_channels_lift_rank_benchmark": two_det.subs({g1: 1, g2: 0, h1: 0, h2: 1}).is_positive,
        "collinear_second_channel_preserves_rank_one": collinear == 0,
        "small_correction_lifts_rank_linearly": sp.simplify(perturbed_det-eps*chi*wedge**2) == 0,
        "deleting_second_channel_restores_rank_one": two_det.subs(eta, 0) == 0,
        "shell_ratio_depends_on_couplings": sp.solve(sp.Eq(amplitude, 0), X) == [-Y*g2/g1],
        "orthogonal_hostile_pair_has_full_rank": two.subs({g1: 1, g2: 0, h1: 0, h2: 1}).rank() == 2,
        "aligned_hostile_pair_has_rank_one": two.subs({g1: 1, g2: 2, h1: 3, h2: 6}).rank() == 1,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP390",
        "admitted_state_domain": "two invariant CP-odd response coordinates X,Y coupled to one or two positive-susceptibility source channels",
        "faithful_quotient_coordinate": "the physical16 shell response vector (X,Y), with carrier orientation quotiented unless a reference port is calibrated",
        "source_authorized_probe_family": "source-channel coupling vectors, positive susceptibilities, response Gram determinant, and singular-rank test",
        "contextual_partition": "one channel and any collinear completions have rank one; any noncollinear positive channel has rank two and removes the shell kernel",
        "classification": "structural conditional selector: a genuinely unique shared causal channel forces rank-one saturation, but its coupling ratio remains source data",
        "one_channel_gram": str(one),
        "two_channel_determinant": str(two_det),
        "shell_equation": str(sp.Eq(amplitude, 0)),
        "smallest_exact_falsifier": "add a positive orthogonal channel v=(1,0), w=(0,1); the determinant becomes chi*eta and the response rank becomes two",
        "remaining_physical_instrument_gate": "derive uniqueness or exact alignment of all allowed channels and the coupling ratio g2/g1, then measure a response Gram matrix whose smallest singular value remains zero within declared uncertainty",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp390_single_causal_channel_rank.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
