"""Exact finite tests for the six-arrow Marici seed, 2026-11-09.

No assumption that the native source supplies triangle 2-cells or green fillers.
The filled R/B cases are explicit conditional extensions.
"""
from collections import defaultdict
from itertools import product, permutations
from fractions import Fraction
from math import gcd

V = ('A','B','C','D')
E = {'AB':('A','B'), 'BC':('B','C'), 'CA':('C','A'),
     'AD':('A','D'), 'DB':('D','B'), 'BA':('B','A')}
RHO = {'A':'B','B':'A','C':'D','D':'C'}
RHO_EDGE = {'AB':'BA','BA':'AB','BC':'AD','AD':'BC','CA':'DB','DB':'CA'}
assert all(E[RHO_EDGE[e]] == (RHO[s],RHO[t]) for e,(s,t) in E.items())
assert all(RHO_EDGE[RHO_EDGE[e]] == e for e in E)
# The only directed graph automorphisms are identity and this reflection.
autos=[]
for seq in permutations(V):
    f=dict(zip(V,seq))
    image_pairs={(f[u],f[v]) for u,v in E.values()}
    if image_pairs==set(E.values()):
        autos.append(f)
assert len(autos)==2
assert any(f==RHO for f in autos)
print('Directed graph automorphisms: 2 (identity and reflection)')

# Exhaustively check all nontrivial two-step diamonds in the seed category.
two_step = defaultdict(list)
for e,(start,mid) in E.items():
    for f,(middle,finish) in E.items():
        if mid == middle:
            two_step[(start,finish)].append((e,f))
assert sum(map(len,two_step.values())) == 10
assert all(len(paths) == 1 for paths in two_step.values())
print('Commuting two-step diamonds with distinct paths: 0')

# Oriented face boundaries in the conditional four-triangle delta-complex.
F = {
 'R': {'AB':1,'BC':1,'CA':1},
 'B': {'AD':1,'DB':1,'BA':1},
 'G1':{'AD':1,'DB':1,'AB':-1},
 'G2':{'BC':1,'CA':1,'BA':-1},
}

def rank(matrix):
    m = [[Fraction(x) for x in row] for row in matrix]
    if not m: return 0
    pivot_row = 0
    for col in range(len(m[0])):
        piv = next((r for r in range(pivot_row,len(m)) if m[r][col]), None)
        if piv is None: continue
        m[pivot_row],m[piv] = m[piv],m[pivot_row]
        pivot = m[pivot_row][col]
        m[pivot_row] = [x/pivot for x in m[pivot_row]]
        for row in range(len(m)):
            if row != pivot_row and m[row][col]:
                factor = m[row][col]
                m[row] = [u-factor*v for u,v in zip(m[row],m[pivot_row])]
        pivot_row += 1
        if pivot_row == len(m): break
    return pivot_row

edges = tuple(E)
vertices = tuple(V)
D1 = [[int(E[e][1] == v) - int(E[e][0] == v) for e in edges] for v in vertices]
assert rank(D1) == 3

def report(faces):
    D2 = [[F[f].get(e,0) for f in faces] for e in edges]
    assert all(sum(D1[v][e] * D2[e][f] for e in range(6))==0
               for v in range(4) for f in range(len(faces)))
    rank2=rank(D2)
    b1=6-rank(D1)-rank2
    b2=len(faces)-rank2
    chi=4-6+len(faces)
    return dict(faces=faces, chi=chi, boundary_rank=rank2,b1=b1,b2=b2)

for faces in ((),('R','B'),('R','B','G1'),('R','B','G1','G2')):
    print('Cellular homology ranks:',report(faces))
assert report(('R','B'))['b1'] == 1
assert report(('R','B','G1'))['b1'] == 0
assert report(('R','B','G1','G2'))['b2'] == 1
# R - B + G1 - G2 = 0 as integral 1-chains.
assert all(F['R'].get(e,0)-F['B'].get(e,0)+F['G1'].get(e,0)-F['G2'].get(e,0)==0 for e in E)
# Every edge has exactly two incident faces. Each vertex link is a connected
# degree-two multigraph, hence a circle; verifies a closed 2-manifold.
assert all(sum(abs(F[f].get(e,0)) for f in F)==2 for e in E)
for v in V:
    incident=[e for e,(s,t) in E.items() if v==s or v==t]
    link=defaultdict(list)
    for f in F:
        involved=[e for e in F[f] if e in incident]
        if involved:
            assert len(involved)==2
            p,q=involved
            link[p].append(q)
            link[q].append(p)
    assert set(link)==set(incident)
    assert all(len(xs)==2 for xs in link.values())
    seen={incident[0]}
    todo=[incident[0]]
    while todo:
        for w in link[todo.pop()]:
            if w not in seen:
                seen.add(w)
                todo.append(w)
    assert seen==set(incident)
