"""Exact finite audit: Born intensity needs the source *-pairing."""

from __future__ import annotations

import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "research/nima/results/quadratic-readout-typed-closure.json"
Gaussian = tuple[int, int]


def add(z: Gaussian, w: Gaussian) -> Gaussian:
    return z[0] + w[0], z[1] + w[1]


def conjugate(z: Gaussian) -> Gaussian:
    return z[0], -z[1]


def multiply(z: Gaussian, w: Gaussian) -> Gaussian:
    return z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0]


def norm2(z: Gaussian) -> int:
    product = multiply(z, conjugate(z))
    assert product[1] == 0
    return product[0]


def intensity(a: Gaussian, b: Gaussian) -> int:
    return norm2(add(a, b))


grid = tuple(itertools.product(range(-2, 3), repeat=2))

# The scaling law alone rules out every linear readout on amplitude space.
linear_scaling_counterexamples = [
    z for z in grid if z != (0, 0) and norm2((2 * z[0], 2 * z[1])) != 2 * norm2(z)
]

construction_checks = 0
polarization_checks = 0
phase_checks = 0
units = ((1, 0), (-1, 0), (0, 1), (0, -1))
for a in grid:
    for b in grid:
        constructed = multiply(add(a, b), conjugate(add(a, b)))
        construction_checks += 1
        assert constructed == (intensity(a, b), 0)

        cross = (
            multiply(a, conjugate(b))[0] + multiply(conjugate(a), b)[0]
        )
        polarization_checks += 1
        assert intensity(a, b) - norm2(a) - norm2(b) == cross

        for unit in units:
            phase_checks += 1
            assert intensity(multiply(unit, a), multiply(unit, b)) == intensity(a, b)

gates = {
    "linear_amplitude_closure_cannot_contain_intensity": bool(linear_scaling_counterexamples),
    "star_pairing_constructs_intensity_exactly": construction_checks == len(grid) ** 2,
    "interference_is_the_polarized_cross_term": polarization_checks == len(grid) ** 2,
    "common_phase_invariance_is_derived": phase_checks == len(grid) ** 2 * len(units),
    "readout_is_quadratic_under_integer_scaling": norm2((2, 0)) == 4 * norm2((1, 0)),
    "pairing_is_not_recoverable_from_linear_scaling": norm2((2, 0)) != 2 * norm2((1, 0)),
}
assert all(gates.values()), gates

result = {
    "schema": "marici.nima.quadratic-readout-typed-closure.v1",
    "gaussian_integer_grid_size": len(grid),
    "construction_checks": construction_checks,
    "polarization_checks": polarization_checks,
    "phase_checks": phase_checks,
    "gates": gates,
    "conclusion": (
        "Born intensity is absent from linear probe closure but is generated "
        "canonically by amplitude addition, conjugation, and multiplication. "
        "The coefficient *-pairing is therefore a necessary typed operation, "
        "not a freely fitted readout."
    ),
}
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"passed": sum(gates.values()), "total": len(gates)}))
