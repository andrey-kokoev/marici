#!/usr/bin/env python3
"""Compute the homogeneous Morse filling torsor and full boundary attachment.

Run with Python 3.10+: python morse_q_filling_torsor_and_attachment_checker.py
Standard library only; writes the specifically named certificate beside itself.
Reconstructs the full 2,338-state source and 786-state Q quotient first.
Then computes the ENTIRE multidegree-zero component, not a bounded polynomial
sample, using polynomial monomial weights and mixed-sheet relations.
All contractions of this component are integral. No claim is made that these
componentwise homotopies extend B-linearly to the whole graded source, or that
an independently constructed physical conductor homotopy has been transported.
"""
from __future__ import annotations
from collections import Counter
from itertools import combinations
from pathlib import Path
import hashlib
import json

DIAGONALS = ('02','03','04','13','14','15','24','25','35')
PLUS = frozenset(('13','15','35'))
MINUS = frozenset(('02','04','24'))
SHORT = tuple(sorted(PLUS | MINUS))
LONG = ('03','14','25')
VARIABLES = tuple('X'+d for d in DIAGONALS) + tuple('t'+d for d in SHORT) + tuple('u'+d for d in LONG)
INDEX = {v:i for i,v in enumerate(VARIABLES)}
ZERO_MONO = (0,)*len(VARIABLES)
ONE = {ZERO_MONO:1}
ZERO = {}
CHECKS = Counter()

def verify(condition: bool, label: str) -> None:
    CHECKS[label] += 1
    if not condition:
        raise AssertionError(label)

def survives(m: tuple[int,...]) -> bool:
    return not (any(m[INDEX['X'+d]] for d in PLUS) and any(m[INDEX['X'+d]] for d in MINUS))

def add(p: dict, q: dict, factor: int=1) -> dict:
    r = dict(p)
    for m,c in q.items():
        r[m] = r.get(m,0) + factor*c
        if r[m] == 0:
            del r[m]
    return r

def neg(p: dict) -> dict:
    return {m:-c for m,c in p.items()}

def mul(p: dict, q: dict) -> dict:
    r = {}
    for a,c in p.items():
        for b,d in q.items():
            m = tuple(x+y for x,y in zip(a,b))
            if survives(m):
                r[m] = r.get(m,0)+c*d
                if r[m] == 0:
                    del r[m]
    return r

def variable(name: str) -> dict:
    m = list(ZERO_MONO); m[INDEX[name]] = 1
    return {tuple(m):1}

def product(names) -> dict:
    p = ONE
    for name in names:
        p = mul(p, variable(name))
    return p

def epsilon(p: dict) -> dict:
    return {m:c for m,c in p.items() if not any(m[INDEX['X'+d]] for d in SHORT)}

def order(p: dict):
    if not p:
        return None
    return min(sum(m[INDEX['X'+d]] for d in SHORT) for m in p)

def normal(d: str) -> dict:
    return product(('t'+d,'X'+d)) if d in SHORT else variable('u'+d)

def pstr(p: dict) -> str:
    if not p:
        return '0'
    terms=[]
    for m,c in sorted(p.items()):
        factors=[v if power==1 else f'{v}^{power}' for v,power in zip(VARIABLES,m) if power]
        mon='*'.join(factors)
        text=(str(abs(c))+'*' if abs(c)!=1 and mon else str(abs(c)) if not mon else '')+mon
        terms.append(('-' if c<0 else '+')+text)
    ans=''.join(terms)
    return ans[1:] if ans.startswith('+') else ans

def vadd(out: dict, key, p: dict, scale: int=1) -> None:
    if not p:
        return
    out[key]=add(out.get(key,{}),p,scale)
    if not out[key]:
        del out[key]

def combine(a: dict, b: dict, scale: int=1) -> dict:
    r=dict(a)
    for key,p in b.items():
        vadd(r,key,p,scale)
    return r

def vmul(v: dict, p: dict) -> dict:
    out={}
    for key,q in v.items():
        vadd(out,key,mul(p,q))
    return out

def apply(columns: dict, vector: dict) -> dict:
    out={}
    for key,c in vector.items():
        for target,p in columns.get(key,{}).items():
            vadd(out,target,mul(c,p))
    return out

def cross(d: str, e: str) -> bool:
    a,b=map(int,d); c,f=map(int,e)
    if len({a,b,c,f}) < 4:
        return False
    def inside(x,y,z):return 0<(x-y)%6<(z-y)%6
    return (inside(c,a,b)!=inside(f,a,b)) and (inside(a,c,f)!=inside(b,c,f))

def powerset(values):
    vals=tuple(sorted(values))
    for n in range(len(vals)+1):
        yield from combinations(vals,n)

old_faces={frozenset(c) for n in range(4) for c in combinations(DIAGONALS,n)
           if all(not cross(d,e) for d,e in combinations(c,2))}
new_faces=set()
for face in old_faces:
    if not {'03','13'} <= face:
        new_faces.add(face)
    else:
        for retained in (set(),{'03'},{'13'}):
            new_faces.add(frozenset((set(face)-{'03','13'}) | {'E'} | retained))
FACES=tuple(sorted(new_faces,key=lambda f:(len(f),tuple(sorted(f)))))

def oldof(face):
    return (face-{'E'}) | (frozenset(('03','13')) if 'E' in face else frozenset())

FLAGS=[]
def extend(flag):
    FLAGS.append(tuple(flag))
    for face in FACES:
        if flag[-1] < face:
            extend(flag+[face])
for face in FACES:
    extend([face])

# A generator consists of (strict flag, old normal-circle subset, occurrence-Koszul bit).
BASE=tuple((flag,H) for flag in FLAGS for H in powerset(oldof(flag[0])))
GENS=tuple((flag,H,k) for flag,H in BASE for k in (0,1))
GSET=set(GENS)

def degree(g):return len(g[0])-1+len(g[1])+g[2]

