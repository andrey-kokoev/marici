"""Exact WP656 independent-sideband background calibration."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
tau = sp.symbols("tau", positive=True, real=True)

# Two signal bins respond to source log-magnitudes u,v and a common background
# nuisance beta. The sideband row observes beta independently with precision tau.
J_signal = sp.Matrix([[2, 0, 1], [0, 2, 1]])
F_signal = J_signal.T*J_signal
A = F_signal[:2, :2]
B = F_signal[:2, 2:]
C0 = F_signal[2, 2]
profiled_without_sideband = sp.simplify(A-B*(sp.Matrix([[C0]]).inv())*B.T)
profiled_with_sideband = sp.simplify(A-B*(sp.Matrix([[C0+tau]]).inv())*B.T)

checks = {
    "signal_region_jacobian_has_only_two_records": J_signal.rank() == 2,
    "unconstrained_background_profile_has_rank_one": profiled_without_sideband.rank() == 1,
    "unconstrained_background_erases_common_mode": profiled_without_sideband*sp.ones(2, 1) == sp.zeros(2, 1),
    "positive_sideband_restores_rank_two": profiled_with_sideband.subs(tau, 1).rank() == 2,
    "sideband_profile_determinant": sp.simplify(
        profiled_with_sideband.det()-16*tau/(tau+2)) == 0,
    "common_mode_information": sp.simplify(
        (sp.ones(1, 2)*profiled_with_sideband*sp.ones(2, 1))[0]/2
        -4*tau/(tau+2)) == 0,
    "zero_sideband_limit_recovers_rank_loss": sp.simplify(
        profiled_with_sideband.subs(tau, 0)
        -profiled_without_sideband) == sp.zeros(2),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)
result = {
    "work_package": "WP656", "status": "PASS", "checks": checks,
    "signal_model": "two labelled signal records plus one common additive background nuisance",
    "uncalibrated_profile": "rank one; common source-rate mode is erased",
    "calibration_instrument": "an independently observed background-only sideband with Fisher precision tau>0",
    "calibrated_profile_determinant": "16 tau/(tau+2)>0",
    "common_mode_information": "4 tau/(tau+2)",
    "completion_stability": "fails as sideband precision tau approaches zero",
    "classification": "detector-derived calibration channel restores local source-magnitude identifiability; it does not select source values",
    "smallest_exact_falsifier": "tau=0, or a sideband contaminated by the same unknown source amplitudes",
    "remaining_gate": "instantiate sideband support, transfer factors, efficiencies, covariance, and uncertainty from a declared experiment without fitting them from the target signal",
}
(ROOT / "results" / "wp656_sideband_background_calibration.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
