"""Exact hostile upper bound for the 45-contour apparatus cospark."""

import hashlib
import itertools
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
ARTIFACT = ROOT / "research/strominger/spin-memory-contour-cospark-attack.md"

z = sp.symbols("z", real=True)
latitudes = (-sp.Rational(2, 3), -sp.Rational(1, 3), sp.Integer(0),
             sp.Rational(1, 3), sp.Rational(2, 3))
longitude_count = 9
degrees = (2, 3, 4)


def surviving_abs_m(dark_indices):
    survivors = []
    for abs_m in range(5):
        admitted = [degree for degree in degrees if degree >= abs_m]
        evaluation = sp.Matrix([
            [sp.assoc_legendre(degree, abs_m, latitudes[index]) for degree in admitted]
            for index in dark_indices
        ])
        if evaluation.rank() < len(admitted):
            survivors.append(abs_m)
    return survivors


four_dark_survivors = {
    str(indices): surviving_abs_m(indices)
    for indices in itertools.combinations(range(5), 4)
}
three_dark_survivors = {
    str(indices): surviving_abs_m(indices)
    for indices in itertools.combinations(range(5), 3)
}

radial = sp.assoc_legendre(4, 1, z) - sp.Rational(5, 54) * sp.assoc_legendre(2, 1, z)
radial_samples = [sp.simplify(radial.subs(z, latitude)) for latitude in latitudes]

# The real m=+-1 combination sin(phi) vanishes at j=0. Because 9 is odd,
# no other sampled longitude is an integer multiple of pi.
dark_longitudes = [
    j for j in range(longitude_count)
    if sp.simplify(sp.sin(2 * sp.pi * sp.Rational(j, longitude_count))) == 0
]
sample_support = [
    (latitude_index, longitude_index)
    for latitude_index, radial_value in enumerate(radial_samples)
    for longitude_index in range(longitude_count)
    if radial_value != 0 and longitude_index not in dark_longitudes
]

checks = {
    "no_four_latitude_rings_can_be_dark": all(not value for value in four_dark_survivors.values()),
    "outer_equator_triple_leaves_only_abs_m_one": (
        three_dark_survivors[str((0, 2, 4))] == [1]
    ),
    "only_two_three_ring_dark_patterns_exist": sum(
        bool(value) for value in three_dark_survivors.values()
    ) == 2,
    "radial_hostile_vanishes_on_outer_and_equator_rings": all(
        radial_samples[index] == 0 for index in (0, 2, 4)
    ),
    "radial_hostile_survives_on_inner_rings": all(
        radial_samples[index] != 0 for index in (1, 3)
    ),
    "odd_longitude_grid_has_one_sine_zero": dark_longitudes == [0],
    "hostile_support_is_exactly_16": len(sample_support) == 16,
    "hostile_zero_count_is_29": 45 - len(sample_support) == 29,
    "sixteen_deletions_can_destroy_faithfulness": len(sample_support) == 16,
    "universal_erasure_tolerance_at_most_15": len(sample_support) - 1 == 15,
}
checks = {name: bool(value) for name, value in checks.items()}
failed = [name for name, passed in checks.items() if not passed]

payload = {
    "schema": "marici.strominger.spin-memory-contour-cospark-attack-result.v1",
    "artifact_sha256": hashlib.sha256(ARTIFACT.read_bytes()).hexdigest().upper(),
    "passed": sum(checks.values()),
    "total": len(checks),
    "checks": checks,
    "observed": {
        "hostile_radial_factor": "P_4^1(z) - (5/54) P_2^1(z)",
        "hostile_azimuthal_factor": "sin(phi)",
        "radial_samples": [str(value) for value in radial_samples],
        "dark_latitude_indices": [0, 2, 4],
        "dark_longitude_indices_on_surviving_rings": dark_longitudes,
        "hostile_support_size": len(sample_support),
        "hostile_zero_count": 45 - len(sample_support),
        "certified_universal_deletions_lower_bound": 2,
        "universal_deletions_upper_bound": 15,
    },
    "verdict": (
        "An exact m=+-1 packet has only 16 nonzero contour readings. Deleting those "
        "16 ports destroys faithfulness, so universal deletion tolerance is at most 15. "
        "Combined with the frame theorem it lies between 2 and 15 inclusive."
    ),
}
print(json.dumps(payload, indent=2, sort_keys=True))
if failed:
    raise SystemExit("failed checks: " + ", ".join(failed))
