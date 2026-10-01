"""Pointed S4 edge-action extensions of the two specified triangle actions.
Finite compatibility test, not a source-selected physical transport law.
"""
from itertools import permutations, product
from pathlib import Path
import runpy
V=tuple(range(4))
perms=tuple(permutations(V))
I=V
def mul(b,a): return tuple(b[a[i]] for i in V)
def inv(a): return tuple(a.index(i) for i in V)
def chain(*actions):
    result=I
    for a in actions: result=mul(a,result)
    return result

prior=runpy.run_path(str(Path(__file__).with_name('check_seed_cycle_response_transport.py')))
g,h=prior['g'],prior['h']
assert g==(1,2,0,3) and h==(3,0,2,1)
# Slots x=AB,y=BC,z=CA,u=AD,v=DB,w=BA. Each edge maps its
# marked source vertex to target. g,h are global vertex permutations, not
# based-loop pointed fillers: notably g(A)=B and h(A)=D.
ends=((0,1),(1,2),(2,0),(0,3),(3,1),(1,0))
choices=tuple(tuple(p for p in perms if p[s]==t) for s,t in ends)
assert all(len(c)==6 for c in choices)
# Endpoint-compatible A-based closed words MUST fix A. The existing g,h do not.
assert g[0]!=0 and h[0]!=0
assert all(chain(x,y,z)[0]==0 for x,y,z in product(*choices[:3]))
assert all(chain(u,v,w)[0]==0 for u,v,w in product(*choices[3:]))
assert not any(chain(x,y,z)==g for x,y,z in product(*choices[:3]))
assert not any(chain(u,v,w)==h for u,v,w in product(*choices[3:]))
print('OBSTRUCTION: pointed edge transports around an A-based loop fix A; g and h move A.')

# If marked endpoint compatibility is removed, algebraic factorizations exist
# freely: choose x,y,u,v, solve z=g*(y*x)^-1 and w=h*(v*u)^-1.
# Two explicit examples show unfixed AB-BA holonomy, not just coordinate names.
def extend(x,y,u,v):
    z=mul(g,inv(mul(y,x)))
    w=mul(h,inv(mul(v,u)))
    assert chain(x,y,z)==g and chain(u,v,w)==h
    return x,y,z,u,v,w

def swap(a,b):
    p=list(V);p[a],p[b]=p[b],p[a];return tuple(p)
a=extend(I,I,I,I)
b=extend(swap(0,1),I,I,I)
ha=chain(a[0],a[5]); hb=chain(b[0],b[5])
assert ha!=hb
# Conjugacy-invariant fixed-point counts differ, so this freedom cannot be
# eliminated by a base-frame conjugation of the shared-edge loop response.
assert sum(ha[i]==i for i in V)!=sum(hb[i]==i for i in V)
print('CONTROL: unpointed extensions exist, but AB-BA loop responses can differ even up to conjugacy.')
print('Scope: S4 common-carrier adapter with vertex marks; no universal obstruction for arbitrary fibers.')
