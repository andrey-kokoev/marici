"""Dispersively reconstruct g2 and g3 from the two typed Phi1 cuts."""

import hashlib
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
from check_breit_wheeler_tree_normalization import kernel_matrix, kinematics  # noqa: E402
from check_nonforward_breit_wheeler_cut import (  # noqa: E402
    helicity_polarization, photon, trace_pair
)


def two_diagonal_cuts(s, transfer, inner_order):
    """Return C[++ ,++] and C[+- ,+-] at fixed physical transfer."""
    E = np.sqrt(s)/2
    beta = np.sqrt(1-4/s)
    theta = np.arccos(1+2*transfer/s)
    p1 = photon(E, 0, 0)
    p2 = photon(E, np.pi, 0)
    p3 = photon(E, theta, 0)
    p4 = photon(E, np.pi-theta, np.pi)
    eps_pp = (
        helicity_polarization(0, 0, 1),
        helicity_polarization(np.pi, 0, 1),
    )
    eps_pm = (
        helicity_polarization(0, 0, 1),
        helicity_polarization(np.pi, 0, -1),
    )
    # Use the declared final-state spherical frames literally.  At theta=0
    # simplifying these vectors by eye loses the azimuth-pi frame rotation.
    final_pp = (
        helicity_polarization(theta, 0, 1),
        -helicity_polarization(np.pi-theta, np.pi, 1),
    )
    final_pm = (
        helicity_polarization(theta, 0, 1),
        -helicity_polarization(np.pi-theta, np.pi, -1),
    )
    mus, weights = np.polynomial.legendre.leggauss(inner_order)
    phis = 2*np.pi*(np.arange(inner_order)+0.5)/inner_order
    total = np.zeros(2, dtype=complex)
    for mu, weight in zip(mus, weights):
        for phi in phis:
            _, _, k1, k2 = kinematics(beta, mu, phi)
            x_pp = kernel_matrix(p1, p2, k1, *eps_pp)
            x_pm = kernel_matrix(p1, p2, k1, *eps_pm)
            r_pp = kernel_matrix(p3, p4, k1, *final_pp)
            r_pm = kernel_matrix(p3, p4, k1, *final_pm)
            angular_weight = weight*(2*np.pi/inner_order)
            total[0] += angular_weight*trace_pair(k1, k2, x_pp, r_pp)
            total[1] += angular_weight*trace_pair(k1, k2, x_pm, r_pm)
    return beta*total/(64*np.pi**2)


def moments(transfer, outer_order, inner_order):
    nodes, weights = np.polynomial.legendre.leggauss(outer_order)
    betas = (nodes+1)/2
    weights = weights/2
    result = np.zeros((2, 2), dtype=complex)  # cut component, inverse powers 3 and 4
    for beta, weight in zip(betas, weights):
        s = 4/(1-beta**2)
        jacobian = 8*beta/(1-beta**2)**2
        nu = s+transfer/2
        cuts = two_diagonal_cuts(s, transfer, inner_order)
        result[:, 0] += weight*cuts*jacobian/nu**3/np.pi
        result[:, 1] += weight*cuts*jacobian/nu**4/np.pi
    return result


coarse = moments(0.0, 30, 32)
fine = moments(0.0, 48, 48)
assert np.max(np.abs(fine.imag)) < 2e-12
values = fine.real
g2 = values[0, 0]+values[1, 0]
g3 = values[0, 1]-values[1, 1]
alpha = 1/(4*np.pi)
expected_g2 = 11*alpha**2/45
expected_g3 = 4*alpha**2/315
relative_errors = [abs(g2/expected_g2-1), abs(g3/expected_g3-1)]
assert max(relative_errors) < 2e-6

nonforward_transfer = -0.25
nonforward_coarse = moments(nonforward_transfer, 22, 24)
nonforward_fine = moments(nonforward_transfer, 36, 38)
nf_values = nonforward_fine.real
nf_a2 = nf_values[0, 0]+nf_values[1, 0]
nf_a3 = nf_values[0, 1]-nf_values[1, 1]
nf_expected_a2 = expected_g2-1.5*nonforward_transfer*expected_g3
nf_expected_a3 = expected_g3
nf_relative_errors = [abs(nf_a2/nf_expected_a2-1), abs(nf_a3/nf_expected_a3-1)]
# Deliberate failure gate: at nonzero transfer, D12 and higher powers feed
# lower powers of nu after s=nu-T/2.  A fixed inverse moment is therefore not
# a projector onto the D10 coefficient.  The mismatch must remain visible.
assert nf_relative_errors[1] > 0.1

