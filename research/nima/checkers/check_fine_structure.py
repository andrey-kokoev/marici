"""Compute the fine-structure constant from Gram eigenvalue running."""
from pathlib import Path
import json
import math

ROOT = Path(__file__).resolve().parents[1]

# The S4 Gram gives gauge coupling ratios at the fundamental scale:
# g_1^2 : g_2^2 : g_3^2 = 12 : 4 : 4  (from Gram eigenvalues of U(1), SU(2), SU(3) sectors)
#
# In SM normalization: alpha_i = g_i^2 / (4*pi)
# alpha_i^{-1} = (4*pi) / g_i^2

# The Gram eigenvalue k sets the overall scale at M_Pl
# alpha_i^{-1}(M_Pl) = k * (1 / eigenvalue_i)
# where k is the same for all three couplings

# One-loop RG running: alpha_i^{-1}(M_Z) = alpha_i^{-1}(M_Pl) + (b_i/2*pi) * ln(M_Pl/M_Z)

# SM beta function coefficients (GUT-normalized U(1)):
b1 = 41.0 / 10.0  # 4.1
b2 = -19.0 / 6.0  # -3.167
b3 = -7.0         # -7.0

# Scales:
M_Z = 91.0  # GeV
M_Pl = 1.22e19  # GeV
log_ratio = math.log(M_Pl / M_Z)

# Observed couplings at M_Z (PDG):
alpha1_inv_obs = 59.0
alpha2_inv_obs = 30.0
alpha3_inv_obs = 8.5
alpha_inv_obs = 127.95  # fine-structure constant at M_Z

# Gram eigenvalues:
eig1 = 12  # U(1)
eig2 = 4   # SU(2)
eig3 = 4   # SU(3)

print("=== Fine-structure constant from Gram ===")
print()

# At M_Pl: alpha_i^{-1}(M_Pl) = k / eig_i
# Running to M_Z:
# alpha_i^{-1}(M_Z) = k/eig_i + (b_i/2*pi) * ln(M_Pl/M_Z)

# For SU(3): alpha_3^{-1}(M_Z) = k/4 - 7/(2*pi) * log_ratio = 8.5
# => k = 4 * (8.5 + 7*log_ratio/(2*pi))
k3 = 4 * (alpha3_inv_obs + 7 * log_ratio / (2 * math.pi))

# For SU(2): alpha_2^{-1}(M_Z) = k/4 - 19/(6*2*pi) * log_ratio = 30
k2 = 4 * (alpha2_inv_obs + 19 * log_ratio / (12 * math.pi))

# For U(1): alpha_1^{-1}(M_Z) = k/12 + 41/(10*2*pi) * log_ratio = 59
k1 = 12 * (alpha1_inv_obs - 41 * log_ratio / (20 * math.pi))

print(f"Overall scale k from each coupling:")
print(f"  k from SU(3): k3 = {k3:.2f}")
print(f"  k from SU(2): k2 = {k2:.2f}")
print(f"  k from U(1):  k1 = {k1:.2f}")
print()

# If the Gram gives a SINGLE k for all three, they must be equal.
# They are NOT equal — meaning SM running from M_Pl doesn't give unification.
k_avg = (k1 + k2 + k3) / 3
print(f"Average k = {k_avg:.2f}")
print(f"Disagreement: k1/k2 = {k1/k2:.2f}, k2/k3 = {k2/k3:.2f}")
print()

# Now compute what the Gram PREDICTS for low-energy couplings
# using the average k:
print("=== Predicted couplings at M_Z ===")
pred1 = k_avg / eig1 + b1 * log_ratio / (2 * math.pi)
pred2 = k_avg / eig2 + b2 * log_ratio / (2 * math.pi)
pred3 = k_avg / eig3 + b3 * log_ratio / (2 * math.pi)
print(f"  alpha_1^-1 (U(1)):   pred={pred1:.1f} obs={alpha1_inv_obs}")
print(f"  alpha_2^-1 (SU(2)):  pred={pred2:.1f} obs={alpha2_inv_obs}")
print(f"  alpha_3^-1 (SU(3)):  pred={pred3:.1f} obs={alpha3_inv_obs}")
print()

# The fine-structure constant alpha^-1 = alpha_1^-1 + alpha_2^-1? No...
# 1/alpha = 1/alpha_1 + 1/alpha_2 for electromagnetic coupling?
# Actually: 1/alpha = 1/alpha_2 * sin^2(theta_W) = 1/alpha_1 * cos^2(theta_W)
# where sin^2(theta_W) = alpha/alpha_2

