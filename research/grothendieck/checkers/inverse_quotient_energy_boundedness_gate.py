"""Finite-prefix witness for phantom inverse-limit families and energy gate."""

import json
from fractions import Fraction
from pathlib import Path

cutoffs = [1, 2, 4, 8, 16, 32, 64]
ones_energy = [n for n in cutoffs]
harmonic_square_energy = [sum(Fraction(1, k * k) for k in range(1, n + 1)) for n in cutoffs]

checks = {
    "all_one_prefixes_are_compatible": all([1] * n == ([1] * (2 * n))[:n] for n in cutoffs[:-1]),
    "all_one_energy_is_unbounded_on_samples": all(a < b for a, b in zip(ones_energy, ones_energy[1:])),
    "harmonic_square_energy_is_monotone": all(
        a < b for a, b in zip(harmonic_square_energy, harmonic_square_energy[1:])
    ),
    "harmonic_square_energy_has_uniform_bound_two": all(value < 2 for value in harmonic_square_energy),
}
result = {
    "schema": "marici.grothendieck.inverse-quotient-energy-gate.v1",
    "cutoffs": cutoffs,
    "all_one_partial_energies": ones_energy,
    "inverse_coordinate_partial_energies": [str(value) for value in harmonic_square_energy],
    **checks,
    "all_verified": all(checks.values()),
    "claim_boundary": "Finite exact illustration; the infinite conclusions use the elementary monotone-series argument in the packet.",
}
assert result["all_verified"]
output = Path(__file__).parents[1] / "results" / "inverse-quotient-energy-gate.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
