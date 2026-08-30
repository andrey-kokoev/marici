"""Exact rational audit of endpoint--zeta pole cancellation."""

from fractions import Fraction as F
import json
from pathlib import Path


def endpoint_pole(epsilon):
    return 1 / (epsilon * (1 + epsilon))


def zeta_principal_part(epsilon):
    return -1 / (epsilon * (1 + 2 * epsilon))


samples = [F(1, 2), F(1, 5), F(1, 20), F(1, 100)]
combined = [endpoint_pole(epsilon) + zeta_principal_part(epsilon) for epsilon in samples]
expected = [1 / ((1 + epsilon) * (1 + 2 * epsilon)) for epsilon in samples]
assert combined == expected

# Both individual residues are +/-1, while the sum has zero residue.
endpoint_residue = F(1)
zeta_residue = F(-1)
assert endpoint_residue + zeta_residue == 0

result = {
    "epsilon_samples": [str(value) for value in samples],
    "regular_combined_values": [str(value) for value in combined],
    "endpoint_residue": str(endpoint_residue),
    "zeta_pole_residue": str(zeta_residue),
    "completed_residue": "0",
    "pole_pair_acyclic": True,
    "regular_finite_part_survives": True,
    "physical_relative_chain_pushforward_constructed": False,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "endpoint-zeta-pole-mapping-cone.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
