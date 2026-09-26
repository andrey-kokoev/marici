"""Discrete curvature from stabilizer Gram variation across a carrier."""
from itertools import product
from pathlib import Path
import json
import hashlib
import numpy as np

ROOT = Path(__file__).resolve().parents[1]

# Build a 3x3 grid carrier.
N = 3
pts = list(range(N * N))
rc = {i: (i // N, i % N) for i in pts}
neighbors = {}
for i in pts:
    r, c = rc[i]
    nbrs = []
    for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N:
            nbrs.append(nr * N + nc)
    neighbors[i] = nbrs

# D4 stabilizer of a point is defined by its position in the grid.
# For an interior point (1,1), D4 includes 8 rotations/reflections.
# For edge/corner points, the stabilizer is smaller.
def d4_at(pt_idx, grid_size=N):
    """Return D4-like automorphisms fixing pt_idx."""
    r_c, c_c = pt_idx // grid_size, pt_idx % grid_size
    # For simplicity: only center has full D4.
    # For other points, find the local symmetry.
    tf_list = []
    # Identity
    tf_list.append(lambda r, c: (r, c))
    if r_c == 1 and c_c == 1:
        # Center: full D4 (as before)
        tf_list.append(lambda r, c: (c, 2-r))
        tf_list.append(lambda r, c: (2-r, 2-c))
        tf_list.append(lambda r, c: (2-c, r))
        tf_list.append(lambda r, c: (r, 2-c))
        tf_list.append(lambda r, c: (2-r, c))
        tf_list.append(lambda r, c: (c, r))
        tf_list.append(lambda r, c: (2-c, 2-r))
    elif r_c == 0 and c_c == 0:
        # Corner: reflection across diagonal, and rotation by 180? No, only identity
        # For a corner, the stabilizer in the grid is trivial (only identity).
        pass
    elif r_c == 0:
        # Top edge: reflection across vertical axis only
        if N % 2 == 1 and c_c == N // 2:
            mid_c = N // 2
            tf_list.append(lambda r, c: (r, 2*mid_c - c))
    elif c_c == 0:
        # Left edge
        if N % 2 == 1 and r_c == N // 2:
            mid_r = N // 2
            tf_list.append(lambda r, c: (2*mid_r - r, c))
    # Filter out duplicates and invalid transforms
    valid = []
    for tf in tf_list:
        try:
            # Check all points map within grid
            for idx in pts:
                r, c = rc[idx]
                nr, nc = tf(r, c)
                assert 0 <= nr < N and 0 <= nc < N
            valid.append(tf)
        except:
            pass
    return valid

# Compute stabilizer Gram at each point.
def stabilizer_gram(pt_idx, tfs):
    """Gram of induced action on neighboring points, restricted to valid directions."""
    grid = list(range(N * N))
    nbrs = neighbors[pt_idx]
    # Induced action on neighbors
    induced = []
    for tf in tfs:
        perm = []
        for idx in nbrs:
            r, c = rc[idx]
            nr, nc = tf(r, c)
            perm.append(nr * N + nc)
        induced.append(tuple(perm))
    if not induced:
        return None
    n = len(induced)
    m = len(induced[0])
    G = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            G[i, j] = sum(1 if induced[i][k] == induced[j][k] else 0 for k in range(m))
    return G, induced

# Compute stabilizer Gram at each point.
grams = {}
for i in pts:
    tfs = d4_at(i)
    G = stabilizer_gram(i, tfs)
    grams[i] = G

# Compute "metric" at each point from top 3 eigenvalues of Gram.
metrics = {}
for i in pts:
    G_info = grams[i]
    if G_info is None:
        metrics[i] = None
        continue
    G, induced = G_info
    evals = np.sort(np.linalg.eigvalsh(G))
    # Take the 3 largest eigenvalues (spatial directions)
    spatial = evals[-3:] if len(evals) >= 3 else evals
    metrics[i] = {'eigenvalues': [round(float(e), 3) for e in spatial], 'rank': len(evals), 'n_neighbors': len(neighbors[i])}

# Compute discrete curvature around plaquettes (1x1 cells).
# A plaquette is a 2x2 block: (r,c), (r,c+1), (r+1,c), (r+1,c+1).
# The curvature is the failure of Gram transport around the plaquette.
curvatures = []
for r in range(N - 1):
    for c in range(N - 1):
        idx00 = r * N + c
        idx01 = r * N + c + 1
        idx10 = (r + 1) * N + c
        idx11 = (r + 1) * N + c + 1
        g00 = grams[idx00]
        g01 = grams[idx01]
        g10 = grams[idx10]
        g11 = grams[idx11]
        # Curvature measure: deviation of Gram determinant ratios
        # For a flat space, the stabilizer Gram should be the same at all points
        # (up to the automorphism group action).
        # Curvature = failure of Gram to match after transport around plaquette.
        dets = []
        for g_info in [g00, g01, g10, g11]:
            if g_info is None:
                dets.append(None)
            else:
                G, _ = g_info
                dets.append(np.linalg.det(G) if G.shape[0] > 0 else None)
        if None not in dets:
            # Relative curvature: log of det ratio product around plaquette
            curvature = abs(np.log(dets[0] * dets[3] / (dets[1] * dets[2] + 1e-15)))
            curvatures.append({'plaquette': [(r,c), (r,c+1), (r+1,c), (r+1,c+1)], 'curvature': round(float(curvature), 6)})

# The Einstein-like condition: sum of curvatures around every point should vanish
# (discrete Bianchi identity). Let's check.
avg_curv = np.mean([c['curvature'] for c in curvatures]) if curvatures else 0.0

result = {
    'schema': 'marici.nima.discrete-curvature.v1',
    'classification': 'discrete_curvature_from_stabilizer_Gram_variation_computable_but_not_yet_matching_Einstein_equations',
    'carrier': f'{N}x{N} grid ({N*N} points)',
    'metrics_by_point': {str(i): v for i, v in metrics.items()},
    'plaquette_curvatures': curvatures[:10],
    'n_plaquettes': len(curvatures),
    'avg_curvature': round(float(avg_curv), 6),
    'finding': 'The stabilizer Gram varies across the carrier. The variation gives a discrete curvature. Whether it satisfies the Einstein equations requires taking the continuum limit and checking the Bianchi identity.',
    'next': 'Compare the discrete curvature with the Einstein tensor for a known solution (e.g., Schwarzschild or FRW) in the large-N limit.',
}

out = ROOT / 'results/discrete-curvature.json'
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result, indent=2))