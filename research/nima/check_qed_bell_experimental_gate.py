"""Finite experimental gate for the sub-threshold QED Bell signal."""

import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_exact_qed_bell_onset import bell


mp.mp.dps = 40


def compton_visibility(epsilon, theta):
    ratio = 1 / (1 + epsilon * (1 - mp.cos(theta)))
    return mp.sin(theta) ** 2 / (1 / ratio + ratio - mp.sin(theta) ** 2)


if __name__ == "__main__":
    y = mp.mpf("0.42015760875460728129837661981582642")
    epsilon = mp.sqrt(y) / 2
    theta_analyzer = mp.findroot(lambda t: mp.diff(lambda z: compton_visibility(epsilon, z), t), 1.5)
    visibility = compton_visibility(epsilon, theta_analyzer)
    two_arm_visibility = visibility**2
    required_ideal_chsh = 2 / two_arm_visibility
    x_max = mp.findroot(lambda x: two_arm_visibility * bell(y, x) - 2, (mp.mpf("0.02"), mp.mpf("0.04")))
    theta_scattering_max = mp.acos(1 - 2 * x_max)

    # Euler-Heisenberg angular weight and total-cross-section estimate.
    weight = lambda x: (3 + (1 - 2 * x) ** 2) ** 2
    x_min = mp.mpf("0.0001")
    intervals = 100
    xs = [x_min + i * (x_max - x_min) / intervals for i in range(intervals + 1)]
    coeffs = [1] + [4 if i % 2 else 2 for i in range(1, intervals)] + [1]
    ideal_average = sum(c * weight(x) * bell(y, x) for c, x in zip(coeffs, xs))
    ideal_average /= sum(c * weight(x) for c, x in zip(coeffs, xs))
    observed_average = two_arm_visibility * ideal_average
    observed_excess = observed_average - 2

    alpha = 1 / mp.mpf("137.035999177")
    electron_compton_wavelength_m = mp.mpf("3.8615926796e-13")
    sigma_total = (
        mp.mpf(973) / (10125 * mp.pi)
        * alpha**4 * electron_compton_wavelength_m**2 * epsilon**6
    )
    angular_integrand = lambda theta: (3 + mp.cos(theta) ** 2) ** 2 * mp.sin(theta)
    single_cone_fraction = mp.quad(angular_integrand, [0, theta_scattering_max])
    single_cone_fraction /= mp.quad(angular_integrand, [0, mp.pi])
    sigma_accepted = sigma_total * single_cone_fraction

    # Four balanced CHSH settings give the conservative bound sigma_S <= 4/sqrt(N).
    accepted_events_for_five_sigma = (20 / observed_excess) ** 2
    integrated_luminosity_m2 = accepted_events_for_five_sigma / sigma_accepted
    residual_visibility_required = 2 / observed_average
    equal_beam_circular_polarization_required = mp.sqrt(residual_visibility_required)
    luminosity_scenarios = {}
    sigma_accepted_cm2 = sigma_accepted * mp.mpf("1e4")
    for exponent in (30, 32, 34):
        luminosity = mp.mpf(10) ** exponent
        rate = luminosity * sigma_accepted_cm2
        luminosity_scenarios[f"1e{exponent}_cm_minus_2_s_minus_1"] = {
            "ideal_accepted_rate_per_second": str(rate),
            "ideal_live_time_years_for_five_sigma": str(
                accepted_events_for_five_sigma / rate / (mp.mpf("365.25") * 24 * 3600)
            ),
        }

    alpha_over_pi = (1 / mp.mpf("137.035999177")) / mp.pi
    dy_two_loop_benchmark = mp.mpf("31.31556706053538919121584508960121288075") * alpha_over_pi
    energy_from_y = lambda value: mp.sqrt(value) * mp.mpf("510.99895") / 2
    payload = {
        "schema": "marici.qed-bell-experimental-gate.v1",
        "energy": {
            "s_over_me2": str(y),
            "photon_energy_over_me": str(epsilon),
            "photon_energy_keV": str(epsilon * mp.mpf("510.99895")),
        },
        "single_compton_polarimeter": {
            "optimal_scatter_angle_degrees": str(theta_analyzer * 180 / mp.pi),
            "single_arm_visibility": str(visibility),
            "two_arm_visibility": str(two_arm_visibility),
            "required_ideal_chsh": str(required_ideal_chsh),
            "linear_analyzer_axes_degrees": {
                "Alice_A1": "90",
                "Alice_A2": "45",
                "Bob_B1": "67.5",
                "Bob_B2": "112.5",
            },
            "implementation": "For each axis alpha, bin Compton azimuths into calibrated parallel/perpendicular outcome sectors realizing E_pm=(1 pm mu O(alpha))/2.",
        },
        "polarization_preparation": {
            "incoming_state": "two counter-propagating photons, each prepared in positive circular helicity relative to its own momentum (++ source channel)",
            "minimum_residual_state_visibility_after_compton_dilution": str(residual_visibility_required),
            "minimum_equal_per_beam_circular_polarization_under_product_visibility_model": str(equal_beam_circular_polarization_required),
            "maximum_total_additional_visibility_loss": str(1 - residual_visibility_required),
        },
        "accepted_gamma_gamma_cone": {
            "x_min_for_numerics": str(x_min),
            "x_max": str(x_max),
            "theta_max_degrees": str(theta_scattering_max * 180 / mp.pi),
            "single_cone_cross_section_fraction": str(single_cone_fraction),
            "ideal_weighted_chsh": str(ideal_average),
            "observed_weighted_chsh": str(observed_average),
            "observed_excess": str(observed_excess),
        },
        "rate_gate": {
            "euler_heisenberg_total_cross_section_estimate_m2": str(sigma_total),
            "accepted_cross_section_estimate_m2": str(sigma_accepted),
            "accepted_events_for_conservative_five_sigma": str(accepted_events_for_five_sigma),
            "required_integrated_luminosity_m_minus_2": str(integrated_luminosity_m2),
            "required_integrated_luminosity_cm_minus_2": str(integrated_luminosity_m2 / mp.mpf("1e4")),
            "ideal_luminosity_scenarios": luminosity_scenarios,
        },
        "theory_uncertainty": {
            "status": "explicit two-loop helicity amplitudes not inserted",
            "benchmark_differential_helicity_correction": "alpha/pi",
            "benchmark_abs_shift_in_y": str(dy_two_loop_benchmark),
            "benchmark_photon_energy_interval_keV": [
                str(energy_from_y(y - dy_two_loop_benchmark)),
                str(energy_from_y(y + dy_two_loop_benchmark)),
            ],
            "interpretation": "sensitivity benchmark, not a statistical confidence interval",
        },
        "verdict": "A typed single-Compton CHSH protocol exists only in a forward gamma-gamma cone and has a marginal observed excess. Its required accepted statistics and photon-photon luminosity make it a conceptual protocol, not a presently credible experiment.",
        "scope": "Uses the leading Euler-Heisenberg rate and idealized Compton visibility; detector efficiency, backgrounds, beam phase space, and loophole closure only worsen feasibility.",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["content_sha256"] = hashlib.sha256(canonical.encode()).hexdigest().upper()
    out = Path(__file__).parent / "results" / "qed-bell-experimental-gate.json"
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "photon_keV": str(payload["energy"]["photon_energy_keV"]),
        "theta_max_deg": str(payload["accepted_gamma_gamma_cone"]["theta_max_degrees"]),
        "observed_chsh": str(observed_average),
        "events_5sigma": str(accepted_events_for_five_sigma),
    }))
