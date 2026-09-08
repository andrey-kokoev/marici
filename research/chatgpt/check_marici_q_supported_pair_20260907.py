#!/usr/bin/env python3
"""Supported (t04,t35) dual comparison on the filtered Q lifting problem.

Exact standard-library calculation. All combinatorial/coefficient helpers are
embedded from the preceding checked target, not imported from an unavailable
file. This checks the actual supported dual maps, polynomial homotopies, PC
stalk loss, new lifting ideal, and relation defects. No geometric source-to-
target identification or physical scalar trace is inferred.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from itertools import combinations, product
from pathlib import Path
import hashlib
import json

COMMIT = "d1947b67a60d3e88ba77f4ca60ea02c2a306ee61"
COUNTS: Counter[str] = Counter()


def check(ok: bool, category: str, detail: object = None) -> None:
    if not ok:
        raise AssertionError(f"{category}: {detail!r}")
    COUNTS[category] += 1


def pm(n: int) -> int:
    return -1 if n % 2 else 1


def diag(i: int, j: int) -> tuple[int, int]:
    return tuple(sorted((i % 6, j % 6)))


SHORT = tuple(diag(i, i + 2) for i in range(6))
LONG = tuple(diag(i, i + 3) for i in range(3))
DIAGS = tuple(sorted(SHORT + LONG))
VAR = {d: i for i, d in enumerate(SHORT + LONG)}
PLUS = frozenset(SHORT[i] for i in (1, 3, 5))
MINUS = frozenset(SHORT[i] for i in (0, 2, 4))
ENDPOINTS = {tuple(sorted(PLUS)), tuple(sorted(MINUS))}
ZERO = (0,) * 18
# Coordinates 0:9 are X_short then X_long; 9:15 are t_short; 15:18 are u_long.
# In the independent input only, coordinates 9:15 instead denote u_short.
NAMES = tuple("X" + ''.join(map(str, d)) for d in SHORT + LONG) + tuple(
    ("t" if d in SHORT else "u") + ''.join(map(str, d)) for d in SHORT + LONG)


def cross(a, b):
    i, j = a
    k, l = b
    return i < k < j < l or k < i < l < j


def subsets(xs):
    xs = tuple(sorted(xs))
    for k in range(len(xs) + 1):
        yield from combinations(xs, k)


FACES = tuple(f for k in range(4) for f in combinations(DIAGS, k)
              if all(not cross(a, b) for a, b in combinations(f, 2)))
FACESET = set(FACES)
CELLS = tuple((f, h) for f in FACES for h in subsets(f))


def degree(c):
    f, h = c
    return 3 - len(f) + len(h)


def level(c):
    f = c[0]
    if f in ENDPOINTS:
        return 0
    return 1 if set(f) & set(SHORT) else 2


def mon(xs=(), normal=()):
    m = [0] * 18
    for a in xs:
        m[VAR[a]] += 1
    for a in normal:
        m[9 + VAR[a]] += 1
    return tuple(m)


def plus_support(m):
    return {s for s in PLUS if m[VAR[s]] != 0}


def minus_support(m):
    return {s for s in MINUS if m[VAR[s]] != 0}


def add_m(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub_m(a, b):
    return tuple(x - y for x, y in zip(a, b))


def normalize(c, m, cech=False):
    """Normal form of a monomial in the specified cell's actual coefficient ring."""
    if not cech:
        if any(e < 0 for e in m):
            raise ValueError("Negative exponent in unlocalized ring")
        return None if plus_support(m) and minus_support(m) else m
    localized = set(c[0]) - set(c[1])
    lp, lm = localized & PLUS, localized & MINUS
    if lp and lm:
        return None  # localization of a zero product is the zero ring
    if lp and minus_support(m):
        return None
    if lm and plus_support(m):
        return None
    if not lp and not lm and plus_support(m) and minus_support(m):
        return None
    for a in SHORT:
        if (m[VAR[a]] < 0 or m[9 + VAR[a]] < 0) and a not in localized:
            raise ValueError(f"Illegal short inverse at {c}: {a}, {m}")
    for a in LONG:
        if m[VAR[a]] < 0:
            raise ValueError("Occurrence inversion is not allowed for a long diagonal")
        if m[9 + VAR[a]] < 0 and a not in localized:
            raise ValueError("Long normal inverse outside its Cech summand")
    return m


def add(*vectors):
    out = {}
    for v in vectors:
        for key, n in v.items():
            out[key] = out.get(key, 0) + n
            if not out[key]:
                del out[key]
    return out


def scale(v, n):
    return {key: n * c for key, c in v.items() if n * c}


def basis(c, m=ZERO, n=1, cech=False):
    mm = normalize(c, m, cech)
    return {} if mm is None or n == 0 else {(c, mm): n}


def multiply(v, m, cech=False):
    out = {}
    for (c, a), n in v.items():
        out = add(out, basis(c, add_m(a, m), n, cech))
    return out


def project(v, pred):
    return {key: n for key, n in v.items() if pred(key[0])}


def apply(table, v, cech=False):
    out = {}
    for (c, m), n in v.items():
        out = add(out, scale(multiply(table[c], m, cech), n))
    return out


def graph_substitution_monomial(m):
    out = list(m)
    for s in SHORT:
        out[VAR[s]] += m[9 + VAR[s]]
    return tuple(out)


def graph_substitution(v):
    out = {}
    for (c, m), n in v.items():
        out = add(out, basis(c, graph_substitution_monomial(m), n))
    return out


def independent_d(c):
    f, h = c
    out = {}
    for a in DIAGS:
        ff = tuple(sorted(f + (a,)))
        if a not in f and ff in FACESET:
            out[((ff, h), mon(xs=(a,)))] = pm(sum(b < a for b in f))
    for j, a in enumerate(h):
        hh = tuple(b for b in h if b != a)
        out[((f, hh), mon(normal=(a,)))] = pm(3 - len(f) + j)
    return out


