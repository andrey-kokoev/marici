"""Neutrino mass scale from the seesaw in Gram framework."""
from pathlib import Path
import json
import math

ROOT = Path(__file__).resolve().parents[1]

# Gram numbers:
r_S12 = 11      # S12 overlap ratio G_ii/G_ij = 11!/10!
l_U1 = 12       # S4 overlap eigenvalue for U(1) (trivial irrep)
l_SU2 = 4       # S4 overlap eigenvalue for SU(2) (2D irrep)
G_self = 3456   # S4xS4xS4 self-overlap for nu_R
G_same = 1152   # same-generation off-diagonal for nu_R
G_cross = 576   # cross-generation off-diagonal for nu_R
v = 246.22      # Higgs vev (GeV)

# Observed neutrino parameters (NO, NuFIT 5.3):
dm2_21 = 7.41e-5   # eV^2
dm2_31 = 2.507e-3  # eV^2 (normal ordering)
m_nu2 = math.sqrt(dm2_21) if dm2_21 > 0 else 0  # eV
m_nu3 = math.sqrt(dm2_31) if dm2_31 > 0 else 0  # eV (approx, ignoring m_nu1)

# The 3x3 Gram for the sterile neutrino sector (nu_R across 3 generations):
# Diagonal: G_self (nu_R self-energy)
# Off-diagonal: depends on whether same or different generation
# Same gen, different type: G_same (but nu_R only connects to nu_R...)
# Actually: nu_R is the 1_b state (one per S4 block). The 3x3 Gram is:
# [G_self, G_cross, G_cross]
# [G_cross, G_self, G_cross]
# [G_cross, G_cross, G_self]

# Eigenvalues (Gram's sterile sector):
eig_heavy = G_self + 2 * G_cross  # heaviest sterile neutrino
eig_light = G_self - G_cross       # lighter sterile neutrinos (two degenerate)

print("=== Neutrino mass from seesaw in Gram framework ===")
print(f"Sterile neutrino Gram eigenvalues (dimensionless):")
print(f"  Heavy sterile: G_self + 2*G_cross = {G_self + 2*G_cross}")
print(f"  Light sterile: G_self - G_cross = {G_self - G_cross}")
print(f"  Ratio heavy:light = {eig_heavy/eig_light:.4f}")
print()

# Neutrino Yukawa from the Gram (coupling between 1_b and 2):
y_nu_sq = (G_cross / G_self)**2  # (off-diagonal/diagonal)^2
y_nu = G_cross / G_self
print(f"Neutrino Yukawa coupling y_nu = G_cross/G_self = {y_nu:.4f}")
print(f"  y_nu^2 = {y_nu_sq:.4f}")
print()

# Seesaw: m_nu = y_nu^2 * v^2 / M_N
# M_N = sterile neutrino mass = Gram eigenvalue * (scale factor)
# Scale factor: how Gram eigenvalues map to physical masses

# If the sterile neutrino gets its mass from the same mechanism as other fermions:
# M_N = y_sterile * v / sqrt(2) where y_sterile is the sterile's "Yukawa" 
# But nu_R is a SM gauge singlet (Y=0), so it doesn't couple to the Higgs.
# Its mass is a Majorana mass, from a different Gram sector.

# The seesaw mass relation:
# m_nu = y_nu^2 * v^2 / M_N
# => M_N = y_nu^2 * v^2 / m_nu

for label, m_nu in [("m_nu3 (0.050 eV)", 0.050e-9), ("m_nu2 (0.0086 eV)", 0.0086e-9)]:
    M_N = y_nu_sq * v**2 / m_nu
    ratio_to_v = M_N / v
    ratio_to_MPl = M_N / 1.22e19
    
    print(f"Seesaw: m_nu ~ {label}:")
    print(f"  M_N = y_nu^2 * v^2 / m_nu = {M_N:.2e} GeV")
    print(f"  M_N / v = {ratio_to_v:.2e}")
    print(f"  M_N / M_Pl = {ratio_to_MPl:.2e}")
    print()

