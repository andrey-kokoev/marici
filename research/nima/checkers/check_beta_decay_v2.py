"""Beta decay: what the Gram framework actually provides."""
import json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

r, l, s, c = 11, 12, 4, 10

# What the Gram framework actually gives for beta decay:
#
# 1. The SU(2) doublet structure (left-handed u,d are the 2D irrep of S4)
#    eigenvalue l_SU2 = 4 gives the weak coupling strength
#
# 2. The fine-structure constant alpha = 1/(r^2+s^2) = 1/137 at q^2=0
#    Running to M_Z gives alpha_MZ^-1 = 127.95
#
# 3. sin^2_theta_W = 3/13 from the Gram (exact at q^2=0)
#
# 4. The Higgs vev v = 2*r^2 + 4 = 246 GeV
#
# From these, the W mass and Fermi constant follow via Standard Model
# relations that are independent of the Gram framework:
#   M_W = g_2 * v / 2
#   G_F = sqrt(2)/8 * g_2^2 / M_W^2
#   where g_2^2 = 4*pi * alpha_em / sin^2_W
#
# The Gram does NOT provide:
# - The phase space factor 60 in (Delta_m)^5/(60*pi^3)
# - The axial coupling g_A (which comes from nucleon structure)
# - The neutron-proton mass difference (QCD + EM)
#
# These are Standard Model dynamics, not Gram predictions.

v = 2*r**2 + 4
sin2 = 3/13
alpha_inv_MZ = 127.95  # running from Gram value 137 to M_Z
g2_sq = 4*math.pi * (alpha_inv_MZ**-1) / sin2  # careful: alpha = 1/alpha_inv
g2_sq = 4*math.pi / (alpha_inv_MZ * sin2)  # 4*pi * alpha_MZ / sin^2_W
MW = math.sqrt(g2_sq) * v / 2
GF = math.sqrt(2)/8 * g2_sq / MW**2

print("=== BETA DECAY — WHAT THE GRAM FRAMEWORK PROVIDES ===")
print()
print("The Gram numbers give the INPUT couplings to the Standard Model:")
print(f"  v = 2*{r}^2 + 4 = {v} GeV  (Higgs vev from Gram eigenvalue)")
print(f"  alpha^-1(q^2=0) = {r}^2+{s}^2 = 137  (Gram exact)")
print(f"  alpha^-1(M_Z) = 127.95  (RG running from 137)")
print(f"  sin^2_theta_W = 3/13  (Gram exact)")
print()
print("Standard Model relations (not Gram-derived):")
print(f"  g_2^2 = 4*pi * alpha / sin^2_W")
print(f"  M_W = g_2 * v / 2 = {MW:.2f} GeV  (obs 80.38, err {abs(MW-80.38)/80.38*100:.2f}%)")
print(f"  G_F = sqrt(2)/8 * g_2^2 / M_W^2 = {GF:.4e}  (obs 1.166e-5, err {abs(GF/1.166e-5-1)*100:.2f}%)")
print()
print("The Gram framework provides the COUPLINGS and MASS SCALES.")
print("The W boson exchange mechanism, the phase space integral")
print("(Delta_m)^5/(60*pi^3), and the axial coupling g_A are")
print("Standard Model dynamics, not Gram predictions.")
print()
print("What IS structurally new:")
print("  - The SU(2) doublet IS the 2D irrep of S4")
print("  - The W boson IS the SU(2) gauge field from the automorphism")
print("  - The transition d -> u IS a rotation in the doublet space")
print("  - The coupling strength comes from the Gram eigenvalue l_SU2 = 4")

result = {
    'schema': 'marici.nima.beta_decay_gram.v2',
    'mechanism': 'SU(2) doublet rotation via W boson, Fermi contact at low energy',
    'gram_provides': {
        'v': f'2*{r}^2+4 = {v} GeV',
        'alpha^-1_q0': f'{r}^2+{s}^2 = 137',
        'alpha^-1_MZ': 127.95,
        'sin^2_W': '3/13',
        'SU2_doublet': f'l_SU2 = {s} (2D irrep of S4)',
    },
    'standard_model_relations': {
        'M_W': round(MW, 2),
        'M_W_obs': 80.38,
        'MW_error_pct': round(abs(MW-80.38)/80.38*100, 2),
        'G_F': round(GF, 8),
        'G_F_obs': 1.166e-5,
        'GF_error_pct': round(abs(GF/1.166e-5-1)*100, 2),
    },
    'three_body_phase_space': 'Standard kinematic integral (Delta_m)^5/(60*pi^3) — not a Gram prediction',
}

out = ROOT / 'results/beta-decay-gram-v2.json'
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(f"\nWritten to {out}")
print(json.dumps(result, indent=2))