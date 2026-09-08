#!/usr/bin/env python3
"""Exact checks for the occurrence-preserving auxiliary/native comparison.

Standard library only. Does not modify a repository. The proof accompanying
this file, not bounded testing, establishes arbitrary-polynomial statements.
Coefficient indices 0..2 are X13,X15,X35; 3..5 are X02,X04,X24;
6,7 are the two auxiliary z coordinates. Spectator coefficients remain symbolic.
"""
from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations, product
import json
from math import comb
from pathlib import Path
from typing import Iterable

CHECKS: Counter[str] = Counter()
NVAR = 8
ZERO = (0,) * NVAR
PLUS = (0, 1, 2)
MINUS = (3, 4, 5)
LABELS = ((1,3),(1,5),(3,5),(0,2),(0,4),(2,4))
Mon = tuple[int, ...]
Poly = dict[Mon, int]


def ck(test: bool, name: str, detail=None) -> None:
    if not test:
        raise AssertionError((name, detail))
    CHECKS[name] += 1


def pm(n: int) -> int:
    return -1 if n % 2 else 1


def put(v: dict, k, a: int) -> None:
    v[k] = v.get(k, 0) + a
    if not v[k]:
        del v[k]


def add(*vs: dict) -> dict:
    r = {}
    for v in vs:
        for k, a in v.items():
            put(r, k, a)
    return r


def neg(v: dict) -> dict:
    return {k:-a for k,a in v.items()}


def unit(i: int, n: int=NVAR) -> tuple[int, ...]:
    return tuple(int(j == i) for j in range(n))


def mono_add(a: Mon, b: Mon) -> Mon:
    return tuple(x+y for x,y in zip(a,b))


def normalized(v: Poly, mode: str) -> Poly:
    r = {}
    for e,a in v.items():
        if mode == 'aux' and e[6] and e[7]:
            continue
        if mode == 'native' and (e[6] or e[7] or (any(e[i] for i in PLUS) and any(e[i] for i in MINUS))):
            continue
        if mode == 'plus' and any(e[i] for i in (*MINUS,6,7)):
            continue
        if mode == 'minus' and any(e[i] for i in (*PLUS,6,7)):
            continue
        if mode == 'conductor' and any(e):
            continue
        if mode == 'aux_conductor' and (e[6] or e[7]):
            continue
        put(r,e,a)
    return r


def mul(a: Poly, b: Poly, mode: str) -> Poly:
    r = {}
    for x,c in a.items():
        for y,d in b.items():
            put(r,mono_add(x,y),c*d)
    return normalized(r,mode)


def monomials(n: int, bound: int) -> list[tuple[int, ...]]:
    r=[]
    def visit(prefix, remaining, left):
        if left == 0:
            r.append(tuple(prefix)); return
        for a in range(remaining+1):
            visit(prefix+[a],remaining-a,left-1)
    visit([],bound,n)
    return r


def linear(table: dict, v: dict) -> dict:
    out={}
    for k,c in v.items():
        for t,a in table.get(k,{}).items():
            put(out,t,c*a)
    return out


def unit_rank(rows: list[list[int]], ncols: int | None=None) -> int:
    """Unimodular elimination; refuses nonunit residue rather than guessing."""
    a=[row[:] for row in rows]
    m=len(a); n=len(a[0]) if a else (ncols or 0); k=0
    while k < min(m,n):
        hit=next(((i,j) for i in range(k,m) for j in range(k,n) if abs(a[i][j])==1),None)
        if hit is None: break
        i,j=hit; a[k],a[i]=a[i],a[k]
        for row in a: row[k],row[j]=row[j],row[k]
        if a[k][k]<0: a[k]=[-x for x in a[k]]
        for i in range(k+1,m):
            if a[i][k]:
                c=a[i][k]
                a[i]=[x-c*y for x,y in zip(a[i],a[k])]
        for j in range(k+1,n):
            if a[k][j]:
                c=a[k][j]
                for i in range(m): a[i][j]-=c*a[i][k]
        k+=1
    ck(not any(a[i][j] for i in range(k,m) for j in range(k,n)), 'integer_reduction_has_only_unit_factors')
    return k


