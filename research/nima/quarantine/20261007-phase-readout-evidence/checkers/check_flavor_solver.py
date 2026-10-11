"""Solve the fibration phase configuration from Gram numbers."""
from pathlib import Path
import json
import math
import numpy as np

ROOT = Path(__file__).resolve().parents[1]

# Gram structure for the Yukawa matrix (3x3, under S4xS4xS4):
# Diagonal entries = G_same_gen = 1152 (same generation, different S4 type)
# Off-diagonal entries = G_cross_gen = 576 (different generation)
# Phase factor: Y_ij = G_base_ij * exp(i * (phi_j - phi_i))

G_diag = 1152.0
G_off = 576.0

# Mass ratios (from Gram numbers, at the Gram scale):
# y_t : y_c : y_u = 4 : 1 : 1 (base Gram pattern)
# With RG running: amplified to observed
# But we want the phases to produce the correct eigenvalues.

# The observed Yukawa ratios at M_Z (normalized to top = 1):
y_t_obs = 1.0
y_c_obs = 0.007
y_u_obs = 0.000013

# At the Gram scale (before RG), these were:
# y_t(M_Gram) / y_c(M_Gram) = ?
# y_c(M_Gram) / y_u(M_Gram) = ?

# From our flavor hierarchy checker: RG running for up-type = 0.102
# So at the Gram scale: y_c = y_c(M_Z) / 0.102 = 0.007/0.102 = 0.0685
# y_u = y_u(M_Z) / 0.102 = 0.000013/0.102 = 0.000127

# At Gram scale: y_t : y_c : y_u = 1 : 0.0685 : 0.000127
# Or normalized: 1 : 0.069 : 0.00013

# The Gram base eigenvalues are: 2304 : 576 : 576 = 4 : 1 : 1
# We need eigenvalues: 1 : 0.069 : 0.00013

# The fibration phases must split the degenerate 576, 576 into
# 0.069 * 576 = 39.7 and 0.00013 * 576 = 0.075.

# So we need a 3x3 Gram with:
# G = diag(1152) + offdiag(576) with phases
# Having eigenvalues: 2304 (x1), 39.7 (x1), 0.075 (x1)

# The eigenvalues of G depend on the phases:
# For a 3x3 Gram with equal diagonal D and off-diagonal O:
# Eigenvalues: D + O*(eigenvalues of the phase matrix)
# The phase matrix P_ij = exp(i*(phi_j - phi_i))
# Its eigenvalues are real (since it's a unitary transformation)
# Actually, Y = D * I + O * P where P_ij = exp(i*phi_j - i*phi_i)

# The eigenvalues of P are determined by phi_1, phi_2, phi_3.
# For three phases phi = [phi_1, phi_2, phi_3]:
# P is a complex symmetric matrix with all off-diagonals having magnitude 1.
# Its eigenvalues determine the splitting of the degenerate 576, 576 modes.

# Let me set up the numerical solver.

def yukawa_eigenvalues(phi, D=G_diag, O=G_off):
    """Compute Yukawa eigenvalues from fibration phases."""
    Y = np.zeros((3, 3), dtype=complex)
    for i in range(3):
        Y[i, i] = D
        for j in range(3):
            if i != j:
                Y[i, j] = O * complex(math.cos(phi[j] - phi[i]), math.sin(phi[j] - phi[i]))
    # The physical masses come from singular values of Y (not eigenvalues)
    # because Y is not Hermitian (the Yukawa matrix is not Hermitian)
    # The squared masses are eigenvalues of Y @ Y.conj().T
    M_sq = Y @ Y.conj().T
    evals = np.linalg.eigvalsh(M_sq)
    return sorted(np.sqrt(np.maximum(evals, 0)), reverse=True)

def ckm_from_phases(phi_U, phi_D, D=G_diag, O=G_off):
    """Compute CKM matrix from up-type and down-type phases."""
    def gram_evecs(phi):
        Y = np.zeros((3, 3), dtype=complex)
        for i in range(3):
            Y[i, i] = D
            for j in range(3):
                if i != j:
                    Y[i, j] = O * complex(math.cos(phi[j] - phi[i]), math.sin(phi[j] - phi[i]))
        M_sq = Y @ Y.conj().T
        evals, evecs = np.linalg.eigh(M_sq)
        return evecs
    
    V_U = gram_evecs(phi_U)
    V_D = gram_evecs(phi_D)
    CKM = V_U.T.conj() @ V_D
    return CKM

