"""Exact WP657 independent efficiency-control calibration."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
kL, kR = sp.symbols("k_L k_R", positive=True, real=True)
J_signal = sp.Matrix([[2, 0, 1, 0], [0, 2, 0, 1]])
F_signal = J_signal.T*J_signal
A = F_signal[:2, :2]
B = F_signal[:2, 2:]
C_signal = F_signal[2:, 2:]
K = sp.diag(kL, kR)
profiled_uncalibrated = sp.simplify(A-B*C_signal.inv()*B.T)
profiled_calibrated = sp.simplify(A-B*(C_signal+K).inv()*B.T)
expected = sp.diag(4*kL/(1+kL), 4*kR/(1+kR))

checks = {
    "uncalibrated_efficiencies_erase_both_source_modes": profiled_uncalibrated == sp.zeros(2),
    "independent_controls_give_expected_profile": sp.simplify(profiled_calibrated-expected) == sp.zeros(2),
    "positive_controls_restore_rank_two": profiled_calibrated.subs({kL: 1, kR: 1}).rank() == 2,
    "calibrated_profile_determinant": sp.simplify(
        profiled_calibrated.det()-16*kL*kR/((1+kL)*(1+kR))) == 0,
    "one_missing_control_leaves_rank_one": profiled_calibrated.subs({kL: 1, kR: 0}).rank() == 1,
    "both_missing_controls_leave_rank_zero": profiled_calibrated.subs({kL: 0, kR: 0}).rank() == 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)
result = {
    "work_package": "WP657", "status": "PASS", "checks": checks,
    "signal_model": "log yields 2u+eta_L and 2v+eta_R with independent log-efficiency nuisances",
    "uncalibrated_profile": "rank zero; both source magnitudes are exactly confounded",
    "calibration_instrument": "two independently supported efficiency control samples with precisions k_L,k_R",
    "calibrated_profile": "diag(4k_L/(1+k_L),4k_R/(1+k_R))",
    "calibrated_determinant": "16k_Lk_R/((1+k_L)(1+k_R))",
    "classification": "two independent detector controls are necessary and sufficient for local magnitude identification under separate efficiencies",
    "smallest_exact_falsifier": "k_L=0 or k_R=0, which leaves at least one source magnitude unidentifiable",
    "remaining_gate": "bind each control sample, transfer factor, covariance, support, and uncertainty to an actual experiment independently of the signal",
}
(ROOT / "results" / "wp657_efficiency_control_calibration.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
