#!/usr/bin/env python3
"""Finite, source-only axis-family experiment for Paley(13) and R(3,6).

Computes all graph automorphisms, their common permutation centralizer,
all affine order-four frame centers, and all equivariant orbit attachment
choices for orbit lengths 1, 2, 4 with one fixed axis. Does not assume
that an extremal successor must have four new vertices.
"""
from collections import Counter
from itertools import combinations
import networkx as nx
import sympy as sp

N=13
ALL=(1<<N)-1
ADJ=tuple(sum(1<<((v+d)%N) for d in (1,5,8,12)) for v in range(N))

def alpha_dp():
    a=bytearray(1<<N)
    for mask in range(1,len(a)):
        bit=mask&-mask
        v=bit.bit_length()-1
        rest=mask^bit
        a[mask]=max(a[rest],1+a[rest&~ADJ[v]])
    return a
DP=alpha_dp()

def is_independent(s):
    mask=s
    while mask:
        b=mask&-mask;v=b.bit_length()-1;mask^=b
        if ADJ[v]&mask:return False
    return True

INDS=[m for m in range(1<<N) if is_independent(m)]

def sig(m,center=0,mult=5):
    res=0
    while m:
        b=m&-m;v=b.bit_length()-1;m^=b
        res|=1<<((center+mult*(v-center))%N)
    return res

def rot_support(s,q,center=0,mult=5):
    out=[]
    for _ in range(q):
        out.append(s)
        s=sig(s,center,mult)
    assert s==out[0]
    return out

def cycle_options(q):
    """All undirected internal red edge orbits invariant under a q-cycle."""
    if q==1: return [()]
    if q==2: return [(),((0,1),)]
    if q==4:
        pairs=[(i,j) for i in range(q) for j in range(i+1,q)]
        span=[];seen=set()
        for i,j in pairs:
            if (i,j) in seen: continue
            orb=set()
            for shift in range(q):
                a,b=(i+shift)%q,(j+shift)%q
                orb.add(tuple(sorted((a,b))))
            seen|=orb
            span.append(tuple(sorted(orb)))
        out=[]
        for mask in range(1<<len(span)):
            out.append(tuple(sorted(edge for t,orb in enumerate(span) if mask>>t&1 for edge in orb)))
        return out

def validate_attach(columns,edges,limit=5):
    q=len(columns)
    nbr=[0]*q
    for i,j in edges:
        nbr[i]|=1<<j;nbr[j]|=1<<i
    if any((nbr[i]&nbr[j]) for i,j in edges):
        return ('new_red_triangle',None)
    if any(columns[i]&columns[j] for i,j in edges):
        return ('mixed_red_triangle',None)
    best=0
    for j in range(1<<q):
        if any(j>>v&1 and nbr[v]&j for v in range(q)):
            continue
        omit=0
        for v in range(q):
            if j>>v&1: omit|=columns[v]
        best=max(best,j.bit_count()+DP[ALL&~omit])
    if best>limit:return ('blue_clique',best)
    return ('valid',best)

def auts():
    G=nx.Graph()
    G.add_nodes_from(range(N))
    G.add_edges_from((i,j) for i in range(N) for j in range(i+1,N) if ADJ[i]>>j&1)
    a=list(nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter())
    assert len(a)==52
    def ord_perm(p):
        t=list(range(N));m=0
        while True:
            m+=1;t=[p[x] for x in t]
            if t==list(range(N)):return m
    order_counts=Counter(map(ord_perm,a))
    assert order_counts==Counter({4:26,2:13,13:12,1:1})
    center_counts=Counter(next(i for i in range(N) if p[i]==i) for p in a if ord_perm(p)==4)
    assert len(center_counts)==13 and set(center_counts.values())=={2}
    centralizer=[p for p in a if all(all(p[q[i]]==q[p[i]] for i in range(N)) for q in a)]
    assert len(centralizer)==1
    affine=[tuple((shift+m*i)%N for i in range(N)) for shift in range(N) for m in (1,5,12,8)]
    assert {tuple(p[i] for i in range(N)) for p in a}==set(affine)
    return order_counts,center_counts,len(centralizer)

def run():
    print('n=13 | edges=',sum(m.bit_count() for m in ADJ)//2,'alpha=',DP[ALL],'independent neighborhoods=',len(INDS))
    orders,centers,c=auts()
    print('Automorphism orders=',dict(sorted(orders.items())))
    print('Distinct quarter-turn centers=',len(centers),'centralizer size=',c)
    for q,mult in ((1,1),(2,12),(4,5)):
        counts=Counter(); winners=[]
        for s in INDS:
            cols=rot_support(s,q,mult=mult)
            for edges in cycle_options(q):
                result,alpha=validate_attach(cols,edges)
                counts[(len(edges),result)]+=1
                if result=='valid':winners.append((s,edges,alpha))
        print('orbit length',q,'tested',len(INDS)*len(cycle_options(q)),
              'valid',len(winners),'internal patterns',len(cycle_options(q)))
        print('  valid by internal red edge count:',dict(sorted(Counter(len(e) for _,e,_ in winners).items())))
        print('  valid alpha values:',dict(sorted(Counter(a for _,_,a in winners).items())))
        if q==4:
            expected={sum(1<<i for i in s) for s in ((1,7,11),(3,5,9),(2,6,12),(4,8,10))}
            assert {s for s,_,_ in winners}==expected
            assert all(len(e)==4 and a==5 for _,e,a in winners)
        if q==1:
            assert len(winners)==len(INDS)
    # Verify frame-independence of all 13 choices directly.
    good=0
    for center in range(N):
        win=[]
        for s in INDS:
            cols=rot_support(s,4,center=center,mult=5)
            k,al=validate_attach(cols,((0,1),(1,2),(2,3),(0,3)))
            if k=='valid':win.append(s)
        assert len(win)==4
        good+=len(win)
    assert good==52
    mat=sp.Matrix([[int((ADJ[i]>>j)&1) for j in range(N)] for i in range(N)])
    t=sp.symbols('t')
    cp=sp.factor(mat.charpoly(t).as_expr())
    assert cp==(t-4)*(t**3+t**2-4*t+1)**4
    assert (mat**4-3*mat**3-8*mat**2+17*mat-4*sp.eye(N))==sp.zeros(N)
    print('Characteristic polynomial:',cp)
    print('Across all 13 frame centers: 52 valid labeled seeds; 4 per center.')
    print('PASS')

if __name__=='__main__':run()
