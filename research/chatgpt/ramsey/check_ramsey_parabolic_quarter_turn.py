#!/usr/bin/env python3
"""Deterministic quarter-turn two-coordinate sources: local-overlap certificate.

Two source Cayley graphs on F_q^2 use D_H={(t,t*t),(-t,-t*t):t in H}
with q prime congruent 2 mod 3; blue uses rho(D_H), rho(x,y)=(-y,x).
A sparse pair carrier is {(a,b): b-a in T} for a rho-invariant orbit union T.

No Ramsey asymptotic lower bound is claimed. The verified statements are
triangle-freeness, bounded codegree, exact quarter-turn equivariance and local
projection-neighborhood overlap bounds for finite primes.
"""
from collections import Counter
from math import log, sqrt, floor, comb


def add(a,b,q):return ((a[0]+b[0])%q,(a[1]+b[1])%q)
def sub(a,b,q):return ((a[0]-b[0])%q,(a[1]-b[1])%q)
def neg(a,q):return ((-a[0])%q,(-a[1])%q)
def rot(a,q):return ((-a[1])%q,a[0]%q)
def rotneg(a,q):return neg(rot(a,q),q)

def source(q,h):
    ds = {(t,(t*t)%q) for t in range(1,h+1)}
    D=ds | {neg(d,q) for d in ds}
    assert len(D)==2*h and (0,0) not in D
    Dblue={rot(v,q) for v in D}
    assert len(Dblue)==len(D)
    assert not any(add(a,b,q) in D for a in D for b in D)
    assert not any(add(a,b,q) in Dblue for a in Dblue for b in Dblue)
    codeg=Counter(sub(a,b,q) for a in D for b in D if a!=b)
    assert max(codeg.values(),default=0)<=6
    return D,Dblue,max(codeg.values(),default=0)

def shifts(q,r):
    seen={(0,0)};orbits=[]
    for x in range(q):
        for y in range(q):
            if (x,y) in seen:continue
            orbit=set(); v=(x,y)
            for _ in range(4):
                orbit.add(v);v=rotneg(v,q)
            assert len(orbit)==4 and v==(x,y)
            seen.update(orbit)
            orbits.append(tuple(sorted(orbit)))
    T={(0,0)}
    for orbit in orbits[:r]:T.update(orbit)
    assert len(T)==1+4*r
    assert {rotneg(t,q) for t in T}==T
    return T

def cross_overlap_max(q,D,Db,T):
    # The cross-projection overlap for two source positions separated by y
    # is #{(a,t,b): a in D, t in T, b in Db, y=a+t-b}.
    count=Counter(sub(add(a,t,q),b,q) for a in D for t in T for b in Db)
    return max(count.values()),sum(count.values())

def pair_loss_slab(q):
    """One explicit K-set stress test; not a proof about all K-sets."""
    a=run(q)
    r=int(log(q)**2)
    T=sorted(shifts(q,r));s=len(T);D,Db,_=source(q,a['source_degree']//2)
    K=int(10*sqrt(a['n']*log(a['n'])))
    U=[(x,y) for x in range(q) for y in range(q)][:((K+s-1)//s)]
    points=[]
    for x in U:
        for t in T:
            if len(points)<K:points.append((x,add(x,t,q)))
    assert len(points)==K and len(set(points))==K
    red=Counter(a for a,b in points)
    blue=Counter(b for a,b in points)
    def loss(counts,deltas):
        N=Counter()
        for a,weight in counts.items():
            for d in deltas:
                N[add(a,d,q)]+=weight
        return sum(z*(z-1)//2 for z in N.values())
    L_R=loss(red,D); L_B=loss(blue,Db)
    return {'q':q,'K':K,'red_loss':L_R,'blue_loss':L_B,
            'total_loss':L_R+L_B,'loss_over_K_squared':(L_R+L_B)/(K*K)}


def run(q):
    r=min(int(log(q)**2),((q*q)-1)//4)
    T=shifts(q,r); s=len(T);n=q*q*s
    h=max(1,min(q-1,int(q*sqrt(log(n)/s)/2)))
    D,Db,c=source(q,h);d=len(D)
    xover,total=cross_overlap_max(q,D,Db,T)
    assert total==d*d*s
    assert xover<=16*s
    assert c*s<=6*s
    assert d*s<=sqrt(n*log(n))+1e-10
    assert s<=log(n)**2+1e-10
    # tau exchanges the two coordinate graphs, and preserves V by orbit closure
    assert {rot(v,q) for v in D}==Db
    assert {rot(v,q) for v in Db}==D
    assert {rotneg(t,q) for t in T}==T
    return dict(q=q, m=q*q, n=n, fiber=s, source_degree=d,
                source_neighborhood=d*s, max_same_overlap=c*s,
                max_cross_overlap=xover,
                theoretical_overlap_bound=16*s,
                paper_neighborhood_scale=sqrt(n*log(n)),
                paper_fiber_scale=log(n)**2)

if __name__=='__main__':
    for q in (5,11,17,23,29):
        print(run(q))
    print('finite slab stress test:',pair_loss_slab(29))
    print('All deterministic local-overlap checks passed.')
