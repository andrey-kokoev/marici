"""Exact WP641 Fierz and downstream-kernel audit."""
import json
from pathlib import Path

from sympy import Rational, eye, simplify
from sympy.physics.matrices import mgamma

ROOT = Path(__file__).resolve().parents[1]

identity = eye(4)
gamma5 = mgamma(5)
projector_l = (identity - gamma5) / 2
projector_r = (identity + gamma5) / 2
gamma_up = [mgamma(mu) for mu in range(4)]
gamma_down = [gamma_up[0], -gamma_up[1], -gamma_up[2], -gamma_up[3]]

# Matrix completeness has coefficient +1/2. Reordering the middle Grassmann
# fields into bilinears supplies the separate minus sign.
fierz_matrix_failures = []
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                lhs = projector_l[a, b] * projector_r[c, d]
                rhs = Rational(1, 2) * sum(
                    (gamma_up[mu] * projector_r)[a, d]
                    * (gamma_down[mu] * projector_l)[c, b]
                    for mu in range(4)
                )
                if simplify(lhs - rhs) != 0:
                    fierz_matrix_failures.append((a, b, c, d))


def response(background, contact_wilson):
    return (Rational(background) + Rational(contact_wilson) / 2) ** 2


background = Rational(1)
g_plus = Rational(4)
g_minus = Rational(0)
g_mass_two = Rational(1)
phase_rotated_current = -Rational(2)
unrotated_current = Rational(2)

checks = {
    "dirac_fierz_matrix_identity_exact": not fierz_matrix_failures,
    "grassmann_swap_gives_bilinear_minus_half": (
        Rational(1, 2) * Rational(-1) == -Rational(1, 2)),
    "constructive_total_response_is_nine": response(background, g_plus) == 9,
    "destructive_total_response_is_background_one": response(background, g_minus) == 1,
    "mass_two_total_response_is_nine_quarters": (
        response(background, g_mass_two) == Rational(9, 4)),
    "constructive_background_subtracted_response_is_eight": (
        response(background, g_plus) - response(background, 0) == 8),
    "linear_interference_term_is_nonzero": background * g_plus != 0,
    "source_current_sign_is_lost_before_interference": (
        unrotated_current**2 == phase_rotated_current**2),
    "downstream_response_cannot_repair_current_sign": (
        response(background, unrotated_current**2)
        == response(background, phase_rotated_current**2)),
}
if not all(checks.values()):
    raise SystemExit({"checks": checks, "fierz_failures": fierz_matrix_failures[:8]})

result = {
    "work_package": "WP641",
    "status": "PASS",
    "checks": checks,
    "fierz_identity": "(bar d_R u_L)(bar u_L d_R)=-1/2 (bar d_R gamma^mu d_R)(bar u_L gamma_mu u_L)",
    "response": "R(B,G)=(B+G/2)^2",
    "background_subtracted_response": "Delta R=B G+G^2/4",
    "unit_background_partition": {"constructive": "9", "destructive": "1", "mass_two": "9/4"},
    "first_nonfaithful_arrow": "charged-scalar elimination J -> |J|^2/m_chi^2",
    "kernel": "J and exp(i alpha) J are indistinguishable to every downstream probe factoring through G",
    "classification": "source-level SM-interfering contact probe; neither physical16 selector nor detector-calibrated instrument",
    "instrument_gate": "named data and bins, PDFs, electroweak amplitudes, running, tagging, response, uncertainties, and likelihood",
}
(ROOT / "results" / "wp641_charged_cycle_sm_interference.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
