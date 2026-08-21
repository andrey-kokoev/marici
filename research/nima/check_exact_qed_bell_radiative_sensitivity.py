"""Local radiative condition number of the exact one-loop QED Bell crossing."""

import hashlib
import json
from pathlib import Path

import mpmath as mp

from check_exact_qed_bell_onset import amplitudes, bell


mp.mp.dps = 55

if __name__ == "__main__":
    y = mp.mpf("0.420157608754607281298376619815826416015625")
    a, b, c = amplitudes(y)
    value = bell(y)
    slope = mp.diff(bell, y)
    denominator = abs(a) ** 2 + abs(b) ** 2 + 2 * abs(c) ** 2
    sensitivities = {
        "delta_log_abs_Phi1": value * (1 - 2 * abs(a) ** 2 / denominator),
        "delta_log_abs_Phi2": value * (1 - 2 * abs(b) ** 2 / denominator),
        "delta_log_abs_Phi5": -4 * value * abs(c) ** 2 / denominator,
    }
    common_mode = sum(sensitivities.values())
    differential = (sensitivities["delta_log_abs_Phi2"] - sensitivities["delta_log_abs_Phi1"]) / 2
    dy_per_differential_log_ratio = -differential / slope
    alpha_over_pi = (mp.mpf(1) / mp.mpf("137.035999177")) / mp.pi
    one_unit_shift = abs(dy_per_differential_log_ratio) * alpha_over_pi
    required_to_y1 = (mp.mpf(1) - y) / abs(dy_per_differential_log_ratio)
    required_to_pair = (mp.mpf(4) - y) / abs(dy_per_differential_log_ratio)
    payload = {
        "schema": "marici.exact-qed-bell-radiative-sensitivity.v1",
        "onset_y": str(y),
        "bell_value": str(value),
        "d_bell_d_y": str(slope),
        "helicity_amplitudes": {"Phi1": str(a), "Phi2": str(b), "Phi5": str(c)},
        "logarithmic_sensitivities": {key: str(val) for key, val in sensitivities.items()},
        "common_mode_sensitivity": str(common_mode),
        "d_bell_d_differential_log_ratio": str(differential),
        "d_y_onset_d_differential_log_ratio": str(dy_per_differential_log_ratio),
        "alpha_over_pi": str(alpha_over_pi),
        "onset_shift_for_one_alpha_over_pi_differential_unit": str(one_unit_shift),
        "differential_log_ratio_needed_to_move_onset_to_y_1": str(required_to_y1),
        "differential_log_ratio_needed_to_move_onset_to_pair_threshold_y_4": str(required_to_pair),
        "verdict": "The Bell readout annihilates common helicity rescaling and is controlled almost entirely by the Phi2/Phi1 relative correction. An alpha/pi differential correction moves y by about 0.073; moving the crossing to pair threshold requires an implausibly large 0.114 relative logarithmic correction.",
        "scope": "First-order local sensitivity, not an explicit two-loop QED calculation.",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["content_sha256"] = hashlib.sha256(canonical.encode()).hexdigest().upper()
    out = Path(__file__).parent / "results" / "exact-qed-bell-radiative-sensitivity.json"
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "slope": str(slope),
        "common_mode": str(common_mode),
        "dy_per_alpha_over_pi": str(one_unit_shift),
        "relative_shift_to_pair_threshold": str(required_to_pair),
    }))