def source_column(g):
    flag,H,k=g
    base_dim=len(flag)-1
    out={}
    if len(flag)>1:
        for i in range(len(flag)):
            target=(flag[:i]+flag[i+1:],H,k)
            coefficient=ONE
            if i==0:
                coefficient=product('X'+d for d in oldof(flag[1])-oldof(flag[0]))
            vadd(out,target,coefficient,(-1)**i)
    for i,d in enumerate(H):
        vadd(out,(flag,H[:i]+H[i+1:],k),normal(d),(-1)**(base_dim+i))
    if k:
        vadd(out,(flag,H,0),variable('X35'),(-1)**(base_dim+len(H)))
    return out

DS={g:source_column(g) for g in GENS}
for g,col in DS.items():
    verify(all(h in GSET and degree(h)==degree(g)-1 for h in col),'source_degree_and_closure')
    verify(apply(DS,col)=={},'full_source_d_squared')


# Marked Morse chains, with the original loaded signs and independent occurrence factor.
top=frozenset(); qd=frozenset(('03',)); a=PLUS
c=frozenset(('03','02','35'))
ec=frozenset(('13','35')); he=frozenset(('E','35'))
b1=frozenset(('E','13','35')); bd=frozenset(('E','03','35'))
er=frozenset(('03','35'))
def term(flag,coefficient=None,sign=1):
    if coefficient is None:coefficient=ONE
    return {(tuple(flag),(),0):{m:sign*n for m,n in coefficient.items()}}
HM={}
for apex,edge,left,right,coef in ((top,ec,a,b1,ONE),(top,he,b1,bd,ONE),(qd,er,bd,c,variable('X03'))):
    HM=combine(HM,term((apex,edge,right),coef,-1))
    HM=combine(HM,term((apex,edge,left),coef,1))
HM=combine(HM,term((top,qd,bd)))
XI={}
for edge,left,right,coef in ((ec,a,b1,variable('X13')),(he,b1,bd,product(('X03','X13'))),(er,bd,c,variable('X03'))):
    XI=combine(XI,term((edge,right),coef))
    XI=combine(XI,term((edge,left),coef,-1))
QRAW=combine(combine(term((top,a),sign=-1),term((top,qd))),term((qd,c),variable('X03')))
DXI=apply(DS,XI)
def occurrence_partner(v):return {(flag,marks,1):coef for (flag,marks,bit),coef in v.items()}
HHAT=combine(HM,occurrence_partner(XI),-1)
QHAT=combine(QRAW,occurrence_partner(DXI),-1)
verify(apply(DS,HM)==combine(QRAW,vmul(XI,variable('X35')),-1),'loaded_Morse_identity')
verify(apply(DS,HHAT)==QHAT,'corrected_Morse_identity')
verify(apply(DS,QHAT)=={},'corrected_Morse_boundary_closed')

# Actual support: a barycentric simplex lies entirely on the short boundary
# precisely when its initial (largest geometric) face lies there.
def boundary_supported(g):return bool(set(oldof(g[0][0])) & set(SHORT))
def endpoint_supported(g):return g[0] in ((PLUS,),(MINUS,))
BOUNDARY={g for g in GENS if boundary_supported(g)}
ENDPOINT={g for g in GENS if endpoint_supported(g)}
for support in (BOUNDARY,ENDPOINT):
    for g in support:verify(set(DS[g])<=support,'complete_support_subcomplex')
verify((len(ENDPOINT),len(BOUNDARY),len(GENS))==(32,1552,2338),'corrected_support_state_counts')
SID={g:i for i,g in enumerate(GENS)}
END0=(((PLUS,),(),0),((MINUS,),(),0))
CONE=(len(GENS),len(GENS)+1)
END0_IDS=tuple(SID[g] for g in END0)
DOLD={SID[g]:{SID[h]:p for h,p in col.items()} for g,col in DS.items()}
DREL={i:dict(col) for i,col in DOLD.items()}
for endpoint,cone in zip(END0_IDS,CONE):
    DREL[endpoint][cone]=ONE
    DREL[cone]={}

def degree_rel(i):return -1 if i in CONE else degree(GENS[i])
def rel_apply(columns,vector):
    result={}
    for i,p in vector.items():
        for j,q in columns.get(i,{}).items():
            pq=mul(p,q)
            if j in CONE:pq=epsilon(pq)
            vadd(result,j,pq)
    return result

def rel_project(v):return {GENS[i]:p for i,p in v.items() if i not in CONE}
def conductor_extract(v):
    out={}
    for side,i in enumerate(END0_IDS):
        p=epsilon(v.get(i,{}))
        if p:out[side]=p
    return out

def universal_homotopy(v):
    return {side:epsilon(v[i]) for side,i in enumerate(CONE) if i in v and epsilon(v[i])}
for i,col in DREL.items():
    verify(rel_apply(DREL,col)=={},'full_relative_d_squared')
    verify(all(degree_rel(j)==degree_rel(i)-1 for j in col),'full_relative_homological_degree')
    verify(rel_project(col)==apply(DS,rel_project({i:ONE})),'relative_projection_chain_equation')
    verify(universal_homotopy(col)==conductor_extract({i:ONE}),'universal_endpoint_nullhomotopy')
    for p in col.values():verify(all(min(m)>=0 for m in p),'no_inverted_parameters')

RELBOUNDARY={SID[g] for g in BOUNDARY}|set(CONE)
RELENDPOINT={SID[g] for g in ENDPOINT}|set(CONE)
for supp in (RELBOUNDARY,RELENDPOINT):
    for i in supp:verify(set(DREL[i])<=supp,'relative_support_subcomplex')