# The Gram ratio: tan^2(theta_W) = alpha_1/alpha_2 = g_1^2/g_2^2 * (3/5 normalization)???
# Actually, sin^2(theta_W) = g_1^2 / (g_1^2 + g_2^2) = 12 / (12 + 4) = 0.75
# So predicted sin^2(theta_W) = 0.75 -> theta_W = 60 degrees
# Observed: sin^2(theta_W) = 0.231 -> theta_W = 28.8 degrees

sin2thW_pred = eig1 / (eig1 + eig2)
sin2thW_obs = 0.231

print("=== Weak mixing angle ===")
print(f"  Predicted sin^2(theta_W) from Gram: {sin2thW_pred:.3f}")
print(f"  Observed sin^2(theta_W):           {sin2thW_obs:.3f}")
print()

# The fine-structure constant from Gram prediction:
# alpha^-1(M_Z) = alpha_2^-1 * sin^2(theta_W)
alpha_inv_pred = pred2 * sin2thW_pred
print(f"  Predicted alpha^-1(M_Z): {alpha_inv_pred:.1f}")
print(f"  Observed alpha^-1(M_Z):  {alpha_inv_obs:.1f}")
print()

# None of this works without SUSY or additional structure.
# Let me check with MSSM beta functions instead.

print("=== Trying with MSSM (SUSY) beta functions ===")
# MSSM beta function coefficients (GUT-normalized):
b1_susy = 33.0 / 5.0  # 6.6
b2_susy = 1.0         # 1.0
b3_susy = -3.0        # -3.0

# With SUSY scale at M_SUSY = 1 TeV, the running splits into SM below M_SUSY
# and MSSM above M_SUSY. Let me approximate with full MSSM running from M_Pl to M_Z.

log_ratio_susy = math.log(M_Pl / 1000)  # M_Z -> M_SUSY = 1 TeV

k1_s = 12 * (alpha1_inv_obs - b1_susy * log_ratio_susy / (2 * math.pi))
k2_s = 4 * (alpha2_inv_obs - b2_susy * log_ratio_susy / (2 * math.pi))
k3_s = 4 * (alpha3_inv_obs - b3_susy * log_ratio_susy / (2 * math.pi))
print(f"  k from SU(3): {k3_s:.1f}")
print(f"  k from SU(2): {k2_s:.1f}")
print(f"  k from U(1):  {k1_s:.1f}")

k_s_avg = (k1_s + k2_s + k3_s) / 3
print(f"  Average k (MSSM): {k_s_avg:.1f}")
print(f"  Disagreement ratio: k1/k2 = {k1_s/k2_s:.2f}")
print()

# With MSSM, the k values are closer but still not equal.
# The Gram ratio 12:4 = 3:1 doesn't match the SUSY unification either.

print("=== Conclusion ===")
print("The Gram eigenvalue ratios (12:4:4) do NOT reproduce the observed")
print("gauge couplings or the fine-structure constant with SM or MSSM running.")
print()
print("The Gram gives tan^2(theta_W) = 3 (theta_W = 60 deg) at the fundamental scale,")
print("while observed is tan^2(theta_W) = 0.30 (theta_W = 28.8 deg).")
print()
print("137 is NOT predicted by the Gram eigenvalue ratios alone.")
print("The gauge couplings require additional structure beyond the")
print("S4 irrep decomposition—possibly Yukawa threshold corrections,")
print("higher-dimensional operator contributions, or a different")
print("identification of the Gram eigenvalues with physical couplings.")
print()

result = {
    'schema': 'marici.nima.fine_structure_from_gram.v1',
    'classification': 'Gram_eigenvalue_ratios_do_not_predict_137_with_SM_or_MSSM_running',
    'Gram_ratio_g1_g2': eig1/eig2,
    'predicted_sin2thW': round(sin2thW_pred, 4),
    'observed_sin2thW': sin2thW_obs,
    'predicted_alpha_inv_at_MZ': round(alpha_inv_pred, 1),
    'observed_alpha_inv_at_MZ': alpha_inv_obs,
    'status': 'The Gram eigenvalue ratio 12:4:4 gives g1^2:g2^2:g3^2 = 3:1:1 at the fundamental scale. This does NOT reproduce the observed low-energy couplings (59:30:8.5) with standard SM or MSSM running. The Gram fixes the UV boundary but the mapping from Gram eigenvalues to gauge couplings requires additional structure. 137 remains unexplained.',
}

out = ROOT / 'results/fine-structure-from-gram.json'
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(f"\n{json.dumps(result, indent=2)}")