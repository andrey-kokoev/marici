from fractions import Fraction
import json

individual = (Fraction(1, 2), Fraction(1, 2))

same_sign_cross = Fraction(1, 2)
opposite_sign_cross = Fraction(-1, 2)

same_sign_total = sum(individual) + 2 * same_sign_cross
opposite_sign_total = sum(individual) + 2 * opposite_sign_cross

checks = {
    "one_label_periods_identical": individual == (Fraction(1, 2), Fraction(1, 2)),
    "same_sign_total_is_two": same_sign_total == 2,
    "opposite_sign_total_is_zero": opposite_sign_total == 0,
    "same_one_body_data_different_seam_period": same_sign_total != opposite_sign_total,
    "off_diagonal_gram_entry_carries_difference": (
        same_sign_cross != opposite_sign_cross
    ),
}

out = {
    "schema": "marici.grothendieck.seam-period-pair-label-necessity.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "witness": {
        "individual_periods": [str(x) for x in individual],
        "same_sign_cross": str(same_sign_cross),
        "opposite_sign_cross": str(opposite_sign_cross),
        "same_sign_total": str(same_sign_total),
        "opposite_sign_total": str(opposite_sign_total),
    },
}

print(json.dumps(out, indent=2, sort_keys=True))
raise SystemExit(0 if out["passed"] else 1)