verify((len(RELENDPOINT),len(RELBOUNDARY),len(DREL))==(34,1554,2340),'relative_support_state_counts')
RH={SID[g]:p for g,p in HHAT.items()}; RQ={SID[g]:p for g,p in QHAT.items()}
verify(rel_apply(DREL,RH)==RQ,'corrected_disk_lifts_to_full_relative_source')
verify(rel_apply(DREL,RQ)=={},'relative_corrected_generic_closed')
for side in (0,1):
    verify(conductor_extract({END0_IDS[side]:ONE})=={side:ONE},'endpoint_augmentation_detects_cycle')
    verify(DOLD[END0_IDS[side]]=={},'endpoint_unit_closed_before_relativizing')
# Thus an identity-over-M lift M -> fib(e) is impossible, since e is nonzero on H0.

# Endpoint-derived maps into the previous scalar fibre. Their pullbacks to this
# new relative source have an explicit primitive, including the source conductor terms.
J_D1=(1,-1,-1,-1,-1)
Z=(1,0,1,0,0)
READOUT=(0,0,1,1,1)
def scalar_fibre_boundary(vector):
    out={}
    for (side,n,j),p in vector.items():
        if n==1:
            vadd(out,(side,0,0),p,J_D1[j])
            vadd(out,(side,0,1),epsilon(p),READOUT[j])
    return out

def scalar_fibre_apply(columns,vector):
    out={}
    for i,p in vector.items():
        for (side,n,j),q in columns.get(i,{}).items():
            pq=mul(p,q)
            if n==0 and j==1:pq=epsilon(pq)
            vadd(out,(side,n,j),pq)
    return out
MEND={i:{} for i in DREL}
PRIM={i:{} for i in DREL}
for i in DOLD:
    for side,endpoint in enumerate(END0_IDS):
        coeff=neg(DOLD[i].get(endpoint,{}))
        for j,zcoef in enumerate(Z):
            if zcoef:vadd(MEND[i],(side,1,j),coeff,zcoef)
for side,endpoint in enumerate(END0_IDS):
    PRIM[endpoint]={(side,1,j):neg(ONE) for j,zcoef in enumerate(Z) if zcoef}
    PRIM[CONE[side]]={(side,0,1):ONE}
for i in DREL:
    verify(scalar_fibre_boundary(MEND[i])==scalar_fibre_apply(MEND,DREL[i]),'pulled_endpoint_comparison_chain_equation')
    lhs=combine(scalar_fibre_boundary(PRIM[i]),scalar_fibre_apply(PRIM,DREL[i]))
    verify(lhs==MEND[i],'explicit_relative_endpoint_comparison_primitive')

# Full Q quotient before tensoring the extra occurrence factor.
QGENS=tuple(g for g in GENS if g[2]==0 and not boundary_supported(g))
QID={g:i for i,g in enumerate(QGENS)}
DQ={QID[g]:{QID[h]:p for h,p in DS[g].items() if h in QID} for g in QGENS}
verify(len(QGENS)==393,'full_Q_base_count')
verify(dict(Counter(degree(g) for g in QGENS))=={0:4,1:77,2:192,3:120},'full_Q_base_ranks')
for i,col in DQ.items():verify(apply(DQ,col)=={},'full_Q_base_d_squared')

def qproject(v):return {QID[g]:p for g,p in v.items() if g in QID}
for g in GENS:
    if g[2]==0:
        before={QID[g]:ONE} if g in QID else {}
        verify(qproject(DS[g])==apply(DQ,before),'Q_is_actual_chain_quotient')
QB_H=qproject(HM); QB_Q=qproject(QRAW)
verify(qproject(XI)=={},'special_gallery_vanishes_in_Q')
verify(apply(DQ,QB_H)==QB_Q,'Q_Morse_nullhomotopy_with_all_mixed_flags')
verify(len(QB_Q)==3 and len(QB_H)==7,'Q_Morse_retained_terms')

# Reject dropping mixed flags: this is a subcomplex projection which is NOT a chain map.
PURE={i for i,g in enumerate(QGENS) if not(set(oldof(g[0][-1]))&set(SHORT))}
def pure_project(v):return {i:p for i,p in v.items() if i in PURE}
triangle=((top,qd,c),(),0)
tri_id=QID[triangle]; edge_id=QID[((top,qd),(),0)]
verify(tri_id not in PURE,'mixed_triangle_would_be_deleted')
verify(pure_project(DQ[tri_id])=={edge_id:ONE},'unit_chain_defect_of_pure_flag_projection')
verify(pure_project({tri_id:ONE})=={},'mixed_triangle_projection_zero')

# Exact Gaussian chain cancellation, only on coefficient +1 or -1 arrows
# with identical initial face and normal subset.
def unit_sign(poly):
    if poly==ONE:return 1
    if poly==neg(ONE):return -1
    return 0
DWORK={i:dict(col) for i,col in DQ.items()}
PROJ={i:{i:ONE} for i in DQ}
INCL={i:{i:ONE} for i in DQ}
HOM={i:{} for i in DQ}
ACTIVE=set(DQ); CANCELLATIONS=[]
while True:
    pair=None
    for high in sorted(ACTIVE,key=lambda i:(len(QGENS[i][0][0]),-degree(QGENS[i]),i)):
        for low,p in sorted(DWORK[high].items()):
            sign=unit_sign(p)
            if sign and QGENS[low][0][0]==QGENS[high][0][0] and QGENS[low][1]==QGENS[high][1]:
                pair=(low,high,sign);break
        if pair is not None:break
    if pair is None:break
    low,high,sign=pair
    inclusion_high=INCL[high]
    for j,pj in PROJ.items():
        coeff=pj.get(low)
        if coeff:HOM[j]=combine(HOM[j],vmul(inclusion_high,coeff),sign)
    rest={i:p for i,p in DWORK[high].items() if i!=low}
    for j,pj in list(PROJ.items()):
        coeff=pj.get(low)
        nxt={i:p for i,p in pj.items() if i not in (low,high)}
        if coeff:nxt=combine(nxt,vmul(rest,coeff),-sign)
        PROJ[j]=nxt
    for j in ACTIVE-{low,high}:
        coeff=DWORK[j].get(low)
        if coeff:INCL[j]=combine(INCL[j],vmul(inclusion_high,coeff),-sign)
    for j in ACTIVE-{low,high}:
        coeff=DWORK[j].get(low)
        nxt={i:p for i,p in DWORK[j].items() if i not in (low,high)}
        if coeff:nxt=combine(nxt,vmul(rest,coeff),-sign)
        DWORK[j]=nxt
    for j in (low,high):del DWORK[j];del INCL[j]
    ACTIVE-={low,high}
    CANCELLATIONS.append(pair)
