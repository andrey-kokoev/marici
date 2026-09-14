#!/usr/bin/env python3
"""Branch C: typed endpoint/Gysin pullback and relative-operation tests.

Standalone Python 3.10+, integer and polynomial arithmetic only.
Reconstructs the actual 215-state target, complete endpoint Gysin source
Hom complexes, source comparisons, and a native mixed-operation test.
Does not assert a physical bimodule/collar comparison has been constructed.
"""
from __future__ import annotations
import argparse, ast, hashlib, json
from pathlib import Path
from collections import Counter, defaultdict, deque
from itertools import combinations, product
from functools import lru_cache

COMMIT='d1947b67a60d3e88ba77f4ca60ea02c2a306ee61'
NV=18; ZERO=(0,)*NV; COUNT=Counter()
EV=(0,2,4); OD=(1,3,5); ORDER=EV+OD
def check(ok,tag):
    if not ok:raise AssertionError(tag)
    COUNT[tag]+=1

def pm(n):return -1 if n%2 else 1

def subsets(s):return [v for k in range(len(s)+1) for v in combinations(s,k)]

def ex(es):return tuple(es.get(i,0) for i in range(NV))

def ea(a,b):return tuple(x+y for x,y in zip(a,b))

def es(a,b):return tuple(x-y for x,y in zip(a,b))

def add(*vs):
    out={}
    for v in vs:
        for k,c in v.items():
            out[k]=out.get(k,0)+c
            if not out[k]:del out[k]
    return out

def scale(v,c):return {k:c*a for k,a in v.items() if c*a}

def mul(v,e,c=1):return {(b,ea(m,e)):c*a for (b,m),a in v.items() if c*a}

def apply(d,v):
    out={}
    for (b,e),c in v.items():out=add(out,mul(d.get(b,{}),e,c))
    return out

def lin(d,v):
    out={}
    for b,c in v.items():out=add(out,scale(d.get(b,{}),c))
    return out

def one(b):return {(b,ZERO):1}

def wedge(a,b):
    if set(a)&set(b):return None,0
    return tuple(sorted(a+b)),pm(sum(i>j for i in a for j in b))

def koszul(equations,weights=None):
    if weights is None:weights=equations
    g={};d={};wt={}
    for s in subsets(tuple(range(len(equations)))):
        g[s]=len(s);w=ZERO
        for i in s:w=ea(w,weights[i])
        wt[s]=w
        d[s]={(s[:j]+s[j+1:],equations[i]):pm(j)
              for j,i in enumerate(s) if equations[i] is not None}
    return g,d,wt

def tensor_d(left_g,left_d,right):
    g={};d={}
    for a,n in left_g.items():
        for s,k in right[0].items():
            b=(a,s);g[b]=n+k
            z={((aa,s),e):c for (aa,e),c in left_d[a].items()}
            z=add(z,{((a,ss),e):pm(n)*c for (ss,e),c in right[1][s].items()})
            d[b]=z
    return g,d

def fast_reduce(g, original, vectors=()):
    d={x:dict(v) for x,v in original.items()}; incoming=defaultdict(dict); queue=deque()
    for s,vec in d.items():
        for a,c in vec.items():
            incoming[a][s]=c
            if abs(c)==1:queue.append((s,a))
    vs=[dict(v) for v in vectors]; steps=0
    while queue:
        b,a=queue.popleft()
        if b not in d or a not in d:continue
        c=d[b].get(a,0)
        if abs(c)!=1:continue
        check(g[b]==g[a]+1,'class_test_pivot_degree')
        tail={x:-c*v for x,v in d[b].items() if x!=a}
        sources=(set(incoming[a])|set(incoming[b]))-{a,b}
        for s in sources:
            old=d[s];ca=old.get(a,0)
            new={y:v for y,v in old.items() if y not in (a,b)}
            if ca:
                for y,v in tail.items():
                    new[y]=new.get(y,0)+ca*v
                    if not new[y]:del new[y]
            for y in old:incoming[y].pop(s,None)
            d[s]=new
            for y,v in new.items():
                incoming[y][s]=v
                if abs(v)==1:queue.append((s,y))
        for s in (a,b):
            for y in d[s]:incoming[y].pop(s,None)
            del d[s]
        incoming.pop(a,None);incoming.pop(b,None)
        for v in vs:
            va=v.pop(a,0);v.pop(b,None)
            if va:
                for y,c0 in tail.items():
                    v[y]=v.get(y,0)+va*c0
                    if not v[y]:del v[y]
        steps+=1
    check(not any(d.values()),'class_test_no_nonunit_residue')
    return dict(sorted(Counter(g[x] for x in d).items())),vs,steps

def diag(i,j):return tuple(sorted((i%6,j%6)))

def cross(a,b):
    x,y=a;u,v=b
    return x<u<y<v or u<x<v<y

def cell_degree(c):return 3-len(c[0])+len(c[1])

def graph_exp(e):
    out=list(e)
    for i in range(6):out[i]+=out[9+i]
    return tuple(out)

def target_boundary(c):
    f,h=c;out={}
    for a in DS:
        if a not in f and all(not cross(a,b) for b in f):
            t=(tuple(sorted(f+(a,))),h)
            out[t,graph_exp(ex({IX[a]:1,9+IX[a]:-1}))]=pm(sum(b<a for b in f))
    for j,a in enumerate(h):out[(f,tuple(b for b in h if b!=a)),ZERO]=pm(3-len(f)+j)
    return out

def target_legal(c,e):
    local={IX[a] for a in c[0] if a not in c[1]}
    return all(e[i]>=0 or i in local for i in range(6)) and all(e[i]>=0 for i in range(6,9)) and all(e[9+i]>=0 or i in local for i in range(9))

def target_side(cell):
    if cell[0] in (VP,VM):return 'V'
    return 'B' if any(a in SHORT for a in cell[0]) else 'Q'

def target_weight(cell):
    e=ZERO
    for a in cell[0]:e=ea(e,ex({IX[a]:-1,9+IX[a]:1}))
    return graph_exp(e)

def bare_allowed(cell, e, center=()):
    local={IX[a] for a in cell[0] if a not in cell[1]}
    if set(center)&local:return False
    if any(e[9+i] for i in center):return False
    return target_legal(cell,e)

def bare_model():
    return ({c:cell_degree(c) for c in CELLS},BD,{c:target_weight(c) for c in CELLS})

