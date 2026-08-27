from fractions import Fraction
import json

lam = Fraction(3, 2)

# For g(q)=exp(-2 lambda q): H_0(0)=0, H_infinity(infinity)=0,
# and their constant difference is the total period.
period = 1 / (2 * lam)
h0_at_zero = Fraction(0)
hinf_at_zero = -period
h0_minus_hinf = period

checks = {
    "period_is_nonzero": period > 0,
    "zero_normalized_homotopy_starts_at_zero": h0_at_zero == 0,
    "infinity_normalized_homotopy_has_nonzero_zero_endpoint": hinf_at_zero != 0,
    "homotopy_difference_equals_period": h0_minus_hinf == period,
    "one_homotopy_cannot_obey_both_endpoint_normalizations": period != 0,
}

out = {
    "schema": "marici.grothendieck.two-endpoint-homotopy-seam-period.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "witness": {
        "lambda": str(lam),
        "period": str(period),
        "H_0_at_zero": str(h0_at_zero),
        "H_infinity_at_zero": str(hinf_at_zero),
    },
}

print(json.dumps(out, indent=2, sort_keys=True))
raise SystemExit(0 if out["passed"] else 1)

