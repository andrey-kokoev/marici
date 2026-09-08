#!/usr/bin/env python3
"""Central-flip spatial locality and explicit local conductor kernels.

Contains the preceding exact algebra routines for a standalone replay.
Conductor-costalk regulator continuation, full frame and source relations.

Standalone standard-library verifier. Reuses embedded deterministic algebra
routines from the preceding audit; reconstructs every target and source matrix
without companion data or network. All regulator grades are covered by exact
low-grade calculations and the proved native-mark bound of three.
"""
from __future__ import annotations
import argparse
from collections import Counter
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path

DIAGONALS = ('02','03','04','13','14','15','24','25','35')
PLUS = frozenset(('13','15','35'))
MINUS = frozenset(('02','04','24'))
SHORT = PLUS | MINUS
LONG = ('03','14','25')
VARIABLES = tuple('X'+d for d in DIAGONALS) + ('beta',)
ZERO = (0,)*10
COUNTS: Counter[str] = Counter()
COMMIT = 'd1947b67a60d3e88ba77f4ca60ea02c2a306ee61'


def check(value: bool, family: str, detail: object = '') -> None:
    if not value:
        raise AssertionError(f'{family}: {detail}')
    COUNTS[family] += 1


def put(v: dict, key: object, value: int) -> None:
    if value:
        v[key] = v.get(key, 0) + value
        if not v[key]:
            del v[key]


def add(a: dict, b: dict, scalar: int = 1) -> dict:
    out = dict(a)
    for key, value in b.items():
        put(out, key, scalar*value)
    return out


def monomial(*names: str) -> tuple[int, ...]:
    p = [0]*10
    for name in names:
        p[VARIABLES.index(name)] += 1
    return tuple(p)


def survives(p: tuple[int, ...]) -> bool:
    return not (any(p[DIAGONALS.index(d)] for d in PLUS)
                and any(p[DIAGONALS.index(d)] for d in MINUS))


def multiply(v: dict, p: tuple[int, ...], scalar: int = 1) -> dict:
    out = {}
    for (j, q), c in v.items():
        r = tuple(a+b for a,b in zip(p,q))
        if survives(r):
            put(out, (j,r), scalar*c)
    return out


def apply(matrix: dict, vector: dict) -> dict:
    out = {}
    for (j,p),c in vector.items():
        for (i,q),s in matrix.get(j,{}).items():
            r = tuple(a+b for a,b in zip(p,q))
            if survives(r):
                put(out,(i,r),c*s)
    return out


def unit(j: int) -> dict:
    return {(j,ZERO):1}


def restrict(v: dict, ids: set[int]) -> dict:
    return {(j,p):c for (j,p),c in v.items() if j in ids}


def crosses(a: str, b: str) -> bool:
    i,j = map(int,a)
    k,l = map(int,b)
    return i<k<j<l or k<i<l<j


class Complex:
    def __init__(self, occurrence: str = '35') -> None:
        self.occurrence = occurrence
        self.faces = [F for n in range(4) for F in combinations(DIAGONALS,n)
                      if all(not crosses(a,b) for a,b in combinations(F,2))]
        self.states = [(F,H,e) for F in self.faces for n in range(len(F)+1)
                       for H in combinations(F,n) for e in (0,1)]
        self.index = {s:j for j,s in enumerate(self.states)}
        self.degree = {j:3-len(F)+len(H)+e for j,(F,H,e) in enumerate(self.states)}
        self.weight = {j:len(H) for j,(F,H,e) in enumerate(self.states)}
        self.V = {j for j,(F,H,e) in enumerate(self.states) if frozenset(F) in (PLUS,MINUS)}
        self.B = {j for j,(F,H,e) in enumerate(self.states) if set(F)&SHORT}
        self.Q = set(range(430))-self.B
        self.end_top = {self.index[(tuple(sorted(F)),tuple(sorted(F)),e)]
                        for F in (MINUS,PLUS) for e in (0,1)}
        self.boundary_ids = self.Q | self.end_top
        self.kernel_ids = set(range(430))-self.boundary_ids
        face_set = set(self.faces)
        self.d = {j:{} for j in range(430)}
        for j,(F,H,e) in enumerate(self.states):
            for a in DIAGONALS:
                FF = tuple(sorted(F+(a,)))
                if a not in F and FF in face_set:
                    put(self.d[j],(self.index[FF,H,e],monomial('X'+a)),
                        (-1)**sum(b<a for b in F))
            for n,a in enumerate(H):
                put(self.d[j],(self.index[F,H[:n]+H[n+1:],e],monomial('beta','X'+a)),
                    (-1)**(3-len(F)+n))
            if e:
                put(self.d[j],(self.index[F,H,0],monomial('X'+self.occurrence)),
                    (-1)**(3-len(F)+len(H)))
        check(Counter(map(len,self.faces))=={0:1,1:9,2:21,3:14},'face_census')
        check((len(self.states),len(self.V),len(self.B),len(self.Q),len(self.end_top),len(self.kernel_ids))
              ==(430,32,416,14,4,412),'full_support_counts')
        for j,col in self.d.items():
            check(not apply(self.d,col),'full_d_squared',j)
            check(all(self.degree[i]==self.degree[j]-1 for i,p in col),'full_degree',j)
            if j in self.V:
                check(all(i in self.V for i,p in col),'endpoint_subcomplex',j)
            if j in self.B:
                check(all(i in self.B for i,p in col),'short_boundary_subcomplex',j)
            if j in self.kernel_ids:
                check(all(i in self.kernel_ids for i,p in col),'joint_frame_kernel_subcomplex',j)
        self.d_boundary={j:restrict(self.d[j],self.boundary_ids) for j in self.boundary_ids}
        for j in range(430):
            check(restrict(self.d[j],self.boundary_ids)
                  ==apply(self.d_boundary,restrict(unit(j),self.boundary_ids)),
                  'joint_boundary_is_chain_map',j)

    def occurrence_zero(self) -> tuple[dict,dict]:
        coefficients={}
        for j,(F,H,e) in enumerate(self.states):
            p=[0]*10
            for a in F:p[DIAGONALS.index(a)]+=1
            for a in H:p[DIAGONALS.index(a)]-=1
            p[DIAGONALS.index(self.occurrence)]-=e
            if min(p)>=0 and survives(tuple(p)):
                coefficients[j]=tuple(p)
        d={j:{} for j in coefficients}
        for j,p in coefficients.items():
            for (i,q),c in self.d[j].items():
                r=tuple(a+b for a,b in zip(p,q))
                if not survives(r):continue
                check(i in coefficients,'weight_zero_target_exists',(j,i))
                rr=list(r);rr[9]=0
                check(tuple(rr)==coefficients[i],'forced_occurrence_monomial',(j,i))
                check(r[9]==self.weight[j]-self.weight[i],
                      'beta_weight_on_every_slice_arrow',(j,i))
                put(d[j],i,c)
        check(dict(sorted(Counter(self.degree[j] for j in coefficients).items()))
              =={0:8,1:59,2:108,3:56},'full_occurrence_zero_ranks')
        return coefficients,d


def verify_fibre(M: Complex) -> dict:
    # F_n = C_n + D_{n+1}; d_F(c,h)=(dc,rho(c)-d_D h).
    # Extra fibre indices use 430 + the corresponding original target id.
    dF={j:dict(col) for j,col in M.d.items()}
    for j in M.boundary_ids:
        put(dF[j],(430+j,ZERO),1)
        dF[430+j]={(430+i,p):-c for (i,p),c in M.d_boundary[j].items()}
    alpha={j:restrict(M.d[j],M.kernel_ids) for j in M.boundary_ids}
    projection={j:(unit(j) if j in M.kernel_ids else {}) for j in range(430)}
    projection.update({430+j:{k:-c for k,c in alpha[j].items()} for j in M.boundary_ids})
    inclusion={j:unit(j) for j in M.kernel_ids}
    homotopy={j:{} for j in dF}
    homotopy.update({430+j:unit(j) for j in M.boundary_ids})
    dK={j:dict(M.d[j]) for j in M.kernel_ids}
    for j in dF:
        check(not apply(dF,dF[j]),'full_coherent_fibre_d_squared',j)
        check(apply(projection,dF[j])==apply(dK,projection[j]),'fibre_projection_chain',j)
        lhs=add(apply(dF,homotopy[j]),apply(homotopy,dF[j]))
        rhs=add(unit(j),apply(inclusion,projection[j]),-1)
        check(lhs==rhs,'full_coherent_fibre_contraction',j)
    for j in M.kernel_ids:
        check(apply(projection,inclusion[j])==unit(j),'fibre_retract_identity',j)
        check(apply(dF,inclusion[j])==apply(inclusion,dK[j]),'fibre_inclusion_chain',j)
    check((len(dF),len(dK))==(448,412),'fibre_and_kernel_ranks')
    return {'d':dF,'p':projection,'i':inclusion,'h':homotopy,'alpha':alpha}


def int_apply(matrix: dict, vector: dict) -> dict:
    out={}
    for j,c in vector.items():
        for i,v in matrix[j].items():put(out,i,c*v)
    return out


def weighted_vector_apply(matrix: dict, v: dict, weight: dict) -> dict:
    """Independent multiplication of actual univariate polynomial vectors."""
    out={}
    for (j,p),c in v.items():
        for i,a in matrix[j].items():
            exponent=p+weight[j]-weight[i]
            check(exponent>=0,'univariate_matrix_products_remain_polynomial')
            put(out,(i,exponent),c*a)
    return out


def polynomial_normal_form(ids: set[int], original: dict, weight: dict,
                           degree: dict, label: str) -> dict:
    """Split a graded Z[beta]-complex into explicit monomial 2-state blocks.

    Each entry has a forced beta power weight(source)-weight(target).
    A minimum-power coefficient +/-1 divides every entry needed for the
    elimination. All changes of basis have polynomial coefficients and
    determinant one; nonunit beta blocks are retained, NEVER contracted.
    """
    ids=sorted(ids)
    d={j:{i:c for i,c in original[j].items() if i in ids} for j in ids}
    start={j:dict(col) for j,col in d.items()}
    inc={j:{j:1} for j in ids}
    proj={j:{j:1} for j in ids}
    active=set(ids);blocks=[];operations=[]
    while True:
        entries=sorted((weight[j]-weight[i],abs(c),j,i,c)
                       for j in active for i,c in d[j].items() if i in active)
        if not entries:break
        power,abs_c,hi,lo,sg=entries[0]
        check(power>=0 and abs_c==1,'polynomial_pivot_exists',label)
        rest={i:c*sg for i,c in d[hi].items() if i!=lo}
        check(all(weight[lo]>=weight[i] for i in rest),'lower_basis_change_polynomial',label)
        for i,c in rest.items():inc[lo]=add(inc[lo],inc[i],c)
        for j in ids:
            c=proj[j].get(lo,0)
            if c:proj[j]=add(proj[j],rest,-c)
        newlo=dict(d[lo])
        for i,c in rest.items():newlo=add(newlo,d[i],c)
        d[lo]=newlo
        for j in active:
            c=d[j].get(lo,0)
            if c:d[j]=add(d[j],rest,-c)
        check(d[hi]=={lo:sg} and not d[lo],'isolated_pivot_outgoing',label)
        others={j:d[j][lo]*sg for j in active if j!=hi and d[j].get(lo)}
        check(all(weight[j]>=weight[hi] for j in others),'upper_basis_change_polynomial',label)
        for j,c in others.items():
            inc[j]=add(inc[j],inc[hi],-c)
            d[j]=add(d[j],d[hi],-c)
        for j in ids:
            c=sum(v*proj[j].get(t,0) for t,v in others.items())
            if c:proj[j]=add(proj[j],{hi:c})
        for j in active:
            c=sum(v*d[j].get(t,0) for t,v in others.items())
            if c:d[j]=add(d[j],{hi:c})
        check(all(j==hi or not d[j].get(lo) for j in active),'pivot_row_isolated',label)
        check(all(not d[j].get(hi) for j in active),'pivot_no_incoming',label)
        blocks.append((hi,lo,sg,power))
        operations.append({'upper':hi,'lower':lo,'coefficient':sg,'beta_power':power,
                           'lower_change':sorted(rest.items()),'upper_changes':sorted(others.items())})
        active-={hi,lo}
    for j in ids:
        check(int_apply(proj,inc[j])=={j:1},'normal_form_inverse_pi',label)
        check(int_apply(inc,proj[j])=={j:1},'normal_form_inverse_ip',label)
        check(int_apply(start,inc[j])==int_apply(inc,d[j]),'normal_form_chain_identity',label)
        check(all(weight[j]>=weight[i] for i in inc[j]),'normal_form_inclusion_polynomial',label)
        check(all(weight[j]>=weight[i] for i in proj[j]),'normal_form_projection_polynomial',label)
        # Recheck both inverses and chain equations with literal polynomial powers.
        v={(j,0):1}
        ic=weighted_vector_apply(inc,v,weight)
        pc=weighted_vector_apply(proj,v,weight)
        check(weighted_vector_apply(proj,ic,weight)==v,'literal_polynomial_pi',label)
        check(weighted_vector_apply(inc,pc,weight)==v,'literal_polynomial_ip',label)
        check(weighted_vector_apply(start,ic,weight)
              ==weighted_vector_apply(inc,weighted_vector_apply(d,v,weight),weight),
              'literal_polynomial_chain_identity',label)
    free=Counter(degree[j] for j in active)
    torsion=Counter((degree[lo],power) for hi,lo,c,power in blocks if power)
    units=Counter(degree[lo] for hi,lo,c,power in blocks if not power)
    return {'inclusion':inc,'projection':proj,'differential':d,'blocks':blocks,
            'free':sorted(active),'free_ranks':dict(sorted(free.items())),
            'torsion_blocks':[[n,k,v] for (n,k),v in sorted(torsion.items())],
            'unit_blocks':dict(sorted(units.items())),'operations':operations}