verify(len(CANCELLATIONS)==193 and len(ACTIVE)==7,'integral_Q_cancellation_count')

# Normalize the retained top orientation to the original cellular convention.
CELLNAMES=('T','p03','h03','p14','h14','p25','h25')
SURV={}; CSIGN={}
for i in ACTIVE:
    initial=QGENS[i][0][0]
    if not initial:name='T';sign=-1
    else:
        d=next(iter(initial));name=('h' if QGENS[i][1] else 'p')+d;sign=1
    SURV[name]=i;CSIGN[i]=sign
verify(set(SURV)==set(CELLNAMES),'cellular_Q_labels_complete')
CELLID={name:i for i,name in enumerate(CELLNAMES)}
RTOC={SURV[name]:CELLID[name] for name in CELLNAMES}
P={i:{RTOC[j]:p if CSIGN[j]==1 else neg(p) for j,p in col.items()} for i,col in PROJ.items()}
INC={CELLID[name]:vmul(INCL[SURV[name]],ONE if CSIGN[SURV[name]]==1 else neg(ONE)) for name in CELLNAMES}
DC={i:{} for i in range(7)}
for d in LONG:
    DC[0][CELLID['p'+d]]=variable('X'+d)
    DC[CELLID['h'+d]][CELLID['p'+d]]=variable('u'+d)
CDEG={i:3 if name=='T' or name.startswith('h') else 2 for i,name in enumerate(CELLNAMES)}
for i in DQ:
    verify(apply(P,DQ[i])==apply(DC,P[i]),'Q_retraction_projection_chain_equation')
    lhs=combine(apply(DQ,HOM[i]),apply(HOM,DQ[i]))
    rhs=combine({i:ONE},apply(INC,P[i]),-1)
    verify(lhs==rhs,'Q_retraction_full_homotopy_identity')
for i in DC:
    verify(apply(P,INC[i])=={i:ONE},'Q_retraction_split_identity')
    verify(apply(DQ,INC[i])==apply(INC,DC[i]),'Q_retraction_inclusion_chain_equation')

def source_weight(g):
    weights=[0]*len(VARIABLES)
    for d in oldof(g[0][0]):weights[INDEX['X'+d]]-=1
    for d in g[1]:
        mon=next(iter(normal(d)))
        weights=[a+b for a,b in zip(weights,mon)]
    if g[2]:weights[INDEX['X35']]+=1
    return tuple(weights)
CW={i:source_weight(QGENS[SURV[name]]) for i,name in enumerate(CELLNAMES)}
for i,col in P.items():
    for j,p in col.items():
        verify(degree(QGENS[i])==CDEG[j],'Q_projection_degree_preserved')
        for mon in p:verify(source_weight(QGENS[i])==tuple(a+b for a,b in zip(mon,CW[j])),'Q_projection_full_multigrading')
for i,col in HOM.items():
    for j,p in col.items():
        verify(degree(QGENS[j])==degree(QGENS[i])+1,'Q_homotopy_degree')
        for mon in p:verify(source_weight(QGENS[i])==tuple(a+b for a,b in zip(mon,source_weight(QGENS[j]))),'Q_homotopy_full_multigrading')

# The nonzero cellular top cycle; its existence is unrelated to the degree-one raw roof.
THETA={0:product('u'+d for d in LONG)}
for d in LONG:THETA[CELLID['h'+d]]=neg(product(['X'+d]+['u'+e for e in LONG if e!=d]))
verify(apply(DC,THETA)=={},'cellular_Q_top_cycle_closed')
verify(bool(apply(INC,THETA)),'cellular_Q_top_cycle_nonzero')
verify(all(CDEG[i]==3 for i in THETA),'cellular_Q_top_cycle_degree_three')

# Tensor the COMPLETE contraction with K_occ(X35). This retains every correction.
QTGEN=tuple((i,k) for i in DQ for k in (0,1))
CTGEN=tuple((i,k) for i in DC for k in (0,1))
DQT={};DCT={}
for columns,degrees,gens,out in ((DQ,{i:degree(QGENS[i]) for i in DQ},QTGEN,DQT),(DC,CDEG,CTGEN,DCT)):
    for i,k in gens:
        col={(j,k):p for j,p in columns[i].items()}
        if k:vadd(col,(i,0),variable('X35'),(-1)**degrees[i])
        out[(i,k)]=col
PT={(i,k):{(j,k):p for j,p in P[i].items()} for i,k in QTGEN}
IT={(i,k):{(j,k):p for j,p in INC[i].items()} for i,k in CTGEN}
HT={(i,k):{(j,k):p for j,p in HOM[i].items()} for i,k in QTGEN}
for g in QTGEN:
    verify(apply(DQT,DQT[g])=={},'corrected_Q_d_squared')
    verify(apply(PT,DQT[g])==apply(DCT,PT[g]),'corrected_Q_projection_chain_equation')
    lhs=combine(apply(DQT,HT[g]),apply(HT,DQT[g]))
    verify(lhs==combine({g:ONE},apply(IT,PT[g]),-1),'corrected_Q_tensor_homotopy_identity')
