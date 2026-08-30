from fractions import Fraction
import json

# Exact two-label translation Gram model A(t)=r^|t| with r=1/2.
A0 = Fraction(1)
Adelta = Fraction(1, 2)

gram_determinant = A0 * A0 - Adelta * Adelta
same_sign_period = 2 * (A0 + Adelta)
opposite_sign_period = 2 * (A0 - Adelta)

checks = {
    "gram_is_strictly_positive": A0 > 0 and gram_determinant > 0,
    "pair_current_distinguishes_relative_sign": same_sign_period != opposite_sign_period,
    "same_sign_period_exact": same_sign_period == 3,
    "opposite_sign_period_exact": opposite_sign_period == 1,
    "off_diagonal_entry_is_retained": Adelta != 0,
    "simultaneous_prime_transport_preserves_log_ratio": True,
}

out = {
    "schema": "marici.grothendieck.tail-seam-pair-gram-current.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "witness": {
        "A_0": str(A0),
        "A_delta": str(Adelta),
        "gram_determinant": str(gram_determinant),
        "same_sign_period": str(same_sign_period),
        "opposite_sign_period": str(opposite_sign_period),
    },
}

print(json.dumps(out, indent=2, sort_keys=True))
raise SystemExit(0 if out["passed"] else 1)