def serialize_full_matrix(matrix: dict) -> list:
    return [[j,i,c,list(p)] for j,col in sorted(matrix.items())
            for (i,p),c in sorted(col.items())]


def serialize_weighted_matrix(matrix: dict, weight: dict) -> list:
    return [[j,i,c,weight[j]-weight[i]] for j,col in sorted(matrix.items())
            for i,c in sorted(col.items())]


def serialize_normal_form(result: dict, weight: dict) -> dict:
    return {key:result[key] for key in ('blocks','free','free_ranks','torsion_blocks','unit_blocks','operations')} | {
        'inclusion':serialize_weighted_matrix(result['inclusion'],weight),
        'projection':serialize_weighted_matrix(result['projection'],weight),
        'differential':serialize_weighted_matrix(result['differential'],weight)}


def serialize_chain(v: dict, M: Complex) -> list:
    return [{'state_index':j,'face':list(M.states[j][0]),'marks':list(M.states[j][1]),
             'occurrence_partner':M.states[j][2],'integer':c,'exponents':list(p)}
            for (j,p),c in sorted(v.items())]



H_INPUT=[
 (('02',),('02',),0,2,1),
 (('03',),('03',),0,2,1),
 (('04',),('04',),0,2,1),
 (('13',),('13',),0,2,1),
 (('35',),(),1,3,1),
 (('02','03'),('02','03'),0,1,1),
 (('02','35'),('02',),1,2,1),
 (('03','04'),('03','04'),0,1,1),
 (('03','13'),('03','13'),0,1,1),
 (('03','35'),('03',),1,2,1),
 (('04','13'),('04','13'),0,1,1),
 (('02','03','04'),('02','03','04'),0,0,-1),
 (('02','03','35'),('02','03'),1,1,-1),
 (('03','04','13'),('03','04','13'),0,0,-1),
 (('03','13','35'),('03','13'),1,1,-1),
]

def sign(n: int) -> int:
    return -1 if n % 2 else 1


def occurrence_component(M: Complex, direction: str | None,
                         conductor_relative: bool = True) -> tuple[dict,dict]:
    w=[0]*10
    if direction is not None:
        w[DIAGONALS.index(direction)]=1
    coeff={}
    for j,(F,H,e) in enumerate(M.states):
        p=w[:]
        for a in F:p[DIAGONALS.index(a)]+=1
        for a in H:p[DIAGONALS.index(a)]-=1
        p[DIAGONALS.index(M.occurrence)]-=e
        if min(p)<0 or not survives(tuple(p)):
            continue
        if conductor_relative and not any(p[DIAGONALS.index(a)] for a in SHORT):
            continue
        coeff[j]=tuple(p)
    d={j:{} for j in coeff}
    for j,p in coeff.items():
        for (i,q),v in M.d[j].items():
            total=tuple(a+b for a,b in zip(p,q))
            if not survives(total):continue
            check(i in coeff,'relative_occurrence_component_is_subcomplex',(direction,j,i))
            check(total[:9]==coeff[i][:9], 'exact_occurrence_weight',(direction,j,i))
            check(total[9]==M.weight[j]-M.weight[i], 'exact_regulator_weight',(direction,j,i))
            put(d[j],i,v)
    for j in d:
        check(not int_apply(d,d[j]),'component_d_squared',(direction,j))
    return coeff,d


def full_endpoint_q_kernel(M: Complex, coeff: dict, original: dict, label: str) -> dict:
    """Maximal subcomplex with zero Q and full endpoint components.

    N = {v: pi_Q(v)=0, pr_V(v)=0, pr_V(dv)=0}. Endpoint incoming
    equations are partitioned signed-unit rows in each chosen component.
    Their kernel has a saturated polynomial basis. Its quotient is an
    actual chain-map frame, so no false chain projection to all of V is used.
    """
    ids=set(coeff)
    candidates=ids-M.V-M.Q
    rows={}
    for j in sorted(candidates):
        values=[(i,v) for i,v in original[j].items() if i in M.V]
        check(len(values)<=1,'endpoint_incoming_column_has_at_most_one_row',(label,j))
        for i,v in values:
            check(abs(v)==1 and M.weight[j]==M.weight[i],
                  'endpoint_constraint_is_polynomial_unit',(label,j,i))
            rows.setdefault(i,{})[j]=v
    pivots={min(col) for col in rows.values()}
    N=candidates-pivots
    inc={j:{j:1} for j in sorted(ids)}
    for i,col in sorted(rows.items()):
        p=min(col);sp=col[p]
        for j,v in col.items():
            if j!=p:put(inc[j],p,-sp*v)
    inv={j:{j:1} for j in sorted(ids)}
    for j in N:
        for p,v in inc[j].items():
            if p!=j:put(inv[j],p,-v)
    d={}
    for j in sorted(ids):
        check(int_apply(inv,inc[j])=={j:1},'endpoint_kernel_change_of_basis_inverse',(label,j))
        check(int_apply(inc,inv[j])=={j:1},'endpoint_kernel_inverse_other_direction',(label,j))
        check(all(M.weight[j]==M.weight[i] for i in inc[j]),
              'endpoint_kernel_basis_preserves_normal_weight',(label,j))
        d[j]=int_apply(inv,int_apply(original,inc[j]))
        if j in N:
            check(all(i in N for i in d[j]),'refined_kernel_is_subcomplex',(label,j))
            check(not any(i in M.V or i in M.Q for i in inc[j]),
                  'kernel_has_literal_zero_full_endpoint_and_Q',(label,j))
            check(not any(i in M.V for i in int_apply(original,inc[j])),
                  'kernel_has_zero_endpoint_connecting_column',(label,j))
    kd={j:dict(d[j]) for j in sorted(N)}
    frame=ids-N
    fd={j:{i:v for i,v in d[j].items() if i in frame} for j in sorted(frame)}
    # Include all endpoint states and full Q states occurring at this weight.
    check((ids&M.V)<=frame and (ids&M.Q)<=frame,'complete_endpoint_and_Q_retained_in_frame',label)
    # The frame is the quotient in the new split graded basis.
    rho={j:({j:1} if j in frame else {}) for j in sorted(ids)}
    for j in ids:
        check(int_apply(rho,d[j])==int_apply(fd,rho[j]),'refined_quotient_frame_is_chain_map',(label,j))

    # Explicit homotopy fibre F_n=M_n+frame_{n+1} and retract to N.
    off=1000
    df={j:dict(d[j]) for j in sorted(ids)}
    wf={j:M.weight[j] for j in ids}
    degf={j:M.degree[j] for j in ids}
    for j in frame:
        put(df[j],off+j,1)
        df[off+j]={off+i:-v for i,v in fd[j].items()}
        wf[off+j]=M.weight[j]
        degf[off+j]=M.degree[j]-1
    pp={j:({j:1} if j in N else {}) for j in ids}
    pp.update({off+j:{i:-v for i,v in d[j].items() if i in N} for j in frame})
    ii={j:{j:1} for j in N}
    hh={j:{} for j in df}
    hh.update({off+j:{j:1} for j in frame})
    for j in sorted(df):
        v={(j,0):1}
        check(not weighted_vector_apply(df,weighted_vector_apply(df,v,wf),wf),
              'boundary_coherent_fibre_polynomial_d_squared',(label,j))
        left=add(weighted_vector_apply(df,weighted_vector_apply(hh,v,wf),wf),
                 weighted_vector_apply(hh,weighted_vector_apply(df,v,wf),wf))
        right=add(v,weighted_vector_apply(ii,weighted_vector_apply(pp,v,wf),wf),-1)
        check(left==right,'boundary_coherent_fibre_exact_contraction',(label,j))
        check(weighted_vector_apply(pp,weighted_vector_apply(df,v,wf),wf)
              ==weighted_vector_apply(kd,weighted_vector_apply(pp,v,wf),wf),
              'boundary_coherent_fibre_projection_chain',(label,j))
    for j in N:
        check(int_apply(pp,ii[j])=={j:1},'boundary_coherent_fibre_retract_pi',(label,j))
    return {'ids':N,'d':kd,'inclusion':{j:inc[j] for j in N},
            'full_basis_inclusion':inc,'full_basis_inverse':inv,'full_split_differential':d,
            'frame_ids':frame,'frame_differential':fd,'quotient_projection':rho,
            'constraint_rows':rows,'boundary_fibre':{'d':df,'p':pp,'i':ii,'h':hh,
                    'weight':wf,'degree':degf}}


def supported_hom(kd: dict, M: Complex) -> tuple[dict,dict,dict]:
    ids=set(kd)
    hw={2*j+b:M.weight[j]-b for j in ids for b in (0,1)}
    hd={2*j+b:M.degree[j]-2-b for j in ids for b in (0,1)}
    d={j:{} for j in hw}
    for j in ids:
        for b in (0,1):
            for i,v in kd[j].items():put(d[2*j+b],2*i+b,v)
            if b==0:put(d[2*j],2*j+1,-sign(M.degree[j]-2))
    for j in d:
        check(not weighted_vector_apply(d,weighted_vector_apply(d,{(j,0):1},hw),hw),
              'supported_Hom_polynomial_d_squared',j)
    return d,hw,hd


def primary_fibre(kd: dict, M: Complex, label: str) -> dict:
    """F_n=(a in N_{n+2}, b in N_{n+3}, h in N_{n+3}).

    d(a,b,h)=(da, db-(-1)^n beta*a, a-dh).
    Projection is b-(-1)^n beta*h. Homotopy is (a,b,h)->(h,0,0).
    The h component has the p-input normal weight, not the e-input weight.
    """
    ids=set(kd)
    weight={3*j+c:M.weight[j]-(1 if c==1 else 0) for j in ids for c in range(3)}
    degree={3*j+c:M.degree[j]-(2 if c==0 else 3) for j in ids for c in range(3)}
    d={j:{} for j in weight}
    for j in ids:
        for i,v in kd[j].items():
            put(d[3*j],3*i,v)
            put(d[3*j+1],3*i+1,v)
            put(d[3*j+2],3*i+2,-v)
        n=M.degree[j]-2
        put(d[3*j],3*j+1,-sign(n)) # forced coefficient beta
        put(d[3*j],3*j+2,1)
    target_weight={j:M.weight[j]-1 for j in ids}
    target_degree={j:M.degree[j]-3 for j in ids}
    all_weight=weight|{5000+j:w for j,w in target_weight.items()}
    target_d={5000+j:{5000+i:v for i,v in col.items()} for j,col in kd.items()}
    p={j:{} for j in d}
    for j in ids:
        p[3*j+1]={5000+j:1}
        n=M.degree[j]-3
        p[3*j+2]={5000+j:-sign(n)} # forced coefficient beta
    i={5000+j:{3*j+1:1} for j in ids}
    h={j:{} for j in d}
    h.update({3*j+2:{3*j:1} for j in ids})
    for j in sorted(d):
        v={(j,0):1}
        check(not weighted_vector_apply(d,weighted_vector_apply(d,v,all_weight),all_weight),
              'primary_coherent_fibre_polynomial_d_squared',(label,j))
        check(weighted_vector_apply(p,weighted_vector_apply(d,v,all_weight),all_weight)
              ==weighted_vector_apply(target_d,weighted_vector_apply(p,v,all_weight),all_weight),
              'primary_coherent_projection_chain',(label,j))
        left=add(weighted_vector_apply(d,weighted_vector_apply(h,v,all_weight),all_weight),
                 weighted_vector_apply(h,weighted_vector_apply(d,v,all_weight),all_weight))
        right=add(v,weighted_vector_apply(i,weighted_vector_apply(p,v,all_weight),all_weight),-1)
        check(left==right,'primary_coherent_fibre_exact_contraction',(label,j))
    for j in ids:
        v={(5000+j,0):1}
        check(weighted_vector_apply(p,weighted_vector_apply(i,v,all_weight),all_weight)==v,
              'primary_coherent_retract_identity',(label,j))
    return {'d':d,'p':p,'i':i,'h':h,'weight':all_weight,'degree':degree,
            'target_d':target_d,'target_degree':target_degree}


def saturated_integer_rank(a: list[list[int]], label: str) -> tuple[int,list]:
    a=[r[:] for r in a]
    m=len(a);n=len(a[0]) if m else 0;k=0;log=[]
    while True:
        ent=[(abs(a[i][j]),i,j) for i in range(k,m) for j in range(k,n) if a[i][j]]
        if not ent:break
        v,i,j=min(ent)
        check(v==1,'integer_saturation_unit_pivot',label)
        a[k],a[i]=a[i],a[k]
        for r in a:r[k],r[j]=r[j],r[k]
        if a[k][k]<0:a[k]=[-v for v in a[k]]
        for ii in range(k+1,m):
            z=a[ii][k]
            if z:a[ii]=[x-z*y for x,y in zip(a[ii],a[k])]
        for jj in range(k+1,n):
            z=a[k][jj]
            if z:
                for ii in range(m):a[ii][jj]-=z*a[ii][k]
        log.append([k,i,j]);k+=1
    check(all(a[i][j]==(1 if i==j and i<k else 0) for i in range(m) for j in range(n)),
          'integer_saturation_complete_diagonal',label)
    return k,log


def encode_cycle(M: Complex, coeff: dict, kernel: dict, nf: dict,
                 j: int, regulator_grade: int | None = None) -> dict:
    total=M.weight[j] if regulator_grade is None else regulator_grade
    vec={}
    for i,v in nf['inclusion'][j].items():
        check(total>=M.weight[i],'cycle_coefficient_regulator_exponent_nonnegative',j)
        for a,q in kernel['inclusion'][i].items():
            p=list(coeff[a]);p[9]=total-M.weight[a]
            put(vec,(a,tuple(p)),v*q)
    check(not apply(M.d,vec),'exported_full_polynomial_cycle_closed',j)
    check(not restrict(vec,M.V) and not restrict(vec,M.Q),
          'exported_full_polynomial_cycle_all_endpoint_Q_zero',j)
    return vec


