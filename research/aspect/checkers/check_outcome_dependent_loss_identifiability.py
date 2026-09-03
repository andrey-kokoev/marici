#!/usr/bin/env python3
"""Exact identifiability and bias checks for outcome-dependent detector loss."""

import json
from fractions import Fraction
from pathlib import Path


def records(m, eta_plus, eta_minus):
    p_plus = (1 + m) / 2
    p_minus = (1 - m) / 2
    c_plus = eta_plus * p_plus
    c_minus = eta_minus * p_minus
    return c_plus, c_minus, 1 - c_plus - c_minus


def recover_known(records_value, eta_plus, eta_minus):
    if eta_plus == 0 or eta_minus == 0:
        return None
    c_plus, c_minus, _ = records_value
    return c_plus / eta_plus - c_minus / eta_minus


A = (Fraction(0), Fraction(1, 2), Fraction(1, 2))
B = (Fraction(1, 2), Fraction(1, 3), Fraction(1))
records_a = records(*A)
records_b = records(*B)

biased_records = records(Fraction(0), Fraction(1), Fraction(1, 2))
conditional = (biased_records[0] - biased_records[1]) / (biased_records[0] + biased_records[1])

true_m = Fraction(-1, 3)
known_efficiencies = (Fraction(2, 3), Fraction(3, 4))
known_records = records(true_m, *known_efficiencies)
recovered_m = recover_known(known_records, *known_efficiencies)

balanced_efficiencies = (Fraction(2, 5), Fraction(4, 5))
balanced_records = records(Fraction(0), *balanced_efficiencies)
calibrated_from_balanced = (2 * balanced_records[0], 2 * balanced_records[1])

zero_efficiency_records = records(Fraction(1, 2), Fraction(0), Fraction(1))
checks = {
    "distinct_parameter_triples_declared": A != B,
    "distinct_triples_have_identical_records": records_a == records_b,
    "shared_record_is_exact_quarter_quarter_half": records_a == (Fraction(1, 4), Fraction(1, 4), Fraction(1, 2)),
    "no_click_adds_no_independent_equation": records_a[2] == 1 - records_a[0] - records_a[1],
    "conditional_renormalization_is_biased": conditional != 0,
    "conditional_bias_is_exact_one_third": conditional == Fraction(1, 3),
    "known_nonzero_efficiencies_recover_state": recovered_m == true_m,
    "balanced_reference_recovers_both_efficiencies": calibrated_from_balanced == balanced_efficiencies,
    "zero_efficiency_blocks_two_channel_inversion": recover_known(zero_efficiency_records, Fraction(0), Fraction(1)) is None,
    "all_record_probabilities_are_normalized": all(sum(value) == 1 for value in (records_a, records_b, biased_records, known_records, balanced_records)),
    "all_record_probabilities_are_nonnegative": all(entry >= 0 for value in (records_a, records_b, biased_records, known_records, balanced_records) for entry in value),
}
assert all(checks.values()), checks
result = {"schema": "marici.aspect.outcome-dependent-loss-identifiability.v1", "status": "passed", "checks": checks, "indistinguishable_pair": {"A": [str(value) for value in A], "B": [str(value) for value in B], "records": [str(value) for value in records_a]}, "conditional_bias": str(conditional), "known_efficiency_recovery": str(recovered_m), "claim_boundary": "Binary-setting exact diagnostic; full tomography requires the condition settingwise or a proved shared calibration model."}
output = Path(__file__).parents[1] / "results" / "outcome_dependent_loss_identifiability.json"
output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": result["status"], "check_count": len(checks), "conditional_bias": str(conditional)}, sort_keys=True))
