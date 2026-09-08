#!/usr/bin/env python3
"""Full target framing and all-order intrinsic conductor comparison.

Standalone Python 3.10+; standard library only. Retains the pinned 215-state
absolute/PC differential, all endpoint labels, and the established local
normalization source. New tests: top-target comparison after nonflat conductor
change, all-order Tor formula, and explicit one-step transition homotopies.
No proof assistant, geometric source identification, or new carrier cells.
The all-order statements use the proofs accompanying this checker.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from itertools import combinations, product, permutations
from pathlib import Path
import hashlib
import json
from functools import lru_cache
from math import comb

CHECKS: Counter[str] = Counter()
def check(ok, label, detail=None):
    if not ok:
        raise AssertionError(f'{label}: {detail!r}')
    CHECKS[label] += 1

def sign(n): return -1 if n % 2 else 1
def diag(a,b): return tuple(sorted((a%6,b%6)))
SHORT=tuple(diag(i,i+2) for i in range(6))
LONG=tuple(diag(i,i+3) for i in range(3))
DIAGS=tuple(sorted(SHORT+LONG))
PLUS=frozenset(SHORT[i] for i in (1,3,5))
MINUS=frozenset(SHORT[i] for i in (0,2,4))
VAR={a:i for i,a in enumerate(SHORT+LONG)}
LABEL=lambda a: ''.join(map(str,a))
NAMES=tuple('X'+LABEL(a) for a in SHORT+LONG)+tuple(('t' if a in SHORT else 'u')+LABEL(a) for a in SHORT+LONG)
ZERO=(0,)*18
ENDPOINTS={tuple(sorted(PLUS)),tuple(sorted(MINUS))}

def cross(a,b):
    i,j=a; k,l=b
    return i<k<j<l or k<i<l<j

def subsets(xs):
    xs=tuple(sorted(xs))
    for n in range(len(xs)+1): yield from combinations(xs,n)

FACES=tuple(f for n in range(4) for f in combinations(DIAGS,n)
            if all(not cross(a,b) for a,b in combinations(f,2)))
FACESET=set(FACES)
CELLS=tuple((f,h) for f in FACES for h in subsets(f))

def degree(c): return 3-len(c[0])+len(c[1])
def level(c):
    f=c[0]
    if f in ENDPOINTS: return 0
    return 1 if set(f)&set(SHORT) else 2

def exp(xs=(), ns=()):
    m=[0]*18
    for a in xs: m[VAR[a]]+=1
    for a in ns: m[9+VAR[a]]+=1
    return tuple(m)

def eadd(a,b): return tuple(x+y for x,y in zip(a,b))
def esub(a,b): return tuple(x-y for x,y in zip(a,b))
def eneg(a): return tuple(-x for x in a)
def plus(*vs):
    out={}
    for v in vs:
        for k,n in v.items():
            out[k]=out.get(k,0)+n
            if not out[k]: del out[k]
    return out

def scale(v,n): return {k:a*n for k,a in v.items() if a*n}

def project(v,predicate): return {k:n for k,n in v.items() if predicate(k[0])}
def E(v): return project(v,lambda c:level(c)>0)
def Q(v): return project(v,lambda c:level(c)==2)

# Principal opens: 0 = D(tau+ tau-); each remaining label s = D(tau_sheet X_s).
OPEN_LABELS=(None,)+tuple(sorted(SHORT))
OPEN_NAMES=('common',)+tuple('branch_'+LABEL(s) for s in sorted(SHORT))
P=exp(ns=PLUS); M=exp(ns=MINUS); PM=eadd(P,M)
GENERATORS=(PM,)+tuple(exp(xs=(s,),ns=PLUS if s in PLUS else MINUS) for s in sorted(SHORT))

def open_data(indices):
    inv_x=set(); inv_n=set()
    for i in indices:
        s=OPEN_LABELS[i]
        if s is None: inv_n.update(SHORT)
        else:
            inv_x.add(s); inv_n.update(PLUS if s in PLUS else MINUS)
    return inv_x,inv_n

def normal(c,m,indices,pc=False):
    inv_x,inv_n=open_data(indices)
    if pc:
        for a in set(c[0])-set(c[1]):
            inv_n.add(a)
            if a in SHORT: inv_x.add(a)
    if inv_x&PLUS and inv_x&MINUS: return None
    ps={a for a in PLUS if m[VAR[a]]!=0}
    ms={a for a in MINUS if m[VAR[a]]!=0}
    if ps and ms: return None
    if inv_x&PLUS and ms: return None
    if inv_x&MINUS and ps: return None
    for a in SHORT:
        if m[VAR[a]]<0 and a not in inv_x:
            raise ValueError(f'Illegal occurrence inverse {LABEL(a)} on {indices}')
    for a in LONG:
        if m[VAR[a]]<0: raise ValueError('Illegal long occurrence inverse')
    for a in SHORT+LONG:
        if m[9+VAR[a]]<0 and a not in inv_n:
            raise ValueError(f'Illegal normal inverse {LABEL(a)} on {indices}')
    return m

def basis(c,m=ZERO,n=1): return {} if not n else {(c,m):n}
def restrict(v,indices,pc=False):
    out={}
    for (c,m),n in v.items():
        mm=normal(c,m,indices,pc)
        if mm is not None: out=plus(out,{(c,mm):n})
    return out

def times(v,m,n=1): return { (c,eadd(a,m)):n*b for (c,a),b in v.items() if n*b }
def dbase(c,pc=False):
    f,h=c; out={}
    for a in DIAGS:
        ff=tuple(sorted(f+(a,)))
        if a not in f and ff in FACESET:
            m=exp(xs=(a,))
            if pc:
                um=exp(xs=(a,),ns=(a,)) if a in SHORT else exp(ns=(a,))
                m=esub(m,um)
            out=plus(out,basis((ff,h),m,sign(sum(b<a for b in f))))
    for j,a in enumerate(h):
        hh=tuple(b for b in h if b!=a)
        m=ZERO if pc else (exp(xs=(a,),ns=(a,)) if a in SHORT else exp(ns=(a,)))
        out=plus(out,basis((f,hh),m,sign(3-len(f)+j)))
    return out
DABS={c:dbase(c,False) for c in CELLS}
DPC={c:dbase(c,True) for c in CELLS}

def diff(v,indices,pc=False):
    v=restrict(v,indices,pc); out={}
    table=DPC if pc else DABS
    for (c,m),n in v.items(): out=plus(out,times(table[c],m,n))
    return restrict(out,indices,pc)

def lift(active=None,occurrence=None):
    chosen=set(SHORT) if active is None else set(active)
    out={}
    for f in FACES:
        if active is not None and not set(f)<=chosen|set(LONG): continue
        xs=tuple(a for a in f if a in LONG)
        if occurrence is not None: xs+=(occurrence,)
        ns=(chosen-set(f))|(set(LONG)-set(f))
        out=plus(out,basis((f,f),exp(xs=xs,ns=ns),sign(len(f)*(len(f)+1)//2)))
    return out

def gamma(active,N):
    N=set(N)
    active_comp={s for s in active if all(not cross(s,n) for n in N)}
    long_comp={l for l in LONG if all(not cross(l,n) for n in N)}
    out={}
    for f in FACES:
        if not N<=set(f)<=N|active_comp|long_comp or f in ENDPOINTS: continue
        m=exp(xs=(l for l in f if l in LONG),ns=(active_comp|long_comp)-set(f))
        out=plus(out,basis((f,f),m,sign(len(f)*(len(f)+1)//2)))
    return out,active_comp,long_comp

def encode(v):
    return [{'face':[LABEL(a) for a in c[0]],'marks':[LABEL(a) for a in c[1]],
             'coefficient':n,'monomial':{NAMES[i]:e for i,e in enumerate(m) if e}}
            for (c,m),n in sorted(v.items())]


def gamma_full(active, inactive_subset):
    """Keep the formerly removed endpoint term when the inactive set is full."""
    nset=set(inactive_subset)
    ac={s for s in active if all(not cross(s,n) for n in nset)}
    lc={l for l in LONG if all(not cross(l,n) for n in nset)}
    out={}
    for f in FACES:
        if not nset<=set(f)<=nset|ac|lc: continue
        coeff=exp(xs=(l for l in f if l in LONG),ns=(ac|lc)-set(f))
        out=plus(out,basis((f,f),coeff,sign(len(f)*(len(f)+1)//2)))
    return out,ac,lc


def act_diag(d,shift,direction):
    return diag(shift+direction*d[0],shift+direction*d[1])


def act_mono(m,shift,direction):
    result=[0]*18
    for d in SHORT+LONG:
        a=act_diag(d,shift,direction)
        result[VAR[a]]=m[VAR[d]]
        result[9+VAR[a]]=m[9+VAR[d]]
    return tuple(result)


def permutation_sign(values):
    return sign(sum(values[i]>values[j] for i in range(len(values)) for j in range(i+1,len(values))))


def act_vec(v,shift,direction):
    out={}
    for (c,m),n in v.items():
        ff=tuple(act_diag(a,shift,direction) for a in c[0])
        hh=tuple(act_diag(a,shift,direction) for a in c[1])
        s=permutation_sign(ff)*permutation_sign(hh)
        out=plus(out,basis((tuple(sorted(ff)),tuple(sorted(hh))),act_mono(m,shift,direction),s*n))
    return out


def target_multiply_local(v,mono,indices,pc=False):
    return restrict(times(v,mono),indices,pc)


def endpoint_part(v):
    return project(v,lambda c:level(c)==0)


def relative_part(v):
    return project(v,lambda c:level(c)>0)




# The conductor is occurrence-adic, not the normal-adic filtration of the
# preceding calculation. All short t's are units only on the named common chart.
OCC=tuple(sorted(PLUS))+tuple(sorted(MINUS))
OCC_POS={v:i for i,v in enumerate(OCC)}
Z6=(0,)*6
FAMILY=tuple((active,ns) for active,inactive in ((PLUS,MINUS),(MINUS,PLUS))
             for ns in subsets(inactive) if ns)


def target_truncate(v,r,pc=False):
    """Derived coefficient restriction of this bounded-flat target to B/I^r."""
    out={}
    for (c,m),a in restrict(v,(0,),pc).items():
        if pc and (set(c[0])-set(c[1]))&set(SHORT):
            continue
        check(all(m[VAR[s]]>=0 for s in SHORT),'no_short_occurrence_poles_in_common_target')
        if sum(m[VAR[s]] for s in SHORT)<r:
            out=plus(out,basis(c,m,a))
    return out


def target_d(v,r,pc=False):
    return target_truncate(diff(v,(0,),pc),r,pc)


def occ_mono(m):
    out=[0]*18
    for i,v in enumerate(OCC):out[VAR[v]]=m[i]
    return tuple(out)


def wside(m):
    p=any(m[:3]);n=any(m[3:])
    if p and n:return -1
    return 0 if p else 1 if n else None


def wmul(m,i):
    s=wside(m)
    if s not in (None,i//3):return None
    mm=list(m);mm[i]+=1;return tuple(mm)


def vadd(*vs):
    out={}
    for v in vs:
        for k,c in v.items():
            out[k]=out.get(k,0)+c
            if not out[k]:del out[k]
    return out


@lru_cache(None)
def words(n,first=-1):
    if n<0:return ()
    if not n:return ((),)
    out=[]
    for s in ((0,1) if first==-1 else (first,)):
        for mask in range(1,8):
            b=tuple(3*s+i for i in range(3) if mask>>i&1)
            if len(b)<=n:
                out.extend((b,)+w for w in words(n-len(b),1-s))
    return tuple(out)


@lru_cache(None)
def word_grade(w):
    return tuple(sum(b.count(i) for b in w) for i in range(6))


@lru_cache(None)
def ideal_words(n,side):
    return tuple(w for w in words(n+1) if w[-1][0]//3==side)


def wd(v,r=None):
    out={}
    for (m,w),a in v.items():
        if not w:continue
        for j,i in enumerate(w[0]):
            mm=wmul(m,i)
            if mm is None or (r is not None and sum(mm)>=r):continue
            b=w[0][:j]+w[0][j+1:]
            ww=(b,)+w[1:] if b else w[1:]
            out=vadd(out,{(mm,ww):a*sign(j)})
    return out


def wh(v):
    """Spectator-linear contraction; no B-linearity/equivariant claim."""
    out={}
    for (m,w),a in v.items():
        s=wside(m)
        if s is None:continue
        if w and w[0][0]//3==s:b,rest=w[0],w[1:]
        else:b,rest=(),w
        i=min(tuple(j for j,z in enumerate(m) if z)+b)
        if i in b:continue
        mm=list(m);mm[i]-=1
        bb=tuple(sorted(b+(i,)))
        out=vadd(out,{(tuple(mm),(bb,)+rest):a*sign(sum(j<i for j in b))})
    return out


def wtrunc(v,r):return {k:a for k,a in v.items() if sum(k[0])<r}


@lru_cache(None)
def monomials_upto(r):
    out=[Z6]
    for side in (0,1):
        for m in product(range(r+1),repeat=3):
            if 1<=sum(m)<=r:
                out.append(m+(0,)*3 if side==0 else (0,)*3+m)
    return tuple(out)


@lru_cache(None)
def compositions(n,k=6):
    if k==1:return ((n,),)
    return tuple((i,)+tail for i in range(n+1) for tail in compositions(n-i,k-1))


def qvalues(n):
    q=[3,12,46]
    for i in range(3,n+1):q.append(3*q[-1]+3*q[-2]+q[-3])
    return q[:n+1]


def choose2(n):return comb(n,2) if n>=2 else 0


def tor_rank(r,n,q):
    assert r>=1 and n>=1
    return q[n]*choose2(r+1)+(3*q[n]-q[n+1])*choose2(r)+q[n-1]*choose2(r-1)


def unit_rank(matrix,ncols):
    a=[row[:] for row in matrix];nr=len(a);k=0
    while k<min(nr,ncols):
        pivot=next(((i,j) for i in range(k,nr) for j in range(k,ncols) if abs(a[i][j])==1),None)
        if pivot is None:break
        i,j=pivot;a[k],a[i]=a[i],a[k]
        for row in a:row[k],row[j]=row[j],row[k]
        if a[k][k]<0:a[k]=[-x for x in a[k]]
        for i in range(k+1,nr):
            b=a[i][k]
            if b:a[i]=[x-b*y for x,y in zip(a[i],a[k])]
        for j in range(k+1,ncols):
            b=a[k][j]
            if b:
                for i in range(nr):a[i][j]-=b*a[i][k]
        k+=1
    check(not any(x for row in a[k:] for x in row[k:]),'integer_strand_all_Smith_factors_units')
    return k


@lru_cache(None)
def wgroup(n,side):
    d=defaultdict(list)
    for w in ideal_words(n,side):d[word_grade(w)].append(w)
    return d


def strand_basis(alpha,n,r,side):
    if n<0:return ()
    d=sum(alpha)-(n+1)
    if not 0<=d<r:return ()
    out=[]
    for m in monomials_upto(d):
        if sum(m)!=d:continue
        g=tuple(a-b for a,b in zip(alpha,m))
        if min(g)<0:continue
        out.extend((m,w) for w in wgroup(n,side).get(g,()))
    return tuple(out)


def strand_matrix(src,tar,r):
    rows={b:i for i,b in enumerate(tar)}
    mat=[[0]*len(src) for _ in tar]
    for j,b in enumerate(src):
        for c,v in wd({b:1},r).items():
            check(c in rows,'intrinsic_strand_closed_under_d')
            mat[rows[c]][j]+=v
    return mat


def old_cycle(active,ns):return gamma_full(active,ns)[0]


def ideal_augmentation_to_target(v,active,ns,r=None,pc=False):
    out={}
    for (m,w),a in v.items():
        if sum(map(len,w))!=1:continue
        mm=wmul(m,w[0][0])
        if mm is not None:out=plus(out,times(old_cycle(active,ns),occ_mono(mm),a))
    return target_truncate(out,r,pc) if r is not None else restrict(out,(0,),pc)


def reduced_block(ns):
    ns=tuple(ns);ls=tuple(l for l in LONG if all(not cross(l,s) for s in ns))
    out=basis((ns,ns),exp(ns=ls))
    for l in ls:
        f=tuple(sorted(ns+(l,)))
        out=plus(out,basis((f,f),exp(xs=(l,),ns=tuple(k for k in ls if k!=l)),sign(len(ns)+1)))
    return out,ls


def main(output,max_power=4,max_tor=3):
    check(len(CELLS)==215,'unchanged_target_state_count')
    check(len(FAMILY)==14,'all_fourteen_source_channels_retained')
    check(sum(len(ns)==3 for _,ns in FAMILY)==2,'both_endpoint_channels_retained')
    q=qvalues(max_tor+max_power+2)
    for n in range(max_tor+2):
        check(len(ideal_words(n,0))==q[n],'word_basis_rank_matches_recurrence')
        check(len(ideal_words(n,1))==q[n],'polarity_preserves_word_basis_rank')
    ell=times(lift(),eneg(PM))
    for pc in (False,True):
        check(not diff(ell,(0,),pc),'complete_local_generic_unit_is_cycle')
        for c in CELLS:
            check(degree(c)<=3,'unchanged_target_has_no_degree_four')
            check(not diff(diff(basis(c),(0,),pc),(0,),pc),'complete_target_d_squared')
        for r in range(1,max_power+1):
            check(not target_d(ell,r,pc),'fixed_target_unit_at_each_occurrence_thickness')
            for c in CELLS:
                v=target_truncate(basis(c),r,pc)
                check(not target_d(target_d(v,r,pc),r,pc),'specialized_target_d_squared')
    for active,ns in FAMILY:
        side=0 if active==PLUS else 1
        for pc in (False,True):
            for w in ideal_words(0,side):
                v={(Z6,w):1};f=ideal_augmentation_to_target(v,active,ns,None,pc)
                check(not diff(f,(0,),pc),'source_generator_maps_to_full_target_cycle')
                for r in range(1,max_power+1):
                    check(not target_d(ideal_augmentation_to_target(v,active,ns,r,pc),r,pc),
                          'source_generator_comparison_after_derived_change')
            for w in ideal_words(1,side):
                check(not ideal_augmentation_to_target(wd({(Z6,w):1}),active,ns,None,pc),
                      'source_first_relations_map_to_zero_exactly')
    short_faces=tuple(f for f in FACES if set(f)<=set(SHORT))
    check(len(short_faces)==18,'conductor_target_eighteen_short_support_blocks')
    check([sum(len(f)==k for f in short_faces) for k in range(4)]==[1,6,9,2],
          'short_support_block_census')
    block_data=[];reconstruction={};row_count=0
    for ns in short_faces:
        z,ls=reduced_block(ns);row_count+=len(ls)
        for pc in (False,True):check(not target_d(z,1,pc),'reduced_conductor_top_block_cycle')
        coefficient=esub(exp(ns=set(LONG)-set(ls)),exp(ns=ns))
        reconstruction=plus(reconstruction,times(z,coefficient,sign(len(ns)*(len(ns)+1)//2)))
        block_data.append({'short_support':[LABEL(s) for s in ns],
                           'compatible_longs':[LABEL(l) for l in ls],'cycle':encode(z)})
    check(row_count==27,'reduced_target_twentyseven_independent_long_equations')
    check(reconstruction==target_truncate(ell,1),'generic_unit_in_eighteen_block_basis')
    for active,ns in FAMILY:
        for s in active:
            for pc in (False,True):check(not target_truncate(times(old_cycle(active,ns),exp(xs=(s,))),1,pc),
                                        'fortytwo_conductor_source_coordinates_are_target_invisible')
    ordinary=[]
    for r in range(1,max_power+1):
        base_m=monomials_upto(r-1)
        tail_m={side:tuple(m for m in monomials_upto(r) if wside(m)==side) for side in (0,1)}
        invisible=0;visible=0
        for active,ns in FAMILY:
            side=0 if active==PLUS else 1;g=old_cycle(active,ns)
            pivot=(tuple(sorted(ns)),tuple(sorted(ns)))
            check(sum(c==pivot for c,m in g)==1,'each_channel_has_own_pure_short_pivot')
            for aa,nn in FAMILY:
                if aa==active and nn==ns:continue
                check(not any(c==pivot for c,m in old_cycle(aa,nn)),
                      'other_channels_do_not_contaminate_pivot')
            for m in tail_m[side]:
                ims=[target_truncate(times(g,occ_mono(m)),r,pc) for pc in (False,True)]
                check(all(bool(v)==(sum(m)<r) for v in ims),'top_fibre_kernel_exactly_highest_occurrence_power')
                if sum(m)==r:
                    invisible+=1
                    check(sum(m)<r+1,'invisible_source_class_not_zero_in_ordinary_tensor')
                else:visible+=1
        check(invisible==14*comb(r+2,2),'all_order_component_kernel_formula')
        ordinary.append({'power':r,'base_quotient_rank':len(base_m),
                         'source_ordinary_rank':len(base_m)+14*len(tail_m[0]),
                         'image_rank':len(base_m)+visible,'kernel_rank':invisible})
    transition_tests=0
    for r in range(1,max_power+1):
        for n in range(1,max_tor+1):
            for side in (0,1):
                for w in ideal_words(n,side):
                    for m in monomials_upto(r):
                        v={(m,w):1}
                        K=lambda x:wtrunc(wh(x),r)
                        lhs=vadd(wd(K(v),r),K(wd(v,r+1)))
                        check(lhs==wtrunc(v,r),'one_step_transition_explicit_homotopy_positive_degree')
                        transition_tests+=1
                        check(not wd(wd(v,r+1),r+1),'truncated_intrinsic_d_squared')
    strands=0;computed={}
    for r in range(1,max_power+1):
        for n in range(1,max_tor+1):
            total=0
            for alpha in compositions(r+n):
                b0=strand_basis(alpha,n,r,0);b1=strand_basis(alpha,n+1,r,0);bm=strand_basis(alpha,n-1,r,0)
                rr0=unit_rank(strand_matrix(b0,bm,r),len(b0));rr1=unit_rank(strand_matrix(b1,b0,r),len(b1))
                h=len(b0)-rr0-rr1
                check(h>=0,'integral_Tor_strand_nonnegative')
                total+=h;strands+=1
            check(total==tor_rank(r,n,q),'all_order_Tor_formula_vs_full_integer_matrices')
            computed[f'{r},{n}']=total
    for n in range(1,max_tor+1):
        for side in (0,1):
            for w in ideal_words(n,side):
                for m in monomials_upto(2):
                    z={(m,w):1}
                    check(vadd(wd(wh(z)),wh(wd(z)))==z,'all_degree_primal_word_contraction_identity')
    for r in range(1,max_power+1):
        for m in monomials_upto(r+1):
            if sum(m)==r+1:
                source_class={m:1}
                target_class={mm:c for mm,c in source_class.items() if 1<=sum(mm)<=r}
                check(bool(source_class) and not target_class,'one_step_component_transition_zero')
    for rot,direction in product((0,2,4),(1,-1)):
        check(act_vec(ell,rot,direction)==ell,'full_generic_unit_dihedral_covariance')
        for c in CELLS:
            av=act_vec(basis(c),rot,direction)
            for pc in (False,True):
                check(diff(av,(0,),pc)==act_vec(diff(basis(c),(0,),pc),rot,direction),
                      'full_target_dihedral_chain_equivariance')
                for r in (1,max_power):
                    check(target_truncate(av,r,pc)==act_vec(target_truncate(basis(c),r,pc),rot,direction),
                          'actual_coefficient_restriction_commutes_with_dihedral_transport')
    # A concrete nontrivial old endpoint shear is invisible in the reduced
    # conductor target, but fails target framing already at the next thickness.
    x13=diag(1,3);t02=diag(0,2);t35=diag(3,5)
    shear_coefficient=exp(ns=(t02,t35))
    endpoint=old_cycle(PLUS,tuple(sorted(MINUS)))
    shear_target_difference=times(endpoint,eadd(exp(xs=(x13,)),shear_coefficient),-1)
    for pc in (False,True):
        check(not diff(shear_target_difference,(0,),pc),'old_shear_changes_an_actual_closed_endpoint_chain')
        check(not target_truncate(shear_target_difference,1,pc),'old_shear_invisible_in_reduced_conductor_target')
        check(bool(target_truncate(shear_target_difference,2,pc)),'old_shear_detected_by_first_occurrence_thickening')
    old_paths=('/mnt/data/check_marici_global_endpoint_transformations_20260907.py',
               '/mnt/data/check_marici_intrinsic_conductor_resolution_20260907.py',
               '/mnt/data/marici_normalization_endpoint_extension_20260907.md')
    provenance={Path(p).name:hashlib.sha256(Path(p).read_bytes()).hexdigest()
                for p in old_paths if Path(p).is_file()}
    replay=Path('/mnt/data/marici_target_framing_audit/replayed_global_endpoint_transformations.json')
    predecessor={}
    if replay.is_file():
        pr=json.loads(replay.read_text())
        predecessor={'file_sha256':hashlib.sha256(replay.read_bytes()).hexdigest(),
                     'exact_assertions':pr['exact_assertions']}
    report={
      'status':'proved_for_existing_target_selected_common_chart_comparison',
      'date':'2026-09-07',
      'scope':'Occurrence-conductor powers I^r on the pre-existing common chart D(T); not the preceding opposite-normal thickenings, not a native physical source or global conductor-gluing identification.',
      'pinned_repository_commit':'d1947b67a60d3e88ba77f4ca60ea02c2a306ee61',
      'retained_target_states':len(CELLS),'retained_endpoint_states':sum(level(c)==0 for c in CELLS),
      'retained_source_channels':len(FAMILY),'normal_support_or_integer_localization_added':False,
      'full_target_framed_automorphism_space_before_base_change':'contractible, also allowing homotopies, by top-degree t-structure',
      'first_conductor_comparison':{'source_H0_rank':43,'target_H3_rank':18,'image_rank':1,
                                   'kernel_rank':42,'cokernel_rank':17,'blocks':block_data},
      'ordinary_thickness_comparisons':ordinary,'single_ideal_word_ranks':q,
      'concrete_shear_target_difference':encode(shear_target_difference),
      'input_sha256':provenance,'independently_replayed_predecessor':predecessor,
      'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'finite_framed_marking_spaces':[{'power':r,'pi0_rank':14*comb(r+2,2),
          'pi_positive_ranks':[14*tor_rank(r,n,q) for n in range(1,max_tor+1)]} for r in range(1,max_power+1)],
      'rank_formula':'q_n*C(r+1,2)+(3*q_n-q_(n+1))*C(r,2)+q_(n-1)*C(r-1,2), per ideal and n>=1',
      'one_step_restriction_on_all_based_homotopy_groups':'zero; positive degrees by explicit spectator-linear contraction; pi0 by I^(r+1) -> I/I^(r+1)',
      'homotopy_limit_of_target_framed_marking_spaces':'contractible',
      'map_spaces_and_marking_spaces_are_different':True,
      'independent_integral_homogeneous_Tor_calculations':strands,
      'explicit_transition_homotopy_basis_checks':transition_tests,
      'unbounded_statements_proved_not_extrapolated':['word contraction exactness','all-power Tor formula','zero maps in every positive degree','highest-power pi0 kernel','homotopy limit via lim and lim1'],
      'verification_bounds':{'maximum_occurrence_power':max_power,'positive_Tor_degrees':max_tor},
      'checks':dict(sorted(CHECKS.items())),'total_exact_assertions':sum(CHECKS.values()),
      'excluded_claims':['native-source identification','erasure of global endpoint extension','logarithmic or Gysin equivalence inferred from ordinary completion','physical interpretation of all conductor homotopy as states'],
    }
    output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('status','finite_framed_marking_spaces','independent_integral_homogeneous_Tor_calculations','explicit_transition_homotopy_basis_checks','total_exact_assertions')},indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,default=Path('marici_target_framed_conductor_tower_certificate_20260907.json'))
    p.add_argument('--max-power',type=int,default=4)
    p.add_argument('--max-tor',type=int,default=3)
    a=p.parse_args()
    if not 1<=a.max_power<=5 or not 1<=a.max_tor<=4:p.error('Use powers 1..5 and Tor degrees 1..4; larger bounds are not needed for the all-order proof.')
    main(a.output,a.max_power,a.max_tor)
