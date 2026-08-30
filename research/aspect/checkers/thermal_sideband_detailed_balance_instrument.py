"""Exact two-rate thermal sideband and linewidth identifiability audit."""

from fractions import Fraction as F
import json
from pathlib import Path


def observables(g_down, g_up):
    damping = g_down - g_up
    noise_sum = g_down + g_up
    occupation = g_up / damping
    sideband_ratio = g_up / g_down
    return damping, noise_sum, occupation, sideband_ratio


def recover(damping, noise_sum):
    return ((noise_sum + damping) / 2, (noise_sum - damping) / 2)


def main():
    physical = (F(2), F(1))
    hostile = (F(3), F(2))
    p = observables(*physical)
    h = observables(*hostile)
    recovered = recover(p[0], p[1])

    checks = {
        "physical_rates_are_positive_and_stable": physical[0] > physical[1] >= 0,
        "steady_occupation_is_exactly_one": p[2] == 1,
        "detailed_balance_sideband_ratio_is_one_half": p[3] == F(1, 2),
        "linewidth_is_rate_difference": p[0] == 1,
        "symmetrized_noise_weight_is_rate_sum": p[1] == 3,
        "hostile_preserves_linewidth": h[0] == p[0],
        "hostile_changes_noise_and_temperature": h[1] != p[1] and h[2] != p[2] and h[3] != p[3],
        "linewidth_alone_is_not_faithful": physical != hostile and p[0] == h[0],
        "joint_linewidth_and_noise_recover_both_rates": recovered == physical,
        "two_resolved_sidebands_recover_rate_ratio": p[3] * physical[0] == physical[1],
    }
    result = {
        "schema": "marici.aspect.thermal_sideband_detailed_balance_instrument.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "strength": "finite Markov detailed-balance identification theorem",
        "checks": checks,
        "physical": {
            "Gamma_down": str(physical[0]), "Gamma_up": str(physical[1]),
            "damping": str(p[0]), "noise_sum": str(p[1]),
            "occupation": str(p[2]), "sideband_ratio": str(p[3]),
        },
        "linewidth_preserving_hostile": {
            "Gamma_down": str(hostile[0]), "Gamma_up": str(hostile[1]),
            "damping": str(h[0]), "noise_sum": str(h[1]),
            "occupation": str(h[2]), "sideband_ratio": str(h[3]),
        },
        "typed_boundary": {
            "source": "one stable oscillator with declared upward and downward Markov transition rates",
            "constructor": "linewidth from rate difference; sideband/noise record from individual rates",
            "detector": "calibrated two-sideband heterodyne counter plus linewidth fit",
            "hostile": "different positive rates preserve linewidth while changing noise and temperature",
            "completion": "frequency-dependent non-Markov KMS spectrum and microscopic material coupling remain open",
        },
    }
    out = Path(__file__).parents[1] / "results" / "thermal_sideband_detailed_balance_instrument.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass": raise SystemExit(1)


if __name__ == "__main__": main()
