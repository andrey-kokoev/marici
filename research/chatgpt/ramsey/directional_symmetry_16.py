"""Exact 16-position r/s directional coherence counts.

r(i)=i+1 mod 16; s(i)=i+8 mod 16.
Paths remain distinct words. N_i is a proposed witness r^8 => s at i.
The calculation records boundaries, not the admission of higher witnesses.
"""
from itertools import combinations
from collections import Counter
from sympy import Matrix, zeros
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

n=16
m=n//2
edges={tuple(sorted((i,(i+1)%n))) for i in range(n)}
edges|={tuple(sorted((i,(i+m)%n))) for i in range(m)}
assert len(edges)==24

# Fix canonical orientation for the rim and the eight inversion chords.
# The i-th column is the boundary of N_i : r^8 => s.
M=zeros(n+m,n)
for i in range(n):
    for t in range(m):
        M[(i+t)%n,i]+=1
    M[n+i%m,i] += -1 if i<m else 1
assert M.rank()==9
assert [smith_normal_form(M,domain=ZZ)[i,i] for i in range(9)]==[1]*9

# The cycles Z_i=N_i+N_(i+8)-N_0-N_8 are closed and independent.
Z=zeros(n,m-1)
for j in range(1,m):
    Z[j,j-1]=1
    Z[j+m,j-1]=1
    Z[0,j-1]=-1
    Z[m,j-1]=-1
assert M*Z==zeros(n+m,m-1)
assert Z.rank()==7

# Simple cycle enumerator (canonical orientation-independent representatives).
adj={i:set() for i in range(n)}
for a,b in edges:
    adj[a].add(b); adj[b].add(a)
def simple_cycles(k):
    found=set()
    for start in range(n):
        def walk(path):
            if len(path)==k:
                if start in adj[path[-1]]:
                    seq=tuple(path)
                    rots=[seq[j:]+seq[:j] for j in range(k)]
                    rev=seq[::-1]
                    rots += [rev[j:]+rev[:j] for j in range(k)]
                    found.add(min(rots))
                return
            for v in adj[path[-1]]:
                if v not in path:
                    walk(path+[v])
        walk([start])
    return found
assert len(simple_cycles(3))==0
assert len(simple_cycles(4))==8
nonagons=simple_cycles(9)
assert len(nonagons)==16
assert set(Counter(v for c in nonagons for v in c).values())=={9}

# Independent-set check by exhaustive bitmask search.
def alpha():
    masks=[sum(1<<w for w in adj[i]) for i in range(n)]
    best=0
    def dfs(available, taken):
        nonlocal best
        if taken+available.bit_count()<=best:return
        if not available:
            best=max(best,taken);return
        bit=available&-available
        i=bit.bit_length()-1
        dfs(available & ~bit & ~masks[i], taken+1)
        dfs(available & ~bit, taken)
    dfs((1<<n)-1,0)
    return best
assert alpha()==7
print({'positions':n,'group':'C16','r_edges':16,'s_edges':8,
       'nonagons':len(nonagons),'nonagons_per_position':9,
       'squares':len(simple_cycles(4)),'N_boundary_rank':M.rank(),
       'independent_NN_cycles':Z.rank(),'max_independent_set':alpha()})