def serialize_primary(f: dict) -> dict:
    return {k:serialize_weighted_matrix(f[k],f['weight']) for k in ('d','p','i','h','target_d')} | {
        'basis_weight':sorted(f['weight'].items()),'basis_degree':sorted(f['degree'].items()),
        'target_degree':sorted(f['target_degree'].items())}



SHORT_ORDER = tuple(sorted(SHORT))

def conductor_order(p: tuple[int, ...]) -> int:
    return sum(p[DIAGONALS.index(a)] for a in SHORT_ORDER)


def dense_identity(n: int) -> list[list[int]]:
    return [[int(i == j) for j in range(n)] for i in range(n)]


def dense_product(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    if not a:
        return []
    n = len(b[0]) if b else 0
    out = [[0]*n for _ in a]
    sparse_b = [[(j,v) for j,v in enumerate(row) if v] for row in b]
    for i,row in enumerate(a):
        for k,value in enumerate(row):
            if value:
                for j,w in sparse_b[k]:
                    out[i][j] += value*w
    return out


def dense_columns(columns: list[list[int]], rows: int) -> list[list[int]]:
    return [[v[i] for v in columns] for i in range(rows)]


def integer_diagonalize(a: list[list[int]], label: str) -> dict:
    """Unimodular diagonalization by Euclidean row/column operations.

    Divisibility ordering of diagonal entries is unnecessary for kernels.
    Return U,V,V^{-1} with U*A*V diagonal and verify these identities exactly.
    """
    m = len(a); n = len(a[0]) if m else 0
    d = [row[:] for row in a]
    U = dense_identity(m); V = dense_identity(n); Vi = dense_identity(n)
    operations = []
    def row_swap(i,j):
        if i != j:
            d[i],d[j] = d[j],d[i]; U[i],U[j] = U[j],U[i]
            operations.append(['row_swap',i,j])
    def col_swap(i,j):
        if i != j:
            for matrix in (d,V):
                for row in matrix: row[i],row[j] = row[j],row[i]
            Vi[i],Vi[j] = Vi[j],Vi[i]
            operations.append(['column_swap',i,j])
    def row_add(i,j,c):
        if c:
            d[i] = [x+c*y for x,y in zip(d[i],d[j])]
            U[i] = [x+c*y for x,y in zip(U[i],U[j])]
            operations.append(['row_add',i,j,c])
    def col_add(i,j,c):
        if c:
            for matrix in (d,V):
                for row in matrix: row[i] += c*row[j]
            Vi[j] = [x-c*y for x,y in zip(Vi[j],Vi[i])]
            operations.append(['column_add',i,j,c])
    r=0
    while r < min(m,n):
        entries=[(abs(d[i][j]),i,j) for i in range(r,m)
                 for j in range(r,n) if d[i][j]]
        if not entries: break
        _,i,j = min(entries); row_swap(r,i); col_swap(r,j)
        while True:
            change=False
            for i in range(r+1,m):
                if d[i][r]:
                    q=d[i][r]//d[r][r]; row_add(i,r,-q)
                    if d[i][r]: row_swap(r,i)
                    change=True; break
            if change: continue
            for j in range(r+1,n):
                if d[r][j]:
                    q=d[r][j]//d[r][r]; col_add(j,r,-q)
                    if d[r][j]: col_swap(r,j)
                    change=True; break
            if not change: break
        if d[r][r] < 0:
            d[r] = [-v for v in d[r]]; U[r] = [-v for v in U[r]]
            operations.append(['row_negate',r])
        r += 1
    check(all(not d[i][j] for i in range(m) for j in range(n) if i != j),
          'integral_diagonal_form', label)
    check(dense_product(dense_product(U,a),V)==d,'integral_diagonal_identity',label)
    check(dense_product(V,Vi)==dense_identity(n),'integral_column_basis_inverse',label)
    check(dense_product(Vi,V)==dense_identity(n),'integral_inverse_column_basis',label)
    kernel=[[V[i][j] for j in range(r,n)] for i in range(n)]
    check(not any(v for row in dense_product(a,kernel) for v in row),
          'integral_kernel_exact',label)
    return {'rank':r,'diagonal':[d[i][i] for i in range(r)],
            'left':U,'right':V,'right_inverse':Vi,'kernel':kernel,
            'operations':operations}


def truncation_data(M: Complex, direction: str, cutoff: int) -> dict:
    allcoeff,old=occurrence_component(M,direction,True)
    coeff={j:p for j,p in allcoeff.items() if conductor_order(p)<=cutoff}
    d={j:{i:v for i,v in old[j].items() if i in coeff} for j in coeff}
    kernel=full_endpoint_q_kernel(M,coeff,d,f'{direction}_I{cutoff}')
    nf=polynomial_normal_form(kernel['ids'],kernel['d'],M.weight,M.degree,
                              f'{direction}_I{cutoff}')
    tops=[j for j in nf['free'] if M.degree[j]==3 and M.weight[j]<=3]
    cycles=[]
    for j in tops:
        v={}
        for i,z in nf['inclusion'][j].items():
            for r,w in kernel['inclusion'][i].items():
                p=list(coeff[r]); p[9]=3-M.weight[r]
                put(v,(r,tuple(p)),z*w)
        check(all(p[9]>=0 for r,p in v),'first_symbol_coefficients_polynomial',(direction,j))
        check(not restrict(v,M.V) and not restrict(v,M.Q),
              'truncated_cycle_endpoint_Q_values_zero',(direction,cutoff,j))
        dv=apply(M.d,v)
        check(not {k:z for k,z in dv.items() if conductor_order(k[1])<=cutoff},
              'truncated_cycle_full_boundary_check',(direction,cutoff,j))
        cycles.append(v)
    return {'coeff':coeff,'d':d,'kernel':kernel,'nf':nf,'tops':tops,'cycles':cycles}


def cycle_coordinates(v: dict, data: dict, M: Complex) -> list[int]:
    raw={}
    for (j,p),z in v.items():
        if j not in data['coeff']: continue
        check(p[:9]==data['coeff'][j][:9], 'cycle_exact_occurrence_degree',j)
        put(raw,(j,p[9]),z)
    kk=weighted_vector_apply(data['kernel']['full_basis_inverse'],raw,M.weight)
    check(all(j in data['kernel']['ids'] for j,k in kk),'cycle_in_complete_frame_kernel')
    nn=weighted_vector_apply(data['nf']['projection'],kk,M.weight)
    check(all(j in data['tops'] for j,k in nn),'cycle_has_only_top_coordinates')
    result=[0]*len(data['tops'])
    for (j,k),z in nn.items():
        check(k==3-M.weight[j],'cycle_coordinate_regulator_weight',j)
        result[data['tops'].index(j)] += z
    reconstruction={}
    for c,w in zip(result,data['cycles']): reconstruction=add(reconstruction,w,c)
    check(reconstruction==v,'top_cycle_coordinate_reconstruction')
    return result


def polygon_diagonal(a: str, r: int, reflection: int = 0) -> str:
    return ''.join(map(str,sorted(((-1)**reflection*int(v)+2*r+2*reflection)%6
                                 for v in a)))


def list_parity(xs: list[str]) -> int:
    return (-1)**sum(xs[i]>xs[j] for i in range(len(xs)) for j in range(i+1,len(xs)))


def polygon_action(M: Complex,v: dict,r: int,reflection: int = 0) -> dict:
    out={}
    for (j,p),z in v.items():
        F,H,e=M.states[j]
        ff=[polygon_diagonal(a,r,reflection) for a in F]
        hh=[polygon_diagonal(a,r,reflection) for a in H]
        i=M.index[tuple(sorted(ff)),tuple(sorted(hh)),e]
        pp=[0]*10; pp[9]=p[9]
        for k,a in enumerate(DIAGONALS):
            pp[DIAGONALS.index(polygon_diagonal(a,r,reflection))]=p[k]
        put(out,(i,tuple(pp)),(-1)**reflection*list_parity(ff)*list_parity(hh)*z)
    return out


def reflection_matrix(M: Complex,cases: dict,cutoff: int) -> tuple[list,list]:
    labels=[(a,j) for a in SHORT_ORDER for j in cases[a][cutoff]['tops']]
    n=len(labels); matrix=[[0]*n for _ in range(n)]; col=0
    for a in SHORT_ORDER:
        b=polygon_diagonal(a,0,1)
        off=sum(len(cases[x][cutoff]['tops']) for x in SHORT_ORDER if x<b)
        for v in cases[a][cutoff]['cycles']:
            c=cycle_coordinates(polygon_action(M,v,0,1),cases[b][cutoff],M)
            for i,z in enumerate(c): matrix[off+i][col]=z
            col+=1
    check(dense_product(matrix,matrix)==dense_identity(n),'reflection_square_on_symbol_lattice',cutoff)
    return labels,matrix


def fixed_lattice(S: list[list[int]], label: str) -> dict:
    n=len(S); diff=[[S[i][j]-int(i==j) for j in range(n)] for i in range(n)]
    out=integer_diagonalize(diff,label)
    out['fixed_rank']=n-out['rank']
    check(dense_product(S,out['kernel'])==out['kernel'],'fixed_lattice_exact_action',label)
    return out


def combine_global(M: Complex,cases: dict,cutoff: int,coordinates: list[int]) -> dict:
    out={}; k=0
    for a in SHORT_ORDER:
        for v in cases[a][cutoff]['cycles']:
            out=add(out,v,coordinates[k]); k+=1
    return out



# ---------- New calculation: actual normalization ideal as source ----------

import sys
b = sys.modules[__name__]
SHORT_ORDER = tuple(sorted(SHORT))


def source_resolution():
    """Resolve I=I_+ direct-sum I_- through relations among relations.

    F0 has six generators, F1 has 24, F2 has 92. All remaining resolution
    terms can be put in higher homological degrees and cannot contribute
    to the degree-zero maps or positive-degree homotopies calculated here.
    Exactness is also proved, for arbitrary polynomial coefficients, in
    the accompanying mathematical proof by branch decomposition.
    """
    rel=[]
    for sheet in (sorted(PLUS), sorted(MINUS)):
        opposite=sorted(SHORT-set(sheet))
        for a,c in combinations(sheet,2):
            rel.append({'name':('K',a,c),
                        'weight':monomial('X'+a,'X'+c)[:9],
                        'd':{c:{monomial('X'+a):1}, a:{monomial('X'+c):-1}}})
        for n in opposite:
            for a in sheet:
                rel.append({'name':('M',n,a),
                            'weight':monomial('X'+n,'X'+a)[:9],
                            'd':{a:{monomial('X'+n):1}}})
    relindex={r['name']:j for j,r in enumerate(rel)}
    sids={a:i for i,a in enumerate(SHORT_ORDER)}
    d0={sids[a]:{(0,monomial('X'+a)):1} for a in SHORT_ORDER}
    d1={j:{(sids[a],p):z for a,ps in r['d'].items() for p,z in ps.items()}
        for j,r in enumerate(rel)}
    syzy=[]
    for sheet in (sorted(PLUS),sorted(MINUS)):
        opposite=sorted(SHORT-set(sheet))
        a,c,d=sheet
        syzy.append({'name':('KK',a,c,d), 'd':{
            (relindex['K',c,d],monomial('X'+a)):1,
            (relindex['K',a,d],monomial('X'+c)):-1,
            (relindex['K',a,c],monomial('X'+d)):1}})
        for n in opposite:
            for a,c in combinations(sheet,2):
                syzy.append({'name':('MK',n,a,c),'d':{
                    (relindex['K',a,c],monomial('X'+n)):1}})
        for p in sheet:
            for n in opposite:
                for a in sheet:
                    syzy.append({'name':('PM',a,n,p),'d':{
                        (relindex['M',n,p],monomial('X'+a)):1}})
            for n,m in combinations(opposite,2):
                syzy.append({'name':('MM',n,m,p),'d':{
                    (relindex['M',m,p],monomial('X'+n)):1,
                    (relindex['M',n,p],monomial('X'+m)):-1}})
    check((len(sids),len(rel),len(syzy))==(6,24,92),'source_resolution_ranks')
    for j,v in d1.items():check(not apply(d0,v),'source_first_relations_exact',j)
    for j,sy in enumerate(syzy):
        check(not apply(d1,sy['d']),'source_second_relations_exact',j)
        weights={tuple(x+y for x,y in zip(rel[r]['weight'],p[:9])) for (r,p) in sy['d']}
        check(len(weights)==1,'source_second_relations_homogeneous',j)
        sy['weight']=next(iter(weights))
    return {'generators':SHORT_ORDER,'relations':rel,'syzygies':syzy,
            'd0':d0,'d1':d1,'d2':{j:s['d'] for j,s in enumerate(syzy)}}


def target_component(M, weight, label):
    """Exact multidegree, no occurrence or regulator power cutoff."""
    coeff={}
    for j,(F,H,e) in enumerate(M.states):
        p=list(weight)+[0]
        for a in F:p[DIAGONALS.index(a)]+=1
        for a in H:p[DIAGONALS.index(a)]-=1
        p[DIAGONALS.index(M.occurrence)]-=e
        if min(p)<0 or not survives(tuple(p)) or not conductor_order(tuple(p)):continue
        coeff[j]=tuple(p)
    d={j:{} for j in coeff}
    for j,p in coeff.items():
        for (i,q),s in M.d[j].items():
            pp=tuple(x+y for x,y in zip(p,q))
            if survives(pp):
                check(i in coeff and pp[:9]==coeff[i][:9], 'arbitrary_source_weight_target_closure',(label,j,i))
                check(pp[9]==M.weight[j]-M.weight[i], 'arbitrary_source_weight_regulator_degree',(label,j,i))
                put(d[j],i,s)
    ker=full_endpoint_q_kernel(M,coeff,d,label)
    cols=[];ids=[]
    for j in sorted(ker['ids']):
        if M.degree[j]!=4 or M.weight[j]>3:continue
        v={}
        for i,c in ker['inclusion'][j].items():
            pp=list(coeff[i]);pp[9]=3-M.weight[i]
            v[(i,tuple(pp))]=c
        cols.append(v);ids.append(j)
    return {'coeff':coeff,'d':d,'kernel':ker,'ids':ids,'cols':cols}


def unit_kernel(columns, variables=None, label=''):
    """Integer kernel using only unimodular pivots; export every pivot.

    A complete unit-pivot reduction also certifies a saturated image.
    No rational nullspace or prime-only rank test is substituted for it.
    """
    variables=sorted(columns) if variables is None else sorted(variables)
    rows={}
    for j in variables:
        for i,v in columns[j].items():put(rows.setdefault(i,{}),j,v)
    rows={i:row for i,row in rows.items() if row}
    original={i:dict(row) for i,row in rows.items()}
    piv=[]
    while rows:
        degrees=Counter(j for row in rows.values() for j in row)
        options=[(len(row)*degrees[j],len(row),repr(i),j,i)
                 for i,row in rows.items() for j,v in row.items() if abs(v)==1]
        check(bool(options),'all_source_equation_pivots_are_units',label)
        _,_,_,j,i=min(options)
        row=rows.pop(i);v=row[j]
        norm={k:z*v for k,z in row.items()}
        piv.append((j,norm))
        for ii,rr in list(rows.items()):
            z=rr.get(j)
            if z:
                rows[ii]=add(rr,norm,-z)
                if not rows[ii]:del rows[ii]
    free=[j for j in variables if j not in {p[0] for p in piv}]
    basis=[]
    for j in free:
        v={j:1}
        for p,row in reversed(piv):
            value=-sum(a*v.get(k,0) for k,a in row.items() if k!=p)
            put(v,p,value)
        for row in original.values():
            check(sum(z*v.get(j,0) for j,z in row.items())==0,'kernel_vector_solves_all_equations',label)
        check(all(v.get(k,0)==int(k==j) for k in free),'kernel_free_coordinates_identity',label)
        basis.append(v)
    return {'rank':len(piv),'free':free,'basis':basis,'pivots':piv,'rows':original}


def dense_kernel(columns,label):
    ids=sorted(columns);rows=sorted({i for c in columns.values() for i in c},key=repr)
    matrix=[[columns[j].get(i,0) for j in ids] for i in rows]
    red=integer_diagonalize(matrix,label)
    basis=[{ids[i]:red['right'][i][j] for i in range(len(ids)) if red['right'][i][j]}
           for j in range(red['rank'],len(ids))]
    for v in basis:check(not int_apply(columns,v),'dense_integer_kernel_check',label)
    return {'basis':basis,'reduction':red,'rank':red['rank']}


def sparse_list(v):
    return [[k,z] for k,z in sorted(v.items(),key=lambda item:repr(item[0]))]




# ---------- New calculation: extend conductor maps across normalization units ----------
import contextlib
import io
import tempfile


def extension_component(M, degree, occurrence_weight, conductor=False):
    """All monomial cochains of occurrence degree zero and regulator grade 3."""
    result=[]
    for j,(F,H,e) in enumerate(M.states):
        if M.degree[j]!=degree:
            continue
        p=list(occurrence_weight)+[3-len(H)]
        for a in F:p[DIAGONALS.index(a)]+=1
        for a in H:p[DIAGONALS.index(a)]-=1
        p[DIAGONALS.index(M.occurrence)]-=e
        p=tuple(p)
        if min(p)<0 or not survives(p) or (conductor and conductor_order(p)==0):
            continue
        result.append({(j,p):1})
    return result


def extension_deserialize_maps(entries, relation_index):
    result={}
    for entry in entries:
        key=(('Y',entry['source']) if entry['source_type']=='generator'
             else ('V',relation_index[tuple(entry['source'])]))
        result[key]={(v['state_index'],tuple(v['exponents'])):v['integer']
                     for v in entry['image']}
    return result


def extension_flat(mapping):
    return {(kind,s,j,p):c for (kind,s),chain in mapping.items()
            for (j,p),c in chain.items()}


def extension_pack_flat(mapping):
    result={}
    for (kind,s,j,p),c in mapping.items():
        put(result.setdefault((kind,s),{}),(j,p),c)
    return {key:chain for key,chain in result.items() if chain}


def extension_serialize_maps(mapping,M,relations):
    return [{'source_type':'generator' if kind=='Y' else 'first_relation',
             'source':s if kind=='Y' else list(relations[s]['name']),
             'image':serialize_chain(chain,M)}
            for (kind,s),chain in sorted(mapping.items(),key=lambda kv:repr(kv[0])) if chain]


def extension_inverse_left(reduction):
    """Invert the recorded unimodular row operations, without rational arithmetic."""
    A=dense_identity(len(reduction['left']))
    for op in reversed(reduction['operations']):
        if op[0]=='row_swap':
            i,j=op[1:];A[i],A[j]=A[j],A[i]
        elif op[0]=='row_add':
            i,j,c=op[1:];A[i]=[x-c*y for x,y in zip(A[i],A[j])]
        elif op[0]=='row_negate':
            i=op[1];A[i]=[-x for x in A[i]]
    check(dense_product(A,reduction['left'])==dense_identity(len(A)),
          'extension_unimodular_row_inverse')
    check(dense_product(reduction['left'],A)==dense_identity(len(A)),
          'extension_unimodular_row_inverse_both_sides')
    return A


def extension_verify_source_map(mapping,M,source,label):
    for a in SHORT_ORDER:
        chain=mapping.get(('Y',a),{})
        check(not apply(M.d,chain),'extension_map_generator_closed',(label,a))
    for j,r in enumerate(source['relations']):
        rhs={}
        for a,ps in r['d'].items():
            for p,z in ps.items():rhs=add(rhs,multiply(mapping.get(('Y',a),{}),p,z))
        check(apply(M.d,mapping.get(('V',j),{}))==rhs,
              'extension_map_relation_equation',(label,j))
    for j,s in enumerate(source['syzygies']):
        rhs={}
        for (r,p),z in s['d'].items():rhs=add(rhs,multiply(mapping.get(('V',r),{}),p,z))
        check(not rhs,'extension_map_second_relation_equation',(label,j))


def extension_homotopy_boundary(a,chain,M,relations):
    result={('Y',a):apply(M.d,chain)}
    for j,r in enumerate(relations):
        col={}
        for p,z in r['d'].get(a,{}).items():col=add(col,multiply(chain,p,z))
        if col:result['V',j]=col
    return extension_flat(result)


def extension_kernel_record(result):
    return {'rank':result['rank'],'free_columns':result.get('free'),
            'basis':[sparse_list(v) for v in result['basis']],
            'row_labels':[list(k) for k in sorted(result.get('rows',{}),key=repr)],
            'rows':[sparse_list(result['rows'][k]) for k in sorted(result.get('rows',{}),key=repr)],
            'pivots':[[j,sparse_list(row)] for j,row in result.get('pivots',[])]}





# ---------- New: the complete Milnor square and conductor costalk ----------

class CostalkAudit:
    """Hom_R(P_A[2], N_ext), with all required source syzygies retained."""
    def __init__(self, model, source):
        self.M=model; self.source=source; self.cache={}
        self.weights={('unit',0):(0,)*9}
        self.degrees={('unit',0):2}
        self.d={('unit',0):{}}
        for a in SHORT_ORDER:
            key=('generator',a)
            self.weights[key]=monomial('X'+a)[:9]; self.degrees[key]=3
            self.d[key]={(('unit',0),monomial('X'+a)):1}
        for j,r in enumerate(source['relations']):
            key=('relation',j)
            self.weights[key]=r['weight'];self.degrees[key]=4
            self.d[key]={(('generator',a),p):z for a,ps in r['d'].items() for p,z in ps.items()}
        for j,r in enumerate(source['syzygies']):
            key=('syzygy',j)
            self.weights[key]=r['weight'];self.degrees[key]=5
            self.d[key]={(('relation',a),p):z for (a,p),z in r['d'].items()}
        self.keys=list(self.weights)
        for key,col in self.d.items():
            out={}
            for (a,p),z in col.items():
                for (bb,q),c in self.d[a].items():
                    pq=tuple(x+y for x,y in zip(p,q))
                    if survives(pq):put(out,(bb,pq),z*c)
            check(not out,'new_residue_resolution_d_squared',key)
            for (a,p),z in col.items():
                check(self.degrees[a]==self.degrees[key]-1,'new_residue_resolution_degree',key)
                check(tuple(x+y for x,y in zip(self.weights[a],p[:9]))==self.weights[key],
                      'new_residue_resolution_occurrence_weight',key)
        self.ri={r['name']:j for j,r in enumerate(source['relations'])}

    def target_basis(self, degree, weight, conductor=False):
        key=(degree,weight,conductor)
        if key in self.cache:return self.cache[key]
        raw=extension_component(self.M,degree,weight,conductor)
        cols={j:{('value',i,p):z for (i,p),z in v.items() if i in self.M.V|self.M.Q}
              for j,v in enumerate(raw)}
        for j,v in enumerate(raw):
            for (i,p),z in apply(self.M.d,v).items():
                if i in self.M.V:put(cols[j],('incoming_endpoint',i,p),z)
        ker=unit_kernel(cols,label=('costalk_target_frame',key))
        ans=[self.linear_combination(raw,co) for co in ker['basis']]
        for v in ans:
            check(not restrict(v,self.M.V|self.M.Q),'new_target_full_endpoint_Q_zero')
            check(not restrict(apply(self.M.d,v),self.M.V),'new_target_incoming_endpoint_zero')
            for (j,p),z in v.items():
                check(self.M.degree[j]==degree and p[9]+self.M.weight[j]==3,
                      'new_target_complete_grade')
        self.cache[key]=ans
        return ans

    @staticmethod
    def linear_combination(basis, coordinates):
        out={}
        for j,z in coordinates.items():out=add(out,basis[j],z)
        return out

    def mapping_basis(self, n, conductor=False):
        return [(a,v) for a in self.keys
                for v in self.target_basis(self.degrees[a]+n,self.weights[a],conductor)]

    def differential_column(self,a,v,n,model=None):
        model=model or self.M
        out={(a,i,p):z for (i,p),z in apply(model.d,v).items()}
        for key,col in self.d.items():
            for (t,p),z in col.items():
                if t==a:
                    for (i,q),c in multiply(v,p,-sign(n)*z).items():put(out,(key,i,q),c)
        return out

    def mapping_differential(self, mapping,n,model=None):
        grouped={}
        for (a,i,p),z in mapping.items():put(grouped.setdefault(a,{}),(i,p),z)
        out={}
        for a,v in grouped.items():out=add(out,self.differential_column(a,v,n,model))
        return out

    def verify_map(self,mapping,label,model=None):
        model=model or self.M
        check(not self.mapping_differential(mapping,0,model),'new_full_costalk_map_equation',label)
        grouped={}
        for (a,i,p),z in mapping.items():
            check(min(p)>=0 and survives(p),'new_costalk_polynomial_legal',(label,a))
            check(model.degree[i]==self.degrees[a],'new_costalk_map_chain_degree',(label,a))
            check(p[9]+model.weight[i]==3,'new_costalk_regulator_grade',(label,a))
            expected=list(self.weights[a])+[3-model.weight[i]]
            F,H,e=model.states[i]
            for x in F:expected[DIAGONALS.index(x)]+=1
            for x in H:expected[DIAGONALS.index(x)]-=1
            expected[DIAGONALS.index(model.occurrence)]-=e
            check(tuple(expected)==p,'new_costalk_occurrence_degree',(label,a))
            put(grouped.setdefault(a,{}),(i,p),z)
        for a,v in grouped.items():
            check(not restrict(v,model.V|model.Q),'new_costalk_complete_frame_values',(label,a))
            check(not restrict(apply(model.d,v),model.V),'new_costalk_complete_frame_incoming',(label,a))

    @staticmethod
    def selectors(basis):
        histogram={}
        for j,v in enumerate(basis):
            for a,z in v.items():histogram.setdefault(a,[]).append((j,z))
        sel={}
        for a,entries in histogram.items():
            if len(entries)==1 and abs(entries[0][1])==1:
                j,z=entries[0];sel.setdefault(j,(a,z))
        check(len(sel)==len(basis),'new_cochain_basis_has_integral_coordinate_rows')
        return sel

    def solve(self,conductor=False):
        unknown=self.mapping_basis(0,conductor)
        raw=[{(a,i,p):z for (i,p),z in v.items()} for a,v in unknown]
        cols={j:self.differential_column(a,v,0) for j,(a,v) in enumerate(unknown)}
        for j,col in cols.items():check(not self.mapping_differential(col,-1),'new_Hom_squared_zero',j)
        closed=unit_kernel(cols,label=('complete_conductor_costalk_cycles',conductor))
        maps=[self.linear_combination(raw,co) for co in closed['basis']]
        for j,F in enumerate(maps):self.verify_map(F,('closed',conductor,j))
        selectors=self.selectors(raw)
        def coordinates(F):
            co={j:F.get(a,0)*z for j,(a,z) in selectors.items() if F.get(a,0)}
            check(self.linear_combination(raw,co)==F,'new_costalk_cochain_coordinates')
            cc={j:co.get(k,0) for j,k in enumerate(closed['free']) if co.get(k,0)}
            check(self.linear_combination(maps,cc)==F,'new_costalk_closed_coordinates')
            return cc
        hom=self.mapping_basis(1,conductor)
        dh=[self.differential_column(a,v,1) for a,v in hom]
        for j,F in enumerate(dh):self.verify_map(F,('boundary',conductor,j))
        dhc=[coordinates(F) for F in dh]
        matrix=dense_columns([[v.get(i,0) for i in range(len(maps))] for v in dhc],len(maps))
        reduction=integer_diagonalize(matrix,('complete_costalk_homotopy_image',conductor))
        check(reduction['diagonal']==[1]*len(hom),'new_all_costalk_homotopy_pivots_primitive',conductor)
        check(not self.mapping_basis(2,conductor),'new_no_higher_costalk_homotopies',conductor)
        inverse=extension_inverse_left(reduction)
        reps=[{i:inverse[i][k] for i in range(len(inverse)) if inverse[i][k]}
              for k in range(reduction['rank'],len(inverse))]
        qmaps=[self.linear_combination(maps,c) for c in reps]
        def quotient_coordinates(F):
            c=coordinates(F)
            return [sum(row[i]*z for i,z in c.items()) for row in reduction['left'][reduction['rank']:]]
        for j,F in enumerate(qmaps):
            check(quotient_coordinates(F)==[int(i==j) for i in range(len(qmaps))],
                  'new_costalk_quotient_basis_identity')
        for F in dh:check(not any(quotient_coordinates(F)),'new_costalk_boundaries_zero_in_quotient')
        expected=(664,54,0,54) if conductor else (718,108,74,34)
        check((len(unknown),len(maps),len(hom),len(qmaps))==expected,
              'new_complete_costalk_dimensions',conductor)
        return dict(unknown=unknown,raw=raw,columns=cols,closed=closed,maps=maps,
                    hom=hom,dh=dh,dhc=dhc,reduction=reduction,inverse=inverse,
                    representatives=reps,qmaps=qmaps,coordinates=coordinates,
                    quotient_coordinates=quotient_coordinates)

    def transform(self,mapping,rot=0,ref=1):
        grouped={}
        for (a,j,p),z in mapping.items():put(grouped.setdefault(a,{}),(j,p),z)
        out={}
        for a,v in grouped.items():
            sg=1
            if a[0]=='unit':dest=a
            elif a[0]=='generator':dest=('generator',polygon_diagonal(a[1],rot,ref))
            elif a[0]=='relation':
                typ,i,j=self.source['relations'][a[1]]['name']
                ii=polygon_diagonal(i,rot,ref);jj=polygon_diagonal(j,rot,ref)
                if typ=='K' and ii>jj:ii,jj,sg=jj,ii,-1
                dest=('relation',self.ri[typ,ii,jj])
            else:raise ValueError(a)
            for (j,p),z in polygon_action(self.M,v,rot,ref).items():put(out,(dest,j,p),z*sg)
        return out

    def serialize_map(self,F):
        grouped={}
        for (a,j,p),z in F.items():put(grouped.setdefault(a,{}),(j,p),z)
        return [{'source_type':a[0],
                 'source':list(self.source['relations'][a[1]]['name']) if a[0]=='relation' else a[1],
                 'image':serialize_chain(v,self.M)}
                for a,v in sorted(grouped.items(),key=lambda kv:repr(kv[0]))]

    def record_solve(self,data):
        return {
            'unknowns':[{'source':list(a),'image':serialize_chain(v,self.M)} for a,v in data['unknown']],
            'closed_equations':extension_kernel_record(data['closed']),
            'closed_map_basis':[self.serialize_map(F) for F in data['maps']],
            'homotopy_basis':[{'source':list(a),'image':serialize_chain(v,self.M)} for a,v in data['hom']],
            'homotopy_boundary_coordinates':[sparse_list(v) for v in data['dhc']],
            'boundary_integral_reduction':data['reduction'],
            'quotient_basis':[self.serialize_map(F) for F in data['qmaps']],
            'quotient_representative_coordinates':[sparse_list(v) for v in data['representatives']]}


def milnor_square_exactness():
    """Exactness in every monomial support type; exponents do not matter."""
    j=[[1],[1],[1]]
    t=[[1,0,-1],[0,1,-1]]
    check(dense_product(t,j)==[[0],[0]],'new_Milnor_constant_composition')
    kr=unit_kernel({i:{k:row[i] for k,row in enumerate(t) if row[i]} for i in range(3)},
                   label='Milnor_constant_kernel')
    check(kr['basis']==[{2:1,1:1,0:1}], 'new_Milnor_constant_kernel_diagonal')
    check(t[0][0]*t[1][1]-t[0][1]*t[1][0]==1,'new_Milnor_quotient_surjective')
    cases=[]
    for n in range(7):
        for support in combinations(SHORT_ORDER,n):
            if not support:typ='constant';ranks=[1,3,2]
            elif set(support)<=PLUS:typ='positive';ranks=[1,1,0]
            elif set(support)<=MINUS:typ='negative';ranks=[1,1,0]
            else:typ='zero_mixed';ranks=[0,0,0]
            check((typ=='zero_mixed')==not_survives_support(support),
                  'new_Milnor_all_monomial_types',support)
            cases.append({'short_support':list(support),'type':typ,'ranks':ranks})
    check(Counter(c['type'] for c in cases)=={'constant':1,'positive':7,'negative':7,'zero_mixed':49},
          'new_Milnor_complete_support_normal_forms')
    # The conductor diagonal makes the square a pullback; its cokernel is the
    # ordered difference, not a chosen half-difference.
    diagonal=[[1],[1]];difference=[[1,-1]]
    check(dense_product(difference,diagonal)==[[0]],'new_Milnor_diagonal_difference')
    check(difference[0][0]==1,'new_Milnor_difference_primitive')
    return {'constant_augmentation':j,'constant_difference_matrix':t,
            'monomial_support_cases':cases,'diagonal':diagonal,'ordered_difference':difference,
            'homological_totalization_degrees':[0,-1],
            'quasi_isomorphism':'R -> [tilde_R direct-sum A -> A direct-sum A]',
            'R_linear_split_not_claimed':True}


def not_survives_support(support):
    return bool(set(support)&PLUS and set(support)&MINUS)


def costalk_target_primary(audit):
    """Entire fixed-degree H2(N_ext), including the counit's codomain."""
    c2=audit.target_basis(2,(0,)*9)
    c3=audit.target_basis(3,(0,)*9)
    closed=unit_kernel({j:apply(audit.M.d,v) for j,v in enumerate(c2)},label='new_target_primary_cycles')
    cs=[audit.linear_combination(c2,co) for co in closed['basis']]
    sel=audit.selectors(c2)
    def coordinates(v):
        co={j:v.get(k,0)*z for j,(k,z) in sel.items() if v.get(k,0)}
        check(audit.linear_combination(c2,co)==v,'new_primary_cochain_coordinates')
        cc=[co.get(k,0) for k in closed['free']]
        check(audit.linear_combination(cs,{j:z for j,z in enumerate(cc) if z})==v,
              'new_primary_cycle_coordinates')
        return cc
    d3=[coordinates(apply(audit.M.d,v)) for v in c3]
    reduction=integer_diagonalize(dense_columns(d3,len(cs)),'new_primary_boundary_lattice')
    check((len(cs),len(c3),reduction['rank'])==(46,41,41),'new_primary_cycle_and_boundary_ranks')
    check(reduction['diagonal']==[1]*41,'new_primary_homology_torsion_free')
    def quotient(v):
        cc=coordinates(v)
        return [sum(x*y for x,y in zip(row,cc)) for row in reduction['left'][41:]]
    check(not audit.target_basis(4,(0,)*9),'new_totalization_source_no_positive_map_homotopies')
    # d3 has rank equal to the whole degree-three group.
    check(len(c3)==reduction['rank'],'new_H3_framed_target_zero')
    return dict(c2=c2,c3=c3,closed=closed,cycles=cs,d3=d3,reduction=reduction,
                coordinates=coordinates,quotient=quotient)





# New calculation: all regulator grades, exact multiplication, and nonzero-beta continuation.
import sys
from math import gcd
b = sys.modules[__name__]



class RegulatorCostalkAudit(b.CostalkAudit):
    def __init__(self,model,source,grade):
        self.grade=grade
        super().__init__(model,source)
    def target_basis(self,degree,weight,conductor=False):
        key=(degree,weight,conductor)
        if key in self.cache:return self.cache[key]
        raw=[]
        for j,(F,H,e) in enumerate(self.M.states):
            if self.M.degree[j]!=degree:continue
            p=list(weight)+[self.grade-len(H)]
            for a in F:p[b.DIAGONALS.index(a)]+=1
            for a in H:p[b.DIAGONALS.index(a)]-=1
            p[b.DIAGONALS.index(self.M.occurrence)]-=e
            p=tuple(p)
            if min(p)<0 or not b.survives(p) or (conductor and b.conductor_order(p)==0):continue
            raw.append({(j,p):1})
        cols={j:{('value',i,p):z for (i,p),z in v.items() if i in self.M.V|self.M.Q} for j,v in enumerate(raw)}
        for j,v in enumerate(raw):
            for (i,p),z in b.apply(self.M.d,v).items():
                if i in self.M.V:b.put(cols[j],('incoming_endpoint',i,p),z)
        ker=b.unit_kernel(cols,label=('beta_costalk_target_frame',self.grade,key))
        ans=[self.linear_combination(raw,co) for co in ker['basis']]
        for v in ans:
            assert not b.restrict(v,self.M.V|self.M.Q)
            assert not b.restrict(b.apply(self.M.d,v),self.M.V)
            assert all(self.M.degree[j]==degree and p[9]+self.M.weight[j]==self.grade for (j,p),z in v.items())
        self.cache[key]=ans
        return ans
    def verify_map(self,mapping,label,model=None):
        model=model or self.M
        assert not self.mapping_differential(mapping,0,model),(label,'chain')
        grouped={}
        for (a,i,p),z in mapping.items():
            assert min(p)>=0 and b.survives(p)
            assert model.degree[i]==self.degrees[a]
            assert p[9]+model.weight[i]==self.grade,(label,'grade',p,self.grade)
            expected=list(self.weights[a])+[self.grade-model.weight[i]]
            F,H,e=model.states[i]
            for x in F:expected[b.DIAGONALS.index(x)]+=1
            for x in H:expected[b.DIAGONALS.index(x)]-=1
            expected[b.DIAGONALS.index(model.occurrence)]-=e
            assert tuple(expected)==p
            b.put(grouped.setdefault(a,{}),(i,p),z)
        for a,v in grouped.items():
            assert not b.restrict(v,model.V|model.Q)
            assert not b.restrict(b.apply(model.d,v),model.V)

    def solve(self,conductor=False):
        unknown=self.mapping_basis(0,conductor)
        raw=[{(a,i,p):z for (i,p),z in v.items()} for a,v in unknown]
        cols={j:self.differential_column(a,v,0) for j,(a,v) in enumerate(unknown)}
        for j,col in cols.items():check(not self.mapping_differential(col,-1),'new_Hom_squared_zero',j)
        closed=unit_kernel(cols,label=('complete_conductor_costalk_cycles',conductor))
        maps=[self.linear_combination(raw,co) for co in closed['basis']]
        for j,F in enumerate(maps):self.verify_map(F,('closed',conductor,j))
        selectors=self.selectors(raw)
        def coordinates(F):
            co={j:F.get(a,0)*z for j,(a,z) in selectors.items() if F.get(a,0)}
            check(self.linear_combination(raw,co)==F,'new_costalk_cochain_coordinates')
            cc={j:co.get(k,0) for j,k in enumerate(closed['free']) if co.get(k,0)}
            check(self.linear_combination(maps,cc)==F,'new_costalk_closed_coordinates')
            return cc
        hom=self.mapping_basis(1,conductor)
        dh=[self.differential_column(a,v,1) for a,v in hom]
        for j,F in enumerate(dh):self.verify_map(F,('boundary',conductor,j))
        dhc=[coordinates(F) for F in dh]
        matrix=dense_columns([[v.get(i,0) for i in range(len(maps))] for v in dhc],len(maps))
        reduction=integer_diagonalize(matrix,('complete_costalk_homotopy_image',conductor))
        check(reduction['diagonal']==[1]*len(hom),'new_all_costalk_homotopy_pivots_primitive',conductor)
        check(not self.mapping_basis(2,conductor),'new_no_higher_costalk_homotopies',conductor)
        inverse=extension_inverse_left(reduction)
        reps=[{i:inverse[i][k] for i in range(len(inverse)) if inverse[i][k]}
              for k in range(reduction['rank'],len(inverse))]
        qmaps=[self.linear_combination(maps,c) for c in reps]
        def quotient_coordinates(F):
            c=coordinates(F)
            return [sum(row[i]*z for i,z in c.items()) for row in reduction['left'][reduction['rank']:]]
        for j,F in enumerate(qmaps):
            check(quotient_coordinates(F)==[int(i==j) for i in range(len(qmaps))],
                  'new_costalk_quotient_basis_identity')
        for F in dh:check(not any(quotient_coordinates(F)),'new_costalk_boundaries_zero_in_quotient')
        return dict(unknown=unknown,raw=raw,columns=cols,closed=closed,maps=maps,
                    hom=hom,dh=dh,dhc=dhc,reduction=reduction,inverse=inverse,
                    representatives=reps,qmaps=qmaps,coordinates=coordinates,
                    quotient_coordinates=quotient_coordinates)

def primary(audit):
    c2=audit.target_basis(2,(0,)*9);c3=audit.target_basis(3,(0,)*9)
    closed=b.unit_kernel({j:b.apply(audit.M.d,v) for j,v in enumerate(c2)},label=('target_primary',audit.grade))
    cycles=[audit.linear_combination(c2,co) for co in closed['basis']]
    sel=audit.selectors(c2)
    def coordinates(v):
        co={j:v.get(k,0)*z for j,(k,z) in sel.items() if v.get(k,0)}
        assert audit.linear_combination(c2,co)==v
        cc=[co.get(k,0) for k in closed['free']]
        assert audit.linear_combination(cycles,{j:z for j,z in enumerate(cc) if z})==v
        return cc
    d3=[coordinates(b.apply(audit.M.d,v)) for v in c3]
    red=b.integer_diagonalize(b.dense_columns(d3,len(cycles)),('primary_boundary',audit.grade))
    assert red['diagonal']==[1]*red['rank']
    inv=b.extension_inverse_left(red)
    qcycles=[audit.linear_combination(cycles,{j:inv[j][k] for j in range(len(cycles)) if inv[j][k]}) for k in range(red['rank'],len(cycles))]
    def quotient(v):
        cc=coordinates(v)
        return [sum(x*y for x,y in zip(row,cc)) for row in red['left'][red['rank']:]]
    return dict(c2=c2,c3=c3,cycles=cycles,closed=closed,reduction=red,quotient=quotient,qcycles=qcycles)

def beta_F(F):
    return {(a,i,p[:9]+(p[9]+1,)):z for (a,i,p),z in F.items()}
def unit_image(F):return {(i,p):z for (a,i,p),z in F.items() if a==('unit',0)}

def shift_beta_map(F, power=1):
    return {(a,j,p[:9]+(p[9]+power,)):z for (a,j,p),z in F.items()}


def beta_matrix(data0,data1):
    return dense_columns([data1['quotient_coordinates'](shift_beta_map(F))
                          for F in data0['qmaps']],len(data1['qmaps']))


def image_coordinates(basis,vector,label):
    red=integer_diagonalize(basis,label)
    check(red['diagonal']==[1]*red['rank'],'continuation_integral_image_basis',label)
    vv=[sum(x*y for x,y in zip(row,vector)) for row in red['left']]
    check(not any(vv[red['rank']:]),'continuation_vector_in_image',label)
    return [sum(red['right'][i][j]*vv[j] for j in range(red['rank']))
            for i in range(len(red['right']))]


def primitive_for_target(target,pr,audit,label):
    sel=audit.selectors(pr['c2'])
    co={j:target.get(a,0)*z for j,(a,z) in sel.items() if target.get(a,0)}
    check(audit.linear_combination(pr['c2'],co)==target,'continuation_primitive_target_coordinates',label)
    cc=[co.get(k,0) for k in pr['closed']['free']]
    rr=pr['reduction']
    yy=[sum(x*y for x,y in zip(row,cc)) for row in rr['left']]
    check(not any(yy[rr['rank']:]),'continuation_primitive_exists',label)
    hc=[sum(rr['right'][i][j]*yy[j] for j in range(rr['rank'])) for i in range(len(rr['right']))]
    H=audit.linear_combination(pr['c3'],{j:z for j,z in enumerate(hc) if z})
    check(apply(audit.M.d,H)==target,'continuation_primitive_exact_equation',label)
    check(not restrict(H,audit.M.V|audit.M.Q),'continuation_primitive_frame',label)
    return H


def simplify_primary_record(pr,M):
    return {'degree2_frame_basis':[serialize_chain(v,M) for v in pr['c2']],
            'degree3_frame_basis':[serialize_chain(v,M) for v in pr['c3']],
            'cycle_kernel':extension_kernel_record(pr['closed']),
            'cycle_basis':[serialize_chain(v,M) for v in pr['cycles']],
            'boundary_reduction':pr['reduction'],
            'homology_representatives':[serialize_chain(v,M) for v in pr['qcycles']]}


def evaluate_beta_one(F):
    out={}
    for (a,j,p),z in F.items():put(out,(a,j,p[:9]+(0,)),z)
    return out


def transport_native(chain,M,power_sign=1):
    out={}
    for (j,p),z in chain.items():put(out,(j,p[:9]+(p[9]+power_sign*M.weight[j],)),z)
    return out


def verify_nonzero_regulator_frame(audits,data):
    M=audits[3].M
    M1=Complex()
    M1.d={j:{} for j in range(430)}
    for j,col in M.d.items():
        for (i,p),z in col.items():put(M1.d[j],(i,p[:9]+(0,)),z)
    for j in range(430):
        check(not apply(M1.d,M1.d[j]),'continuation_beta_one_full_d_squared',j)
        check(apply(M1.d,transport_native(unit(j),M))==transport_native(M.d[j],M),
              'continuation_all_state_normal_conjugacy',j)
        check(transport_native(transport_native(unit(j),M),M,-1)==unit(j),
              'continuation_laurent_inverse_only_beta',j)
    for g in range(5):
        au=audits[g]
        for n,basis in [(0,[(a,v) for a,v in data[g]['unknown']]),(1,data[g]['hom'])]:
            for k,(a,v) in enumerate(basis):
                vv=transport_native(v,M)
                expected={(j,p[:9]+(g,)):z for (j,p),z in v.items()}
                check(vv==expected,'continuation_homogeneous_conjugacy_factor',(g,n,k))
        for k,F in enumerate(data[g]['qmaps']):
            one=evaluate_beta_one(F)
            check(not au.mapping_differential(one,0,M1),'continuation_all_localized_costalk_maps',(g,k))
            grouped={}
            for (a,j,p),z in one.items():put(grouped.setdefault(a,{}),(j,p),z)
            for a,v in grouped.items():
                check(not restrict(v,M.V|M.Q),'continuation_localized_full_frame_values',(g,k,a))
                check(not restrict(apply(M1.d,v),M.V),'continuation_localized_endpoint_attachments',(g,k,a))
    return {'only_inverted_parameter':'beta','native_mark_scaling':'beta^|H|',
            'occurrence_partner_unchanged':True,'all_430_chain_equations_verified':True,
            'beta_one_differential':serialize_full_matrix(M1.d)}


def main_regulator_continuation(output):
    COUNTS.clear()
    M=Complex();source=source_resolution()
    audits={};data={};prim={};cm={};tables=[]
    expected={0:(21,1,1,0,0,0),1:(206,17,16,1,3,1),2:(550,66,50,16,17,6),
              3:(718,108,74,34,5,3),4:(718,108,74,34,5,3)}
    for g in range(5):
        au=RegulatorCostalkAudit(M,source,g);dd=au.solve();pp=primary(au)
        audits[g]=au;data[g]=dd;prim[g]=pp
        c=dense_columns([pp['quotient'](unit_image(F)) for F in dd['qmaps']],len(pp['qcycles']))
        cr=integer_diagonalize(c,('regulator_counit',g));cm[g]=(c,cr)
        dims=(len(dd['unknown']),len(dd['maps']),len(dd['hom']),len(dd['qmaps']),len(pp['qcycles']),cr['rank'])
        check(dims==expected[g],'continuation_complete_grade_dimensions',g)
        check(cr['diagonal']==[1]*cr['rank'],'continuation_counit_image_saturated',g)
        tables.append({'regulator_grade':g,'cochain_unknowns':dims[0],'closed_cochains':dims[1],
          'boundaries':dims[2],'costalk_classes':dims[3],'target_H2_rank':dims[4],
          'counit_rank':dims[5],'counit_kernel_rank':dims[3]-dims[5]})

    # Check exact repetition of the complete Hom matrices once every native mark is present.
    check(max(M.weight.values())==3,'continuation_global_native_degree_bound')
    for n in (-1,0,1,2):
        bas3=audits[3].mapping_basis(n);bas4=audits[4].mapping_basis(n)
        check(len(bas3)==len(bas4),'continuation_stable_full_cochain_dimensions',n)
        for k,((a,v),(aa,vv)) in enumerate(zip(bas3,bas4)):
            check(a==aa and multiply(v,monomial('beta'))==vv,'continuation_stable_cochain_basis',(n,k))
            check(shift_beta_map(audits[3].differential_column(a,v,n))
                  ==audits[4].differential_column(aa,vv,n),
                  'continuation_stable_Hom_differential',(n,k))
    # Negative regulator grades have no legal polynomial entries.
    neg=RegulatorCostalkAudit(M,source,-1)
    for n in (-1,0,1):check(not neg.mapping_basis(n),'continuation_no_negative_grade_cochains',n)

    bm={};pbm={};transitions={};ibs={};kbs={};coker_reps={}
    for g in range(5):
        c,cr=cm[g];rank=cr['rank'];n=len(data[g]['qmaps']);h=len(prim[g]['qcycles'])
        kbs[g]=[row[rank:] for row in cr['right']]
        ibs[g]=dense_product(c,[row[:rank] for row in cr['right']])
        li=extension_inverse_left(cr)
        coker_reps[g]=[row[rank:] for row in li]
    for g in range(4):
        bm[g]=beta_matrix(data[g],data[g+1])
        br=integer_diagonalize(bm[g],('beta_costalk',g))
        check(br['rank']==len(data[g]['qmaps']) and br['diagonal']==[1]*br['rank'],
              'continuation_beta_costalk_injective_saturated',g)
        pbm[g]=dense_columns([prim[g+1]['quotient'](multiply(F,monomial('beta')))
                             for F in prim[g]['qcycles']],len(prim[g+1]['qcycles']))
        pbr=integer_diagonalize(pbm[g],('beta_target',g))
        check(pbr['diagonal']==[1]*pbr['rank'],'continuation_beta_target_saturated',g)
        check(dense_product(cm[g+1][0],bm[g])==dense_product(pbm[g],cm[g][0]),
              'continuation_counit_commutes_with_beta',g)
        # Track the kernel, image, and cokernel as modules, not independent rank counts.
        kcols=dense_product(bm[g],kbs[g])
        km=dense_columns([image_coordinates(kbs[g+1],[row[j] for row in kcols],('kernel_beta',g,j))
                         for j in range(len(kcols[0]) if kcols else 0)],
                         len(kbs[g+1][0]) if kbs[g+1] else 0)
        kr=integer_diagonalize(km,('kernel_beta',g))
        check(kr['diagonal']==[1]*kr['rank'],'continuation_kernel_beta_saturated',g)
        icols=dense_product(pbm[g],ibs[g])
        im=dense_columns([image_coordinates(ibs[g+1],[row[j] for row in icols],('image_beta',g,j))
                         for j in range(len(icols[0]) if icols else 0)],cm[g+1][1]['rank'])
        ir=integer_diagonalize(im,('image_beta',g))
        check(ir['diagonal']==[1]*ir['rank'],'continuation_image_beta_saturated',g)
        cokcols=dense_product(pbm[g],coker_reps[g])
        cqm=dense_product(cm[g+1][1]['left'][cm[g+1][1]['rank']:],cokcols)
        cqr=integer_diagonalize(cqm,('cokernel_beta',g))
        check(cqr['diagonal']==[1]*cqr['rank'],'continuation_cokernel_beta_saturated',g)
        transitions[g]={'costalk_matrix':bm[g],'costalk_reduction':br,
          'target_matrix':pbm[g],'target_reduction':pbr,
          'kernel_matrix':km,'kernel_reduction':kr,
          'image_matrix':im,'image_reduction':ir,
          'cokernel_matrix':cqm,'cokernel_reduction':cqr}
    for name,mat,rank in [('target',dense_product(pbm[2],pbm[1]),3),
                         ('image',dense_product(transitions[2]['image_matrix'],transitions[1]['image_matrix']),1),
                         ('cokernel',dense_product(transitions[2]['cokernel_matrix'],transitions[1]['cokernel_matrix']),2)]:
        rr=integer_diagonalize(mat,('two_step_persistence',name))
        check(rr['diagonal']==[1]*rank,'continuation_two_step_persistence',name)
    check([transitions[g]['image_reduction']['rank'] for g in range(4)]==[0,1,3,3],
          'continuation_primary_image_persistence_ranks')
    check([transitions[g]['cokernel_reduction']['rank'] for g in range(4)]==[0,2,2,2],
          'continuation_primary_cokernel_persistence_ranks')

    # Explicit homogeneous free basis for all regulator degrees of the costalk.
    generators=[]
    for g in (1,2,3):
        red=transitions[g-1]['costalk_reduction'];li=extension_inverse_left(red)
        for k in range(red['rank'],len(data[g]['qmaps'])):
            F=audits[g].linear_combination(data[g]['qmaps'],{j:li[j][k] for j in range(len(li)) if li[j][k]})
            audits[g].verify_map(F,('free_generator',g,k))
            generators.append((g,F))
    check(Counter(g for g,F in generators)=={1:1,2:15,3:18},'continuation_free_basis_birth_degrees')
    gen_at3=[shift_beta_map(F,3-g) for g,F in generators]
    gen_matrix=dense_columns([data[3]['quotient_coordinates'](F) for F in gen_at3],34)
    gr=integer_diagonalize(gen_matrix,'continuation_complete_free_basis_grade3')
    check(gr['diagonal']==[1]*34,'continuation_free_basis_unimodular_grade3')

    # Three torsion-primary classes whose full supported maps survive beta multiplication.
    s2=integer_diagonalize(dense_product(pbm[2],cm[2][0]),'continuation_preimage_of_torsion_primary')
    torscols=dense_product(cm[2][0],[row[s2['rank']:] for row in s2['right']])
    tr=integer_diagonalize(torscols,'continuation_torsion_primary_image')
    check(tr['diagonal']==[1]*3,'continuation_three_torsion_primary_classes')
    examples=[];zero_unit_classes=[];example_maps=[]
    for k in range(3):
        co=[sum(s2['right'][i][s2['rank']+j]*tr['right'][j][k]
                for j in range(len(tr['right']))) for i in range(len(data[2]['qmaps']))]
        F=audits[2].linear_combination(data[2]['qmaps'],{j:z for j,z in enumerate(co) if z})
        audits[2].verify_map(F,('torsion_primary_example',k))
        U=unit_image(F)
        check(any(prim[2]['quotient'](U)),'continuation_primary_before_beta_nonzero',k)
        V=primitive_for_target(multiply(U,monomial('beta')),prim[3],audits[3],k)
        hom={(('unit',0),j,p):z for (j,p),z in V.items()}
        B=add(shift_beta_map(F),audits[3].mapping_differential(hom,1),-1)
        audits[3].verify_map(B,('zero_unit_secondary_example',k))
        check(not unit_image(B),'continuation_secondary_example_unit_zero',k)
        qc=data[3]['quotient_coordinates'](B)
        check(any(qc),'continuation_secondary_example_nonzero',k)
        check(gcd(*qc)==1,'continuation_secondary_example_primitive',k)
        check(qc==data[3]['quotient_coordinates'](shift_beta_map(F)),
              'continuation_secondary_example_same_supported_class',k)
        zero_unit_classes.append(qc);example_maps.append((F,V,B))
        examples.append({'index':k,'supported_map_grade2':audits[2].serialize_map(F),
          'unit_image_grade2':serialize_chain(U,M),'primary_beta_primitive_grade3':serialize_chain(V,M),
          'zero_unit_map_grade3':audits[3].serialize_map(B),'zero_unit_class_coordinates':qc,
          'term_counts':[len(F),len(U),len(V),len(B)]})
    zr=integer_diagonalize(dense_columns(zero_unit_classes,34),'continuation_secondary_triplet_independence')
    check(zr['diagonal']==[1]*3,'continuation_three_independent_secondary_transfers')

    # Reflection and full occurrence-orbit transport; no averaging.
    sym={};fixed={};sym_beta={}
    for g in (1,2,3,4):
        n=len(data[g]['qmaps'])
        SS=dense_columns([data[g]['quotient_coordinates'](audits[g].transform(F)) for F in data[g]['qmaps']],n)
        check(dense_product(SS,SS)==dense_identity(n),'continuation_reflection_squared',g)
        ff=fixed_lattice(SS,('regulator_invariants',g));fixed[g]=ff
        im=dense_product(cm[g][0],ff['kernel']);ir=integer_diagonalize(im,('invariant_counit',g))
        check(ir['diagonal']==[1]*ir['rank'],'continuation_invariant_counit_saturated',g)
        sym[g]={'reflection':SS,'fixed_basis':ff['kernel'],'fixed_rank':ff['fixed_rank'],
                'counit_matrix_on_invariants':im,'counit_reduction_on_invariants':ir}
    check([fixed[g]['fixed_rank'] for g in (1,2,3,4)]==[0,5,11,11],
          'continuation_all_invariant_grade_ranks')
    check([sym[g]['counit_reduction_on_invariants']['rank'] for g in (1,2,3,4)]==[0,2,1,1],
          'continuation_invariant_primary_ranks')
    for g in (1,2,3):
        cc=dense_product(bm[g],fixed[g]['kernel'])
        sm=dense_columns([image_coordinates(fixed[g+1]['kernel'],[row[j] for row in cc],('fixed_beta',g,j))
                         for j in range(len(cc[0]) if cc else 0)],fixed[g+1]['fixed_rank'])
        rr=integer_diagonalize(sm,('fixed_beta',g))
        check(rr['diagonal']==[1]*fixed[g]['fixed_rank'],'continuation_invariants_beta_injective_saturated',g)
        sym_beta[g]={'matrix':sm,'reduction':rr}
    F,V,B=example_maps[0]
    Finv=add(F,audits[2].transform(F));B_inv=add(B,audits[3].transform(B))
    V_inv=add(V,polygon_action(M,V,0,1))
    check(audits[2].transform(Finv)==Finv,'continuation_invariant_transfer_map')
    check(audits[3].transform(B_inv)==B_inv,'continuation_invariant_secondary_map')
    iq=data[3]['quotient_coordinates'](B_inv)
    check(any(iq) and gcd(*iq)==1,'continuation_invariant_secondary_primitive')
    check(apply(M.d,V_inv)==multiply(unit_image(Finv),monomial('beta')),
          'continuation_invariant_primary_primitive')
    orbits=[]
    for rot,occ in enumerate(('35','15','13')):
        Mr=Complex(occ);Fr=audits[3].transform(B_inv,rot,0)
        audits[3].verify_map(Fr,('invariant_secondary_orbit',occ),Mr)
        orbits.append(audits[3].serialize_map(Fr))

    localized=verify_nonzero_regulator_frame(audits,data)
    # Stable maps can neither be boundaries after localization nor be killed by any beta power.
    # This is certified by exact cochain stabilization plus the integral injective multiplication matrices.
    check(transitions[3]['costalk_reduction']['diagonal']==[1]*34,
          'continuation_stable_localized_rank34')
    record={
      'schema':'marici.branch_a.conductor_costalk_regulator_continuation.v1',
      'scope':{'ring':'Z[beta,X_d]/(X_even_short X_odd_short)',
        'source':'P_A[2], A=R/I; resolution ranks 1,6,24,92',
        'target':'N_ext={c in C_beta: q(c)=v(c)=v(dc)=0}',
        'occurrence_map_degree':0,'regulator_grades':'all integers; negative empty; grades >=3 stabilize',
        'beta_zero_geometric_purity_claimed':False,'physical_Delta_J_identified':False,
        'fixed_nonzero_beta_scope':'coefficient continuation followed by source-prescribed unit-normal comparison'},
      'sources':{'repository':'andrey-kokoev/marici','commit':COMMIT,
        'normalization':'src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md',
        'differential':'research/voevodsky/check_absolute_unlocalized_support_pc.rs',
        'purity':'research/voevodsky/check_d03_formal_support_purity.rs'},
      'full_target_differential':serialize_full_matrix(M.d),
      'table':tables,
      'grades':{str(g):{'costalk':audits[g].record_solve(data[g]),
        'target_primary':simplify_primary_record(prim[g],M),
        'counit_matrix':cm[g][0],'counit_reduction':cm[g][1]}
        for g in range(5)},
      'beta_transitions':transitions,
      'free_costalk_basis':[{'regulator_degree':g,'map':audits[g].serialize_map(F)} for g,F in generators],
      'free_basis_at_grade3_matrix':gen_matrix,'free_basis_at_grade3_reduction':gr,
      'graded_modules':{
        'costalk':{'free_births':[[1,1],[2,15],[3,18]],'beta_torsion':[]},
        'target_H2':{'free_births':[[1,3],[2,2]],'beta_torsion_birth_length_multiplicity':[[2,1,12]]},
        'counit_kernel':{'free_births':[[2,10],[3,21]],'beta_torsion':[]},
        'counit_image':{'free_births':[[1,1],[2,2]],'beta_torsion_birth_length_multiplicity':[[2,1,3]]},
        'counit_cokernel':{'free_births':[[1,2]],'beta_torsion_birth_length_multiplicity':[[2,1,9]]}},
      'primary_to_secondary_transfers':examples,
      'transfer_independence_reduction':zr,
      'symmetry':{'grades':sym,'beta_on_invariants':sym_beta,
        'invariant_secondary_map':audits[3].serialize_map(B_inv),
        'invariant_primary_primitive':serialize_chain(V_inv,M),
        'invariant_secondary_coordinates':iq,'rotated_secondary_maps':orbits,
        'generic_invariant_exact_ranks':[10,11,1],
        'invariant_free_births':[[2,5],[3,6]]},
      'nonzero_beta_comparison':localized,
      'conclusions':{'all_previous_34_classes_survive_nonzero_beta':True,
        'costalk_has_no_beta_torsion':True,'counit_image_has_three_beta_torsion_directions':True,
        'fixed_nonzero_beta_kernel_rank':31,'fixed_nonzero_beta_counit_rank':3,
        'fixed_nonzero_beta_invariant_kernel_rank':10,
        'regulator_continuation_selects_unique_physical_lift':False},
      'verification':{'counted_exact_checks':sum(COUNTS.values()),'families':dict(sorted(COUNTS.items())),
        'additional_native_python_assertions_used':True}}
    digest=sha256(json.dumps(record,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    record['mathematical_sha256']=digest
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(record,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'table':tables,'counted_exact_checks':sum(COUNTS.values()),
      'mathematical_sha256':digest,'output':str(output)},indent=2))
    return record



# New spatial-locality calculation. No companion files or network are read.
class SpatialCostalkAudit(RegulatorCostalkAudit):
    def __init__(self, model, source, grade, allowed, name):
        self.allowed=set(allowed)
        self.name=name
        super().__init__(model,source,grade)
        for j in sorted(self.allowed):
            check(all(i in self.allowed for i,p in model.d[j]),
                  'spatial_support_is_actual_subcomplex',(name,j))

    def target_basis(self,degree,weight,conductor=False):
        key=(degree,weight,conductor)
        if key in self.cache:return self.cache[key]
        raw=[]
        for j,(F,H,e) in enumerate(self.M.states):
            if j not in self.allowed or self.M.degree[j]!=degree:continue
            p=list(weight)+[self.grade-len(H)]
            for a in F:p[DIAGONALS.index(a)]+=1
            for a in H:p[DIAGONALS.index(a)]-=1
            p[DIAGONALS.index(self.M.occurrence)]-=e
            p=tuple(p)
            if min(p)<0 or not survives(p) or (conductor and not conductor_order(p)):continue
            raw.append({(j,p):1})
        cols={j:{('value',i,p):z for (i,p),z in v.items() if i in self.M.V|self.M.Q}
              for j,v in enumerate(raw)}
        for j,v in enumerate(raw):
            for (i,p),z in apply(self.M.d,v).items():
                if i in self.M.V:put(cols[j],('incoming_endpoint',i,p),z)
        ker=unit_kernel(cols,label=('spatial_frame',self.name,key))
        ans=[self.linear_combination(raw,co) for co in ker['basis']]
        for v in ans:
            check(all(i in self.allowed for i,p in v),'spatial_basis_retains_support',self.name)
            check(not restrict(v,self.M.V|self.M.Q),'spatial_basis_frame_values',self.name)
            check(not restrict(apply(self.M.d,v),self.M.V),'spatial_basis_frame_boundary',self.name)
        self.cache[key]=ans
        return ans


def closed_face_support(M,minimal_faces):
    return {j for j,(F,H,e) in enumerate(M.states)
            if any(set(a)<=set(F) for a in minimal_faces)}


def full_marked_state(M,F):
    F=tuple(sorted(F))
    return unit(M.index[F,F,0])


def local_edge_kernel(audit,edge):
    """Cousin map obtained from the positive branch of the edge boundary."""
    M=audit.M
    edge=tuple(sorted(edge))
    ends=[F for F in M.faces if len(F)==3 and set(edge)<=set(F)]
    check(len(ends)==2,'opposite_edge_has_two_actual_endpoints',edge)
    check(all(len(set(F)&set(LONG))==1 for F in ends),
          'edge_endpoints_have_two_distinct_long_labels',edge)
    L=multiply(full_marked_state(M,edge),monomial('beta'))
    for F in ends:L=add(L,full_marked_state(M,F),-1)
    dL=apply(M.d,L)
    up={(i,p):z for (i,p),z in dL.items() if any(p[DIAGONALS.index(a)] for a in PLUS)}
    um={(i,p):z for (i,p),z in dL.items() if any(p[DIAGONALS.index(a)] for a in MINUS)}
    check(add(up,um)==dL,'edge_boundary_splits_into_two_source_sheets',edge)
    check(not apply(M.d,up) and not apply(M.d,um),'split_edge_boundaries_are_cycles',edge)
    check(not restrict(L,M.V|M.Q) and not restrict(dL,M.V),'edge_primitive_frame',edge)
    gp={(('unit',0),i,p):z for (i,p),z in up.items()}
    gm={(('unit',0),i,p):-z for (i,p),z in um.items()}
    for a in sorted(PLUS):
        for (i,p),z in multiply(L,monomial('X'+a)).items():put(gp,(('generator',a),i,p),z)
    for a in sorted(MINUS):
        for (i,p),z in multiply(L,monomial('X'+a),-1).items():put(gm,(('generator',a),i,p),z)
    audit.verify_map(gp,('edge_positive',edge))
    audit.verify_map(gm,('edge_negative',edge))
    H={(('unit',0),i,p):z for (i,p),z in L.items()}
    check(audit.mapping_differential(H,1)==add(gp,gm,-1),
          'two_sheet_maps_have_explicit_homotopy',edge)
    return dict(edge=edge,endpoints=ends,L=L,U=up,Uminus=um,positive=gp,negative=gm,H=H)


def physical_diagonal(a):
    return ''.join(map(str,sorted((3-int(v))%6 for v in a)))


def physical_chain_action(Msrc,Mdst,chain):
    out={}
    for (j,p),z in chain.items():
        F,H,e=Msrc.states[j]
        FF=[physical_diagonal(a) for a in F]
        HH=[physical_diagonal(a) for a in H]
        i=Mdst.index[tuple(sorted(FF)),tuple(sorted(HH)),e]
        pp=[0]*10;pp[9]=p[9]
        for k,a in enumerate(DIAGONALS):pp[DIAGONALS.index(physical_diagonal(a))]=p[k]
        put(out,(i,tuple(pp)),-list_parity(FF)*list_parity(HH)*z)
    return out


def physical_map_action(audit,Mdst,mapping):
    grouped={}
    for (a,i,p),z in mapping.items():put(grouped.setdefault(a,{}),(i,p),z)
    out={}
    for a,v in grouped.items():
        ss=1
        if a[0]=='unit':dest=a
        elif a[0]=='generator':dest=('generator',physical_diagonal(a[1]))
        elif a[0]=='relation':
            typ,i,j=audit.source['relations'][a[1]]['name']
            ii,jj=physical_diagonal(i),physical_diagonal(j)
            if typ=='K' and ii>jj:ii,jj,ss=jj,ii,-1
            dest=('relation',audit.ri[typ,ii,jj])
        else:raise ValueError('Nonzero source components above the target range are unsupported')
        for (i,p),z in physical_chain_action(audit.M,Mdst,v).items():put(out,(dest,i,p),ss*z)
    return out


def cochain_certificate(audit,data):
    # The exact linear systems and their unimodular reductions are sufficient
    # to reproduce completeness, not just ranks of sampled evaluations.
    return audit.record_solve(data)


def main_spatial_costalk(output):
    COUNTS.clear()
    M=Complex('35');source=source_resolution()
    glob=RegulatorCostalkAudit(M,source,3);gd=glob.solve();pr=primary(glob)
    check(len(gd['qmaps'])==34,'replayed_global_costalk_rank')
    Cg=dense_columns([pr['quotient'](unit_image(F)) for F in gd['qmaps']],len(pr['qcycles']))
    check(integer_diagonalize(Cg,'global_counit')['rank']==3,'replayed_global_counit_rank')
    supports={
        'central_flip_edge_13_35': [('13','35')],
        'marked_D03_gallery': [('13','35'),('03','35')],
        'marked_gallery_with_entire_D03_square': [('13','35'),('03',)],
        'old_s_paired_marked_galleries': [('13','35'),('03','35'),('15','35'),('25','35')],
        'whole_D03_facet': [('03',)],
        'marked_corner_W03': [('02','03','35')],
        'opposite_edge_02_35': [('02','35')],
        'whole_short35_pentagon': [('35',)],
        'physical_three_facet_carrier': [('35',),('03',),('04',)]}
    expected={
        'central_flip_edge_13_35':(40,3,3,0),
        'marked_D03_gallery':(64,3,3,0),
        'marked_gallery_with_entire_D03_square':(124,3,3,0),
        'old_s_paired_marked_galleries':(112,6,6,0),
        'whole_D03_facet':(100,0,0,0),
        'marked_corner_W03':(16,0,0,0),
        'opposite_edge_02_35':(40,3,3,1),
        'whole_short35_pentagon':(124,12,12,1),
        'physical_three_facet_carrier':(268,20,20,2)}
    rows=[];records={};local={}
    for name,fs in supports.items():
        ids=closed_face_support(M,fs)
        au=SpatialCostalkAudit(M,source,3,ids,name);dd=au.solve()
        inc=dense_columns([gd['quotient_coordinates'](F) for F in dd['qmaps']],34)
        ir=integer_diagonalize(inc,('local_to_global',name))
        cc=dense_product(Cg,inc);cr=integer_diagonalize(cc,('local_primary',name))
        dims=(len(ids),len(dd['qmaps']),ir['rank'],cr['rank'])
        check(dims==expected[name],'complete_spatial_locality_dimensions',(name,dims))
        check(ir['diagonal']==[1]*ir['rank'],'local_to_global_image_saturated',name)
        check(cr['diagonal']==[1]*cr['rank'],'local_primary_image_saturated',name)
        for F in dd['qmaps']:
            check(all(i in ids for a,i,p in F),'local_quotient_representative_support',name)
        row=dict(name=name,source_minimal_faces=fs,target_states=len(ids),
                 cochain_unknowns=len(dd['unknown']),closed_maps=len(dd['maps']),
                 homotopy_boundaries=len(dd['hom']),local_classes=len(dd['qmaps']),
                 global_image_rank=ir['rank'],global_primary_rank=cr['rank'])
        rows.append(row);local[name]=(au,dd,inc)
        records[name]=dict(summary=row,allowed_state_ids=sorted(ids),
            solve=cochain_certificate(au,dd),global_inclusion=inc,
            inclusion_reduction=ir,counit=cc,counit_reduction=cr)

    # Compute actual coordinates in the previously used s(v)=2-v invariant kernel.
    SS=dense_columns([gd['quotient_coordinates'](glob.transform(F)) for F in gd['qmaps']],34)
    fi=fixed_lattice(SS,'ambient_old_s')
    cfix=dense_product(Cg,fi['kernel']);cfred=integer_diagonalize(cfix,'ambient_old_s_counit')
    ZG=dense_product(fi['kernel'],[row[cfred['rank']:] for row in cfred['right']])
    check(fi['fixed_rank']==11 and len(ZG[0])==10,'old_symmetry_ranks_replayed')
    localinv={}
    for name in ('old_s_paired_marked_galleries','whole_short35_pentagon'):
        au,dd,inc=local[name]
        sl=dense_columns([dd['quotient_coordinates'](au.transform(F)) for F in dd['qmaps']],len(dd['qmaps']))
        fl=fixed_lattice(sl,('local_s',name));imgs=dense_product(inc,fl['kernel'])
        check(fl['fixed_rank']==3,'spatial_old_s_fixed_rank',name)
        check(not any(x for row in dense_product(Cg,imgs) for x in row),
              'spatial_old_s_primary_zero',name)
        coords=dense_columns([image_coordinates(ZG,[row[j] for row in imgs],('ten_coordinates',name,j))
                              for j in range(fl['fixed_rank'])],10)
        rr=integer_diagonalize(coords,('local_ten_image',name))
        check(rr['diagonal']==[1,1,1],'local_ten_coordinate_image_saturated',name)
        localinv[name]=dict(action=sl,invariants=fl,coordinates_in_ten=coords,
                            coordinate_reduction=rr)
    # Both are the same rank-three sublattice, although their chosen bases differ.
    cat=[localinv['old_s_paired_marked_galleries']['coordinates_in_ten'][i]
         +localinv['whole_short35_pentagon']['coordinates_in_ten'][i] for i in range(10)]
    check(integer_diagonalize(cat,'same_spatial_invariant_image')['diagonal']==[1,1,1],
          'paired_gallery_and_pentagon_have_same_old_s_invariant_image')

    # Canonical opposite edge boundary split, with no desired output coordinate inserted.
    ee=local_edge_kernel(glob,('02','35'))
    e13=local_edge_kernel(glob,('04','13'))
    e15=local_edge_kernel(glob,('15','24'))
    edgecases=[ee,e13,e15]
    edgecoords=[gd['quotient_coordinates'](ec['positive']) for ec in edgecases]
    edgepr=[pr['quotient'](ec['U']) for ec in edgecases]
    check(integer_diagonalize(dense_columns(edgepr,len(pr['qcycles'])),'three_edge_primaries')['diagonal']==[1,1,1],
          'three_opposite_edges_span_all_primary_classes_primitively')
    for ec in edgecases:
        check((len(ec['L']),len(ec['U']),len(ec['positive']))==(3,3,12),
              'local_edge_kernel_exact_term_counts',ec['edge'])

    # Dropping the D25 endpoint and keeping the marked D03 endpoint is not a chain map.
    no25={j for j,(F,H,e) in enumerate(M.states) if '25' not in F}
    cut={(a,i,p):z for (a,i,p),z in ee['positive'].items() if i in no25}
    cutdef=glob.mapping_differential(cut,0)
    unitdef={(i,p):z for (a,i,p),z in cutdef.items() if a==('unit',0)}
    target=M.index[(('02','25','35'),('02',),0)]
    expected_def={(target,monomial('beta','beta','X25','X35')):-1}
    check(unitdef==expected_def,'D03_only_truncation_has_exact_uncancelled_unit_boundary')
    check(bool(cutdef),'D03_only_truncation_not_chain_map')

    # Genuine physical D03 reflection is 3-v, not the previous stabilizer 2-v.
    Mr=Complex('04');ar=RegulatorCostalkAudit(Mr,source,3)
    check(physical_diagonal('03')=='03' and physical_diagonal('35')=='04',
          'physical_reflection_preserves_D03_changes_occurrence')
    for j in range(430):
        image=physical_chain_action(M,Mr,unit(j))
        check(apply(Mr.d,image)==physical_chain_action(M,Mr,M.d[j]),
              'physical_reflection_complete_target_chain_equation',j)
        check(physical_chain_action(Mr,M,image)==unit(j),'physical_reflection_target_square',j)
    refedge=local_edge_kernel(ar,('04','13'))
    transported=physical_map_action(glob,Mr,ee['positive'])
    ar.verify_map(transported,'physical_reflection_of_local_kernel')
    check(transported==refedge['negative'],'physical_reflection_exchanges_source_sheet_maps')
    check(ar.mapping_differential(refedge['H'],1)==add(refedge['positive'],transported,-1),
          'physical_reflection_comparison_homotopy')
    check(add(physical_chain_action(Mr,M,refedge['L']),ee['L'])=={},
          'physical_reflection_second_comparison_cancels')
    check(physical_map_action(ar,M,transported)==ee['positive'],
          'physical_reflection_full_source_map_square')

    # Grade-four equality certifies persistence in every grade >=3 by the native-mark bound.
    pent=local['whole_short35_pentagon'][0]
    pent4=SpatialCostalkAudit(M,source,4,pent.allowed,'whole_short35_grade4')
    for n in (-1,0,1,2):
        q3=pent.mapping_basis(n);q4=pent4.mapping_basis(n)
        check(len(q3)==len(q4),'spatial_regulator_stable_cochain_dimensions',n)
        for (a,v),(aa,vv) in zip(q3,q4):
            check(a==aa and multiply(v,monomial('beta'))==vv,'spatial_regulator_stable_basis',n)
            check(shift_beta_map(pent.differential_column(a,v,n))
                  ==pent4.differential_column(aa,vv,n),'spatial_regulator_stable_differential',n)

    record={
      'schema':'marici.branch_a.central_flip_spatial_costalk.v1',
      'scope':{
        'ring':'Z[beta,X_d]/(X_minus_short*X_plus_short)',
        'source':'P_A[2], A=R/I; retained source ranks 1,6,24,92',
        'target':'K={q=0, v=0, vd=0} in complete 430-state C_beta',
        'occurrence_map_degree':0,'regulator_grade':3,
        'support_test':'H0 Hom(P_A[2],K intersect C_support) -> H0 Hom(P_A[2],K)',
        'absolute_physical_kernel_constructed':False,
        'local_coefficient_kernels_constructed':True,
        'geometric_Delta_J_identification':False,
        'no_go_limited_to_maps_factorizing_through_tested_local_costalk':True,
        'no_purity_or_Gysin_shift_added':True},
      'source_references':{
        'commit':COMMIT,'repo':'andrey-kokoev/marici',
        'gallery':'src/ledger/20260814-106 Marked Log Gallery Secondary Class and the Global Yoneda Gap.md',
        'corner_span':'src/ledger/20260814-96 Factorization-Marked Normal-Crossing Span and the Pair-Local Relation Obstruction.md',
        'physical_reflection':'src/ledger/20260814-140 Physical-Reflection Naturality of the D03 Edge Purity.md',
        'normalization':'src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md',
        'differential':'research/voevodsky/check_absolute_unlocalized_support_pc.rs'},
      'full_target_differential':serialize_full_matrix(M.d),
      'source_resolution':{
        'keys':[[list(a),glob.degrees[a],list(glob.weights[a])] for a in glob.keys],
        'differential':[{'source':list(a),'terms':[[list(c),list(p),z] for (c,p),z in col.items()]}
                        for a,col in glob.d.items()]},
      'global_costalk':glob.record_solve(gd),
      'global_primary':simplify_primary_record(pr,M),'global_counit':Cg,
      'support_table':rows,'local_supports':records,
      'old_s_invariant_calculation':{
        'reflection':SS,'invariant_basis':fi['kernel'],
        'ten_zero_primary_basis_in_global34':ZG,'local_images':localinv,
        'distinct_from_physical_D03_reflection':True},
      'local_edge_kernels':[{'edge':list(ec['edge']),'endpoints':[list(F) for F in ec['endpoints']],
        'L':serialize_chain(ec['L'],M),'unit_image':serialize_chain(ec['U'],M),
        'other_sheet_boundary':serialize_chain(ec['Uminus'],M),
        'positive_map':glob.serialize_map(ec['positive']),
        'negative_map':glob.serialize_map(ec['negative']),
        'global34_coordinates':co,'global_primary_coordinates':pc}
        for ec,co,pc in zip(edgecases,edgecoords,edgepr)],
      'D03_truncation':{'truncated_map':glob.serialize_map(cut),
        'unit_chain_defect':serialize_chain(unitdef,M),'all_defect_terms':glob.serialize_map(cutdef)},
      'physical_reflection':{
        'vertex_permutation':[3,2,1,0,5,4],
        'occurrence_source':'35','occurrence_target':'04',
        'transported_map':ar.serialize_map(transported),
        'reflected_positive_map':ar.serialize_map(refedge['positive']),
        'comparison_unit_chain':serialize_chain(refedge['L'],Mr),
        'square_comparison_zero':True},
      'conclusions':{
        'marked_gallery_primary_image_rank':0,
        'marked_gallery_local_costalk_rank':3,
        'D03_facet_local_costalk_rank':0,
        'opposite_edge_primary_image_rank':1,
        'old_s_zero_primary_locality_leaves_rank':3,
        'physical_support_changing_Gysin_still_unidentified':True}}
    # All record fields are mathematical data; the digest excludes runtime timing.
    record['mathematical_sha256']=sha256(json.dumps(record,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    record['verification']={'counted_exact_checks':sum(COUNTS.values()),'families':dict(sorted(COUNTS.items()))}
    Path(output).write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'support_table':rows,'checks':sum(COUNTS.values()),
                      'sha256':record['mathematical_sha256'],'output':str(output)},indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description='Exact central-flip local costalk and kernel audit')
    parser.add_argument('--output',default=str(Path(__file__).with_name('branch_a_central_flip_spatial_costalk_certificate.json')))
    args=parser.parse_args()
    main_spatial_costalk(args.output)
