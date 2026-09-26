"""Flavor puzzle with chain-attenuated off-diagonals (exponential hierarchy)."""
from pathlib import Path
import json
import math
import numpy as np

ROOT = Path(__file__).resolve().parents[1]

# Gram base values:
G_diag = 1152.0  # same-generation coupling
G_base_off = 576.0  # cross-generation coupling (base)

# The exponential attenuation law from chain composition (Blockworld PDF):
# Effective coupling between gen i and gen j:
# G_ij = G_base_off * K^{|i-j|-1}
# where K < 1 is the chain transfer coefficient.
# For a chain 1-2-3: G_12 = G_base_off, G_23 = G_base_off, G_13 = K * G_base_off

# The value of K determines the hierarchy splitting.
# From the observed mass ratios, K should be approximately:
# y_c / y_t ~ 0.007 (charm/top), y_u / y_c ~ 0.002 (up/charm)
# The ratio y_u/y_c ~ K^2? Or K?

print("=== Chain-attenuated Yukawa matrix ===")
print()

def yukawa_eigenvalues_chain(K, phases, D=G_diag, O=G_base_off):
    """Compute Yukawa eigenvalues with chain-attenuated off-diagonals."""
    Y = np.zeros((3, 3), dtype=complex)
    for i in range(3):
        Y[i, i] = D
    # Chain: gen 1-2-3 with exponential attenuation
    Y[0, 1] = O * complex(math.cos(phases[1] - phases[0]), math.sin(phases[1] - phases[0]))
    Y[1, 0] = O * complex(math.cos(phases[0] - phases[1]), math.sin(phases[0] - phases[1]))
    Y[1, 2] = O * complex(math.cos(phases[2] - phases[1]), math.sin(phases[2] - phases[1]))
    Y[2, 1] = O * complex(math.cos(phases[1] - phases[2]), math.sin(phases[1] - phases[2]))
    # Gen 1-3: attenuated by K
    Y[0, 2] = K * O * complex(math.cos(phases[2] - phases[0]), math.sin(phases[2] - phases[0]))
    Y[2, 0] = K * O * complex(math.cos(phases[0] - phases[2]), math.sin(phases[0] - phases[2]))
    M_sq = Y @ Y.conj().T
    evals = np.linalg.eigvalsh(M_sq)
    return sorted(np.sqrt(np.maximum(evals, 0)), reverse=True)

def ckm_chain(K, phi_U, phi_D):
    """CKM from chain-attenuated Yukawa matrices."""
    def gram_evecs(phases):
        Y = np.zeros((3, 3), dtype=complex)
        for i in range(3):
            Y[i, i] = G_diag
        Y[0, 1] = G_base_off * complex(math.cos(phases[1]-phases[0]), math.sin(phases[1]-phases[0]))
        Y[1, 0] = G_base_off * complex(math.cos(phases[0]-phases[1]), math.sin(phases[0]-phases[1]))
        Y[1, 2] = G_base_off * complex(math.cos(phases[2]-phases[1]), math.sin(phases[2]-phases[1]))
        Y[2, 1] = G_base_off * complex(math.cos(phases[1]-phases[2]), math.sin(phases[1]-phases[2]))
        Y[0, 2] = K * G_base_off * complex(math.cos(phases[2]-phases[0]), math.sin(phases[2]-phases[0]))
        Y[2, 0] = K * G_base_off * complex(math.cos(phases[0]-phases[2]), math.sin(phases[0]-phases[2]))
        M_sq = Y @ Y.conj().T
        evals, evecs = np.linalg.eigh(M_sq)
        return evecs
    
    V_U = gram_evecs(phi_U)
    V_D = gram_evecs(phi_D)
    CKM = V_U.T.conj() @ V_D
    V_abs = np.abs(CKM)
    s13 = min(V_abs[0, 2], 1.0)
    c13 = math.sqrt(1 - s13**2) if s13 < 1 else 1e-10
    s12 = min(V_abs[0, 1] / c13, 1.0)
    s23 = min(V_abs[1, 2] / c13, 1.0)
    return math.degrees(math.asin(s12)), math.degrees(math.asin(s23)), math.degrees(math.asin(s13))

# Search for K and phases that reproduce the observed hierarchy
# Target: y_t:y_c:y_u ~ 1:0.007:0.000013 (at M_Z)
# At Gram scale (before RG): 1:0.069:0.00013 (using RG factor ~0.102)

y_target = [1.0, 0.069, 0.00013]
theta_target = [13.02, 2.35, 0.201]

best = None
best_err = float('inf')

for K in [x/100 for x in range(1, 51)]:  # K from 0.01 to 0.50
    for pU1 in np.linspace(0, 2*math.pi, 19):
        for pU2 in np.linspace(0, 2*math.pi, 19):
            phi_U = [0, pU1, pU2]
            evals = yukawa_eigenvalues_chain(K, phi_U)
            if evals[0] == 0: continue
            scale = evals[0] / y_target[0]
            e_norm = [e/scale for e in evals]
            err_mass = sum((e - t)**2 for e, t in zip(e_norm, y_target))
            if err_mass > 0.1: continue
            
            for pD1 in np.linspace(0, 2*math.pi, 19):
                for pD2 in np.linspace(0, 2*math.pi, 19):
                    phi_D = [0, pD1, pD2]
                    t12, t23, t13 = ckm_chain(K, phi_U, phi_D)
                    err_ckm = (t12-theta_target[0])**2 + (t23-theta_target[1])**2 + (t13-theta_target[2])**2
                    total = err_mass + 0.001 * err_ckm
                    if total < best_err:
                        best_err = total
                        best = (K, phi_U, phi_D, e_norm, t12, t23, t13)

if best:
    K, pu, pd, ev, t12, t23, t13 = best
    print(f"Best fit:")
    print(f"  K (chain transfer) = {K:.2f}")
    print(f"  Up phases = [{pu[0]:.2f}, {pu[1]:.2f}, {pu[2]:.2f}] rad")
    print(f"  Down phases = [{pd[0]:.2f}, {pd[1]:.2f}, {pd[2]:.2f}] rad")
    print(f"  Eigenvalues: [{ev[0]:.4f}, {ev[1]:.6f}, {ev[2]:.8f}]")
    print(f"  Target:      [1.0, 0.069, 0.00013]")
    print(f"  CKM: theta12={t12:.2f}, theta23={t23:.2f}, theta13={t13:.4f} deg")
    print(f"  Target: theta12=13.02, theta23=2.35, theta13=0.201 deg")
    print(f"  Error: {best_err:.6f}")
    
    # Compute RG amplification factor
    print(f"\n  At Gram scale: y_c = {ev[1]:.4f}, y_u = {ev[2]:.6f}")
    print(f"  With RG factor ~0.102:")
    print(f"  y_c(M_Z) ≈ {ev[1]*0.102:.6f} (target 0.007)")
    print(f"  y_u(M_Z) ≈ {ev[2]*0.102:.8f} (target 0.000013)")

result = {
    'schema': 'marici.nima.flavor_chain_attenuation.v1',
    'K': round(K, 4) if best else None,
    'best_error': round(best_err, 6) if best else None,
}

out = ROOT / 'results/flavor-chain-attenuation.json'
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(f"\n{json.dumps(result, indent=2)}")