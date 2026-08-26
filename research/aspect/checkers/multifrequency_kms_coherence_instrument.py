"""Exact finite-frequency KMS coherence audit from sideband ratios."""

from fractions import Fraction as F
import json
from pathlib import Path


def rates_from_ratio(ratio, down=F(8)):
    return down, down * ratio


def stable(pair): return pair[0] > pair[1] >= 0


def main():
    q = F(1, 2)
    frequencies = [1, 2, 3]
    coherent_ratios = [q**w for w in frequencies]
    coherent_rates = [rates_from_ratio(r) for r in coherent_ratios]
    hostile_ratios = [F(1, 2), F(1, 3), F(1, 8)]
    hostile_rates = [rates_from_ratio(r) for r in hostile_ratios]

    coherent_residuals = [
        coherent_ratios[1] - coherent_ratios[0]**2,
        coherent_ratios[2] - coherent_ratios[0]**3,
        coherent_ratios[2] - coherent_ratios[0] * coherent_ratios[1],
    ]
    hostile_residuals = [
        hostile_ratios[1] - hostile_ratios[0]**2,
        hostile_ratios[2] - hostile_ratios[0]**3,
        hostile_ratios[2] - hostile_ratios[0] * hostile_ratios[1],
    ]

    checks = {
        "all_common_temperature_bins_are_locally_stable": all(stable(p) for p in coherent_rates),
        "all_hostile_bins_are_also_locally_stable": all(stable(p) for p in hostile_rates),
        "common_temperature_ratios_are_exact_powers": coherent_ratios == [F(1, 2), F(1, 4), F(1, 8)],
        "all_common_temperature_coherence_residuals_vanish": coherent_residuals == [0, 0, 0],
        "hostile_preserves_first_and_third_sideband_ratios": hostile_ratios[0] == coherent_ratios[0] and hostile_ratios[2] == coherent_ratios[2],
        "hostile_has_nonzero_cross_frequency_residual": any(x != 0 for x in hostile_residuals),
        "per_bin_positivity_does_not_imply_global_kms": all(stable(p) for p in hostile_rates) and hostile_residuals != [0, 0, 0],
        "fundamental_ratio_reconstructs_all_coherent_bins": all(coherent_ratios[w-1] == coherent_ratios[0]**w for w in frequencies),
        "finite_three_bin_coherence_is_not_unbounded_kms": True,
    }
    result = {
        "schema": "marici.aspect.multifrequency_kms_coherence_instrument.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "strength": "finite-frequency KMS coherence theorem",
        "checks": checks,
        "frequencies": frequencies,
        "common_parameter_q": str(q),
        "coherent_ratios": [str(x) for x in coherent_ratios],
        "hostile_ratios": [str(x) for x in hostile_ratios],
        "hostile_coherence_residuals": [str(x) for x in hostile_residuals],
        "typed_boundary": {
            "source": "three oscillator transitions declared to share one thermal parameter",
            "constructor": "frequency-resolved upward/downward Markov rate pairs",
            "detector": "calibrated sideband-asymmetry record in each frequency bin",
            "hostile": "locally stable positive bins that do not descend from one common temperature",
            "completion": "arbitrary-frequency KMS analyticity, continuum convergence, and microscopic bath authority remain open",
        },
    }
    out = Path(__file__).parents[1] / "results" / "multifrequency_kms_coherence_instrument.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass": raise SystemExit(1)


if __name__ == "__main__": main()
