"""Exact finite checks for an R(3,5) sign witness and 3D Frenet-frame compatibility.
Requires numpy and scipy.  No optimization or Ramsey-number lookup is used.
"""
import itertools
import numpy as np
from scipy.spatial.transform import Rotation

N = 13
j = np.arange(N)
# The B traversal is 0,1,...,12,0. Its A edges have distances 4 and 6.
q = np.column_stack([
    np.cos(16*np.pi*j/N), np.sin(16*np.pi*j/N),
    np.cos(24*np.pi*j/N), np.sin(24*np.pi*j/N),
]) / np.sqrt(2)
inner = q @ q.T
edges = inner < -1e-10
np.fill_diagonal(edges, False)
assert np.min(np.abs(inner[np.triu_indices(N, 1)])) > 0.06
assert all(edges[i, k] == (min((k-i) % N, (i-k) % N) in (4, 6))
           for i, k in itertools.combinations(range(N), 2))
triangles = [s for s in itertools.combinations(range(N), 3)
             if all(edges[i, k] for i,k in itertools.combinations(s, 2))]
independent_fives = [s for s in itertools.combinations(range(N), 5)
                     if not any(edges[i,k] for i,k in itertools.combinations(s, 2))]
assert len(triangles) == len(independent_fives) == 0
assert all(inner[i, (i+1)%N] > 0 for i in range(N))

frames = Rotation.from_quat(q, scalar_first=True).as_matrix()
tangents = frames[:, :, 0]
binormals = frames[:, :, 2]
cross = np.cross(np.roll(tangents, 1, axis=0), tangents)
scaled = cross / np.linalg.norm(cross, axis=1)[:,None]
# For actual discrete Frenet frames, binormals would equal scaled, all 13 nodes.
perp_failure = np.einsum('ij,ij->i',binormals,np.roll(tangents,1,axis=0))
frame_error = np.linalg.norm(binormals-scaled,axis=1)
# With unit segment lengths, the tangents do make a closed polygon.
p = np.vstack([np.zeros(3),np.cumsum(tangents,axis=0)])
dists = np.linalg.norm(p[:N,None,:]-p[None,:N,:],axis=2)
np.fill_diagonal(dists,np.inf)

print('N:',N)
print('A connections:', np.count_nonzero(np.triu(edges,1)))
print('A triangles:',len(triangles),'B independent fives:',len(independent_fives))
print('Minimum abs pairwise quaternion dot:', np.min(np.abs(inner[np.triu_indices(N,1)])))
print('Minimum B-cycle quaternion dot:', min(inner[i,(i+1)%N] for i in range(N)))
print('Closed polygon displacement error:', np.linalg.norm(p[-1]-p[0]))
print('Minimum distinct polygon vertex distance:', np.min(dists))
print('Nodes failing binormal orthogonality:', np.count_nonzero(np.abs(perp_failure)>1e-8))
print('Nodes failing complete Frenet frame condition:',np.count_nonzero(frame_error>1e-8))
assert np.linalg.norm(p[-1]-p[0])<1e-10
assert np.min(dists)>0.2
assert np.count_nonzero(np.abs(perp_failure)>1e-8)==12
assert np.count_nonzero(frame_error>1e-8)==13
print('Verified: Ramsey-critical sign graph and positional closure, but not Frenet-frame compatibility.')