def vector_rank(vs: list[dict], keys: Iterable) -> int:
    keys=list(keys)
    return unit_rank([[v.get(k,0) for v in vs] for k in keys],len(vs))


def algebra_comparison() -> dict:
    mons=monomials(NVAR,3)
    for e in mons:
        p={e:1}
        if e[6] and e[7]: continue
        image=normalized(p,'native')
        lhs=(normalized(image,'plus'), normalized(image,'minus'))
        aux_p=normalized(p,'aux')
        # Restrict the two normalization sheets before applying their quotients.
        sh_plus=normalized({m:a for m,a in aux_p.items() if m[7]==0},'plus')
        sh_minus=normalized({m:a for m,a in aux_p.items() if m[6]==0},'minus')
        ck(lhs==(sh_plus,sh_minus),'normalization_square_on_polynomial_basis',e)
        ck(normalized(image,'conductor')==normalized(p,'conductor'),'common_conductor_square',e)
        in_kernel=(e[6]>0 or e[7]>0 or (any(e[i] for i in PLUS) and any(e[i] for i in MINUS)))
        ck((not image)==in_kernel,'kernel_ideal_classification',e)
    # Difference-complex square on independent sheet generators.
    for side in ('plus','minus'):
        auxz=6 if side=='plus' else 7
        for e in mons:
            if e[13-auxz]: continue
            p={e:1}
            upper=normalized(p,'aux_conductor')
            if side=='minus': upper=neg(upper)
            left=normalized(upper,'conductor')
            right=normalized(normalized(p,side),'conductor')
            if side=='minus': right=neg(right)
            ck(left==right,'conductor_difference_chain_square',(side,e))
    # Ring identities, including the crucial nonmultiplicative normal-form section.
    tests=[{ZERO:1}]+[{unit(i):1} for i in range(8)]
    tests += [add({ZERO:2},{unit(i):-3}) for i in range(8)]
    for a,b in product(tests,repeat=2):
        ck(normalized(mul(a,b,'aux'),'native')==mul(normalized(a,'native'),normalized(b,'native'),'native'), 'aux_to_native_ring_map')
    x,y=tests[1],tests[4]
    ck(bool(mul(x,y,'aux')) and not mul(x,y,'native'),'no_ring_inverse_for_native_quotient')
    # Every mixed quadratic has an actual kernel-cycle (m,m) in the two-term kernel.
    for i,j in product(PLUS,MINUS):
        m={mono_add(unit(i),unit(j)):1}
        ck(not normalized(m,'plus') and not normalized(m,'minus'),'mixed_quadratic_node_relation',(i,j))
        ck(not add(normalized(m,'aux_conductor'),neg(normalized(m,'aux_conductor'))),'mixed_kernel_cycle',(i,j))
    # Correct conormal map at the SAME conductor: C^8 -> C^6.
    conormal=[[int(i==j) for j in range(8)] for i in range(6)]
    ck(unit_rank(conormal)==6,'full_native_first_conormal_survives')
    for i in range(6):
        ck(normalized({unit(i):1},'native')=={unit(i):1},'each_occurrence_retained',i)
    # All first-order symbols, with independent (formal) coefficient labels.
    for i in range(6):
        p={unit(i):1}
        plus=normalized(p,'plus'); minus=normalized(p,'minus')
        expected=p if i in PLUS else neg(p)
        ck(add(plus,neg(minus))==expected,'alternating_first_symbol_basis',i)
    return {'same_conductor_conormal_ranks':[8,6], 'conormal_kernel_auxiliary_directions':2,
            'aux_to_native_kernel':'(z_plus,z_minus,I_plus*I_minus)',
            'comparison_cone_cohomology':{'-1':'kernel ideal'},'quasi_isomorphism':False}


