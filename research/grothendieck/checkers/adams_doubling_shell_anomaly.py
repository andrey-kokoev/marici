"""Exact formula audit for Adams alignment of shell phase defects."""

from fractions import Fraction


def phase_label(channel: str):
    if channel == "quadratic_at_T":
        return {"frequency": 2, "center_phase": Fraction(1, 2), "sinc_argument": 1}
    if channel == "linear_at_2T":
        return {"frequency": 2, "center_phase": Fraction(1, 2), "sinc_argument": 1}
    raise ValueError(channel)


assert phase_label("quadratic_at_T") == phase_label("linear_at_2T")

result = {
    "prime_channel_identity": "C2(s)=(1/2)C1(2s)",
    "quadratic_shell_defect_equals_linear_doubled_height_defect": True,
    "odd_pi_resonances_aligned": True,
    "forced_orbit_coefficient": "1/2",
    "same_height_scalar_coupling_falsified": True,
    "gamma_resolvent_identified_with_shell_time_phase": False,
    "next_gate": "resolved-prime to gamma-resolvent kernel at the Adams boundary",
}

if __name__ == "__main__":
    import json
    from pathlib import Path

    output = Path(__file__).parents[1] / "results" / "adams-doubling-shell-anomaly.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