for g in CTGEN:
    verify(apply(PT,IT[g])=={g:ONE},'corrected_Q_split_identity')
    verify(apply(DQT,IT[g])==apply(IT,DCT[g]),'corrected_Q_inclusion_chain_equation')
verify(len(QTGEN)==786 and len(CTGEN)==14,'corrected_Q_contraction_state_counts')

def qhat_project(v):
    out={}
    for (flag,H,k),coef in v.items():
        base=(flag,H,0)
        if base in QID:vadd(out,(QID[base],k),coef)
    return out
Q_HHAT=qhat_project(HHAT);Q_QHAT=qhat_project(QHAT)
verify(apply(DQT,Q_HHAT)==Q_QHAT,'corrected_Morse_in_full_Q')
verify(apply(PT,Q_HHAT)=={},'cellular_projection_of_Morse_homotopy')
verify(apply(PT,Q_QHAT)=={},'cellular_projection_of_corrected_roof')
CANON_H=apply(HT,Q_QHAT)
SECOND_H=apply(HT,Q_HHAT)
verify(apply(DQT,CANON_H)==Q_QHAT,'cellular_contraction_supplies_roof_primitive')
verify(apply(DQT,SECOND_H)==combine(Q_HHAT,CANON_H,-1),'explicit_homotopy_between_roof_primitives')


# ---------------------------------------------------------------------------
# New computation: all fillings in the actual Morse multidegree and their
# short-boundary attachments. All 18 coefficient weights remain distinct.
# ---------------------------------------------------------------------------
REPLAY_CHECKS=dict(CHECKS)
REPLAY_TOTAL=sum(CHECKS.values())

def izadd(left, right, scale=1):
    out=dict(left)
    for k,c in right.items():
        out[k]=out.get(k,0)+scale*c
        if out[k]==0:del out[k]
    return out

def izapply(columns,vector):
    out={}
    for j,c in vector.items():out=izadd(out,columns.get(j,{}),c)
    return out

SLICE_MONOMIAL={}
for g in GENS:
    mono=tuple(-v for v in source_weight(g))
    if min(mono)>=0 and survives(mono):SLICE_MONOMIAL[g]=mono
SLICE_IDS=tuple(SID[g] for g in GENS if g in SLICE_MONOMIAL)
SLICE_BY_ID={SID[g]:mono for g,mono in SLICE_MONOMIAL.items()}
SLICE_DEG={SID[g]:degree(g) for g in SLICE_MONOMIAL}

def slice_coordinates(vector):
    out={}
    for g,p in vector.items():
        verify(g in SLICE_MONOMIAL,'exact_multidegree_zero_membership')
        mono=SLICE_MONOMIAL[g]
        verify(len(p)==1 and mono in p,'unique_legal_coefficient_monomial')
        out[SID[g]]=p[mono]
    return out

def slice_as_polynomial(vector):
    return {GENS[i]:{SLICE_BY_ID[i]:c} for i,c in vector.items()}

D_SLICE={SID[g]:slice_coordinates(vmul(DS[g],{mono:1}))
         for g,mono in SLICE_MONOMIAL.items()}
for i,col in D_SLICE.items():
    verify(izapply(D_SLICE,col)=={},'full_zero_weight_d_squared')
verify(len(SLICE_IDS)==611,'full_zero_weight_state_count')
verify(all(not GENS[i][1] for i in SLICE_IDS),'normal_marks_excluded_by_weights_not_truncation')
for v in (HHAT,QHAT):
    coords=slice_coordinates(v)
    verify(slice_as_polynomial(coords)==v,'complete_Morse_chains_in_zero_weight_component')

# The two added conductor terms have endpoint weights. Their complementary
# monomials require short X coordinates, unavailable in C=B/I. They therefore
# have zero multidegree-zero component. This is not ordinary base change.
for endpoint in (PLUS,MINUS):
    required=product('X'+d for d in endpoint)
    verify(bool(required) and epsilon(required)=={},'conductor_fibre_additions_absent_in_zero_weight')
for i,col in D_SLICE.items():
    pp={i:{SLICE_BY_ID[i]:1}}
    relimage=rel_apply(DREL,pp)
    verify(not(set(relimage)&set(CONE)),'relative_fibre_differential_same_in_zero_weight')

SLICE_SUPPORTS={
 'M':set(SLICE_IDS),
 'B':{i for i in SLICE_IDS if boundary_supported(GENS[i])},
 'V':{i for i in SLICE_IDS if endpoint_supported(GENS[i])},
 'Q':{i for i in SLICE_IDS if not boundary_supported(GENS[i])}}
SLICE_DIFFERENTIALS={name:{i:{j:c for j,c in D_SLICE[i].items() if j in ids} for i in sorted(ids)}
                     for name,ids in SLICE_SUPPORTS.items()}
for name,cols in SLICE_DIFFERENTIALS.items():
    for i,col in cols.items():verify(izapply(cols,col)=={},'support_slice_d_squared')
for i in SLICE_IDS:
    expected={j:c for j,c in D_SLICE[i].items() if j in SLICE_SUPPORTS['Q']}
    actual=SLICE_DIFFERENTIALS['Q'].get(i,{})
    verify(actual==expected,'zero_weight_support_sequence_exact_on_differentials')


