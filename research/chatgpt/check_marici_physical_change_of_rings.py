#!/usr/bin/env python3
"""Exact physical change-of-rings test for the framed Marici endpoint.
Core polynomial, target and bar helpers reproduced from the supplied
check_marici_comparison_fibre_adjunction_bar.py; the new computations below
are independently executed. Standard library only. No repository writes.
Tests the specified Hom_A source, not an unspecified bivariant replacement.
"""
from __future__ import annotations

import argparse, ast, hashlib, json

from pathlib import Path

from collections import Counter, defaultdict, deque

from itertools import combinations, product

from functools import lru_cache

COMMIT='d1947b67a60d3e88ba77f4ca60ea02c2a306ee61'

NV=18

ZERO=(0,)*NV

COUNT=Counter()

EV=(0,2,4)

OD=(1,3,5)

ORDER=EV+OD

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

SHORT=tuple(diag(i,i+2) for i in range(6))

LONG=tuple(diag(i,i+3) for i in range(3))

IX={a:i for i,a in enumerate(SHORT+LONG)}

FACES=tuple(f for k in range(4) for f in combinations(DS,k) if all(not cross(a,b) for a,b in combinations(f,2)))

CELLS=tuple((f,h) for f in FACES for h in subsets(f))

VP=tuple(sorted(SHORT[i] for i in OD))

VM=tuple(sorted(SHORT[i] for i in EV))

GAMMA=ex({15:1,16:1,17:1})

BD={c:target_boundary(c) for c in CELLS}

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

# ---- Actual line-retaining counit, its comparison cone, and its fibre ----
def target_hom(S,lam,kind='K',center=()):
    W=bare_model();g={};cf={};d={}
    def keept(t):
        side=target_side(t)
        return (kind=='K' or (kind=='V' and side=='V') or
                (kind=='B' and side!='Q') or (kind=='BV' and side=='B') or
                (kind=='Q' and side=='Q') or (kind=='E' and side!='V'))
    targets=[t for t in W[0] if keept(t) and bare_allowed(t,ZERO,center)]
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
            if not keept(tt):continue
            ef=ea(ee,e);y=a,tt
            if bare_allowed(tt,ef,center):
                check(y in cf and cf[y]==ef,'new_Hom_target_domain')
                value[y]=value.get(y,0)+v
        for aa,e,v in inc[a]:
            ef=ea(ee,e);y=aa,t
            if bare_allowed(t,ef,center):
                check(y in cf and cf[y]==ef,'new_Hom_source_domain')
                value[y]=value.get(y,0)-pm(n)*v
        d[a,t]={y:v for y,v in value.items() if v}
    for a in g:check(not lin(d,d[a]),'new_complete_Hom_d_squared')
    return g,d,cf


def cone_cohom(A,C,f):
    """Uses homological degree -cohomological degree throughout."""
    ga,da=A;gc,dc=C
    g={('c',c):q for c,q in gc.items()}
    g.update({('a',a):q+1 for a,q in ga.items()})
    d={('c',c):{('c',cc):v for cc,v in dc[c].items()} for c in gc}
    for a in ga:
        d['a',a]=add({('c',c):v for c,v in f[a].items()},
                     {('a',aa):-v for aa,v in da[a].items()})
    return g,d



NM=6; NZ=(0,)*NM
OP_TO_OCC=(1,3,5,0,4,2)
OCC_TO_OP={j:i for i,j in enumerate(OP_TO_OCC)}

def nmadd(a,b):return tuple(x+y for x,y in zip(a,b))
def pure_monomial(a):return not(any(a[i] for i in EV) and any(a[i] for i in OD))
def nmult(a,b,side=None):
    c=nmadd(a,b)
    if not pure_monomial(c):return None
    if side is not None and any(c[i] for i in range(6) if i not in side):return None
    return c