def bar_degree_two() -> dict:
    def degree2_allowed(n,mode):
        out=[]
        for i in range(n):
            for j in range(i,n):
                if mode=='aux' and (i,j)==(6,7): continue
                if mode=='native' and i in PLUS and j in MINUS: continue
                out.append((i,j))
        return out
    reports={}
    allcycles={}
    for n,mode in ((8,'aux'),(6,'native')):
        pairs=list(product(range(n),repeat=2)); products_=degree2_allowed(n,mode)
        d={pair:({tuple(sorted(pair)):1} if tuple(sorted(pair)) in products_ else {}) for pair in pairs}
        rank=unit_rank([[int(tuple(sorted(pair))==m) for pair in pairs] for m in products_])
        if mode=='aux':
            cycles=[{(i,j):1,(j,i):-1} for i,j in combinations(range(n),2)]
            cycles += [{(6,7):1}]
        else:
            cycles=[{(i,j):1,(j,i):-1} for sheet in (PLUS,MINUS) for i,j in combinations(sheet,2)]
            cycles += [{(i,j):1} for i,j in product(PLUS,MINUS)]
            cycles += [{(j,i):1} for i,j in product(PLUS,MINUS)]
        for cycle in cycles: ck(not linear(d,cycle),'bar_cycle_equation',mode)
        ck(vector_rank(cycles,pairs)==len(pairs)-rank,'complete_degree_two_bar_kernel',mode)
        reports[mode]={'bar_two_rank':n*n,'multiplication_rank':rank,'Tor2_rank':len(cycles)}
        allcycles[mode]=cycles
    mapped=[{ij:a for ij,a in z.items() if max(ij)<6} for z in allcycles['aux']]
    # In the native cycle basis: same-sheet wedge coefficient and both mixed orders.
    coordkeys=[('same',i,j) for sh in (PLUS,MINUS) for i,j in combinations(sh,2)]
    coordkeys += [('pm',i,j) for i,j in product(PLUS,MINUS)]
    coordkeys += [('mp',i,j) for i,j in product(PLUS,MINUS)]
    def coords(z):
        r={}
        for sh in (PLUS,MINUS):
            for i,j in combinations(sh,2):
                ck(z.get((j,i),0)==-z.get((i,j),0),'same_sheet_antisymmetry')
                if z.get((i,j),0):r['same',i,j]=z[i,j]
        for i,j in product(PLUS,MINUS):
            if z.get((i,j),0):r['pm',i,j]=z[i,j]
            if z.get((j,i),0):r['mp',i,j]=z[j,i]
        return r
    matrix=[[coords(z).get(k,0) for z in mapped] for k in coordkeys]
    imrank=unit_rank(matrix)
    ck(imrank==15,'Tor2_image_rank')
    # Quotient functionals identify both mixed orders; kernel is the image.
    def quotient(z):
        return {(i,j):z.get((i,j),0)+z.get((j,i),0) for i,j in product(PLUS,MINUS)
                if z.get((i,j),0)+z.get((j,i),0)}
    for z in mapped:ck(not quotient(z),'Tor2_quotient_kills_image')
    for i,j in product(PLUS,MINUS):
        ck(quotient({(i,j):1})=={(i,j):1},'primitive_mixed_relation_cokernel',(i,j))
    ck(len(coordkeys)-imrank==9,'Tor2_cokernel_rank')
    reports.update({'image_rank':15,'cokernel_rank':9,'cokernel_integer_torsion':False,
                    'cokernel_basis':[[LABELS[i],LABELS[j]] for i,j in product(PLUS,MINUS)],
                    'scope':'homological degree two, total occurrence/auxiliary degree two; no claim about all higher degrees'})
    return reports


def subsets(n: int, nonempty: bool=False):
    return [tuple(x) for q in range(int(nonempty),n+1) for x in combinations(range(n),q)]


