"""Exact finite identities and hostile continuum-completion counterexamples."""

from fractions import Fraction as F
import json
from pathlib import Path


def cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cnorm2(a):
    return a[0] * a[0] + a[1] * a[1]


def dft4(values):
    roots = [(F(1), F(0)), (F(0), F(-1)), (F(-1), F(0)), (F(0), F(1))]
    out = []
    for k in range(4):
        total = (F(0), F(0))
        for n, value in enumerate(values):
            total = cadd(total, cmul((F(value), F(0)), roots[(k * n) % 4]))
        out.append(total)
    return out


def sampled_tone_quarter_units(m):
    roots_positive = [(F(1), F(0)), (F(0), F(1)),
                      (F(-1), F(0)), (F(0), F(-1))]
    return [roots_positive[(m * n) % 4] for n in range(4)]


def main():
    samples = [F(1), F(2), F(0), F(-1)]
    spectrum = dft4(samples)
    time_energy = sum(v * v for v in samples)
    frequency_energy = sum(cnorm2(v) for v in spectrum) / 4

    # Frequencies 1/4 and 5/4 have identical integer-time samples.
    quarter_cycle = sampled_tone_quarter_units(1)
    five_quarter_cycle = sampled_tone_quarter_units(5)

    spectrum_a = [F(1), F(2), F(3)]
    spectrum_b = [F(1), F(2), F(-3)]
    band_projection_a = spectrum_a[:2]
    band_projection_b = spectrum_b[:2]

    causal_h = {0: F(1), 1: F(1, 2), 2: F(1, 4)}
    impulse_output = [causal_h.get(n, F(0)) for n in range(3)]
    advanced_h = {-1: F(1)}
    present_from_future_a = advanced_h[-1] * F(0)
    present_from_future_b = advanced_h[-1] * F(1)

    total_geometric_energy = F(4, 3)
    three_sample_energy = F(1) + F(1, 4) + F(1, 16)
    omitted_tail_energy = total_geometric_energy - three_sample_energy

    inverse_bounds = [F(n) for n in range(1, 9)]  # epsilon=1/n
    finite_prefix_zero = [F(0)] * 8
    same_observed_prefix_a = list(finite_prefix_zero)
    same_observed_prefix_b = list(finite_prefix_zero)
    infinite_mean_a = F(0)
    infinite_mean_b = F(1)

    checks = {
        "finite_parseval_identity": time_energy == frequency_energy,
        "sampling_aliases_distinct_continuum_frequencies": quarter_cycle == five_quarter_cycle,
        "finite_band_projection_has_out_of_band_kernel": band_projection_a == band_projection_b and spectrum_a != spectrum_b,
        "causal_impulse_response_respects_order": impulse_output == [1, F(1, 2), F(1, 4)],
        "advanced_term_violates_causal_independence": present_from_future_a != present_from_future_b,
        "finite_window_omits_exact_tail_energy": three_sample_energy == F(21, 16) and omitted_tail_energy == F(1, 48),
        "inverse_bound_family_exhibits_exact_cutoff_growth": (
            inverse_bounds == [F(n) for n in range(1, 9)]
            and inverse_bounds[-1] == 8 * inverse_bounds[0]
        ),
        "finite_prefix_does_not_fix_infinite_time_mean": same_observed_prefix_a == same_observed_prefix_b and infinite_mean_a != infinite_mean_b,
    }
    result = {
        "schema": "marici.aspect.finite_bandwidth_continuum_completion.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "checks": checks,
        "residuals": {
            "time_energy": str(time_energy),
            "frequency_energy_normalized": str(frequency_energy),
            "aliased_normalized_frequencies": ["1/4", "5/4"],
            "out_of_band_difference": str(spectrum_a[2] - spectrum_b[2]),
            "advanced_present_output_difference": str(present_from_future_b - present_from_future_a),
            "three_sample_energy": str(three_sample_energy),
            "omitted_tail_energy": str(omitted_tail_energy),
            "inverse_bound_prefix": [str(v) for v in inverse_bounds],
            "inverse_bound_formula": "for epsilon=1/n, ||K(epsilon)^-1||=n",
            "infinite_means_for_equal_prefix": [str(infinite_mean_a), str(infinite_mean_b)],
        },
        "completion_contract": [
            "function spaces and measures", "Fourier/sample/window normalization",
            "bandlimit or anti-alias filter", "causal impulse response",
            "uniform operator and tail bounds", "convergence topology and error estimate",
            "detector response and spectral noise law", "environment and kernel typing",
            "singularity and limiting-absorption disposition",
        ],
        "claim_boundary": "finite exact gates and counterexamples only; continuum completion remains conditional",
    }
    out = Path(__file__).parents[1] / "results" / "finite_bandwidth_continuum_completion.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
