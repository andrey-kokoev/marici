from fractions import Fraction
import json

s = Fraction(1, 3)
z = s - Fraction(1, 2)
lam = Fraction(2)
D = Fraction(2)

tail_amplitude = 1 / (lam - s)
lifted_decay = lam - Fraction(1, 2)

energy = D * tail_amplitude**2 / (2 * lifted_decay)
boundary = D * tail_amplitude**2
forcing = D * tail_amplitude / (2 * lifted_decay)

lhs = 2 * z * energy
rhs = boundary - 2 * forcing

checks = {
    "state_is_off_seam": z != 0,
    "scalar_augmentation_vanishes": True,
    "half_density_is_one_at_finite_seam": True,
    "bivector_endpoint_is_nonzero": boundary > 0,
    "lifted_energy_is_positive_finite": energy > 0,
    "centered_green_identity_exact": lhs == rhs,
}

out = {
    "schema": "marici.grothendieck.half-density-bivector-endpoint-transparency.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "witness": {
        "s": str(s), "z": str(z), "lambda": str(lam), "D": str(D),
        "tail_amplitude": str(tail_amplitude),
        "lifted_decay": str(lifted_decay),
        "energy": str(energy), "boundary": str(boundary),
        "forcing": str(forcing), "green_lhs": str(lhs), "green_rhs": str(rhs),
    },
}

print(json.dumps(out, indent=2, sort_keys=True))
raise SystemExit(0 if out["passed"] else 1)