def ckm_angles(phi_U, phi_D):
    """Compute CKM angles and CP phase from phases."""
    V = ckm_from_phases(phi_U, phi_D)
    V_abs = np.abs(V)
    
    # Extract angles
    s13 = V_abs[0, 2]
    if s13 > 1: s13 = 1
    c13 = math.sqrt(1 - s13**2)
    s12 = V_abs[0, 1] / c13
    if s12 > 1: s12 = 1
    s23 = V_abs[1, 2] / c13
    if s23 > 1: s23 = 1
    
    theta12 = math.degrees(math.asin(s12))
    theta23 = math.degrees(math.asin(s23))
    theta13 = math.degrees(math.asin(s13))
    
    # CP phase from Jarlskog
    J = np.imag(V[0,1] * V[1,2] * V[2,0] * np.conj(V[0,2] * V[1,0] * V[2,1]))
    denom = 0.974 * 0.999 * 0.999**2 * 0.225 * 0.041 * 0.0035
    if denom > 0 and abs(J/denom) <= 1:
        delta = math.degrees(math.asin(J/denom))
    else:
        delta = 0
    
    return theta12, theta23, theta13, delta

print("=== Flavor puzzle solver ===")
print("Searching for fibration phases that give the observed flavor structure...")
print()

# Target values (observed at M_Z, scaled to Gram scale):
y_target = [1.0, 0.0685, 0.00013]  # top, charm, up at Gram scale
theta_target = [13.02, 2.35, 0.201]  # CKM angles

# Search over phase space
best = None
best_err = float('inf')

# Phase search: phi_U and phi_D are 3-tuples
# Overall phase cancels: set phi_U_0 = 0
# Free parameters: phi_U_1, phi_U_2, phi_D_1, phi_D_2 (4 d.o.f.)

for pU1 in np.linspace(0, 2*math.pi, 37):  # 10 deg steps
    for pU2 in np.linspace(0, 2*math.pi, 37):
        for pD1 in np.linspace(0, 2*math.pi, 37):
            for pD2 in np.linspace(0, 2*math.pi, 37):
                phi_U = [0, pU1, pU2]
                phi_D = [0, pD1, pD2]
                
                # Get eigenvalues
                evals = yukawa_eigenvalues(phi_U)
                
                # Check if eigenvalues match targets (allow scaling)
                ratio_scale = evals[0] / y_target[0]
                if ratio_scale == 0: continue
                e_norm = [e/ratio_scale for e in evals]
                
                err_mass = sum((e - t)**2 for e, t in zip(e_norm, y_target))
                if err_mass > 100: continue
                
                # Get CKM
                t12, t23, t13, delta = ckm_angles(phi_U, phi_D)
                err_ckm = ((t12 - theta_target[0])**2 + 
                          (t23 - theta_target[1])**2 + 
                          (t13 - theta_target[2])**2)
                
                total_err = err_mass + 0.01 * err_ckm
                if total_err < best_err:
                    best_err = total_err
                    best = (phi_U, phi_D, e_norm, t12, t23, t13, delta)

if best:
    pu, pd, ev, t12, t23, t13, d = best
    print(f"Best fit phases (10 deg scan):")
    print(f"  Up-type: phi_U = [{pu[0]:.2f}, {pu[1]:.2f}, {pu[2]:.2f}] rad")
    print(f"  Down-type: phi_D = [{pd[0]:.2f}, {pd[1]:.2f}, {pd[2]:.2f}] rad")
    print(f"  Yukawa eigenvalues: [{ev[0]:.4f}, {ev[1]:.4f}, {ev[2]:.6f}]")
    print(f"  Target:             [1.0, 0.0685, 0.00013]")
    print(f"  CKM angles: theta12={t12:.2f}, theta23={t23:.2f}, theta13={t13:.3f} deg")
    print(f"  Target:      theta12=13.02, theta23=2.35, theta13=0.201 deg")
    print(f"  CP phase: delta = {d:.1f} deg")
    print(f"  Total error: {best_err:.4f}")
else:
    # Try a finer search around promising regions
    print("No good fit found in coarse scan.")
    print("The flavor puzzle requires a more localized search.")

result = {
    'schema': 'marici.nima.flavor_puzzle_solver.v1',
    'status': 'starting phase search',
}

out = ROOT / 'results/flavor-puzzle-solver.json'
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(f"\n{json.dumps(result, indent=2)}")