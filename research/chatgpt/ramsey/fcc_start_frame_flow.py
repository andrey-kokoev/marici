"""Start-anchored deterministic dual flows on the FCC cuboctahedral shell.

Tests the precise relaxation of a global 48-dart successor: the starting
head vertex p is retained as a persistent 12-valued frame parameter.
At seven vertices relative to p, both preferences use an opposite-port
transition; elsewhere red/right uses +1 and blue/left uses -1.

This is a constructed model, NOT a derivation of the seven vertices from
unlabelled FCC incidence, and does NOT encode the 7R/3B word constraint.
"""
from itertools import product, permutations
from math import atan2

V = sorted(v for v in product((-1,0,1), repeat=3) if v.count(0)==1)
vi = {v:i for i,v in enumerate(V)}
def dot(x,y): return sum(a*b for a,b in zip(x,y))
def sub(x,y): return tuple(a-b for a,b in zip(x,y))
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
N={i:[j for j in range(12) if dot(sub(V[i],V[j]),sub(V[i],V[j]))==2] for i in range(12)}
assert all(len(x)==4 for x in N.values())
ORDER={}
for i in range(12):
    normal=V[i]; z=(0,0,1)
    u=tuple(2*r-dot(z,normal)*n for r,n in zip(z,normal))
    w=cross(normal,u)
    ORDER[i]=sorted(N[i],key=lambda j:atan2(dot(sub(V[j],V[i]),w),dot(sub(V[j],V[i]),u)))
DARTS=tuple((i,j) for i in range(12) for j in N[i])
assert len(DARTS)==48

# The proper octahedral rotation group: all signed-coordinate permutations
# of determinant +1.
def parity(t): return (-1)**sum(t[i]>t[j] for i in range(3) for j in range(i+1,3))
ROTATIONS=[]
for t in permutations(range(3)):
    for signs in product((-1,1),repeat=3):
        if parity(t)*signs[0]*signs[1]*signs[2]==1:
            ROTATIONS.append(tuple(vi[tuple(signs[j]*v[t[j]] for j in range(3))] for v in V))
assert len(ROTATIONS)==24

# Half-turn about the axis through +/- (1,1,0).
h=tuple(vi[(v[1],v[0],-v[2])] for v in V)
assert all(h[h[i]]==i for i in range(12))
p0=vi[(1,1,0)]
assert {V[i] for i in range(12) if h[i]==i}=={(1,1,0),(-1,-1,0)}

def transform(seams,rotation): return frozenset(rotation[i] for i in seams)
def step(dart,preferred,seams):
    i,j=dart
    k=ORDER[j].index(i)
    offset=2 if j in seams else (1 if preferred=='R' else -1)
    return (j,ORDER[j][(k+offset)%4])

def cycle(preferred,seams,first):
    out=[];cur=first;seen=set()
    while cur not in seen:
        seen.add(cur);out.append(cur);cur=step(cur,preferred,seams)
    assert cur==first
    return out

# Exhaust the 2^7 subsets invariant under the chosen half-turn, then search
# for a globally covering 48-arrow cycle.
INVARIANT_SEAMS=[]
for mask in range(1<<12):
    S=frozenset(i for i in range(12) if mask>>i&1)
    if transform(S,h)==S:
        INVARIANT_SEAMS.append(S)
assert len(INVARIANT_SEAMS)==128
solutions=[S for S in INVARIANT_SEAMS if len(cycle('R',S,DARTS[0]))==48]
minimum=min(map(len,solutions))
assert minimum==7
assert sum(len(S)==minimum for S in solutions)==4
# Fix a reference template; unlike the generated family, it is NOT canonical.
template=min((S for S in solutions if len(S)==minimum),key=lambda s:tuple(sorted(s)))

# Every rotation sending reference vertex p0 to p gives the SAME seam set,
# because the stabilizer of p0 is {identity, h}, which fixes 'template'.
FRAME={}
for p in range(12):
    candidates=[transform(template,g) for g in ROTATIONS if g[p0]==p]
    assert len(candidates)==2 and candidates[0]==candidates[1]
    FRAME[p]=candidates[0]
assert len(set(FRAME.values()))==12

# 'p' is the head of the *initial* arrow and is retained throughout the walk.
for first in DARTS:
    p=first[1]
    for preference in ('R','B'):
        route=cycle(preference,FRAME[p],first)
        assert len(route)==48 and set(route)==set(DARTS)
        assert step(route[-1],preference,FRAME[p])==first
        assert all(route[i][1]==route[(i+1)%48][0] for i in range(48))

# Covariance: rotate the initial dart and the retained reference vertex,
# and the resulting directed walk rotates accordingly.
for g in ROTATIONS:
    for p in range(12):
        assert transform(FRAME[p],g)==FRAME[g[p]]
        for first in DARTS:
            for preference in ('R','B'):
                left=tuple(g[i] for i in step(first,preference,FRAME[p]))
                right=step(tuple(g[i] for i in first),preference,FRAME[g[p]])
                assert left==right

print('Directed arrows:',len(DARTS))
print('Rotation group size:',len(ROTATIONS))
print('Invariant seam sets examined:',len(INVARIANT_SEAMS))
print('Minimum opposite-port vertices, with half-turn invariance:',minimum)
print('Number of minimum reference templates:',sum(len(S)==minimum for S in solutions))
print('Selected reference vertex:',V[p0])
print('Reference opposite-port vertices:',[V[i] for i in sorted(template)])
print('Distinct start-dependent frames:',len(set(FRAME.values())))
print('Checked starting arrows:',len(DARTS))
print('Checked group preferences:',2)
print('Every walk length:',48)
print('All 24 rotations preserve the start-anchored rule: YES')
