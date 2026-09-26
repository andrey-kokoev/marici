"""Hierarchical mass spectrum and CKM mixing from Gram misalignment."""
from pathlib import Path
import json
import hashlib
import numpy as np

ROOT = Path(__file__).resolve().parents[1]

# CKM matrix from misalignment of up-type and down-type mass eigenbases.
# Both sectors live on the 3 quark points {1,2,3} with S3-broken Gram.
# Up-type masses: hierarchical (top ~ 1, charm ~ 0.004, up ~ 3e-5)
# Down-type masses: also hierarchical (bottom ~ 1, strange ~ 0.02, down ~ 0.001)
# The off-diagonal mixing parameter delta is the same for both sectors.

delta = 0.02
beta_up = [1.0, 0.004, 0.00003]
beta_down = [1.0, 0.02, 0.001]

def gram_3pt(beta, delta):
    G = np.zeros((3, 3))
    for i in range(3):
        G[i, i] = beta[i]
        for j in range(3):
            if i != j:
                G[i, j] = delta
    return G

G_up = gram_3pt(beta_up, delta)
G_down = gram_3pt(beta_down, delta)

evals_up, evecs_up = np.linalg.eigh(G_up)
evals_down, evecs_down = np.linalg.eigh(G_down)

idx_up = np.argsort(evals_up)[::-1]
evecs_up_s = evecs_up[:, idx_up]
idx_down = np.argsort(evals_down)[::-1]
evecs_down_s = evecs_down[:, idx_down]

V = evecs_up_s.T @ evecs_down_s
for col in range(3):
    mi = np.argmax(np.abs(V[:, col]))
    V[:, col] *= np.sign(V[mi, col])
if np.linalg.det(V) < 0:
    V[:, 0] *= -1

print("Up eigenvalues:", np.sort(evals_up)[::-1])
print("Down eigenvalues:", np.sort(evals_down)[::-1])
print("\nCKM (absolute):")
print(np.round(np.abs(V), 4))

s12 = np.abs(V[0, 1])
s23 = np.abs(V[1, 2])
s13 = np.abs(V[0, 2])
t12 = np.degrees(np.arcsin(min(s12, 0.999)))
t23 = np.degrees(np.arcsin(min(s23, 0.999)))
t13 = np.degrees(np.arcsin(min(s13, 0.999)))

print(f"\ntheta12 = {t12:.2f} deg (SM ~13.0)")
print(f"theta23 = {t23:.2f} deg (SM ~2.4)")
print(f"theta13 = {t13:.2f} deg (SM ~0.2)")

sm = [[0.974, 0.225, 0.0035],
      [0.225, 0.973, 0.041],
      [0.009, 0.040, 0.999]]
print("\nSM reference:")
print(np.round(sm, 4))

result = {
    'schema': 'marici.nima.mass-diagonalization.v1',
    'classification': 'CKM_from_Gram_misalignment',
    'up_masses': [round(float(e), 6) for e in np.sort(evals_up)[::-1]],
    'down_masses': [round(float(e), 6) for e in np.sort(evals_down)[::-1]],
    'CKM': [[round(float(np.abs(V[i,j])), 6) for j in range(3)] for i in range(3)],
    'angles_deg': [round(t12, 2), round(t23, 2), round(t13, 2)],
    'sm_angles': [13.0, 2.4, 0.2],
    'open': 'Parameters delta=0.02 and mass ratios are not yet derived from carrier geometry.',
}

out = ROOT / 'results/mass-diagonalization.json'
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result, indent=2))