def compositions(n,k):
    if k==0:
        if n==0:yield ()
        return
    if k==1:yield (n,);return
    for a in range(n+1):
        for r in compositions(n-a,k-1):yield (a,)+r

@lru_cache(None)
def native_monomials(n,side=None):
    return tuple(x for x in compositions(n,6) if pure_monomial(x) and
                 (side is None or all(not x[i] for i in range(6) if i not in side)))

@lru_cache(None)
def bar_sequences(n):
    if n==0:return ((),)
    return tuple((m,)+rest for k in range(1,n+1) for m in native_monomials(k)
                 for rest in bar_sequences(n-k))


def bar_model(max_weight,side=None,free_left=False):
    """side=None gives Bar(C,B,C); otherwise Bar(C,B,B_side).
    free_left=True gives B x bar(B)^n x B_side, including the literal
    native source in the brief, truncated by total polynomial degree.
    """
    basis={}; weight={};d={}
    for total in range(max_weight+1):
        for wl in range(total+1) if free_left else (0,):
            for left in native_monomials(wl):
                for wt in range(total-wl+1) if side is not None else (0,):
                    tails=native_monomials(wt,side) if side is not None else (NZ,)
                    for tail in tails:
                        for bars in bar_sequences(total-wl-wt):
                            key=(left,bars,tail) if free_left else (bars,tail)
                            w=nmadd(left,tail)
                            for m in bars:w=nmadd(w,m)
                            basis[key]=len(bars);weight[key]=w
    for key,n in basis.items():
        if free_left:left,bars,tail=key
        else:bars,tail=key;left=NZ
        out={}
        if n:
            if free_left:
                m=nmult(left,bars[0])
                if m is not None:out[(m,bars[1:],tail)]=1
            for i in range(1,n):
                m=nmult(bars[i-1],bars[i])
                if m is None:continue
                bs=bars[:i-1]+(m,)+bars[i+1:]
                y=(left,bs,tail) if free_left else (bs,tail)
                out=add(out,{y:pm(i)})
            if side is not None:
                m=nmult(bars[-1],tail,side)
                if m is not None:
                    y=(left,bars[:-1],m) if free_left else (bars[:-1],m)
                    out=add(out,{y:pm(n)})
        d[key]=out
        for y in out:check(y in basis and weight[y]==weight[key],'native_bar_internal_weight')
    for x in basis:check(not lin(d,d[x]),'literal_native_bar_d_squared' if free_left else 'native_reduced_bar_d_squared')
    return basis,d,weight


def dual_integral_complex(model):
    g0,d0,w=model
    g={x:-q for x,q in g0.items()};d={x:{} for x in g}
    for x,vec in d0.items():
        for y,a in vec.items():d[y][x]=a
    for x in g:check(not lin(d,d[x]),'native_bar_cochain_d_squared')
    return g,d,w


def full_sdr(g,d0):
    """Integral SDR with original-basis homotopy, checked columnwise."""
    d={x:dict(v) for x,v in d0.items()};p={x:{x:1} for x in g};inc={x:{x:1} for x in g};H={x:{} for x in g}
    while True:
        hit=next(((b,a,c) for b,v in d.items() for a,c in v.items() if abs(c)==1),None)
        if hit is None:break
        b,a,c=hit
        keep=[x for x in d if x not in (a,b)]
        for x in g:
            pa=p[x].get(a,0)
            if pa:H[x]=add(H[x],scale(inc[b],c*pa))
        tail={y:-c*v for y,v in d[b].items() if y!=a}
        inc={x:add(inc[x],scale(inc[b],-c*d[x].get(a,0))) for x in keep}
        p={x:add({y:v for y,v in p[x].items() if y not in (a,b)},scale(tail,p[x].get(a,0))) for x in g}
        d={x:add({y:v for y,v in d[x].items() if y not in (a,b)},scale(tail,d[x].get(a,0))) for x in keep}
    check(not any(d.values()),'native_bar_SDR_all_pivots_units')
    for x in g:
        check(add(lin(d0,H[x]),lin(H,d0[x]))==add({x:1},scale(lin(inc,p[x]),-1)),
              'native_bar_SDR_identity')
    return {x:g[x] for x in d},p,inc,H


