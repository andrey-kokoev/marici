#!/usr/bin/env python3
"""Graded lifting and coefficient-linearity obstruction for Marici's Q target.

Standard-library exact arithmetic. Reconstructs the 215-state target, the
7-generator lifting ideal, its complete 30-relation presentation, and a
43-generator / 174-relation presentation of the top lifting module.
Finite calculations complement the arbitrary-polynomial proof in the note.
No network, scalar averaging, or repository writes are used.
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


def top_grade_audit(occurrences, normal_support):
    """Integral forest solution of every top-cycle equation in this fine degree.

    After the explicit top orientation gauge, each two-column row is a
    signed difference. Singleton rows pin a component to zero. This gives
    the full integral kernel, not a rank computed over a finite field.
    """
    a = mon(xs=occurrences, normal=normal_support)
    g = add_m(a, mon(normal=LONG))
    top = [c for c in CELLS if degree(c) == 3 and level(c) != 0
           and coefficient_at_grade(c, g) is not None]
    rows = defaultdict(dict)
    top_sign = {c: pm(len(c[0]) * (len(c[0]) + 1) // 2) for c in top}
    for c in top:
        coeff = coefficient_at_grade(c, g)
        dv = project(multiply(D[c], coeff), lambda t: level(t) != 0)
        for (r, mm), n in dv.items():
            check(mm == coefficient_at_grade(r, g), "fine_degree_preserved")
            rows[r][c] = n * top_sign[c]
    parent = {c: c for c in top}
    def find(c):
        while parent[c] != c:
            parent[c] = parent[parent[c]]
            c = parent[c]
        return c
    def union(a, b):
        aa, bb = find(a), find(b)
        if aa != bb:
            parent[aa] = bb
    pins = []
    for r, row in rows.items():
        check(len(row) <= 2 and all(abs(n) == 1 for n in row.values()),
              "fine_degree_unit_incidence_rows")
        if len(row) == 1:
            pins.append(next(iter(row)))
        elif len(row) == 2:
            check(sum(row.values()) == 0, "fine_degree_orientation_gauge")
            x, y = row
            union(x, y)
    pinned = {find(c) for c in pins}
    empty = ((), ())
    check(empty in top, "generic_top_coefficient_present")
    connected = {find(c) for c in top}
    unpinned = connected - pinned
    extends = find(empty) in unpinned
    check(extends == ann_member(a), "exhaustive_annihilator_control")
    # Every unpinned component is an integral kernel basis vector. Check it
    # against the complete differential; no unwritten rational rank step.
    for component in unpinned:
        v = {}
        for c in top:
            if find(c) == component:
                v = add(v, basis(c, coefficient_at_grade(c, g), top_sign[c]))
        check(not project(apply(D, v), lambda t: level(t) != 0),
              "fine_degree_integral_kernel_basis")
    expected_ambiguity = 0
    if occurrences:
        active = PLUS if set(occurrences) & PLUS else MINUS
        inactive = set(SHORT) - set(active)
        for n in subsets(inactive):
            if 0 < len(n) < 3:
                compat = {a for a in active if all(not cross(a, b) for b in n)}
                if set(n) | compat <= set(normal_support):
                    expected_ambiguity += 1
    check(len(unpinned) - int(extends) == expected_ambiguity,
          "boundary_ambiguity_module_fine_degree_control")
    return {"short_occurrence_support": [label(a) for a in occurrences],
            "short_Rees_support": [label(a) for a in normal_support],
            "top_chain_rank": len(top), "top_kernel_rank": len(unpinned),
            "boundary_top_kernel_rank": expected_ambiguity,
            "unit_generic_coefficient_lifts": extends}


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


def top_kernel_at_grade(g):
    top=[c for c in CELLS if degree(c)==3 and level(c)>0
         and coefficient_at_grade(c,g) is not None]
    rows=defaultdict(dict)
    signs={c:pm(len(c[0])*(len(c[0])+1)//2) for c in top}
    for c in top:
        dv=project(multiply(D[c],coefficient_at_grade(c,g)),lambda z:level(z)>0)
        for (z,mm),n in dv.items():
            check(mm==coefficient_at_grade(z,g),'top_kernel_degree')
            rows[z][c]=n*signs[c]
    parent={c:c for c in top}
    def find(c):
        while parent[c]!=c:
            parent[c]=parent[parent[c]];c=parent[c]
        return c
    def union(a,b):
        aa,bb=find(a),find(b)
        if aa!=bb: parent[aa]=bb
    pins=[]
    for row in rows.values():
        check(len(row)<=2 and all(abs(n)==1 for n in row.values()),'top_unit_rows')
        if len(row)==1:pins.append(next(iter(row)))
        elif len(row)==2:
            check(sum(row.values())==0,'top_oriented_difference')
            union(*row.keys())
    pinned={find(c) for c in pins}
    comps=sorted({find(c) for c in top}-pinned)
    reps={component:next(c for c in top if find(c)==component) for component in comps}
    return top,find,pinned,comps,reps,signs


def execute(output: Path):
    check(len(CELLS)==215,'entire_loaded_target')
    check(max(map(degree,CELLS))==3,'no_degree_four_boundaries')
    for c in CELLS:
        check(not apply(D,D[c]),'full_polynomial_d_squared')
        check(kappa(D[c])==apply(DC,kappa(basis(c)),True),'source_PC_square')
    theta=basis(((),()),mon(normal=LONG))
    for l in LONG:
        theta=add(theta,basis(((l,),(l,)),mon(xs=(l,),normal=set(LONG)-{l}),-1))
    beta=apply(D,theta)
    check(len(beta)==18 and not apply(D,beta),'retained_connecting_class')

    shorts=tuple(sorted(SHORT)); short_index={s:i+1 for i,s in enumerate(shorts)}
    gs=[mon(normal=SHORT)]
    lifts=[project(lift_cycle('both'),lambda c:level(c)>0)]
    lift_names=['lambda_0']
    for s in shorts:
        active=PLUS if s in PLUS else MINUS
        gs.append(mon(xs=(s,),normal=active))
        lifts.append(project(lift_cycle('+' if s in PLUS else '-',s),lambda c:level(c)>0))
        lift_names.append('lambda_'+label(s))
    for g,v in zip(gs,lifts):
        check(not project(apply(D,v),lambda c:level(c)>0),'seven_lifts_closed')
        check(project(v,lambda c:level(c)==2)==multiply(theta,g),'seven_lift_projection')

    # A complete presentation of a over B: 6 seam, 6 same-sheet Koszul,
    # 18 opposite-sheet annihilator relations.
    a_rel=[]; a_names=[]; a_kind=[]
    for s in shorts:
        opp=MINUS if s in PLUS else PLUS
        a_rel.append({(0,mon(xs=(s,))):1,(short_index[s],mon(normal=opp)):-1})
        a_names.append('seam_'+label(s));a_kind.append('seam')
    for active in (PLUS,MINUS):
        for s,t in combinations(sorted(active),2):
            a_rel.append({(short_index[s],mon(xs=(t,))):1,(short_index[t],mon(xs=(s,))):-1})
            a_names.append('koszul_'+label(s)+'_'+label(t));a_kind.append('koszul')
        for s in sorted(active):
            for t in sorted(set(SHORT)-set(active)):
                a_rel.append({(short_index[s],mon(xs=(t,))):1})
                a_names.append('ann_'+label(t)+'_'+label(s));a_kind.append('annihilator')
    check(len(a_rel)==30,'thirty_ideal_relations')
    a_rdeg=[relation_degree(r,gs) for r in a_rel]
    rel_images=[]
    for name,rel,kind in zip(a_names,a_rel,a_kind):
        ideal_image={};target_image={}
        for (i,m),n in rel.items():
            mm=add_m(gs[i],m)
            if ring_monomial_ok(mm):
                ideal_image[mm]=ideal_image.get(mm,0)+n
            target_image=add(target_image,scale(multiply(lifts[i],m),n))
        check(not {m:n for m,n in ideal_image.items() if n},'actual_ideal_syzygy',name)
        check(bool(target_image)==(kind=='seam'),'only_seam_relations_have_defect',name)
        check(not project(apply(D,target_image),lambda c:level(c)>0),'syzygy_defect_closed',name)
        check(not project(target_image,lambda c:level(c)==2),'syzygy_defect_boundary_supported',name)
        rel_images.append(target_image)

    # All 36 generators of the 12 labelled ideal-valued ambiguity summands.
    m_keys=[];m_vec=[]
    for active,sgn in ((PLUS,'+'),(MINUS,'-')):
        inactive=set(SHORT)-set(active)
        for nset in subsets(inactive):
            if not 0<len(nset)<3:continue
            for s in sorted(active):
                key=(sgn,nset,s)
                v=boundary_top_cycle(active,nset,s)
                m_keys.append(key);m_vec.append(v)
                check(v and all(level(c)==1 for c,_ in v),'boundary_generator_endpoint_support')
                check(not apply(D,v),'boundary_generator_closed')
    check(len(m_keys)==36,'thirty_six_ideal_generators')
    m_pos={key:i+7 for i,key in enumerate(m_keys)}
    all_images=lifts+m_vec
    all_names=lift_names+['M'+sgn+'_'+'_'.join(map(label,n))+'_X'+label(s) for sgn,n,s in m_keys]
    hweights=[homogeneous_degree(v) for v in all_images]

    def seam_factor(active,nset):
        inactive=set(SHORT)-set(active);nset=set(nset)
        compat_s={s for s in active if all(not cross(s,n) for n in nset)}
        compat_l={l for l in LONG if all(not cross(l,n) for n in nset)}
        return mon(normal=(inactive-nset)|(set(active)-compat_s)|(set(LONG)-compat_l))

    seam_records=[];seam_decompositions=[]
    for s in shorts:
        active=PLUS if s in PLUS else MINUS
        inactive=set(SHORT)-set(active);sgn='+' if s in PLUS else '-'
        idx=shorts.index(s); defect=rel_images[idx]
        decomposition={};factors=[]
        for nset in subsets(inactive):
            if not 0<len(nset)<3:continue
            fac=seam_factor(active,nset); key=(sgn,nset,s)
            decomposition[(m_pos[key],fac)]=1
            # Colon (tau_inactive):fac is the product of the missing inactive variables.
            tau=mon(normal=inactive)
            colon=tuple(max(0,a-b) for a,b in zip(tau,fac))
            check(colon==mon(normal=nset),'exact_component_symbol_annihilator')
            check(not all(fac[i]>=tau[i] for i in range(18)),'seam_symbol_nonzero_component')
            factors.append({'inactive_subset':list(map(label,nset)),
                            'factor':{NAMES[i]:e for i,e in enumerate(fac) if e},
                            'annihilator':list(map(label,nset))})
        recombined={}
        for (i,m),n in decomposition.items():recombined=add(recombined,scale(multiply(all_images[i],m),n))
        check(recombined==defect,'exact_six_component_seam_defect')
        check(len(defect)==24,'twenty_four_term_seam_defect')
        # One singleton coefficient gives a transparent fixed normal obstruction.
        for n in sorted(inactive):
            cell=((n,),(n,))
            expected=scale(basis(cell,mon(xs=(s,),normal=(set(SHORT)-{n})|set(LONG))),-1)
            observed={key:v for key,v in defect.items() if key[0]==cell}
            check(observed==expected,'missing_Rees_factor_detector')
            term_m=next(iter(observed))[1]
            check(term_m[9+VAR[n]]==0,'detector_not_divisible_by_opposite_tau')
        full_colon=ZERO
        for nset in subsets(inactive):
            if 0<len(nset)<3:
                z=mon(normal=nset)
                full_colon=tuple(max(a,b) for a,b in zip(full_colon,z))
        check(full_colon==mon(normal=inactive),'combined_symbol_exact_annihilator')
        # No positive integer kills the primitive detector. Finite checks below
        # are controls; polynomial coefficient one proves every characteristic.
        for modulus in (2,3,5,7,11,101):
            check(any(v%modulus for v in defect.values()),'seam_survives_characteristic_control')
        seam_decompositions.append(decomposition)
        seam_records.append({'branch_occurrence':label(s),'defect':encode_vector(defect),
                             'components':factors,'symbol_annihilator':'tau_minus' if s in PLUS else 'tau_plus'})

    # Exact scalar annihilator of the Ext^1 class. The ideal I+(tau_all)
    # kills it. These explicit corrections exhibit lifts of multiplication
    # by every short occurrence and by tau_all, with no denominators.
    scalar_annihilator_controls=[]
    for s in shorts:
        scalar=mon(xs=(s,))
        correction=[{} for _ in lifts]
        correction[0]=rel_images[shorts.index(s)]
        scaled_section=[add(multiply(v,scalar),scale(h,-1)) for v,h in zip(lifts,correction)]
        for name,r,defect in zip(a_names,a_rel,rel_images):
            corr_value={};lift_value={}
            for (i,m),n in r.items():
                corr_value=add(corr_value,scale(multiply(correction[i],m),n))
                lift_value=add(lift_value,scale(multiply(scaled_section[i],m),n))
            check(corr_value==multiply(defect,scalar),'short_occurrence_kills_extension_class',name)
            check(not lift_value,'scaled_short_section_descends_to_ideal',name)
        for gi,v in zip(gs,scaled_section):
            check(project(v,lambda c:level(c)==2)==multiply(theta,add_m(scalar,gi)),
                  'scaled_short_section_has_correct_generic_map')
        scalar_annihilator_controls.append('X'+label(s))
    scalar=mon(normal=SHORT)
    correction=[{}]
    for s in shorts:
        active=PLUS if s in PLUS else MINUS
        correction.append(scale(multiply(rel_images[shorts.index(s)],mon(normal=active)),-1))
    for name,r,defect in zip(a_names,a_rel,rel_images):
        corr_value={}
        for (i,m),n in r.items():corr_value=add(corr_value,scale(multiply(correction[i],m),n))
        check(corr_value==multiply(defect,scalar),'all_Rees_product_kills_extension_class',name)
    scalar_annihilator_controls.append('tau_all')

    # The branch-normal-form section is C-linear and grading preserving.
    # Tests choose arbitrary admitted monomials, without altering the ring.
    def normal_form_section(m):
        if not ring_monomial_ok(m):return {}
        ps,ms=plus_support(m),minus_support(m)
        if not ps and not ms:
            remainder=sub_m(m,gs[0])
            if not ring_monomial_ok(remainder):raise ValueError('outside lifting ideal')
            return multiply(lifts[0],remainder)
        active=PLUS if ps else MINUS
        first=sorted(ps or ms)[0]
        remainder=sub_m(m,mon(normal=active))
        remainder=sub_m(remainder,mon(xs=(first,)))
        if not ring_monomial_ok(remainder):raise ValueError('outside lifting ideal')
        return multiply(lifts[short_index[first]],remainder)
    for occurrences in subsets(SHORT):
        if set(occurrences)&PLUS and set(occurrences)&MINUS:continue
        active=set(SHORT) if not occurrences else (PLUS if set(occurrences)&PLUS else MINUS)
        for extra in ((),(SHORT[0],),tuple(SHORT)):
            k=add_m(mon(xs=occurrences,normal=active),mon(normal=extra))
            section=normal_form_section(k)
            check(project(section,lambda c:level(c)==2)==multiply(theta,k),'C_linear_section_generic_value')
            check(not project(apply(D,section),lambda c:level(c)>0),'C_linear_section_closed')
            check(homogeneous_degree(section)==add_m(k,mon(normal=LONG)),'C_linear_section_grade')
            for s in shorts:
                km=add_m(k,mon(xs=(s,)))
                lhs=add(multiply(section,mon(xs=(s,))),scale(normal_form_section(km),-1))
                expected={} if occurrences else multiply(rel_images[shorts.index(s)],sub_m(k,gs[0]))
                check(lhs==expected,'complete_first_coefficient_naturality_defect_formula')
            for tr,ori in ((0,1),(2,1),(4,1),(3,-1),(5,-1),(1,-1)):
                image_k=next(iter(action(basis(((),()),k),tr,ori)))[1]
                check(action(section,tr,ori)==normal_form_section(image_k),'C_linear_section_semilinear_transport')

    # H3(E) = (M + B^7)/(-defect, syzygy). Generate all internal M relations.
    hrel=[];hrel_names=[]
    for active,sgn in ((PLUS,'+'),(MINUS,'-')):
        inactive=set(SHORT)-set(active)
        for nset in subsets(inactive):
            if not 0<len(nset)<3:continue
            for s,t in combinations(sorted(active),2):
                hrel.append({(m_pos[(sgn,nset,s)],mon(xs=(t,))):1,
                             (m_pos[(sgn,nset,t)],mon(xs=(s,))):-1})
                hrel_names.append('M_koszul_'+sgn+'_'+str(nset)+'_'+label(s)+'_'+label(t))
            for s in sorted(active):
                for t in sorted(inactive):
                    hrel.append({(m_pos[(sgn,nset,s)],mon(xs=(t,))):1})
                    hrel_names.append('M_ann_'+sgn+'_'+str(nset)+'_'+label(t)+'_'+label(s))
    check(len(hrel)==144,'complete_internal_boundary_module_relations')
    for i,rel in enumerate(a_rel):
        r=dict(rel)
        if i<6:
            for key,n in seam_decompositions[i].items():r[key]=-n
        hrel.append(r);hrel_names.append(a_names[i])
    check((len(all_images),len(hrel))==(43,174),'full_lifting_module_presentation_sizes')
    hrdeg=[relation_degree(r,hweights) for r in hrel]
    for name,r in zip(hrel_names,hrel):
        v={}
        for (i,m),n in r.items():v=add(v,scale(multiply(all_images[i],m),n))
        check(not v,'all_presentation_relations_hold_in_actual_target',name)

    # Minimal framing: seven separate generators have no same-degree ambiguity.
    framing_records=[]
    for name,g,v in zip(lift_names,gs,lifts):
        grade=add_m(g,mon(normal=LONG))
        top,find,pinned,comps,reps,signs=top_kernel_at_grade(grade)
        check(len(comps)==1,'minimal_lift_unique')
        framing_records.append({'lift':name,'kernel_rank':len(comps),'boundary_ambiguity_rank':0})
    for s in shorts:
        grade=add_m(mon(xs=(s,),normal=SHORT),mon(normal=LONG))
        top,find,pinned,comps,reps,signs=top_kernel_at_grade(grade)
        check(len(comps)==7,'relation_degree_seven_lifts_one_generic_six_boundary')
        framing_records.append({'relation':'seam_'+label(s),'kernel_rank':7,'boundary_ambiguity_rank':6})

    # Integral exactness of the lifting-ideal presentation: squarefree modes
    # plus repeated-exponent cases. Illegal mixed output degrees are essential:
    # they test the opposite-sheet annihilator relations, not just Koszul rows.
    ideal_hist=Counter();ideal_cases=0
    grades=[mon(xs=occ,normal=ts) for occ in subsets(SHORT) for ts in subsets(SHORT)]
    for exps in product(range(3),repeat=6):
        if max(exps)<2:continue
        for ts in (PLUS,MINUS,set(SHORT)):
            g=list(mon(normal=ts))
            for s,n in zip(SHORT,exps):g[VAR[s]]=n
            grades.append(tuple(g))
    for g in grades:
        chosen,coeff,mat=relations_in_grade(g,gs,a_rel,a_rdeg)
        r,res=unit_reduce(mat)
        check(not any(any(row) for row in res),'ideal_presentation_integral_unit_reduction')
        outputs=[]
        for i in chosen:
            mm=add_m(coeff[i],gs[i]);outputs.append(int(ring_monomial_ok(mm)))
        targetrank=int(any(outputs))
        check(len(chosen)-r==targetrank,'ideal_presentation_exact_in_grade')
        for j in range(len(mat[0]) if mat else 0):
            check(sum(outputs[i]*mat[i][j] for i in range(len(chosen)))==0,'ideal_relation_matrix_kernel')
        ideal_hist[(len(chosen),r,targetrank)]+=1;ideal_cases+=1

    # Independent full top-kernel comparison with the 43/174 presentation in
    # 960 previous source multigrades and all generator-minimal multigrades.
    valid_occ=[s for s in subsets(SHORT) if not(set(s)&PLUS and set(s)&MINUS)]
    hgrades={add_m(mon(xs=o,normal=t),mon(normal=LONG)) for o in valid_occ for t in subsets(SHORT)}
    hgrades.update(hweights)
    module_hist=Counter();hcases=0
    for g in sorted(hgrades):
        top,find,pinned,comps,reps,signs=top_kernel_at_grade(g)
        chosen,coeff,mat=relations_in_grade(g,hweights,hrel,hrdeg)
        r,res=unit_reduce(mat)
        check(not any(any(row) for row in res),'module_relations_saturated_integer_lattice')
        check(len(chosen)-r==len(comps),'complete_module_presentation_rank')
        image_matrix=[[0]*len(chosen) for _ in comps]
        for j,i in enumerate(chosen):
            v=multiply(all_images[i],coeff[i])
            check(not project(apply(D,v),lambda c:level(c)>0),'presentation_column_is_actual_cycle')
            for k,component in enumerate(comps):
                c=reps[component]
                image_matrix[k][j]=signs[c]*v.get((c,coefficient_at_grade(c,g)),0)
        rr,rest=unit_reduce(image_matrix)
        check(rr==len(comps) and not any(any(row) for row in rest),'presentation_surjects_integrally_onto_actual_top_kernel')
        module_hist[(len(chosen),r,len(comps))]+=1;hcases+=1

    # The seven chosen lifts and all six syzygy defects form equivariant
    # families, without a division by group order or an invariant projector.
    group=[(0,1),(2,1),(4,1),(3,-1),(5,-1),(1,-1)]
    for tr,orient in group:
        perm=lambda s:diag(tr+orient*s[0],tr+orient*s[1])
        for c in CELLS:
            check(action(D[c],tr,orient)==apply(D,action(basis(c),tr,orient)),'full_dihedral_chain_action')
        check(action(lifts[0],tr,orient)==lifts[0],'common_lift_dihedral_invariance')
        for s in shorts:
            t=perm(s)
            check(action(lifts[short_index[s]],tr,orient)==lifts[short_index[t]],'branch_minimal_lift_covariance')
            check(action(rel_images[shorts.index(s)],tr,orient)==rel_images[shorts.index(t)],'seam_obstruction_family_covariance')
        for (sgn,nset,s),v in zip(m_keys,m_vec):
            t=perm(s);newsgn='+' if t in PLUS else '-'
            newn=tuple(sorted(map(perm,nset)))
            check(action(v,tr,orient)==all_images[m_pos[(newsgn,newn,t)]],'boundary_module_labelled_covariance')
    for defect in rel_images[:6]:
        check(kappa(defect)==defect,'fully_marked_syzygy_retained_in_PC')
        check(not apply(DC,defect,True),'syzygy_defect_PC_closed')

    def formal_encode(r):
        return [{'generator':all_names[i],'coefficient':n,
                 'monomial':{NAMES[j]:e for j,e in enumerate(m) if e}}
                for (i,m),n in sorted(r.items())]
    result={
        'schema':'marici.filtered_q.graded_lift_naturality.v1',
        'date':'2026-09-07','input_commit':COMMIT,
        'scope':'Fixed 215-state target over the alternating-sheet/Rees ring; not a complete physical source identification.',
        'target_states':215,'target_top_degree':3,
        'lifting_ideal_generators':[{'name':n,'monomial':{NAMES[j]:e for j,e in enumerate(g) if e}}
                                   for n,g in zip(lift_names,gs)],
        'ideal_relation_count':30,'ideal_relation_types':dict(Counter(a_kind)),
        'lifting_module_generator_count':43,'lifting_module_relation_count':174,
        'full_presentation_generators':[{'name':name,'image':encode_vector(v)} for name,v in zip(all_names,all_images)],
        'full_presentation_relations':[{'name':name,'terms':formal_encode(r)} for name,r in zip(hrel_names,hrel)],
        'seam_obstructions':seam_records,'fine_framing_controls':framing_records,
        'B_linear_section':'does not exist, even without grading or equivariance',
        'Ext1_extension_class':'nonzero; infinite additive order over Z; detected by first-conductor symbols',
        'Ext1_class_exact_B_annihilator':'I_plus + I_minus + (tau_plus*tau_minus)',
        'Ext1_class_cyclic_module':'C/(tau_plus*tau_minus)',
        'Ext1_annihilator_constructive_controls':scalar_annihilator_controls,
        'minimal_separate_lifts':'unique in all seven minimum fine degrees',
        'coefficient_naturality_defect':'24-term nonzero top boundary cycle for each of six common-to-branch relations',
        'higher_homotopy_repair_in_this_target':'impossible for these top-cycle differences because H4(E)=0 and difference in H3(A_boundary) is nonzero',
        'dihedral_status':'chosen lifts and nonzero defects are covariant; obstruction exists before imposing symmetry',
        'spectator_linear_section':'explicit graded D3-equivariant C-linear section on the entire lifting ideal, from its unique common/positive/negative normal form',
        'spectator_linear_zero_occurrence_sector':'lift h*tau_all -> h*lambda_0 over C only',
        'first_symbol_annihilators':{'+':'(tau_minus)','-':'(tau_plus)'},
        'first_symbol_effect':'conductor base restriction kills the displayed branch coefficients but their conormal symbols remain nonzero',
        'ideal_presentation_grade_cases':ideal_cases,
        'ideal_presentation_grade_histogram':[{'free_rank':a,'relation_rank':b,'quotient_rank':c,'cases':n}
              for (a,b,c),n in sorted(ideal_hist.items())],
        'full_module_grade_cases':hcases,
        'full_module_grade_histogram':[{'free_rank':a,'relation_rank':b,'quotient_rank':c,'cases':n}
              for (a,b,c),n in sorted(module_hist.items())],
        'checks':dict(sorted(COUNTS.items())),'exact_assertions':sum(COUNTS.values()),
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'proof_scope':'Arbitrary-polynomial completeness and non-splitting follow from the module presentation and first-conductor-symbol argument in the proof; finite exact grades independently test them.',
        'not_claimed':['No map from the native physical source to this target is invented.',
                       'The theta class is not identified with the exact Morse roof or the Entry-436 unit.',
                       'No scalar division by Rees factors, base occurrence inversion, or averaging is used.',
                       'No claim that the whole physical moduli groupoid is empty.',
                       'No assertion that the twelve ambiguity ideals may be discarded physically.',
                       'No full Ext1 group computation or proof-assistant verification.']}
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('schema','target_states','ideal_relation_count','lifting_module_generator_count',
          'lifting_module_relation_count','ideal_presentation_grade_cases','full_module_grade_cases','exact_assertions','B_linear_section')},indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('marici_q_lift_naturality_certificate_20260907.json'))
    args=parser.parse_args()
    execute(args.output)
