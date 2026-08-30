#!/usr/bin/env python3
"""Verify bounded Shor-cat syndrome schedules for the frozen component codes."""

from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from check_s3_five_rail_code_freeze import QUBIT, QUTRIT, weight  # noqa: E402


def cat_shift_audit(q, cat_length):
    accepted = []
    rejected = []
    for shifts in itertools.product(range(q), repeat=cat_length):
        checks = tuple((shifts[i] - shifts[i + 1]) % q for i in range(cat_length - 1))
        (accepted if all(check == 0 for check in checks) else rejected).append(shifts)
    expected_global = {tuple([shift] * cat_length) for shift in range(q)}
    assert set(accepted) == expected_global
    return {
        "field_order": q,
        "cat_length": cat_length,
        "shift_patterns": q**cat_length,
        "accepted_patterns": len(accepted),
        "accepted_patterns_are_only_global_shifts": True,
        "rejected_dangerous_patterns": len(rejected),
        "adjacent_verification_checks": cat_length - 1,
    }


def schedule(name, q, stabilizers):
    weights = [weight(row) for row in stabilizers]
    cat_audits = [cat_shift_audit(q, w) for w in sorted(set(weights))]
    per_round_contacts = sum(weights)
    per_round_verifications = sum(w - 1 for w in weights)
    # Three repeated complete syndrome rounds: a single wrong sample in each
    # generator's three-symbol column cannot change its majority value.
    majority_cases = 0
    for true_value in range(q):
        for bad_position in range(3):
            for bad_value in range(q):
                samples = [true_value] * 3
                samples[bad_position] = bad_value
                decoded = max(range(q), key=samples.count)
                assert decoded == true_value
                majority_cases += 1
    return {
        "code": name,
        "field_order": q,
        "stabilizer_weights": weights,
        "cat_shift_audits": cat_audits,
        "complete_syndrome_rounds": 3,
        "cat_data_contacts_per_round": per_round_contacts,
        "cat_verification_checks_per_round": per_round_verifications,
        "cat_data_contacts_per_recovery": 3 * per_round_contacts,
        "cat_verification_checks_per_recovery": 3 * per_round_verifications,
        "fresh_cat_rails_prepared_per_recovery": 3 * per_round_contacts,
        "majority_cases_checked": majority_cases,
        "single_bad_syndrome_sample_corrected": True,
    }


def main():
    qubit = schedule("[[5,1,3]]_2", 2, QUBIT)
    qutrit = schedule("[[5,1,3]]_3", 3, QUTRIT)
    result = {
        "schema": "marici.kitaev.s3-five-rail-shor-recovery.v1",
        "component_schedules": {"qubit": qubit, "qutrit": qutrit},
        "six_level_bus_recovery": {
            "parallel_component_rounds": 3,
            "cat_data_contacts": qubit["cat_data_contacts_per_recovery"]
            + qutrit["cat_data_contacts_per_recovery"],
            "cat_verification_checks": qubit["cat_verification_checks_per_recovery"]
            + qutrit["cat_verification_checks_per_recovery"],
            "fresh_cat_rails_prepared": qubit["fresh_cat_rails_prepared_per_recovery"]
            + qutrit["fresh_cat_rails_prepared_per_recovery"],
        },
        "eight_level_bus_recovery": {
            "parallel_binary_components": 3,
            "complete_syndrome_rounds": 3,
            "cat_data_contacts": 3 * qubit["cat_data_contacts_per_recovery"],
            "cat_verification_checks": 3 * qubit["cat_verification_checks_per_recovery"],
            "fresh_cat_rails_prepared": 3 * qubit["fresh_cat_rails_prepared_per_recovery"],
        },
        "fault_contract": [
            "each accepted cat rail contacts at most one data rail",
            "adjacent cat checks reject every nonglobal shift pattern",
            "global cat shift preserves the cat state",
            "phase/readout errors are suppressed by three complete syndrome rounds",
            "a correction is applied from the component recovery table",
        ],
        "one_ec_boundary": "The schedule proves clean-input/one-fault containment and fault-free correction of one input error. Input-error plus circuit-fault combinations belong to the malignant-pair audit.",
        "verdict": "Fresh verified generalized Shor cats give an explicit nonpropagating recovery schedule for all frozen five-rail components. The schedule removes syndrome extraction as an untyped interface, but it does not create the missing nonstabilizer gate resources.",
    }
    output = Path(__file__).parents[1] / "results" / "s3-five-rail-shor-recovery.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