print('Four-face completion: every edge in exactly two faces; every vertex link is S1')

# General exact counting theorem for cyclic C_m effects.
# Reflection orbit edge maps: AB=BA=a, BC=AD=b, CA=DB=c.
# R and B flat iff a+b+c=0, then G1=G2=-2a, return=2a.
for m in range(2,10):
    models = 0
    flat = 0
    for a,b,c in product(range(m),repeat=3):
        if (a+b+c)%m: continue
        models += 1
        assert (b+c+a)%m==0
        return_res = (2*a)%m
        green1 = (b+c-a)%m
        green2 = (b+c-a)%m
        assert (green1+return_res)%m == 0
        assert green1 == green2
        flat += green1 == 0
    assert models == m*m
    assert flat == m*gcd(m,2)
    print(f'C{m}: red/blue-flat models {models}, G-flat {flat}, G-obstructed {models-flat}')

# Nonabelian groups: all choices a,b, with c=(ab)^-1, give
# R=abc=1, B=bca=1, G1=G2= a^-2, return=a^2.
class Group:
    def __init__(self, elements,identity,multiply):
        self.elements=list(elements)
        self.identity=identity
        self.mul=multiply
        self.inv={a:next(b for b in elements if multiply(a,b)==identity and multiply(b,a)==identity) for a in elements}

perms=list(permutations(range(3)))
id3=(0,1,2)
def pmul(a,b): return tuple(a[b[i]] for i in range(3))
S3=Group(perms,id3,pmul)

# Q8 as signed basis units; (sign, axis) with axis in 1,i,j,k.
axes=('1','i','j','k')
q_base={
 ('1','1'):(1,'1'),('1','i'):(1,'i'),('1','j'):(1,'j'),('1','k'):(1,'k'),
 ('i','1'):(1,'i'),('j','1'):(1,'j'),('k','1'):(1,'k'),
 ('i','i'):(-1,'1'),('j','j'):(-1,'1'),('k','k'):(-1,'1'),
 ('i','j'):(1,'k'),('j','k'):(1,'i'),('k','i'):(1,'j'),
 ('j','i'):(-1,'k'),('k','j'):(-1,'i'),('i','k'):(-1,'j'),
}
q8=[(sign,axis) for sign in (1,-1) for axis in axes]
def qmul(a,b):
    sign,axis=q_base[(a[1],b[1])]
    return (a[0]*b[0]*sign,axis)
Q8=Group(q8,(1,'1'),qmul)

for name,G in (('S3',S3),('Q8',Q8)):
    nmodels=0
    nflat=0
    for a,b in product(G.elements,repeat=2):
        c=G.inv[G.mul(a,b)]
        assert G.mul(G.mul(a,b),c)==G.identity
        assert G.mul(G.mul(b,c),a)==G.identity
        green=G.mul(G.mul(b,c),G.inv[a])
        assert green==G.inv[G.mul(a,a)]
        nmodels += 1
        nflat += green==G.identity
    inv_count=sum(G.mul(a,a)==G.identity for a in G.elements)
    assert nmodels == len(G.elements)**2
    assert nflat == inv_count*len(G.elements)
    print(f'{name}: red/blue-flat models {nmodels}, G-flat {nflat}, G-obstructed {nmodels-nflat}')

# Q8 source reflection acts as an order-two permutation of labels,
# yet a=i has order 4 and its return/green residue is the central -1.
a=(1,'i'); b=(1,'j'); c=Q8.inv[Q8.mul(a,b)]
assert c == (-1,'k')
assert Q8.mul(a,a)==(-1,'1')
assert Q8.mul(Q8.mul(b,c),Q8.inv[a])==(-1,'1')
assert all(Q8.mul((-1,'1'),q)==Q8.mul(q,(-1,'1')) for q in Q8.elements)
print('Q8 control: a=i, b=j, c=-k; R=B=1, G1=G2=-1, return=-1')
print('All exact checks passed.')
