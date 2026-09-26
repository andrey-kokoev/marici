"""Larger carrier: stabilizer Gram eigenvalues and metric signature."""
from itertools import permutations, combinations, product
from pathlib import Path
import json
import hashlib
import numpy as np

ROOT = Path(__file__).resolve().parents[1]

def carrier_automorphisms(points):
    """All permutations of the carrier set."""
    n = len(points)
    return list(permutations(range(n)))

def stabilizer(automs, point_idx):
    """Automorphisms fixing a given point."""
    return [p for p in automs if p[point_idx] == point_idx]

def gram_matrix(elements):
    """Gram matrix of permutation vectors."""
    n = len(elements)
    G = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            G[i, j] = sum(elements[i][k] * elements[j][k] for k in range(len(elements[i])))
    return G

# --- Test 1: 4-point carrier (reference) ---
pts4 = list(range(4))
automs4 = carrier_automorphisms(pts4)
stab4 = stabilizer(automs4, 0)  # stabilizer of point 0
G4 = gram_matrix(stab4)
eig4 = np.sort(np.linalg.eigvalsh(G4))
print("4-point carrier:")
print("  Stabilizer size:", len(stab4))
print(f"  Gram eigenvalues: {[round(ev, 3) for ev in eig4]}")

# The induced action on the 3 remaining points:
induced4 = [tuple(p[1:]) for p in stab4]
G4_ind = gram_matrix(induced4)
eig4_ind = np.sort(np.linalg.eigvalsh(G4_ind))
print(f"  Induced Gram eigenvalues: {[round(ev, 3) for ev in eig4_ind]}")

# --- Test 2: 9-point 3x3 grid carrier (D4 stabilizer only, no full S9 enumeration) ---
pts9 = list(range(9))

def d4_stabilizer_3x3():
    """D4 stabilizer of center in 3x3 grid, as permutations of {0..8}."""
    grid = list(range(9))
    # Map (row, col) -> index
    rc = { (r,c): r*3 + c for r in range(3) for c in range(3) }
    idx_to_rc = {v: k for k, v in rc.items()}
    center = rc[(1,1)]  # index 4
    neighbors = [i for i in range(9) if i != center]
    
    # Rotations: (r,c) -> (c, 2-r), (2-r, 2-c), (2-c, r) for 90, 180, 270
    # Reflections: (r,c) -> (r, 2-c) (vertical), (2-r, c) (horizontal),
    #              (c, r) (diagonal), (2-c, 2-r) (anti-diagonal)
    transformations = []
    # Rotation 0 (identity)
    transformations.append(lambda r, c: (r, c))
    # Rotation 90
    transformations.append(lambda r, c: (c, 2-r))
    # Rotation 180
    transformations.append(lambda r, c: (2-r, 2-c))
    # Rotation 270
    transformations.append(lambda r, c: (2-c, r))
    # Reflection vertical
    transformations.append(lambda r, c: (r, 2-c))
    # Reflection horizontal
    transformations.append(lambda r, c: (2-r, c))
    # Reflection diagonal
    transformations.append(lambda r, c: (c, r))
    # Reflection anti-diagonal
    transformations.append(lambda r, c: (2-c, 2-r))
    
    perms = []
    for tf in transformations:
        perm = list(range(9))
        for idx in range(9):
            r, c = idx_to_rc[idx]
            nr, nc = tf(r, c)
            perm[idx] = rc[(nr, nc)]
        perms.append(tuple(perm))
    return perms

d4 = d4_stabilizer_3x3()
print("\n9-point 3x3 grid:")
print("  D4 stabilizer size:", len(d4))
# Induced action on 8 neighbors
induced_neighbors = [tuple(p[i] for i in range(9) if i != 4) for p in d4]
G_d4 = gram_matrix(induced_neighbors)
eig_d4 = np.sort(np.linalg.eigvalsh(G_d4))
print(f"  D4 induced Gram eigenvalues: {[round(ev, 3) for ev in eig_d4]}")

# --- Test 3: Metric signature from stabilizer Gram ---
# For the 4-point carrier, the stabilizer S3 acts on 3 points.
# The Gram eigenvalues of the S3 action give the "local geometry" at a point.
# If all eigenvalues > 0: Euclidean (+++)
# If one eigenvalue < 0: Lorentzian (++-) 
# If all eigenvalues equal: isotropic (conformal)

# For the 3x3 grid D4 action on 8 neighbors:
# Count positive, negative, zero eigenvalues
pos = np.sum(eig_d4 > 1e-10)
neg = np.sum(eig_d4 < -1e-10)
zero = np.sum(np.abs(eig_d4) < 1e-10)
print(f"\n  Metric signatures: {pos}+, {neg}-, {zero}0")
signature = f"({''.join('+' for _ in range(pos))}{''.join('-' for _ in range(neg))})"
print(f"  Signature: {signature}")

result = {
    'schema': 'marici.nima.machian-metric-larger-carrier.v1',
    'classification': 'stabilizer_gram_signature_depends_on_carrier_geometry_not_imported_from_external_manifold',
    'carrier_4pt': {
        'stabilizer': 'S3 on 3 points (from S4 automorphism group)',
        'induced_gram_eigenvalues': [round(ev, 3) for ev in eig4_ind],
    },
    'carrier_3x3_grid': {
        'stabilizer': 'D4 on 8 neighbors of center',
        'induced_gram_eigenvalues': [round(ev, 3) for ev in eig_d4],
        'signature': signature,
        'positive': int(pos),
        'negative': int(neg),
        'zero': int(zero),
    },
    'finding': 'The stabilizer Gram eigenvalues are determined entirely by the carrier geometry. No external metric is needed.',
    'next': 'Compare with the LP^2 norm on the stabilizer space to see if the Gram matches the spatial metric of a 2D surface.',
}

out = ROOT / 'results/machian-metric-larger-carrier.json'
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result, indent=2))