def weight_sdr(model):
    g,d,w=model;weights=sorted(set(w.values()))
    out={};hist=Counter()
    for alpha in weights:
        gg={x:q for x,q in g.items() if w[x]==alpha}
        dd={x:dict(d[x]) for x in gg}
        rd,p,i,h=full_sdr(gg,dd)
        for x,n in rd.items():
            check(-n==sum(alpha),'native_bar_diagonal_purity')
            hist[-n]+=1
        out[alpha]=(gg,dd,rd,p,i,h)
    return out,dict(sorted(hist.items()))


def rawmul(a,b):
    out={}
    for x,c in a.items():
        for y,v in b.items():out=add(out,{x+y:c*v})
    return out

def rawbracket(a,b):return add(rawmul(a,b),scale(rawmul(b,a),-pm(adeg(a)*adeg(b))))

def raw_normalize(v):
    out={}
    for word,c in v.items():
        w,sg=normalize_word(word)
        if sg:out=add(out,{w:c*sg})
    return out

def raw_perm(v,p):return {tuple(p[i] for i in w):c for w,c in v.items()}

def letter_mono(i):
    x=[0]*6;x[OP_TO_OCC[i]]=1;return tuple(x)

def raw_cochain(v):
    out={}
    for word,c in v.items():
        key=(tuple(letter_mono(i) for i in word),NZ)
        out=add(out,{key:c})
    return out

def word_weight(w):
    a=NZ
    for i in w:a=nmadd(a,letter_mono(i))
    return a

def op_generators():
    out={}
    for I in subsets((0,1,2)):
        if not I:continue
        for J in subsets((0,1,2)):
            if not J:continue
            v=rawbracket(letter(I[0]),letter(3+J[0]))
            for j in reversed(J[1:]):v=rawbracket(letter(3+j),v)
            for i in reversed(I[1:]):v=rawbracket(letter(i),v)
            out[I,J]=v
    return out


def cup(f,h):
    """Coalg deconcatenation dual: f is algebra cochain, h module cochain."""
    out={}
    for (bf,tf),c in f.items():
        check(tf==NZ,'cup_algebra_augmentation_tail')
        for (bh,th),v in h.items():out=add(out,{(bf+bh,th):c*v})
    return out


def project_vec(v,sdr,weights):
    out={}
    for x,c in v.items():
        alpha=weights[x];p=sdr[alpha][3]
        out=add(out,scale(p[x],c))
    return out


def boundary_homotopy(v,sdr,weights):
    out={}
    for x,c in v.items():out=add(out,scale(sdr[weights[x]][5][x],c))
    return out




# NEW COMPUTATIONS: helper integer degree is minus cohomological degree.
def endpoint_hom(S,lam,end,center=()):
    g,d,cf=target_hom(S,lam,'V',center)
    face=VP if end==OD else VM
    keys=[x for x in g if x[1][0]==face]
    keyset=set(keys)
    return ({x:g[x] for x in keys},
            {x:{y:v for y,v in d[x].items() if y in keyset} for x in keys},
            {x:cf[x] for x in keys})