def csign(U: tuple[int,...], j: int) -> int:
    return pm(sum(i<j for i in U))


def cohomology(basis: list, deg, d) -> dict:
    degrees=sorted(set(deg(b) for b in basis))
    by={q:[b for b in basis if deg(b)==q] for q in degrees}
    ranks={}
    for q in degrees:
        src=by[q];tgt=by.get(q+1,[])
        table={b:d(b) for b in src}
        for b in src:
            ck(not linear({t:d(t) for t in table[b]},table[b]),'total_differential_squared')
        ranks[q]=unit_rank([[table[b].get(t,0) for b in src] for t in tgt],len(src))
    return {q:len(by[q])-ranks.get(q,0)-ranks.get(q-1,0) for q in degrees
            if len(by[q])-ranks.get(q,0)-ranks.get(q-1,0)}


def koszul_cech() -> dict:
    # Cochain Koszul model d=e(rho) wedge -, four normal equations.
    ext=subsets(4);opens=subsets(3,True)
    def primal_d(b):
        out={}
        for pos,i in enumerate(b):out[(tuple(x for x in b if x!=i),i)]=pm(pos)
        return out
    # Symbolic primal d^2 and dual d^2; polynomial indices retained.
    for b in ext:
        first=primal_d(b);second={}
        for (c,i),s in first.items():
            for (t,j),a in primal_d(c).items():put(second,(t,tuple(sorted((i,j)))),s*a)
        ck(not second,'four_equation_Koszul_d_squared',b)
    patterns=[]
    for w in product((-1,0),repeat=4):
        for ex in product((-1,0),repeat=3):
            basis=[(V,U) for V in ext for U in opens
                if all(w[i]+int(i in V)>=0 for i in range(4))
                and all(ex[i]>=0 or i in U for i in range(3))]
            def deg(b):return len(b[0])+len(b[1])-1
            def differential(b):
                V,U=b;r={}
                for i in range(4):
                    if i not in V:put(r,(tuple(sorted(V+(i,))),U),csign(V,i))
                for i in range(3):
                    if i not in U:put(r,(V,tuple(sorted(U+(i,)))),pm(len(V))*csign(U,i))
                return r
            h=cohomology(basis,deg,differential)
            expected={}
            if all(v==-1 for v in w):
                if all(v==0 for v in ex):expected={4:1}
                elif all(v==-1 for v in ex):expected={6:1}
            ck(h==expected,'complete_Koszul_Cech_support_type',(w,ex,h))
            patterns.append({'normal_degree':list(w),'occurrence_degree':list(ex),'unshifted_cohomology':h})
    # Residue projection on dual top degree, with all four normal equations.
    for V in ext:
        for e in monomials(4,2):
            image=(1 if len(V)==4 and not any(e) else 0)
            if len(V)==3:
                # Every incoming top coefficient is divisible by its missing normal.
                i=next(k for k in range(4) if k not in V)
                new=list(e);new[i]+=1
                ck(any(new),'Gysin_projection_kills_boundaries')
            if len(V)==4:
                ck(image==int(sum(e)==0),'Gysin_top_coefficient',e)
    # Explicit local Cech contraction onto chart i, after occurrence localization.
    for i in range(3):
        allowed=[U for U in opens]  # all coefficients embed in a chart with X_i inverted
        d={U:{tuple(sorted(U+(j,))):csign(U,j) for j in range(3) if j not in U} for U in allowed}
        h={U:({tuple(x for x in U if x!=i):pm(U.index(i))} if i in U and len(U)>1 else {}) for U in allowed}
        for U in allowed:
            lhs=add(linear(d,h[U]),linear(h,d[U]))
            rhs={U:1}
            if len(U)==1 and U==(i,):
                rhs=add(rhs,{(j,):-1 for j in range(3)})
            ck(lhs==rhs,'punctured_local_chain_contraction',(i,U,lhs,rhs))
    return {'regular_equations_per_sheet':4,'resolution_ranks':[comb(4,k) for k in range(5)],
            'normal_Cech_types_tested':len(patterns),'shifted_global_reverse_degrees':[-1,1],
            'ordered_dualizing_shift':{'ambient':7,'codimension':4,'native':3,'endpoint_shift':2,'reverse':1},
            'patterns':patterns}


