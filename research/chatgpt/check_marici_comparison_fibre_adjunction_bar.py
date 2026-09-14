#!/usr/bin/env python3
"""Comparison support fibre and native normalized bar audit.

Explicit coefficient support quotient; native chain operations are verified
separately. No unconstructed mixed physical action is inferred.
Standard library only, Python >=3.10.
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


def adjunction_case(T,end,center,complete=False):
    P=koszul([ex({i:1}) for i in range(6)]+[ex({9+i:1 for i in T})])
    S=tensor_model(P,dual_koszul(end))
    lam=es(es(GAMMA,ex({i:1 for i in range(6)})),ex({9+i:1 for i in T}))
    ll=ea(lam,ex({9+i:1 for i in end}))
    a,da,cfa=target_hom(P,ll,'V',center)
    c,dc,cfc=target_hom(S,ll,'V',center)
    f={x:{((x[0],()),x[1]):1} for x in a}
    for x in a:
        for y in f[x]:check(y in c and cfa[x]==cfc[y],'line_counit_preserves_internal_frame')
        check(lin(dc,f[x])==lin(f,da[x]),'line_counit_precomposition_chain_map')
    za,dz=cone_cohom((a,da),(c,dc),f)
    for x in za:check(not lin(dz,dz[x]),'adjunction_comparison_cone_squared')
    ha,_,pa=fast_reduce(a,da);hc,_,pc=fast_reduce(c,dc);hz,_,pz=fast_reduce(za,dz)
    check(ha=={-4:1} and hc=={-4:1},'actual_line_and_Gysin_endpoint_cohomology')
    check(not hz,'line_retaining_counit_endpoint_quasiisomorphism')
    # A primitive source cocycle, derived from the actual differential.
    rd,ci,_=sdr_cycles(a,da)
    check(len(rd)==1,'one_primitive_line_framed_endpoint_class')
    w=next(iter(ci.values()))
    face=VP if end==OD else VM
    key=(tuple(range(7)),(face,face))
    check(abs(w.get(key,0))==1,'source_counit_unit_top_coefficient')
    w=scale(w,w[key]);nu=lin(f,w)
    check(not lin(da,w) and not lin(dc,nu),'primitive_endpoint_and_preimage_closed')
    # Honest integral detector: top fully marked coefficient has no incoming boundary.
    nu_key=((tuple(range(7)),()),(face,face))
    check(nu.get(nu_key)==1,'primitive_endpoint_orientation')
    check(all(not v.get(nu_key,0) for v in dc.values()),'endpoint_integral_detector')
    h={('a',x):v for x,v in w.items()}
    pinu={('c',x):v for x,v in nu.items()}
    check(lin(dz,h)==pinu,'primitive_endpoint_discrepancy_has_comparison_homotopy')
    # Fibre J of C -> Cone(f), with exact retraction to A.
    gj={('p',x):q for x,q in c.items()}
    gj.update({('z',x):q-1 for x,q in za.items()})
    dj={('p',x):add({('p',y):v for y,v in dc[x].items()},
                         {('z',('c',x)):1}) for x in c}
    for x in za:dj['z',x]={('z',y):-v for y,v in dz[x].items()}
    proj={x:{} for x in gj};incl={x:{} for x in a};hh={x:{} for x in gj}
    for x in a:
        proj['z',('a',x)]={x:1}
        incl[x]=add({('p',y):v for y,v in f[x].items()}, {('z',('a',x)):1})
    for x in c:hh['z',('c',x)]={('p',x):1}
    for x in gj:
        check(not lin(dj,dj[x]),'comparison_fibre_squared')
        check(lin(proj,dj[x])==lin(da,proj[x]),'comparison_fibre_projection_chain_map')
        lhs=add(lin(dj,hh[x]),lin(hh,dj[x]))
        rhs=add({x:1},scale(lin(incl,proj[x]),-1))
        check(lhs==rhs,'comparison_fibre_explicit_integral_SDR')
    for x in a:
        check(lin(proj,incl[x])=={x:1},'comparison_fibre_section')
        check(lin(dj,incl[x])==lin(incl,da[x]),'comparison_fibre_section_chain_map')
    hj,_,pj=fast_reduce(gj,dj)
    check(hj=={-4:1},'comparison_fibre_endpoint_relative_class_retained')
    record={'T':T,'endpoint':'plus' if end==OD else 'minus','central_face':center,
            'columns':{'line_Hom':len(a),'Gysin_Hom':len(c),'comparison_cone':len(za),'fibre':len(gj)},
            'normalized_cohomology':{'line':{'0':1},'Gysin':{'0':1},'comparison':{},'fibre':{'0':1}},
            'unit_pivots':[pa,pc,pz,pj], 'preimage_terms':len(w),'endpoint_terms':len(nu)}
    if complete:
        record['preimage']=[{'source':repr(x[0]),'target':repr(x[1]),'coefficient':v,
                            'monomial':cfa[x]} for x,v in sorted(w.items(),key=repr)]
        for kind in ('B','BV','K','E','Q'):
            gk,dk,_=target_hom(S,ll,kind,center);rk,_,pk=fast_reduce(gk,dk)
            record.setdefault('other_support_Hom',{})[kind]={str(-q-4):r for q,r in rk.items()}
        # The actual support quotient B -> B/V is a second independently existing candidate.
        gb,db,_=target_hom(S,ll,'B',center)
        gz={x:q for x,q in gb.items() if target_side(x[1])=='B'}
        dz0={x:{y:v for y,v in db[x].items() if y in gz} for x in gz}
        rz,_,_=fast_reduce(gz,dz0)
        rb,vb,_=fast_reduce(gb,db,[nu])
        check(any(abs(v)==1 for v in vb[0].values()),'endpoint_inclusion_short_support_nonzero')
        check(not {x:v for x,v in nu.items() if x in gz},'endpoint_support_quotient_kills_only_comparison_image')
        record['support_quotient_fibre']={'H0':1,'Hminus1':0,'Hminus2':0,'H1':0}
    return record

# ---- The requested native bar, not its cohomology algebra ----
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


def native_bar_audit(maxw=4):
    alg=dual_integral_complex(bar_model(maxw,None))
    asdr,aranks=weight_sdr(alg)
    check(aranks=={0:1,1:6,2:24,3:92,4:354},'native_algebra_low_degree_ranks')
    mods={};msdr={};ranks={};literal_counts={}
    for sign,side in [('plus',OD),('minus',EV)]:
        lit=bar_model(maxw,side,True);literal_counts[sign]=len(lit[0])
        # The free-left augmentation is a chain map to the actual branch.
        aug={x:({nmult(x[0],x[2],side):1} if not x[1] and nmult(x[0],x[2],side) is not None else {}) for x in lit[0]}
        for x in lit[0]:check(not lin(aug,lit[1][x]),'native_bar_branch_augmentation')
        model=dual_integral_complex(bar_model(maxw,side));mods[sign]=model
        msdr[sign],ranks[sign]=weight_sdr(model)
        check(ranks[sign]=={0:1,1:3,2:12,3:46,4:177},'native_endpoint_bar_low_degree_ranks')
    gens=op_generators()
    check(len(gens)==49,'all_49_native_cocycle_formulas')
    degcounts=Counter(adeg(v) for v in gens.values())
    check(dict(degcounts)=={2:9,3:18,4:15,5:6,6:1},'49_primitive_degree_counts')
    quadr={key:v for key,v in gens.items() if adeg(v)==2}
    # Fixed low-degree relative algebra basis: primitives and ordered products.
    rbasis={():{():1}}
    for key,v in gens.items():
        if adeg(v)<=maxw:rbasis[('g',key)]=v
    for ka,a in quadr.items():
        for kb,b in quadr.items():rbasis[('p',ka,kb)]=rawmul(a,b)
    histR=Counter(adeg(v) for v in rbasis.values())
    check(dict(histR)=={0:1,2:9,3:18,4:96},'relative_orbit_basis_counts_through_four')
    for v in rbasis.values():
        c=raw_cochain(v)
        check(all(x in alg[0] for x in c),'all_operation_bar_rows_present')
        check(not lin(alg[1],c),'chain_operation_cocycle')
        # Both module actions are actual deconcatenation actions, not cohomology declarations.
        for sign in mods:
            check(not lin(mods[sign][1],c),'endpoint_action_cochain_closed')
    orbit_ranks={};quotient_ranks={};pbw_ranks={}
    for sign in mods:
        projected_by_degree=defaultdict(list)
        for v in rbasis.values():
            pr=project_vec(raw_cochain(v),msdr[sign],mods[sign][2])
            projected_by_degree[adeg(v)].append(pr)
        orbit_ranks[sign]={n:linear_rank(vs) for n,vs in projected_by_degree.items()}
        check(orbit_ranks[sign]==dict(histR),'entire_tested_R_unit_orbit_primitive')
        quotient_ranks[sign]={n:ranks[sign][n]-orbit_ranks[sign].get(n,0) for n in ranks[sign]}
        # Ordered native PBW free-module dictionary, including all external exterior modes.
        other=(3,4,5) if sign=='plus' else (0,1,2)
        vv=defaultdict(list)
        for v in rbasis.values():
            for subset in subsets(other):
                if adeg(v)+len(subset)>maxw:continue
                value=rawmul(v,{subset:1})
                co=raw_cochain(value)
                vv[adeg(value)].append(project_vec(co,msdr[sign],mods[sign][2]))
        pbw_ranks[sign]={n:linear_rank(v) for n,v in vv.items()}
        check(pbw_ranks[sign]==ranks[sign],'native_PBW_unit_pivots_through_four')
    # Leibniz for every pair of elementary cochains whose total weight <=4.
    # Include nonclosed cochains to test the actual bar differential.
    algebra_by_w=defaultdict(list)
    for x in alg[0]:algebra_by_w[sum(alg[2][x])].append(x)
    for sign,M in mods.items():
        module_by_w=defaultdict(list)
        for y in M[0]:module_by_w[sum(M[2][y])].append(y)
        for wx,xs in algebra_by_w.items():
            for wy,ys in module_by_w.items():
                if wx+wy>maxw:continue
                for x in xs:
                    for y in ys:
                        p=-alg[0][x]
                        lhs=lin(M[1],cup({x:1},{y:1}))
                        rhs=add(cup(alg[1][x],{y:1}),scale(cup({x:1},M[1][y]),pm(p)))
                        check(lhs==rhs,'native_bar_chain_module_Leibniz')
    # Differential identities for same-sheet exterior relations are retained as explicit homotopies.
    relation_homotopies=[]
    for i in range(6):
        for j in range(i,6):
            if i//3!=j//3:continue
            mono=nmadd(letter_mono(i),letter_mono(j))
            h={((mono,),NZ):-1}
            r=raw_cochain(rawmul(letter(i),letter(j))) if i==j else raw_cochain(rawbracket(letter(i),letter(j)))
            check(lin(alg[1],h)==r,'same_sheet_exterior_relation_is_bar_boundary')
            relation_homotopies.append((i,j))
    # Semilinear D3 action on literal bar rows.
    rot=(1,2,0,5,3,4);ref=(3,4,5,0,1,2)
    def comp(p,q):return tuple(p[q[i]] for i in range(6))
    ident=tuple(range(6));group=[ident,rot,comp(rot,rot),ref,comp(rot,ref),comp(comp(rot,rot),ref)]
    def pmono(a,p):
        z=[0]*6
        for k,v in enumerate(a):z[OP_TO_OCC[p[OCC_TO_OP[k]]]]=v
        return tuple(z)
    def pkey(x,p):return tuple(pmono(a,p) for a in x[0]),pmono(x[1],p)
    def pv(v,p):return {pkey(x,p):c for x,c in v.items()}
    for p in group:
        for x in alg[0]:
            check(pv(alg[1][x],p)==alg[1][pkey(x,p)],'native_bar_group_chain_equivariance')
        flips=p[0]>=3
        for sign,M in mods.items():
            dest=mods[('minus' if sign=='plus' else 'plus') if flips else sign]
            for x in M[0]:check(pv(M[1][x],p)==dest[1][pkey(x,p)],'native_endpoint_group_chain_equivariance')
    for p in group:
        for q in group:
            for i in range(6):check(comp(p,q)[i] in range(6),'group_pair_defined')
            for r in group:check(comp(comp(p,q),r)==comp(p,comp(q,r)),'group_triple_associativity')
    rr={(i,j):rawbracket(letter(i),letter(3+j)) for i in range(3) for j in range(3)}
    W=rawbracket(letter(1),rawbracket(letter(4),rr[0,0]));decomp=rawbracket(rr[1,1],rr[0,0])
    check(raw_perm(W,ref)==add(scale(W,-1),decomp),'decomposable_reflection_identity_on_chain_cochains')
    check(raw_normalize(decomp),'decomposable_term_nonzero_in_native_algebra')
    for sign in mods:
        v=project_vec(raw_cochain(decomp),msdr[sign],mods[sign][2])
        check(bool(v),'decomposable_reflection_action_nonzero_at_endpoint')
    # Coordinate restrictions into a regular ambient chart kill the mixed primitive:
    # in B the mixed degree-two monomial is absent; in A it supplies the homotopy.
    for i in range(3):
        for j in range(3):
            mixed=nmadd(letter_mono(i),letter_mono(3+j))
            check(not pure_monomial(mixed),'mixed_ambient_primitive_missing_from_native_ring')
    return {'maximum_total_occurrence_weight':maxw,'native_free_left_bar_columns':literal_counts,
            'native_cochain_columns':{'algebra':len(alg[0]),**{k:len(v[0]) for k,v in mods.items()}},
            'algebra_cohomology_ranks':aranks,'endpoint_cohomology_ranks':ranks,
            'primitive_cocycle_counts':dict(sorted(degcounts.items())),
            'minimal_R_orbit_ranks':orbit_ranks,'quotient_outside_minimal_orbit':quotient_ranks,
            'ordered_free_R_dictionary_ranks':pbw_ranks,
            'chain_level_same_sheet_relation_homotopies':relation_homotopies,
            'decomposable_reflection':'s(W)=-W+[r11,r00] strictly on chosen bar cup expressions',
            'cohomology_not_substituted_for_native_bar':True,
            'R_generators_5_6':'Explicit closed word formulas; no full degree-five/six module reduction claimed',
            'physical_endpoint_chain_action_identified':False}

# ---- Minimal native orbit comparison: an adjunction cone, not a killed target class ----
def orbit_comparison_audit(maxw=4):
    gens=op_generators();rs={k:v for k,v in gens.items() if adeg(v)==2}
    rr={():{():1}}
    rr.update({('g',k):v for k,v in gens.items() if adeg(v)<=maxw})
    rr.update({('p',a,b):rawmul(x,y) for a,x in rs.items() for b,y in rs.items()})
    gr={x:-adeg(v) for x,v in rr.items()};dr={x:{} for x in rr}
    report={}
    for sign,side in [('plus',OD),('minus',EV)]:
        M=dual_integral_complex(bar_model(maxw,side));gm,dm,wm=M
        act={x:raw_cochain(v) for x,v in rr.items()}
        for x in rr:check(not lin(dm,act[x]),'relative_orbit_chain_map')
        gz,dz=cone_cohom((gr,dr),(gm,dm),act)
        for x in gz:check(not lin(dz,dz[x]),'minimal_native_comparison_cone_d_squared')
        # Build the full comparison fibre, including its path component.
        gf={('p',x):q for x,q in gm.items()}
        gf.update({('z',x):q-1 for x,q in gz.items()})
        df={('p',x):add({('p',y):v for y,v in dm[x].items()}, {('z',('c',x)):1}) for x in gm}
        for x in gz:df['z',x]={('z',y):-v for y,v in dz[x].items()}
        pp={x:{} for x in gf};ii={x:{} for x in rr};hh={x:{} for x in gf}
        for x in rr:
            pp['z',('a',x)]={x:1}
            ii[x]=add({('p',y):v for y,v in act[x].items()}, {('z',('a',x)):1})
        for x in gm:hh['z',('c',x)]={('p',x):1}
        for x in gf:
            check(not lin(df,df[x]),'minimal_native_comparison_fibre_d_squared')
            check(add(lin(df,hh[x]),lin(hh,df[x]))==add({x:1},scale(lin(ii,pp[x]),-1)),
                  'minimal_native_comparison_fibre_integral_contraction')
        for x in rr:
            check(lin(pp,ii[x])=={x:1},'minimal_native_comparison_fibre_retraction')
            check(not lin(df,ii[x]),'every_tested_operation_orbit_has_relative_lift')
            # Canonical comparison cochain, including products and decomposable corrections.
            h={('a',x):1}
            check(lin(dz,h)=={('c',y):v for y,v in act[x].items()},
                  'all_native_orbit_discrepancies_filled_by_adjunction_cone')
        rz,_,pz=fast_reduce(gz,dz);rf,_,pf=fast_reduce(gf,df)
        check({-q:n for q,n in rf.items()}=={0:1,2:9,3:18,4:96},'minimal_native_fibre_full_low_degree_cohomology')
        check({-q:n for q,n in rz.items()}=={1:3,2:3,3:28,4:81},'minimal_native_comparison_retains_other_endpoint_modes')
        report[sign]={'native_endpoint_columns':len(gm),'minimal_orbit_columns':len(rr),
          'comparison_columns':len(gz),'fibre_columns':len(gf),
          'H_fibre':{-q:n for q,n in rf.items()},'H_comparison':{-q:n for q,n in rz.items()},
          'primitive_discrepancy':0,'quadratic_discrepancies':[0]*9,
          'two_quadratic_product_discrepancies':[0]*81,
          'primitive_detector':'projection to the unit coordinate in the free relative-operation source',
          'unit_pivots_comparison_fibre':[pz,pf]}
    return report


def integer_coordinates(columns,v):
    piv={}
    for j,column in enumerate(columns):
        a=dict(column);coord={j:1}
        for key,(row,c) in piv.items():
            mult=a.get(key,0)
            if mult:a=add(a,scale(row,-mult));coord=add(coord,scale(c,-mult))
        if not a:raise AssertionError('dependent_relative_basis')
        key=next(iter(sorted(a)))
        check(abs(a[key])==1,'R_dihedral_basis_unimodular')
        mult=a[key];a=scale(a,mult);coord=scale(coord,mult);piv[key]=(a,coord)
    out={};a=dict(v)
    for key,(row,c) in piv.items():
        mult=a.get(key,0)
        if mult:a=add(a,scale(row,-mult));out=add(out,scale(c,mult))
    check(not a,'R_dihedral_transport_in_full_relative_algebra')
    return out


def group_operation_coherence_audit(maxw=4):
    A=dual_integral_complex(bar_model(maxw,None));sdr,_=weight_sdr(A)
    gg,dd,ww=A;gens=op_generators();quad={k:v for k,v in gens.items() if adeg(v)==2}
    rr={():{():1}}
    rr.update({('g',k):v for k,v in gens.items() if adeg(v)<=maxw})
    rr.update({('p',a,b):rawmul(x,y) for a,x in quad.items() for b,y in quad.items()})
    keys=list(rr);rawbasis=[rr[k] for k in keys];co=[raw_cochain(v) for v in rawbasis]
    cb=[raw_normalize(v) for v in rawbasis]
    groups=[];rot=(1,2,0,5,3,4);ref=(3,4,5,0,1,2);ident=tuple(range(6))
    cp=lambda p,q:tuple(p[q[i]] for i in range(6))
    groups=[ident,rot,cp(rot,rot),ref,cp(rot,ref),cp(cp(rot,rot),ref)]
    gi={p:i for i,p in enumerate(groups)}
    # Build coordinate solvers weight by weight, keeping decomposable terms.
    byweight=defaultdict(list)
    for j,v in enumerate(rawbasis):byweight[word_weight(next(iter(v)))].append(j)
    mats={};hs={}
    def pmono(a,p):
        b=[0]*6
        for k,v in enumerate(a):b[OP_TO_OCC[p[OCC_TO_OP[k]]]]=v
        return tuple(b)
    def pv(v,p):
        return {(tuple(pmono(a,p) for a in x[0]),pmono(x[1],p)):c for x,c in v.items()}
    def hom(v):
        check(not lin(dd,v),'group_operation_comparison_is_closed')
        check(not project_vec(v,sdr,ww),'group_operation_comparison_has_zero_class')
        out=boundary_homotopy(v,sdr,ww)
        check(lin(dd,out)==v,'group_operation_integral_homotopy_equation')
        return out
    for z,p in enumerate(groups):
        mats[z]={};hs[z]={}
        for j,v in enumerate(rawbasis):
            rv=raw_perm(v,p);alpha=word_weight(next(iter(rv)))
            inds=byweight[alpha]
            cc=integer_coordinates([cb[i] for i in inds],raw_normalize(rv))
            coords={inds[i]:c for i,c in cc.items()};mats[z][j]=coords
            target=lin({i:co[i] for i in range(len(keys))},coords)
            diff=add(raw_cochain(rv),scale(target,-1));hs[z][j]=hom(diff)
    for a,p in enumerate(groups):
        for b,q in enumerate(groups):
            c=gi[cp(p,q)]
            for j in range(len(keys)):
                check(lin(mats[a],mats[b][j])==mats[c][j],'D3_decomposable_matrices_group_law')
    pairs={}
    for a,p in enumerate(groups):
        for b,q in enumerate(groups):
            ab=gi[cp(p,q)];pairs[a,b]={}
            for j in range(len(keys)):
                v=add(pv(hs[b][j],p),lin(hs[a],mats[b][j]),scale(hs[ab][j],-1))
                pairs[a,b][j]=hom(v)
    triples=0;nonzero_h=0;nonzero_k=0;nonzero_l=0
    for H in hs.values():nonzero_h+=sum(bool(v) for v in H.values())
    for H in pairs.values():nonzero_k+=sum(bool(v) for v in H.values())
    for a,p in enumerate(groups):
        for b,q in enumerate(groups):
            for c,r in enumerate(groups):
                ab=gi[cp(p,q)];bc=gi[cp(q,r)]
                for j in range(len(keys)):
                    v=add(pv(pairs[b,c][j],p),scale(pairs[ab,c][j],-1),pairs[a,bc][j],scale(lin(pairs[a,b],mats[c][j]),-1))
                    L=hom(v);nonzero_l+=bool(L);triples+=1
    return {'relative_basis_columns':len(keys),'operation_weight_bound':maxw,
      'group_elements':6,'pair_equations':36*len(keys),'triple_equations':triples,
      'nonzero_transport_homotopies':nonzero_h,'nonzero_pair_homotopies':nonzero_k,
      'nonzero_triple_homotopies':nonzero_l,'all_transports_use_integral_bar_homotopies':True,
      'higher_than_operation_weight_four':'not enumerated; no full physical action claimed'}

# ---- Normal-cube descent of the actual adjunction maps ----
def normal_cube_audit(T,end):
    P=koszul([ex({i:1}) for i in range(6)]+[ex({9+i:1 for i in T})]);S=tensor_model(P,dual_koszul(end))
    lam=ea(es(es(GAMMA,ex({i:1 for i in range(6)})),ex({9+i:1 for i in T})),ex({9+i:1 for i in end}))
    models={};hist=Counter();cols=0
    for face in subsets(tuple(range(6))):
        A=target_hom(P,lam,'V',face);C=target_hom(S,lam,'V',face)
        f={x:{((x[0],()),x[1]):1} for x in A[0]}
        for x in A[0]:check(lin(C[1],f[x])==lin(f,A[1][x]),'all_Rees_faces_line_counit')
        z=cone_cohom(A[:2],C[:2],f)
        rz,_,piv=fast_reduce(z[0],z[1]);check(not rz,'every_Rees_face_comparison_is_acyclic')
        ra,_,_=fast_reduce(A[0],A[1]);check(ra=={-4:1},'every_Rees_face_relative_endpoint_rank_one')
        models[face]=(A,C,f);cols+=len(A[0])+len(C[0])+len(z[0]);hist[len(face)]+=1
    A0,C0,f0=models[()]
    rd,inc,_=sdr_cycles(A0[0],A0[1]);w=next(iter(inc.values()))
    ep=VP if end==OD else VM;key=(tuple(range(7)),(ep,ep));w=scale(w,w[key])
    for face,(A,C,f) in models.items():
        ws={x:v for x,v in w.items() if x in A[0]}
        check(not lin(A[1],ws) and ws.get(key)==1,'global_primitive_preimage_survives_every_face')
        check(lin(f,ws)=={x:v for x,v in lin(f0,w).items() if x in C[0]},'all_faces_primitive_orbit_lift_naturality')
    arrows=0;squares=0;cubes=0
    for face,(A,C,f) in models.items():
        outside=[i for i in range(6) if i not in face]
        for i in outside:
            nf=tuple(sorted(face+(i,)));AA,CC,ff=models[nf]
            for X,Y in [(A,AA),(C,CC)]:
                for x in X[0]:
                    lhs={y:v for y,v in X[1][x].items() if y in Y[0]}
                    rhs=Y[1].get(x,{})
                    check(lhs==rhs,'all_normal_cube_arrows_are_Hom_chain_maps')
            for x in A[0]:
                check({y:v for y,v in f[x].items() if y in CC[0]}==ff.get(x,{}),'line_counit_normal_base_change_square')
            arrows+=1
        for i,j in combinations(outside,2):
            dst=models[tuple(sorted(face+(i,j)))];squares+=1
            for x in A[0]:
                onepath=x in models[tuple(sorted(face+(i,)))][0][0] and x in dst[0][0]
                other=x in models[tuple(sorted(face+(j,)))][0][0] and x in dst[0][0]
                check(onepath==other,'all_normal_pair_squares_commute')
        for i,j,k in combinations(outside,3):
            cubes+=1
            dst=models[tuple(sorted(face+(i,j,k)))][0][0]
            for x in A[0]:
                check((x in dst)==(x in dst and all(x in models[tuple(sorted(face+(a,)))][0][0] for a in (i,j,k))),
                      'normal_triple_coherence')
    check((arrows,squares,cubes)==(192,240,160),'six_normal_cube_census')
    return {'T':T,'endpoint':'plus' if end==OD else 'minus','faces':64,'arrows':arrows,'squares':squares,'three_cubes':cubes,
            'all_complete_Hom_and_cone_columns':cols,'all_endpoint_fibre_H0':1,'all_endpoint_fibre_H1_Hminus1_Hminus2':0}


def free_R_bar_audit():
    gs=op_generators();letters0=tuple(k for k,v in gs.items() if adeg(v)<=4)
    wt={k:adeg(gs[k]) for k in letters0}
    words=[()]+[(k,) for k in letters0]
    words +=[(a,b) for a in letters0 for b in letters0 if wt[a]+wt[b]<=4]
    deg=lambda w:sum(wt[x] for x in w)
    bars=[()]+[(w,) for w in words if w]
    bars +=[(u,v) for u in words if u for v in words if v and deg(u)+deg(v)<=4]
    gg={};dd={};HH={};proj={};sec={w:{(w,(),()):1} for w in words}
    for l in words:
        for r in words:
            for bs in bars:
                if deg(l)+deg(r)+sum(deg(a) for a in bs)>4:continue
                x=(l,bs,r);n=len(bs);gg[x]=n
                out={}
                if bs:
                    out[(l+bs[0],bs[1:],r)]=1
                    for i in range(1,n):out=add(out,{(l,bs[:i-1]+(bs[i-1]+bs[i],)+bs[i+1:],r):pm(i)})
                    out=add(out,{(l,bs[:-1],bs[-1]+r):pm(n)})
                dd[x]=out
                HH[x]={(l,bs+(r,),()):pm(n+1)} if r else {}
                proj[x]={l+r:1} if not bs else {}
    for x in gg:
        check(not lin(dd,dd[x]),'relative_operation_bar_d_squared')
        check(add(lin(dd,HH[x]),lin(HH,dd[x]))==add({x:1},scale(lin(sec,proj[x]),-1)),
              'relative_operation_bar_free_source_explicit_contraction')
    return {'free_R_bar_columns':len(gg),'maximum_operation_weight':4,'maximum_bar_length':2,
            'bar_resolution_of_free_orbit_contracts_R_linearly':True}


def total_sign_and_group_tests():
    # All five cosimplicial/Hom directions with prefix Koszul signs.
    for p in product(range(-3,4),range(4),range(4),range(4),range(3)):
        for i,j in combinations(range(5),2):
            first=pm(sum(p[:i]));pi=list(p);pi[i]+=1
            ij=first*pm(sum(pi[:j]))
            first2=pm(sum(p[:j]));pj=list(p);pj[j]+=1
            ji=first2*pm(sum(pj[:i]))
            check(ij+ji==0,'five_direction_total_Koszul_cross_square')
    # The actual three normal-presentation indices have the full augmented
    # simplex; no extra physical-cover incidence is assumed.
    gg={s:len(s) for s in subsets((0,1,2))};d={s:{s[:i]+s[i+1:]:pm(i) for i in range(len(s))} for s in gg}
    for s in gg:check(not lin(d,d[s]),'presentation_Cech_d_squared')
    g0={s:len(s)-1 for s in gg if s};d0={s:{v:c for v,c in d[s].items() if v} for s in g0}
    rc,_,_=fast_reduce(g0,d0);check(rc=={0:1},'three_presentation_Cech_integrally_contractible')
    # Normalized group bar, through degree four, for each actual stabilizer.
    group_results={}
    for order in (1,3):
        ident=0;els=tuple(range(1,order));bases={n:list(product(els,repeat=n)) for n in range(5)}
        g={w:-n for n,xs in bases.items() for w in xs};d={w:{} for w in g}
        # Tuple length determines degree, hence () occurs only once.
        for n in range(4):
            for target in bases[n+1]:
                # (delta f)(g1,...,g[n+1]) for trivial coefficient C.
                terms=add({target[1:]:1},{target[:-1]:pm(n+1)})
                for i in range(n):
                    h=(target[i]+target[i+1])%order
                    if h==0:continue # normalized cochain vanishes on identity
                    source=target[:i]+(h,)+target[i+2:]
                    terms=add(terms,{source:pm(i+1)})
                for source,a in terms.items():d[source]=add(d[source],{target:a})
        for x in g:check(not lin(d,d[x]),'normalized_group_bar_d_squared')
        # H0=Z, H1=0 for a finite cyclic stabilizer with trivial integral coefficients.
        # The 1-cocycle law imposes order*f(generator)=0; verify integer determinant
        # of the two independent C3 cocycle equations explicitly.
        if order==3:
            # delta f(1,1)=2f1-f2; delta f(1,2)=f1+f2.
            check(2*1-(-1)*1==3,'C3_H1_integral_detector')
        group_results[str(order)]={'Hminus2':0,'Hminus1':0,'H0':1,'H1':0,
                                   'full_bar_columns_through_four':len(g)}
    return {'five_total_directions':['Hom','Cech','normal_cube','dihedral_bar','operation_bar'],
      'Cech_scope':'the existing normal-presentation simplex; not a new assertion about physical road descent',
      'group_stabilizers':group_results,'primitive_orbit_H0_per_pair':2,'H1_Hminus1_Hminus2':0,
      'full_physical_mixed_totalization_identified':False}


def labelled_target_transport_audit():
    def transform_vertex(v,r,f):return (2*r+(3-v if f else v))%6
    def trans_diag(a,r,f):return diag(transform_vertex(a[0],r,f),transform_vertex(a[1],r,f))
    def sign_sort(vals):return pm(sum(vals[i]>vals[j] for i in range(len(vals)) for j in range(i+1,len(vals))))
    def action_cell(c,r,f):
        ff=tuple(trans_diag(x,r,f) for x in c[0]);hh=tuple(trans_diag(x,r,f) for x in c[1])
        return (tuple(sorted(ff)),tuple(sorted(hh))),pm(f)*sign_sort(ff)*sign_sort(hh)
    def action_exp(e,r,f):
        out=[0]*18
        for a,i in IX.items():
            j=IX[trans_diag(a,r,f)];out[j]=e[i];out[9+j]=e[9+i]
        return tuple(out)
    def action_poly(v,r,f):
        out={}
        for (c,e),a in v.items():
            cc,s=action_cell(c,r,f);out=add(out,{(cc,action_exp(e,r,f)):s*a})
        return out
    for r in range(3):
        for f in range(2):
            for c in CELLS:
                cc,s=action_cell(c,r,f)
                check(action_poly(BD[c],r,f)==scale(BD[cc],s),'six_actual_target_semilinear_chain_maps')
                check(target_side(cc)==target_side(c),'six_actual_target_support_filtration_maps')
                for (t,e),a in BD[c].items():
                    tt,_=action_cell(t,r,f)
                    check(target_legal(tt,action_exp(e,r,f)),'six_actual_target_stalk_domains')
    return {'target_states':len(CELLS),'labelled_transformations':6,'endpoint_labels':'reflection exchanged; no physical parity selected',
            'short_occurrence_permutations':'rotation i->i+2, reflection i->1-i (mod 6)'}


def main_new(path):
    import time
    started=time.time()
    inherited=Path('/mnt/data/check_marici_physical_endpoint_pullback.py')
    provenance={'input_commit':COMMIT,
      'basis':'pinned signed 215-state target and source definitions reconstructed in this standalone file',
      'read_task':'Pasted text(3).txt',
      'new_claim_scope':'explicit adjunction-cone comparison, native normalized bar kernel, and bounded operation enhancement; not the full physical collar'}
    # Code is standalone: these paths are used only for optional provenance, never as imports.
    if inherited.exists():provenance['inherited_checker_sha256']=hashlib.sha256(inherited.read_bytes()).hexdigest()
    labels=[t for t in subsets(OD) if len(t)>=2]
    coefficient=[]
    for T in labels:
        for end in (OD,EV):
            for face in ((),tuple(range(6))):
                coefficient.append(adjunction_case(T,end,face,complete=T in ((1,3),(1,3,5))))
    normal=[normal_cube_audit(T,end) for T in labels for end in (OD,EV)]
    native=native_bar_audit(4)
    orbit=orbit_comparison_audit(4)
    group=group_operation_coherence_audit(4)
    opbar=free_R_bar_audit()
    total=total_sign_and_group_tests()
    target=labelled_target_transport_audit()
    result={
      'status':'relative_adjunction_comparison_constructed_native_low_degree_orbits_retained',
      'provenance':provenance,
      'line_retaining_adjunction_comparison':coefficient,
      'complete_normal_cube':normal,
      'native_bar_source_and_action':native,
      'minimal_native_orbit_comparison':orbit,
      'decomposable_dihedral_homotopies':group,
      'relative_operation_bar':opbar,
      'total_differential_tests':total,
      'actual_target_transport':target,
      'reported_minimal_candidate_pair_cohomology':{'Hminus2':0,'Hminus1':0,'H0':2,'H1':0},
      'fixed_primitive_pair_component':'contractible in the constructed comparison model',
      'primitive_endpoint_obstruction':[0,0],
      'original_endpoint_classes_remain_nonzero':[1,1],
      'candidate_verdicts':{
          'A':'line-retaining adjunction cone: primitive endpoint preimages constructed, no Euler evaluation',
          'B':'existing short-support quotient also retains the primitive class in its fibre; plain endpoint inclusion does not kill it',
          'C':'native augmentation sends the unit to 1, so it cannot put the primitive endpoint unit in its kernel',
          'D':'not required for this comparison test; no pyramid cells adjoined'},
      'full_requested_physical_totalization':'not identified with the constructed conductor/native-bar comparison; the mixed ringed bivariant source/action map is not provided by this calculation',
      'all_check_categories':dict(sorted(COUNT.items())),
      'total_exact_assertions':sum(COUNT.values()),
      'scope':[
       'All eight trace-channel labels remain distinct; two excess labels share each underlying tested Koszul source only up to tensoring their labelled free line.',
       'Literal native bar sources retain their polynomial monomial differential. No cohomology algebra was substituted for those chains.',
       'All nine quadratics, all 81 ordered two-quadratic products, and all relative primitive types through operation weight four are calculated as chain cochains.',
       'The 49-generator freeness theorem is supplied input; the remaining degree-five/six cocycle formulas are defined but their whole modules are not reduced here.',
       'The native orbit construction is an endpoint-facing comparison kernel, not an equality with the original physical source tensor product.',
       'The normal and presentation totalizations are the constructed coefficient diagrams; no unavailable physical multi-road Cech attachment is assumed.',
       'No physical collar/Verdier identification, Branch A conormal map, or physical reflection parity is claimed.',
       'Exact integer chain verification is not proof-assistant verification.'
      ]}
    # Runtime is deliberately excluded from the certificate for reproducibility.
    path.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':result['status'],'assertions':result['total_exact_assertions'],
      'coefficient_cases':len(coefficient),'normal_cube_cases':len(normal),
      'normal_face_count':sum(x['faces'] for x in normal),
      'native_bar_free_left_columns':native['native_free_left_bar_columns'],
      'comparison_fibre_columns_per_endpoint':orbit['plus']['fibre_columns'],
      'candidate_Hminus2_Hminus1_H0_H1':[0,0,2,0],
      'elapsed_seconds':round(time.time()-started,3),'output':str(path)},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('marici_comparison_fibre_adjunction_bar_certificate.json'))
    main_new(parser.parse_args().output)