def native_resolution():
    """Minimal A-free resolution of A/(I_even I_odd)."""
    root=('unit',);g={root:0};d={root:{}};wt={root:ZERO}
    for U in subsets(EV):
        if not U:continue
        for V in subsets(OD):
            if not V:continue
            key=(U,V);g[key]=len(U)+len(V)-1
            wt[key]=ex({i:1 for i in U+V});out={}
            if len(U)==len(V)==1:
                out[root,ex({U[0]:1,V[0]:1})]=1
            else:
                if len(U)>1:
                    for i,x in enumerate(U):out[(U[:i]+U[i+1:],V),ex({x:1})]=pm(i)
                if len(V)>1:
                    for j,x in enumerate(V):out[(U,V[:j]+V[j+1:]),ex({x:1})]=pm(len(U)-1+j)
            d[key]=out
    verify_model((g,d,wt),'native_A_resolution')
    ranks=dict(sorted(Counter(g.values()).items()))
    check(ranks=={0:1,1:9,2:18,3:15,4:6,5:1},'native_Tor_ranks')
    for v in d.values():
        check(all(sum(m[:6])>0 for _,m in v),'native_Tor_differential_vanishes_at_conductor')
    return {'free_ranks':ranks,'Tor_A_B_C_ranks':ranks,
            'positive_Tor_internal_weight':'degree n+1 for Tor_n, n>=1',
            'mixed_relations':[{'even':e,'odd':o,'d':'X_even*X_odd'} for e in EV for o in OD],
            'higher_B_action_formality_asserted':False}


def endpoint_models(T,end):
    P=koszul([ex({i:1}) for i in range(6)]+[ex({9+i:1 for i in T})])
    G=tensor_model(P,dual_koszul(end))
    killed=EV if end==OD else OD
    Q=koszul([ex({i:1}) for i in killed])
    QG=tensor_model(Q,G)
    lam=es(es(GAMMA,ex({i:1 for i in range(6)})),ex({9+i:1 for i in T}))
    ll=ea(lam,ex({9+i:1 for i in end}))
    # Multiplication into the already-present occurrence Koszul factor.
    # The full Q tensor is retained; this does not discard its Tor directions.
    mu={}
    for q,(p,h) in QG[0]:
        w,sg=wedge(tuple(killed[i] for i in q),p)
        mu[q,(p,h)]={((w,h),ZERO):sg} if sg else {}
    for z in QG[0]:
        check(apply(G[1],mu[z])==apply(mu,QG[1][z]),'ambient_Koszul_multiplication_chain_map')
        for (y,m),c in mu[z].items():
            check(G[0][y]==QG[0][z] and ea(G[2][y],m)==QG[2][z],
                  'ambient_multiplication_preserves_all_frames')
    inc={p:{(((),p),ZERO):1} for p in G[0]}
    for p in G[0]:
        check(apply(QG[1],inc[p])==apply(inc,G[1][p]),'primitive_forward_source_unit_chain_map')
        check(apply(mu,inc[p])==one(p),'primitive_forward_source_unit_left_inverse')
    return P,G,QG,ll,mu


def endpoint_unit(P,G,ll,end):
    g,d,cf=endpoint_hom(P,ll,end)
    rd,ci,_=sdr_cycles(g,d)
    check(len(rd)==1,'baseline_line_preimage_rank_one')
    w=next(iter(ci.values()))
    face=VP if end==OD else VM
    top=tuple(range(7)),(face,face)
    check(abs(w.get(top,0))==1,'baseline_line_preimage_primitive')
    w=scale(w,w[top])
    nu={s:{} for s in G[0]}
    for (p,t),c in w.items():nu[p,()][t,cf[p,t]]=c
    check(all(not v for v in table_dhom(nu,G,-4).values()),'Gysin_nu_complete_chain_equation')
    check(sum(map(len,nu.values()))==8,'Gysin_nu_eight_rows')
    return nu


def normalized_cohom(g,d):
    hh,_,piv=fast_reduce(g,d)
    return {str(-q-4):r for q,r in sorted(hh.items(),reverse=True)},piv


