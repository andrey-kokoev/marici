"""Proton-electron mass ratio from Gram numbers."""
from pathlib import Path
import json
import math

ROOT = Path(__file__).resolve().parents[1]

# Gram numbers:
l_U1 = 12       # U(1) eigenvalue from S4
C_SU2 = 3       # SU(2) matter trace = 6 doublets x 1/2

# Observed proton and electron masses:
m_p = 938.272   # MeV
m_e = 0.510998  # MeV
ratio_obs = m_p / m_e

# Gram prediction:
# m_p / m_e = l_U1 * (l_U1^2 + C_SU2^2) = 12 * (144 + 9) = 12 * 153 = 1836
ratio_pred = l_U1 * (l_U1**2 + C_SU2**2)

print("=== Proton-electron mass ratio ===")
print(f"m_p/m_e = l_U1 * (l_U1^2 + C_SU2^2)")
print(f"        = {l_U1} * ({l_U1}^2 + {C_SU2}^2)")
print(f"        = {l_U1} * ({l_U1**2} + {C_SU2**2})")
print(f"        = {l_U1} * {l_U1**2 + C_SU2**2}")
print(f"        = {ratio_pred}")
print(f"Observed: {ratio_obs:.4f}")
print(f"Error: {abs(ratio_pred - ratio_obs)/ratio_obs*100:.4f}%")
print()

# Both m_p and m_e individually from Gram expressions:
# m_p = 14/3 * Lambda_QCD = 14/3 * M_Pl / 11^19
# m_e = m_p / (12 * (12^2 + 3^2)) = m_p / 1836

# So m_e = m_p / ratio_pred = 938.272 / 1836 = 0.51104 MeV
m_e_from_ratio = m_p / ratio_pred
print(f"m_e from m_p / 1836 = {m_e_from_ratio:.6f} MeV")
print(f"m_e observed = {m_e:.6f} MeV")
print(f"Error: {abs(m_e_from_ratio - m_e)/m_e*100:.4f}%")

result = {
    'schema': 'marici.nima.proton_electron_ratio.v1',
    'classification': 'proton_electron_mass_ratio_equals_l_U1_times_l_U1_sq_plus_C_SU2_sq_12_times_153_1836',
    'expression': f'{l_U1} * ({l_U1}^2 + {C_SU2}^2)',
    'predicted': ratio_pred,
    'observed': round(ratio_obs, 4),
    'error_percent': round(abs(ratio_pred - ratio_obs)/ratio_obs*100, 4),
    'finding': f'Proton-electron mass ratio m_p/m_e = {l_U1} * ({l_U1}² + {C_SU2}²) = 12 × 153 = {ratio_pred}. Observed {ratio_obs}. Error < 0.01%.',
}

out = ROOT / 'results/proton-electron-ratio.json'
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(f"\n{json.dumps(result, indent=2)}")