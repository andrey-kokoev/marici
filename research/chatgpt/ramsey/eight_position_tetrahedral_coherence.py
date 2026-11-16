#!/usr/bin/env python3
"""Exact integer-chain audit of the eight-position r/s path-coherence model.

The source has eight vertices, r_i:i->i+1 and s_i:i->i+4, with all
16 directed edge OCCURRENCES retained separately. Unlike an undirected
projection, s_{i+4} is NOT silently identified with -s_i.

N_i: r_i r_{i+1} r_{i+2} r_{i+3} => s_i is a *proposed* 2-cell.
U_i: s_i s_{i+4} => empty at i is an extra proposed 2-cell.
There is no assertion that these 2-cells exist in a native source.

After U, Q_i=N_i+N_{i+4}+U_i have common chain boundary C8.
Whiskering makes corresponding 2-morphisms type-correct parallel paths
from r^16 to r^8 based at vertex zero.

The 3/4/5-cell columns below encode formal candidate witnesses, not
actual generated fillers. A zero boundary is a necessary compatibility
condition, never a construction of a higher witness.
"""
from itertools import combinations
from sympy import zeros, Matrix

m=4
n=2*m
V=n
E=2*n
N=n
U=m

def evec(d, j):
    x=zeros(d,1)
    x[j]=1
    return x

# C1 basis: r0..r7, s0..s7 (the eight *directed* s occurrences).
d1=zeros(V,E)
for i in range(n):
    d1[(i+1)%n,i]+=1
    d1[i,i]-=1
    d1[(i+m)%n,n+i]+=1
    d1[i,n+i]-=1

# Each N_i is a distinct pentagonal 2-cell.
d2N=zeros(E,N)
for i in range(n):
    for j in range(m):
        d2N[(i+j)%n,i]+=1
    d2N[n+i,i]-=1

# Each U_i is a distinct witness of s_i s_{i+m} => identity path.
d2U=zeros(E,U)
for i in range(m):
    d2U[n+i,i]+=1
    d2U[n+i+m,i]+=1

d2=d2N.row_join(d2U)
assert d1*d2N==zeros(V,N)
assert d1*d2==zeros(V,N+U)

# Q_i=N_i+N_{i+m}+U_i, all mapping to C8, with common CHAIN boundary.
q=[]
full_r=zeros(E,1)
for i in range(n):full_r[i,0]=1
for i in range(m):
    v=zeros(N+U,1)
    v[i,0]=1
    v[i+m,0]=1
    v[N+i,0]=1
    assert d2*v==full_r
    q.append(v)

# The independent 2-cycles are Z_i=Q_i-Q_0, i=1,2,3.
zs=Matrix.hstack(*[q[i]-q[0] for i in range(1,m)])
assert d2*zs==zeros(E,m-1)
assert zs.rank()==m-1

# Check the globular typing, without treating any word equal to another.
def rotation_word(start, length):
    return tuple(('r', (start+j) % n) for j in range(length))

for i in range(m):
    # Q_i : rotation_word(i,8) => empty_word_i.
    # Left and right whiskering: r^i Q_i r^(8-i), based at 0.
    prefix=rotation_word(0,i)
    suffix=rotation_word(i,n-i)
    top=prefix + rotation_word(i,n) + suffix
    bottom=prefix + suffix
    assert top == rotation_word(0,2*n)
    assert bottom == rotation_word(0,n)
assert rotation_word(0,2*n) != rotation_word(0,n)

# Possible 3-witnesses T_ij: Q_i => Q_j, with boundary Q_j-Q_i.
edges=list(combinations(range(m),2))
d3=Matrix.hstack(*[q[j]-q[i] for i,j in edges])
assert d2*d3==zeros(E,len(edges))

# Possible 4-witnesses on each triangular coherence boundary.
triangles=list(combinations(range(m),3))
d4=zeros(len(edges),len(triangles))
edge_index={e:i for i,e in enumerate(edges)}
for col,(i,j,k) in enumerate(triangles):
    d4[edge_index[(j,k)],col]+=1
    d4[edge_index[(i,k)],col]-=1
    d4[edge_index[(i,j)],col]+=1
assert d3*d4==zeros(N+U,len(triangles))

# The proposed tetrahedral top coherence cell is degree 5, not degree 3.
d5=zeros(len(triangles),1)
for t in range(len(triangles)):
    d5[t,0]=(-1)**t
assert d4*d5==zeros(len(edges),1)

print('8 directed positions, 8 r-arrows, 8 s-arrows')
print('r^4 and s have the same action, different retained words')
print('free N stage: rank(d1)=%d rank(d2_N)=%d H2=%d H1=%d' %
      (d1.rank(),d2N.rank(),N-d2N.rank(),E-d1.rank()-d2N.rank()))
print('with 4 explicit U witnesses: rank(d2)=%d H2=%d H1=%d' %
      (d2.rank(),N+U-d2.rank(),E-d1.rank()-d2.rank()))
print('4 parallel Q_i after reanchoring: 6 comparison pairs')
print('3 independent Q_i-Q_0 2-cycles: rank=%d' % zs.rank())
print('candidate 3-cell boundary rank=%d, 3-cycles=%d' %
      (d3.rank(),len(edges)-d3.rank()))
print('candidate 4-cell boundary rank=%d, 4-cycles=%d' %
      (d4.rank(),len(triangles)-d4.rank()))
print('candidate 5-cell boundary rank=%d' % d5.rank())
print('all squared-boundary identities verified')
print('No 3-, 4-, or 5-cell is implied to exist by these rank calculations.')