def bare_hom(S,lam,center=()):
    W=bare_model();g={};cf={};d={}
    targets=[t for t in W[0] if bare_allowed(t,ZERO,center)]
    for a,da in S[0].items():
        alpha=ea(S[2][a],lam)
        for t in targets:
            e=es(alpha,W[2][t])
            if bare_allowed(t,e,center):g[a,t]=W[0][t]-da;cf[a,t]=e
    inc={a:[] for a in S[0]}
    for a,terms in S[1].items():
        for (aa,e),v in terms.items():inc[aa].append((a,e,v))
    for (a,t),n in g.items():
        value={};ee=cf[a,t]
        for (tt,e),v in W[1][t].items():
            ef=ea(ee,e);y=a,tt
            if bare_allowed(tt,ef,center):
                check(y in cf and cf[y]==ef,'bare_Hom_target_degree_and_domain')
                value[y]=value.get(y,0)+v
        for aa,e,v in inc[a]:
            ef=ea(ee,e);y=aa,t
            if bare_allowed(t,ef,center):
                check(y in cf and cf[y]==ef,'bare_Hom_source_degree_and_domain')
                value[y]=value.get(y,0)-pm(n)*v
        d[a,t]={y:v for y,v in value.items() if v}
    for a in g:check(not lin(d,d[a]),'bare_complete_Hom_d_squared')
    return g,d,cf

def bare_section(g,d,kind):
    def keep(key):
        side=target_side(key[1])
        return kind=='K' or (kind=='E' and side!='V') or (kind=='Q' and side=='Q') or (kind=='B' and side!='Q') or (kind=='V' and side=='V')
    gg={a:n for a,n in g.items() if keep(a)}
    dd={a:{b:v for b,v in d[a].items() if b in gg} for a in gg}
    return gg,dd

def bare_vector(table,cf,keys):
    vec={}
    for a,terms in table.items():
        for (t,e),v in terms.items():
            if (a,t) in keys:
                check(cf[a,t]==e,'bare_class_exact_fine_degree')
                vec[a,t]=vec.get((a,t),0)+v
    return {x:v for x,v in vec.items() if v}

def omega(t):
    f=tuple(sorted(SHORT[i] for i in t))
    if f not in FACES:return {}
    e=ea(GAMMA,ex({9+i:-1 for i in t}));z={((f,()),e):1}
    for l in LONG:
        if all(not cross(l,b) for b in f):
            c=(tuple(sorted(f+(l,))),(l,));m=ea(e,ex({IX[l]:1,9+IX[l]:-1}))
            z[c,m]=-pm(sum(b>l for b in f))
    return z

DS=tuple((i,j) for i in range(6) for j in range(i+1,6) if j-i not in (1,5))
SHORT=tuple(diag(i,i+2) for i in range(6)); LONG=tuple(diag(i,i+3) for i in range(3))
IX={a:i for i,a in enumerate(SHORT+LONG)}
FACES=tuple(f for k in range(4) for f in combinations(DS,k) if all(not cross(a,b) for a,b in combinations(f,2)))
CELLS=tuple((f,h) for f in FACES for h in subsets(f))
VP=tuple(sorted(SHORT[i] for i in OD)); VM=tuple(sorted(SHORT[i] for i in EV))
GAMMA=ex({15:1,16:1,17:1})
BD={c:target_boundary(c) for c in CELLS}

