"""Test: is alpha^{-1} = 11^2 + 4^2 + running corrections?"""
from pathlib import Path
import json
import math

ROOT = Path(__file__).resolve().parents[1]

# The conjecture: alpha^{-1}(M_Gram) = 11^2 + 4^2 = 137
# and alpha^{-1}(0) = 137 + running_from_M_Gram_to_zero

alpha_inv_obs = 137.035999084  # observed at zero energy
alpha_inv_at_Z = 127.95  # observed at M_Z

# 11 and 4 from the Gram framework
G_ratio = 11  # G_ii / G_ij = 11!/10! = 11
eig_SU2 = 4   # Gram eigenvalue of SU(2) doublet

conjecture = G_ratio**2 + eig_SU2**2
print("=== Testing: alpha^{-1} = 11^2 + 4^2 ===")
print(f"11^2 + 4^2 = {G_ratio}^2 + {eig_SU2}^2 = {conjecture}")
print(f"Observed alpha^{-1}(0) = {alpha_inv_obs}")
print(f"Difference: {alpha_inv_obs - conjecture:.6f}")
print()

# The difference is 0.035999...
# Could this be QED running from some scale to zero?

# QED running from mu to 0 (one-loop, electron only):
# alpha^{-1}(mu) - alpha^{-1}(0) = (2/(3*pi)) * ln(mu/m_e)
# For delta = 0.036:
delta = alpha_inv_obs - conjecture
ln_factor = delta * 3 * math.pi / 2
mu_over_me = math.exp(ln_factor)
mu_scale = mu_over_me * 0.000511  # in GeV (m_e = 0.511 MeV)

print(f"To get delta = {delta:.6f} from QED running (electron only):")
print(f"  ln(mu/m_e) = {ln_factor:.4f}")
print(f"  mu/m_e = {mu_over_me:.4f}")
print(f"  mu = {mu_scale:.4f} GeV = {mu_scale*1000:.4f} MeV")
print()

# This gives mu ~ 0.62 MeV - way too low for a fundamental scale.
# So the conjecture 137 = 11^2 + 4^2 at a HIGH scale doesn't work
# because the running from high scale to zero is ~9, not ~0.036.

# Check: what if 11^2 + 4^2 = 137 is the value at M_Z?
# Then alpha^{-1}(M_Z) should be 137.
# But observed alpha^{-1}(M_Z) = 127.95, not 137.

diff_at_Z = 127.95 - conjecture
print(f"If 137 is at M_Z:")
print(f"  alpha^{-1}(M_Z) - 137 = {diff_at_Z:.2f}")
print(f"  The observed alpha^{-1}(M_Z) = 127.95 is FAR from 137.")
print()

# Check: what if 11^2 + 4^2 gives the value at which couplings unify?
# Standard GUT: alpha_GUT^{-1} approx 24 at M_GUT approx 2e16 GeV
diff_GUT = conjecture - 24
print(f"If 137 is at GUT scale:")
print(f"  standard alpha_GUT^{-1} approx 24")
print(f"  137 - 24 = {diff_GUT:.0f}")
print(f"  Running from GUT to zero of 113 would require many more")
print(f"  charged particles than the SM contains.")
print()

# So 11^2 + 4^2 = 137 is a number-theoretic coincidence
# but it doesn't match any known scale's alpha^{-1}.

# What about the original idea: alpha_inv = (G_ratio)^2 + (SU2_eig)^2
# at the Gram scale (whereever that is)?

# The Gram scale should be the scale where the Gram eigenvalue structure
# is manifest. This is likely M_Pl (where quantum gravity becomes important).
# At M_Pl, the QED coupling would be very different from 137.

print("=== Summary ===")
print("The identity 137 = 11^2 + 4^2 is exact in the Gram framework.")
print("But 11 and 4 are Gram numbers, not physical coupling values.")
print()
print("alpha^{-1} = 11^2 + 4^2 at the Gram scale would require:")
print("  - Running from Gram scale to zero of only 0.036")
print("  - This implies Gram scale ~ 0.6 MeV (unphysical)")
print()
print("OR: 11^2 + 4^2 is a NUMBER-THEORETIC coincidence, not a")
print("direct prediction of alpha at a specific scale.")
print("The Gram numbers 11 and 4 appear in the group structure,")
print("and 11^2 + 4^2 accidentally equals 137 (the fine-structure"),
print("constant's integer part). This is suggestive but not a")
print("derivation of alpha's value.")

result = {
    'schema': 'marici.nima.test_137_conjecture.v1',
    'classification': '11_sq_plus_4_sq_equals_137_is_numeric_coincidence_not_physical_prediction',
    '11_squared_plus_4_squared': conjecture,
    'alpha_inv_observed': alpha_inv_obs,
    'Gram_scale_from_delta_low_energy_GeV': round(mu_scale, 6),
    'status': 'The identity alpha^{-1} approx 11^2 + 4^2 is numerically exact but does not give the correct RG running from any physical scale. It is a coincidence between the Gram numbers (11 from S12 ratio, 4 from S4 SU(2) eigenvalue) and the fine-structure constant. No derivation of alpha from the Gram framework has been found.',
}

out = ROOT / 'results/test-137-conjecture.json'
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(f"\n{json.dumps(result, indent=2)}")