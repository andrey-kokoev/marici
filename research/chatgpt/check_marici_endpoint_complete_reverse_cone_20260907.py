#!/usr/bin/env python3
"""Endpoint-complete reverse normalization cone, with all attachment maps.

Self-contained standard-library exact checker. The finite target/localization
helpers below are preserved from check_marici_descent_duality_20260907.py.
New code constructs the normalization presentation for the whole 14-residue
source, its ambient free mapping-fibre resolution and the complete transposed
cone. Residues are first treated as independent scalar symbols, then matched
to the actual labelled Laurent residues. No monomial truncation is imposed.

This is coefficient-side verification, not a physical-source identification,
a proof assistant, or an interchange of global sections with duality.
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



# -------------------- New reverse normalization calculation -----------------

def family_data():
    out=[]
    for side,active,inactive in [('+',PLUS,MINUS),('-',MINUS,PLUS)]:
        for n in subsets(inactive):
            if not n: continue
            g,r,cs,cl=gamma_raw(active,n,True)
            out.append(dict(side=side,active=active,inactive=n,gamma=g,
                            residue=r,endpoint=len(n)==3))
    return out

FAMILY=family_data()
UNIV_N=6+len(FAMILY)  # six ambient occurrences, fourteen independent residues
UZ=(0,)*UNIV_N
OCC_ORDER=tuple(SHORT[i] for i in (1,3,5,0,2,4))
OIDX={x:i for i,x in enumerate(OCC_ORDER)}


def umon(i):
    return tuple(int(k==i) for k in range(UNIV_N))


def ua(table,v):
    out={}
    for (c,m),a in v.items():
        for (target,n),b in table.get(c,{}).items():
            key=(target,tuple(x+y for x,y in zip(m,n)))
            out[key]=out.get(key,0)+a*b
            if not out[key]: del out[key]
    return out


def uterm(c, m=UZ, a=1):
    return {} if not a else {(c,m):a}


def koszul_terms(kind,label,subset,overall=1):
    return {((kind,label,tuple(x for x in subset if x!=i)),umon(i)):overall*pm(j)
            for j,i in enumerate(subset)}


class Presentation:
    """Free fibre of normalization evaluation, over the smooth ambient ring.

    L-column (+/-) resolves a polynomial normalization branch with the
    opposite three-variable Koszul complex. Every conductor row resolves the
    conductor by the full six-variable Koszul complex. The homological fibre
    has F_n=L_n + C_{n+1}, d(l,c)=(d_L l, A_r l-d_C c).
    """
    def __init__(self, channels):
        self.channels=tuple(channels)
        self.cols=('+','-')+tuple('z'+str(j) for j in self.channels)
        self.rows=('g',)+tuple(str(j) for j in self.channels)
        self.side={'+':'+','-':'-'}
        self.side.update({'z'+str(j):FAMILY[j]['side'] for j in self.channels})
        self.opposite={c:tuple(range(3,6)) if self.side[c]=='+' else tuple(range(3))
                       for c in self.cols}
        self.A={c:{} for c in self.cols}
        self.A['+'][('g',UZ)]=1
        self.A['-'][('g',UZ)]=-1
        for j in self.channels:
            self.A[FAMILY[j]['side']][(str(j),umon(6+j))]=-1
            self.A['z'+str(j)][(str(j),UZ)]=1
        self.L={n:tuple(('L',c,s) for c in self.cols
                         for s in combinations(self.opposite[c],n)) for n in range(4)}
        self.C={n:tuple(('C',r,s) for r in self.rows
                         for s in combinations(range(6),n)) for n in range(7)}
        self.f={}; self.dL={};self.dC={}
        for n,cs in self.L.items():
            for c in cs:
                _,label,s=c
                self.dL[c]=koszul_terms('L',label,s)
                self.f[c]={ (('C',r,s),m):a for (r,m),a in self.A[label].items()}
        for n,cs in self.C.items():
            for c in cs:
                _,r,s=c
                self.dC[c]=koszul_terms('C',r,s)
        self.bs={n:self.L.get(n,())+self.C.get(n+1,()) for n in range(-1,6)}
        self.deg={c:n for n,cs in self.bs.items() for c in cs}
        self.d={}
        for n,cs in self.bs.items():
            for c in cs:
                if c[0]=='L': self.d[c]=add(self.dL[c],self.f[c])
                else: self.d[c]=scale(self.dC[c],-1)
        self.dual={c:{} for c in self.deg}
        for c,terms in self.d.items():
            for (t,m),a in terms.items():
                # cohomological degree of t^dual is deg(t)-6
                self.dual[t][(c,m)]=pm(self.deg[t]+1)*a
        self.dualdeg={c:n-6 for c,n in self.deg.items()}
        self.dLd={c:{} for cs in self.L.values() for c in cs}
        self.dCd={c:{} for cs in self.C.values() for c in cs}
        self.ft={c:{} for cs in self.C.values() for c in cs}
        for c,terms in self.dL.items():
            for (t,m),a in terms.items(): self.dLd[t][(c,m)]=pm(len(t[2])+1)*a
        for c,terms in self.dC.items():
            for (t,m),a in terms.items(): self.dCd[t][(c,m)]=pm(len(t[2])+1)*a
        for c,terms in self.f.items():
            for (t,m),a in terms.items(): self.ft[t][(c,m)]=a
        # Actual cohomological Cone(A_r^dual), with its own signs.
        self.coned={}
        for c in self.deg:
            if c[0]=='L': self.coned[c]=self.dLd[c]
            else: self.coned[c]=add(self.ft[c],scale(self.dCd[c],-1))
        self.to_cone={c:uterm(c,a=1 if c[0]=='L' else pm(self.deg[c]+1))
                      for c in self.deg}

    def audit(self):
        for c in self.dL:
            check(ua(self.dC,self.f[c])==ua(self.f,self.dL[c]),'normalization_Koszul_chain_map')
        for c in self.deg:
            check(all(self.deg[t]==self.deg[c]-1 for (t,_m) in self.d[c]),'fibre_degree')
            check(not ua(self.d,self.d[c]),'full_primal_fibre_d_squared')
            check(not ua(self.dual,self.dual[c]),'full_ambient_dual_d_squared')
            check(not ua(self.coned,self.coned[c]),'full_reverse_cone_d_squared')
            check(ua(self.to_cone,self.dual[c])==ua(self.coned,self.to_cone[c]),
                  'dual_fibre_equals_reverse_cone_with_exact_signs')
            for (s,m),a in self.dual[c].items():
                primal=self.d[s].get((c,m),0)
                check(a+pm(self.dualdeg[c])*primal==0,'dual_evaluation_chain_pairing')
        for c in self.ft:
            check(ua(self.dLd,self.ft[c])==ua(self.ft,self.dCd[c]),'transposed_attachment_chain_map')

    def fibre_ranks(self):
        """Prove rank and saturation of every conductor-fibre differential.

        After setting occurrences to zero, only the evaluation maps f_n
        remain. Chosen unit triangular minors prove all ranks over any
        coefficient ring and leave free cokernels; no numeric rank guess.
        """
        ranks={}
        for n in range(7):
            cols=list(self.L.get(n,()))
            if n==0:
                cols=[c for c in cols if c[1]!='-']
            if not cols:
                ranks[n]=0;continue
            pivots=[]
            for c in cols:
                kind,label,s=c
                row='g' if label in ('+','-') else label[1:]
                pivots.append(('C',row,s))
            check(len(set(pivots))==len(pivots),'unit_minor_distinct_rows')
            for i,c in enumerate(cols):
                for j,t in enumerate(pivots):
                    entry={m:a for (r,m),a in self.f[c].items() if r==t}
                    if i==j: check(entry=={UZ:(-1 if c[1]=='-' else 1)},'unit_minor_diagonal')
                    if j<i: check(not entry,'unit_minor_above_diagonal_zero')
            ranks[n]=len(cols)
            if n==0: check(ranks[n]==len(self.C[n]),'augmentation_surjective')
            else: check(ranks[n]==len(self.L.get(n,())),'positive_Koszul_injection')
        b={n:len(self.L.get(n,()))-ranks.get(n,0)
             +len(self.C.get(n+1,()))-ranks.get(n+1,0) for n in range(6)}
        check(len(self.C[0])-ranks[0]==0,'no_degree_minus_one_primal_homology')
        return b,ranks


def projection(large,small):
    return {c:uterm(c) if c in small.deg else {} for c in large.deg}


def inclusion(small,large):
    return {c:uterm(c) for c in small.deg}


def perm_sign(seq):
    return pm(sum(a>b for i,a in enumerate(seq) for b in seq[i+1:]))


def relabel_data(r,s):
    geo=lambda a:diag(r+s*a[0],r+s*a[1])
    occ=tuple(OIDX[geo(a)] for a in OCC_ORDER)
    swap=geo(next(iter(PLUS))) in MINUS
    fam={}
    for j,item in enumerate(FAMILY):
        side=('+' if item['side']=='-' else '-') if swap else item['side']
        ns=tuple(sorted(geo(a) for a in item['inactive']))
        k=next(k for k,z in enumerate(FAMILY) if z['side']==side and z['inactive']==ns)
        fam[j]=k
        # Check the coefficient formula before treating residues as symbols.
        old=item['residue'];new=[0]*18
        for a in DIAGS:
            new[VAR[geo(a)]]=old[VAR[a]]
            new[9+VAR[geo(a)]]=old[9+VAR[a]]
        check(tuple(new)==FAMILY[k]['residue'],'actual_residue_covariance')
    univ=occ+tuple(6+fam[j] for j in range(14))
    return occ,fam,swap,univ


def act_u(v,occ,fam,swap,univ,dual_volume=False):
    out={}
    for (c,m),a in v.items():
        kind,label,ss=c
        if kind=='L':
            if label in ('+','-'): lab=('-' if label=='+' else '+') if swap else label
            else: lab='z'+str(fam[int(label[1:])])
            sg=1
        else:
            lab='g' if label=='g' else str(fam[int(label)])
            sg=-1 if label=='g' and swap else 1
        ns=tuple(occ[i] for i in ss);sg*=perm_sign(ns)
        if dual_volume:sg*=perm_sign(occ)
        mm=[0]*UNIV_N
        for i,j in enumerate(univ):mm[j]=m[i]
        out=add(out,uterm((kind,lab,tuple(sorted(ns))),tuple(mm),a*sg))
    return out


def raw_kappa_new(v):
    out={}
    for (cell,m),a in v.items():
        denom=ZERO
        for lab in set(cell[0])-set(cell[1]):denom=add_m(denom,u_m(lab))
        out=add(out,{(cell,sub_m(m,denom)):a})
    return out


def check_target_and_transitions():
    global D_PC
    D_PC=DC
    for cell in CELLS:
        check(not apply(D,D[cell]),'inherited_215_state_target_d_squared')
        check(not apply(DC,DC[cell],True),'inherited_PC_target_d_squared')
    sec0=raw_shift(lift_cycle('both'),tuple(-x for x in TEXP))
    secp=raw_shift(lift_cycle('+'),tuple(-x for x in PAEXP))
    secm=raw_shift(lift_cycle('-'),tuple(-x for x in MBEXP))
    ss=[sec0]+[secp]*3+[secm]*3
    for i,sec in enumerate(ss):
        check(not ld(sec,(i,)),'endpoint_complete_local_source_map')
        check(not ld(raw_kappa_new(sec),(i,),True),'PC_local_source_map')
    for item in FAMILY:
        for x in item['active']:
            check(not apply(D,multiply(item['gamma'],mon(xs=(x,)))),
                  'all_fourteen_ideal_generators_are_full_target_cycles')
        if item['endpoint']:
            check(len(item['gamma'])==1,'endpoint_is_not_erased')
            rs=item['residue']
            op=MINUS if item['side']=='+' else PLUS
            check(rs==sub_m(mon(normal=LONG),mon(normal=op)),
                  'actual_triple_pole_endpoint_residue')
    deltas={}
    for i,j in combinations(range(7),2):
        if (i,j) not in PATCHES:continue
        v=localize(add(ss[j],scale(ss[i],-1)),(i,j))
        deltas[i,j]=v
        if i==0:
            side='+' if j<=3 else '-'
            coeff={}
            for item in FAMILY:
                if item['side']==side:
                    coeff=add(coeff,scale(raw_shift(item['gamma'],item['residue']),-1))
            check(v==localize(coeff,(i,j)),'normalization_transition_equals_full_target_difference')
            check(localize(raw_kappa_new(v),(i,j),True)==
                  localize(raw_kappa_new(coeff),(i,j),True),'PC_transition_same_endpoints')
    for patch in PATCH_DEG[2]:
        i,j,k=patch
        check(not localize(add(deltas[j,k],scale(deltas[i,k],-1),deltas[i,j]),patch),
              'full_transition_cocycle')
    return [len(PATCH_DEG[i]) for i in range(4)]


def fibre_negative_control(q):
    from math import comb
    # H^-3 has q+2 total branch-volume lines, half on each branch;
    # H^-1 has q+1 conductor lines. This is the *split* derived object.
    rank=Counter()
    for j in range(4):rank[-3-j]+=(q+2)*comb(3,j)
    for j in range(7):rank[-1-j]+=(q+1)*comb(6,j)
    return dict(sorted(rank.items()))


def main(path):
    cover=check_target_and_transitions()
    channel12=tuple(j for j,v in enumerate(FAMILY) if not v['endpoint'])
    m0=Presentation(())
    m12=Presentation(channel12)
    m14=Presentation(range(14))
    models=[m0,m12,m14]
    reports={}
    for model in models:
        model.audit()
        betti,ranks=model.fibre_ranks()
        q=len(model.channels)
        reports[str(q)]={
          'normalization_branch_columns':len(model.cols),
          'normalization_conductor_rows':len(model.rows),
          'free_mapping_fibre_ranks':{str(n):len(cs) for n,cs in model.bs.items()},
          'free_mapping_fibre_total':len(model.deg),
          'fibre_evaluation_map_ranks':ranks,
          'primal_ambient_conductor_Tor_ranks':betti,
          'full_dual_ambient_conductor_cohomology':{str(n-6):r for n,r in betti.items() if r},
          'incorrect_split_ambient_conductor_cohomology':fibre_negative_control(q),
          'global_sheaf_cohomology_degrees':{'-3':f'{q//2+1} branch-volume lines on each sheet',
                                             '-1':f'{q+1} labelled conductor lines'},
        }
    check(list(reports['0']['primal_ambient_conductor_Tor_ranks'].values())==[1,9,18,15,6,1],
          'recovered_original_alternating_ring_Betti_numbers')
    check(list(reports['12']['primal_ambient_conductor_Tor_ranks'].values())==[37,153,246,195,78,13],
          'twelve_channel_complete_ambient_fibre')
    check(list(reports['14']['primal_ambient_conductor_Tor_ranks'].values())==[43,177,284,225,90,15],
          'fourteen_channel_complete_ambient_fibre')
    for large,small,tag in [(m14,m12,'endpoint'),(m14,m0,'generic'),(m12,m0,'generic_twelve')]:
        proj=projection(large,small);inc=inclusion(small,large)
        for c in large.deg:
            check(ua(proj,large.d[c])==ua(small.d,proj[c]),tag+'_primal_projection_chain_map')
        for c in small.deg:
            check(ua(large.dual,inc[c])==ua(inc,small.dual[c]),tag+'_reverse_inclusion_chain_map')
    # The endpoint quotient of the reverse complex must retain exactly both
    # ideal duals. Detect the actual off-diagonal endpoint attachments.
    extra=set(m14.deg)-set(m12.deg)
    check(len(extra)==144,'two_endpoint_dual_ideal_resolutions_retained')
    offdiag=[]
    for c in extra:
        for (target,mono),a in m14.dual[c].items():
            if target in m12.deg:
                check(c[0]=='C' and FAMILY[int(c[1])]['endpoint'],
                      'offdiagonal_has_actual_endpoint_source')
                check(target[0]=='L' and target[1] in ('+','-'),
                      'offdiagonal_targets_generic_branch_volume_resolution')
                j=int(c[1]);check(mono==umon(6+j),'endpoint_offdiagonal_coefficient_is_retained_residue')
                offdiag.append((c,target,mono,a))
    check(len(offdiag)==16,'sixteen_Koszul_entries_of_two_endpoint_attachments')
    # Remove those off-diagonal entries: yields a split complex with the same
    # underlying terms, but not the previously defined endpoint extension.
    splitdual={c:{k:a for k,a in v.items() if not (c in extra and k[0] in m12.deg)}
               for c,v in m14.dual.items()}
    for c in splitdual:check(not ua(splitdual,splitdual[c]),'negative_control_endpoint_erasure_also_square_zero')
    check(splitdual!=m14.dual,'square_zero_alone_does_not_recover_endpoint_comparison')
    # Actual labelled dihedral covariance, on whole free complexes, not only H.
    for tr,orient in [(0,1),(2,1),(4,1),(1,-1),(3,-1),(5,-1)]:
        occ,fam,swap,univ=relabel_data(tr,orient)
        for c in m14.deg:
            action=act_u(uterm(c),occ,fam,swap,univ)
            check(ua(m14.d,action)==act_u(m14.d[c],occ,fam,swap,univ),
                  'full_primal_dihedral_covariance')
            dualaction=act_u(uterm(c),occ,fam,swap,univ,True)
            check(ua(m14.dual,dualaction)==act_u(m14.dual[c],occ,fam,swap,univ,True),
                  'full_reverse_dihedral_covariance_with_volume_line')
    # Principal occurrence open: the relevant Koszul complex is contractible
    # by e_i wedge / X_i. Verify all signs with formal Laurent exponents.
    def ktable(seq):
        return {s:{(tuple(x for x in s if x!=i),umon(i)):pm(j) for j,i in enumerate(s)}
                for s in subsets(seq)}
    for seq in [tuple(range(6)),tuple(range(3)),tuple(range(3,6))]:
        d=ktable(seq)
        for i in seq:
            h={}
            for s in d:
                if i in s:h[s]={}
                else:
                    monm=tuple(-int(k==i) for k in range(UNIV_N))
                    h[s]=uterm(tuple(sorted(s+(i,))),monm,pm(sum(j<i for j in s)))
            for s in d:
                check(add(ua(d,h[s]),ua(h,d[s]))==uterm(s),'Koszul_localization_contraction_on_occurrence_charts')
    # Full derived-chart descent of the attachment. On an occurrence open,
    # conductor Koszul resolutions are contractible. Products of the actual
    # insertion homotopies give their pair/triple comparison homotopies.
    hs={}
    for i in range(6):
        hh={}
        for c in m14.dC:
            kind,row,ss=c
            if i in ss:hh[c]={}
            else:
                xx=tuple(-int(k==i) for k in range(UNIV_N))
                hh[c]=uterm((kind,row,tuple(sorted(ss+(i,)))),xx,
                             pm(sum(j<i for j in ss)))
        hs[i]=hh
    def composed_h(indices,v):
        for i in reversed(indices):v=ua(hs[i],v)
        return v
    higher_comparisons=Counter()
    for side in [tuple(range(3)),tuple(range(3,6))]:
        for k in range(1,4):
            for ii in combinations(side,k):
                for c,fv in m14.f.items():
                    lhs=add(ua(m14.dC,composed_h(ii,fv)),
                            scale(composed_h(ii,ua(m14.f,m14.dL[c])),-pm(k)))
                    rhs={}
                    for j in range(k):
                        rhs=add(rhs,scale(composed_h(ii[:j]+ii[j+1:],fv),pm(j)))
                    check(lhs==rhs,'explicit_occurrence_chart_higher_homotopies')
                    higher_comparisons[k]+=1
    # Audit every differential in the original eighteen-coordinate fine
    # grading after substituting the actual Laurent residue degrees. Generic
    # base generators have shift zero; residue rows and extra branch columns
    # have the negative residue degree. Exterior conormals add their labels.
    def coefficient_grade(m):
        out=[0]*18
        for i,a in enumerate(OCC_ORDER):out[VAR[a]]+=m[i]
        for j,it in enumerate(FAMILY):
            for k,v in enumerate(it['residue']):out[k]+=m[6+j]*v
        return tuple(out)
    def generator_grade(c):
        typ,label,subset=c
        j=None
        if typ=='L' and label.startswith('z'):j=int(label[1:])
        if typ=='C' and label!='g':j=int(label)
        out=[0]*18 if j is None else [-x for x in FAMILY[j]['residue']]
        for i in subset:out[VAR[OCC_ORDER[i]]]+=1
        return tuple(out)
    volume=mon(xs=OCC_ORDER)
    for c,v in m14.d.items():
        cs=generator_grade(c)
        for (t,m),a in v.items():
            check(cs==add_m(generator_grade(t),coefficient_grade(m)),
                  'complete_original_fine_grading_primal')
    for c,v in m14.dual.items():
        cs=sub_m(volume,generator_grade(c))
        for (t,m),a in v.items():
            check(cs==add_m(sub_m(volume,generator_grade(t)),coefficient_grade(m)),
                  'complete_original_fine_grading_reverse_with_volume')
    result={
      'status':'constructed_full_coefficient_reverse_cone_with_endpoint_and_generic_maps',
      'source_commit':COMMIT,
      'scope':'Coherent normalization-pullback source S14 on the previous test open V. Not the independent native physical source, not global-section/duality interchange, not an intrinsic derived B-conductor-fibre calculation.',
      'target_states':len(CELLS),'cover_terms':cover,
      'residue_channels':[{'index':j,'side':it['side'],
          'inactive_subset':[''.join(map(str,x)) for x in it['inactive']],
          'endpoint':it['endpoint'],
          'Laurent_residue':{NAMES[k]:e for k,e in enumerate(it['residue']) if e}}
          for j,it in enumerate(FAMILY)],
      'normalization_matrix':{'rows':['difference']+['residue_'+str(j) for j in range(14)],
          'columns':list(m14.cols),
          'entries':[{'column':c,'row':r,'coefficient':a,
                      'residue_index':next((k-6 for k,e in enumerate(m) if e and k>=6),None)}
                     for c,v in m14.A.items() for (r,m),a in v.items()]},
      'reverse_cone_formula':'Cone(C_D^15 -> (lambda_plus^8 + lambda_minus^8)[3]) with transposed evaluation/Koszul Gysin attachment',
      'endpoint_extra_dual_resolution_generators':len(extra),
      'endpoint_offdiagonal_Koszul_entries':len(offdiag),
      'explicit_occurrence_chart_homotopy_checks_by_order':dict(higher_comparisons),
      'endpoint_attachment_pole_coefficients':['-U_L/tau_minus','-U_L/tau_plus'],
      'non_splitting_annihilator_transported_by_coherent_biduality':'I_plus + I_minus + n_plus*n_minus',
      'annihilator_provenance':'Earlier normalization_endpoint_extension theorem, transported by faithful C-linear duality; not re-inferred from a finite rank sample.',
      'models':reports,
      'negative_control':'Replacing the reverse complex by the direct sum of its two cohomology sheaves creates 15 spurious degree -7 classes in its derived smooth-ambient conductor fibre.',
      'assertions':dict(sorted(COUNTS.items())), 'total_exact_assertions':sum(COUNTS.values()),
      'verification_limits':['Regular-sequence and exact normalization arguments prove arbitrary-polynomial statements.',
         'Unit minors prove fibre ranks for every residue specialization on the stated open, not just over a field.',
         'A correct cohomology rank or square-zero differential is not an independent identification of the source.',
         'Free ambient matrices on the central chart represent the derived B-linear maps after forgetting to A; no false strict B-action is assigned to free A-resolution terms.',
         'No repository modifications and no proof-assistant certification.']}
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','target_states','cover_terms','endpoint_offdiagonal_Koszul_entries','total_exact_assertions']},indent=2))
    print(json.dumps(reports['14'],indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('marici_endpoint_complete_reverse_cone_certificate_20260907.json'))
    args=parser.parse_args()
    main(args.output)