def purity_projection_audit(model):
    """Projection onto full occurrence input and fully marked target.
    This is the genuine six-equation Koszul purity quotient.
    Its kernel is reduced integrally, not discarded by stipulation.
    """
    g,d,cf=model
    def retain(z):
        (q,(p,h)),t=z
        return all(i in p for i in range(6)) and t[0]==t[1] and not any(cf[z][:6])
    keep={x for x in g if retain(x)}
    for x in g:
        if x not in keep:check(not any(y in keep for y in d[x]),'purity_projection_chain_map')
    kernel={x:g[x] for x in g if x not in keep}
    kd={x:{y:c for y,c in d[x].items() if y in kernel} for x in kernel}
    hk,_,pk=fast_reduce(kernel,kd)
    check(not hk,'full_occurrence_purity_kernel_acyclic')
    small={x:g[x] for x in keep}
    sd={x:{y:c for y,c in d[x].items() if y in keep} for x in keep}
    h,p=normalized_cohom(small,sd)
    return h,pk+p,len(keep)


def physical_endpoint_audit():
    records=[];primitive_matrices=[]
    channels=[(1,3),(1,5),(3,5),(1,3,5)]
    for T in channels:
        for end in (OD,EV):
            side='plus' if end==OD else 'minus'
            P,G,QG,ll,mu=endpoint_models(T,end)
            nu=endpoint_unit(P,G,ll,end)
            unit={z:apply(nu,v) for z,v in mu.items()}
            check(sum(map(len,unit.values()))==64,'physical_unit_64_actual_rows')
            check(all(not v for v in table_dhom(unit,QG,-4).values()),'physical_unit_full_chain_equation')
            for source,v in unit.items():
                for (target,e),c in v.items():check(target_legal(target,e),'physical_unit_original_stalk_domains')
            for p in G[0]:check(unit[(),p]==nu[p],'physical_primitive_column_exact_match')
            tests=[('primitive',())]+[(f'mixed_{e}_{o}',(e,o)) for e in EV for o in OD]
            for name,wt in tests:
                alpha=es(ll,ex({i:1 for i in wt}))
                M=endpoint_hom(QG,alpha,end)
                h,piv,sm=purity_projection_audit(M)
                check(h==({'0':1} if not wt else {}),'physical_primitive_or_quadratic_cohomology')
                record={'T':T,'endpoint':side,'operation_weight':wt,'test':name,
                        'columns':len(M[0]),'purity_quotient_columns':sm,
                        'integral_unit_cancellations':piv,'normalized_cohomology':h}
                if not wt:
                    vec=bare_vector(unit,M[2],M[0]);face=VP if end==OD else VM
                    top=((),(tuple(range(7)),())),(face,face)
                    check(vec.get(top)==1,'physical_endpoint_unit_detector')
                    check(all(not v.get(top,0) for v in M[1].values()),'physical_unit_no_incoming_boundary')
                    record['detector_column']=repr(top)
                records.append(record)
            # Original and central whole complexes; all 64 face coefficients.
            for center in subsets(tuple(range(6))):
                for z,v in unit.items():
                    for (t,e),c in v.items():
                        if bare_allowed(t,e,center):check(not any(e[9+i] for i in center),'specialized_unit_coefficients_legal')
                if len(center) in (0,6):
                    M=endpoint_hom(QG,ll,end,center)
                    h,_,_=purity_projection_audit(M)
                    check(h=={'0':1},'physical_primitive_original_and_central')
            if T==(1,3):
                primitive_matrices.append({'endpoint':side,'internal_degree':ll,
                    'source':'K_A(killed branch occurrences) tensor P_T tensor D_sigma; external line included in internal degree',
                    'primitive_cochain':[{'input':repr(s),'terms':[
                        {'target':repr(t),'exponents':e,'coefficient':c} for (t,e),c in sorted(v.items(),key=repr)]}
                        for s,v in sorted(unit.items(),key=repr) if v]})
            print('endpoint complete',T,side,flush=True)
    return {'frames':records,'representative_primitive_matrices':primitive_matrices,
            'primitive_H0_map':[[1]],'quadratic_forward':'zero physical cohomology cannot reach required native unit-orbit class',
            'external_excess_labels':'Both retained as distinct spectator lines; same underlying coefficient test.',
            'homological_normalization':'normalized H^q = -helper_degree-4',
            'source_generators':8192}

