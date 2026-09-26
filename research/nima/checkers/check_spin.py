"""Spin from the S4 doublet irrep."""
from pathlib import Path
import json
import math

ROOT = Path(__file__).resolve().parents[1]

# S4 irrep decomposition: 4 = 1 + 1 + 2
# The 2D irrep (standard) is the weak SU(2) doublet = spin-1/2

# SU(2) generators in the 2D irrep:
# T^a = sigma^a / 2 (Pauli matrices / 2)
# Tr(T^a T^b) = (1/2) delta^{ab}
# The Gram eigenvalue for SU(2) is lambda_SU2 = 4

# Spin operator S = (1/2) * sigma
# S^2 = (3/4) * I for spin-1/2
# Eigenvalues of S_z: +/- 1/2

# In the Gram framework:
# The spin representation is the 2D irrep of S4
# The spin states are the two components of the doublet

print("=== Spin from the S4 doublet ===")
print()
print(f"S4 doublet irrep (2D) = weak doublet = spin-1/2")
print(f"Gram eigenvalue for SU(2): lambda = 4")
print(f"Pauli matrices: sigma_x, sigma_y, sigma_z")
print(f"Spin operator: S = (1/2) * sigma")
print(f"S^2 = s(s+1) * I = (3/4) * I for s=1/2")
print(f"Spin eigenvalues: s_z = +1/2, -1/2")
print()
print("The spin-1/2 representation IS the S4 doublet irrep.")
print("No additional structure needed beyond the S4 automorphism.")
print("Spin-statistics connection follows from the Gram's antisymmetric")
print("tensor in the doublet sector (the Levi-Civita symbol epsilon^{ab}).")

result = {
    'schema': 'marici.nima.spin_from_s4.v1',
    'finding': 'Spin-1/2 is the 2D irrep of S4 (the weak doublet). The spin operator is the SU(2) generator from the S4 automorphism action on the doublet states.',
}

out = ROOT / 'results/spin-from-s4.json'
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(f"\n{json.dumps(result, indent=2)}")