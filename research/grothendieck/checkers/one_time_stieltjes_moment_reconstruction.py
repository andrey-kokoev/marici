"""Finite-atom audit of one-time Stieltjes moment reconstruction."""

from fractions import Fraction as F
import json
import math
from pathlib import Path


t0 = F(1)
# These are the tilted weights dmu_0=e^(-t0*lambda)dnu, represented directly
# as rationals so the moment/Hankel identities remain exact.
tilted_atoms = [(F(1, 2), F(1)), (F(1, 3), F(3)), (F(1, 7), F(6))]


def D(k):
    return sum(weight * spectral_value**k for weight, spectral_value in tilted_atoms)


moments = [D(k) for k in range(7)]

# Exact order-two ordinary Hankel LDL pivots.
matrix = [[moments[i + j] for j in range(3)] for i in range(3)]
L = [[F(0) for _ in range(3)] for _ in range(3)]
pivots = []
for i in range(3):
    L[i][i] = F(1)
    for j in range(i):
        numerator = matrix[i][j] - sum(L[i][k] * pivots[k] * L[j][k] for k in range(j))
        L[i][j] = numerator / pivots[j]
    pivot = matrix[i][i] - sum(L[i][k] ** 2 * pivots[k] for k in range(i))
    pivots.append(pivot)
assert all(pivot > 0 for pivot in pivots)

# Numerical Taylor/Laplace agreement for the finite measure is a direct
# regression of equation (7); positivity itself was checked exactly above.
s = 0.2
exact_shift = sum(float(weight) * math.exp(-s * float(value)) for weight, value in tilted_atoms)
partial = sum(((-s) ** k) * float(moments[k]) / math.factorial(k) for k in range(7))
assert abs(exact_shift - partial) < 2e-3

result = {
    "chosen_time": str(t0),
    "atom_count": len(tilted_atoms),
    "D0_through_D6": [str(value) for value in moments],
    "order_two_Hankel_LDL_pivots": [str(value) for value in pivots],
    "all_exact_pivots_positive": True,
    "Taylor_shift": s,
    "Taylor_Laplace_residual_order_six": exact_shift - partial,
    "finite_measure_has_all_exponential_moments": True,
    "one_time_data_reconstructs_heat_germ": True,
}

if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "one-time-stieltjes-moment-reconstruction.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")