BARE_MAP_DATA = [{'input': '(0, 2, 4, 6)', 'terms': [{'target': '(((1, 3), (1, 5), (3, 5)), ())', 'coefficient': 1, 'exponents': [0, -1, 0, -1, 0, -1, 0, 0, 0, 0, -1, 0, -1, 0, -1, 1, 1, 1]}]}, {'input': '(1, 3, 5, 6)', 'terms': [{'target': '(((0, 2), (0, 4), (2, 4)), ())', 'coefficient': -1, 'exponents': [-1, 0, -1, 0, -1, 0, 0, 0, 0, -1, 0, -1, 0, -1, 0, 1, 1, 1]}]}, {'input': '(0, 1, 2, 4, 6)', 'terms': [{'target': '(((1, 5), (2, 5), (3, 5)), ((2, 5),))', 'coefficient': -1, 'exponents': [0, 0, 0, -1, 0, -1, 0, 0, 1, 0, 0, 0, -1, 0, -1, 1, 1, 0]}, {'target': '(((1, 5), (3, 5)), ())', 'coefficient': -1, 'exponents': [0, 0, 0, -1, 0, -1, 0, 0, 0, 0, 0, 0, -1, 0, -1, 1, 1, 1]}]}, {'input': '(0, 1, 3, 4, 6)', 'terms': [{'target': '(((1, 4), (1, 5), (2, 4)), ((1, 4),))', 'coefficient': -1, 'exponents': [0, 0, -1, 0, 0, -1, 0, 1, 0, 0, 0, -1, 0, 0, -1, 1, 0, 1]}, {'target': '(((1, 5), (2, 4)), ())', 'coefficient': 1, 'exponents': [0, 0, -1, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, -1, 1, 1, 1]}, {'target': '(((1, 5), (2, 4), (2, 5)), ((2, 5),))', 'coefficient': -1, 'exponents': [0, 0, -1, 0, 0, -1, 0, 0, 1, 0, 0, -1, 0, 0, -1, 1, 1, 0]}]}, {'input': '(0, 1, 3, 5, 6)', 'terms': [{'target': '(((0, 4), (1, 4), (2, 4)), ((1, 4),))', 'coefficient': -1, 'exponents': [0, 0, -1, 0, -1, 0, 0, 1, 0, 0, 0, -1, 0, -1, 0, 1, 0, 1]}, {'target': '(((0, 4), (2, 4)), ())', 'coefficient': -1, 'exponents': [0, 0, -1, 0, -1, 0, 0, 0, 0, 0, 0, -1, 0, -1, 0, 1, 1, 1]}]}, {'input': '(0, 2, 3, 4, 6)', 'terms': [{'target': '(((1, 3), (1, 4), (1, 5)), ((1, 4),))', 'coefficient': 1, 'exponents': [0, -1, 0, 0, 0, -1, 0, 1, 0, 0, -1, 0, 0, 0, -1, 1, 0, 1]}, {'target': '(((1, 3), (1, 5)), ())', 'coefficient': 1, 'exponents': [0, -1, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, -1, 1, 1, 1]}]}, {'input': '(0, 2, 3, 5, 6)', 'terms': [{'target': '(((0, 3), (0, 4), (1, 3)), ((0, 3),))', 'coefficient': -1, 'exponents': [0, -1, 0, 0, -1, 0, 1, 0, 0, 0, -1, 0, 0, -1, 0, 0, 1, 1]}, {'target': '(((0, 4), (1, 3)), ())', 'coefficient': 1, 'exponents': [0, -1, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, -1, 0, 1, 1, 1]}, {'target': '(((0, 4), (1, 3), (1, 4)), ((1, 4),))', 'coefficient': -1, 'exponents': [0, -1, 0, 0, -1, 0, 0, 1, 0, 0, -1, 0, 0, -1, 0, 1, 0, 1]}]}, {'input': '(0, 2, 4, 5, 6)', 'terms': [{'target': '(((0, 3), (1, 3), (3, 5)), ((0, 3),))', 'coefficient': -1, 'exponents': [0, -1, 0, -1, 0, 0, 1, 0, 0, 0, -1, 0, -1, 0, 0, 0, 1, 1]}, {'target': '(((1, 3), (3, 5)), ())', 'coefficient': 1, 'exponents': [0, -1, 0, -1, 0, 0, 0, 0, 0, 0, -1, 0, -1, 0, 0, 1, 1, 1]}]}, {'input': '(1, 2, 3, 5, 6)', 'terms': [{'target': '(((0, 2), (0, 3), (0, 4)), ((0, 3),))', 'coefficient': 1, 'exponents': [-1, 0, 0, 0, -1, 0, 1, 0, 0, -1, 0, 0, 0, -1, 0, 0, 1, 1]}, {'target': '(((0, 2), (0, 4)), ())', 'coefficient': 1, 'exponents': [-1, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, 1, 1, 1]}]}, {'input': '(1, 2, 4, 5, 6)', 'terms': [{'target': '(((0, 2), (0, 3), (3, 5)), ((0, 3),))', 'coefficient': -1, 'exponents': [-1, 0, 0, -1, 0, 0, 1, 0, 0, -1, 0, 0, -1, 0, 0, 0, 1, 1]}, {'target': '(((0, 2), (2, 5), (3, 5)), ((2, 5),))', 'coefficient': -1, 'exponents': [-1, 0, 0, -1, 0, 0, 0, 0, 1, -1, 0, 0, -1, 0, 0, 1, 1, 0]}, {'target': '(((0, 2), (3, 5)), ())', 'coefficient': -1, 'exponents': [-1, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, -1, 0, 0, 1, 1, 1]}]}, {'input': '(1, 3, 4, 5, 6)', 'terms': [{'target': '(((0, 2), (2, 4)), ())', 'coefficient': 1, 'exponents': [-1, 0, -1, 0, 0, 0, 0, 0, 0, -1, 0, -1, 0, 0, 0, 1, 1, 1]}, {'target': '(((0, 2), (2, 4), (2, 5)), ((2, 5),))', 'coefficient': -1, 'exponents': [-1, 0, -1, 0, 0, 0, 0, 0, 1, -1, 0, -1, 0, 0, 0, 1, 1, 0]}]}, {'input': '(0, 1, 2, 3, 4, 6)', 'terms': [{'target': '(((1, 4), (1, 5)), ((1, 4),))', 'coefficient': -1, 'exponents': [0, 0, 0, 0, 0, -1, 0, 1, 0, 0, 0, 0, 0, 0, -1, 1, 0, 1]}, {'target': '(((1, 5), (2, 5)), ((2, 5),))', 'coefficient': 1, 'exponents': [0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, -1, 1, 1, 0]}, {'target': '(((1, 5),), ())', 'coefficient': -1, 'exponents': [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 1, 1]}]}, {'input': '(0, 1, 2, 3, 5, 6)', 'terms': [{'target': '(((0, 3), (0, 4)), ((0, 3),))', 'coefficient': 1, 'exponents': [0, 0, 0, 0, -1, 0, 1, 0, 0, 0, 0, 0, 0, -1, 0, 0, 1, 1]}, {'target': '(((0, 4), (1, 4)), ((1, 4),))', 'coefficient': -1, 'exponents': [0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 1, 0, 1]}, {'target': '(((0, 4),), ())', 'coefficient': 1, 'exponents': [0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 1, 1, 1]}]}, {'input': '(0, 1, 2, 4, 5, 6)', 'terms': [{'target': '(((0, 3), (3, 5)), ((0, 3),))', 'coefficient': -1, 'exponents': [0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 1, 1]}, {'target': '(((2, 5), (3, 5)), ((2, 5),))', 'coefficient': -1, 'exponents': [0, 0, 0, -1, 0, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 1, 1, 0]}, {'target': '(((3, 5),), ())', 'coefficient': -1, 'exponents': [0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 1, 1, 1]}]}, {'input': '(0, 1, 3, 4, 5, 6)', 'terms': [{'target': '(((1, 4), (2, 4)), ((1, 4),))', 'coefficient': 1, 'exponents': [0, 0, -1, 0, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 1]}, {'target': '(((2, 4), (2, 5)), ((2, 5),))', 'coefficient': -1, 'exponents': [0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0, 0, 1, 1, 0]}, {'target': '(((2, 4),), ())', 'coefficient': 1, 'exponents': [0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 1, 1, 1]}]}, {'input': '(0, 2, 3, 4, 5, 6)', 'terms': [{'target': '(((0, 3), (1, 3)), ((0, 3),))', 'coefficient': -1, 'exponents': [0, -1, 0, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 1]}, {'target': '(((1, 3), (1, 4)), ((1, 4),))', 'coefficient': 1, 'exponents': [0, -1, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0, 0, 0, 1, 0, 1]}, {'target': '(((1, 3),), ())', 'coefficient': -1, 'exponents': [0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 1, 1, 1]}]}, {'input': '(1, 2, 3, 4, 5, 6)', 'terms': [{'target': '(((0, 2), (0, 3)), ((0, 3),))', 'coefficient': -1, 'exponents': [-1, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 1, 1]}, {'target': '(((0, 2), (2, 5)), ((2, 5),))', 'coefficient': -1, 'exponents': [-1, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 1, 1, 0]}, {'target': '(((0, 2),), ())', 'coefficient': 1, 'exponents': [-1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 1, 1]}]}, {'input': '(0, 1, 2, 3, 4, 5, 6)', 'terms': [{'target': '(((0, 3),), ((0, 3),))', 'coefficient': -1, 'exponents': [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]}, {'target': '(((1, 4),), ((1, 4),))', 'coefficient': -1, 'exponents': [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1]}, {'target': '(((2, 5),), ((2, 5),))', 'coefficient': -1, 'exponents': [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0]}, {'target': '((), ())', 'coefficient': 1, 'exponents': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]}]}]