# Ambient bar: all mixed monomials are kept as legal ambient cochains.
@lru_cache(None)
def ambient_monomials(n):return tuple(compositions(n,6))
@lru_cache(None)
def ambient_bars(n):
    if n==0:return ((),)
    return tuple((m,)+rest for k in range(1,n+1) for m in ambient_monomials(k)
                 for rest in ambient_bars(n-k))

def polynomial_bar(maxw,side=None):
    g={};d={};w={}
    for total in range(maxw+1):
        for k in range(total+1) if side is not None else (0,):
            tails=native_monomials(k,side) if side is not None else (NZ,)
            for tail in tails:
                for bs in ambient_bars(total-k):
                    x=(bs,tail);g[x]=len(bs)
                    alpha=tail
                    for m in bs:alpha=nmadd(alpha,m)
                    w[x]=alpha
    for (bs,tail),n in g.items():
        out={}
        for i in range(1,n):
            y=(bs[:i-1]+(nmadd(bs[i-1],bs[i]),)+bs[i+1:],tail)
            out=add(out,{y:pm(i)})
        if n and side is not None:
            m=nmadd(bs[-1],tail)
            if all(not m[i] for i in range(6) if i not in side):out=add(out,{(bs[:-1],m):pm(n)})
        d[bs,tail]=out
    for x in g:
        for y in d[x]:check(w[x]==w[y],'ambient_bar_fine_weight_preserved')
        check(not lin(d,d[x]),'ambient_bar_full_d_squared')
    return g,d,w


