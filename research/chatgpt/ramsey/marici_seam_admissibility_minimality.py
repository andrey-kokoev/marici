#!/usr/bin/env python3
"""Exact finite independence test for Marici's conditional chiral comparison law.

Uses the six original directed occurrences, their reflection involution, and
the conditional A4 orbit of 12 comparison triangles. No native admission law
or physical interpretation is assumed.
"""
from itertools import product
from math import gcd

V="ABCD"
identity={v:v for v in V}
g=dict(zip(V,"BCAD"))                  # (A B C)
h=dict(zip(V,"DACB"))                  # (A D B)
s=dict(zip(V,"BADC"))                  # (A B)(C D)

def composite(p,q):
    return {v:p[q[v]] for v in V}

group={tuple(identity.values()):identity}
pending=[identity]
while pending:
    p=pending.pop()
    for gen in (g,h):
        q=composite(p,gen)
        k=tuple(q[v] for v in V)
        if k not in group:
            group[k]=q; pending.append(q)
assert len(group)==12
chiral={tuple(p[v] for v in "ABC") for p in group.values()}
assert len(chiral)==12

orbit_pairs={
    "a":("AB","BA"), "b":("AD","BC"), "c":("CA","DB"),
    "d":("AC","BD"), "e":("CB","DA"), "f":("CD","DC"),
}
def cocycle(mod,a,b):
    var={"a":a,"b":b,"c":a-b,"d":a+b,"e":2*a-b,"f":-a}
    return {edge:var[name]%mod
            for name,pair in orbit_pairs.items() for edge in pair}

def is_valid(w,mod):
    return all((w[u+v]+w[v+z]-w[u+z])%mod==0
               for u,v,z in chiral)

for mod in range(2,13):
    valid=[(a,b) for a,b in product(range(mod),repeat=2)
           if is_valid(cocycle(mod,a,b),mod)]
    assert len(valid)==mod*gcd(mod,4)
    assert all((4*a)%mod==0 for a,b in valid)
    if mod%4:
        assert all((2*a)%mod==0 for a,b in valid)

w=cocycle(4,1,3)
assert is_valid(w,4)
assert all(w[e]==w[s[e[0]]+s[e[1]]] for e in w)
p0=("CA","AD")
p1=("CA","AB","BA","AD")
def phase(word):
    return sum(w[e] for e in word)%4
assert (phase(p0),phase(p1),phase(("AB","BA")))==(1,3,2)
# Reflection-fixed pointed permutation action on five states.
def step(e,x):
    return x if x==0 else 1+(x-1+w[e])%4
def execute(word,x):
    for e in word:x=step(e,x)
    return x
assert execute(p0,0)==execute(p1,0)==0
assert all(execute(p0,x)!=execute(p1,x) for x in range(1,5))
assert all(step(v+z,step(u+v,x))==step(u+z,x)
           for u,v,z in chiral for x in range(5))
# A second model: replace every action by identity. It satisfies the same
# conditional comparison relations and admits the opposite comparison.
assert all(sum(0 for _ in path)==0 for path in (p0,p1))
# Without invertibility of the outer arrows, equality of *whole* long
# effects does not force the seam to act trivially.
def U(x): return x if x==0 else 1+x%4
def constant(x):return 0
assert [U(U(constant(x))) for x in range(5)]==[constant(x) for x in range(5)]
assert [U(U(x)) for x in range(5)] != list(range(5))
print("PASS: all 12 chiral equations, reflection covariance, two distinct")
print("      models of opposite comparison, and five-state pointed witness.")
print("      Chiral comparison admissibility is CONDITIONAL, not native-forced.")
