"""Optimistic inverse-Compton source bound for the indirect QED helicity witness."""

import hashlib
import json
from pathlib import Path

import mpmath as mp


mp.mp.dps = 40

if __name__ == "__main__":
    repetition_hz = mp.mpf("1e8")
    spot_sigma_m = mp.mpf("3.2e-6")
    accepted_cross_section_cm2 = mp.mpf("1.051652929473551084617274266854357711314e-35")
    event_targets = {
        "five_sigma_nonzero_modulation": mp.mpf("109.5663050220895890096402038092457605904"),
        "one_percent_modulation": mp.mpf("43826.52200883583560385608152369830423614"),
    }

    def scenario(flux_per_second):
        photons_per_pulse = flux_per_second / repetition_hz
        luminosity_m2_s = repetition_hz * photons_per_pulse**2 / (4 * mp.pi * spot_sigma_m**2)
        luminosity_cm2_s = luminosity_m2_s / mp.mpf("1e4")
        rate = luminosity_cm2_s * accepted_cross_section_cm2
        return {
            "flux_per_beam_per_second": str(flux_per_second),
            "photons_per_pulse": str(photons_per_pulse),
            "ideal_gamma_gamma_luminosity_cm_minus_2_s_minus_1": str(luminosity_cm2_s),
            "ideal_accepted_rate_per_second": str(rate),
            "live_time_years": {
                key: str(target / rate / (mp.mpf("365.25") * 24 * 3600))
                for key, target in event_targets.items()
            },
        }

    payload = {
        "schema": "marici.qed-bell-source-luminosity-bound.v1",
        "source_proxy": {
            "paper": "Deitrick et al., High-brilliance, high-flux compact inverse Compton light source, arXiv:1803.10326",
            "reported_energy_keV": "12",
            "reported_repetition_hz": str(repetition_hz),
            "reported_interaction_spot_m": str(spot_sigma_m),
            "warning": "Applying the reported source flux and interaction spot to two refocused 165-keV gamma beams is an optimistic extrapolation, not a demonstrated facility.",
        },
        "total_flux_proxy": scenario(mp.mpf("1.4e14")),
        "point_one_percent_bandwidth_proxy": scenario(mp.mpf("2.1e11")),
        "assumptions": [
            "two identical synchronized beams",
            "round Gaussian gamma spots equal to the reported laser interaction spot",
            "perfect transport, refocusing, polarization, overlap, detection, and duty cycle",
            "no penalty for raising the photon energy from 12 to 165 keV",
        ],
        "verdict": "Even this deliberately optimistic total-flux proxy needs about 2.2e3 years for a five-sigma indirect modulation detection; the 0.1-percent-bandwidth proxy needs about 9.7e8 years. Present inverse-Compton source scaling does not rescue the experiment.",
        "scope": "Source-side upper-bound proxy, not an engineering design or exclusion theorem for future coherent gamma sources.",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["content_sha256"] = hashlib.sha256(canonical.encode()).hexdigest().upper()
    out = Path(__file__).parent / "results" / "qed-bell-source-luminosity.json"
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "optimistic_luminosity_cm2_s": payload["total_flux_proxy"]["ideal_gamma_gamma_luminosity_cm_minus_2_s_minus_1"],
        "optimistic_five_sigma_years": payload["total_flux_proxy"]["live_time_years"]["five_sigma_nonzero_modulation"],
        "narrow_band_five_sigma_years": payload["point_one_percent_bandwidth_proxy"]["live_time_years"]["five_sigma_nonzero_modulation"],
    }))
