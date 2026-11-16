"""Exact 7R/3B ten-window and simultaneous two-cycle test, no lattice.
States are (phase i mod 10, nonzero vector in F_2^2).
"""
from itertools import combinations
from collections import Counter, defaultdict
U = ((1, 1), (0, 1))   # I + (-E12), reduced modulo 2
V = ((1, 0), (1, 1))   # I + E21, reduced modulo 2
S = ((0, 1), (1, 0))   # UVU, reduced modulo 2
I = ((1, 0), (0, 1))
FRAMES = ((1, 0), (0, 1), (1, 1))

def mm(A, B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) % 2
                       for j in range(2)) for i in range(2))

def mv(A, v):
    return tuple(sum(A[i][j]*v[j] for j in range(2)) % 2 for i in range(2))

def monodromy(w):
    P = I
    for x in w: P = mm(V if x == 'B' else U, P)
    return P

def successor(s, w, pref):
    i, v = s
    T = V if w[i] == 'B' else U
    if pref == 'B': T = mm(mm(S, T), S)
    return ((i + 1) % 10, mv(T, v))

def orbit(s, w, pref):
    out=[]
    while s not in out:
        out.append(s)
        s = successor(s, w, pref)
    assert s == out[0], (w, pref, s)
    return out

def matint(w):
    a=((1, -1),(0, 1)); b=((1, 0),(1, 1)); P=((1,0),(0,1))
    for x in w:
        T = b if x=='B' else a
        P=tuple(tuple(sum(T[i][k]*P[k][j] for k in range(2)) for j in range(2)) for i in range(2))
    return P

assert mm(mm(S,U),S) == V and mm(mm(S,V),S) == U
buckets=Counter(); classes=defaultdict(list)
for bs in combinations(range(10), 3):
    w=''.join('B' if j in bs else 'R' for j in range(10))
    if 'BB' in w+w[0]: continue
    m=matint(w); t=m[0][0]+m[1][1]
    buckets[t]+=1
    cyc=min(w[i:]+w[:i] for i in range(10))
    classes[cyc].append(w)
    size=len(orbit((0,(1,0)), w, 'R'))
    assert size == (30 if t==1 else 10), (w,t,size)
    for p in ('R','B'):
        assert all(len(orbit((i,v),w,p))==size for i in range(10) for v in FRAMES)
print('admissible cyclic words:', sum(buckets.values()))
print('integer-matrix traces:', dict(buckets))
print('cyclic word types:',[(x,len(y),sum(matint(x)[i][i] for i in range(2))) for x,y in sorted(classes.items())])

w='BRBRRBRRRR'
assert w.count('R')==7 and w.count('B')==3 and 'BB' not in w+w[0]
P=monodromy(w)
assert mm(mm(P,P),P)==I and P!=I
orbits={p:orbit((0,(1,0)),w,p) for p in ('R','B')}
assert all(len(o)==30 and len(set(o))==30 for o in orbits.values())
assert all(all(sum(w[(i+j)%10]=='B' for j in range(10))==3 for i,_ in o) for o in orbits.values())
assert all(successor(s,w,'R') != successor(s,w,'B') for s in orbits['R'])
print('example word:',w)
print('exact integer monodromy:',matint(w))
print('mod-2 monodromy:',P)
print('full orbit sizes:',{p:len(o) for p,o in orbits.items()})
print('shared vertices:',len(set(orbits['R']) & set(orbits['B'])))
print('shared directed transitions:', sum(successor(s,w,'R')==successor(s,w,'B') for s in orbits['R']))