def integral_retract(original):
    """Cancel only signed unit differential entries, tracking every map."""
    d={i:dict(col) for i,col in original.items()}
    p={i:{i:1} for i in original}; inc={i:{i:1} for i in original}
    hom={i:{} for i in original}; active=set(original); log=[]
    key=lambda i:(-SLICE_DEG[i],i)
    while True:
        pivot=None
        for hi in sorted(active,key=key):
            for lo,c in sorted(d[hi].items(),key=lambda kv:key(kv[0])):
                if abs(c)==1:pivot=(lo,hi,c);break
            if pivot is not None:break
        if pivot is None:break
        lo,hi,sign=pivot
        rest={i:c for i,c in d[hi].items() if i!=lo}
        ih=inc[hi]
        for j,pj in list(p.items()):
            coeff=pj.get(lo,0)
            if coeff:hom[j]=izadd(hom[j],ih,sign*coeff)
            p[j]=izadd({i:c for i,c in pj.items() if i not in (lo,hi)},rest,-sign*coeff)
        for j in sorted(active-{lo,hi}):
            coeff=d[j].get(lo,0)
            if coeff:inc[j]=izadd(inc[j],ih,-sign*coeff)
            d[j]=izadd({i:c for i,c in d[j].items() if i not in (lo,hi)},rest,-sign*coeff)
        for j in (lo,hi):del d[j];del inc[j]
        active-={lo,hi};log.append(pivot)
    for i,col in original.items():
        verify(izapply(p,col)==izapply(d,p[i]),'integral_retract_projection_chain_equation')
        lhs=izadd(izapply(original,hom[i]),izapply(hom,col))
        rhs=izadd({i:1},izapply(inc,p[i]),-1)
        verify(lhs==rhs,'integral_retract_full_homotopy_equation')
        verify(all(SLICE_DEG[j]==SLICE_DEG[i]+1 for j in hom[i]),'integral_retract_homotopy_degree')
    for i in d:
        verify(izapply(p,inc[i])=={i:1},'integral_retract_split_identity')
        verify(izapply(original,inc[i])==izapply(inc,d[i]),'integral_retract_inclusion_chain_equation')
    return {'d':d,'p':p,'i':inc,'h':hom,'cancellations':log}

RETRACTS={name:integral_retract(cols) for name,cols in SLICE_DIFFERENTIALS.items()}
EXPECTED_RESIDUAL={'M':{1:3},'B':{1:5},'V':{0:1},'Q':{2:2}}
EXPECTED_PAIRS={'M':304,'B':132,'V':1,'Q':170}
for name,ret in RETRACTS.items():
    verify(all(not col for col in ret['d'].values()),'all_residual_slice_differentials_zero')
    verify(dict(Counter(SLICE_DEG[i] for i in ret['d']))==EXPECTED_RESIDUAL[name],
           'exact_integral_slice_homology')
    verify(len(ret['cancellations'])==EXPECTED_PAIRS[name],'integral_slice_cancellation_count')

# Polynomial presentation for the full, unlocalized Q-filling torsor.
LOWER=[(CELLID['p'+d],0) for d in LONG]
UPPER=[(CELLID['T'],0)]+[(CELLID['h'+d],0) for d in LONG]+[(CELLID['p'+d],1) for d in LONG]
Q_PRESENTATION=[[DCT[j].get(i,{}) for j in UPPER] for i in LOWER]
for i,d in enumerate(LONG):
    expected=[variable('X'+d)]+[variable('u'+d) if k==i else {} for k in range(3)]+[variable('X35') if k==i else {} for k in range(3)]
    verify(Q_PRESENTATION[i]==expected,'full_polynomial_H2_filling_presentation')

# Construct three explicit degree-two variations using the full Q inclusion.
# These are legitimate new fillings of the same Q-roof.
Q_VARIATIONS={};B_ATTACHMENTS={};ATTACH_COORDS={}
B_H1=sorted(RETRACTS['B']['d']);M_H1=sorted(RETRACTS['M']['d'])
for d in LONG:
    v=apply(INC,{CELLID['p'+d]:variable('X'+d)})
    lift={QGENS[i]:poly for i,poly in v.items()}
    lift0=slice_coordinates(lift)
    verify(all(i in SLICE_SUPPORTS['Q'] for i in lift0),'variation_Q_support')
    verify(izapply(SLICE_DIFFERENTIALS['Q'],lift0)=={},'variation_closed_in_full_Q')
    verify(apply(P,v)=={CELLID['p'+d]:variable('X'+d)},'variation_normalization_not_fitted')
    beta=izapply(D_SLICE,lift0)
    verify(set(beta)<=SLICE_SUPPORTS['B'],'variation_boundary_on_actual_short_support')
    verify(izapply(SLICE_DIFFERENTIALS['B'],beta)=={},'actual_attachment_cycle_closed')
    projection=izapply(RETRACTS['B']['p'],beta)
    Q_VARIATIONS[d]=lift0;B_ATTACHMENTS[d]=beta
    ATTACH_COORDS[d]=[projection.get(i,0) for i in B_H1]
    verify(len(lift0)==8 and len(beta)==8,'full_labeled_variation_and_attachment_term_counts')
    # They have no endpoint-state component, but their boundary attachment is
    # generally nonzero. Endpoint signatures alone cannot determine a filling.
    verify(not(set(lift0)&SLICE_SUPPORTS['V']),'variation_has_zero_endpoint_components')

ATTACH_MATRIX=[[ATTACH_COORDS[d][i] for d in LONG] for i in range(5)]
verify(ATTACH_MATRIX==[[-1,1,0],[1,0,-1],[1,0,-1],[-1,1,0],[0,-1,1]],
       'computed_integral_short_boundary_attachment_matrix')

# Carry the old top relation into the short boundary. This retains its full
# seventy-two-term B-chain instead of discarding lower corrections.
qt=apply(INC,{CELLID['T']:ONE})
full_top=slice_coordinates({QGENS[i]:poly for i,poly in qt.items()})
D_TOP=izapply(D_SLICE,full_top)
TOTAL_VARIATION={};TOTAL_ATTACHMENT={}
for d in LONG:
    TOTAL_VARIATION=izadd(TOTAL_VARIATION,Q_VARIATIONS[d])
    TOTAL_ATTACHMENT=izadd(TOTAL_ATTACHMENT,B_ATTACHMENTS[d])
