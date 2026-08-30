"""WP401: exact two-error, two-readout calibration for the WP400 mediator."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

def main():
    dm, dj = sp.symbols("delta_m delta_j", real=True)
    M2 = sp.symbols("M2", positive=True)
    J0 = sp.symbols("J0", real=True, nonzero=True)
    wH, wA = sp.symbols("w_H w_A", positive=True)
    H = M2+dm
    A = (J0+dj)/H
    readout = sp.Matrix([H, A])
    jacobian = sp.simplify(readout.jacobian((dm, dj)).subs({dm: 0, dj: 0}))
    determinant = sp.factor(jacobian.det())
    metric = sp.diag(wH, wA)
    gram = sp.simplify(jacobian.T*metric*jacobian)
    gram_det = sp.factor(gram.det())
    displacement_row = jacobian[1, :]
    blind_vector = sp.Matrix([M2, J0])
    recovered_dm = H-M2
    recovered_dj = sp.factor(A*H-J0)
    J1 = sp.symbols("J1", real=True)
    locked_source_direction = sp.Matrix([1, J1])
    locked_detector_direction = sp.simplify(jacobian*locked_source_direction)
    checks = {
        "jacobian_exact": jacobian == sp.Matrix([[1, 0], [-J0/M2**2, 1/M2]]),
        "jacobian_rank_two": jacobian.rank() == 2,
        "jacobian_determinant_positive": determinant == 1/M2,
        "positive_metric_gram_determinant": sp.simplify(gram_det-wH*wA/M2**2) == 0,
        "positive_metric_gram_full_rank": gram_det.is_positive,
        "displacement_only_rank_one": displacement_row.rank() == 1,
        "displacement_only_blind_vector_exact": sp.simplify((displacement_row*blind_vector)[0]) == 0,
        "curvature_readout_detects_blind_vector": (jacobian[0, :]*blind_vector)[0] == M2,
        "global_mass_error_reconstruction_exact": recovered_dm == dm,
        "global_tadpole_error_reconstruction_exact": recovered_dj == dj,
        "locked_knob_detector_tangent_exact": locked_detector_direction == sp.Matrix([1, (J1*M2-J0)/M2**2]),
        "deleting_curvature_readout_restores_kernel": len(displacement_row.nullspace()) == 1,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP401",
        "admitted_state_domain": "the WP400 stable mediator with independent small curvature and tadpole perturbations and positive calibrated detector weights",
        "faithful_quotient_coordinate": "the two-dimensional source-error packet (delta_m,delta_j)",
        "source_authorized_probe_family": "mediator curvature or pole readout H and stationary displacement readout A_star in one calibrated frame",
        "contextual_partition": "displacement alone has one-dimensional fibers; the joint curvature-displacement map has singleton fibers on the healthy domain",
        "classification": "exact source-calibrated two-error separator and instrument design, not a selector of the locked knob slope",
        "detector_jacobian": str(jacobian),
        "jacobian_determinant": str(determinant),
        "weighted_gram_determinant": str(gram_det),
        "displacement_blind_vector": str(blind_vector),
        "locked_knob_detector_direction": str(locked_detector_direction),
        "smallest_exact_falsifier": "with displacement readout alone, the nonzero source perturbation (delta_m,delta_j) proportional to (M2,J0) is invisible to first order",
        "remaining_physical_instrument_gate": "measure mediator pole curvature and mean displacement with a shared calibration, uncertainties, widths, backgrounds, and support sufficient to keep the smallest singular value positive",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp401_two_readout_knob_calibration.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