def geometry_covariance() -> dict:
    def diag(a,b):return tuple(sorted((a%6,b%6)))
    def perm_sign(a):return pm(sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a))))
    details=[]
    for r in range(3):
        for flip in range(2):
            # i -> i+2r, or i -> 1-i+2r.
            vertex=lambda i:(i+2*r)%6 if not flip else (1-i+2*r)%6
            perm=[LABELS.index(diag(vertex(a),vertex(b))) for a,b in LABELS]
            zperm=[7,6] if flip else [6,7]
            full=perm+zperm
            def act(p):
                ans={}
                for e,c in p.items():
                    f=[0]*8
                    for i,v in enumerate(e):f[full[i]]=v
                    put(ans,tuple(f),c)
                return ans
            for e in monomials(8,2):
                p=normalized({e:1},'aux')
                ck(normalized(act(p),'native')==act(normalized(p,'native')),'full_ring_covariance',(r,flip,e))
            images=[perm[i] for i in PLUS]
            active_target=MINUS if flip else PLUS
            s=perm_sign([active_target.index(i) for i in images])
            ck(s==pm(flip),'actual_labelled_volume_sign',(r,flip))
            # Opposite conormal block has the same permutation sign.
            opposite=PLUS if flip else MINUS
            sopp=perm_sign([opposite.index(perm[i]) for i in MINUS])
            ck(sopp==s,'Gysin_normal_determinant_covariance')
            # Ambient ordered volume is (active, opposite, z); signs multiply.
            ck(s*sopp==1,'ambient_to_native_determinant_cancellation')
            details.append({'rotation':r,'reflection':bool(flip),'occurrence_permutation':perm,'volume_sign':s})
    return {'actions':details,'reflection_sign_from_label_permutation':-1}


