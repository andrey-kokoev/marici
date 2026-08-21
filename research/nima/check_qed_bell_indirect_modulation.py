"""Indirect continuous-azimuth estimator of the QED Bell helicity ratio."""

import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_exact_qed_bell_onset import amplitudes
from check_qed_bell_experimental_gate import compton_visibility


mp.mp.dps = 40

if __name__ == "__main__":
    y = mp.mpf("0.42015760875460728129837661981582642")
    epsilon = mp.sqrt(y) / 2
    a, b, c = amplitudes(y)
    norm = abs(a) ** 2 + abs(b) ** 2 + 2 * abs(c) ** 2
    coherence = 2 * abs(a * b) / norm
    mixed_helicity_weight = 2 * abs(c) ** 2 / norm
    ratio = abs(b / a)

    analyzer_theta = mp.findroot(
        lambda t: mp.diff(lambda z: compton_visibility(epsilon, z), t), 1.5
    )
    mu = compton_visibility(epsilon, analyzer_theta)
    modulation = mu**2 * coherence

    # If p(phi)=(1+V cos(2 phi))/(2 pi), Vhat=2 mean(cos(2 phi)) and
    # Var(Vhat)=(2-V^2)/N.
    events_five_sigma_from_zero = 25 * (2 - modulation**2) / modulation**2
    events_one_percent = (2 - modulation**2) / (modulation**2 * mp.mpf("0.01") ** 2)

    angular_weight = lambda theta: (3 + mp.cos(theta) ** 2) ** 2 * mp.sin(theta)
    total_weight = mp.quad(angular_weight, [0, mp.pi])
    half_width = mp.radians(5)
    bin_fraction = mp.quad(angular_weight, [mp.pi / 2 - half_width, mp.pi / 2 + half_width])
    bin_fraction /= total_weight

    alpha = 1 / mp.mpf("137.035999177")
    electron_compton_wavelength_m = mp.mpf("3.8615926796e-13")
    sigma_total = (
        mp.mpf(973) / (10125 * mp.pi)
        * alpha**4 * electron_compton_wavelength_m**2 * epsilon**6
    )
    sigma_bin_cm2 = sigma_total * bin_fraction * mp.mpf("1e4")
    rate_scenarios = {}
    for exponent in (30, 32, 34):
        luminosity = mp.mpf(10) ** exponent
        rate = luminosity * sigma_bin_cm2
        rate_scenarios[f"1e{exponent}_cm_minus_2_s_minus_1"] = {
            "ideal_events_per_second": str(rate),
            "days_for_five_sigma_nonzero_modulation": str(
                events_five_sigma_from_zero / rate / (24 * 3600)
            ),
            "years_for_one_percent_modulation": str(
                events_one_percent / rate / (mp.mpf("365.25") * 24 * 3600)
            ),
        }

    payload = {
        "schema": "marici.qed-bell-indirect-modulation.v1",
        "observable": "continuous double-Compton azimuthal modulation p(phi)=(1+V cos(2 phi))/(2 pi)",
        "state_relation": "V=mu_A mu_B C, C=2|Phi1 Phi2|/(|Phi1|^2+|Phi2|^2+2|Phi5|^2)",
        "kinematics": {
            "s_over_me2": str(y),
            "photon_energy_keV": str(epsilon * mp.mpf("510.99895")),
            "gamma_gamma_bin": "85 degrees <= theta <= 95 degrees",
            "leading_angular_cross_section_fraction": str(bin_fraction),
        },
        "helicity_data": {
            "abs_Phi2_over_Phi1": str(ratio),
            "coherence_C": str(coherence),
            "mixed_helicity_weight": str(mixed_helicity_weight),
        },
        "polarimeter": {
            "optimal_compton_angle_degrees": str(analyzer_theta * 180 / mp.pi),
            "single_arm_visibility": str(mu),
            "observed_modulation_V": str(modulation),
        },
        "statistics": {
            "events_for_five_sigma_rejection_of_zero_modulation": str(events_five_sigma_from_zero),
            "events_for_one_percent_relative_modulation_precision": str(events_one_percent),
            "variance_formula": "Var(Vhat)=(2-V^2)/N",
        },
        "rate_gate": {
            "accepted_cross_section_estimate_cm2": str(sigma_bin_cm2),
            "ideal_luminosity_scenarios": rate_scenarios,
        },
        "verdict": "The continuous modulation estimates the same Phi2/Phi1 coherence with about 110 events for a five-sigma nonzero signal, versus about two million events for analyzer-diluted CHSH. It is a model-dependent amplitude witness, not a device-independent Bell test.",
        "scope": "Leading Euler-Heisenberg rate, ideal detector efficiency, source support for the selected ++ channel, and no background dilution.",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["content_sha256"] = hashlib.sha256(canonical.encode()).hexdigest().upper()
    out = Path(__file__).parent / "results" / "qed-bell-indirect-modulation.json"
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "modulation": str(modulation),
        "events_5sigma": str(events_five_sigma_from_zero),
        "events_1pct": str(events_one_percent),
        "bin_fraction": str(bin_fraction),
    }))
