"""WP403: exact completion-safe calibration and withheld-context design."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

def main():
    c, omega = sp.symbols("c omega", real=True)
    M2, J0, J1, J2, Q2 = sp.symbols("M2 J0 J1 J2 Q2", real=True)
    G0, G1 = sp.symbols("Gamma0 Gamma1", real=True)
    H = M2+c+Q2*c**2
    T = J0+J1*c+J2*c**2
    Astatic = T/H
    static_parameters = (M2, J0, J1, J2, Q2)
    static_contexts = (0, 1, 2)
    joint_records = []
    for point in static_contexts:
        joint_records.extend((H.subs(c, point), Astatic.subs(c, point)))
    baseline = {M2: 1, J0: 1, J1: 2, J2: 0, Q2: 0}
    joint_jacobian = sp.simplify(sp.Matrix(joint_records).jacobian(static_parameters).subs(baseline))
    certified_minor = sp.factor(joint_jacobian[[0, 1, 2, 3, 5], :].det())

    dynamic = T/(H-omega**2-sp.I*omega*(G0+G1*c))
    imag_dynamic = sp.simplify(sp.im(dynamic))
    width_points = ((0, 2), (1, 2))
    width_records = sp.Matrix([imag_dynamic.subs({c: cp, omega: op}) for cp, op in width_points])
    width_baseline = baseline | {G0: 1, G1: 1}
    width_jacobian = sp.simplify(width_records.jacobian((G0, G1)).subs(width_baseline))

    R2, MX2 = sp.symbols("R2 MX2", real=True)
    extra_residual = R2/(MX2-omega**2)
    extra_points = (0, 1)
    extra_records = sp.Matrix([extra_residual.subs(omega, point) for point in extra_points])
    extra_baseline = {R2: 1, MX2: 9}
    extra_jacobian = sp.simplify(extra_records.jacobian((R2, MX2)).subs(extra_baseline))

    static_withheld = sp.Matrix([H, Astatic]).subs(baseline | {c: 3})
    dynamic_withheld = sp.simplify(dynamic.subs(width_baseline | {c: 2, omega: 2}))
    extra_withheld = sp.simplify(extra_residual.subs(extra_baseline | {omega: 2}))
    checks = {
        "joint_static_calibration_rank_five": joint_jacobian.rank() == 5,
        "joint_static_certified_minor_nonzero": certified_minor == sp.Rational(1, 3),
        "three_contexts_identify_quadratic_curvature_and_tadpole": len(joint_jacobian.nullspace()) == 0,
        "displacement_only_common_factor_kernel_removed": joint_jacobian*sp.Matrix([-1, -1, -1, 2, 1]) != sp.zeros(6, 1),
        "two_dynamic_contexts_identify_width": width_jacobian.rank() == 2,
        "width_minor_nonzero": width_jacobian.det() != 0,
        "two_spectral_residuals_identify_nonzero_extra_pole": extra_jacobian.rank() == 2,
        "extra_pole_minor_nonzero": extra_jacobian.det() != 0,
        "withheld_static_prediction_exact": static_withheld == sp.Matrix([4, sp.Rational(7, 4)]),
        "withheld_dynamic_prediction_exact": dynamic_withheld == -sp.Rational(5, 37)+sp.I*sp.Rational(30, 37),
        "withheld_extra_pole_prediction_exact": extra_withheld == sp.Rational(1, 5),
        "zero_extra_residue_still_deletes_mass_authority": sp.diff(extra_residual, MX2).subs(R2, 0) == 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP403",
        "admitted_state_domain": "the WP402 completed grammar with nonzero extra-pole residue, calibrated at three joint static contexts, two absorptive contexts, and two extra-pole spectral points",
        "faithful_quotient_coordinate": "the nine-parameter completed source packet away from pole singularities and the zero-extra-residue mass fiber",
        "source_authorized_probe_family": "joint curvature-displacement records, absorptive line-shape records, and residual extra-pole spectroscopy",
        "contextual_partition": "the staged calibration has singleton local fibers on the admitted nonzero-residue domain; decoupled extra-pole masses remain quotiented",
        "classification": "completion-safe exact calibration schedule with three reserved no-refit predictions; not yet an executed experiment",
        "joint_static_jacobian_rank": joint_jacobian.rank(),
        "joint_static_minor": str(certified_minor),
        "width_jacobian_determinant": str(sp.factor(width_jacobian.det())),
        "extra_pole_jacobian_determinant": str(sp.factor(extra_jacobian.det())),
        "withheld_predictions": {
            "static_H_A_at_c3": [str(value) for value in static_withheld],
            "dynamic_A_at_c2_omega2": str(dynamic_withheld),
            "extra_residual_at_omega2": str(extra_withheld),
        },
        "smallest_exact_falsifier": "any withheld record differing from (H,A)=(4,7/4), A(omega=2,c=2)=(-5+30i)/37, or extra residual 1/5 rejects the frozen benchmark without refitting",
        "remaining_physical_instrument_gate": "bind each calibration and withheld context to a real trace-adjoint/Higgs mediator operation and certified pole, displacement, and line-shape measurements",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp403_completion_safe_context_design.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
