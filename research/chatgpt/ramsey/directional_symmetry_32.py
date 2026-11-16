"""Exact finite combinatorial checks of 32-position r/s symmetry model.

Paths are retained as formal words. N_i is a proposed 2-cell with boundary
r_i+...+r_(i+15) - s_i. s_(i+16) = -s_i in oriented 1-chains.
"""
from collections import Counter
from sympy import Matrix
from scipy.optimize import milp, Bounds, LinearConstraint
import numpy as np

N = 32
M = N // 2
vertices = range(N)
rotation_edges = {frozenset((i, (i+1)%N)) for i in vertices}
inversion_edges = {frozenset((i, (i+M)%N)) for i in vertices}
undirected_edges = rotation_edges | inversion_edges
assert len(rotation_edges) == 32 and len(inversion_edges) == 16
assert len(undirected_edges) == 48

# Formal oriented edge basis consists of all cyclic r_i (i->i+1),
# plus s_i (i->i+16) for i=0..15.
def edge_coordinates(i):
    if i<M:
        return (i, 1)
    return (i-M, -1)

boundary_columns = []
for i in vertices:
    col = [0]*(N+M)
    for j in range(M):
        col[(i+j)%N] += 1
    index, sign = edge_coordinates(i)
    col[N+index] -= sign
    boundary_columns.append(col)
B = Matrix.hstack(*(Matrix(col) for col in boundary_columns))
assert B.rank() == 17

rotation_cycle = Matrix([1]*N + [0]*M)
for i in range(M):
    assert B[:, i] + B[:, i+M] == rotation_cycle
for j in range(1,M):
    z = Matrix([int(i in (j,j+M))-int(i in (0,M)) for i in vertices])
    assert B*z == Matrix.zeros(N+M,1)

# Each distinguished polygon N_i visits M+1 distinct nodes.
incidences = Counter()
for i in vertices:
    for j in range(M+1):
        incidences[(i+j)%N] += 1
assert set(incidences.values()) == {17}

squares = {frozenset((i,(i+1)%N,(i+M)%N,(i+M+1)%N)) for i in vertices}
assert len(squares) == 16

# Triangle-free check.
edge_lookup = {tuple(sorted(edge)) for edge in undirected_edges}
def adjacent(a,b): return tuple(sorted((a,b))) in edge_lookup
triangles = [(a,b,c) for a in vertices for b in range(a+1,N) for c in range(b+1,N) if adjacent(a,b) and adjacent(b,c) and adjacent(a,c)]
assert len(triangles) == 0

# Integer-programming certificate for alpha(G)=15: maximize sum x_i,
# with x_u + x_v <= 1 for every edge.
A = np.zeros((len(undirected_edges), N))
for row, e in enumerate(undirected_edges):
    for v in e: A[row,v] = 1
result = milp(c=-np.ones(N),integrality=np.ones(N),bounds=Bounds(0,1),constraints=LinearConstraint(A,-np.inf,np.ones(len(undirected_edges))),options={'mip_rel_gap':0})
assert result.success
alpha = int(round(-result.fun))
assert alpha == 15, alpha
# Verify explicit witness too.
independent = [i for i,v in enumerate(result.x) if v > .5]
assert len(independent) == alpha
assert all(not adjacent(a,b) for i,a in enumerate(independent) for b in independent[i+1:])

print({'positions': N,
       'undirected_edges': len(undirected_edges),
       'distinguished_N_boundaries': N,
       'N_per_node': next(iter(incidences.values())),
       'coherence_boundary_edges': M+1,
       'distinct_squares': len(squares),
       'N_boundary_matrix_rank_Q': B.rank(),
       'independent_NN_cycles': N-B.rank(),
       'graph_cycle_rank': len(undirected_edges)-N+1,
       'triangles': len(triangles),
       'independence_number': alpha,
       'maximum_independent_set_witness': independent})