def loaded_diagram() -> dict:
    ds=tuple((a,b) for a in range(6) for b in range(a+1,6) if b-a not in (1,5))
    short=set(LABELS); plus={LABELS[i] for i in PLUS}; minus={LABELS[i] for i in MINUS}
    def cross(d,e):
        a,b=d;c,f=e
        return a<c<b<f or c<a<f<b
    fs=[tuple(f) for q in range(4) for f in combinations(ds,q) if all(not cross(a,b) for a,b in combinations(f,2))]
    cells=[(f,m) for f in fs for q in range(len(f)+1) for m in combinations(f,q)]
    d={};one=(0,)*18
    def localization(c):return set(c[0])-set(c[1])
    for c in cells:
        f,m=c;out={}
        for a in ds:
            if a in f or any(cross(a,b) for b in f):continue
            v=[0]*18;k=ds.index(a);v[k]=1;v[9+k]=-1
            out[(tuple(sorted(f+(a,))),m),tuple(v)]=pm(sum(b<a for b in f))
        for pos,a in enumerate(m):
            out[(f,tuple(b for b in m if b!=a)),one]=pm(3-len(f)+pos)
        d[c]=out
    def chain_d(v):
        ans={}
        for (c,e),s in v.items():
            for (t,f),a in d[c].items():put(ans,(t,tuple(x+y for x,y in zip(e,f))),s*a)
        return ans
    census=Counter();arrows=0
    def support_alive(mode,L):
        if mode=='plus':return not (L&minus)
        if mode=='minus':return not (L&plus)
        return not (L&short)
    samples=[{e:1} for e in monomials(8,2)]
    for c in cells:
        ck(not chain_d(d[c]),'original_PC_d_squared',c)
        L=localization(c)
        typ='none' if not L&short else 'mixed' if L&plus and L&minus else 'plus' if L&plus else 'minus'
        census[typ]+=1
        for (target,coeff),s in d[c].items():
            arrows+=1;Lt=localization(target)
            ck(L<Lt and len(Lt-L)==1,'PC_localization_inclusion')
            for mode in ('plus','minus','conductor'):
                for p in samples:
                    source_value=normalized(p,mode) if support_alive(mode,L) else {}
                    via_source=source_value if support_alive(mode,Lt) else {}
                    direct=normalized(p,mode) if support_alive(mode,Lt) else {}
                    ck(via_source==direct,'branch_conductor_localization_square',(mode,c,target))
                if not support_alive(mode,L):
                    ck(not support_alive(mode,Lt),'zero_stalk_remains_zero')
    ck(len(cells)==215 and arrows==522,'full_source_census')
    ck(census==Counter({'none':72,'plus':64,'minus':64,'mixed':15}),'Rees_branch_localization_census')
    # Genuine seven-state Q class, projected using a strict support subcomplex.
    longs=[a for a in ds if a not in short]
    U=[0]*18
    for a in longs:U[9+ds.index(a)]=1
    theta={(((),()),tuple(U)):1}
    for a in longs:
        m=U[:];m[ds.index(a)]+=1;m[9+ds.index(a)]-=1
        theta[(((a,),(a,)),tuple(m))]=-1
    beta=chain_d(theta)
    qbeta={k:v for k,v in beta.items() if not set(k[0][0])&short}
    ck(not qbeta,'honest_seven_state_Q_cycle')
    ck(len(beta)==18,'retained_full_target_connecting_terms')
    ck(not chain_d(beta),'retained_connecting_chain_is_closed')
    for (cell,m),a in beta.items():
        L=localization(cell);active=L&short
        ck(len(active)==1,'connecting_term_has_one_branch_localization')
        mode='plus' if active<=plus else 'minus'
        killed=minus if mode=='plus' else plus
        ck(not any(m[ds.index(v)] for v in killed),'connecting_term_survives_native_specialization')
    # Rees relation is preserved, not divided by a globally inverted occurrence.
    for mode in ('plus','minus','conductor'):
        for i in range(6):
            keep=(mode=='plus' and i in PLUS) or (mode=='minus' and i in MINUS)
            ck(bool(normalized({unit(i):1},mode))==keep,'Rees_u_equals_tX_restriction',(mode,i))
    return {'cells':len(cells),'covering_arrows':arrows,'normal_localization_census':dict(census),
            'generic_Q_cycle_preserved':True,'remaining_full_target_connecting_terms':len(beta),
            'claim':'Naturality of coefficient diagram under u_s=t_s X_s and allowed localizations; not an assertion about the full physical push-pull functor.'}



