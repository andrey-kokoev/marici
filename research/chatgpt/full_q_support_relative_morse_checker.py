#!/usr/bin/env python3
"""Full Q-support quotient and endpoint-relative Morse comparison.

Run: python full_q_support_relative_morse_checker.py
Uses only Python's standard library. Writes its specifically named certificate.
Reconstructs the 2,338-state loaded source, constructs the endpoint-augmentation
fibre, and supplies an explicit integral contraction of the complete barycentric
Q quotient to the seven-state cellular Q packet (fourteen with occurrence factor).
No physical conductor--Morse invariant is assumed.
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

# Serialization. All maps are sparse, exact, polynomial and fully reproducible.
def state_label(g):
    flag,H,k=g
    return {'flag':[sorted(f) for f in flag],'marks':list(H),'occurrence_bit':k,'degree':degree(g)}
def poly_json(p):return [[list(m),c] for m,c in sorted(p.items())]
def matrix_json(cols):
    return [{'source':src,'target':dst,'polynomial':poly_json(p),'coefficient':pstr(p)}
            for src,col in sorted(cols.items()) for dst,p in sorted(col.items())]
def vector_json(v):
    return [{'state':g,'polynomial':poly_json(p),'coefficient':pstr(p)} for g,p in sorted(v.items())]
def labelled_source_vector(v):
    return [{'state':state_label(g),'polynomial':poly_json(p),'coefficient':pstr(p)}
            for g,p in sorted(v.items(),key=lambda item:SID[item[0]])]

payload={
 'schema':'marici.full_q_support_relative_morse.v1',
 'scope':{'constructed':'full endpoint-augmentation fibre and actual short-support quotient; explicit quotient cellularization',
          'physical_Delta_J_computed':False,
          'physical_extraordinary_source_identification':False,
          'no_claim_of_nonzero_H1_from_unit_edge_coefficient':True},
 'provenance':{'repo':'andrey-kokoev/marici','commit':'d1947b67a60d3e88ba77f4ca60ea02c2a306ee61',
               'Morse_source':'research/voevodsky/check_d03_pabs_morse_pullback.rs',
               'Morse_blob_sha':'46624341c7956a8557249a54b117a88d43adfd62',
               'normalization_source':'src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md',
               'challenged_projection_claim':'src/ledger/20260817-397 The Descended qJ Roof Is the Canonical D03 Yoneda Generator.md'},
 'coefficients':{'variables':VARIABLES,'mixed_short_products':'Xeven*Xodd=0','short_normal_graph':'u_d=t_d*X_d',
                 'independent_long_normals':LONG,'inverted_parameters':[]},
 'state_counts':{'full_corrected_Morse':len(GENS),'old_support_filtration':[32,1552,2338],
                 'endpoint_relative_filtration':[34,1554,2340],
                 'relative_degree_minus_one_conductor_summands':2,
                 'Q_base_flags':len({g[0] for g in QGENS}),
                 'Q_base_states':len(QGENS),'Q_base_ranks':dict(sorted(Counter(degree(g) for g in QGENS).items())),
                 'Q_corrected_states':len(QTGEN),
                 'Q_corrected_ranks':dict(sorted(Counter(degree(QGENS[i])+k for i,k in QTGEN).items())),
                 'cellular_Q_base_states':7,'cellular_Q_corrected_states':14,
                 'cellular_Q_corrected_ranks':dict(sorted(Counter(CDEG[i]+k for i,k in CTGEN).items())),
                 'cancelled_unit_pairs_base':len(CANCELLATIONS)},
 'relative_source':{'definition':'fib(e_plus,e_minus: Mhat -> C ell_plus direct-sum C ell_minus)',
                     'new_differential_columns':[{'source_endpoint':s,'target_conductor':s,'coefficient':1} for s in ('plus','minus')],
                     'Q_quotient_unchanged':True,'identity_over_M_lift_exists':False,
                     'Morse_disk_inclusion':{'H':labelled_source_vector(HHAT),'q':labelled_source_vector(QHAT)},
                     'pulled_endpoint_maps_nullhomotopic':True,
                     'nullhomotopy':'endpoint basis -> -z in F1; source conductor comparison -> +1 in F0 conductor component'},
 'Q_base_states':[state_label(g) for g in QGENS],
 'Q_base_differential':matrix_json(DQ),
 'Q_to_cellular':matrix_json(P),'cellular_to_Q':matrix_json(INC),'Q_contraction':matrix_json(HOM),
 'cellular_Q_labels':CELLNAMES,'cellular_Q_differential':matrix_json(DC),
 'unit_cancellations':CANCELLATIONS,
 'Q_roof_data':{'Morse_top':vector_json(Q_HHAT),'corrected_roof':vector_json(Q_QHAT),
                'contraction_primitive':vector_json(CANON_H),'comparison_of_primitives':vector_json(SECOND_H),
                'degree_one_homology':0,'coefficient_of_top_D03_edge':1,
                'Morse_top_cellular_projection':0,'corrected_roof_cellular_projection':0},
 'invalid_projection_witness':{'triangle':state_label(triangle),'triangle_image':0,
                              'projected_boundary':[{'state':state_label(QGENS[edge_id]),'coefficient':1}],
                              'pure_flag_count':len({QGENS[i][0] for i in PURE}),
                              'pure_loaded_states':len(PURE)},
 'surviving_Q':{'H3_before_occurrence_tensor':'B generated by theta',
                'H2_before_occurrence_tensor':'coker([X03,u03,0,0; X14,0,u14,0; X25,0,0,u25])',
                'theta':vector_json(THETA),
                'corrected_Q_homology_in_degrees_below_two':'zero'},
 'verification':{'checks_by_family':dict(CHECKS),'exact_checks':sum(CHECKS.values()),
                  'numeric_parameter_sampling':False,'proofs_not_inferred_from_check_count':True,
                  'degree_one_vanishing_proof':'full chain contraction to a complex with no terms below degree two'}
}
raw=json.dumps(payload,sort_keys=True,separators=(',',':'))
payload['results_sha256']=hashlib.sha256(raw.encode()).hexdigest()
payload['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
path=Path(__file__).with_name('full_q_support_relative_morse_certificate.json')
path.write_text(json.dumps(payload,sort_keys=True,indent=2)+'\n')
print(json.dumps({'state_counts':payload['state_counts'],'exact_checks':payload['verification']['exact_checks'],
                  'Q_H_terms':len(Q_HHAT),'Q_q_terms':len(Q_QHAT),
                  'canonical_primitive_terms':len(CANON_H),'primitive_comparison_terms':len(SECOND_H),
                  'results_sha256':payload['results_sha256'],'certificate':str(path)},indent=2))
