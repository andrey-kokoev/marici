"""Exact two-atom reconstruction of the first Jacobi operator."""

from fractions import Fraction as F
import json
from pathlib import Path


atoms = [(F(1, 2), F(1)), (F(1, 3), F(4))]


def D(k):
    return sum(weight * value**k for weight, value in atoms)


D0, D1, D2, D3 = (D(k) for k in range(4))
a0 = D1 / D0
b1_squared = (D0 * D2 - D1**2) / D0**2
h1 = D2 - 2 * a0 * D1 + a0**2 * D0
a1 = (D3 - 2 * a0 * D2 + a0**2 * D1) / h1
assert b1_squared > 0

trace = a0 + a1
determinant = a0 * a1 - b1_squared
assert trace == 5
assert determinant == 4

result = {
    "support": [str(value) for _, value in atoms],
    "D0_through_D3": [str(value) for value in (D0, D1, D2, D3)],
    "a0": str(a0),
    "b1_squared": str(b1_squared),
    "a1": str(a1),
    "Jacobi_trace": str(trace),
    "Jacobi_determinant": str(determinant),
    "reconstructed_characteristic_polynomial": "z^2-5z+4",
    "reconstructed_support_exactly": True,
    "scalar_atom_weights_create_eigenspace_multiplicity": False,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "one-time-hankel-jacobi-operator.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