BARE_RAW_DATA = [{'input': '(0, 1, 2, 4, 6)', 'terms': [{'target': '(((1, 5), (2, 5), (3, 5)), ((2, 5),))', 'coefficient': -1, 'exponents': [0, 0, 0, -1, 0, -1, 0, 0, 1, 0, 0, 0, -1, 0, -1, 1, 1, 0]}, {'target': '(((1, 5), (3, 5)), ())', 'coefficient': -1, 'exponents': [0, 0, 0, -1, 0, -1, 0, 0, 0, 0, 0, 0, -1, 0, -1, 1, 1, 1]}]}, {'input': '(0, 1, 3, 4, 6)', 'terms': [{'target': '(((1, 4), (1, 5), (2, 4)), ((1, 4),))', 'coefficient': -1, 'exponents': [0, 0, -1, 0, 0, -1, 0, 1, 0, 0, 0, -1, 0, 0, -1, 1, 0, 1]}, {'target': '(((1, 5), (2, 4)), ())', 'coefficient': 1, 'exponents': [0, 0, -1, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, -1, 1, 1, 1]}, {'target': '(((1, 5), (2, 4), (2, 5)), ((2, 5),))', 'coefficient': -1, 'exponents': [0, 0, -1, 0, 0, -1, 0, 0, 1, 0, 0, -1, 0, 0, -1, 1, 1, 0]}]}, {'input': '(0, 1, 3, 5, 6)', 'terms': [{'target': '(((0, 4), (1, 4), (2, 4)), ((1, 4),))', 'coefficient': -1, 'exponents': [0, 0, -1, 0, -1, 0, 0, 1, 0, 0, 0, -1, 0, -1, 0, 1, 0, 1]}, {'target': '(((0, 4), (2, 4)), ())', 'coefficient': -1, 'exponents': [0, 0, -1, 0, -1, 0, 0, 0, 0, 0, 0, -1, 0, -1, 0, 1, 1, 1]}]}, {'input': '(0, 2, 3, 4, 6)', 'terms': [{'target': '(((1, 3), (1, 4), (1, 5)), ((1, 4),))', 'coefficient': 1, 'exponents': [0, -1, 0, 0, 0, -1, 0, 1, 0, 0, -1, 0, 0, 0, -1, 1, 0, 1]}, {'target': '(((1, 3), (1, 5)), ())', 'coefficient': 1, 'exponents': [0, -1, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, -1, 1, 1, 1]}]}, {'input': '(0, 2, 3, 5, 6)', 'terms': [{'target': '(((0, 3), (0, 4), (1, 3)), ((0, 3),))', 'coefficient': -1, 'exponents': [0, -1, 0, 0, -1, 0, 1, 0, 0, 0, -1, 0, 0, -1, 0, 0, 1, 1]}, {'target': '(((0, 4), (1, 3)), ())', 'coefficient': 1, 'exponents': [0, -1, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, -1, 0, 1, 1, 1]}, {'target': '(((0, 4), (1, 3), (1, 4)), ((1, 4),))', 'coefficient': -1, 'exponents': [0, -1, 0, 0, -1, 0, 0, 1, 0, 0, -1, 0, 0, -1, 0, 1, 0, 1]}]}, {'input': '(0, 2, 4, 5, 6)', 'terms': [{'target': '(((0, 3), (1, 3), (3, 5)), ((0, 3),))', 'coefficient': -1, 'exponents': [0, -1, 0, -1, 0, 0, 1, 0, 0, 0, -1, 0, -1, 0, 0, 0, 1, 1]}, {'target': '(((1, 3), (3, 5)), ())', 'coefficient': 1, 'exponents': [0, -1, 0, -1, 0, 0, 0, 0, 0, 0, -1, 0, -1, 0, 0, 1, 1, 1]}]}, {'input': '(1, 2, 3, 5, 6)', 'terms': [{'target': '(((0, 2), (0, 3), (0, 4)), ((0, 3),))', 'coefficient': 1, 'exponents': [-1, 0, 0, 0, -1, 0, 1, 0, 0, -1, 0, 0, 0, -1, 0, 0, 1, 1]}, {'target': '(((0, 2), (0, 4)), ())', 'coefficient': 1, 'exponents': [-1, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, 1, 1, 1]}]}, {'input': '(1, 2, 4, 5, 6)', 'terms': [{'target': '(((0, 2), (0, 3), (3, 5)), ((0, 3),))', 'coefficient': -1, 'exponents': [-1, 0, 0, -1, 0, 0, 1, 0, 0, -1, 0, 0, -1, 0, 0, 0, 1, 1]}, {'target': '(((0, 2), (2, 5), (3, 5)), ((2, 5),))', 'coefficient': -1, 'exponents': [-1, 0, 0, -1, 0, 0, 0, 0, 1, -1, 0, 0, -1, 0, 0, 1, 1, 0]}, {'target': '(((0, 2), (3, 5)), ())', 'coefficient': -1, 'exponents': [-1, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, -1, 0, 0, 1, 1, 1]}]}, {'input': '(1, 3, 4, 5, 6)', 'terms': [{'target': '(((0, 2), (2, 4)), ())', 'coefficient': 1, 'exponents': [-1, 0, -1, 0, 0, 0, 0, 0, 0, -1, 0, -1, 0, 0, 0, 1, 1, 1]}, {'target': '(((0, 2), (2, 4), (2, 5)), ((2, 5),))', 'coefficient': -1, 'exponents': [-1, 0, -1, 0, 0, 0, 0, 0, 1, -1, 0, -1, 0, 0, 0, 1, 1, 0]}]}, {'input': '(0, 1, 2, 3, 4, 6)', 'terms': [{'target': '(((1, 4), (1, 5)), ((1, 4),))', 'coefficient': -1, 'exponents': [0, 0, 0, 0, 0, -1, 0, 1, 0, 0, 0, 0, 0, 0, -1, 1, 0, 1]}, {'target': '(((1, 5), (2, 5)), ((2, 5),))', 'coefficient': 1, 'exponents': [0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, -1, 1, 1, 0]}, {'target': '(((1, 5),), ())', 'coefficient': -1, 'exponents': [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 1, 1]}]}, {'input': '(0, 1, 2, 3, 5, 6)', 'terms': [{'target': '(((0, 3), (0, 4)), ((0, 3),))', 'coefficient': 1, 'exponents': [0, 0, 0, 0, -1, 0, 1, 0, 0, 0, 0, 0, 0, -1, 0, 0, 1, 1]}, {'target': '(((0, 4), (1, 4)), ((1, 4),))', 'coefficient': -1, 'exponents': [0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 1, 0, 1]}, {'target': '(((0, 4),), ())', 'coefficient': 1, 'exponents': [0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 1, 1, 1]}]}, {'input': '(0, 1, 2, 4, 5, 6)', 'terms': [{'target': '(((0, 3), (3, 5)), ((0, 3),))', 'coefficient': -1, 'exponents': [0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 1, 1]}, {'target': '(((2, 5), (3, 5)), ((2, 5),))', 'coefficient': -1, 'exponents': [0, 0, 0, -1, 0, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 1, 1, 0]}, {'target': '(((3, 5),), ())', 'coefficient': -1, 'exponents': [0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 1, 1, 1]}]}, {'input': '(0, 1, 3, 4, 5, 6)', 'terms': [{'target': '(((1, 4), (2, 4)), ((1, 4),))', 'coefficient': 1, 'exponents': [0, 0, -1, 0, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0, 1, 0, 1]}, {'target': '(((2, 4), (2, 5)), ((2, 5),))', 'coefficient': -1, 'exponents': [0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0, 0, 1, 1, 0]}, {'target': '(((2, 4),), ())', 'coefficient': 1, 'exponents': [0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 1, 1, 1]}]}, {'input': '(0, 2, 3, 4, 5, 6)', 'terms': [{'target': '(((0, 3), (1, 3)), ((0, 3),))', 'coefficient': -1, 'exponents': [0, -1, 0, 0, 0, 0, 1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 1]}, {'target': '(((1, 3), (1, 4)), ((1, 4),))', 'coefficient': 1, 'exponents': [0, -1, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0, 0, 0, 1, 0, 1]}, {'target': '(((1, 3),), ())', 'coefficient': -1, 'exponents': [0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 1, 1, 1]}]}, {'input': '(1, 2, 3, 4, 5, 6)', 'terms': [{'target': '(((0, 2), (0, 3)), ((0, 3),))', 'coefficient': -1, 'exponents': [-1, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 1, 1]}, {'target': '(((0, 2), (2, 5)), ((2, 5),))', 'coefficient': -1, 'exponents': [-1, 0, 0, 0, 0, 0, 0, 0, 1, -1, 0, 0, 0, 0, 0, 1, 1, 0]}, {'target': '(((0, 2),), ())', 'coefficient': 1, 'exponents': [-1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 1, 1, 1]}]}, {'input': '(0, 1, 2, 3, 4, 5, 6)', 'terms': [{'target': '(((0, 3),), ((0, 3),))', 'coefficient': -1, 'exponents': [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]}, {'target': '(((1, 4),), ((1, 4),))', 'coefficient': -1, 'exponents': [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1]}, {'target': '(((2, 5),), ((2, 5),))', 'coefficient': -1, 'exponents': [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0]}, {'target': '((), ())', 'coefficient': 1, 'exponents': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]}]}]

