"""Find K (chain transfer) that splits the degenerate eigenvalues correctly."""
from pathlib import Path
import json
import math
import numpy as np

ROOT = Path(__file__).resolve().parents[1]

G_diag = 1152.0
G_off = 576.0

# Chain-attenuated eigenvalues depend on K, not on phases (phases are unitary)
# For a chain 1-2-3 with off-diagonals:
# G_12 = G_23 = G_off, G_13 = K * G_off

def eval_chain(K):
    G = np.array([
        [G_diag, G_off, K*G_off],
        [G_off, G_diag, G_off],
        [K*G_off, G_off, G_diag]
    ])
    evals = np.linalg.eigvalsh(G)
    return sorted(evals, reverse=True)

# Target: 4:1:1 pattern (heavy:light:light) = 2304:576:576
# Observed target (Gram scale): 1:0.069:0.00013
# Which means the two light eigenvalues must split from 576 to approximately:
# light1 = 576 * 0.069 / 0.25 = 158.976? No, normalized differently.
# light2 = 576 * 0.00013 / 0.25 = 0.2995

# After eigenvalue splitting: we need the three eigenvalues to be in ratio 1:0.069:0.00013

print("=== Eigenvalues for chain-attenuated Gram ===")
print(f"Diagonal = {G_diag}, Off-diagonal (base) = {G_off}")
print()

for K in [x/100 for x in range(1, 101)]:
    ev = eval_chain(K)
    # Normalize to heavy = 1
    heavy = ev[0]
    if heavy == 0: continue
    e_norm = [e/heavy for e in ev]
    # Check how close the two light eigenvalues are to target
    # The target at Gram scale: medium ~ 0.069, light ~ 0.00013
    # But we need to check if the splitting goes in the right direction
    # medium/light ratio should be ~0.069/0.00013 ≈ 530
    ratio_ml = e_norm[1] / max(e_norm[2], 1e-30)
    if 500 < ratio_ml < 600:
        print(f"K = {K:.2f}: ev = [{ev[0]:.1f}, {ev[1]:.1f}, {ev[2]:.4f}], ratio m/l = {ratio_ml:.1f}")

# Also try different structures: what if G_12, G_13, G_23 are all different?
print("\n=== Full asymmetric off-diagonals ===")
for O12 in [0.1, 0.2, 0.5, 0.8, 1.0]:
    for O13 in [0.01, 0.02, 0.05, 0.1, 0.2]:
        for O23 in [0.1, 0.2, 0.5, 0.8, 1.0]:
            G = np.array([
                [G_diag, O12*G_off, O13*G_off],
                [O12*G_off, G_diag, O23*G_off],
                [O13*G_off, O23*G_off, G_diag]
            ])
            ev = np.linalg.eigvalsh(G)
            heavy = ev[2]
            if heavy == 0: continue
            e_norm = [e/heavy for e in ev]
            # Target: e_norm = [1, 0.069, 0.00013]
            err = (e_norm[2]-1)**2 + (e_norm[1]/0.069-1)**2 + (e_norm[0]/0.00013-1)**2
            if err < 10:
                print(f"O12={O12}, O13={O13}, O23={O23}: ev_norm=[{e_norm[2]:.4f}, {e_norm[1]:.4f}, {e_norm[0]:.6f}], err={err:.2f}")

result = {
    'schema': 'marici.nima.chain_parameter_scan.v1',
}

out = ROOT / 'results/chain-parameter-scan.json'
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(f"\n{json.dumps(result, indent=2)}")