#!/usr/bin/env python3
"""Normalization-ideal descent of the conductor-symbol comparison.

Standalone standard-library checker. Reconstructs the 430-state framed target,
the first three free terms of the actual conductor ideal's resolution, the
complete source-linear map equations, their integral solutions and reflection
action. Does not assign the physical conductor--Morse comparison.

The target algebra routines below are retained from the preceding standalone
conductor-symbol checker; the new source resolution and all map equations are
recomputed here. No companion data files or network are used.
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


def main_ideal_descent(output):
    M=Complex()
    cases={a:truncation_data(M,a,4) for a in SHORT_ORDER}
    source=source_resolution(); rel=source['relations']; syzy=source['syzygies']
    rcases={}
    for j,r in enumerate(rel):
        if r['weight'] not in rcases:rcases[r['weight']]=target_component(M,r['weight'],repr(r['name']))
    for a in SHORT_ORDER:
        aa=target_component(M,monomial('X'+a)[:9],a+'_homotopies')
        check(not aa['cols'],'no_degree_one_map_homotopies',a)
    unknown=[]
    for a,data in cases.items():
        for k,v in enumerate(data['cycles']):unknown.append(('Y',a,k,v))
    for rj,r in enumerate(rel):
        for k,v in enumerate(rcases[r['weight']]['cols']):unknown.append(('V',rj,k,v))
    check(len(unknown)==348,'source_linear_unknown_count')
    check(sum(x[0]=='Y' for x in unknown)==60,'old_generator_assignment_rank')
    uindex={entry[:3]:j for j,entry in enumerate(unknown)}
    columns={}
    for k,(kind,src,vk,v) in enumerate(unknown):
        col={}
        if kind=='Y':
            check(not apply(M.d,v),'generator_image_cycle',k)
            for rj,r in enumerate(rel):
                for p,z in r['d'].get(src,{}).items():
                    for (ti,pp),vv in multiply(v,p,-z).items():put(col,('r',rj,ti,pp),vv)
        else:
            for (ti,pp),vv in apply(M.d,v).items():put(col,('r',src,ti,pp),vv)
            for sj,sy in enumerate(syzy):
                for (rj,p),z in sy['d'].items():
                    if rj==src:
                        for (ti,pp),vv in multiply(v,p,-z).items():put(col,('s',sj,ti,pp),vv)
        columns[k]=col
    allmaps=unit_kernel(columns,label='complete_ideal_maps')
    strict=unit_kernel(columns,range(60),label='strict_ideal_maps')
    higher=unit_kernel(columns,range(60,len(unknown)),label='relation_only_maps')
    check((len(allmaps['rows']),allmaps['rank'],len(allmaps['basis']),len(strict['basis']),len(higher['basis']))
          ==(1101,308,40,16,6),'full_source_descent_dimensions')
    def pack(vec):
        maps={}
        for ui,z in vec.items():
            kind,src,k,v=unknown[ui];maps[kind,src]=add(maps.get((kind,src),{}),v,z)
        return {key:v for key,v in maps.items() if v}
    def unpack(maps):
        ans={}
        for (kind,src),v in maps.items():
            if kind=='Y':co=cycle_coordinates(v,cases[src],M)
            else:
                rc=rcases[rel[src]['weight']];nums={}
                for (j,p),z in v.items():
                    want=list(rc['coeff'][j]);want[9]=3-M.weight[j]
                    check(tuple(want)==p,'relation_homotopy_exact_weight',(src,j))
                    put(nums,j,z)
                vv=int_apply(rc['kernel']['full_basis_inverse'],nums)
                check(set(vv)<=set(rc['ids']),'relation_homotopy_in_frame_kernel',src)
                co=[vv.get(j,0) for j in rc['ids']]
            for k,z in enumerate(co):
                if z:put(ans,uindex[kind,src,k],z)
        check(pack(ans)=={key:v for key,v in maps.items() if v},'map_coordinate_reconstruction')
        return ans
    def verify_map(vec,model=M,label=''):
        maps=pack(vec)
        for (kind,src),v in maps.items():
            check(not restrict(v,model.V) and not restrict(v,model.Q),'full_endpoint_and_Q_zero',(label,kind,src))
            check(not restrict(apply(model.d,v),model.V),'full_endpoint_connector_zero',(label,kind,src))
        for a in SHORT_ORDER:
            check(not apply(model.d,maps.get(('Y',a),{})),'source_generator_chain_equation',(label,a))
        for rj,r in enumerate(rel):
            rhs={}
            for a,ps in r['d'].items():
                for p,z in ps.items():rhs=add(rhs,multiply(maps.get(('Y',a),{}),p,z))
            check(apply(model.d,maps.get(('V',rj),{}))==rhs,'source_relation_chain_equation',(label,rj))
        for sj,sy in enumerate(syzy):
            rhs={}
            for (rj,p),z in sy['d'].items():rhs=add(rhs,multiply(maps.get(('V',rj),{}),p,z))
            check(not rhs,'source_relation_of_relations_equation',(label,sj))
        return maps
    map_basis=[verify_map(v,label=('basis',j)) for j,v in enumerate(allmaps['basis'])]
    for j,v in enumerate(strict['basis']):verify_map(v,label=('strict',j))
    for j,v in enumerate(higher['basis']):verify_map(v,label=('higher',j))
    projections={j:{i:z for i,z in v.items() if i<60} for j,v in enumerate(allmaps['basis'])}
    projred=unit_kernel(projections,label='generator_image_projection')
    check((projred['rank'],len(projred['basis']))==(34,6),'generator_image_rank_and_kernel')
    sheet_ranks={}
    for name,sheet in (('positive',PLUS),('negative',MINUS)):
        ids=[j for j,(kind,src,k,v) in enumerate(unknown)
             if (src in sheet if kind=='Y' else rel[src]['name'][-1] in sheet)]
        kk=unit_kernel(columns,ids,label=name+'_source')
        sheet_ranks[name]=len(kk['basis'])
    check(sheet_ranks=={'positive':31,'negative':9},'sheet_resolved_map_ranks')

    # Actual cellular reflection and source-generator/relation transport.
    ri={r['name']:j for j,r in enumerate(rel)}
    def source_relation_action(rj,rot=0,ref=1):
        kind,a,c=rel[rj]['name'];aa=polygon_diagonal(a,rot,ref);cc=polygon_diagonal(c,rot,ref);sg=1
        if kind=='K' and aa>cc:aa,cc,sg=cc,aa,-1
        return ri[kind,aa,cc],sg
    def transform_maps(maps,rot=0,ref=1):
        out={}
        for (kind,src),v in maps.items():
            if kind=='Y':dest,sg=polygon_diagonal(src,rot,ref),1
            else:dest,sg=source_relation_action(src,rot,ref)
            out[kind,dest]=add({},polygon_action(M,v,rot,ref),sg)
        return out
    Scols={}
    for j,v in enumerate(allmaps['basis']):
        sv=unpack(transform_maps(pack(v)))
        check(not int_apply(columns,sv),'reflected_map_solves_full_source_equations',j)
        co={k:sv.get(i,0) for k,i in enumerate(allmaps['free']) if sv.get(i,0)}
        rec={}
        for k,z in co.items():rec=add(rec,allmaps['basis'][k],z)
        check(rec==sv,'source_map_reflection_coordinate_identity',j)
        Scols[j]=co
    for j in Scols:check(int_apply(Scols,Scols[j])=={j:1},'map_reflection_squared',j)
    fixed=dense_kernel({j:add(Scols[j],{j:1},-1) for j in Scols},'full_ideal_map_invariants')
    check(len(fixed['basis'])==13,'reflection_fixed_complete_maps')
    fixed_maps={}
    for j,v in enumerate(fixed['basis']):
        vv={}
        for k,z in v.items():vv=add(vv,allmaps['basis'][k],z)
        verify_map(vv,label=('invariant',j));fixed_maps[j]=vv
    fixedprojection=unit_kernel({j:{k:z for k,z in v.items() if k<60} for j,v in fixed_maps.items()},label='fixed_map_generator_images')
    check((fixedprojection['rank'],len(fixedprojection['basis']))==(11,2),'fixed_generator_image_and_relation_only_ranks')
    SS={}
    for j,v in enumerate(strict['basis']):
        sv=unpack(transform_maps(pack(v)))
        co={k:sv.get(i,0) for k,i in enumerate(strict['free']) if sv.get(i,0)}
        rec={}
        for k,z in co.items():rec=add(rec,strict['basis'][k],z)
        check(rec==sv,'strict_map_reflection_coordinate_identity',j);SS[j]=co
    fixedstrict=dense_kernel({j:add(SS[j],{j:1},-1) for j in SS},'strict_ideal_map_invariants')
    check(len(fixedstrict['basis'])==5,'strict_invariant_rank')
    # Check surjectivity on invariant generator assignments over Z, not just Q.
    Pmat=dense_columns([[projections[j].get(i,0) for i in range(60)] for j in range(40)],60)
    pr=integer_diagonalize(Pmat,'ideal_generator_image_integral_basis')
    check(pr['rank']==34 and pr['diagonal']==[1]*34,'generator_image_is_saturated')
    Smat=dense_columns([[Scols[j].get(i,0) for i in range(40)] for j in range(40)],40)
    Sbasis=dense_product(pr['right_inverse'],dense_product(Smat,pr['right']))
    check(not any(Sbasis[i][j] for i in range(34) for j in range(34,40)),'reflection_preserves_relation_only_kernel')
    Si=[row[:34] for row in Sbasis[:34]]
    fi=fixed_lattice(Si,'ideal_generator_image_invariants')
    Fmat=dense_columns([[v.get(i,0) for i in range(40)] for v in fixed['basis']],40)
    ImF=dense_product(pr['right_inverse'],Fmat)[:34]
    ir=integer_diagonalize(fi['kernel'],'invariant_generator_basis')
    coords=dense_product(ir['left'],ImF)
    check(not any(x for row in coords[fi['fixed_rank']:] for x in row),'fixed_map_images_in_fixed_generator_lattice')
    incoord=dense_product(ir['right'],coords[:fi['fixed_rank']])
    finv=integer_diagonalize(incoord,'invariant_ideal_lift_surjectivity')
    check(fi['fixed_rank']==11 and finv['diagonal']==[1]*11,'invariant_source_descent_has_no_index_defect')
    # Three occurrence-mark orbit: verify transformed full map equations.
    orbit_models={label:Complex(label) for label in ('35','15','13')}
    orbit_records=[]
    for j,v in fixed_maps.items():
        original=pack(v); orbit=[]
        for rot,occ in enumerate(('35','15','13')):
            mm=transform_maps(original,rot,0);target=orbit_models[occ]
            for a in SHORT_ORDER:check(not apply(target.d,mm.get(('Y',a),{})),'rotated_generator_equation',(j,occ,a))
            for rj,r in enumerate(rel):
                rhs={}
                for a,ps in r['d'].items():
                    for p,z in ps.items():rhs=add(rhs,multiply(mm.get(('Y',a),{}),p,z))
                check(apply(target.d,mm.get(('V',rj),{}))==rhs,'rotated_relation_equation',(j,occ,rj))
            for sj,sy in enumerate(syzy):
                rhs={}
                for (rj,p),z in sy['d'].items():rhs=add(rhs,multiply(mm.get(('V',rj),{}),p,z))
                check(not rhs,'rotated_second_relation_equation',(j,occ,sj))
            for key,chain in mm.items():
                check(not restrict(chain,target.V) and not restrict(chain,target.Q),'rotated_full_frame_zero',(j,occ,key))
            orbit.append(mm)
        for k,mm in enumerate(orbit):
            check(transform_maps(mm,1,0)==orbit[(k+1)%3],'rotation_family_exact',(j,k))
            check(transform_maps(mm,0,1)==orbit[(-k)%3],'reflection_family_exact',(j,k))
        orbit_records.append(orbit)

    # Tangible source-linear lift and a target-closed assignment that fails.
    edge=('13','35');vertex=('03','13','35')
    L=add(unit(M.index[vertex,vertex,0]),multiply(unit(M.index[edge,edge,0]),monomial('beta')),-1)
    good=multiply(L,monomial('X02'))
    check(not apply(M.d,good),'known_gallery_target_cycle_replayed')
    isolated=unpack({('Y','02'):good})
    test=unit_kernel(projections|{40:{k:-z for k,z in isolated.items()}},label='isolated_conormal_generator_test')
    check(not any(v.get(40) for v in test['basis']),'isolated_target_cycle_has_no_source_linear_lift')
    failedrel=ri['K','02','04']
    failure=multiply(good,monomial('X04'),-1)
    check(bool(failure),'actual_source_same_sheet_relation_nonzero')
    check(not rcases[rel[failedrel]['weight']]['cols'],'failed_relation_has_no_degree_four_correction')
    direct=unpack({('Y',a):multiply(L,monomial('X'+a)) for a in sorted(MINUS)})
    verify_map(direct,label='explicit_negative_sheet_gallery_map')
    check(all(j<60 for j in direct),'explicit_example_is_strict_on_source_relations')
    even=add(direct,unpack(transform_maps(pack(direct))))
    verify_map(even,label='equivariant_gallery_map')
    check(unpack(transform_maps(pack(even)))==even,'equivariant_gallery_map_reflection')
    sigma={'02':(-1,'14'),'04':(-1,'25'),'13':(1,'25'),
           '15':(1,'03'),'24':(-1,'03'),'35':(1,'14')}
    def evaluate(vec):
        maps=pack(vec);v={}
        for a,(sg,l) in sigma.items():v=add(v,multiply(maps.get(('Y',a),{}),monomial('X'+l),sg))
        check(not apply(M.d,v),'actual_normalization_symbol_image_closed')
        check(not restrict(v,M.V) and not restrict(v,M.Q),'actual_symbol_image_full_frame_zero')
        return v
    evalcols={j:evaluate(v) for j,v in enumerate(allmaps['basis'])}
    ev=unit_kernel(evalcols,label='actual_six_term_symbol_evaluation')
    check((ev['rank'],len(ev['basis']))==(34,6),'scalar_symbol_evaluation_rank')
    inv_eval={j:evaluate(v) for j,v in fixed_maps.items()}
    iev=unit_kernel(inv_eval,label='actual_symbol_invariant_evaluation')
    check((iev['rank'],len(iev['basis']))==(11,2),'invariant_scalar_symbol_evaluation_rank')
    eg=evaluate(even)
    check(len(eg)==12 and bool(eg),'explicit_equivariant_symbol_has_twelve_terms')
    for a,(sg,l) in sigma.items():
        w=monomial('X'+a,'X'+l)[:9]
        cc=target_component(M,w,a+'_actual_symbol_homotopies')
        check(not cc['cols'],'no_degree_four_homotopies_on_actual_scalar_symbol',a)
    # Inspect one explicit higher-only map: it vanishes on every generator.
    highsample=higher['basis'][0]
    check(all(kind=='V' for kind,src in pack(highsample)),'relation_only_sample_has_zero_all_generator_images')
    check(not evaluate(highsample),'relation_only_map_invisible_on_scalar_symbol')

    def ser_maps(maps):
        return [{'source_type':'generator' if kind=='Y' else 'first_relation',
                 'source':src if kind=='Y' else list(rel[src]['name']),
                 'image':serialize_chain(v,M)}
                for (kind,src),v in sorted(maps.items(),key=lambda item:repr(item[0]))]
    def serker(k):
        return {'rank':k['rank'],'free_columns':k.get('free'),
                'basis':[sparse_list(v) for v in k['basis']],
                'unit_pivots':[[j,sparse_list(v)] for j,v in k.get('pivots',[])]}
    def ser_source_matrix(mat):
        return [[j,[[i,list(p),z] for (i,p),z in sorted(v.items())]] for j,v in sorted(mat.items())]
    record={
      'schema':'marici.branch_a.normalization_ideal_descent.v1',
      'scope':{'coefficient_ring':'Z[beta,X02,X03,X04,X13,X14,X15,X24,X25,X35]/(X_even X_odd)',
               'source':'actual conductor ideal I in homological degree 3, with its free resolution',
               'target':'N={c in I C_beta: q(c)=v(c)=v(dc)=0}',
               'map_degree':0,'occurrence_map_multidegree':[0]*9,'regulator_normal_map_grade':3,
               'geometric_purity_at_beta_zero':False,'physical_Delta_J_identified':False},
      'sources':{'repository':'andrey-kokoev/marici','commit':COMMIT,
                 'normalization':'src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md',
                 'absolute_target':'research/voevodsky/check_absolute_unlocalized_support_pc.rs'},
      'source_resolution':{'ranks':[6,24,92],
            'generators':list(SHORT_ORDER),'relation_labels':[list(r['name']) for r in rel],
            'second_relation_labels':[list(s['name']) for s in syzy],
            'd0':ser_source_matrix(source['d0']),'d1':ser_source_matrix(source['d1']),
            'd2':ser_source_matrix(source['d2']),
            'exactness_scope':'arbitrary polynomial coefficients; branch-decomposition proof, not finite-degree inference'},
      'target_differential':serialize_full_matrix(M.d),
      'source_equations':{'unknowns':len(unknown),'nonzero_rows':len(allmaps['rows']),
            'row_labels':[[typ,src,j,list(p)] for typ,src,j,p in sorted(allmaps['rows'])],
            'rows':[sparse_list(allmaps['rows'][row]) for row in sorted(allmaps['rows'])],
            'unknown_labels':[[kind,src,k] for kind,src,k,v in unknown],
            'unknown_polynomial_basis':[serialize_chain(v,M) for kind,src,k,v in unknown],
            'solution':serker(allmaps),'strict_solution':serker(strict),'relation_only_solution':serker(higher)},
      'dimensions':{'complete_maps':40,'generator_image':34,'relation_only':6,'strict_maps':16,
                    'positive_source':31,'negative_source':9,
                    'invariant_complete_maps':13,'invariant_generator_image':11,'invariant_relation_only':2,
                    'invariant_strict_maps':5,'scalar_symbol_image':34,'invariant_scalar_symbol_image':11},
      'complete_map_basis':[ser_maps(mm) for mm in map_basis],
      'projection_to_previous_sixty_symbols':{'matrix':Pmat,'integral_reduction':pr},
      'symmetry':{'reflection_matrix':Smat,'fixed_lattice':fixed['reduction'],
            'strict_fixed_lattice':fixedstrict['reduction'],'generator_image_reflection':Si,
            'invariant_generator_preimage_diagonal_factors':finv['diagonal'],
            'invariant_source_descent_index':1,
            'invariant_maps':[ser_maps(pack(v)) for v in fixed_maps.values()],
            'occurrence_orbit':list(orbit_models),'all_orbit_chain_equations_verified':True},
      'examples':{'isolated_assignment':serialize_chain(good,M),
            'failed_source_relation':list(rel[failedrel]['name']),
            'failed_relation_value':serialize_chain(failure,M),
            'strict_negative_sheet_map':ser_maps(pack(direct)),
            'equivariant_gallery_map':ser_maps(pack(even)),
            'source_symbol_coefficients':sigma,
            'equivariant_source_symbol_image':serialize_chain(eg,M),
            'relation_only_map':ser_maps(pack(highsample))},
      'scalar_symbol_evaluation':{'solution_rank':ev['rank'],'kernel_rank':len(ev['basis']),
            'image_basis_chains':[serialize_chain(v,M) for v in evalcols.values()],
            'invariant_image_basis_chains':[serialize_chain(v,M) for v in inv_eval.values()]},
      'no_degree_one_map_homotopies':True,
      'verification':{'checks':dict(sorted(COUNTS.items())),'total':sum(COUNTS.values())}}
    mathematical=json.dumps(record,sort_keys=True,separators=(',',':')).encode()
    record['mathematical_sha256']=sha256(mathematical).hexdigest()
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(record,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'complete_maps':40,'generator_images':34,'relation_only':6,
        'strict_maps':16,'equivariant_maps':13,'equivariant_symbol_images':11,
        'exact_checks':sum(COUNTS.values()),'certificate':str(output),
        'sha256':record['mathematical_sha256']},indent=2))
    return record


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,
      default=Path(__file__).with_name('branch_a_normalization_ideal_descent_certificate.json'))
    args=parser.parse_args()
    main_ideal_descent(args.output)