ENDPOINT_DATA = [{'input': '(0, 1, 2, 4, 6)', 'terms': [{'target': '(((1, 3), (1, 5), (3, 5)), ())', 'coefficient': -1, 'exponents': [0, 0, 0, -1, 0, -1, 0, 0, 0, 0, -1, 0, -1, 0, -1, 1, 1, 1]}]}, {'input': '(0, 1, 3, 5, 6)', 'terms': [{'target': '(((0, 2), (0, 4), (2, 4)), ())', 'coefficient': -1, 'exponents': [0, 0, -1, 0, -1, 0, 0, 0, 0, -1, 0, -1, 0, -1, 0, 1, 1, 1]}]}, {'input': '(0, 2, 3, 4, 6)', 'terms': [{'target': '(((1, 3), (1, 5), (3, 5)), ())', 'coefficient': 1, 'exponents': [0, -1, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, -1, 0, -1, 1, 1, 1]}]}, {'input': '(0, 2, 4, 5, 6)', 'terms': [{'target': '(((1, 3), (1, 5), (3, 5)), ())', 'coefficient': -1, 'exponents': [0, -1, 0, -1, 0, 0, 0, 0, 0, 0, -1, 0, -1, 0, -1, 1, 1, 1]}]}, {'input': '(1, 2, 3, 5, 6)', 'terms': [{'target': '(((0, 2), (0, 4), (2, 4)), ())', 'coefficient': 1, 'exponents': [-1, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, -1, 0, -1, 0, 1, 1, 1]}]}, {'input': '(1, 3, 4, 5, 6)', 'terms': [{'target': '(((0, 2), (0, 4), (2, 4)), ())', 'coefficient': -1, 'exponents': [-1, 0, -1, 0, 0, 0, 0, 0, 0, -1, 0, -1, 0, -1, 0, 1, 1, 1]}]}]

NULLHOMOTOPY_DATA = [{'input': '(0, 2, 4, 6)', 'terms': [{'target': '(((1, 3), (1, 5), (3, 5)), ())', 'coefficient': -1, 'exponents': [0, -1, 0, -1, 0, -1, 0, 0, 0, 0, -1, 0, -1, 0, -1, 1, 1, 1]}]}, {'input': '(1, 3, 5, 6)', 'terms': [{'target': '(((0, 2), (0, 4), (2, 4)), ())', 'coefficient': 1, 'exponents': [-1, 0, -1, 0, -1, 0, 0, 0, 0, -1, 0, -1, 0, -1, 0, 1, 1, 1]}]}]

def decode_map(rows, basis):
    out={s:{} for s in basis}
    for row in rows:
        s=ast.literal_eval(row['input'])
        out[s]={(ast.literal_eval(t['target']),tuple(t['exponents'])):t['coefficient'] for t in row['terms']}
    return out


def tensor_model(S,T):
    g,d=tensor_d(S[0],S[1],T)
    w={(s,t):ea(S[2][s],T[2][t]) for s,t in g}
    return g,d,w


def dual_koszul(labels):
    K=koszul([ex({9+i:1}) for i in labels])
    g={s:-n for s,n in K[0].items()}
    w={s:tuple(-a for a in z) for s,z in K[2].items()}
    d={s:{} for s in g}
    for s,terms in K[1].items():
        for (sm,e),c in terms.items():
            d[sm][s,e]=pm(K[0][sm]+1)*c
    return g,d,w