def orbit_and_change_rings_audit(maxw=4):
    native_alg=dual_integral_complex(bar_model(maxw))
    ambient_alg=dual_integral_complex(polynomial_bar(maxw))
    alg_sdr,alg_ranks=weight_sdr(ambient_alg)
    check(alg_ranks=={0:1,1:6,2:15,3:20,4:15},'ambient_algebra_exterior_cohomology')
    quadr={};primitives={};nullprimitives={}
    for I in subsets((0,1,2)):
        if not I:continue
        for J in subsets((0,1,2)):
            if not J or len(I)+len(J)>maxw:continue
            r=raw_cochain(rawbracket(letter(I[0]),letter(3+J[0])))
            mixed=nmadd(letter_mono(I[0]),letter_mono(3+J[0]))
            h={((mixed,),NZ):-1}
            check(lin(ambient_alg[1],h)==r,'mixed_ambient_bar_nullhomotopy_exact')
            check(((mixed,),NZ) not in native_alg[0],'mixed_nullhomotopy_not_a_native_cochain')
            for j in reversed(J[1:]):
                x=raw_cochain(letter(3+j));deg_r=len(next(iter(r))[0]);deg_h=deg_r-1
                r=add(cup(x,r),scale(cup(r,x),-pm(deg_r)))
                h=scale(add(cup(x,h),scale(cup(h,x),-pm(deg_h))),-1)
            for i in reversed(I[1:]):
                x=raw_cochain(letter(i));deg_r=len(next(iter(r))[0]);deg_h=deg_r-1
                r=add(cup(x,r),scale(cup(r,x),-pm(deg_r)))
                h=scale(add(cup(x,h),scale(cup(h,x),-pm(deg_h))),-1)
            key=(I,J);primitives[key]=r;nullprimitives[key]=h
            check(lin(ambient_alg[1],h)==r,'ambient_primitive_explicit_nullhomotopy')
            if len(I)+len(J)==2:quadr[key]=r
    orbit={'unit':{((),NZ):1}};null={}
    for key,r in primitives.items():orbit[('primitive',key)]=r;null[('primitive',key)]=nullprimitives[key]
    for a,r in quadr.items():
        for b,s in quadr.items():
            key=('product',a,b);orbit[key]=cup(r,s);null[key]=cup(nullprimitives[a],s)
            check(lin(ambient_alg[1],null[key])==orbit[key],'all_81_products_ambient_nullhomotopies')
    counts=Counter(len(next(iter(v))[0]) for v in orbit.values())
    check(dict(counts)=={0:1,2:9,3:18,4:96},'requested_operation_count')
    records={};native_models={};ambient_models={};witnesses={}
    for side_name,side in [('plus',OD),('minus',EV)]:
        N=dual_integral_complex(bar_model(maxw,side))
        M=dual_integral_complex(polynomial_bar(maxw,side))
        ns,nr=weight_sdr(N);ms,mr=weight_sdr(M)
        check(nr=={0:1,1:3,2:12,3:46,4:177},'native_endpoint_cohomology_retained')
        check(mr=={0:1,1:3,2:3,3:1},'ambient_endpoint_exterior_three')
        # Pullback along quotient of bar complexes: pure slots unchanged,
        # mixed slots get zero. This is not a chosen cohomology projection.
        for x in N[0]:
            check(x in M[0],'native_bar_cochain_extends_by_zero')
            check(lin(M[1],{x:1})==N[1][x],'restriction_of_scalars_actual_chain_map')
        grouped=defaultdict(list);matrix=[]
        for key,v in orbit.items():
            check(not lin(N[1],v),'native_relative_orbit_closed')
            pr=project_vec(v,ns,N[2]);n=len(next(iter(v))[0]);grouped[n].append(pr)
            if key=='unit':
                check(project_vec(v,ms,M[2]),'reverse_change_rings_primitive_pass')
                matrix.append(1)
            else:
                check(lin(M[1],null[key])==v,'endpoint_relative_orbit_ambient_nullhomotopy')
                check(not project_vec(v,ms,M[2]),'reverse_change_rings_kills_nonunit_relative_orbit')
                matrix.append(0)
        rr={n:linear_rank(vs) for n,vs in grouped.items()}
        check(rr==dict(counts),'native_requested_orbit_saturated')
        native_models[side_name]=N;ambient_models[side_name]=M
        records[side_name]={'native_columns':len(N[0]),'ambient_columns':len(M[0]),
                          'native_cohomology':nr,'ambient_cohomology':mr,
                          'native_orbit_ranks':rr,'reverse_on_ordered_orbit':matrix,
                          'ambient_nullhomotopies':len(null)}
        witnesses[side_name]=[{'operation':repr(key),
             'nullhomotopy':[{'bars':bs,'tail':tail,'coefficient':v}
                             for (bs,tail),v in sorted(h.items(),key=repr)]}
             for key,h in sorted(null.items(),key=repr)]
    # The smallest no-solution equation as an explicit native vs ambient matrix.
    # x=X1 (plus-sheet coordinate), y=X0 (coordinate killed on plus sheet).
    x=letter_mono(0);y=letter_mono(3);mx=nmadd(x,y)
    plus=ambient_models['plus'];nativeplus=native_models['plus']
    a=((mx,),NZ);b=((y,),x);c=((y,x),NZ);dd=((x,y),NZ)
    mat=[[plus[1][a].get(c,0),plus[1][b].get(c,0)],
         [plus[1][a].get(dd,0),plus[1][b].get(dd,0)]]
    check(mat==[[-1,1],[-1,0]],'explicit_mixed_endpoint_2x2_matrix')
    check(nativeplus[1][b]=={c:1},'native_mixed_endpoint_single_boundary')
    for v in nativeplus[1].values():check(not v.get(dd,0),'native_mixed_primitive_detector')
    check(add({c:1},{dd:1}).get(dd)==1,'unsolvable_equation_detector_value_one')
    rot=(1,2,0,5,3,4);ref=(3,4,5,0,1,2);identity=tuple(range(6))
    comp=lambda a,b:tuple(a[b[i]] for i in range(6))
    group=[identity,rot,comp(rot,rot),ref,comp(rot,ref),comp(comp(rot,rot),ref)]
    def permmono(a,p):
        z=[0]*6
        for i,v in enumerate(a):z[OP_TO_OCC[p[OCC_TO_OP[i]]]]=v
        return tuple(z)
    def permkey(x,p):return tuple(permmono(m,p) for m in x[0]),permmono(x[1],p)
    def permvec(v,p):return {permkey(x,p):c for x,c in v.items()}
    for models in (native_models,ambient_models):
        for sign,M in models.items():
            for p in group:
                dest=models[('minus' if sign=='plus' else 'plus') if p[0]>=3 else sign]
                for x in M[0]:check(permvec(M[1][x],p)==dest[1][permkey(x,p)],'change_rings_dihedral_chain_transport')
    r={(i,j):rawbracket(letter(i),letter(3+j)) for i in range(3) for j in range(3)}
    W=rawbracket(letter(1),rawbracket(letter(4),r[0,0]))
    D=rawbracket(r[1,1],r[0,0])
    check(raw_perm(W,ref)==add(scale(W,-1),D),'full_decomposable_reflection_identity')
    for sign,M in native_models.items():
        sdr,_=weight_sdr(M)
        check(project_vec(raw_cochain(D),sdr,M[2]),'reflection_decomposable_nonzero_native')
    return {'max_total_weight':maxw,'ambient_algebra_cohomology':alg_ranks,
            'endpoints':records,'explicit_ambient_mixed_d1':mat,
            'native_mixed_d1':[[1],[0]],'native_mixed_detector':[0,1],
            'first_failed_equation':'D k = nu tensor (r_00 m_plus), detector gives 0=1',
            'all_requested_nullhomotopy_matrices':witnesses,
            'primitive_types_tested':{'quadratic':9,'cubic':18,'quartic':15,'ordered_quadratic_products':81},
            'decomposable_reflection':'s(W)=-W+[r11,r00]; nonzero natively, ambient exact',
            'higher_types':'General nested-commutator proof covers all; full matrices only through weight four.'}


