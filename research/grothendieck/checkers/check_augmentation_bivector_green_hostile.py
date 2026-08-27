"""Exact off-seam hostile for the augmentation-bivector Green identity."""

from fractions import Fraction
import json


s = Fraction(1, 2)
omega = (Fraction(1), Fraction(1))
v = (Fraction(1), Fraction(-1))

# G(q)=exp(-(s+1)q)v and f(q)=G(q).
decay_rate = s + 1
wedge_at_zero = omega[0] * v[1] - omega[1] * v[0]
endpoint_energy = wedge_at_zero * wedge_at_zero
integrated_energy = endpoint_energy / (2 * decay_rate)
forcing_overlap = integrated_energy
green_left = 2 * s * integrated_energy
green_right = endpoint_energy - 2 * forcing_overlap

checks = {
    "off_seam_real_part_positive": s > 0,
    "scalar_augmentation_vanishes": omega[0] * v[0] + omega[1] * v[1] == 0,
    "bivector_endpoint_is_nonzero": endpoint_energy > 0,
    "canonical_tail_decay_rate": decay_rate == Fraction(3, 2),
    "integrated_energy_exact": integrated_energy == Fraction(4, 3),
    "green_identity_exact": green_left == green_right == Fraction(4, 3),
}

result = {
    "schema": "marici.grothendieck.augmentation-bivector-green-hostile.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "witness": {
        "s": str(s),
        "omega": [str(x) for x in omega],
        "v": [str(x) for x in v],
        "endpoint_energy": str(endpoint_energy),
        "integrated_energy": str(integrated_energy),
        "forcing_overlap": str(forcing_overlap),
    },
}

print(json.dumps(result, indent=2, sort_keys=True))
