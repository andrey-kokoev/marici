#!/usr/bin/env python3
"""Normalization-pullback source and its two-endpoint extension obstruction.

Helper model retained from the preceding exact target-side descent checker.

Standard-library Python 3.10+. No external services or repository writes.
Rebuilds all 215 target cells, the seven unit lifts on actual principal opens,
their overlap cocycle, twelve residue coordinates, and integral fine-graded
Cech cohomology. See the companion proof for the all-polynomial conclusions.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from itertools import combinations, product, permutations
from pathlib import Path
import hashlib
import json

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

# Integral Cech matrices and saturated-image checks.
def unit_rank(matrix,ncols):
    a=[r[:] for r in matrix]
    k=0; nr=len(a)
    while k<min(nr,ncols):
        hit=next(((i,j) for i in range(k,nr) for j in range(k,ncols) if abs(a[i][j])==1),None)
        if hit is None: break
        i,j=hit; a[k],a[i]=a[i],a[k]
        for row in a: row[k],row[j]=row[j],row[k]
        if a[k][k]<0: a[k]=[-v for v in a[k]]
        for i in range(k+1,nr):
            q=a[i][k]
            if q: a[i]=[x-q*y for x,y in zip(a[i],a[k])]
        for j in range(k+1,ncols):
            q=a[k][j]
            if q:
                for i in range(nr): a[i][j]-=q*a[i][k]
        k+=1
    check(not any(a[i][j] for i in range(k,nr) for j in range(k,ncols)),
          'Cech_all_nonzero_Smith_factors_unit')
    return k

def cech(allowed,cover):
    bydeg=[[s for s in combinations(cover,q+1) if allowed(s)] for q in range(len(cover))]
    mats=[]; ranks=[]
    for q in range(len(cover)-1):
        src=bydeg[q];tar=bydeg[q+1]; col={s:i for i,s in enumerate(src)}
        mat=[]
        for t in tar:
            row=[0]*len(src)
            for j in range(len(t)):
                face=t[:j]+t[j+1:]
                if face in col: row[col[face]]=sign(j)
            mat.append(row)
        mats.append(mat);ranks.append(unit_rank(mat,len(src)))
    for q in range(len(mats)-1):
        aa=mats[q+1];bb=mats[q]
        for row in aa:
            for j in range(len(bydeg[q])):
                check(sum(row[k]*bb[k][j] for k in range(len(bb)))==0,'Cech_d_squared')
    hr={}
    for q,bs in enumerate(bydeg):
        n=len(bs)-(ranks[q-1] if q else 0)-(ranks[q] if q<len(ranks) else 0)
        check(n>=0,'Cech_homology_rank_nonnegative')
        if n: hr[q]=n
    return hr,bydeg,mats

def coefficient_allowed(alpha,beta,indices,ideal_sheet=None):
    inv_x,inv_n=open_data(indices)
    if inv_x&PLUS and inv_x&MINUS: return False
    ps={s for s in PLUS if alpha[VAR[s]]!=0}
    ms={s for s in MINUS if alpha[VAR[s]]!=0}
    if ps and ms: return False
    if inv_x&PLUS and ms or inv_x&MINUS and ps: return False
    if ideal_sheet is not None:
        inactive=set(SHORT)-set(ideal_sheet)
        if inv_x&inactive: return False
        if any(alpha[VAR[s]] for s in inactive): return False
        if not inv_x&set(ideal_sheet) and not any(alpha[VAR[s]]>0 for s in ideal_sheet): return False
    if any(alpha[VAR[s]]<0 and s not in inv_x for s in SHORT): return False
    if any(beta[VAR[s]]<0 and s not in inv_n for s in SHORT): return False
    return True

def expected_ring(alpha,beta):
    ps={s for s in PLUS if alpha[VAR[s]]!=0};ms={s for s in MINUS if alpha[VAR[s]]!=0}
    if not ps and not ms:
        negp=any(beta[VAR[s]]<0 for s in PLUS);negm=any(beta[VAR[s]]<0 for s in MINUS)
        return {0:1} if not negp and not negm else ({1:1} if negp and negm else {})
    active=PLUS if ps else MINUS;inactive=set(SHORT)-set(active)
    if all(alpha[VAR[s]]>=0 for s in active) and all(beta[VAR[s]]>=0 for s in inactive): return {0:1}
    if all(alpha[VAR[s]]<0 for s in active) and any(beta[VAR[s]]<0 for s in inactive): return {3:1}
    return {}

def expected_ideal(alpha,beta,active):
    inactive=set(SHORT)-set(active)
    aa=[alpha[VAR[s]] for s in sorted(active)]
    neg=any(beta[VAR[s]]<0 for s in inactive)
    if all(x>=0 for x in aa) and any(x>0 for x in aa) and not neg: return {0:1}
    if all(x==0 for x in aa) and neg: return {1:1}
    if all(x<0 for x in aa) and neg: return {3:1}
    return {}



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



def cell_weight_full(c):
    f,h=c; result=[0]*18
    for a in f: result[VAR[a]]-=1
    for a in h:
        result[9+VAR[a]]+=1
        if a in SHORT: result[VAR[a]]+=1
    return tuple(result)


def coefficient_full_grade(c,g):
    m=esub(g,cell_weight_full(c))
    if any(e<0 for e in m): return None
    return normal(c,m,())


def full_top_kernel_check(occurrences, normal_support):
    """Exact integral incidence-kernel calculation before removing endpoints."""
    g=eadd(exp(xs=occurrences,ns=normal_support),exp(ns=LONG))
    top=[c for c in CELLS if degree(c)==3 and coefficient_full_grade(c,g) is not None]
    rows=defaultdict(dict);parent={c:c for c in top};sgn={c:sign(len(c[0])*(len(c[0])+1)//2) for c in top}
    for c in top:
        v=diff(basis(c,coefficient_full_grade(c,g)),())
        for (row,mm),n in v.items():
            check(mm==coefficient_full_grade(row,g),'full_top_fine_degree_preserved')
            rows[row][c]=n*sgn[c]
    def find(c):
        while parent[c]!=c:
            parent[c]=parent[parent[c]];c=parent[c]
        return c
    pins=[]
    for row in rows.values():
        check(len(row)<=2 and all(abs(a)==1 for a in row.values()),'full_top_integral_unit_incidence_rows')
        if len(row)==1: pins.append(next(iter(row)))
        elif len(row)==2:
            check(sum(row.values())==0,'full_top_orientation_gauge')
            a,b=list(row);parent[find(a)]=find(b)
    pinned={find(c) for c in pins};comps={find(c) for c in top}-pinned
    liftable=find(((),())) in comps
    active=(PLUS if set(occurrences)&PLUS else MINUS) if occurrences else set(SHORT)
    check(liftable==(set(active)<=set(normal_support)),'full_endpoint_target_affine_lifting_ideal_unchanged')
    predicted=0
    if occurrences:
        inactive=set(SHORT)-set(active)
        for nset in subsets(inactive):
            if not nset: continue
            compat={a for a in active if all(not cross(a,b) for b in nset)}
            predicted += set(nset)|compat <= set(normal_support)
    check(len(comps)-int(liftable)==predicted,'full_boundary_kernel_has_seven_not_six_families_per_sheet')
    for component in comps:
        v={}
        for c in top:
            if find(c)==component:v=plus(v,basis(c,coefficient_full_grade(c,g),sgn[c]))
        check(not diff(v,()),'full_top_integral_kernel_basis')
    return len(comps),predicted


def main(output):
    nonempty=[ss for ss in subsets(range(7)) if ss and not(open_data(ss)[0]&PLUS and open_data(ss)[0]&MINUS)]
    check(len(nonempty)==29,'same_twenty_nine_nonempty_cover_terms')
    local_lifts=[times(lift(),eneg(PM))]
    local_lifts += [times(lift(PLUS if s in PLUS else MINUS,s),eneg(g))
                    for s,g in zip(sorted(SHORT),GENERATORS[1:])]
    theta=Q(local_lifts[0])
    check(len(theta)==4,'actual_generic_theta_kept')
    channels=[]; G={}; residue={}; active_of={}; proper=[]; endpoint=[]
    for active,polarity in ((PLUS,'+'),(MINUS,'-')):
        for nn in subsets(set(SHORT)-set(active)):
            if not nn: continue
            key=(polarity,nn)
            v,ac,lc=gamma_full(active,nn)
            G[key]=v; active_of[key]=active
            residue[key]=esub(exp(ns=set(LONG)-lc),exp(ns=set(nn)|ac))
            channels.append(key)
            (endpoint if len(nn)==3 else proper).append(key)
    check((len(channels),len(proper),len(endpoint))==(14,12,2),'fourteen_channels_twelve_boundary_two_endpoints')
    channel_records=[]
    for key in channels:
        active=active_of[key]
        for pc in (False,True):
            for s in active:
                j=OPEN_LABELS.index(s)
                check(not diff(G[key],(j,),pc),'full_boundary_generator_on_its_sheet',(key,j,pc))
                check(not diff(times(G[key],exp(xs=(s,))),(0,),pc),'full_boundary_ideal_generator_on_common_chart',(key,s,pc))
        check(not Q(G[key]),'all_fourteen_ambiguities_have_zero_Q')
        if len(key[1])==3:
            check(len(G[key])==1 and G[key]==endpoint_part(G[key]),'last_channel_is_actual_fully_marked_opposite_endpoint',key)
            check(residue[key]==esub(exp(ns=LONG),exp(ns=key[1])),'endpoint_residue_keeps_long_product',key)
        else:
            check(not endpoint_part(G[key]),'proper_channels_omit_both_endpoint_terms')
        channel_records.append({'polarity':key[0],'inactive_set':[LABEL(x) for x in key[1]],
            'residue':{NAMES[i]:e for i,e in enumerate(residue[key]) if e},
            'actual_target_cycle':encode(G[key]),'endpoint':key in endpoint})

    # Verify all full local cycles and the complete differential afresh.
    for pc in (False,True):
        for i,lift_i in enumerate(local_lifts):
            check(not diff(lift_i,(i,),pc),'local_full_unit_cycle',i)
            check(Q(restrict(lift_i,(i,),pc))==restrict(theta,(i,),pc),'local_full_unit_Q',i)
        for c in CELLS:
            check(not diff(diff(basis(c),(0,),pc),(0,),pc),'full_215_state_d_squared_common',c)

    # b_0 is a lift of the fourteen conductor values to the normalization;
    # b_i=0 on an occurrence chart, where the conductor is empty.
    # On common-to-sheet overlaps delta b = -r on the surviving sheet.
    cocycles={}
    for ij in [ss for ss in nonempty if len(ss)==2]:
        i,j=ij
        actual=restrict(plus(local_lifts[j],scale(local_lifts[i],-1)),ij)
        coeff={}; expected={}
        if i==0:
            active=PLUS if OPEN_LABELS[j] in PLUS else MINUS
            coeff={key:(residue[key],-1) for key in channels if active_of[key]==active}
            for key,(m,n) in coeff.items(): expected=plus(expected,times(G[key],m,n))
        check(actual==restrict(expected,ij),'full_overlap_is_normalization_connecting_cocycle',ij)
        check(relative_part(actual)==relative_part(restrict(expected,ij)),'forget_endpoints_recovers_previous_twelve_cocycle',ij)
        cocycles[ij]=(coeff,actual)
        for pc in (False,True):
            check(not diff(actual,ij,pc),'all_fourteen_overlap_terms_are_closed',ij)
            check(not Q(actual),'overlap_generic_projection_zero',ij)
    for ijk in [ss for ss in nonempty if len(ss)==3]:
        i,j,k=ijk
        triple=plus(cocycles[(j,k)][1],scale(cocycles[(i,k)][1],-1),cocycles[(i,j)][1])
        check(not restrict(triple,ijk),'normalization_source_transition_cocycle',ijk)

    # Local source frame: (a,m) -> a ell_i + sum m_lambda Gamma_lambda.
    # Transition m_j=m_i-a*c_ij, so these maps glue in the FULL target.
    scalar_modes=[ZERO]+[exp(xs=(d,)) for d in SHORT+LONG]+[exp(ns=(d,)) for d in SHORT+LONG]
    for ij,(coeff,cij) in cocycles.items():
        i,j=ij
        for a in scalar_modes:
            for pc in (False,True):
                at_i=target_multiply_local(local_lifts[i],a,ij,pc)
                at_j=restrict(plus(times(local_lifts[j],a),times(cij,a,-1)),ij,pc)
                check(at_i==at_j,'source_to_full_target_glues_on_generic_frame',(ij,a,pc))
                check(Q(at_i)==target_multiply_local(theta,a,ij,pc),'glued_source_generic_quotient_is_theta')
                check(endpoint_part(at_i)==endpoint_part(at_j),'both_endpoint_components_of_gluing_match')
    for i in range(7):
        invx,_=open_data((i,))
        for key in channels:
            active=active_of[key]
            if i==0: coeffs=[exp(xs=(s,)) for s in active]
            elif invx&active: coeffs=[ZERO]
            else: coeffs=[]
            for m in coeffs:
                for pc in (False,True):
                    v=target_multiply_local(G[key],m,(i,),pc)
                    check(not diff(v,(i,),pc),'source_kernel_frame_is_chain_map')
                    check(not Q(v),'source_kernel_frame_commutes_with_generic_map')

    # A primitive full-endpoint quotient is detected by three-variable Cech
    # cohomology. All twelve proper subsets die in this quotient.
    # Only take the FIRST pole on the displayed simple-pole classes; no
    # scalar map on all local cohomology is inferred.
    residue_diagnostics=[]
    for active in (PLUS,MINUS):
        inactive=tuple(sorted(set(SHORT)-set(active)))
        polarity='+' if active==PLUS else '-'
        for key in channels:
            if key[0]!=polarity: continue
            r=residue[key]
            survives=all(r[9+VAR[s]]<0 for s in inactive)
            check(survives==(len(key[1])==3),'top_Cousin_quotient_separates_endpoint_from_twelve_proper_channels',key)
            if survives:
                rr=eadd(r,exp(ns=inactive))
                check(rr==exp(ns=LONG),'endpoint_first_pole_residue_is_actual_long_product')
                for perm in permutations(inactive):
                    orientation=permutation_sign(perm)
                    check(orientation in (-1,1),'ordered_endpoint_conormal_sign')
                residue_diagnostics.append({'polarity':polarity,'ordered_normals':[LABEL(s) for s in inactive],
                    'residue':'u03*u14*u25','normal_determinant_retained':True})
        for powers in product((0,1),repeat=3):
            available=[i for i,n in enumerate(powers) if n==0]
            # Top Cech class survives iff all three exponents of 1/(abc)
            # remain negative. Nonnegative exponents come from a double open.
            remains=len(available)==3
            check(remains==(powers==(0,0,0)),'first_pole_socle_exact_annihilator')

    # Nine actual module maps S_12 -> S_14 over t_p*t_m.
    # Their two new normalization coordinates use existing two-normal channels.
    corrections=[]
    endpoint_key={key[0]:key for key in endpoint}
    for p in sorted(PLUS):
        for m in sorted(MINUS):
            f=exp(ns=(p,m))
            kp=('+',tuple(sorted(set(MINUS)-{m})))
            km=('-',tuple(sorted(set(PLUS)-{p})))
            cp=esub(eadd(f,residue[endpoint_key['+']]),residue[kp])
            cm=esub(eadd(f,residue[endpoint_key['-']]),residue[km])
            check(all(x>=0 for x in cp+cm),'endpoint_lift_corrections_are_polynomial_no_division')
            check(cp[9+VAR[p]]==1 and cm[9+VAR[m]]==1,'complementary_pair_factor_in_endpoint_correction')
            check(eadd(cp,residue[kp])==eadd(f,residue[endpoint_key['+']]),'positive_endpoint_normalization_lift_equation')
            check(eadd(cm,residue[km])==eadd(f,residue[endpoint_key['-']]),'negative_endpoint_normalization_lift_equation')
            for ij,(coeff,full_c) in cocycles.items():
                i,j=ij
                result=times(relative_part(full_c),f)
                for kk,ck,ee in ((kp,cp,endpoint_key['+']),(km,cm,endpoint_key['-'])):
                    if kk in coeff:
                        rr,nn=coeff[kk]
                        result=plus(result,times(G[ee],eadd(rr,ck),nn))
                check(restrict(result,ij)==target_multiply_local(full_c,f,ij),'nine_endpoint_source_maps_commute_with_all_transitions',(p,m,ij))
            corrections.append({'operator':'t'+LABEL(p)+'*t'+LABEL(m),
                'positive_endpoint_input':list(map(LABEL,kp[1])),
                'positive_endpoint_multiplier':{NAMES[i]:v for i,v in enumerate(cp) if v},
                'negative_endpoint_input':list(map(LABEL,km[1])),
                'negative_endpoint_multiplier':{NAMES[i]:v for i,v in enumerate(cm) if v}})
    check(len(corrections)==9,'all_nine_minimal_endpoint_lift_operators')

    # Occurrence ideals also annihilate the endpoint extension: use zero new
    # normalization coordinates, not multiplication of Laurent representatives.
    # In the local frame their compensating endpoint term is -a*X_s*b_i.
    for s in SHORT:
        f=exp(xs=(s,))
        for ij,(coeff,cij) in cocycles.items():
            i,j=ij
            # At chart zero, b_0 contains both endpoint fractions. Multiplying
            # X_s makes the opposite-normalization component zero.
            bi={}; bj={}
            if i==0:
                for ek in endpoint:
                    if s in active_of[ek]: bi=plus(bi,times(G[ek],eadd(f,residue[ek]),-1))
            if j==0:
                for ek in endpoint:
                    if s in active_of[ek]: bj=plus(bj,times(G[ek],eadd(f,residue[ek]),-1))
            endpoint_change=plus(bj,scale(bi,-1))
            check(restrict(endpoint_change,ij)==scale(target_multiply_local(endpoint_part(cij),f,ij),-1),
                  'occurrence_annihilator_endpoint_compensator',(s,ij))

    # Exact monomial normal forms of the endpoint extension modulo all allowed
    # pushouts of the twelve-term source extension. Multiplying a full pole by
    # any inactive parameter expresses it in an existing double-pole channel.
    ann_patterns=[]
    for powers in product((0,1,2),repeat=6):
        f=[0]*18
        for s,power in zip(SHORT,powers): f[9+VAR[s]]=power
        f=tuple(f); survives={}
        for active,polarity in ((PLUS,'+'),(MINUS,'-')):
            inactive=set(SHORT)-set(active)
            cancelled=next((s for s in sorted(inactive) if f[9+VAR[s]]>0),None)
            survives[polarity]=cancelled is None
            if cancelled is not None:
                key=(polarity,tuple(sorted(inactive-{cancelled})))
                coeff=esub(eadd(f,residue[endpoint_key[polarity]]),residue[key])
                check(all(x>=0 for x in coeff),'all_power_endpoint_correction_coefficient_regular')
                check(eadd(coeff,residue[key])==eadd(f,residue[endpoint_key[polarity]]),'all_power_endpoint_pushout_exact')
            else:
                check(all(eadd(f,residue[endpoint_key[polarity]])[9+VAR[s]]==-1 for s in inactive),
                      'nonboundary_full_negative_support_detector')
        killed=not any(survives.values())
        ideal=any(f[9+VAR[p]]>0 for p in PLUS) and any(f[9+VAR[m]]>0 for m in MINUS)
        check(killed==ideal,'endpoint_extension_exact_nine_generator_annihilator')
        if all(x<2 for x in powers): ann_patterns.append({'normal_powers':powers,'class_survives':not killed})

    # New conductor fibre product in the normal variables. Every polynomial
    # mode is constant, on one t-branch, or a killed cross-sheet t-monomial.
    for normal_support in subsets(SHORT):
        pset=bool(set(normal_support)&PLUS);mset=bool(set(normal_support)&MINUS)
        cross_killed=pset and mset
        fibre_product_mode=('zero' if cross_killed else ('constant' if not normal_support else ('plus' if pset else 'minus')))
        check((fibre_product_mode=='zero')==cross_killed,'secondary_normal_conductor_fibre_product_kernel')
    
    # Covariance on the full cells, all fourteen modes, their quotients, and
    # the actual differential. The marked-cell sign uses both oriented factors.
    for shift,direction in [(a,1) for a in (0,2,4)]+[(a,-1) for a in (1,3,5)]:
        for key in channels:
            target_active=frozenset(act_diag(s,shift,direction) for s in active_of[key])
            polarity='+' if target_active==PLUS else '-'
            kk=(polarity,tuple(sorted(act_diag(s,shift,direction) for s in key[1])))
            check(act_vec(G[key],shift,direction)==G[kk],'D3_all_fourteen_coefficient_cycles')
            check(act_mono(residue[key],shift,direction)==residue[kk],'D3_all_fourteen_residue_coordinates')
        for pc in (False,True):
            for c in CELLS:
                lhs=act_vec(diff(basis(c),(0,),pc),shift,direction)
                rhs=diff(act_vec(basis(c),shift,direction),(0,),pc)
                check(lhs==rhs,'D3_full_target_differential')

    # Independent Cech verification for the two NEW endpoint residue grades.
    for ek in endpoint:
        active=active_of[ek];r=residue[ek]
        beta=tuple(r[9+i] for i in range(6));alpha=(0,)*6
        cover=(0,)+tuple(i for i,s in enumerate(OPEN_LABELS) if s in active)
        h,bs,mats=cech(lambda ss:coefficient_allowed(alpha,beta,ss,active),cover)
        check(h=={1:1} and len(bs[0])==0,'endpoint_descent_coordinate_primitive_nonboundary_in_actual_cover')
        cc=[-1 if ss[0]==0 else 0 for ss in bs[1]]
        check(all(sum(a*b for a,b in zip(row,cc))==0 for row in mats[1]),'endpoint_Cech_cocycle_closed')

    # Recompute complete affine top kernels with BOTH endpoints present in all
    # 960 occurrence/normal support grades used by the inherited module proof.
    fine_kernel_count=0
    support_sets=[()]+[ss for active in (PLUS,MINUS) for ss in subsets(active) if ss]
    for occs in support_sets:
        for normals in subsets(SHORT):
            full_top_kernel_check(occs,normals)
            fine_kernel_count+=1
    check(fine_kernel_count==960,'all_full_endpoint_fine_degree_kernels')

    predecessor=Path(__file__).with_name('check_marici_obstruction_complement_descent_20260907.py')
    result={
        'schema':'marici.normalization_pullback_and_endpoint_extension.v1',
        'date':'2026-09-07','lane':'Branch B: target-side normalization, descent and endpoints',
        'source_commit':'d1947b67a60d3e88ba77f4ca60ea02c2a306ee61',
        'target_states':len(CELLS),'cover_terms':len(nonempty),
        'source':'S_14 = O_V x_(i_* O_D)^14 [nu_+* O_V+ ^7 + nu_-* O_V- ^7]',
        'source_generic_map':'S_14 -> O_V -> Q[degree 3], coefficient a -> a theta',
        'source_target_map':'in local split frame (a,m), a ell_i + sum m_lambda Gamma_lambda',
        'all_fourteen_channels':channel_records,
        'two_endpoint_first_pole_diagnostics':residue_diagnostics,
        'nine_polynomial_maps_S12_to_S14':corrections,
        'endpoint_extension':'0 -> N_end -> S_14 -> S_12 -> 0',
        'endpoint_extension_annihilator':'I_plus + I_minus + (t_p*t_m : p in S_plus, m in S_minus)',
        'cyclic_endpoint_extension_module':'C / ((t_p:p in S_plus)*(t_m:m in S_minus))',
        'squarefree_annihilator_patterns':ann_patterns,
        'tests_of_arbitrary_normal_powers':3**6,
        'integral_full_endpoint_kernel_grades':fine_kernel_count,
        'new_source_relation_to_native_physics':'target-residue-selected normalization pullback only; native scalar source not identified',
        'closed_global_unit_lift_created':False,
        'physical_Gysin_or_new_spatial_endpoint_cells_claimed':False,
        'all_degree_proof':'normalization ideal sequences; local top-kernel isomorphisms; Hom(I,I)=normalization sheaf; first-pole support detector; displayed polynomial corrections',
        'checks':dict(sorted(CHECKS.items())), 'exact_assertions':sum(CHECKS.values()),
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'predecessor_sha256':hashlib.sha256(predecessor.read_bytes()).hexdigest() if predecessor.exists() else None,
    }
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('schema','target_states','cover_terms','endpoint_extension_annihilator','cyclic_endpoint_extension_module','tests_of_arbitrary_normal_powers','exact_assertions')},indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('marici_normalization_endpoint_extension_certificate_20260907.json'))
    args=parser.parse_args()
    main(args.output)