SHORT_TOP=izadd(D_TOP,TOTAL_VARIATION,-1)
verify(set(SHORT_TOP)<=SLICE_SUPPORTS['B'],'top_relation_short_boundary_support')
verify(izapply(D_SLICE,SHORT_TOP)=={i:-c for i,c in TOTAL_ATTACHMENT.items()},
       'complete_chain_homotopy_for_diagonal_attachment_relation')
verify(len(SHORT_TOP)==72,'top_relation_retains_all_lower_terms')

# Inclusion on H1(B)->H1(M); all bases are integral, not rational row spaces.
INCLUSION_H1=[]
for j in B_H1:
    v=izapply(RETRACTS['M']['p'],RETRACTS['B']['i'][j])
    INCLUSION_H1.append([v.get(i,0) for i in M_H1])
INCLUSION_H1=[list(row) for row in zip(*INCLUSION_H1)]
verify(INCLUSION_H1==[[0,-1,1,0,0],[-1,0,0,1,0],[1,1,0,0,1]],'support_inclusion_H1_matrix')

def matrix_product(a,b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]

def det_int(a):
    """Small exact Laplace determinant, no division."""
    if not a:return 1
    if len(a)==1:return a[0][0]
    return sum((-1)**j*a[0][j]*det_int([[row[k] for k in range(len(a)) if k!=j] for row in a[1:]]) for j in range(len(a)))

U=[[ATTACH_COORDS['03'][i],ATTACH_COORDS['14'][i]]+[int(i==j) for j in range(2,5)] for i in range(5)]
verify(det_int(U)==-1,'adapted_boundary_basis_is_unimodular')
DELTA_ADAPTED=[[1,0,-1],[0,1,-1],[0,0,0],[0,0,0],[0,0,0]]
verify(matrix_product(U,DELTA_ADAPTED)==ATTACH_MATRIX,'attachment_in_adapted_basis')
verify(matrix_product(INCLUSION_H1,U)==[[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]],'exact_sequence_split_in_adapted_basis')
verify(matrix_product(INCLUSION_H1,ATTACH_MATRIX)==[[0,0,0] for _ in range(3)],'connecting_then_inclusion_is_zero')
verify(det_int([[ATTACH_MATRIX[i][j] for j in (0,1)] for i in (0,1)])==-1,'attachment_has_unit_rank_two_minor')

# The full homogeneous filling space has no ambiguity in homotopy. This
# constructs a universal primitive for any degree-two cycle in this component.
FULL_HOMOTOPY=RETRACTS['M']['h']
for i in SLICE_IDS:
    if SLICE_DEG[i]==2:
        verify(RETRACTS['M']['p'][i]=={},'full_degree_two_homology_projection_zero')
        lhs=izadd(izapply(D_SLICE,FULL_HOMOTOPY[i]),izapply(FULL_HOMOTOPY,D_SLICE[i]))
        verify(lhs=={i:1},'universal_homogeneous_filling_difference_contraction')
QM0=slice_coordinates(QHAT);HM0=slice_coordinates(HHAT)
verify(izapply(D_SLICE,HM0)==QM0,'entire_corrected_Morse_disk_in_component')
CANON_FULL_H=izapply(FULL_HOMOTOPY,QM0)
verify(CANON_FULL_H==HM0,'full_component_contraction_recovers_corrected_Morse_primitive')

# A compact exact readout for the two free Q-filling coordinates.
# P has degrees, so degree-two zero-weight cochains project only to X_d p_d.
QZERO_PROJECTION={}
for i in sorted(SLICE_SUPPORTS['Q']):
    g=GENS[i];flag,marks,k=g
    bi=QID[(flag,marks,0)]
    pv=apply(PT,{(bi,k):{SLICE_BY_ID[i]:1}})
    out={}
    for (j,bit),poly in pv.items():
        if SLICE_DEG[i]!=2:continue
        name=CELLNAMES[j]
        verify(bit==0 and name in ('p03','p14','p25'),'all_degree_two_projection_coordinates_classified')
        d=name[1:];mono=next(iter(variable('X'+d)))
        verify(len(poly)==1 and mono in poly,'no_inverse_in_road_coefficient_readout')
        out[d]=poly[mono]
    if SLICE_DEG[i]==2:QZERO_PROJECTION[i]=out

def q_filling_class(v):
    p=izapply(QZERO_PROJECTION,v)
    return (p.get('03',0)-p.get('25',0),p.get('14',0)-p.get('25',0))
for i,col in SLICE_DIFFERENTIALS['Q'].items():
    if SLICE_DEG[i]==3:verify(q_filling_class(col)==(0,0),'two_integer_readout_annihilates_all_Q_homotopies')
for d,expected in zip(LONG,((1,0),(0,1),(-1,-1))):
    verify(q_filling_class(Q_VARIATIONS[d])==expected,'two_integer_readout_detects_variation_generators')
verify(q_filling_class({i:c for i,c in HM0.items() if i in SLICE_SUPPORTS['Q']})==(0,0),
       'chosen_Morse_filling_has_zero_affine_coordinates')

# Data exports contain actual sparse maps, not signature assertions.
def state_label(g):
    return {'flag':[sorted(face) for face in g[0]],'marks':list(g[1]),'occurrence_bit':g[2],'degree':degree(g)}

def serialize_int_matrix(cols):
    return [[i,j,c] for i in sorted(cols) for j,c in sorted(cols[i].items())]

def serialize_int_vector(vec):return [[i,c] for i,c in sorted(vec.items())]

def serialize_poly_vector(v):
    return [{'source_state_id':i,'state':state_label(GENS[i]),'coefficient':pstr({SLICE_BY_ID[i]:c})}
            for i,c in sorted(v.items())]

