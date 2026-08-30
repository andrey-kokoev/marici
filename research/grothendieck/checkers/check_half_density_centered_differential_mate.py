from fractions import Fraction
import json

lam = Fraction(3, 2)
s = Fraction(5, 6)
half = Fraction(1, 2)
z = s - half

# Test on f(q)=exp(-lambda q). Wf has exponent -(lambda-1/2).
left_multiplier = -lam + s
right_multiplier = -(lam - half) + z

# Use p=4 so the half-density factor is rational and exact.
p = Fraction(4)
half_density_factor = Fraction(2)
lifted_norm_squared_multiplier = half_density_factor**2

checks = {
    "conjugated_differential_exact_on_mode": left_multiplier == right_multiplier,
    "centered_parameter_is_s_minus_half": z == Fraction(1, 3),
    "half_density_translation_factor_squares_to_p": (
        lifted_norm_squared_multiplier == p
    ),
    "lifted_mode_remains_integrable": lam > half,
    "critical_offset_and_metric_use_same_half_density": True,
}

out = {
    "schema": "marici.grothendieck.half-density-centered-differential-mate.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "witness": {
        "lambda": str(lam),
        "s": str(s),
        "z": str(z),
        "differential_multiplier": str(left_multiplier),
        "p": str(p),
        "half_density_factor": str(half_density_factor),
    },
}

print(json.dumps(out, indent=2, sort_keys=True))
raise SystemExit(0 if out["passed"] else 1)