# The ratio M_N / M_Pl might be a Gram number combination:
# For m_nu3 (0.050 eV): M_N = 3.36e13 GeV, M_N/M_Pl = 2.75e-6
# 2.75e-6 = 1/363000. Is this a Gram combination?
# 363000 = 11^5 + 4^6 + 4*11? = 161051 + 4096 + 44 = 165191. No.
# 363000 = (11+4)!/something? 15! = 1.3e12. No.

# Ratio of Gram eigenvalues to v:
print("=== Gram ratios to Higgs vev ===")
# The Gram eigenvalues for the sterile sector:
# eig_heavy = 4608, eig_light = 2880
# If M_N = (eig_value) * (scale_factor) * v:
# For m_nu3: M_N = 3.36e13 GeV
# scale = M_N / (4608 * v) = 3.36e13 / (4608*246) = 3.36e13 / 1.13e6 = 2.97e7

scale_for_heavy = (y_nu_sq * v**2 / 0.050e-9) / (eig_heavy * v)
scale_for_light = (y_nu_sq * v**2 / 0.0086e-9) / (eig_light * v)

print(f"Scale factor: M_N = scale * eig * v")
print(f"  For heavy sterile: scale = {scale_for_heavy:.2e}")
print(f"  For light sterile: scale = {scale_for_light:.2e}")
print()

# The scale factor might be 1/11^6?
# 11^6 = 1771561. 1/11^6 = 5.64e-7.
# But we need O(10^7), not O(10^-7).

# What about M_Pl / v = 4.96e16?
# M_N = v * (eig value) * (M_Pl/v) / (something)?
# For heavy: M_N = 3.36e13 = 246 * 4608 * (1.22e19/246) / X?
# = 246 * 4608 * 4.96e16 / X
# = 5.63e22 / X
# X = 5.63e22 / 3.36e13 = 1.67e9

# 1.67e9 = ?
# 11^8 = 2.14e8. Close.
# 11^8 * 4 = 8.6e8. Closer.
# 11^8 * 4 * 2 = 1.7e9. Close but 2 is not Gram.

# 11^9 / 4 = 2.36e9 / 4 = 5.9e8. No.
# 11^8 + 4^12 = 2.14e8 + 1.68e7 = 2.3e8. No.

# The scale factor might not have a simple Gram expression.

print("=== Summary ===")
print("The neutrino mass scale from the seesaw:")
print(f"  m_nu3 ~ {0.050e-9*1e9:.4f} eV (from dm2_31 = 2.5e-3 eV^2)")
print(f"  m_nu2 ~ {0.0086e-9*1e9:.4f} eV (from dm2_21 = 7.4e-5 eV^2)")
print(f"  Ratio m_nu3/m_nu2 = {m_nu3/m_nu2:.2f}")
print()
print("The seesaw scale M_N from Gram numbers:")
print(f"  M_N = (G_cross/G_self)^2 * v^2 / m_nu")
print(f"  For m_nu3: M_N = 3.4e13 GeV, M_N/v = 1.38e11")
print(f"  For m_nu2: M_N = 2.0e14 GeV, M_N/v = 8.0e11")
print()
print("A clean Gram expression for M_N/v is not obvious.")
print("The neutrino mass scale requires further structure.")

result = {
    'schema': 'marici.nima.neutrino_seesaw_gram.v1',
    'classification': 'Neutrino_masses_from_seesaw_in_Gram_framework_seesaw_scale_not_yet_clean',
    'sterile_Gram_eigenvalues': {'heavy': int(eig_heavy), 'light': int(eig_light)},
    'y_nu': round(y_nu, 4),
    'M_N_for_nu3_GeV': float(y_nu_sq * v**2 / 0.050e-9),
    'M_N_for_nu2_GeV': float(y_nu_sq * v**2 / 0.0086e-9),
    'ratio_m_nu3_m_nu2': round(m_nu3/m_nu2, 2),
    'status': 'The seesaw mechanism determines neutrino masses from the sterile neutrino Gram. The Yukawa y_nu = G_cross/G_self = 1/6 is a Gram ratio. The sterile mass scale M_N = 3.4e13 GeV (for m_nu3) does not have an obvious clean Gram expression. Further structure is needed to determine the absolute seesaw scale.',
}

out = ROOT / 'results/neutrino-seesaw.json'
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(f"\n{json.dumps(result, indent=2)}")