#!/usr/bin/env python3
"""Milnor totalization and full conductor-costalk audit.

Replays the normalization-ideal and sheet-extension calculations, then
constructs the whole affine conductor costalk in the tested grading.
The implementation is standalone and uses only the Python standard library.

Inherited normalization-ideal descent of the conductor-symbol comparison.

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


def main_normalization_extension(output):
    # Replay the entire preceding construction from its equations. No input files.
    with tempfile.TemporaryDirectory() as td, contextlib.redirect_stdout(io.StringIO()):
        preceding=main_ideal_descent(Path(td)/'replayed_normalization_ideal_descent.json')
    preceding_checks=sum(COUNTS.values())
    M=Complex();source=source_resolution();relations=source['relations']
    ri={tuple(r['name']):j for j,r in enumerate(relations)}
    maps=[extension_deserialize_maps(x,ri) for x in preceding['complete_map_basis']]
    flatmaps={j:extension_flat(x) for j,x in enumerate(maps)}
    check(len(maps)==40,'extension_replayed_ideal_map_rank')
    for j,x in enumerate(maps):extension_verify_source_map(x,M,source,('original',j))

    # R_sheet = R/I_opposite. Its free resolution starts R, P0(I_opp), P1(I_opp).
    # Retain the WHOLE target here, not just the endpoint/Q/conductor kernel.
    sheet_records=[]
    for label,sheet in (('plus',PLUS),('minus',MINUS)):
        opposite=sorted(SHORT-sheet)
        units=extension_component(M,3,(0,)*9)
        relationcols=[(a,v) for a in opposite
                      for v in extension_component(M,4,monomial('X'+a)[:9])]
        matrix={}
        for j,v in enumerate(units):
            col={('closed',i,p):z for (i,p),z in apply(M.d,v).items()}
            for a in opposite:
                for (i,p),z in multiply(v,monomial('X'+a),-1).items():
                    put(col,('relation',a,i,p),z)
            matrix[j]=col
        for j,(a,v) in enumerate(relationcols,len(units)):
            col={('relation',a,i,p):z for (i,p),z in apply(M.d,v).items()}
            for rj,r in enumerate(relations):
                if not set(r['d'])<=set(opposite):continue
                for p,z in r['d'].get(a,{}).items():
                    for (i,q),c in multiply(v,p,-z).items():
                        put(col,('second_relation',rj,i,q),c)
            matrix[j]=col
        solution=unit_kernel(matrix,label=('full_normalization_sheet',label))
        expected=56 if label=='plus' else 101
        check(len(matrix)==expected and solution['rank']==expected and not solution['basis'],
              'no_closed_normalization_module_maps_even_unframed',label)
        check(not extension_component(M,4,(0,)*9),
              'no_unit_map_positive_degree_homotopies',label)
        sheet_records.append({'sheet':label,'annihilator_generators':opposite,
            'source_resolution_ranks_through_degree_six':[1,3,12,46],
            'unit_image_unknowns':len(units),'relation_image_unknowns':len(relationcols),
            'unknowns':len(matrix),'closed_map_rank':0,
            'unknown_basis':([{'source':'unit','chain':serialize_chain(v,M)} for v in units]
                +[{'source':a,'chain':serialize_chain(v,M)} for a,v in relationcols]),
            'equation_reduction':extension_kernel_record(solution)})

    # Compute all possible chain homotopies P(I)[3] -> C_beta of degree +1.
    homotopies=[(a,v) for a in SHORT_ORDER
                for v in extension_component(M,4,monomial('X'+a)[:9])]
    check(len(homotopies)==45 and all(a=='35' for a,v in homotopies),
          'only_source_35_all_fortyfive_homotopy_states')
    for a in SHORT_ORDER:
        check(not extension_component(M,4,monomial('X'+a)[:9],conductor=True),
              'no_conductor_valued_source_map_homotopies',a)
    dh={j:extension_homotopy_boundary(a,v,M,relations)
        for j,(a,v) in enumerate(homotopies)}
    kh=unit_kernel(dh,label='all_ambient_homotopy_boundary_kernel')
    check(kh['rank']==45 and not kh['basis'],'ambient_map_homotopy_boundary_injective')
    for j,col in dh.items():extension_verify_source_map(extension_pack_flat(col),M,source,('dH',j))

    system=dict(flatmaps)
    system.update({40+j:{k:-z for k,z in col.items()} for j,col in dh.items()})
    comparison=unit_kernel(system,label='conductor_maps_equal_ambient_boundaries')
    check((len(system),comparison['rank'],len(comparison['basis']))==(85,76,9),
          'nine_of_forty_are_ambient_boundaries')
    killed={j:{i:z for i,z in v.items() if i<40}
            for j,v in enumerate(comparison['basis'])}
    K=dense_columns([[v.get(i,0) for i in range(40)] for v in killed.values()],40)
    Kdiag=integer_diagonalize(K,'nine_dimensional_forgetting_kernel')
    check(Kdiag['diagonal']==[1]*9,'ambient_quotient_rank31_is_torsion_free')
    killchains={};primitive_records=[]
    for j,v in enumerate(comparison['basis']):
        U={}
        for k,z in v.items():
            if k>=40:U=add(U,homotopies[k-40][1],z)
        boundary=extension_homotopy_boundary('35',U,M,relations)
        F={}
        for k,z in killed[j].items():F=add(F,flatmaps[k],z)
        check(F==boundary and bool(F),'forgetting_explicit_primitive_identity',j)
        check(not restrict(U,M.V|M.Q),'forgetting_homotopy_preserves_full_endpoint_Q',j)
        check(not restrict(apply(M.d,U),M.V|M.Q),
              'forgetting_homotopy_incoming_endpoints_zero',j)
        check(all(conductor_order(p)==0 for i,p in U),
              'only_relaxed_condition_is_conductor_order',j)
        check(all(conductor_order(p)>0 for kind,s,i,p in F),
              'boundary_is_conductor_valued',j)
        check(len(U)==3,'three_term_zero_order_primitives',j)
        killchains[j]=F
        primitive_records.append({'ideal_map_coordinates':sparse_list(killed[j]),
            'H_on_a35':serialize_chain(U,M),'H_on_other_generators':[],
            'full_map':extension_serialize_maps(extension_pack_flat(F),M,relations)})
    # Neither strict maps nor the six relation-only classes are lost.
    strict_inter=unit_kernel({j:{key:z for key,z in col.items() if key[0]=='V'}
                              for j,col in killchains.items()},label='strict_intersection_with_lost_lattice')
    relation_inter=unit_kernel({j:{key:z for key,z in col.items() if key[0]=='Y'}
                                for j,col in killchains.items()},label='relation_only_intersection_with_lost_lattice')
    check(not strict_inter['basis'] and not relation_inter['basis'],
          'strict_and_relation_only_subspaces_both_survive')

    # Actual reflection and integral invariant quotient, with no averaging.
    S=preceding['symmetry']['reflection_matrix']
    SK=dense_product(S,K);kc=dense_product(Kdiag['left'],SK)
    check(not any(z for row in kc[9:] for z in row),'reflection_preserves_lost_lattice')
    S_k=dense_product(Kdiag['right'],kc[:9])
    fixed_k=fixed_lattice(S_k,'lost_class_reflection')
    Uinv=extension_inverse_left(Kdiag)
    S_new=dense_product(dense_product(Kdiag['left'],S),Uinv)
    check(not any(S_new[i][j] for i in range(9,40) for j in range(9)),
          'quotient_reflection_well_defined')
    S_q=[row[9:] for row in S_new[9:]]
    fixed_q=fixed_lattice(S_q,'remaining_obstruction_reflection')
    fixed_h=fixed_lattice(S,'replayed_ideal_class_reflection')
    check((fixed_k['fixed_rank'],fixed_h['fixed_rank'],fixed_q['fixed_rank'])==(3,13,10),
          'equivariant_extension_dimensions')
    images=dense_product(Kdiag['left'],fixed_h['kernel'])[9:]
    qred=integer_diagonalize(fixed_q['kernel'],'obstruction_fixed_basis')
    qc=dense_product(qred['left'],images)
    check(not any(z for row in qc[10:] for z in row),'invariant_images_are_fixed')
    invariant_coordinates=dense_product(qred['right'],qc[:10])
    invred=integer_diagonalize(invariant_coordinates,'invariant_normalization_extension_cokernel')
    check(invred['diagonal']==[1]*10,'equivariant_extension_no_finite_index_defect')

    # Construct the connecting cocycles on each component of the doubled conductor.
    # A free resolution Q(C)[2] has R in degree2, P0(I) in degree3,
    # P1(I) in degree4, P2(I) in degree5. We use the displayed positive
    # differentials; this fixes the shift rephasing throughout.
    def supported_obstruction(mapping,label):
        branches=[]
        for name,sheet in (('plus',PLUS),('minus',MINUS)):
            part={key:v for key,v in mapping.items()
                  if (key[0]=='Y' and key[1] in sheet)
                  or (key[0]=='V' and set(relations[key[1]]['d'])<=set(sheet))}
            extension_verify_source_map(part,M,source,('boundary_obstruction',label,name))
            for key,v in part.items():
                check(not restrict(v,M.V|M.Q),'obstruction_full_endpoint_Q_zero',(label,name,key))
                check(all(conductor_order(p)>0 for i,p in v),'obstruction_retains_conductor_factors')
            branches.append({'sheet':name,'unit_image_degree2':[],
                'remaining_images':extension_serialize_maps(part,M,relations)})
        combined={}
        for name,sheet in (('plus',PLUS),('minus',MINUS)):
            for key,v in mapping.items():
                if ((key[0]=='Y' and key[1] in sheet)
                   or (key[0]=='V' and set(relations[key[1]]['d'])<=set(sheet))):
                    combined[key]=add(combined.get(key,{}),v)
        check(extension_flat(combined)==extension_flat(mapping),
              'doubled_conductor_keeps_both_source_summands',label)
        return branches
    all_obstructions=[supported_obstruction(x,('all',j)) for j,x in enumerate(maps)]
    # Select an integral basis of the quotient by its certified unimodular coordinates.
    quotient_maps=[];quotient_coords=[]
    for k in range(9,40):
        co={j:Uinv[j][k] for j in range(40) if Uinv[j][k]}
        F={}
        for j,z in co.items():F=add(F,flatmaps[j],z)
        quotient_coords.append(sparse_list(co))
        quotient_maps.append(extension_pack_flat(F))
    quotient_obstructions=[supported_obstruction(F,('quotient',j))
                           for j,F in enumerate(quotient_maps)]
    check(len(quotient_maps)==31,'independent_normalization_obstructions')

    # A relation-only cocycle remains nonzero after all ambient homotopies.
    high=extension_deserialize_maps(preceding['examples']['relation_only_map'],ri)
    high_eq=dict(dh);high_eq[45]={key:-z for key,z in extension_flat(high).items()}
    high_test=unit_kernel(high_eq,label='relation_only_obstruction_survives_unframed')
    check(not high_test['basis'],'relation_only_class_not_an_ambient_boundary')
    strict=extension_deserialize_maps(preceding['examples']['strict_negative_sheet_map'],ri)
    strict_eq=dict(dh);strict_eq[45]={key:-z for key,z in extension_flat(strict).items()}
    strict_test=unit_kernel(strict_eq,label='strict_gallery_obstruction_survives_unframed')
    check(not strict_test['basis'],'strict_gallery_not_an_ambient_boundary')

    counts_after=sum(COUNTS.values())
    record={
        'schema':'marici.branch_a.normalization_sheet_extension_obstruction.v1',
        'scope':{'ring':'Z[beta,X02,X03,X04,X13,X14,X15,X24,X25,X35]/(X_minus X_plus)',
                 'source_shift':3,'occurrence_map_degree':[0]*9,'regulator_normal_grade':3,
                 'original_target':'N={c in I*C_beta: q(c)=v(c)=v(dc)=0}',
                 'enlarged_target':'K={c in C_beta: q(c)=v(c)=v(dc)=0}',
                 'full_target':'complete 430-state C_beta',
                 'physical_Delta_J_identified':False,
                 'geometric_regulator_zero_purity_claimed':False},
        'sources':preceding['sources'],
        'preceding_reconstruction':{'sha256':preceding['mathematical_sha256'],
                                    'checks':preceding_checks,'dimensions':preceding['dimensions']},
        'normalization_sequence':'0 -> I -> R_plus direct-sum R_minus -> C direct-sum C -> 0',
        'normalization_module_tests':sheet_records,
        'source_resolution':preceding['source_resolution'],
        'target_differential':serialize_full_matrix(M.d),
        'ideal_map_basis':preceding['complete_map_basis'],
        'ambient_homotopy_basis':[{'source':a,'image':serialize_chain(v,M)} for a,v in homotopies],
        'ambient_homotopy_boundary_injectivity':extension_kernel_record(kh),
        'map_boundary_intersection':extension_kernel_record(comparison),
        'lost_map_inclusion_matrix':K,
        'lost_map_integral_reduction':Kdiag,
        'lost_maps_and_explicit_homotopies':primitive_records,
        'quotient_map_coordinates':quotient_coords,
        'obstructions_on_doubled_conductor':all_obstructions,
        'independent_obstruction_basis':quotient_obstructions,
        'symmetry':{'original_reflection':S,'lost_reflection':S_k,'quotient_reflection':S_q,
                    'lost_fixed_basis':fixed_k['kernel'],'original_fixed_basis':fixed_h['kernel'],
                    'quotient_fixed_basis':fixed_q['kernel'],
                    'invariant_quotient_image_reduction':invred},
        'dimensions':{'original_conductor_relative_classes':40,
            'endpoint_Q_preserving_but_not_conductor_relative_boundaries':9,
            'remaining_obstruction_lattice':31,
            'equivariant_original':13,'equivariant_removed':3,'equivariant_remaining':10,
            'strict_maps_remaining':16,'relation_only_maps_remaining':6,
            'normalization_maps_in_tested_grade_even_without_frame':0},
        'examples':{'three_term_homotopy_example':primitive_records[0],
                    'strict_gallery_map':preceding['examples']['strict_negative_sheet_map'],
                    'strict_gallery_obstruction':supported_obstruction(strict,'strict_gallery_example'),
                    'relation_only_map':preceding['examples']['relation_only_map'],
                    'relation_only_obstruction':supported_obstruction(high,'relation_only_example')},
        'verification':{'replayed_check_count':preceding_checks,
                        'new_check_count':sum(COUNTS.values())-preceding_checks,
                        'total_check_count':sum(COUNTS.values()),
                        'by_family':dict(sorted(COUNTS.items()))},
        'interpretation':{'nonzero_same_degree_normalization_sheet_extension':False,
            'coherent_extension_of_original_F_into_K_exists_iff_F_in_rank_nine_kernel':True,
            'nonzero_classes_retyped_as_doubled_conductor_connecting_obstructions':31,
            'conductor_relative_homotopy_requirement_relaxed_only_in_explicit_forgetting_test':True}
    }
    data=json.dumps(record,sort_keys=True,separators=(',',':')).encode()
    record['mathematical_sha256']=sha256(data).hexdigest()
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(record,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'normalization_module_maps':0,'original_relative_classes':40,
        'lost_after_conductor_homotopy_forgetting':9,'independent_extension_obstructions':31,
        'equivariant_obstructions':10,'new_exact_checks':record['verification']['new_check_count'],
        'replayed_exact_checks':preceding_checks,'certificate':str(output),
        'sha256':record['mathematical_sha256']},indent=2))
    return record



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


def main_milnor_costalk(output):
    with tempfile.TemporaryDirectory() as td,contextlib.redirect_stdout(io.StringIO()):
        old=main_normalization_extension(Path(td)/'inherited_replay.json')
    inherited=sum(COUNTS.values())
    M=Complex();source=source_resolution();audit=CostalkAudit(M,source)
    milnor=milnor_square_exactness()
    data=audit.solve(False)
    relative=audit.solve(True)
    primary=costalk_target_primary(audit)

    def unit_image(F):return {(j,p):z for (a,j,p),z in F.items() if a==('unit',0)}
    counit=dense_columns([primary['quotient'](unit_image(F)) for F in data['qmaps']],5)
    cr=integer_diagonalize(counit,'new_costalk_counit_matrix')
    check(cr['rank']==3 and cr['diagonal']==[1]*3,'new_costalk_counit_rank_and_saturation')
    check(len(data['qmaps'])-cr['rank']==31,'new_costalk_counit_kernel_rank')
    for F in data['dh']:
        check(not any(primary['quotient'](unit_image(F))),'new_counit_respects_all_map_homotopies')

    # Diagonal restriction of both normalized upper-conductor obstructions.
    oldmaps=[extension_deserialize_maps(x,audit.ri) for x in old['ideal_map_basis']]
    def diagonal_obstruction(mm):
        out={}
        for (kind,a),v in mm.items():
            key=('generator',a) if kind=='Y' else ('relation',a)
            for (j,p),z in v.items():put(out,(key,j,p),z)
        return out
    obstruction_maps=[diagonal_obstruction(mm) for mm in oldmaps]
    for j,F in enumerate(obstruction_maps):
        audit.verify_map(F,('diagonal_obstruction',j))
        check(not unit_image(F),'new_connecting_obstruction_has_zero_unit',j)
        pieces=[]
        for sheet in (MINUS,PLUS):
            piece={}
            for (kind,a),v in oldmaps[j].items():
                belongs=(a in sheet if kind=='Y' else set(source['relations'][a]['d'])<=sheet)
                if belongs:
                    key=('generator',a) if kind=='Y' else ('relation',a)
                    for (i,p),z in v.items():put(piece,(key,i,p),z)
            audit.verify_map(piece,('upper_conductor_piece',j,tuple(sorted(sheet))))
            pieces.append(piece)
        check(add(*pieces)==F,'new_actual_diagonal_pullback_keeps_all_source_relations',j)
    obcols=[data['quotient_coordinates'](F) for F in obstruction_maps]
    obmat=dense_columns(obcols,34)
    obred=integer_diagonalize(obmat,'new_diagonal_obstruction_image')
    check(obred['rank']==31 and obred['diagonal']==[1]*31,'new_diagonal_obstruction_injective_on_old_quotient')
    check(dense_product(counit,obmat)==[[0]*40 for _ in range(5)],'new_obstruction_image_is_counit_kernel')
    # Two saturated rank31 sublattices agree by inclusion and rank.
    check(len(data['qmaps'])-cr['rank']==obred['rank'],'new_complete_costalk_exact_sequence')
    lost=old['lost_map_inclusion_matrix']
    check(dense_product(obmat,lost)==[[0]*9 for _ in range(34)],'new_exact_same_nine_homotopies_lost')
    check(40-obred['rank']==9,'new_no_additional_diagonal_cancellation')

    # Exhibit a supported map selected by an actual target chain and the
    # source's sheet decomposition, not by prescribing a scalar residue.
    L={
      (M.index[(('04','13'),('04','13'),0)],monomial('beta')):1,
      (M.index[(('04','13','14'),('04','13','14'),0)],ZERO):-1,
      (M.index[(('03','04','13'),('03','04','13'),0)],ZERO):-1}
    dL=apply(M.d,L)
    U={(j,p):z for (j,p),z in dL.items() if any(p[DIAGONALS.index(a)] for a in PLUS)}
    opposite=add(dL,U,-1)
    example={(('unit',0),j,p):z for (j,p),z in U.items()}
    for a in sorted(PLUS):
        for (j,p),z in multiply(L,monomial('X'+a)).items():put(example,(('generator',a),j,p),z)
    audit.verify_map(example,'new_twelve_term_conductor_unit_map')
    check((len(L),len(U),len(opposite),len(example))==(3,3,3,12),'new_explicit_unit_map_term_counts')
    check(not apply(M.d,U),'new_conductor_unit_image_closed')
    unit_co=primary['quotient'](U)
    check(any(abs(z)==1 for z in unit_co),'new_unit_primary_primitive_detector')
    check(any(data['quotient_coordinates'](example)),'new_unit_map_nonzero')
    invariant_example=add(example,audit.transform(example))
    audit.verify_map(invariant_example,'new_invariant_conductor_unit_example')
    check(audit.transform(invariant_example)==invariant_example,'new_explicit_unit_example_strict_involution')
    check((len(invariant_example),len(unit_image(invariant_example)))==(24,6),
          'new_invariant_example_term_counts')

    # The counit has two further target directions outside its image. Retain
    # the older transgression as an explicit negative control.
    phi={(M.index[(),(),0],monomial('beta')):1}
    for long in LONG:put(phi,(M.index[(long,),(long,),0],ZERO),-1)
    chi=multiply(apply(M.d,phi),monomial('beta','beta'))
    check(not apply(M.d,chi) and not restrict(chi,M.V|M.Q),'new_transgression_full_frame_check')
    chi_co=primary['quotient'](chi)
    transformed_chi=[sum(x*y for x,y in zip(row,chi_co)) for row in cr['left']]
    check(transformed_chi[3:] and any(transformed_chi[3:]),'new_transgression_not_in_counit_image')
    check(any(abs(z)==1 for z in transformed_chi[3:]),'new_transgression_primitive_counit_obstruction')

    # Reflection on complete derived classes and actual strict representative lifts.
    Smat=dense_columns([data['quotient_coordinates'](audit.transform(F)) for F in data['qmaps']],34)
    check(dense_product(Smat,Smat)==dense_identity(34),'new_costalk_reflection_squared')
    fixed=fixed_lattice(Smat,'new_conductor_costalk_invariants')
    check(fixed['fixed_rank']==11,'new_costalk_invariant_rank')
    inverse_ob=extension_inverse_left(obred)
    Snew=dense_product(obred['left'],dense_product(Smat,inverse_ob))
    check(not any(Snew[i][j] for i in range(31,34) for j in range(31)),
          'new_reflection_preserves_counit_kernel')
    Sker=[row[:31] for row in Snew[:31]];Sprimary=[row[31:] for row in Snew[31:]]
    fker=fixed_lattice(Sker,'new_counit_kernel_invariants')
    fprimary=fixed_lattice(Sprimary,'new_supported_primary_invariants')
    check((fker['fixed_rank'],fprimary['fixed_rank'])==(10,1),'new_equivariant_costalk_exact_ranks')
    Im=dense_product(obred['left'],fixed['kernel'])[31:]
    fpr=integer_diagonalize(fprimary['kernel'],'new_invariant_primary_basis')
    co=dense_product(fpr['left'],Im)
    check(not any(z for row in co[1:] for z in row),'new_invariant_counit_invariant_image')
    ico=dense_product(fpr['right'],co[:1])
    ir=integer_diagonalize(ico,'new_invariant_counit_surjectivity')
    check(ir['diagonal']==[1],'new_invariant_costalk_no_index_obstruction')
    exco=data['quotient_coordinates'](invariant_example)
    exprimary=[sum(x*y for x,y in zip(row,exco)) for row in obred['left'][31:]]
    exprco=[sum(x*y for x,y in zip(row,exprimary)) for row in fpr['left']]
    exprco=dense_product(fpr['right'],[[x] for x in exprco[:1]])
    check(abs(exprco[0][0])==1,'new_explicit_invariant_primary_is_primitive')

    Scoc=dense_columns([[data['coordinates'](audit.transform(F)).get(i,0) for i in range(108)]
                       for F in data['maps']],108)
    check(dense_product(Scoc,Scoc)==dense_identity(108),'new_closed_costalk_reflection_squared')
    fcoc=fixed_lattice(Scoc,'new_strict_invariant_costalk_cycles')
    check(fcoc['fixed_rank']==42,'new_strict_invariant_cycle_rank')
    images=dense_product(data['reduction']['left'][74:],fcoc['kernel'])
    fr=integer_diagonalize(fixed['kernel'],'new_derived_invariant_costalk_basis')
    co=dense_product(fr['left'],images)
    check(not any(z for row in co[11:] for z in row),'new_strict_invariant_classes_are_fixed')
    ici=dense_product(fr['right'],co[:11])
    cir=integer_diagonalize(ici,'new_strict_invariant_representative_surjectivity')
    check(cir['diagonal']==[1]*11,'new_all_invariant_costalk_classes_have_strict_representatives')
    orbit_models={a:Complex(a) for a in ('35','15','13')}
    invariant_maps=[];orbit_records=[]
    for k in range(11):
        fixedcoords=[sum(cir['right'][i][j]*cir['left'][j][k] for j in range(11)) for i in range(42)]
        coccoords=[sum(row[i]*fixedcoords[i] for i in range(42)) for row in fcoc['kernel']]
        F=audit.linear_combination(data['maps'],{j:z for j,z in enumerate(coccoords) if z})
        check(audit.transform(F)==F,'new_strict_invariant_representative',k)
        check(data['quotient_coordinates'](F)==[row[k] for row in fixed['kernel']],
              'new_invariant_representative_class',k)
        family=[]
        for rot,occ in enumerate(('35','15','13')):
            ff=audit.transform(F,rot,0)
            audit.verify_map(ff,('new_complete_orbit',k,occ),orbit_models[occ]);family.append(ff)
        for rot,ff in enumerate(family):
            check(audit.transform(ff,1,0)==family[(rot+1)%3],'new_orbit_rotation_equation',(k,rot))
            check(audit.transform(ff,0,1)==family[(-rot)%3],'new_orbit_reflection_equation',(k,rot))
        invariant_maps.append(F);orbit_records.append(family)

    # Three explicit supported classes lifting a basis of the counit image.
    new_primary_maps=[]
    for k in range(3):
        F=audit.linear_combination(data['qmaps'],{j:cr['right'][j][k] for j in range(34) if cr['right'][j][k]})
        audit.verify_map(F,('new_primary_image_basis',k))
        vv=primary['quotient'](unit_image(F))
        vv=[sum(x*y for x,y in zip(row,vv)) for row in cr['left']]
        check(vv==[int(j==k) for j in range(5)],'new_counit_image_basis_primitive',k)
        new_primary_maps.append(F)

    record={
      'schema':'marici.branch_a.milnor_totalization_conductor_costalk.v1',
      'scope':{'coefficient_ring':old['scope']['ring'],'target':'N_ext={c in C_beta:q(c)=v(c)=v(dc)=0}',
        'conductor':'A=R/I','computed_costalk_component':'Hom_D(R)(A[2],N_ext), occurrence map degree0, regulator grade3',
        'normalization_totalization_source_degree':3,'all_occurrence_powers_determined_exactly':True,
        'regulator_zero_geometric_purity_claimed':False,'physical_Delta_J_identified':False},
      'sources':old['sources'],
      'inherited_replay':{'mathematical_sha256':old['mathematical_sha256'],'checks':inherited,'dimensions':old['dimensions']},
      'milnor_totalization':milnor,
      'complete_target_differential':serialize_full_matrix(M.d),
      'source_resolution':old['source_resolution'],
      'costalk':audit.record_solve(data),
      'conductor_valued_control':{'unknowns':len(relative['unknown']),'closed_map_rank':len(relative['maps']),
                  'homotopies':len(relative['hom']),'derived_rank':len(relative['qmaps']),
                  'closed_equations':extension_kernel_record(relative['closed'])},
      'target_primary_homology':{
        'degree2_basis':[serialize_chain(v,M) for v in primary['c2']],
        'degree3_basis':[serialize_chain(v,M) for v in primary['c3']],
        'cycle_equations':extension_kernel_record(primary['closed']),
        'cycle_basis':[serialize_chain(v,M) for v in primary['cycles']],
        'boundary_reduction':primary['reduction'],'rank':5,'H3_zero':True},
      'counit':{'matrix_to_target_H2':counit,'integral_reduction':cr,'rank':3,'kernel_rank':31,
                'new_supported_primary_maps':[audit.serialize_map(F) for F in new_primary_maps]},
      'diagonal_obstruction':{'matrix_from_original40':obmat,'integral_reduction':obred,
            'original_nine_killed_inclusion':lost,'maps':[audit.serialize_map(F) for F in obstruction_maps],
            'same_image_as_counit_kernel':True,'totalization_alone_removes_no_new_class':True},
      'symmetry':{'costalk_reflection':Smat,'fixed_basis':fixed['kernel'],
          'counit_kernel_reflection':Sker,'counit_image_reflection':Sprimary,
          'invariant_ranks':[10,11,1],'invariant_counit_reduction':ir,
          'closed_cochain_reflection':Scoc,'strict_fixed_rank':42,
          'strict_to_derived_invariant_reduction':cir,
          'strict_invariant_representatives':[audit.serialize_map(F) for F in invariant_maps],
          'three_occurrence_orbits':[[audit.serialize_map(F) for F in fam] for fam in orbit_records]},
      'examples':{'three_term_comparison':serialize_chain(L,M),'dL':serialize_chain(dL,M),
          'positive_primary':serialize_chain(U,M),'opposite_primary':serialize_chain(opposite,M),
          'twelve_term_supported_map':audit.serialize_map(example),
          'unit_primary_coordinates':unit_co,'twentyfour_term_invariant_map':audit.serialize_map(invariant_example),
          'invariant_primary_coordinate':exprco[0][0],
          'old_transgression_grade3':serialize_chain(chi,M),
          'transgression_target_homology_coordinates':chi_co,
          'transgression_counit_cokernel_coordinates':transformed_chi[3:]},
      'dimensions':{'costalk_closed_maps':108,'costalk_boundaries':74,'costalk_classes':34,
          'old_obstruction_image':31,'counit_image':3,'target_primary_homology':5,
          'counit_cokernel_in_target_primary':2,'invariant_obstruction':10,
          'invariant_costalk':11,'invariant_primary':1,
          'same_degree_full_Milnor_totalization_maps':0},
      'verification':{'inherited_checks':inherited,'new_checks':sum(COUNTS.values())-inherited,
          'total_checks':sum(COUNTS.values()),'families':dict(sorted(COUNTS.items()))}}
    encoded=json.dumps(record,sort_keys=True,separators=(',',':')).encode()
    record['mathematical_sha256']=sha256(encoded).hexdigest()
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(record,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'dimensions':record['dimensions'],'new_checks':record['verification']['new_checks'],
        'inherited_checks':inherited,'sha256':record['mathematical_sha256'],'output':str(output)},indent=2))
    return record


if __name__=='__main__':
    parser=argparse.ArgumentParser(description='Exact Milnor totalization and complete conductor-costalk computation')
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name(
        'branch_a_milnor_totalization_conductor_costalk_certificate.json'))
    main_milnor_costalk(parser.parse_args().output)
