#!/usr/bin/env python3
"""Normalization-sheet extension of the framed conductor-ideal comparison.

Standalone standard-library checker. Reconstructs the 430-state framed target,
the conductor-ideal and normalization resolutions, the complete source
map equations, and their coherent extension obstructions. Does not assign the physical conductor--Morse comparison.

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



# ---------- Normalization-sheet extension and conductor-frame forgetting ----------

from fractions import Fraction


def unimodular_inverse(a, label):
    n=len(a)
    rows=[[Fraction(x) for x in a[i]]+[Fraction(i==j) for j in range(n)] for i in range(n)]
    for c in range(n):
        p=next(i for i in range(c,n) if rows[i][c])
        rows[c],rows[p]=rows[p],rows[c]
        v=rows[c][c];rows[c]=[x/v for x in rows[c]]
        for i in range(n):
            if i!=c and rows[i][c]:
                v=rows[i][c];rows[i]=[x-v*y for x,y in zip(rows[i],rows[c])]
    check(all(x.denominator==1 for row in rows for x in row[n:]),'inverse_is_integral',label)
    inv=[[int(x) for x in row[n:]] for row in rows]
    check(dense_product(a,inv)==dense_identity(n),'unimodular_inverse_identity',label)
    check(dense_product(inv,a)==dense_identity(n),'unimodular_inverse_other_identity',label)
    return inv


class ExtensionAudit:
    def __init__(self):
        self.M=Complex()
        self.presentation=source_resolution()
        self.components={}
        self.I=self.ideal_source()
        self.Q=self.normalization_source()
        self.j={sid:{} for sid in self.I}
        for sid,g in self.I.items():
            if sid[0]==0:
                a=SHORT_ORDER[sid[1]]
                self.j[sid]={((0,0 if a in PLUS else 1),monomial('X'+a)):1}
        self.verify_source(self.I,'ideal')
        self.verify_source(self.Q,'normalization')
        dQ={sid:g['d'] for sid,g in self.Q.items()}
        for sid,g in self.I.items():
            check(apply(dQ,self.j[sid])==apply(self.j,g['d']),
                  'resolved_ideal_normalization_inclusion_chain',sid)
        self.cone=self.conductor_cone()
        self.verify_source(self.cone,'doubled_conductor_cone')

    def component(self,weight,relative):
        key=(tuple(weight),relative)
        if key in self.components:return self.components[key]
        M=self.M;coeff={}
        for j,(F,H,e) in enumerate(M.states):
            p=list(weight)+[0]
            for a in F:p[DIAGONALS.index(a)]+=1
            for a in H:p[DIAGONALS.index(a)]-=1
            p[DIAGONALS.index(M.occurrence)]-=e
            if min(p)<0 or not survives(tuple(p)) or (relative and not conductor_order(tuple(p))):continue
            coeff[j]=tuple(p)
        d={j:{} for j in coeff}
        for j,p in coeff.items():
            for (i,q),s in M.d[j].items():
                pp=tuple(a+c for a,c in zip(p,q))
                if survives(pp):
                    check(i in coeff and pp[:9]==coeff[i][:9],
                          'extension_target_multidegree_closure',(key,j,i))
                    check(pp[9]==M.weight[j]-M.weight[i],
                          'extension_target_regulator_weight',(key,j,i))
                    put(d[j],i,s)
        ker=full_endpoint_q_kernel(M,coeff,d,repr(key))
        self.components[key]=(coeff,ker)
        return coeff,ker

    def target_basis(self,weight,degree,relative):
        coeff,k=self.component(weight,relative);out=[]
        for j in sorted(k['ids']):
            if self.M.degree[j]!=degree or self.M.weight[j]>3:continue
            v={}
            for i,c in k['inclusion'][j].items():
                p=list(coeff[i]);p[9]=3-self.M.weight[i]
                v[i,tuple(p)]=c
            check(next(iter(v))[0]==j and next(iter(v.values()))==1,
                  'target_basis_coordinate_is_identity',(weight,degree,j))
            out.append(v)
        return out

    def ideal_source(self):
        p=self.presentation;src={}
        for i,a in enumerate(SHORT_ORDER):
            src[0,i]={'degree':0,'weight':monomial('X'+a)[:9],'d':{}}
        for i,r in enumerate(p['relations']):
            src[1,i]={'degree':1,'weight':r['weight'],
                      'd':{((0,j),m):c for (j,m),c in p['d1'][i].items()}}
        for i,r in enumerate(p['syzygies']):
            src[2,i]={'degree':2,'weight':r['weight'],
                      'd':{((1,j),m):c for (j,m),c in p['d2'][i].items()}}
        return src

    def normalization_source(self):
        # Q0=R b_plus + R b_minus. The annihilator of b_plus is I_minus,
        # and the annihilator of b_minus is I_plus. Higher terms resolve those ideals.
        src={(0,0):{'degree':0,'weight':(0,)*9,'d':{}},
             (0,1):{'degree':0,'weight':(0,)*9,'d':{}}}
        for i,a in enumerate(SHORT_ORDER):
            src[1,i]={'degree':1,'weight':monomial('X'+a)[:9],
                      'd':{((0,1 if a in PLUS else 0),monomial('X'+a)):1}}
        for (degree,i),g in self.I.items():
            if degree:
                src[degree+1,i]={'degree':degree+1,'weight':g['weight'],
                    'd':{((q[0]+1,q[1]),m):c for (q,m),c in g['d'].items()}}
        return src

    def conductor_cone(self):
        # E_n = Q_{n-2} + P_{n-3}; differential (-d_Q q-j p, d_P p).
        # E resolves the doubled upper conductor in degree 2. This is a signed
        # cone model; the sign convention is exported rather than suppressed.
        src={}
        for sid,g in self.Q.items():
            src['Q',sid]={'degree':g['degree']+2,'weight':g['weight'],
                'd':{(('Q',q),m):-c for (q,m),c in g['d'].items()}}
        for sid,g in self.I.items():
            d={(('P',q),m):c for (q,m),c in g['d'].items()}
            for (q,m),c in self.j[sid].items():put(d,(('Q',q),m),-c)
            src['P',sid]={'degree':g['degree']+3,'weight':g['weight'],'d':d}
        return src

    def verify_source(self,source,label):
        d={sid:g['d'] for sid,g in source.items()}
        for sid,g in source.items():
            check(not apply(d,g['d']),'resolved_source_d_squared',(label,sid))
            for (dest,p),c in g['d'].items():
                check(source[dest]['degree']==g['degree']-1,
                      'resolved_source_degree',(label,sid,dest))
                check(tuple(x+y for x,y in zip(source[dest]['weight'],p[:9]))==g['weight'],
                      'resolved_source_occurrence_degree',(label,sid,dest))

    def hom(self,source,relative,homdeg=0,shift=3,label=''):
        unknown=[]
        for sid,g in source.items():
            n=g['degree']+shift+homdeg
            if n<0 or n>4:continue
            for v in self.target_basis(g['weight'],n,relative):unknown.append((sid,v))
        columns={}
        for ui,(sid,v) in enumerate(unknown):
            col={}
            for (ti,p),c in apply(self.M.d,v).items():put(col,(sid,ti,p),c)
            for dest,g in source.items():
                for (sc,p),c in g['d'].items():
                    if sc==sid:
                        for (ti,pm),z in multiply(v,p,-((-1)**homdeg)*c).items():
                            put(col,(dest,ti,pm),z)
            columns[ui]=col
        kernel=unit_kernel(columns,label=label)
        def pack(v):
            out={}
            for ui,c in v.items():
                sid,col=unknown[ui];out[sid]=add(out.get(sid,{}),col,c)
            return {s:c for s,c in out.items() if c}
        maps=[pack(v) for v in kernel['basis']]
        result={'unknown':unknown,'columns':columns,'kernel':kernel,'maps':maps,
                'pack':pack,'source':source,'relative':relative,'homdeg':homdeg,'shift':shift}
        for j,mp in enumerate(maps):
            check(not self.hom_differential(source,mp,homdeg),
                  'complete_exported_map_is_closed',(label,j))
            self.verify_frame(mp,relative,(label,j))
        return result

    def hom_differential(self,source,mp,homdeg=0):
        out={}
        for sid,g in source.items():
            v=apply(self.M.d,mp.get(sid,{}))
            for (sc,p),c in g['d'].items():
                v=add(v,multiply(mp.get(sc,{}),p,-((-1)**homdeg)*c))
            if v:out[sid]=v
        return out

    def verify_frame(self,mp,relative,label):
        for sid,v in mp.items():
            check(not restrict(v,self.M.V),'complete_endpoint_frame',(label,sid))
            check(not restrict(v,self.M.Q),'complete_Q_frame',(label,sid))
            check(not restrict(apply(self.M.d,v),self.M.V),
                  'incoming_endpoint_frame',(label,sid))
            if relative:
                check(all(conductor_order(p)>0 for ti,p in v),'conductor_image_condition',(label,sid))

    def raw_coordinates(self,hd,mp):
        ans={}
        for ui,(sid,v) in enumerate(hd['unknown']):
            key=next(iter(v));check(v[key]==1,'raw_basis_primitive')
            z=mp.get(sid,{}).get(key,0)
            if z:ans[ui]=z
        check(hd['pack'](ans)==mp,'raw_map_coordinate_reconstruction')
        return ans

    def closed_coordinates(self,hd,mp):
        aa=self.raw_coordinates(hd,mp)
        vv={i:aa.get(fr,0) for i,fr in enumerate(hd['kernel']['free']) if aa.get(fr,0)}
        test={}
        for i,c in vv.items():test=add(test,hd['kernel']['basis'][i],c)
        check(test==aa,'closed_map_coordinate_reconstruction')
        return vv

    def reflect_map(self,mp):
        ri={tuple(r['name']):j for j,r in enumerate(self.presentation['relations'])}
        out={}
        for (degree,i),v in mp.items():
            if degree==0:
                dest=SHORT_ORDER.index(polygon_diagonal(SHORT_ORDER[i],0,1));sg=1
            elif degree==1:
                kind,a,c=self.presentation['relations'][i]['name']
                a=polygon_diagonal(a,0,1);c=polygon_diagonal(c,0,1);sg=1
                if kind=='K' and a>c:a,c,sg=c,a,-1
                dest=ri[kind,a,c]
            else:raise AssertionError('map has an unexpected source degree')
            out[degree,dest]=add({},polygon_action(self.M,v,0,1),sg)
        return out


def flatten_map(mp):
    return {(sid,ti,p):c for sid,v in mp.items() for (ti,p),c in v.items()}


def combine_maps(maps,v):
    out={}
    for j,c in v.items():
        for sid,col in maps[j].items():out[sid]=add(out.get(sid,{}),col,c)
    return {sid:col for sid,col in out.items() if col}


def serialize_map(mp,M):
    return [{'source':sid,'image':serialize_chain(v,M)}
            for sid,v in sorted(mp.items(),key=lambda item:repr(item[0]))]


def serialize_source(src):
    return [{'id':sid,'degree':g['degree'],'weight':g['weight'],
             'differential':[[dest,p,c] for (dest,p),c in sorted(g['d'].items(),key=lambda item:repr(item[0]))]}
            for sid,g in sorted(src.items(),key=lambda item:repr(item[0]))]


def serialize_hom(hd,M,include_maps=True):
    out={'unknown_count':len(hd['unknown']),'differential_rank':hd['kernel']['rank'],
         'closed_rank':len(hd['maps']),
         'unknowns':[{'source':sid,'image':serialize_chain(v,M)} for sid,v in hd['unknown']],
         'differential':[sparse_list(col) for col in hd['columns'].values()],
         'kernel_basis':[sparse_list(v) for v in hd['kernel']['basis']],
         'free_coordinates':hd['kernel']['free'],
         'pivots':[[j,sparse_list(row)] for j,row in hd['kernel']['pivots']]}
    if include_maps:out['closed_maps']=[serialize_map(v,M) for v in hd['maps']]
    return out


def run_normalization_extension(output):
    A=ExtensionAudit();M=A.M
    hn=A.hom(A.I,True,label='conductor_ideal_to_N')
    hhN=A.hom(A.I,True,1,label='conductor_ideal_to_N_homotopies')
    hk=A.hom(A.I,False,label='conductor_ideal_to_K')
    hhK=A.hom(A.I,False,1,label='conductor_ideal_to_K_homotopies')
    hnQ=A.hom(A.Q,True,label='normalization_to_N')
    hkQ=A.hom(A.Q,False,label='normalization_to_K')
    hhQ=A.hom(A.Q,False,1,label='normalization_to_K_homotopies')
    check((len(hn['unknown']),hn['kernel']['rank'],len(hn['maps']))==(604,564,40),
          'replayed_conductor_comparison_lattice')
    check((len(hk['unknown']),hk['kernel']['rank'],len(hk['maps']))==(628,564,64),
          'ambient_framed_closed_map_lattice')
    check((len(hhK['unknown']),hhK['kernel']['rank'],len(hhK['maps']))==(33,33,0),
          'ambient_homotopy_injectivity')
    check(not hhN['unknown'] and not hnQ['unknown'] and not hhQ['unknown'],
          'vanishing_graded_extension_slots')
    check((len(hkQ['unknown']),hkQ['kernel']['rank'],len(hkQ['maps']))==(115,115,0),
          'no_nonzero_normalization_sheet_maps')

    # The 40 conductor maps together with ambient homotopy boundaries.
    fcols={i:flatten_map(mp) for i,mp in enumerate(hn['maps'])}
    joint=dict(fcols)
    for j,col in hhK['columns'].items():joint[40+j]={i:-v for i,v in col.items()}
    extensions=unit_kernel(joint,label='coherent_normalization_extension_equations')
    check((extensions['rank'],len(extensions['basis']))==(64,9),
          'coherent_extension_rank')
    Ecols={j:{i:c for i,c in v.items() if i<40} for j,v in enumerate(extensions['basis'])}
    Emat=dense_columns([[Ecols[j].get(i,0) for i in range(40)] for j in Ecols],40)
    er=integer_diagonalize(Emat,'coherent_extension_saturated_inclusion')
    check(er['rank']==9 and er['diagonal']==[1]*9,'extension_inclusion_has_no_torsion')
    quotient=er['left'][9:]
    ext_data=[]
    for j,v in enumerate(extensions['basis']):
        f=combine_maps(hn['maps'],{i:c for i,c in v.items() if i<40})
        h=hhK['pack']({i-40:c for i,c in v.items() if i>=40})
        check(A.hom_differential(A.I,h,1)==f,'coherent_extension_full_equation',j)
        A.verify_frame(f,True,('extension_ideal',j));A.verify_frame(h,False,('extension_homotopy',j))
        check(set(h)=={(0,SHORT_ORDER.index('35'))},'extension_homotopy_only_on_35',j)
        check(any(conductor_order(p)==0 for col in h.values() for ti,p in col),
              'extension_homotopy_leaves_conductor_filtration',j)
        ext_data.append({'ideal_map':serialize_map(f,M),'normalization_map':[],
                         'compatibility_homotopy':serialize_map(h,M),
                         'ideal_coordinates':sparse_list(Ecols[j])})

    # Verify that these 40 images span all 64 ambient cocycles modulo 33 boundaries.
    kmaps={i:flatten_map(mp) for i,mp in enumerate(hk['maps'])}
    span=dict(kmaps)
    for j,col in hhK['columns'].items():span[64+j]=col
    kr=unit_kernel(span,label='ambient_closed_maps_and_boundaries')
    check(kr['rank']==64,'all_ambient_boundaries_are_closed')
    check(extensions['rank']-hhK['kernel']['rank']==31,
          'conductor_classes_surject_to_ambient_H0')

    # Explicit source-cone obstruction: copy an ideal map to the P summand.
    obstruction_cocycles=[]
    for j,f in enumerate(hn['maps']):
        eta={('P',sid):col for sid,col in f.items()}
        check(not A.hom_differential(A.cone,eta,0),'normalization_connecting_cocycle',j)
        obstruction_cocycles.append(serialize_map(eta,M))
    # A coherent extension makes precisely this source-cone obstruction exact.
    for j,v in enumerate(extensions['basis']):
        h=hhK['pack']({i-40:c for i,c in v.items() if i>=40})
        hcone={('P',sid):col for sid,col in h.items()}
        f=combine_maps(hn['maps'],Ecols[j])
        eta={('P',sid):col for sid,col in f.items()}
        check(A.hom_differential(A.cone,hcone,1)==eta,
              'source_cone_obstruction_primitive',j)

    # Reflection action on all 40 maps and on the 9/31 exact sequence.
    Smcols={j:A.closed_coordinates(hn,A.reflect_map(mp)) for j,mp in enumerate(hn['maps'])}
    for j in Smcols:check(int_apply(Smcols,Smcols[j])=={j:1},'map_reflection_squared',j)
    Sm=dense_columns([[Smcols[j].get(i,0) for i in range(40)] for j in range(40)],40)
    temp=dense_product(er['left'],dense_product(Sm,Emat))
    check(not any(v for row in temp[9:] for v in row),'reflection_preserves_extension_kernel')
    S9=dense_product(er['right'],temp[:9])
    invU=unimodular_inverse(er['left'],'obstruction_quotient_coordinates')
    Snew=dense_product(er['left'],dense_product(Sm,invU))
    check(not any(v for row in Snew[9:] for v in row[:9]),'quotient_reflection_is_defined')
    S31=[row[9:] for row in Snew[9:]]
    fi40=fixed_lattice(Sm,'conductor_map_invariants')
    fi9=fixed_lattice(S9,'coherent_extension_invariants')
    fi31=fixed_lattice(S31,'normalization_obstruction_invariants')
    check((fi40['fixed_rank'],fi9['fixed_rank'],fi31['fixed_rank'])==(13,3,10),
          'normalization_extension_invariant_ranks')
    Im=dense_product(quotient,fi40['kernel'])
    ir=integer_diagonalize(fi31['kernel'],'obstruction_invariant_basis')
    co=dense_product(ir['left'],Im)
    check(not any(v for row in co[10:] for v in row),'invariant_obstruction_target_coordinates')
    ico=dense_product(ir['right'],co[:10])
    idg=integer_diagonalize(ico,'invariant_obstruction_image')
    check(idg['rank']==10 and idg['diagonal']==[1]*10,
          'invariant_obstruction_sequence_saturated')

    # The six source-relation-only maps all survive the new obstruction quotient.
    Ycols={j:{(sid,ti,p):c for sid,col in mp.items() if sid[0]==0 for (ti,p),c in col.items()}
           for j,mp in enumerate(hn['maps'])}
    hy=unit_kernel(Ycols,label='relation_only_source_comparisons')
    R6=dense_columns([[v.get(i,0) for i in range(40)] for v in hy['basis']],40)
    QR6=dense_product(quotient,R6)
    r6=integer_diagonalize(QR6,'relation_only_normalization_obstructions')
    check(len(hy['basis'])==6 and r6['rank']==6 and r6['diagonal']==[1]*6,
          'all_relation_only_maps_remain_obstructed')

    r6basis=integer_diagonalize(R6,'relation_only_primitive_basis')
    relref=dense_product(r6basis['left'],dense_product(Sm,R6))
    check(not any(v for row in relref[6:] for v in row),
          'reflection_preserves_relation_only_maps')
    S6=dense_product(r6basis['right'],relref[:6])
    fi6=fixed_lattice(S6,'relation_only_invariant_obstructions')
    check(fi6['fixed_rank']==2,'two_invariant_relation_only_obstructions')

    # Verify reflected and rotated coherent extension equations on complete targets.
    relindex={tuple(r['name']):j for j,r in enumerate(A.presentation['relations'])}
    def transport(mp,rot=0,ref=0):
        out={}
        for (n,i),col in mp.items():
            if n==0:dst=SHORT_ORDER.index(polygon_diagonal(SHORT_ORDER[i],rot,ref));sg=1
            else:
                kind,a,c=A.presentation['relations'][i]['name']
                a=polygon_diagonal(a,rot,ref);c=polygon_diagonal(c,rot,ref);sg=1
                if kind=='K' and a>c:a,c,sg=c,a,-1
                dst=relindex[kind,a,c]
            out[n,dst]=add({},polygon_action(M,col,rot,ref),sg)
        return out
    orbit_models={o:Complex(o) for o in ('35','15','13')}
    invariant_extensions=[]
    for k in range(3):
        ec={j:fi9['kernel'][j][k] for j in range(9) if fi9['kernel'][j][k]}
        total={}
        for j,c in ec.items():total=add(total,extensions['basis'][j],c)
        f=combine_maps(hn['maps'],{i:c for i,c in total.items() if i<40})
        h=hhK['pack']({i-40:c for i,c in total.items() if i>=40})
        check(A.reflect_map(f)==f and A.reflect_map(h)==h,
              'coherent_extension_invariant_as_chains',k)
        for rot in range(3):
            mf=transport(f,rot);mh=transport(h,rot);mt=orbit_models[polygon_diagonal('35',rot)]
            for sid,g in A.I.items():
                lhs=apply(mt.d,mh.get(sid,{}))
                for (sc,p),c in g['d'].items():lhs=add(lhs,multiply(mh.get(sc,{}),p,c))
                check(lhs==mf.get(sid,{}),'all_orbit_coherent_extension_equations',(k,rot,sid))
            for mp in (mf,mh):
                for sid,col in mp.items():
                    check(not restrict(col,mt.V) and not restrict(col,mt.Q),
                          'all_orbit_endpoint_Q_frames',(k,rot,sid))
                    check(not restrict(apply(mt.d,col),mt.V),
                          'all_orbit_endpoint_connectors',(k,rot,sid))
        invariant_extensions.append({'ideal_map':serialize_map(f,M),
                                     'compatibility_homotopy':serialize_map(h,M)})

    sigma_coefficients={'02':('14',-1),'04':('25',-1),'13':('25',1),
                        '15':('03',1),'24':('03',-1),'35':('14',1)}
    def evaluate_sigma(mp):
        out={}
        for i,a in enumerate(SHORT_ORDER):
            l,sg=sigma_coefficients[a]
            out=add(out,multiply(mp.get((0,i),{}),monomial('X'+l),sg))
        return out
    sigma_columns={}
    for j,v in Ecols.items():sigma_columns[j]=evaluate_sigma(combine_maps(hn['maps'],v))
    sigma_rank=unit_kernel(sigma_columns,label='coherent_extension_symbol_detection')
    check(sigma_rank['rank']==9 and not sigma_rank['basis'],
          'all_coherent_extensions_detected_by_scalar_symbol')

    # Explicit shortest extension representative, chosen only for presentation.
    choices=[]
    for j,v in enumerate(extensions['basis']):
        h=hhK['pack']({i-40:c for i,c in v.items() if i>=40})
        choices.append((sum(map(len,h.values())),j,h))
    count,j,h=min(choices,key=lambda item:(item[0],item[1]))
    U=next(iter(h.values()))
    check(count==3,'three_term_compatibility_example')
    f=combine_maps(hn['maps'],Ecols[j])
    check(len(apply(M.d,U))==9,'three_term_example_has_nine_term_boundary')
    symbol={'02':('14',-1),'04':('25',-1),'13':('25',1),
            '15':('03',1),'24':('03',-1),'35':('14',1)}
    ev={}
    for i,a in enumerate(SHORT_ORDER):
        l,sg=symbol[a];ev=add(ev,multiply(f.get((0,i),{}),monomial('X'+l),sg))
    huv=multiply(U,monomial('X14'))
    check(ev==apply(M.d,huv),'source_scalar_symbol_has_recorded_ambient_primitive')

    # A source-compatible ideal map which provably does not extend to sheets.
    def state(F,H,e):return M.index[tuple(F),tuple(H),e]
    L=add(unit(state(('03','13','35'),('03','13','35'),0)),
          multiply(unit(state(('13','35'),('13','35'),0)),monomial('beta')),-1)
    phi={(0,i):multiply(L,monomial('X'+a)) for i,a in enumerate(SHORT_ORDER) if a in MINUS}
    check(not A.hom_differential(A.I,phi),'negative_sheet_ideal_example_closed')
    phi_coords=A.closed_coordinates(hn,phi)
    obstruction_coordinates=[sum(row[i]*c for i,c in phi_coords.items()) for row in quotient]
    check(any(obstruction_coordinates),'negative_sheet_ideal_example_obstructed')
    check(not A.target_basis(monomial('X02')[:9],4,False),
          'no_homotopy_can_change_negative_example_a02')

    cert={
      'schema':'marici.branchA.normalization_sheet_extension_obstructions.v1',
      'scope':{
        'coefficient_ring':'Z[beta,X_d]/(X_minus X_plus)',
        'source_placement':'I and normalization placed in homological degree 3',
        'occurrence_map_degree':[0]*9,
        'regulator_normal_output_grade':3,
        'K':'full endpoint/Q-zero subcomplex including incoming endpoint boundary',
        'N':'K intersect I C_beta',
        'extension_equation':'delta H = inclusion*f - g*j; f:I[3]->N, g:normalization[3]->K',
        'geometric_source_identification':False,
        'physical_Delta_J_selected':False,
        'beta_zero_geometric_purity_claimed':False,
        'source_resolution_tail':'Exact beyond displayed terms is unnecessary for these degrees; target vanishes above degree 4.'},
      'sources':{
        'repository':'andrey-kokoev/marici','commit':COMMIT,
        'normalization_ledger_blob':'840258522d45e450e4f1e8bb927d9aae58c75566',
        'absolute_target_blob':'b967151cb0ee822e2361b9334a4ab26082c12682',
        'prior_checker_sha256':'6ad40b248557d9ef96f2e5b598a6cd4b5d782f7364919c3287bf23723162848a1e',
        'hom_sign_convention':'Stacks 0A8H','cone_convention':'Stacks 014D','derived_maps':'Stacks 064B'},
      'dimensions':{
        'conductor_ideal_maps':40,'ambient_ideal_cocycles':64,'ambient_ideal_boundaries':33,
        'ambient_ideal_derived_maps':31,'normalization_sheet_derived_maps':0,
        'strict_normalization_extensions':0,'coherent_filtered_extensions':9,
        'genuine_extension_obstructions':31,'relation_only_obstructions':6,
        'invariant_conductor_maps':13,'invariant_coherent_extensions':3,
        'invariant_obstructions':10,'invariant_relation_only_obstructions':2,
        'positive_homotopy_groups_of_extension_components':0},
      'source_complexes':{'ideal_resolution':serialize_source(A.I),
                         'normalization_resolution':serialize_source(A.Q),
                         'ideal_inclusion':[[sid,[[dest,p,c] for (dest,p),c in col.items()]] for sid,col in A.j.items()],
                         'doubled_conductor_cone':serialize_source(A.cone)},
      'target':{'states':M.states,'differential':serialize_full_matrix(M.d)},
      'hom_equations':{'I_to_N':serialize_hom(hn,M),'I_to_K':serialize_hom(hk,M),
                       'I_to_K_homotopies':serialize_hom(hhK,M),
                       'normalization_to_K':serialize_hom(hkQ,M,False),
                       'normalization_to_N_unknowns':len(hnQ['unknown']),
                       'normalization_homotopies_unknowns':len(hhQ['unknown'])},
      'coherent_extensions':{'equation_rank':extensions['rank'],
        'equation_basis':[sparse_list(v) for v in extensions['basis']],
        'basis':ext_data,'inclusion_matrix':Emat,'integral_inclusion_reduction':er,
        'obstruction_readout':quotient,'source_cone_obstruction_cocycles':obstruction_cocycles,
        'relation_only_inclusion':R6,'relation_only_obstruction_coordinates':QR6,
        'source_symbol_on_extension_basis':[serialize_chain(sigma_columns[j],M) for j in range(9)]},
      'symmetry':{'reflection_on_40':Sm,'reflection_on_9':S9,'reflection_on_31':S31,
        'fixed_40_basis':fi40['kernel'],'fixed_9_basis':fi9['kernel'],'fixed_31_basis':fi31['kernel'],
        'invariant_obstruction_map':ico,'invariant_obstruction_diagonal_factors':idg['diagonal'],
        'relation_only_reflection':S6,'relation_only_invariant_basis':fi6['kernel'],
        'explicit_invariant_extensions':invariant_extensions,
        'transported_occurrence_labels':['35','15','13']},
      'examples':{'three_term_homotopy':serialize_map(h,M),
                  'its_ideal_map':serialize_map(f,M),
                  'its_scalar_symbol_image':serialize_chain(ev,M),
                  'scalar_symbol_primitive':serialize_chain(huv,M),
                  'nonextendable_negative_sheet_map':serialize_map(phi,M),
                  'its_obstruction_coordinates':obstruction_coordinates},
      'verification':{'exact_checks':sum(COUNTS.values()),'by_family':dict(sorted(COUNTS.items()))}
    }
    # The precursor's mathematical content is reconstructed, not read at runtime.
    cert['sources'].pop('prior_checker_sha256')
    payload=json.dumps(cert,sort_keys=True,separators=(',',':'))
    cert['mathematical_sha256']=sha256(payload.encode()).hexdigest()
    Path(output).write_text(json.dumps(cert,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'conductor_maps':40,'coherent_extensions':9,'obstructions':31,
                      'invariant_extensions':3,'invariant_obstructions':10,
                      'exact_checks':sum(COUNTS.values()),'certificate':str(output),
                      'sha256':cert['mathematical_sha256']},indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',default='branch_a_normalization_sheet_extension_obstructions_certificate.json')
    run_normalization_extension(parser.parse_args().output)