NEW_COUNTS={k:v-REPLAY_CHECKS.get(k,0) for k,v in CHECKS.items() if v>REPLAY_CHECKS.get(k,0)}
new_checks=sum(NEW_COUNTS.values())
payload={
 'schema':'marici.morse_q_filling_torsor_and_attachment.v1',
 'provenance':{'repository':'andrey-kokoev/marici','commit':'d1947b67a60d3e88ba77f4ca60ea02c2a306ee61',
   'source_file':'research/voevodsky/check_d03_pabs_morse_pullback.rs','source_blob':'46624341c7956a8557249a54b117a88d43adfd62',
   'prior_reconstruction':'full_q_support_relative_morse_checker.py'},
 'scope':{'coefficient_ring':'B=C[Xshort]/(Xeven*Xodd), polynomial, short u_d=t_d X_d; long normals independent',
   'inverted_parameters':[], 'all_18_weights_retained':True,
   'computed_filling_domain':'one fixed homogeneous degree-one chain / free probe, with fixed full differential',
   'physical_Hcond_constructed':False,'physical_DeltaJ_identified':False,
   'no_claim_of_B_linear_extension_of_component_contractions':True,
   'no_claim_that_every_component_homotopy_preserves_unprovided_physical_frames':True},
 'full_Q_filling_torsor':{'module':'B^3 / (B*(X03,X14,X25) + u03 B e03 + u14 B e14 + u25 B e25 + X35 B^3)',
   'presentation':[[pstr(p) for p in row] for row in Q_PRESENTATION],
   'column_labels':['T','h03','h14','h25','p03_hocc','p14_hocc','p25_hocc']},
 'homogeneous_component':{'multidegree':[0]*len(VARIABLES),'variables':VARIABLES,
   'source_state_count':len(GENS),'component_state_counts':{n:len(ids) for n,ids in SLICE_SUPPORTS.items()},
   'component_chain_ranks':{n:dict(sorted(Counter(SLICE_DEG[i] for i in ids).items())) for n,ids in SLICE_SUPPORTS.items()},
   'homology':{'M':{'H1':'Z^3','other':'0'},'B':{'H1':'Z^5','other':'0'},'Q':{'H2':'Z^2','other':'0'},'V':{'H0':'Z','other':'0'}},
   'relative_conductor_cone_terms_in_this_component':0,
   'coefficient_sampling':False,'completeness_reason':'a homogeneous coefficient has uniquely forced exponents; reject iff negative or a mixed-sheet zero monomial',
   'states':[{'source_state_id':i,'state':state_label(GENS[i]),'coefficient_monomial':list(SLICE_BY_ID[i]),'coefficient':pstr({SLICE_BY_ID[i]:1})} for i in SLICE_IDS]},
 'contractions':{name:{'residual_basis':sorted(ret['d']), 'residual_degrees':[SLICE_DEG[i] for i in sorted(ret['d'])],
   'unit_pair_count':len(ret['cancellations']), 'cancellations':ret['cancellations'],
   'original_differential':serialize_int_matrix(SLICE_DIFFERENTIALS[name]),
   'projection':serialize_int_matrix(ret['p']),'inclusion':serialize_int_matrix(ret['i']),
   'homotopy':serialize_int_matrix(ret['h']),'residual_differential':serialize_int_matrix(ret['d'])}
    for name,ret in RETRACTS.items()},
 'Q_filling_classes':{'reference':'full projected corrected Morse filling',
   'group':'Z^3/Z*(1,1,1)','free_coordinates':['c03-c25','c14-c25'],
   'higher_homotopy_groups_in_this_component':'zero',
   'variations':{d:serialize_poly_vector(v) for d,v in Q_VARIATIONS.items()},
   'readout_matrix':[[i,d,c] for i,col in sorted(QZERO_PROJECTION.items()) for d,c in sorted(col.items())]},
 'actual_short_boundary_attachment':{'boundary_homology_basis_source_ids':B_H1,
   'total_homology_basis_source_ids':M_H1,
   'connecting_matrix':ATTACH_MATRIX,'inclusion_H1_matrix':INCLUSION_H1,
   'adapted_boundary_basis_columns':U,'adapted_basis_determinant':det_int(U),
   'adapted_connecting_matrix':DELTA_ADAPTED,
   'kernel_before_diagonal_quotient':'Z*(1,1,1)','kernel_on_H2_Q':'zero',
   'cokernel':'Z^3, torsion-free',
   'attachment_cycles':{d:serialize_poly_vector(v) for d,v in B_ATTACHMENTS.items()},
   'chain_witness_for_sum_relation':serialize_poly_vector(SHORT_TOP)},
 'full_filling_comparison':{'homotopy_class_count':1,'space_contractible_in_homogeneous_chain_model':True,
   'universal_primitive_formula':'H_M(y) for dy=0 and homological degree(y)=2',
   'corrected_Morse_filling':serialize_poly_vector(HM0),'corrected_roof':serialize_poly_vector(QM0),
   'computed_contraction_filling':serialize_poly_vector(CANON_FULL_H),
   'not_a_physical_conductor_identification':True},
 'verification':{'replayed_checks':REPLAY_TOTAL,'new_checks':new_checks,'new_checks_by_family':NEW_COUNTS,
   'basis_and_homotopy_proofs':'signed-unit integral contractions and unimodular support exact sequence',
   'no_inference_from_check_count':True}}
raw=json.dumps(payload,sort_keys=True,separators=(',',':'))
payload['result_sha256']=hashlib.sha256(raw.encode()).hexdigest()
payload['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
cert_path=Path(__file__).with_name('morse_q_filling_torsor_and_attachment_certificate.json')
cert_path.write_text(json.dumps(payload,sort_keys=True,indent=2)+'\n')
print(json.dumps({'certificate':str(cert_path),'new_checks':new_checks,'replayed_checks':REPLAY_TOTAL,
    'component_chain_ranks':payload['homogeneous_component']['component_chain_ranks'],
    'homology':payload['homogeneous_component']['homology'],
    'connecting_matrix':ATTACH_MATRIX,'adapted_connecting_matrix':DELTA_ADAPTED,
    'result_sha256':payload['result_sha256']},indent=2))