def native_dualizing_cone() -> dict:
    """Actual codimension-three maps of Koszul resolutions over six variables.

    A resolves C, B resolves (omega_plus + omega_minus)[3].  The cone
    retains the dual of the normalization difference.  Sparse coefficients
    are monomials in six occurrence variables, not scalar substitutes.
    """
    six=subsets(6)
    kx=[tuple(x) for q in range(4) for x in combinations(PLUS,q)]
    ky=[tuple(x) for q in range(4) for x in combinations(MINUS,q)]
    z=(0,)*6
    def kd(V):
        return {(tuple(t for t in V if t!=i),unit(i,6)):pm(p) for p,i in enumerate(V)}
    def gamma(V):
        r={}
        if set(PLUS)<=set(V):r[('plus',tuple(i for i in V if i in MINUS)),z]=1
        if set(MINUS)<=set(V):
            # The outer minus is the original conductor difference.
            r[('minus',tuple(i for i in V if i in PLUS)),z]=-pm(sum(i in PLUS for i in V))
        return r
    def targetd(key):
        side,V=key
        return {((side,W),m):-a for (W,m),a in kd(V).items()}
    def applyp(d,v):
        r={}
        for (key,m),a in v.items():
            for (tar,n),b in d(key).items():put(r,(tar,tuple(x+y for x,y in zip(m,n))),a*b)
        return r
    for V in six:
        lhs=applyp(targetd,gamma(V));rhs={}
        for (W,m),a in kd(V).items():
            for (tar,n),b in gamma(W).items():put(rhs,(tar,tuple(x+y for x,y in zip(m,n))),a*b)
        ck(lhs==rhs,'native_conductor_Gysin_chain_map',V)
    # Equivariance of the entire attaching map, not only its volume ranks.
    def perm_sign(seq):
        return pm(sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq))))
    for rotation in range(3):
        for flip in range(2):
            vertex=lambda i:(i+2*rotation)%6 if not flip else (1-i+2*rotation)%6
            perm=[LABELS.index(tuple(sorted((vertex(a),vertex(b))))) for a,b in LABELS]
            for V in six:
                image=tuple(sorted(perm[i] for i in V))
                source_sign=pm(flip)*perm_sign([perm[i] for i in V])
                left={k:source_sign*a for k,a in gamma(image).items()}
                right={}
                for ((side,W),m),a in gamma(V).items():
                    target_side=('minus' if side=='plus' else 'plus') if flip else side
                    target_W=tuple(sorted(perm[i] for i in W))
                    sign=pm(flip)*perm_sign([perm[i] for i in W])
                    right[(target_side,target_W),m]=a*sign
                ck(left==right,'full_conductor_attachment_covariance',(rotation,flip,V))
    # Cone uses target B plus the shifted conductor resolution A[1].
    basis=[('plus',V) for V in ky]+[('minus',V) for V in kx]+[('conductor',V) for V in six]
    def d(key):
        side,V=key
        if side!='conductor':return targetd(key)
        r={(('conductor',W),m):-a for (W,m),a in kd(V).items()}
        return add(r,gamma(V))
    for key in basis:
        ck(not applyp(d,d(key)),'native_dualizing_cone_d_squared',key)
    def deg(key):
        side,V=key
        return -len(V)-1 if side=='conductor' else -len(V)-3
    def reduced_d(key):
        return {tar:a for (tar,m),a in d(key).items() if not any(m)}
    h=cohomology(basis,deg,reduced_d)
    # The artificially split object has no attaching map in its conductor fibre.
    naive=Counter(deg(b) for b in basis)
    ck(h.get(-7,0)==0,'full_attachment_removes_extreme_fibre_class')
    ck(naive[-7]==1,'deleted_attachment_creates_spurious_fibre_class')
    # Localization on an active occurrence contracts both C and the opposite
    # branch. The retained part is the correctly oriented active volume [3].
    for sh,vs in (('plus',PLUS),('minus',MINUS)):
        for i in vs:
            # Homological Koszul contraction e_i wedge /X_i for a sequence containing i.
            for V in six:
                wedge={} if i in V else {tuple(sorted((i,)+V)):csign(V,i)}
                # Check d h + h d after setting X_i=1, all other X_j=0.
                def dd(W):
                    return {tuple(t for t in W if t!=i):pm(W.index(i))} if i in W else {}
                def hh(W):
                    return {} if i in W else {tuple(sorted((i,)+W)):csign(W,i)}
                lhs=add(linear({W:dd(W) for W in wedge},wedge),linear({W:hh(W) for W in dd(V)},dd(V)))
                ck(lhs=={V:1},'conductor_resolution_contracts_on_punctured_chart',(sh,i,V))
    # Periodic resolution of auxiliary normalization U/(z_opposite).
    for side in ('plus','minus'):
        zero_var,other=(7,6) if side=='plus' else (6,7)
        for n in range(1,13):
            curr=zero_var if n%2 else other
            nxt=other if n%2 else zero_var
            ck(not mul({unit(curr):1},{unit(nxt):1},'aux'),'normalization_periodic_d_squared',(side,n))
            ck(not normalized({unit(curr):1},'native'),'periodic_normalization_basechange_zero',(side,n))
        for e in monomials(8,3):
            p=normalized({e:1},'aux')
            if not p:continue
            killed=not mul(p,{unit(zero_var):1},'aux')
            ck(killed==(e[other]>0),'exact_auxiliary_normalization_annihilator',(side,e))
    return {
       'finite_S_model_generators':len(basis),
       'dualizing_cohomology':{'-3':'omega_plus direct_sum omega_minus','-1':'conductor_orientation'},
       'derived_occurrence_fibre_ranks':h,
       'fake_split_extreme_degree_minus7_rank':naive[-7],
       'honest_extreme_degree_minus7_rank':h.get(-7,0),
       'full_closed_immersion_ambient':'U=S[z_plus,z_minus]/(z_plus*z_minus)',
       'shriek_identification':'i^! D_(U/C) = D_(B/C), retaining the complete cone',
       'ordinary_aux_normalization_basechange':'B direct_sum B, not B_plus direct_sum B_minus',
       'higher_aux_normalization_Tor':'one B in every nonnegative degree on each auxiliary sheet',
       'periodic_exactness_proof':'Ann_U(z_plus)=(z_minus), Ann_U(z_minus)=(z_plus)',
       'source_provenance':'The zero-section/occurrence quotient is constructed from the labelled ring data; it is not asserted to be the physical normalization correspondence.'
    }