D_INPUT = {c: independent_d(c) for c in CELLS}
D = {c: graph_substitution(v) for c, v in D_INPUT.items()}


def u_m(a):
    return mon(xs=(a,), normal=(a,)) if a in SHORT else mon(normal=(a,))


def cech_d(c):
    if normalize(c, ZERO, True) is None:
        return {}
    f, h = c
    out = {}
    for a in DIAGS:
        ff = tuple(sorted(f + (a,)))
        if a not in f and ff in FACESET:
            out = add(out, basis((ff, h), sub_m(mon(xs=(a,)), u_m(a)),
                                 pm(sum(b < a for b in f)), True))
    for j, a in enumerate(h):
        hh = tuple(b for b in h if b != a)
        out = add(out, basis((f, hh), ZERO, pm(3 - len(f) + j), True))
    return out


DC = {c: cech_d(c) for c in CELLS}


def kappa(v):
    out = {}
    for (c, m), n in v.items():
        denom = ZERO
        for a in set(c[0]) - set(c[1]):
            denom = add_m(denom, u_m(a))
        out = add(out, basis(c, sub_m(m, denom), n, True))
    return out


def set_zero(v, variables):
    variables = set(variables)
    return {key: n for key, n in v.items()
            if all(key[1][i] == 0 for i in variables)}


def derivative_at_conductor(v, s):
    out = {}
    for (c, m), n in v.items():
        if m[VAR[s]] != 1 or any(m[VAR[a]] for a in SHORT if a != s):
            continue
        mm = list(m)
        mm[VAR[s]] = 0
        out = add(out, basis(c, tuple(mm), n))
    return out


