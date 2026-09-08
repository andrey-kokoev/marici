#!/usr/bin/env python3
"""Local lifts and nonzero Cech descent on the exact Q-obstruction complement.

Standard-library exact arithmetic, Python 3.10+.
Reconstructs the 215-state target and the seven principal-open local lifts.
Computes the actual overlap defects, their twelve labelled residue components,
both endpoint discrepancies, and all 6,848 monomial sign-pattern Cech complexes.
The prior top homology presentation is an explicit prerequisite, not re-proved
by the new cover calculation. Its source routines are embedded for standalone
execution. No network, native-base inversions, or repository writes are used.
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



# The seven principal opens cover Spec(B) minus V(a).
PP = tuple(sorted(PLUS)); MM = tuple(sorted(MINUS))
COVER = (None,) + PP + MM
PATCHES = tuple(s for k in range(1,8) for s in combinations(range(7),k)
                if not (any(1<=i<=3 for i in s) and any(4<=i<=6 for i in s)))
PATCH_DEG = {q:tuple(s for s in PATCHES if len(s)==q+1) for q in range(4)}
TEXP = mon(normal=SHORT)
PAEXP = mon(normal=PLUS)
MBEXP = mon(normal=MINUS)


def raw_shift(v, exp):
    """Laurent expression; validity is checked in a particular open below."""
    return {(c,add_m(m,exp)):n for (c,m),n in v.items()}


def patch_normalize(cell, exp, patch, pc=False):
    base_x={COVER[i] for i in patch if i}
    base_t=set(SHORT) if 0 in patch else (set(PLUS) if any(i<=3 for i in patch) else set(MINUS))
    cell_l=set(cell[0])-set(cell[1]) if pc else set()
    inv_x=base_x | (cell_l & set(SHORT))
    inv_t=base_t | (cell_l & set(SHORT))
    fp,fm=inv_x & PLUS, inv_x & MINUS
    if fp and fm: return None
    xp={a for a in PLUS if exp[VAR[a]]}
    xm={a for a in MINUS if exp[VAR[a]]}
    if (fp and xm) or (fm and xp) or (xp and xm): return None
    for a in SHORT:
        if exp[VAR[a]]<0 and a not in inv_x: raise ValueError(('illegal X pole',a,patch,cell))
        if exp[9+VAR[a]]<0 and a not in inv_t: raise ValueError(('illegal t pole',a,patch,cell))
    for a in LONG:
        if exp[VAR[a]]<0: raise ValueError('long occurrence inverted')
        if exp[9+VAR[a]]<0 and (not pc or a not in cell_l): raise ValueError('long normal pole')
    return exp


def localize(v, patch, pc=False):
    out={}
    for (c,m),n in v.items():
        e=patch_normalize(c,m,patch,pc)
        if e is not None: out=add(out,{(c,e):n})
    return out


def ld(v, patch, pc=False):
    out={}
    table=D_PC if pc else D
    for (c,m),n in localize(v,patch,pc).items():
        for (target,z),a in table[c].items():
            term={(target,add_m(m,z)):n*a}
            out=add(out,localize(term,patch,pc))
    return out


def generic_part(v): return project(v,lambda c:level(c)==2)
def endpoint_part(v): return project(v,lambda c:level(c)==0)
def e_part(v): return project(v,lambda c:level(c)>0)


def gamma_raw(active,N,include_endpoint=False):
    N=set(N)
    compatible_s={p for p in active if all(not cross(p,n) for n in N)}
    compatible_l={l for l in LONG if all(not cross(l,n) for n in N)}
    v={}
    for f in FACES:
        if not N<=set(f)<=N|compatible_s|compatible_l: continue
        if not include_endpoint and f in ENDPOINTS: continue
        m=mon(xs=set(f)&set(LONG),normal=(compatible_s|compatible_l)-set(f))
        v=add(v,basis((f,f),m,pm(len(f)*(len(f)+1)//2)))
    numerator=mon(normal=set(LONG)-compatible_l)
    denominator=mon(normal=N|compatible_s)
    return v,sub_m(numerator,denominator),compatible_s,compatible_l


def act_raw(v,tr,orientation):
    out={}
    for ((f,h),m),n in v.items():
        perm=lambda a:diag(tr+orientation*a[0],tr+orientation*a[1])
        ff=tuple(map(perm,f));hh=tuple(map(perm,h))
        sign=pm(sum(ff[i]>ff[j] for i in range(len(ff)) for j in range(i+1,len(ff))))
        sign*=pm(sum(hh[i]>hh[j] for i in range(len(hh)) for j in range(i+1,len(hh))))
        e=[0]*18
        for a in DIAGS:
            t=perm(a);e[VAR[t]]=m[VAR[a]];e[9+VAR[t]]=m[9+VAR[a]]
        key=((tuple(sorted(ff)),tuple(sorted(hh))),tuple(e))
        out=add(out,{key:n*sign})
    return out


def unit_reduce(mat):
    if not mat: return 0,[]
    a=[r[:] for r in mat];nr=len(a);nc=len(a[0]);k=0
    while k<min(nr,nc):
        p=next(((i,j) for i in range(k,nr) for j in range(k,nc) if abs(a[i][j])==1),None)
        if p is None: break
        i,j=p;a[k],a[i]=a[i],a[k]
        for row in a:row[k],row[j]=row[j],row[k]
        if a[k][k]<0:a[k]=[-x for x in a[k]]
        for i in range(nr):
            if i!=k and a[i][k]:
                q=a[i][k];a[i]=[x-q*y for x,y in zip(a[i],a[k])]
        for j in range(nc):
            if j!=k and a[k][j]:
                q=a[k][j]
                for i in range(nr):a[i][j]-=q*a[i][k]
        k+=1
    return k,[row[k:] for row in a[k:]]


def allowed(module, ex, normal, patch):
    """One monomial fine degree of O, I+, or I- on a cover intersection.

    ex: 6 exponents in PP+MM order. normal: same order, for t.
    Only signs matter. I+ on a patch with X+ inverted is the full ring.
    """
    hasp=any(1<=i<=3 for i in patch);hasm=any(4<=i<=6 for i in patch)
    xp=any(ex[:3]);xm=any(ex[3:])
    if (xp and xm) or (hasp and xm) or (hasm and xp):return False
    if module=='+' and (hasm or xm):return False
    if module=='-' and (hasp or xp):return False
    invx={i-1 for i in patch if i}
    invt=set(range(6)) if 0 in patch else (set(range(3)) if hasp else set(range(3,6)))
    if any(e<0 and i not in invx for i,e in enumerate(ex)):return False
    if any(e<0 and i not in invt for i,e in enumerate(normal)):return False
    if module=='+' and not hasp and not any(e>0 for e in ex[:3]):return False
    if module=='-' and not hasm and not any(e>0 for e in ex[3:]):return False
    return True


def matrices(module,ex,normal):
    bs={q:tuple(p for p in PATCH_DEG[q] if allowed(module,ex,normal,p)) for q in range(4)}
    ds=[]
    for q in range(3):
        a=[[0]*len(bs[q]) for _ in bs[q+1]];index={p:i for i,p in enumerate(bs[q])}
        for j,p in enumerate(bs[q+1]):
            for k in range(len(p)):
                face=p[:k]+p[k+1:]
                if face in index:a[j][index[face]]=pm(k)
        ds.append(a)
    return bs,ds


def rankmat(a):
    k,tail=unit_reduce(a)
    check(not any(x for row in tail for x in row),'integral_unit_smith')
    return k


def predicted(module,ex,normal):
    negp=any(e<0 for e in normal[:3]);negm=any(e<0 for e in normal[3:])
    xp=any(ex[:3]);xm=any(ex[3:]);out=[0]*4
    if module=='O' and not xp and not xm:
        out[0]=int(not negp and not negm);out[1]=int(negp and negm);return out
    side=module if module!='O' else ('+' if xp else '-')
    a=ex[:3] if side=='+' else ex[3:]
    inactive=negm if side=='+' else negp
    if not any(a):out[1]=int(inactive)
    else:
        out[0]=int(all(e>=0 for e in a) and not inactive)
        out[3]=int(all(e<0 for e in a) and inactive)
    return out


def dot(row,v):return sum(a*b for a,b in zip(row,v))


def cohomology(module,ex,normal):
    bs,ds=matrices(module,ex,normal)
    for q in range(2):
        left,right=ds[q+1],ds[q]
        check(all(sum(row[k]*right[k][j] for k in range(len(right)))==0
                  for row in left for j in range(len(bs[q]))),'cech_square_zero')
    ranks=[rankmat(a) for a in ds]
    h=[len(bs[q])-(ranks[q-1] if q else 0)-(ranks[q] if q<3 else 0) for q in range(4)]
    check(h==predicted(module,ex,normal),'all_degree_cohomology_formula',(module,ex,normal,h))
    return h


def residue_vector(side,ex,normal,negative=False):
    bs,ds=matrices(side,ex,normal)
    selected=set(range(1,4)) if side=='+' else set(range(4,7))
    v=[(-1 if negative else 1) if p[0]==0 and p[1] in selected else 0 for p in bs[1]]
    check(all(dot(row,v)==0 for row in ds[1]),'residue_cocycle')
    rank=rankmat(ds[0])
    enlarged=[row+[v[i]] for i,row in enumerate(ds[0])]
    extended=rankmat(enlarged)
    return extended>rank,bs,ds,v


def mon_list(m):return {NAMES[i]:e for i,e in enumerate(m) if e}
def vector_list(v):return [{'face':[''.join(map(str,a)) for a in c[0]],
   'marks':[''.join(map(str,a)) for a in c[1]],'coefficient':n,'monomial':mon_list(m)} for (c,m),n in sorted(v.items())]


def main(path):
    check(len(CELLS)==215,'fixed_target_census')
    check([len(PATCH_DEG[q]) for q in range(4)]==[7,12,8,2],'cover_census')
    check(len(PATCHES)==29,'nonempty_intersections')
    # Independently reconstruct the input identities in all degrees.
    for c in CELLS:
        check(not apply(D,D[c]),'original_target_square_zero')
        check(not apply(D_PC,D_PC[c],True),'original_pc_square_zero')
    common=raw_shift(lift_cycle('both'),tuple(-e for e in TEXP))
    pos=raw_shift(lift_cycle('+'),tuple(-e for e in PAEXP))
    neg=raw_shift(lift_cycle('-'),tuple(-e for e in MBEXP))
    local=[common]+[pos]*3+[neg]*3
    theta=generic_part(common)
    for i,v in enumerate(local):
        check(localize(v,(i,))==v,'local_lift_poles_admissible',i)
        check(not ld(v,(i,)),'full_absolute_local_lift',i)
        check(not ld(v,(i,),True),'full_pc_local_lift',i)
        check(generic_part(v)==theta,'local_generic_unit',i)
    cocycles={}
    for patch in PATCH_DEG[1]:
        i,j=patch
        v=localize(add(local[j],scale(local[i],-1)),patch)
        cocycles[patch]=e_part(v)
        check(not ld(v,patch),'full_overlap_cycle',patch)
        check(not ld(v,patch,True),'full_pc_overlap_cycle',patch)
        check(not generic_part(v),'overlap_supported_boundary',patch)
    for p in PATCH_DEG[2]:
        i,j,k=p
        v=localize(add(cocycles[j,k],scale(cocycles[i,k],-1),cocycles[i,j]),p)
        check(not v,'triple_overlap_compatibility',p)
    # Check source-labelled semilinear transports on the actual local atlas.
    group=[(0,1),(2,1),(4,1),(3,-1),(5,-1),(1,-1)]
    for tr,ori in group:
        perm=lambda a:diag(tr+ori*a[0],tr+ori*a[1])
        vertex={0:0};vertex.update({i:COVER.index(perm(COVER[i])) for i in range(1,7)})
        for i,v in enumerate(local):
            check(act_raw(v,tr,ori)==local[vertex[i]],'local_lift_dihedral_covariance')
        for (i,j),v in cocycles.items():
            ii,jj=vertex[i],vertex[j];target=tuple(sorted((ii,jj)))
            check(act_raw(v,tr,ori)==scale(cocycles[target],1 if ii<jj else -1),
                  'cech_cocycle_oriented_covariance')
    # Construct actual global lifts for every minimal annihilator generator.
    sufficient=[('T',TEXP,lift_cycle('both'))]
    for side,act,tau in [('+',PLUS,PAEXP),('-',MINUS,MBEXP)]:
        for x in act:
            sufficient.append(('X'+''.join(map(str,x)),mon(xs=(x,)),
              raw_shift(lift_cycle(side,x),tuple(-e for e in tau))))
    for name,m,v in sufficient:
        sections={i:localize(v,(i,)) for i in range(7)}
        for i,w in sections.items():
            check(not ld(w,(i,),True),'annihilator_generators_have_global_pc_lifts',name)
            check(generic_part(w)==localize(raw_shift(theta,m),(i,),True),
                  'annihilator_lift_generic_coefficient',name)
        for patch in PATCH_DEG[1]:
            i,j=patch
            check(localize(sections[i],patch)==localize(sections[j],patch),
                  'annihilator_lifts_glue_strictly',name)
    records=[]
    for side,active,inactive,first in [('+',PLUS,MINUS,1),('-',MINUS,PLUS,4)]:
        expected={};full_expected={}
        for N in subsets(inactive):
            if not N:continue
            gamma,r,ps,ls=gamma_raw(active,N,include_endpoint=True)
            full_expected=add(full_expected,raw_shift(gamma,r))
            if len(N)==3:continue
            gamma=e_part(gamma)
            expected=add(expected,raw_shift(gamma,r))
            n6=tuple(r[9+VAR[a]] for a in PP+MM)
            nonzero,bs,ds,v=residue_vector(side,(0,)*6,n6)
            check(nonzero,'twelve_primitive_nonboundary_residues',(side,N))
            check(not bs[0],'no_zero_cochains_in_residue_grade',(side,N))
            # Multiplication by a chosen active occurrence becomes a Cech boundary.
            for k in range(3):
                ex=[0]*6;ex[k+(0 if side=='+' else 3)]=1
                killed,*_=residue_vector(side,tuple(ex),n6)
                check(not killed,'active_occurrence_kills_residue')
            # Opposite occurrences annihilate I_side termwise (not used as inverses).
            # Opposite Rees product also makes the residue a Cech boundary.
            nplus=list(n6)
            for a in inactive:nplus[(PP+MM).index(a)]+=1
            killed,*_=residue_vector(side,(0,)*6,tuple(nplus))
            check(not killed,'opposite_rees_product_kills_residue')
            records.append({'side':side,'inactive_subset':[''.join(map(str,a)) for a in N],
               'compatible_active':[''.join(map(str,a)) for a in sorted(ps)],
               'compatible_long':[''.join(map(str,a)) for a in sorted(ls)],
               'residue_monomial':mon_list(r),'gamma':vector_list(gamma)})
        patch=(0,first)
        diff=localize(add(common,scale(local[first],-1)),patch)
        check(diff==localize(full_expected,patch),'full_endpoint_overlap_decomposition',side)
        check(e_part(diff)==localize(expected,patch),'twelve_family_overlap_decomposition',side)
        # Endpoint vectors have not been quietly discarded from the calculation.
        end=endpoint_part(diff)
        opposite=tuple(sorted(inactive));m=sub_m(mon(normal=LONG),mon(normal=inactive))
        check(end=={((opposite,opposite),m):1},'opposite_endpoint_residue',side)
    # All normal supports check the exact annihilator of the Cech torsor.
    for bits in product((0,1),repeat=6):
        nz=[]
        for rec in records:
            m=[0]*18
            for key,e in rec['residue_monomial'].items():m[NAMES.index(key)]=e
            n6=tuple(m[9+VAR[a]]+bits[i] for i,a in enumerate(PP+MM))
            alive,*_=residue_vector(rec['side'],(0,)*6,n6)
            nz.append(alive)
        check(any(nz)==(not all(bits)),'exact_torsor_annihilator_support',bits)
    # Exhaustive sign patterns prove the Cech formulas at arbitrary degrees.
    histogram=Counter();cases=0
    zero=(0,)*6
    occurs=[zero]
    for side in (0,1):
        for a in product((-1,0,1),repeat=3):
            if a==(0,0,0):continue
            occurs.append(a+(0,0,0) if side==0 else (0,0,0)+a)
    for normal in product((-1,0),repeat=6):
        for ex in occurs:
            h=cohomology('O',ex,normal);histogram[('O',tuple(h))]+=1;cases+=1
        for side in ('+','-'):
            for a in product((-1,0,1),repeat=3):
                ex=a+(0,0,0) if side=='+' else (0,0,0)+a
                h=cohomology(side,ex,normal);histogram[(side,tuple(h))]+=1;cases+=1
    check(cases==6848,'exhaustive_cech_degree_cases')
    # Exact divisibility/non-affineness controls independent of target signs.
    # H1(O) has one generator in every degree with at least one negative
    # exponent on EACH normal sheet and no occurrence. Example: 1/(t13 t02).
    p0=PP.index(diag(1,3));m0=3+MM.index(diag(0,2));norm=[0]*6;norm[p0]=norm[m0]=-1
    check(cohomology('O',zero,tuple(norm))==[0,1,0,0],'nonaffine_open_witness')
    # A unit lift has no fine-degree correction in an exhibited M component.
    witness=next(rec for rec in records if rec['side']=='+' and rec['inactive_subset']==['02'])
    inputs={}
    for name in ('marici_union_recollement_20260907.md','marici_q_graded_lift_naturality_20260907.md',
                 'check_marici_q_lift_naturality_20260907.py'):
        p=Path('/mnt/data')/name
        if p.exists():inputs[name]=hashlib.sha256(p.read_bytes()).hexdigest()
    replay={}
    for name,key in [('lift_naturality','exact_assertions'),('union_recollement','exact_assertions')]:
        rp=Path('/mnt/data/divisor_descent_replays')/(name+'.json')
        if rp.exists():
            rc=json.loads(rp.read_text())
            replay[name]={'sha256':hashlib.sha256(rp.read_bytes()).hexdigest(),
                          'assertions':rc.get(key, rc.get('total_exact_assertions',rc.get('total_checks')))}
    result={'status':'proved_for_fixed_alternating_Rees_target_and_explicit_principal_open_cover',
      'optional_prerequisite_replays':replay,
      'source_commit':COMMIT,'input_sha256':inputs,
      'target_loaded_cells':len(CELLS),'cover_open_count':7,'nonzero_cech_terms':[7,12,8,2],
      'cover_generators':['tau_plus*tau_minus']+['tau_plus*X'+''.join(map(str,a)) for a in PP]+['tau_minus*X'+''.join(map(str,a)) for a in MM],
      'open':'V=Spec(B) minus V(a); not declared physical generic fibre',
      'local_generic_unit_lifts':7,'global_generic_unit_lift':False,
      'cech_torsor_residue_families':records,'primitive_nonboundary_witness':witness,
      'global_coefficient_ring':'C + I_plus C[tau_plus^-1][X_plus] + I_minus C[tau_minus^-1][X_minus]',
      'H1_M':'(C[T^-1]/C[tau_plus^-1])^6 + (C[T^-1]/C[tau_minus^-1])^6, with all Gamma gradings',
      'torsor_class_annihilator_over_B':'I_plus+I_minus+(T)',
      'image_on_original_coefficients':'I_plus+I_minus+(T)',
      'image_on_open_global_ring':'T*C + I_plus C[tau_plus^-1][X_plus] + I_minus C[tau_minus^-1][X_minus]',
      'nonempty_lifting_spaces':'discrete torsors under (I_plus C[tau_plus^-1][X_plus])^6 + (I_minus C[tau_minus^-1][X_minus])^6',
      'endpoint_overlap_residues':{'positive_overlap':'U_L/tau_minus at v_minus','negative_overlap':'U_L/tau_plus at v_plus'},
      'all_degree_cases':cases,'cohomology_histogram':[{'module':a,'h':list(b),'cases':n} for (a,b),n in sorted(histogram.items())],
      'checks':dict(sorted(COUNTS.items())),'total_exact_assertions':sum(COUNTS.values()),
      'scope':['No new physical support operation or inverse in the native source.',
               'Local divisions only on their stated principal opens.',
               'No identification of theta with the Morse roof or with the reverse generic pairing.',
               'No new geometric endpoint connector; both endpoint discrepancies recorded.',
               'No proof-assistant verification; all-degree theorems proved by monomial and normalization arguments.']}
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','nonzero_cech_terms','local_generic_unit_lifts','global_generic_unit_lift','all_degree_cases','total_exact_assertions')},indent=2))


D_PC={c:cech_d(c) for c in CELLS}
if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('marici_divisor_complement_descent_certificate_20260907.json'))
    args=parser.parse_args();main(args.output)