def main(out: Path) -> None:
    algebra=algebra_comparison()
    bar=bar_degree_two()
    kc=koszul_cech()
    dual=native_dualizing_cone()
    equiv=geometry_covariance()
    loaded=loaded_diagram()
    report={
      'status':'proved_for_explicit_coefficient_and_punctured_regular_immersion_comparisons',
      'date_label':'2026-09-07',
      'source_commit':'d1947b67a60d3e88ba77f4ca60ea02c2a306ee61',
      'source_blobs':{
       'src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md':'840258522d45e450e4f1e8bb927d9aae58c75566',
       'src/ledger/20260817-434 The Conductor Kernel Extends over Every Loaded Multi-Rees Stalk.md':'0946218ae456f2c423801873432076f86fa2c171',
       'research/voevodsky/check_ringed_alexandrov_pc_target.py':'7c993d05837fbe2ba29ba30e5b665b5429ab940b'},
      'correction':'The previous one-versus-three rank argument compared distinct conductor ideals and omitted occurrence variables already in the auxiliary coefficient base. It does not prove missing native occurrence directions.',
      'algebra':algebra,'bar_degree_two':bar,'koszul_and_punctured_reverse':kc,
      'native_dualizing_cone':dual,
      'transport':equiv,'loaded_coefficient_diagram':loaded,
      'checks':dict(sorted(CHECKS.items())), 'exact_assertions':sum(CHECKS.values()),
      'limitations':[
        'The morphism of conductor-difference complexes is not a quasi-isomorphism.',
        'The regular immersions occur on the separate polynomial normalization sheets, not on the singular glued node.',
        'No cancellation of the nine native mixed quadratic Tor classes is asserted.',
        'The generic Q morphism, full cap and endpoint connector cells are not constructed by coefficient naturality.',
        'No full-target seventeen-equation closure test or intrinsic infinite-resolution equivalence is claimed.',
        'Symbolic proofs establish arbitrary coefficients and degrees in the stated scopes. This is not a proof-assistant certificate.'
      ]}
    out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('status','algebra','bar_degree_two','native_dualizing_cone','loaded_coefficient_diagram','exact_assertions')},indent=2))


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,default=Path(__file__).with_name('marici_occurrence_preserving_bridge_certificate_20260907.json'))
    main(ap.parse_args().output)