def lift_cycle(which, occurrence=None):
    """Universal actual top cycle for each generator of the new lifting ideal."""
    chosen = set(SHORT) if which == "both" else set(PLUS if which == "+" else MINUS)
    out = {}
    for f in FACES:
        if which != "both" and not set(f) <= chosen | set(LONG):
            continue
        xs = tuple(a for a in f if a in LONG)
        if occurrence is not None:
            xs += (occurrence,)
        normals = (chosen - set(f)) | (set(LONG) - set(f))
        out = add(out, basis((f, f), mon(xs=xs, normal=normals),
                             pm(len(f) * (len(f) + 1) // 2)))
    return out


def boundary_top_cycle(active, inactive_subset, occurrence):
    """One of the labelled I_+ or I_- summands in H3(A_boundary)."""
    inactive_subset = set(inactive_subset)
    compat_s = {a for a in active if all(not cross(a, b) for b in inactive_subset)}
    compat_l = {a for a in LONG if all(not cross(a, b) for b in inactive_subset)}
    out = {}
    for f in FACES:
        if not inactive_subset <= set(f) <= inactive_subset | compat_s | compat_l:
            continue
        if f in ENDPOINTS:
            continue
        xs = tuple(a for a in f if a in LONG) + (occurrence,)
        normal = (compat_s | compat_l) - set(f)
        out = add(out, basis((f, f), mon(xs=xs, normal=normal),
                             pm(len(f) * (len(f) + 1) // 2)))
    return out


def ann_member(m):
    if normalize(((), ()), m) is None:
        return True
    support = plus_support(m) or minus_support(m)
    required = set(SHORT) if not support else (PLUS if plus_support(m) else MINUS)
    return all(m[9 + VAR[s]] > 0 for s in required)


def cell_weight(c):
    f, h = c
    w = [0] * 18
    for a in f:
        w[VAR[a]] -= 1
    for a in h:
        w[9 + VAR[a]] += 1
        if a in SHORT:
            w[VAR[a]] += 1
    return tuple(w)


def coefficient_at_grade(c, g):
    m = sub_m(g, cell_weight(c))
    if any(e < 0 for e in m):
        return None
    return normalize(c, m)


def label(d):
    return ''.join(map(str, d))


def action(v, translation, orientation, cech=False):
    out = {}
    for ((f, h), m), n in v.items():
        def perm(d):
            return diag(translation + orientation * d[0], translation + orientation * d[1])
        ff = tuple(perm(d) for d in f)
        hh = tuple(perm(d) for d in h)
        sf = pm(sum(ff[i] > ff[j] for i in range(len(ff)) for j in range(i + 1, len(ff))))
        sh = pm(sum(hh[i] > hh[j] for i in range(len(hh)) for j in range(i + 1, len(hh))))
        mm = [0] * 18
        for d in DIAGS:
            e = perm(d)
            mm[VAR[e]] = m[VAR[d]]
            mm[9 + VAR[e]] = m[9 + VAR[d]]
        out = add(out, basis((tuple(sorted(ff)), tuple(sorted(hh))), tuple(mm), n * sf * sh, cech))
    return out


def encode_vector(v):
    return [{"face": [label(a) for a in c[0]], "marks": [label(a) for a in c[1]],
             "coefficient": n,
             "monomial": {NAMES[i]: e for i, e in enumerate(m) if e}}
            for (c, m), n in sorted(v.items())]




def ring_monomial_ok(m):
    return all(e >= 0 for e in m) and not (plus_support(m) and minus_support(m))


def homogeneous_degree(v):
    vals={add_m(m,cell_weight(c)) for (c,m),n in v.items() if n}
    check(len(vals)==1,'homogeneous_loaded_vector',len(vals))
    return next(iter(vals))


def unit_reduce(matrix):
    """Integer row/column unit pivots. Returns rank and uneliminated block."""
    if not matrix: return 0,[]
    a=[r[:] for r in matrix]
    nr,nc=len(a),len(a[0]); k=0
    while k < min(nr,nc):
        hit=next(((i,j) for i in range(k,nr) for j in range(k,nc)
                  if abs(a[i][j])==1),None)
        if hit is None: break
        i,j=hit; a[k],a[i]=a[i],a[k]
        if j!=k:
            for row in a: row[k],row[j]=row[j],row[k]
        if a[k][k]<0: a[k]=[-z for z in a[k]]
        for i in range(nr):
            if i!=k and a[i][k]:
                q=a[i][k]
                for j in range(k,nc): a[i][j]-=q*a[k][j]
        for j in range(k+1,nc):
            if a[k][j]:
                q=a[k][j]
                for i in range(nr): a[i][j]-=q*a[i][k]
        k+=1
    return k,[row[k:] for row in a[k:]]


def relation_degree(rel,weights):
    vals={add_m(weights[i],m) for (i,m),n in rel.items() if n}
    check(len(vals)==1,'homogeneous_presentation_relation')
    return next(iter(vals))


def relations_in_grade(g,weights,relations,relweights):
    """Expand one exact multigrade of a free-module presentation over B."""
    chosen=[]; coeff={}
    for i,w in enumerate(weights):
        m=sub_m(g,w)
        if ring_monomial_ok(m): chosen.append(i); coeff[i]=m
    pos={i:j for j,i in enumerate(chosen)}
    columns=[]
    for rel,rw in zip(relations,relweights):
        shift=sub_m(g,rw)
        if not ring_monomial_ok(shift): continue
        col=[0]*len(chosen)
        for (i,m),n in rel.items():
            mm=add_m(m,shift)
            if ring_monomial_ok(mm):
                check(i in pos and mm==coeff[i],'relation_grade_coefficient')
                col[pos[i]]+=n
        if any(col): columns.append(col)
    mat=[[col[i] for col in columns] for i in range(len(chosen))]
    return chosen,coeff,mat



PAIR = frozenset((diag(0,4),diag(3,5)))
S_COORD = 9+VAR[diag(0,4)]
T_COORD = 9+VAR[diag(3,5)]


def supported(v, zeros=PAIR, cech=False):
    """Derived coefficient restriction on free/flat target summands.

    A PC summand inverting a zeroed t is the zero ring. It is not evaluated
    as a Laurent polynomial at zero. Other admissible monomials specialize.
    """
    indices={9+VAR[z] for z in zeros}
    out={}
    for (c,m),n in v.items():
        if cech and ((set(c[0])-set(c[1])) & set(zeros)):
            continue
        if any(m[i]<0 for i in indices):
            raise ValueError('Negative supported exponent on a nonzero stalk')
        if any(m[i]>0 for i in indices):
            continue
        out=add(out,basis(c,m,n,cech))
    return out


def differential(v, zeros=PAIR, cech=False, support_level=None):
    out=supported(apply(DC if cech else D,v,cech),zeros,cech)
    if support_level is not None:
        out=project(out,support_level)
    return out


def remaining_lift(zeros, which='both', occurrence=None):
    active=set(SHORT) if which=='both' else set(PLUS if which=='+' else MINUS)
    active-=set(zeros)
    out={}
    for f in FACES:
        if set(f)&set(zeros):continue
        if which!='both' and not set(f)<=active|set(LONG):continue
        xs=tuple(x for x in f if x in LONG)+(() if occurrence is None else (occurrence,))
        coeff=mon(xs=xs,normal=(active|set(LONG))-set(f))
        out=add(out,basis((f,f),coeff,pm(len(f)*(len(f)+1)//2)))
    return out


def remaining_boundary(active,nset,occurrence,zeros=PAIR):
    active=set(active)-set(zeros); nset=set(nset)
    cs={s for s in active if all(not cross(s,n) for n in nset)}
    cl={l for l in LONG if all(not cross(l,n) for n in nset)}
    out={}
    for f in FACES:
        if set(f)&set(zeros) or f in ENDPOINTS:continue
        if not nset<=set(f)<=nset|cs|cl:continue
        out=add(out,basis((f,f),mon(xs=tuple(l for l in f if l in LONG)+(occurrence,),
                                   normal=(cs|cl)-set(f)),pm(len(f)*(len(f)+1)//2)))
    return out


def remaining_seam_factor(active,nset,zeros=PAIR):
    ar=set(active)-set(zeros)
    ir=(set(SHORT)-set(active))-set(zeros)
    nset=set(nset)
    cs={s for s in ar if all(not cross(s,n) for n in nset)}
    cl={l for l in LONG if all(not cross(l,n) for n in nset)}
    return mon(normal=(ir-nset)|(ar-cs)|(set(LONG)-cl))


def divide_known(v,coord):
    out={}
    for (c,m),n in v.items():
        if m[coord]<=0:raise ValueError('Not in the indicated principal ideal')
        mm=list(m);mm[coord]-=1
        out=add(out,basis(c,tuple(mm),n))
    return out


def split_supported_ideal(v):
    va={key:n for key,n in v.items() if key[1][S_COORD]>0}
    vb=add(v,scale(va,-1))
    return divide_known(va,S_COORD),divide_known(vb,T_COORD)


# The supplied dual comparison resolution P^vee. Its q=0,1,2 factor
# positions have ranks 3,4,1, and cohomological differential -M^T,w^T.
F_DUAL={
 (0,0):[(1,1,mon(normal=(diag(3,5),)),1),(1,2,mon(normal=(diag(0,4),)),-1)],
 (0,1):[(1,0,ZERO,-1),(1,2,ZERO,1)],
 (0,2):[(1,1,ZERO,-1),(1,3,ZERO,1)],
 (1,0):[(2,0,mon(normal=(diag(3,5),)),1)],
 (1,1):[(2,0,mon(normal=(diag(0,4),)),1)],
 (1,2):[(2,0,mon(normal=(diag(3,5),)),1)],
 (1,3):[(2,0,mon(normal=(diag(0,4),)),1)],
 (2,0):[]}


def tensor(q,i,v):
    return {(q,i,c,m):n for (c,m),n in v.items()}


def tensor_sum(*vs):
    out={}
    for v in vs:
        for k,n in v.items():
            out[k]=out.get(k,0)+n
            if not out[k]:del out[k]
    return out


def td(v,cech=False):
    out={}
    for (q,i,c,m),n in v.items():
        for qq,ii,a,sign in F_DUAL[q,i]:
            w=multiply(basis(c,m,n,cech),a,cech)
            out=tensor_sum(out,tensor(qq,ii,scale(w,sign)))
        dv=scale(multiply((DC if cech else D)[c],m,cech),pm(q)*n)
        out=tensor_sum(out,tensor(q,i,dv))
    return out


def purity(v,cech=False):
    out={}
    for (q,i,c,m),n in v.items():
        if q==2:
            out=add(out,supported(basis(c,m,-n,cech),PAIR,cech))
    return out


def counit(v,cech=False):
    out={}
    for (q,i,c,m),n in v.items():
        if (q,i)==(0,0):out=add(out,basis(c,m,n,cech))
    return out


def tensor_pc(v):
    out={}
    for (q,i,c,m),n in v.items():
        out=tensor_sum(out,tensor(q,i,kappa(basis(c,m,n))))
    return out


def encode_tensor(v):
    return [{'dual_degree':q,'dual_column':i,'face':list(map(label,c[0])),
             'marks':list(map(label,c[1])),'coefficient':n,
             'monomial':{NAMES[j]:e for j,e in enumerate(m) if e}}
            for (q,i,c,m),n in sorted(v.items())]


def predicted_ann(m,zeros,cech):
    ps=plus_support(m);ms=minus_support(m)
    if ps and ms:return True
    if cech:
        required=(set(PLUS) if ps else set(MINUS) if ms else set(SHORT))-set(zeros)
        return all(m[9+VAR[s]]>0 for s in required)
    zp=set(zeros)&PLUS;zm=set(zeros)&MINUS
    if zp and zm:return False
    if zp:
        return bool(ms) and all(m[9+VAR[s]]>0 for s in MINUS)
    if zm:
        return bool(ps) and all(m[9+VAR[s]]>0 for s in PLUS)
    return ann_member(m)


def kernel_at_grade(g,zeros=PAIR,cech=True,block=None):
    top=[c for c in CELLS if degree(c)==3 and level(c)>0
         and (block is None or set(c[0])&set(zeros)==set(block))
         and coefficient_at_grade(c,g) is not None
         and all(coefficient_at_grade(c,g)[9+VAR[z]]==0 for z in zeros)]
    rows=defaultdict(dict)
    signs={c:pm(len(c[0])*(len(c[0])+1)//2) for c in top}
    for c in top:
        v=basis(c,coefficient_at_grade(c,g))
        for key,n in differential(v,zeros,cech,lambda t:level(t)>0).items():
            rows[key][c]=n*signs[c]
    parent={c:c for c in top}
    def find(c):
        while parent[c]!=c:
            parent[c]=parent[parent[c]];c=parent[c]
        return c
    def union(a,b):
        aa,bb=find(a),find(b)
        if aa!=bb:parent[aa]=bb
    pins=[]
    for row in rows.values():
        check(len(row)<=2 and all(abs(n)==1 for n in row.values()),'supported_fine_degree_unit_rows')
        if len(row)==1:pins.append(next(iter(row)))
        elif len(row)==2:
            check(sum(row.values())==0,'supported_fine_degree_sign_gauge')
            union(*row.keys())
    pinned={find(c) for c in pins}
    comps=sorted({find(c) for c in top}-pinned)
    reps={r:next(c for c in top if find(c)==r) for r in comps}
    return top,find,pinned,comps,reps,signs


def all_ideal_relations(shorts,remaining_plus,remaining_minus):
    ids={s:i+1 for i,s in enumerate(shorts)}
    rels=[];names=[]
    for s in shorts:
        opp=remaining_minus if s in PLUS else remaining_plus
        rels.append({(0,mon(xs=(s,))):1,(ids[s],mon(normal=opp)):-1})
        names.append('seam_'+label(s))
    for active in (PLUS,MINUS):
        for a,b in combinations(sorted(active),2):
            rels.append({(ids[a],mon(xs=(b,))):1,(ids[b],mon(xs=(a,))):-1})
            names.append('koszul_'+label(a)+'_'+label(b))
        for a in sorted(active):
            for b in sorted(set(SHORT)-set(active)):
                rels.append({(ids[a],mon(xs=(b,))):1})
                names.append('ann_'+label(b)+'_'+label(a))
    return rels,names


def image_relation(rel,images):
    return add(*(scale(multiply(images[i],m),n) for (i,m),n in rel.items()))


def encode_relation(rel,names):
    return [{'generator':names[i],'coefficient':n,
             'monomial':{NAMES[j]:e for j,e in enumerate(m) if e}}
            for (i,m),n in sorted(rel.items())]


def execute(output:Path, exhaustive:bool=True):
    print('Checking full maps and support squares...',flush=True)
    check(len(CELLS)==215,'original_215_cells_retained')
    check(cross(*sorted(PAIR)),'supported_pair_is_crossing_not_a_face')
    check(max(map(degree,CELLS))==3,'no_target_degree_four')
    pc_blocks=Counter();zero_pc=0;zero_pair=0
    for c in CELLS:
        check(not apply(D,D[c]),'original_d_squared')
        check(kappa(D[c])==apply(DC,kappa(basis(c)),True),'full_finite_PC_comparison')
        for pc in (False,True):
            v=supported(basis(c,cech=pc),PAIR,pc)
            dv=differential(v,PAIR,pc)
            check(not differential(dv,PAIR,pc),'supported_d_squared')
            if v and pc:
                block=tuple(sorted(set(c[0])&PAIR));pc_blocks[block]+=1
                check(set(c[0])&PAIR==set(c[1])&PAIR,'surviving_pair_labels_are_marked')
                check(all(tuple(sorted(set(t[0])&PAIR))==block for t,_ in dv),
                      'supported_PC_direct_summand_equations')
            for q,i in F_DUAL:
                vv=tensor(q,i,basis(c,cech=pc)); dd=td(vv,pc)
                check(not td(dd,pc),'entire_dual_tensor_d_squared')
                check(purity(dd,pc)==differential(purity(vv,pc),PAIR,pc),
                      'supplied_purity_chain_map_all_cells')
                check(counit(dd,pc)==apply(DC if pc else D,counit(vv,pc),pc),
                      'supplied_counit_chain_map_all_cells')
                for predicate in (lambda z:level(z)>0,lambda z:level(z)==2):
                    proj_v={key:n for key,n in vv.items() if predicate(key[2])}
                    check(project(purity(vv,pc),predicate)==purity(proj_v,pc),
                          'purity_endpoint_and_Q_squares')
        if not basis(c,cech=True):zero_pc+=1
        elif not supported(basis(c,cech=True),PAIR,True):zero_pair+=1
        for q,i in F_DUAL:
            vv=tensor(q,i,basis(c))
            check(tensor_pc(td(vv))==td(tensor_pc(vv),True),'dual_tensor_localization_square')
            check(supported(kappa(purity(vv)),PAIR,True)==purity(tensor_pc(vv),True),
                  'purity_localization_square')

    theta=basis(((),()),mon(normal=LONG))
    for l in LONG:
        theta=add(theta,basis(((l,),(l,)),mon(xs=(l,),normal=set(LONG)-{l}),-1))
    beta=apply(D,theta)
    check(len(beta)==18,'eighteen_term_primary_boundary')
    check(not apply(D,beta),'primary_boundary_closed')
    check(not project(differential(theta,PAIR,False),lambda c:level(c)==2),'supported_generic_cycle')
    beta_pc=differential(theta,PAIR,True)
    check(beta_pc and differential(theta,PAIR,False),'primary_representatives_not_zero')

    print('Constructing old-defect nullhomotopies...',flush=True)
    shorts=tuple(sorted(SHORT));old0=lift_cycle('both');oldrecords=[]
    check(not apply(D,old0),'old_common_full_cycle')
    check(not supported(old0),'old_common_specializes_to_zero')
    for a in shorts:
        active=PLUS if a in PLUS else MINUS;opp=set(SHORT)-set(active)
        olda=lift_cycle('+' if a in PLUS else '-',a)
        olddef=add(multiply(old0,mon(xs=(a,))),scale(multiply(olda,mon(normal=opp)),-1))
        check(olddef and not apply(D,olddef),'old_relation_defect_full_cycle')
        check(not supported(olddef),'old_six_defects_zero_on_support')
        aa,bb=split_supported_ideal(olddef)
        cc=divide_known(apply(D,aa),T_COORD)
        check(apply(D,bb)==scale(multiply(cc,mon(normal=(diag(0,4),))),-1),
              'old_defect_two_parameter_syzygy')
        check(not apply(D,cc),'old_defect_coherence_closed')
        witness=tensor_sum(tensor(1,1,scale(aa,-1)),tensor(1,2,scale(bb,-1)),
                           tensor(0,0,scale(cc,-1)))
        eta_def=tensor(2,0,scale(olddef,-1))
        check(td(witness)==eta_def,'explicit_old_defect_boundary_in_dual_tensor')
        check(not purity(eta_def),'old_defect_purity_zero')
        check(td(tensor_pc(witness),True)==tensor_pc(eta_def),'old_defect_PC_boundary_witness')
        check(all(level(c)<2 for _,_,c,_ in witness),'witness_retains_boundary_support')
        oldrecords.append({'short':label(a),'full_defect_terms':len(olddef),
              'quotient_defect_terms':len(project(olddef,lambda c:level(c)>0)),
              'witness_terms':len(witness),'full_defect':encode_vector(olddef),
              'nullhomotopy_in_supplied_dual':encode_tensor(witness)})

    rp=set(PLUS)-PAIR;rm=set(MINUS)-PAIR
    gs=[mon(normal=rp|rm)]+[mon(xs=(a,),normal=rp if a in PLUS else rm) for a in shorts]
    names=['Lambda0_supported']+['Lambda_'+label(a)+'_supported' for a in shorts]
    lifts=[remaining_lift(PAIR)]+[remaining_lift(PAIR,'+' if a in PLUS else '-',a) for a in shorts]
    print('Checking newly derived PC lifts and six relation defects...',flush=True)
    for g,v in zip(gs,lifts):
        check(not differential(v,PAIR,True),'new_seven_PC_lifts_closed')
        check(project(v,lambda c:level(c)==2)==multiply(theta,g),'new_seven_generic_coefficients')
        check(differential(v,PAIR,False)!= {},'new_PC_lifts_are_not_absolute_lifts')
    check(len(lifts[0])==23 and all(len(v)==12 for v in lifts[1:]),'new_lift_term_counts')
    rels,rnames=all_ideal_relations(shorts,rp,rm)
    check(len(rels)==30,'new_ideal_thirty_relations')
    defects=[image_relation(r,lifts) for r in rels]
    for i,(r,v) in enumerate(zip(rels,defects)):
        out={}
        for (j,m),n in r.items():
            mm=add_m(gs[j],m)
            if ring_monomial_ok(mm):out[mm]=out.get(mm,0)+n
        check(not {m:n for m,n in out.items() if n},'supported_ideal_relation')
        check(bool(v)==(i<6),'exactly_six_new_relation_defects')
        check(not differential(v,PAIR,True),'new_defect_is_PC_cycle')
        check(all(level(c)==1 for c,_ in v),'new_defect_has_no_generic_or_endpoint_terms')
        if i<6:check(len(v)==11,'eleven_terms_per_new_defect')

    mkeys=[];mvectors=[]
    for active,sgn in ((PLUS,'+'),(MINUS,'-')):
        inactive=(set(SHORT)-set(active))-PAIR
        for ns in subsets(inactive):
            if not ns:continue
            for a in sorted(active):
                v=remaining_boundary(active,ns,a)
                check(v and not differential(v,PAIR,True),'new_boundary_generators_closed')
                check(all(level(c)==1 and not(set(c[0])&PAIR) for c,_ in v),
                      'new_boundary_generators_in_generic_block')
                mkeys.append((sgn,ns,a));mvectors.append(v)
    check(len(mkeys)==18,'eighteen_ideal_generators_six_summands')
    images=lifts+mvectors
    names+=['M'+sgn+'_'+'_'.join(map(label,ns))+'_X'+label(a) for sgn,ns,a in mkeys]
    pos={key:i+7 for i,key in enumerate(mkeys)}
    decomps=[];symbol_records=[]
    for i,a in enumerate(shorts):
        active=PLUS if a in PLUS else MINUS;sgn='+' if a in PLUS else '-'
        inactive=(set(SHORT)-set(active))-PAIR
        dec={};component_data=[]
        for ns in subsets(inactive):
            if not ns:continue
            fac=remaining_seam_factor(active,ns)
            dec[(pos[(sgn,ns,a)],fac)]=1
            tau=mon(normal=inactive)
            colon=tuple(max(0,u-v) for u,v in zip(tau,fac))
            check(colon==mon(normal=ns),'new_symbol_exact_colon_ideal')
            component_data.append({'inactive_subset':list(map(label,ns)),
                  'coefficient':{NAMES[j]:e for j,e in enumerate(fac) if e},
                  'annihilator_monomial':{NAMES[j]:e for j,e in enumerate(colon) if e}})
        check(image_relation(dec,images)==defects[i],'new_defect_three_component_decomposition')
        check(len(dec)==3,'three_independent_new_symbol_components')
        lcm=tuple(max(mon(normal=ns)[j] for ns in subsets(inactive) if ns) for j in range(18))
        check(lcm==mon(normal=inactive),'full_side_symbol_annihilator')
        decomps.append(dec)
        symbol_records.append({'short':label(a),'defect':encode_vector(defects[i]),
                               'decomposition':component_data})

    hrels=[];hrnames=[]
    for active,sgn in ((PLUS,'+'),(MINUS,'-')):
        inactive=(set(SHORT)-set(active))-PAIR
        for ns in subsets(inactive):
            if not ns:continue
            for a,b in combinations(sorted(active),2):
                hrels.append({(pos[sgn,ns,a],mon(xs=(b,))):1,(pos[sgn,ns,b],mon(xs=(a,))):-1})
                hrnames.append('M_koszul_'+sgn+'_'+str(ns)+'_'+label(a)+'_'+label(b))
            for a in sorted(active):
                for b in sorted(set(SHORT)-set(active)):
                    hrels.append({(pos[sgn,ns,a],mon(xs=(b,))):1})
                    hrnames.append('M_ann_'+sgn+'_'+str(ns)+'_'+label(a)+'_'+label(b))
    check(len(hrels)==72,'seventy_two_internal_ambiguity_relations')
    for i,r in enumerate(rels):
        rr=dict(r)
        if i<6:
            for k,n in decomps[i].items():rr[k]=-n
        hrels.append(rr);hrnames.append(rnames[i])
    check((len(images),len(hrels))==(25,102),'supported_generic_block_presentation_size')
    for name,r in zip(hrnames,hrels):
        check(not image_relation(r,images),'all_102_relations_vanish_as_target_chains',name)

    for a in shorts:
        cochain=[defects[shorts.index(a)]]+[{} for _ in shorts]
        for r,v in zip(rels,defects):
            check(image_relation(r,cochain)==multiply(v,mon(xs=(a,))),
                  'new_extension_short_occurrence_nullcochain')
    cochain=[{}]+[scale(multiply(defects[i],mon(normal=rp if a in PLUS else rm)),-1)
                  for i,a in enumerate(shorts)]
    for r,v in zip(rels,defects):
        check(image_relation(r,cochain)==multiply(v,mon(normal=rp|rm)),
              'new_extension_four_Rees_product_nullcochain')

    print('Computing integral homogeneous kernel and presentation checks...',flush=True)
    weights=[homogeneous_degree(v) for v in images]
    rweights=[relation_degree(r,weights) for r in hrels]
    gs_test=set(weights+rweights)
    for occ in [()]+[(a,) for a in shorts]+[(a,a) for a in shorts]:
        for rs in subsets(rp|rm):
            gs_test.add(add_m(mon(xs=occ,normal=rs),mon(normal=LONG)))
    for p in PLUS:
        for m in MINUS:
            for rs in subsets(rp|rm):
                gs_test.add(add_m(mon(xs=(p,m),normal=rs),mon(normal=LONG)))
    presentation_checks=0
    for g in sorted(gs_test):
        chosen,coeff,rmat=relations_in_grade(g,weights,hrels,rweights)
        check(all(all(coeff[i][9+VAR[z]]==0 for z in PAIR) for i in chosen),
              'presentation_stays_on_actual_support')
        rank,res=unit_reduce(rmat)
        check(not any(x for row in res for x in row),'supported_relation_smith_all_unit')
        top,find,pins,comps,reps,signs=kernel_at_grade(g,PAIR,True,())
        columns=[]
        for i in chosen:
            vv=multiply(images[i],coeff[i])
            check(not differential(vv,PAIR,True),'presentation_image_full_kernel')
            col=[]
            for comp in comps:
                c=reps[comp];m=coefficient_at_grade(c,g)
                col.append(vv.get((c,m),0)*signs[c])
            columns.append(col)
        imat=[[col[i] for col in columns] for i in range(len(comps))]
        irank,ires=unit_reduce(imat)
        check(not any(x for row in ires for x in row),'supported_generators_saturated_image')
        check(irank==len(comps),'supported_presentation_spans_entire_top_kernel',g)
        check(len(chosen)-rank==len(comps),'supported_presentation_no_missing_relations',g)
        presentation_checks+=1

    print('Testing supported-normal patterns against actual target kernels...',flush=True)
    pattern_records=[];kernel_tests=0
    sets=list(subsets(SHORT)) if exhaustive else [tuple(sorted(PAIR))]
    for zeros_tuple in sets:
        zeros=frozenset(zeros_tuple);rem=set(SHORT)-zeros
        local_count=0;outcome=Counter()
        for occ in [()]+[(a,) for a in shorts]:
            for ns in subsets(rem):
                coeff=mon(xs=occ,normal=ns);g=add_m(coeff,mon(normal=LONG))
                for pc in (False,True):
                    top,find,pins,comps,reps,signs=kernel_at_grade(g,zeros,pc)
                    empty=((),())
                    check(empty in top,'generic_coefficient_exists_after_support')
                    lifts_unit=find(empty) not in pins
                    check(lifts_unit==predicted_ann(coeff,zeros,pc),
                          'all_support_primary_ideal_theorem',(zeros_tuple,occ,ns,pc))
                    local_count+=1;kernel_tests+=1
                    outcome[('PC' if pc else 'absolute')+('_lifts' if lifts_unit else '_obstructed')]+=1
        for occ in [None]+list(shorts):
            v=remaining_lift(zeros,'both' if occ is None else '+' if occ in PLUS else '-',occ)
            check(not differential(v,zeros,True),'all_support_PC_generator_cycles')
        pattern_records.append({'zero_normals':list(map(label,zeros_tuple)),
              'remaining_plus':list(map(label,sorted(set(PLUS)-zeros))),
              'remaining_minus':list(map(label,sorted(set(MINUS)-zeros))),
              'exact_kernel_tests':local_count,'outcomes':dict(outcome)})

    print('Checking labelled symmetry and exporting...',flush=True)
    for rotation in (0,2,4):
        for orientation in (1,-1):
            rot=(rotation+(3 if orientation == -1 else 0))%6
            def perm(a):return diag(rot+orientation*a[0],rot+orientation*a[1])
            zz=frozenset(perm(z) for z in PAIR)
            for c in CELLS:
                left=action(differential(supported(basis(c,cech=True),PAIR,True),PAIR,True),rot,orientation,True)
                right=differential(supported(action(basis(c,cech=True),rot,orientation,True),zz,True),zz,True)
                check(left==right,'labelled_supported_D3_chain_covariance')
            for occ,v in zip([None]+list(shorts),lifts):
                if occ is None:target=remaining_lift(zz)
                else:
                    newocc=perm(occ)
                    target=remaining_lift(zz,'+' if newocc in PLUS else '-',newocc)
                check(action(v,rot,orientation)==target,'labelled_new_lift_covariance')

    # The three labelled rotations of the supplied pair cover the six short
    # Rees coordinates. Their composite is a separately typed codimension-six
    # dual-support operation, not silently the original native source functor.
    orbit_pairs=[]
    for rot in (0,2,4):
        orbit_pairs.append(tuple(diag(rot+a,rot+b) for a,b in ((0,4),(3,5))))
    check(set().union(*map(set,orbit_pairs))==set(SHORT),'three_rotated_pairs_cover_six_normals')
    check(sum(len(set(a)&set(b)) for a,b in combinations(orbit_pairs,2))==0,
          'three_pairs_are_disjoint_regular_parameters')
    from itertools import permutations
    for order in permutations(range(3)):
        for c in CELLS:
            v=basis(c,cech=True)
            for i in order:v=supported(v,orbit_pairs[i],True)
            check(v==supported(basis(c,cech=True),SHORT,True),
                  'all_six_orders_same_derived_PC_support')
            check(supported(apply(DC,basis(c,cech=True),True),SHORT,True)==
                  differential(v,SHORT,True),'orbit_support_chain_square')
    full_support_blocks=Counter()
    for c in CELLS:
        if supported(basis(c,cech=True),SHORT,True):
            full_support_blocks[tuple(sorted(set(c[0])&set(SHORT)))]+=1
        if level(c)==2:
            dv=differential(basis(c),SHORT,True)
            check(all(level(t)==2 for t,_ in dv),'six_normal_Q_inclusion_is_chain_map')
            check(project(dv,lambda t:level(t)==2)==dv,'six_normal_Q_section_square')
    check(not differential(theta,SHORT,True),'six_normal_generic_unit_is_closed')
    check(full_support_blocks[()]==7,'full_seven_state_Q_direct_summand')
    check(sum(1 for c in CELLS if level(c)==0 and supported(basis(c,cech=True),SHORT,True))==2,
          'both_endpoints_survive_in_their_supported_grades')
    # Reordering two rank-two normal factors has sign (-1)^4=+1.
    check(pm(2*2)==1,'ordered_pair_blocks_even_commutation')
    ordered_normals=[a for pair in orbit_pairs for a in pair]
    for rotation in (0,2,4):
        for orient in (1,-1):
            rot=(rotation+(3 if orient == -1 else 0))%6
            image=[diag(rot+orient*a,rot+orient*b) for a,b in ordered_normals]
            indices=[ordered_normals.index(a) for a in image]
            determinant=pm(sum(indices[i]>indices[j] for i in range(6) for j in range(i+1,6)))
            endpoint_sign=1
            for first,second in orbit_pairs:
                aa=diag(rot+orient*first[0],rot+orient*first[1])
                endpoint_sign *= 1 if aa in MINUS else -1
            check(determinant*endpoint_sign==1,'orbit_endpoint_and_determinant_orientation_cancel')
    orbit_record={
      'ordered_rotated_pairs':[[label(a) for a in pair] for pair in orbit_pairs],
      'operation':'Tensor the three independently specified rotated P_pair duals, or equivalently ordered six-parameter Koszul duality; cohomological support placement [-6].',
      'supported_Q_retraction':'E_PC after all six t=0 splits as Q plus supported boundary blocks; inclusion on all seven Q states is a strict chain map.',
      'primitive_Q_unit_lifts':True,
      'coefficient_linearity_obstruction_after_all_six':0,
      'source_identification':'Not supplied: the native physical source is not shown to factor through the triple-dualized domain.',
      'nonzero_PC_stalks':sum(full_support_blocks.values()),
      'nonzero_endpoint_stalks':2,
      'direct_blocks':[{'short_marked_support':list(map(label,k)),'stalks':v} for k,v in sorted(full_support_blocks.items())]
    }

    result={
       'status':'proved_scoped_supported_dual_and_recomputed_PC_lifting_obstructions',
       'date':'2026-09-07','source_commit':COMMIT,
       'input_artifact_sha256':{'check_marici_q_lift_naturality_20260907.py': '66a8245add48efc65e820cf571dab438d925f62cdc6a8a32b59500a2872cbc20', 'marici_q_graded_lift_naturality_20260907.md': '0c8507fc48e84bd945d4a9515a666c337e29bd239354f7f3d6ecdbe24f0927ea', 'check_marici_q_alternating_rees_base_change.py': 'f4c4a4bc9299fbdf30fa893f575d1a24b9a80edd3b87c9ba98899363a2ee6783'},
       'supported_dual_source':'supported_gysin_proof.md, library version 1, 2026-09-07; ordered t04,t35 matrices and top -z^vee convention retained',
       'support':list(map(label,sorted(PAIR))),
       'operation':'supplied ordered dual comparison P^vee, top -z^vee ->1 modulo (t04,t35); retains endpoint line and ordered conormal determinant',
       'independent_u03_normal':'Retained as an external Koszul-dual identity factor when required; not identified with channel orientation or removed.',
       'original_target_cells':215,
       'original_zero_PC_stalks':zero_pc,
       'additional_zero_PC_stalks_on_pair':zero_pair,
       'surviving_PC_blocks':{'/'.join(map(label,k)) or 'empty':v for k,v in pc_blocks.items()},
       'old_defects':oldrecords,
       'rotated_pair_composite':orbit_record,
       'old_six_defects_image':'zero, with explicit boundaries in supplied dual tensor before specialization',
       'primary_absolute_annihilator':'(0)',
       'primary_PC_annihilator':'(sigma_plus*sigma_minus, sigma_plus*I_plus, sigma_minus*I_minus)',
       'sigma_plus':'t13*t15','sigma_minus':'t02*t24',
       'new_generic_block_ambiguity':'I_plus^3 + I_minus^3 (not a free rank-six B module)',
       'new_extension_annihilator':'I_plus + I_minus + (t13*t15*t02*t24)',
       'new_extension_cyclic_module':'C/(t04,t35,t13*t15*t02*t24)',
       'new_defects':symbol_records,
       'generic_block_generators':[{'name':n,'vector':encode_vector(v)} for n,v in zip(names,images)],
       'generic_block_relations':[{'name':n,'terms':encode_relation(r,names)} for n,r in zip(hrnames,hrels)],
       'integral_presentation_grade_tests':presentation_checks,
       'supported_pattern_kernel_tests':kernel_tests,
       'supported_pattern_records':pattern_records,
       'primary_beta_PC_terms_after_pair':len(beta_pc),
       'primary_beta_PC':encode_vector(beta_pc),
       'primary_beta_absolute_terms_after_pair':len(differential(theta,PAIR,False)),
       'counts':dict(sorted(COUNTS.items())),
       'total_exact_assertions':sum(COUNTS.values()),
       'scope':[
         'Application of an already supplied supported-dual functor to the fixed target, not a native-source physical identification.',
         'All endpoint cells, the full support sequence and the seven-state Q quotient retained before taking indicated honest subquotients.',
         'Absolute and PC targets have different supported primary annihilators; no equivalence between them claimed.',
         'New lifts are reconstructed in the supported complex, not images of the seven old generators, whose generic coefficients specialize to zero.',
         'No scalar replacement of Rees parameters by one. Quotient and normal determinant have their proper supports and shifts.',
         'No new cells are added to kill relations. Free presentations record actual target cycles and relations only.',
         'The all-degree claims use polynomial divisibility and kernel decomposition proofs, not finite grade tests alone.',
         'The three rotated supported-pair functors have an explicitly computed composite on this target; their composite domain is not identified with the native physical source.'
       ]}
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','original_zero_PC_stalks','additional_zero_PC_stalks_on_pair','surviving_PC_blocks','primary_absolute_annihilator','primary_PC_annihilator','new_extension_annihilator','integral_presentation_grade_tests','supported_pattern_kernel_tests','total_exact_assertions')},indent=2),flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('marici_q_supported_pair_certificate_20260907.json'))
    parser.add_argument('--pair-only',action='store_true',help='Skip the other 63 coordinate-support control patterns')
    args=parser.parse_args()
    execute(args.output,not args.pair_only)