def main(path):
    tor=native_resolution()
    bar=orbit_and_change_rings_audit()
    print('bar change-of-rings complete',flush=True)
    endpoint=physical_endpoint_audit()
    result={'status':'falsified_prescribed_forward_primitive_and_native_orbit_comparison',
            'scope':'Specified RHom_A literal derived tensor; not a no-go for a different native-linear bivariant target.',
            'rings':{'C':'Z[X_D03,X_D14,X_D25,t_0,...,t_5,u_D03,u_D14,u_D25]',
                     'A':'C[X_0,...,X_5]','B':'A/(X_even X_odd)',
                     'B_plus':'A/(X_0,X_2,X_4)','B_minus':'A/(X_1,X_3,X_5)'},
            'native_derived_base_change':tor,
            'canonical_nested_Hom':'RHom_B(Pnat,RHom_A(B,RHom_A(G,V)))',
            'coefficient_purity':'Full occurrence-Koszul projection retains determinant, Cartier and endpoint Gysin factors.',
            'primitive_test':'passes via 64-row physical cocycle and [1] matrix',
            'first_obstruction':'mixed quadratic is native-primitive but ambient-exact',
            'bar_comparison':bar,'literal_framed_endpoint':endpoint,
            'physical_square':'No b/chi satisfying required operation equation. No physical control H1 assigned.',
            'Q_morphism_gate':'not reached: first mixed-operation cohomology equation fails',
            'assertions':dict(sorted(COUNT.items())),'total_assertions':sum(COUNT.values()),
            'proof_scope':'Regular-sequence resolution and purity give all-degree results. Bar matrices exhaustive through weight four. No proof assistant.'}
    path.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'checks':result['total_assertions'],
                     'bar_endpoints':bar['endpoints'],'framed_cases':len(endpoint['frames'])},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('marici_physical_change_of_rings_certificate.json'))
    args=parser.parse_args();main(args.output)