def table_dhom(table,S,n):
    return {s:add(apply(BD,table.get(s,{})),scale(apply(table,S[1][s]),-pm(n))) for s in S[0]}


def select_face_table(table,face):
    return {s:{(c,e):a for (c,e),a in v.items() if c[0]==face} for s,v in table.items()}


def compose_source(table,comparison):
    return {s:apply(table,v) for s,v in comparison.items()}


def verify_model(M,tag):
    for s,n in M[0].items():
        for (t,e),a in M[1][s].items():
            check(M[0][t]==n-1,tag+'_degree')
            check(ea(M[2][t],e)==M[2][s],tag+'_internal_degree')
        check(not apply(M[1],M[1][s]),tag+'_d_squared')


def source_comparison(S,P,end,twisted=True):
    fac=ex({9+i:1 for i in end}) if twisted else ZERO
    return {(s,h):({(s,fac):1} if not h else {}) for s,h in S[0]}


def sdr_cycles(g,original):
    """Signed-unit elimination retaining actual original-basis cycle inclusions."""
    d={s:dict(v) for s,v in original.items()}; inc={s:{s:1} for s in g};steps=0
    while True:
        hit=next(((b,a,c) for b,v in d.items() for a,c in v.items() if abs(c)==1),None)
        if hit is None:break
        b,a,c=hit
        keep=[s for s in d if s not in (a,b)]
        tail={y:-c*v for y,v in d[b].items() if y!=a}
        # New survivor x embeds as x-c*d[x][a]*b.
        inc={x:add(inc[x],scale(inc[b],-c*d[x].get(a,0))) for x in keep}
        nd={}
        for x in keep:
            ca=d[x].get(a,0)
            nd[x]=add({y:v for y,v in d[x].items() if y not in (a,b)},scale(tail,ca))
        d=nd;steps+=1
    check(not any(d.values()),'endpoint_SDR_only_unit_pivots')
    for v in inc.values():check(not lin(original,v),'endpoint_SDR_cycles_closed')
    return d,inc,steps


def encode_candidate(table):
    return [{'input':repr(s),'terms':[{'target':repr(c),'exponents':list(e),'coefficient':a} for (c,e),a in sorted(v.items(),key=repr)]} for s,v in table.items() if v]


def endpoint_candidate_audit():
    records=[]; primitive_records=[];states=0;hom_columns=0
    check(len(CELLS)==215,'target_215_states')
    for c in CELLS:
        check(not apply(BD,BD[c]),'original_target_d_squared')
        for (t,e),a in BD[c].items():
            check(target_legal(t,e),'original_target_stalk_domains')
    for labels in [t for t in subsets(OD) if len(t)>=2]:
        P=koszul([ex({i:1}) for i in range(6)]+[ex({9+i:1 for i in labels})])
        lam=es(es(GAMMA,ex({i:1 for i in range(6)})),ex({9+i:1 for i in labels}))
        G=decode_map(BARE_MAP_DATA,P[0]); raw=decode_map(BARE_RAW_DATA,P[0]); aa=decode_map(ENDPOINT_DATA,P[0]); hh=decode_map(NULLHOMOTOPY_DATA,P[0])
        for s in P[0]:
            check(not table_dhom(G,P,-4)[s],'inherited_bare_map_rechecked')
            check(table_dhom(raw,P,-4)[s]==aa[s],'inherited_full_endpoint_equation')
            check(table_dhom(hh,P,-4)[s]==aa[s],'inherited_nullhomotopy_equation')
        for side,end,face in [('plus',OD,VP),('minus',EV,VM)]:
            D=dual_koszul(end);S=tensor_model(P,D);verify_model(S,'Gysin_source')
            beta=ex({9+i:1 for i in end}); Sfr=(S[0],S[1],{s:ea(w,beta) for s,w in S[2].items()})
            comp=source_comparison(Sfr,P,end,True)
            for s in Sfr[0]:
                check(apply(P[1],comp[s])==apply(comp,Sfr[1][s]),'Euler_counit_chain_map')
                for (p,e),v in comp[s].items():check(ea(P[2][p],e)==Sfr[2][s],'Euler_counit_internal_degree')
            # Euler evaluation kills the ordinary counit as a derived map.
            # This is a negative control, not the physical Gysin transition.
            ti=end[0]; partial_tau=ex({9+i:1 for i in end if i!=ti})
            kc={(p,h):({(p,partial_tau):pm(P[0][p]+1)} if h==(0,) else {})
                for p,h in Sfr[0]}
            for s in Sfr[0]:
                lhs=add(apply(P[1],kc[s]),apply(kc,Sfr[1][s]))
                check(lhs==comp[s],'Euler_counit_explicit_nullhomotopy')
            hside=select_face_table(hh,face);aside=select_face_table(aa,face)
            HC=compose_source(hside,comp);AC=compose_source(aside,comp);FC=compose_source(G,comp)
            dh=table_dhom(HC,Sfr,-4);df=table_dhom(FC,Sfr,-4)
            for s in Sfr[0]:
                check(dh[s]==AC[s],'Gysin_transported_endpoint_nullhomotopy')
                check(not df[s],'Gysin_transported_generic_closed')
            # Polynomial identities restrict to all 64 faces, with support-safe
            # specialization (a stalk with an inverted vanishing normal is zero).
            for center in subsets(tuple(range(6))):
                for s in Sfr[0]:
                    left={(c,e):a for (c,e),a in dh[s].items() if bare_allowed(c,e,center)}
                    right={(c,e):a for (c,e),a in AC[s].items() if bare_allowed(c,e,center)}
                    check(left==right,'all_64_faces_complete_endpoint_identity')
            for fshift in (False,True):
                ll=ea(lam,beta) if fshift else lam
                for central in (False,True):
                    center=tuple(range(6)) if central else ()
                    g,d,cf=bare_hom(S,ll,center);hom_columns+=len(g)
                    sections={}
                    for kind in ('K','E','Q','B','V'):
                        gg,dd=bare_section(g,d,kind);ranks,_,steps=fast_reduce(gg,dd)
                        sections[kind]={'columns':len(gg),'Ext':{str(-k):v for k,v in ranks.items()},'unit_pivots':steps}
                    if not fshift:
                        for kind in ('K','E','Q'):check(sections[kind]['Ext']=={'4':1},'same_frame_Gysin_generic_rank_one')
                        for kind in ('B','V'):check(sections[kind]['Ext']=={},'same_frame_Gysin_endpoints_acyclic')
                    else:
                        check(sections['V']['Ext']=={'4':1},'framed_Gysin_endpoint_rank_one')
                        check('4' not in sections['Q']['Ext'],'framed_Gysin_no_degree_four_generic')
                    rec={'T':list(labels),'endpoint':side,'Gysin_determinant_frame':fshift,'central_short_Rees':central,'sections':sections}
                    records.append(rec)
                    if fshift and not central:
                        gv,dv=bare_section(g,d,'V');rd,inc,steps=sdr_cycles(gv,dv)
                        survivors=[s for s in rd if gv[s]==-4]
                        check(len(survivors)==1,'unique_endpoint_cycle_class')
                        cycle=inc[survivors[0]]
                        top=(tuple(range(7)),())
                        distinguished=(top,(face,face))
                        val=cycle.get(distinguished,0)
                        check(abs(val)==1,'primitive_fully_marked_endpoint_top')
                        cycle=scale(cycle,val)
                        tab={s:{} for s in S[0]}
                        for (s,c),v in cycle.items():tab[s][c,cf[s,c]]=v
                        td=table_dhom(tab,S,-4)
                        for s in S[0]:check(not td[s],'physical_candidate_endpoint_cochain_closed')
                        rr,pv,_=fast_reduce(gv,dv,[cycle])
                        check(any(abs(v)==1 for v in pv[0].values()),'endpoint_class_not_any_boundary')
                        # Add the primitive endpoint class to the transported
                        # nullhomotopy. Their difference is nonzero in H^4.
                        theta={s:add(HC[s],tab[s]) for s in S[0]}
                        dtheta=table_dhom(theta,Sfr,-4)
                        for s in Sfr[0]:check(dtheta[s]==AC[s],'independently_framed_connector_same_boundary')
                        primitive_records.append({'T':list(labels),'endpoint':side,'terms':sum(map(len,tab.values())), 'cycle':encode_candidate(tab),'comparison_to_coefficient_nullhomotopy_obstruction':1,'degree':4,'fine_degree':list(ll)})
            states+=len(S[0])
    return {'source_generator_count_each':1024,'channels_with_eta_labels':8,'distinct_Koszul_sources':4,'endpoint_variants':8,'coefficient_frames_and_central_controls':records,'explicit_primitive_endpoint_classes':primitive_records,'complete_Hom_columns':hom_columns,'same_target_unit_framing_pair_obstruction':[1,1],'Euler_counit_derived_map':'nullhomotopic by explicit single-normal primitive','full_physical_identification':False}


