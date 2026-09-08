#!/usr/bin/env python3
"""Exact target-side descent on the complement of the true Q obstruction.

Standard-library Python 3.10+. No external services or repository writes.
Rebuilds all 215 target cells, the seven unit lifts on actual principal opens,
their overlap cocycle, twelve residue coordinates, and integral fine-graded
Cech cohomology. See the companion proof for the all-polynomial conclusions.
"""
from __future__ import annotations
import argparse
from collections import Counter
from itertools import combinations, product
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

def main(output):
    check(len(CELLS)==215,'target_cell_count')
    nonempty=[s for s in subsets(range(7)) if s and not (open_data(s)[0]&PLUS and open_data(s)[0]&MINUS)]
    census=[sum(len(s)==n for s in nonempty) for n in range(1,5)]
    check(census==[7,12,8,2],'seven_open_cover_intersection_census')
    # Check the entire coefficient differential after every permitted open restriction.
    for pc in (False,True):
        for s in nonempty:
            for c in CELLS:
                v=restrict(basis(c),s,pc)
                check(not diff(diff(v,s,pc),s,pc),'localized_full_target_d_squared')
    full_lifts=[lift()]+[lift(PLUS if s in PLUS else MINUS,s) for s in sorted(SHORT)]
    locals_=[times(v,eneg(g)) for v,g in zip(full_lifts,GENERATORS)]
    theta=Q(times(full_lifts[0],eneg(PM)))
    check(len(theta)==4,'genuine_generic_cycle_four_terms')
    for i,v in enumerate(locals_):
        for pc in (False,True):
            check(not diff(v,(i,),pc),'local_unit_lift_closed_before_endpoint_quotient',i)
            check(Q(restrict(v,(i,),pc))==restrict(theta,(i,),pc),'local_unit_lift_projection',i)
    records=[]; residue_vectors={};gammas={}
    for active,sheet in ((PLUS,'+'),(MINUS,'-')):
        inactive=set(SHORT)-set(active)
        for ns in subsets(inactive):
            if not 0<len(ns)<3: continue
            gv,ac,lc=gamma(active,ns)
            numerator=exp(ns=set(LONG)-lc)
            denominator=exp(ns=set(ns)|ac)
            q=esub(numerator,denominator)
            key=(sheet,ns);residue_vectors[key]=q;gammas[key]=gv
            records.append({'sheet':sheet,'inactive_subset':[LABEL(a) for a in ns],
                            'compatible_active':[LABEL(a) for a in sorted(ac)],
                            'residue_exponents':{NAMES[i]:e for i,e in enumerate(q) if e},
                            'annihilator_over_C':[LABEL(a) for a in ns],
                            'target_generator':encode(gv)})
    check(len(records)==12,'twelve_residue_coordinates')
    overlaps={}
    endpoint_records=[]
    for i,j in combinations(range(7),2):
        if (i,j) not in nonempty: continue
        overlap=E(restrict(plus(locals_[j],scale(locals_[i],-1)),(i,j)))
        overlaps[(i,j)]=overlap
        for pc in (False,True):
            actual=E(restrict(plus(locals_[j],scale(locals_[i],-1)),(i,j),pc))
            check(not E(diff(actual,(i,j),pc)),'overlap_is_actual_boundary_supported_cycle')
            check(not Q(actual),'overlap_has_zero_generic_projection')
        if i==0:
            active=PLUS if OPEN_LABELS[j] in PLUS else MINUS;sheet='+' if active==PLUS else '-'
            rhs={}
            for key,q in residue_vectors.items():
                if key[0]==sheet: rhs=plus(rhs,times(gammas[key],q,-1))
            check(overlap==restrict(rhs,(i,j)),'actual_overlap_equals_twelve_residue_formula',j)
            endpoint=project(restrict(plus(locals_[j],scale(locals_[i],-1)),(i,j)),lambda c:level(c)==0)
            endpoint_records.append({'chart':OPEN_NAMES[j],'full_endpoint_difference':encode(endpoint)})
            check(bool(endpoint),'endpoint_differences_retained_not_set_zero')
        else: check(not overlap,'same_sheet_local_unit_lifts_agree')
    for ijk in [s for s in nonempty if len(s)==3]:
        i,j,k=ijk
        defect=restrict(plus(overlaps[(j,k)],scale(overlaps[(i,k)],-1),overlaps[(i,j)]),ijk)
        check(not defect,'all_triple_overlap_cocycle_equations')

    # Independent exact fine-graded Cech computation on the 7-open cover.
    alpha_types=[(0,)*6]
    for active in (PLUS,MINUS):
        for a in product((-1,0,1),repeat=3):
            if a==(0,0,0): continue
            v=[0]*6
            for s,e in zip(sorted(active),a): v[VAR[s]]=e
            alpha_types.append(tuple(v))
    ring_hist=Counter();fine_count=0
    for alpha in alpha_types:
        for beta in product((-1,0),repeat=6):
            got,_,_=cech(lambda s:coefficient_allowed(alpha,beta,s),tuple(range(7)))
            expect=expected_ring(alpha,beta)
            check(got==expect,'whole_open_ring_fine_degree_cohomology',(alpha,beta,got,expect))
            ring_hist[tuple(sorted(got.items()))]+=1;fine_count+=1
    check(fine_count==3392,'all_whole_ring_sign_support_types')
    ideal_hist=Counter();ideal_count=0
    for active in (PLUS,MINUS):
        inactive=set(SHORT)-set(active)
        cover=(0,)+tuple(i for i,s in enumerate(OPEN_LABELS) if s in active)
        for aa in product((-1,0,1),repeat=3):
            alpha=[0]*6
            for s,e in zip(sorted(active),aa):alpha[VAR[s]]=e
            for bb in product((-1,0),repeat=3):
                beta=[0]*6
                for s,e in zip(sorted(inactive),bb):beta[VAR[s]]=e
                got,_,_=cech(lambda ss:coefficient_allowed(alpha,beta,ss,active),cover)
                expect=expected_ideal(alpha,beta,active)
                check(got==expect,'boundary_ideal_fine_degree_cohomology',(aa,bb,got,expect))
                ideal_hist[tuple(sorted(got.items()))]+=1;ideal_count+=1
    check(ideal_count==432,'all_boundary_ideal_sign_support_types')

    # Check each explicit residue is a primitive Cech cocycle and has no degree-0
    # cochain in its exact internal degree. Arbitrary numerator divisibility is
    # proved separately, and all squarefree annihilator patterns checked here.
    for key,q in residue_vectors.items():
        active=PLUS if key[0]=='+' else MINUS
        beta=tuple(q[9+i] for i in range(6));alpha=(0,)*6
        cover=(0,)+tuple(i for i,s in enumerate(OPEN_LABELS) if s in active)
        h,bs,mats=cech(lambda ss:coefficient_allowed(alpha,beta,ss,active),cover)
        check(h=={1:1} and len(bs[0])==0,'each_residue_primitive_and_nonboundary')
        cv=[-1 if s[0]==0 else 0 for s in bs[1]]
        check(all(sum(a*b for a,b in zip(row,cv))==0 for row in mats[1]),'explicit_residue_cocycle_is_closed')
    for bits in product((0,1),repeat=6):
        both_zero=True
        per_sheet={'+':True,'-':True}
        for key,q in residue_vectors.items():
            active=PLUS if key[0]=='+' else MINUS
            inactive=set(SHORT)-set(active)
            killed=all(q[9+VAR[s]]+bits[VAR[s]]>=0 for s in inactive)
            per_sheet[key[0]] &= killed;both_zero &= killed
            expect=all(bits[VAR[s]] for s in key[1])
            check(killed==expect,'individual_residue_exact_monomial_annihilator')
        check(per_sheet['+']==all(bits[VAR[s]] for s in MINUS),'positive_six_residues_annihilator_tau_minus')
        check(per_sheet['-']==all(bits[VAR[s]] for s in PLUS),'negative_six_residues_annihilator_tau_plus')
        check(both_zero==all(bits),'total_residue_annihilator_six_factor_product')

    # Independent monomial test of B/a = (B+/(p)) x_{C/(p,m)} (B-/(m)).
    normalization_cases=0
    supports=[set()]+[set(s) for act in (PLUS,MINUS) for s in subsets(act) if s]
    for support in supports:
        for bits in product((0,1),repeat=6):
            pp=all(bits[VAR[s]] for s in PLUS);mm=all(bits[VAR[s]] for s in MINUS)
            in_a=pp and mm if not support else (pp if support&PLUS else mm)
            first_zero=(not support or bool(support&PLUS)) and pp or bool(support&MINUS)
            second_zero=(not support or bool(support&MINUS)) and mm or bool(support&PLUS)
            check(in_a==(first_zero and second_zero),'normalization_quotient_exact_kernel')
            normalization_cases+=1

    # Canonical local field of all short normal fractions proves actual global
    # lifts for pm and for every permitted positive-degree branch Laurent term.
    # In these tests all short t's are inverted ONLY to compare the restrictions;
    # the proof gives their global regularity via normalization, not scalar poles.
    common_open=(0,)
    check(not diff(full_lifts[0],common_open),'global_multiple_pm_lift')
    Laurent_count=0
    for active in (PLUS,MINUS):
        bare=lift(active)
        p=exp(ns=active)
        for occ in sorted(active):
            for power in range(4):
                # k=X_occ/t_occ^power, in I_sheet[1/tau_sheet].
                k=esub(exp(xs=(occ,)),tuple(power*x for x in exp(ns=(occ,))))
                v=times(bare,esub(k,p))
                check(not diff(v,common_open),'global_branch_Laurent_lift_closed')
                check(Q(v)==times(theta,k),'global_branch_Laurent_lift_projection')
                # Each displayed coefficient remains on this branch and has
                # no pole in the inactive normal parameters.
                for (c,a),n in v.items():
                    check(any(a[VAR[s]]>0 for s in active) and
                          all(a[9+VAR[s]]>=0 for s in set(SHORT)-set(active)),
                          'global_branch_Laurent_coefficient_gluing_domain')
                Laurent_count+=1
    result={
      'schema':'marici.true_obstruction_complement_descent.v1',
      'date':'2026-09-07','lane':'Branch B target/coefficient/descent',
      'source_commit':'d1947b67a60d3e88ba77f4ca60ea02c2a306ee61',
      'full_target_cells':len(CELLS),
      'cover_names':OPEN_NAMES,'cover_intersection_ranks':census,
      'local_unit_lifts':[{ 'open':OPEN_NAMES[i], 'chain_before_endpoint_quotient':encode(v)} for i,v in enumerate(locals_)],
      'endpoint_differences_before_quotient':endpoint_records,
      'residue_coordinates':records,
      'whole_open_ring_fine_degrees':fine_count,
      'whole_open_ring_cohomology_histogram':[{ 'cohomology':dict(k),'cases':n} for k,n in sorted(ring_hist.items())],
      'boundary_ideal_fine_degrees':ideal_count,
      'boundary_ideal_cohomology_histogram':[{ 'cohomology':dict(k),'cases':n} for k,n in sorted(ideal_hist.items())],
      'normalization_quotient_monomial_support_cases':normalization_cases,
      'explicit_branch_Laurent_lifts_checked':Laurent_count,
      'global_coefficient_ring':'C + I_plus[1/tau_plus] + I_minus[1/tau_minus]',
      'H1_of_boundary_ambiguity':'(C[1/(tau_plus*tau_minus)]/C[1/tau_plus])^6 + (C[1/(tau_plus*tau_minus)]/C[1/tau_minus])^6',
      'global_unit_lift_torsor':'locally nonempty on seven principal opens, no global section',
      'cyclic_descent_class':'C/(tau_plus*tau_minus)',
      'global_lift_image':'(tau_plus*tau_minus) C + I_plus[1/tau_plus] + I_minus[1/tau_minus]',
      'new_native_source_or_endpoint_connectors_constructed':False,
      'checks':dict(sorted(CHECKS.items())), 'exact_assertions':sum(CHECKS.values()),
      'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'proof_boundary':[
        'Finite sign/support calculations check matrices; arbitrary exponents follow from localization monomial bases and the displayed divisibility proof.',
        'Uses the previously proved full-target M and seven lifts; reconstructs their actual cells and checks local differentials anew.',
        'The open is D(a), not the physical generic deformation. Its coefficient inverses are sheaf-chart restrictions, not newly admitted physical poles.',
        'No theorem of native source identification, ringed physical Gysin realization, reflection parity or RH is asserted.'
      ]}
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('schema','full_target_cells','cover_intersection_ranks','whole_open_ring_fine_degrees','boundary_ideal_fine_degrees','cyclic_descent_class','global_unit_lift_torsor','exact_assertions')},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('marici_obstruction_complement_descent_certificate_20260907.json'))
    args=parser.parse_args()
    main(args.output)
