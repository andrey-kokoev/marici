"""Finite cubic-grid counts and a SUPPLIED Euclidean direction Gram.

Historical filename; this diagnostic constructs no continuum interpolant.
See ../continuum-embedding-evidence-boundary.md. Original code is archived in
../quarantine/20261007-continuum-evidence/checkers/.
"""
from itertools import product
from pathlib import Path
import json
import hashlib
import numpy as np

ROOT = Path(__file__).resolve().parents[1]

def cubic_grid(L):
    """LxLxL cubic grid, returns list of neighbor counts per point."""
    pts = list(range(L**3))
    rc = {i: (i // (L*L), (i // L) % L, i % L) for i in pts}
    
    nbrs = {}
    sym_rank = {}
    for i in pts:
        x, y, z = rc[i]
        count = 0
        sym_k = 0
        # Count neighbors (6 directions in 3D)
        for dx, dy, dz in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
            nx, ny, nz = x+dx, y+dy, z+dz
            if 0 <= nx < L and 0 <= ny < L and 0 <= nz < L:
                count += 1
        nbrs[i] = count
        # Historical variable name: this is just the neighbor count,
        # NOT a computed point stabilizer or symmetry rank.
        if count == 6:
            sym_k = 6  # interior
        elif count == 5:
            sym_k = 5  # face
        elif count == 4:
            sym_k = 4  # edge  
        elif count == 3:
            sym_k = 3  # corner
        sym_rank[i] = sym_k
    return pts, rc, nbrs, sym_rank

# Test for increasing L
for L in [2, 3, 4, 5, 6]:
    pts, rc, nbrs, sym_rank = cubic_grid(L)
    interior = [i for i in pts if nbrs[i] == 6]
    face = [i for i in pts if nbrs[i] == 5]
    edge = [i for i in pts if nbrs[i] == 4]
    corner = [i for i in pts if nbrs[i] == 3]
    
    print(f"L={L}: total={L**3}, interior={len(interior)}, face={len(face)}, edge={len(edge)}, corner={len(corner)}")

# For the 2x2x2 grid (L=2), check if any interior points exist.
# For L=2, every point is a corner (3 neighbors), so no interior.
# For L=3, interior points start appearing (1 center point).

# The six vectors below are prescribed Euclidean directions, not the
# permutation-label vectors computed by check_machian_metric_larger.py.
# Their finite Gram calculation is independent of L once an interior point
# exists. It does not construct a metric interpolant or a convergence map.

# Let's compute it for L=5 (interior exists).
L = 5
pts, rc, _, _ = cubic_grid(L)
interior = [i for i in pts if len([j for j in pts if abs(rc[i][0]-rc[j][0])+abs(rc[i][1]-rc[j][1])+abs(rc[i][2]-rc[j][2])==1]) == 6]
print(f"\nL={L}: {len(interior)} interior points")
if interior:
    i = interior[0]
    x, y, z = rc[i]
    # 6 neighbor direction vectors
    dirs = []
    for dx, dy, dz in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
        nx, ny, nz = x+dx, y+dy, z+dz
        if 0 <= nx < L and 0 <= ny < L and 0 <= nz < L:
            dirs.append((nx, ny, nz))
    # The Gram of the 6 direction vectors (as embedded in 3D Euclidean space)
    vecs = np.array([[dx, dy, dz] for dx, dy, dz in 
                     [(1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)]])
    G = vecs @ vecs.T  # 6x6 Gram matrix
    evals = np.sort(np.linalg.eigvalsh(G))
    print(f"  Direction Gram eigenvalues: {[round(e, 3) for e in evals]}")
    # The 3 larger eigenvalues correspond to the 3 spatial dimensions.
    # Each direction comes with a + and − pair, giving same eigenvalue.
    # So eigenvalues should be [0,0,0,2,2,2] for 3 positive spatial directions.
    # This gives signature (+++).

result = {
    'schema': 'marici.nima.continuum-limit-test.v1',
    'status': 'finite_diagnostic_only',
    'classification': 'finite_grid_counts_and_supplied_euclidean_direction_gram',
    'specific_finding': 'The supplied six axis vectors have a rank-three positive semidefinite Gram. Interior fractions approach one; this is not a metric convergence theorem.',
    'superseding_packet': 'continuum-embedding-evidence-boundary.md',
    'interior_fraction': {str(L): round(len([i for i in range(L**3) if len([j for j in range(L**3) if abs(i//(L*L)-j//(L*L))+abs((i//L)%L-(j//L)%L)+abs(i%L-j%L)==1]) == 6]) / L**3, 4) for L in [2,3,4,5,6]},
    'not_established': 'No stabilizer-to-tangent comparison, metric interpolation, Dirac distribution limit, or continuum constraint algebra is implemented here.',
}

out = ROOT / 'results/continuum-limit-test.json'
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result, indent=2))