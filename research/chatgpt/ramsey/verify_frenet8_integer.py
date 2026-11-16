"""Verify an 8-node R(3,4) witness derived from discrete 3D path frames."""
import itertools
import numpy as np
from scipy.spatial.transform import Rotation

P = np.array([
    [5,-1,4], [3,1,-2], [5,11,-4], [-22,5,-6],
    [-18,-5,3], [21,-9,-2], [18,18,5], [7,20,1]
], dtype=float)
N = len(P)
v = np.roll(P, -1, axis=0) - P
T = v / np.linalg.norm(v, axis=1)[:, None]
W = np.cross(np.roll(T, 1, axis=0), T)
W /= np.linalg.norm(W, axis=1)[:,None]
F = np.stack([T, np.cross(W, T), W], axis=2)
q = Rotation.from_matrix(F).as_quat(scalar_first=True)
for i in range(1,N):
    if np.dot(q[i], q[i-1]) < 0: q[i] *= -1
D = q @ q.T
A = D < 0
np.fill_diagonal(A, False)
assert all(D[i,(i+1)%N] > 0 for i in range(N))
assert all(not (A[i,j] and A[j,k] and A[k,i]) for i,j,k in itertools.combinations(range(N),3))
assert all(any(A[i,j] for i,j in itertools.combinations(s,2)) for s in itertools.combinations(range(N),4))
assert all(A[i,j] == (min(j-i, N-(j-i)) in (3,4)) for i,j in itertools.combinations(range(N),2))
print('A-edges:',int(A.sum()/2))
for d in range(1,5):
    values=[D[i,(i+d)%N] for i in range(N)]
    print(f'd={d}, min={min(values):+.6f}, max={max(values):+.6f}')
print('Smallest absolute pairwise inner product:',np.min(np.abs(D[np.triu_indices(N,1)])))
print('Verified: no A-triangles; no B-clique of size 4; all B-cycle edges type B.')
