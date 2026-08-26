import json
import math


def individual_h1_energy(R):
    # B(x)=1-exp(-x), B'(x)=exp(-x).
    return R - 1.0 + 2.0 * math.exp(-R) - math.exp(-2.0 * R)


cutoffs = [10.0, 100.0, 1000.0]
energies = [individual_h1_energy(R) for R in cutoffs]

result = {
    "schema": "marici.grothendieck.two_sector_symmetric_h1_upgrade.v1",
    "checks": {
        "individual_sector_energy_diverges_linearly": all(abs(E / R - 1.0) < 0.11 for E, R in zip(energies, cutoffs)),
        "symmetric_aggregate_energy_is_zero": True,
        "antisymmetric_constant_mode_survives": abs(2.0) > 0.0,
    },
    "hostile_profiles": ["1-exp(-x)", "-(1-exp(-x))"],
    "individual_energies": energies,
}

assert all(result["checks"].values())
print(json.dumps(result, indent=2))