# A second transfer resolves the first triangular D12 coefficient.  If
# Phi1_D12=g41*s^4+g42*s^2*(s^2+t^2+u^2), then
# [nu^3]Phi1=g3-2*T*(g41+g42)+O(T^2).
near_transfer = -0.125
near_coarse = moments(near_transfer, 18, 20)
near_fine = moments(near_transfer, 30, 32)
near_values = near_fine.real
near_a3 = near_values[0, 1]-near_values[1, 1]
g4sum_at_quarter = (nf_a3-g3)/(-2*nonforward_transfer)
g4sum_at_eighth = (near_a3-g3)/(-2*near_transfer)
g4sum_richardson = 2*g4sum_at_eighth-g4sum_at_quarter
tiny_transfer = -0.0625
tiny_coarse = moments(tiny_transfer, 18, 20)
tiny_fine = moments(tiny_transfer, 30, 32)
tiny_values = tiny_fine.real
tiny_a3 = tiny_values[0, 1]-tiny_values[1, 1]
g4sum_at_sixteenth = (tiny_a3-g3)/(-2*tiny_transfer)
g4sum_richardson_fine = 2*g4sum_at_sixteenth-g4sum_at_eighth

payload = {
    "schema": "marici.qed-phi1-crossed-cut.v1",
    "source_convention": "source t=(p2+p3)^2 and u=(p1+p3)^2; source u is the physical transfer used by the cut checker",
    "crossing": "at fixed physical transfer, the left cut is M--++ under s<->t_source, hence M+--+ and physical C[+-,+-]",
    "moments": "J_n^h=(1/pi) integral_4^infinity C[h,h](s,0)/s^(n+1) ds",
    "assembly": {"g2": "J_2^(++)+J_2^(+-)", "g3": "J_3^(++)-J_3^(+-)"},
    "quadrature": {"coarse": [30, 32], "fine": [48, 48], "max_difference": float(np.max(np.abs(fine-coarse)))},
    "component_moments": {
        "J2_pp": float(values[0, 0]), "J2_pm": float(values[1, 0]),
        "J3_pp": float(values[0, 1]), "J3_pm": float(values[1, 1]),
    },
    "reconstruction": {"g2": float(g2), "g3": float(g3)},
    "expected": {"g2": float(expected_g2), "g3": float(expected_g3)},
    "relative_errors": {"g2": float(relative_errors[0]), "g3": float(relative_errors[1])},
    "nonforward_gate": {
        "transfer": nonforward_transfer,
        "coarse": [22, 24], "fine": [36, 38],
        "max_difference": float(np.max(np.abs(nonforward_fine-nonforward_coarse))),
        "reconstructed_nu2": float(nf_a2), "naive_d10_nu2": float(nf_expected_a2),
        "reconstructed_nu3": float(nf_a3), "naive_d10_nu3": float(nf_expected_a3),
        "relative_errors": {"nu2": float(nf_relative_errors[0]), "nu3": float(nf_relative_errors[1])},
        "verdict": "The nonzero-transfer inverse moments contain D12-and-higher contamination and are not D10 projectors.",
    },
    "triangular_d12_extraction": {
        "symbolic_law": "[nu^3]Phi1=g3-2*T*(g41+g42)+O(T^2)",
        "second_transfer": near_transfer,
        "second_transfer_coarse": [18, 20], "second_transfer_fine": [30, 32],
        "second_transfer_max_difference": float(np.max(np.abs(near_fine-near_coarse))),
        "nu3_at_second_transfer": float(near_a3),
        "g41_plus_g42_estimate_at_T_minus_1_over_4": float(g4sum_at_quarter),
        "g41_plus_g42_estimate_at_T_minus_1_over_8": float(g4sum_at_eighth),
        "linear_richardson_T_to_zero": float(g4sum_richardson),
        "third_transfer": tiny_transfer,
        "third_transfer_coarse": [18, 20], "third_transfer_fine": [30, 32],
        "third_transfer_max_difference": float(np.max(np.abs(tiny_fine-tiny_coarse))),
        "nu3_at_third_transfer": float(tiny_a3),
        "g41_plus_g42_estimate_at_T_minus_1_over_16": float(g4sum_at_sixteenth),
        "nested_linear_richardson_T_to_zero": float(g4sum_richardson_fine),
        "nested_richardson_over_g2": float(g4sum_richardson_fine/g2),
        "candidate_rational_ratio": "1/70 (comparison only; not used by the reconstruction)",
        "candidate_relative_residual": float(abs((g4sum_richardson_fine/g2)/(1/70)-1)),
        "strength": "numerical discovery estimate; higher-transfer grades are removed only to first Richardson order",
    },
    "conclusion": "The vector-valued crossing completion dispersively reproduces both Phi1 coefficients at the forward point. At nonzero transfer the same moments remain well-defined, but a naive D10 identification fails because the shifted nu grading mixes higher EFT orders. A scalar crossing parity would still miss the second helicity channel.",
}
canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
payload["content_sha256"] = hashlib.sha256(canonical.encode()).hexdigest().upper()
(HERE / "results" / "qed-phi1-crossed-cut.json").write_text(
    json.dumps(payload, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps({"phi1_crossed_cut": True, "sha256": payload["content_sha256"]}))