# --- Mixed operations in the native two-exterior-block algebra ---
# xi_i = odd occurrence (1,3,5); eta_i = even occurrence (0,4,2).
# These align reflection so that it swaps xi_i with eta_i.
# Canonical words contain alternating, increasing squarefree blocks.
@lru_cache(None)
def normalize_word(word):
    word=tuple(word)
    if not word:return (),1
    out=[];sg=1;j=0
    while j<len(word):
        side=word[j]//3;end=j
        while end<len(word) and word[end]//3==side:end+=1
        block=word[j:end]
        if len(set(block))!=len(block):return (),0
        sg*=pm(sum(block[a]>block[b] for a in range(len(block)) for b in range(a+1,len(block))))
        out.extend(sorted(block));j=end
    return tuple(out),sg

def algadd(*xs):return add(*xs)
def algmul(a,b):
    out={}
    for x,c in a.items():
        for y,d in b.items():
            z,s=normalize_word(x+y)
            if s:out=add(out,{z:c*d*s})
    return out

def letter(i):return {(i,):1}
def adeg(a):
    ns={len(w) for w in a}
    if len(ns)>1:raise ValueError('homogeneous input required')
    return next(iter(ns),0)
def bracket(a,b):return add(algmul(a,b),scale(algmul(b,a),-pm(adeg(a)*adeg(b))))
def endpoint_module(a,plus=True):
    killed=0 if plus else 1
    return {w:c for w,c in a.items() if not w or w[-1]//3!=killed}
def exterior_image(a):
    out={}
    for w,c in a.items():
        if len(set(w))!=len(w):continue
        sg=pm(sum(w[i]>w[j] for i in range(len(w)) for j in range(i+1,len(w))))
        out=add(out,{tuple(sorted(w)):c*sg})
    return out

def perm_alg(a,p):
    out={}
    for w,c in a.items():
        z,s=normalize_word(tuple(p[i] for i in w))
        if s:out=add(out,{z:c*s})
    return out

def linear_rank(vectors):
    # Only signed-unit reductions are used on these explicit independent rows.
    piv={}
    for v in vectors:
        v=dict(v)
        for key,b in piv.items():
            if v.get(key):v=add(v,scale(b,-v[key]))
        if v:
            key=next(iter(sorted(v)))
            check(abs(v[key])==1,'mixed_action_unit_pivot')
            v=scale(v,v[key]);piv[key]=v
    return len(piv)

def mixed_operation_audit():
    rs={(i,j):bracket(letter(i),letter(3+j)) for i in range(3) for j in range(3)}
    records=[]
    for (i,j),v in rs.items():
        check(not exterior_image(v),'mixed_generator_exterior_image_zero')
        pp=endpoint_module(v,True);mm=endpoint_module(v,False)
        check(pp=={(i,3+j):1},'quadratic_plus_action_nonzero')
        check(mm=={(3+j,i):1},'quadratic_minus_action_nonzero')
        records.append({'i':i,'j':j,'plus_action':repr(pp),'minus_action':repr(mm)})
    check(linear_rank([endpoint_module(v,True) for v in rs.values()])==9,'plus_nine_independent_classes')
    check(linear_rank([endpoint_module(v,False) for v in rs.values()])==9,'minus_nine_independent_classes')
    rr=rs[0,0];powv={():1}
    for n in range(1,9):
        powv=algmul(rr,powv)
        check(endpoint_module(powv,True)=={(0,3)*n:1},'nonzero_quadratic_orbit_arbitrary_n_pattern')
        check(endpoint_module(powv,False)=={(3,0)*n:1},'nonzero_quadratic_orbit_other_endpoint')
    rot=(1,2,0,5,3,4);ref=(3,4,5,0,1,2)
    def compose(p,q):return tuple(p[q[i]] for i in range(6))
    ident=tuple(range(6))
    check(compose(rot,compose(rot,rot))==ident,'operation_rotation_cube')
    check(compose(ref,ref)==ident,'operation_reflection_square')
    check(compose(ref,compose(rot,ref))==compose(rot,rot),'operation_D3_relation')
    for (i,j),v in rs.items():
        check(perm_alg(v,rot)==rs[(i+1)%3,(j-1)%3],'nine_rotation_formulas')
        check(perm_alg(v,ref)==rs[j,i],'nine_reflection_formulas')
    W=bracket(letter(1),bracket(letter(4),rs[0,0]))
    dec=bracket(rs[1,1],rs[0,0])
    check(perm_alg(W,ref)==add(scale(W,-1),dec),'reflection_requires_decomposable_correction')
    check(bool(dec),'decomposable_correction_nonzero')
    # Verify D3 on products and nested generators, not on indecomposables alone.
    generators=list(rs.values())+[W]
    examples=generators+[algmul(a,b) for a in generators for b in generators]
    for a in examples:
        check(perm_alg(perm_alg(a,ref),ref)==a,'full_words_reflection_square')
        check(perm_alg(perm_alg(perm_alg(a,rot),rot),rot)==a,'full_words_rotation_cube')
        check(perm_alg(perm_alg(perm_alg(a,ref),rot),ref)==perm_alg(perm_alg(a,rot),rot),'full_words_dihedral_relation')
    # r is primitive for the graded tensor coproduct, checked explicitly.
    for v in rs.values():
        copro={}
        for word,c in v.items():
            for mask in range(1<<len(word)):
                l=tuple(word[i] for i in range(len(word)) if mask>>i&1)
                r=tuple(word[i] for i in range(len(word)) if not(mask>>i&1))
                sign=pm(sum(not(mask>>i&1) and (mask>>j&1) for i in range(len(word)) for j in range(i+1,len(word))))
                copro=add(copro,{(l,r):c*sign})
        expected=add({(w,()):c for w,c in v.items()},{((),w):c for w,c in v.items()})
        check(copro==expected,'quadratic_Hopf_primitives')
    return {'presentation':'Lambda(xi0,xi1,xi2) * Lambda(eta0,eta1,eta2)', 'nine_quadratic_actions':records, 'independent_degree_two_endpoint_classes':{'plus':9,'minus':9},'exterior_factorization_fails':True,'augmentation_source_unit_lift_first_obstruction_nonzero':True,'augmentation_projection_from_endpoint_module_is_allowed':True,'decomposable_reflection_identity':'s(W)=-W+[r11,r00]', 'W':repr(W),'decomposable_term':repr(dec),'all_49_named_generator_table_retrieved':False,'actual_physical_chain_action_constructed':False}


# --- Product divisor versus intersection: full normal maps and coherences ---
def normal_source_audit():
    records=[]
    for labels in [t for t in subsets(OD) if len(t)>=2]:
        pe=ex({9+i:1 for i in labels});P=koszul([pe]); K=koszul([ex({9+i:1}) for i in OD])
        maps={}
        for i in labels:
            maps[i]={():one(()),(0,):{((OD.index(i),),es(pe,ex({9+i:1}))):1}}
            for s in P[0]:check(apply(K[1],maps[i][s])==apply(maps[i],P[1][s]),'product_to_intersection_chain_map')
        hs={}
        for i,j in combinations(labels,2):
            h={():{},(0,):{((OD.index(i),OD.index(j)),es(pe,ex({9+i:1,9+j:1}))):1}}
            hs[i,j]=h
            for s in P[0]:check(add(apply(K[1],h[s]),apply(h,P[1][s]))==add(maps[j][s],scale(maps[i][s],-1)),'normal_pair_comparison')
        if len(labels)==3:
            h={():{},(0,):{((0,1,2),ZERO):1}}
            for s in P[0]:
                rhs=add(hs[3,5][s],scale(hs[1,5][s],-1),hs[1,3][s])
                check(add(apply(K[1],h[s]),scale(apply(h,P[1][s]),-1))==rhs,'normal_triple_comparison')
        for center in subsets(tuple(range(6))):
            spec=lambda v:{(b,e):c for (b,e),c in v.items() if all(e[9+i]==0 for i in center)}
            for i,j in combinations(labels,2):
                for s in P[0]:check(spec(add(apply(K[1],hs[i,j][s]),apply(hs[i,j],P[1][s])))==spec(add(maps[j][s],scale(maps[i][s],-1))),'normal_all_Rees_faces')
        # Opposite endpoint triple: p_T remains nonzero after setting its
        # three independent even Rees equations to zero. This witnesses the
        # obstruction to a unit-preserving product->intersection map.
        check(all(pe[9+i]==0 for i in EV),'opposite_triple_unit_map_obstructed')
        records.append({'T':list(labels),'same_branch_primary_maps':len(labels),'pair_homotopies':len(hs),'triple_homotopy':len(labels)==3,'opposite_branch_unit_map_obstruction':'t_T modulo (t0,t2,t4) is nonzero'})
    return records


def main(path):
    endpoints=endpoint_candidate_audit()
    operations=mixed_operation_audit()
    normal=normal_source_audit()
    result={'status':'typed_candidate_and_obstructions_not_physical_identification','pinned_commit':COMMIT,
      'endpoint_candidate':endpoints,'relative_operations':operations,'normal_comparisons':normal,
      'full_physical_pullback':'depends on an unconstructed operation-compatible bivariant endpoint comparison',
      'linear_control':'Cone(coefficient_variations plus physical_variations -> comparison_variations)[-1]',
      'all_check_categories':dict(sorted(COUNT.items())),'total_exact_checks':sum(COUNT.values()),
      'scope':['The 49-generator Hopf-kernel statement is an established input from the user, not re-proved by this script.',
      'All nine quadratic endpoint actions are checked in the explicit native two-exterior-block module presentation.',
      'The normal Gysin sources, Euler counits, and endpoint cochains are constructed in the ambient coefficient model.',
      'No action on the physical spatial target or bivariant collar comparison is declared from coefficient tests.',
      'No proof-assistant verification, repository writes, or inference of physical reflection parity.']}
    path.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':result['status'],'checks':result['total_exact_checks'], 'complete_Hom_columns':endpoints['complete_Hom_columns'],'endpoint_variants':endpoints['endpoint_variants'],'quadratic_endpoint_ranks':operations['independent_degree_two_endpoint_classes'],'output':str(path)},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('marici_physical_endpoint_pullback_certificate.json'))
    main(parser.parse_args().output)
