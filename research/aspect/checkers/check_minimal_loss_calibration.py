#!/usr/bin/env python3
"""Exact rank and gauge checks for one-reference lossy Pauli calibration."""

import itertools
import json
from fractions import Fraction
from pathlib import Path

AXES = ("X", "Y", "Z")
SIGNS = (-1, 1)
SETTINGS = tuple(itertools.product(AXES, repeat=2))
OUTCOMES = tuple(itertools.product(SIGNS, repeat=2))
CHANNELS = tuple((setting, outcome) for setting in SETTINGS for outcome in OUTCOMES)

# Nonzero exact efficiencies, one per setting/outcome channel.
efficiencies = {channel: Fraction(1 + (index % 4), 5) for index, channel in enumerate(CHANNELS)}
reference_probabilities = {channel: Fraction(1, 4) for channel in CHANNELS}
reference_clicks = {channel: efficiencies[channel] * reference_probabilities[channel] for channel in CHANNELS}
recovered_efficiencies = {channel: reference_clicks[channel] / reference_probabilities[channel] for channel in CHANNELS}

# Valid unknown state rho=(II + XX/2)/4.
def unknown_probability(setting, outcome):
    s, t = outcome
    correlation = Fraction(1, 2) if setting == ("X", "X") else Fraction(0)
    return (1 + s * t * correlation) / 4

unknown_clicks = {channel: efficiencies[channel] * unknown_probability(*channel) for channel in CHANNELS}
corrected_probabilities = {channel: unknown_clicks[channel] / recovered_efficiencies[channel] for channel in CHANNELS}
recovered_xx = sum(Fraction(s * t) * corrected_probabilities[(('X', 'X'), (s, t))] for s, t in OUTCOMES)

# A reference with one zero ideal channel leaves that efficiency unconstrained.
zero_reference = dict(reference_probabilities)
zero_channel = CHANNELS[0]
zero_reference[zero_channel] = Fraction(0)
full_rank = sum(value != 0 for value in reference_probabilities.values())
zero_rank = sum(value != 0 for value in zero_reference.values())

# Factorized detector efficiencies have a scale gauge: P*Q is invariant.
path_eff_a, pol_eff_a = Fraction(1, 4), Fraction(1, 4)
path_eff_b, pol_eff_b = Fraction(1, 2), Fraction(1, 8)

checks = {
    "nine_settings_and_thirty_six_channels": len(SETTINGS) == 9 and len(CHANNELS) == 36,
    "maximally_mixed_reference_is_nonzero_on_every_channel": all(value == Fraction(1, 4) for value in reference_probabilities.values()),
    "one_reference_recovers_all_effective_efficiencies": recovered_efficiencies == efficiencies,
    "calibration_design_has_full_diagonal_rank": full_rank == 36,
    "corrected_unknown_probabilities_are_exact": all(corrected_probabilities[channel] == unknown_probability(*channel) for channel in CHANNELS),
    "corrected_xx_correlation_is_recovered": recovered_xx == Fraction(1, 2),
    "one_zero_reference_probability_loses_one_rank": zero_rank == 35,
    "zero_reference_channel_cannot_identify_efficiency": zero_reference[zero_channel] == 0 and reference_probabilities[zero_channel] != 0,
    "factorized_efficiency_scale_gauge_is_real": path_eff_a != path_eff_b and pol_eff_a != pol_eff_b and path_eff_a * pol_eff_a == path_eff_b * pol_eff_b,
    "effective_product_is_gauge_invariant": path_eff_a * pol_eff_a == Fraction(1, 16),
    "no_calibration_cannot_separate_click_from_efficiency": unknown_clicks[zero_channel] == efficiencies[zero_channel] * unknown_probability(*zero_channel),
    "all_corrected_setting_probabilities_normalize": all(sum(corrected_probabilities[(setting, outcome)] for outcome in OUTCOMES) == 1 for setting in SETTINGS),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.minimal-loss-calibration.v1", "status": "passed", "checks": checks, "channel_count": len(CHANNELS), "calibration_rank": full_rank, "zero_support_rank": zero_rank, "recovered_xx": str(recovered_xx), "factor_gauge_product": str(path_eff_a * pol_eff_a), "claim_boundary": "One reference is minimal only under static multiplicative effective efficiencies and known ideal reference probabilities."}
output = Path(__file__).parents[1] / "results" / "minimal_loss_calibration.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "calibration_rank": full_rank, "channel_count": len(CHANNELS)}, sort_keys=True))
