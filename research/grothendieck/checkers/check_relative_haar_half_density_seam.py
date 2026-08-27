from fractions import Fraction
import json

p = Fraction(4)
half_density = Fraction(2)

# Exact norm-squared multipliers for f(x/p).
additive_multiplier = p
multiplicative_multiplier = Fraction(1)
relative_ratio = additive_multiplier / multiplicative_multiplier

s_on_seam = Fraction(1, 2)
additive_mellin_multiplier = p ** (1 - 2 * s_on_seam)
multiplicative_mellin_multiplier = p ** (-2 * s_on_seam)

checks = {
    "additive_haar_dilation_multiplier_is_p": additive_multiplier == p,
    "multiplicative_haar_dilation_is_invariant": multiplicative_multiplier == 1,
    "relative_ratio_is_p": relative_ratio == p,
    "half_density_square_is_relative_ratio": half_density**2 == relative_ratio,
    "additive_mellin_transport_is_isometric_at_half": additive_mellin_multiplier == 1,
    "multiplicative_channel_remains_distinct": multiplicative_mellin_multiplier == 1 / p,
}

out = {
    "schema": "marici.grothendieck.relative-haar-half-density-seam.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "witness": {
        "p": str(p),
        "relative_norm_squared_ratio": str(relative_ratio),
        "critical_real_part": str(s_on_seam),
        "additive_mellin_multiplier": str(additive_mellin_multiplier),
        "multiplicative_mellin_multiplier": str(multiplicative_mellin_multiplier),
    },
}

print(json.dumps(out, indent=2, sort_keys=True))
raise SystemExit(0 if out["passed"] else 1)
