#!/usr/bin/env python3
"""Conductor-ideal source relations and derived marked-chain comparisons.

Standalone Python 3 standard-library checker. Reconstructs the full signed
regulator complex and its complete endpoint/Q frame. Computes the actual
first-conductor associated-grade cycle spaces, their quadratic obstruction,
the uniquely liftable sublattices, and the symmetry action on those lattices.
No physical conductor--Morse map is assigned or inferred from signatures.
The source module is the actual conductor ideal, resolved by alternating
Koszul words; all target frame and normal data are retained.

Derived from the explicitly reconstructed coefficient framework in
branch_a_first_conductor_coherent_primary_lifts_checker.py. All reused
algebraic routines are included; no companion files or network are required.
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



# The following routines implement the new source-side test. The algebraic
# routines above reconstruct (rather than import) the preceding target model.
from functools import lru_cache

@lru_cache(None)
def resolution_words(n: int, first_side: int = -1) -> tuple:
    if n==0:return ((),)
    out=[]
    sides=range(2) if first_side<0 else (first_side,)
    for side in sides:
        sheet=tuple(sorted((MINUS,PLUS)[side]))
        for k in range(1,min(3,n)+1):
            for block in combinations(sheet,k):
                for tail in resolution_words(n-k,1-side):
                    out.append((block,)+tail)
    return tuple(sorted(out))


def word_differential(w: tuple) -> dict:
    if not w:return {}
    block=w[0];out={}
    for k,a in enumerate(block):
        rem=block[:k]+block[k+1:]
        target=((rem,)+w[1:]) if rem else w[1:]
        put(out,(target,monomial('X'+a)),(-1)**k)
    return out


def word_apply_d(v: dict) -> dict:
    out={}
    for (w,p),c in v.items():
        for (v0,q),a in word_differential(w).items():
            pp=tuple(x+y for x,y in zip(p,q))
            if survives(pp):put(out,(v0,pp),c*a)
    return out


def word_contract(v: dict) -> dict:
    """Coefficient-base-linear, not R-linear, contraction in all word degrees.

    Coefficients are pure-sheet monomials. If their sheet differs from the
    first block, prepend their first occurring variable. Otherwise use the
    ordered polynomial Koszul contraction on that block. Independent long
    variables and beta remain coefficients in the base ring.
    """
    out={}
    for (w,p),c in v.items():
        present=tuple(a for a in SHORT_ORDER if p[DIAGONALS.index(a)])
        if not w and not present:continue
        opposite=bool(present and w and ((present[0] in PLUS)!=(w[0][0] in PLUS)))
        if not w or opposite:
            a=present[0];pp=list(p);pp[DIAGONALS.index(a)]-=1
            put(out,(((a,),)+w,tuple(pp)),c)
        else:
            block=w[0];a=min(set(block)|set(present))
            if a in block:continue
            pp=list(p);pp[DIAGONALS.index(a)]-=1
            target=(tuple(sorted(block+(a,))),)+w[1:]
            put(out,(target,tuple(pp)),c*(-1)**sum(j<a for j in block))
    return out


def word_reflect(w: tuple) -> tuple[tuple,int]:
    blocks=[[polygon_diagonal(a,0,1) for a in block] for block in w]
    return tuple(tuple(sorted(block)) for block in blocks),__import__('math').prod(list_parity(b) for b in blocks)


def sparse_solve(rows: list[dict], n: int, label: str) -> dict:
    """Integral row elimination; require every nonzero pivot to be a unit.

    Produces exact equations and a complete integer kernel basis. Each
    equation is obtained by subtracting integer multiples of earlier unit
    rows. Reconstructs all input rows and verifies the kernel on all rows.
    """
    pivots={};logs=[]
    for ri,source in enumerate(rows):
        row=dict(source);log=[]
        while row:
            k=min(row)
            if k in pivots:
                q=row[k];row=add(row,pivots[k],-q);log.append((k,q))
            else:
                q=row[k];check(abs(q)==1,'new_unit_row_pivot',(label,ri,k,q))
                row={j:v*q for j,v in row.items()};pivots[k]=row
                log.append(('pivot',k,q));break
        logs.append(log)
    free=sorted(set(range(n))-set(pivots));basis=[]
    for f in free:
        vec={f:1}
        for k in sorted(pivots,reverse=True):
            x=-sum(v*vec.get(j,0) for j,v in pivots[k].items() if j!=k)
            if x:vec[k]=x
        for ri,row in enumerate(rows):
            check(sum(v*vec.get(j,0) for j,v in row.items())==0,'new_kernel_equation',(label,f,ri))
        check([vec.get(g,0) for g in free]==[int(g==f) for g in free],'new_kernel_free_coordinates',(label,f))
        basis.append(vec)
    # Replay operations against the original rows to certify all ranks.
    for ri,(source,log) in enumerate(zip(rows,logs)):
        row=dict(source)
        for op in log:
            if op[0]=='pivot':
                _,k,q=op;row={j:v*q for j,v in row.items()}
                check(row==pivots[k],'new_echelon_pivot_replay',(label,ri))
                row={}
            else:
                k,q=op;row=add(row,pivots[k],-q)
        check(not row,'new_echelon_row_replay',(label,ri))
    return {'rank':len(pivots),'free':free,'basis':basis,
            'echelon':[[k,sorted(v.items())] for k,v in sorted(pivots.items())],
            'operations':logs}


def sparse_coordinates(v: dict, sol: dict, label: str) -> list[int]:
    c=[v.get(j,0) for j in sol['free']];reconstructed={}
    for z,w in zip(c,sol['basis']):reconstructed=add(reconstructed,w,z)
    check(v==reconstructed,'new_solution_coordinate_reconstruction',label)
    return c


def generic_component(M: Complex, m: tuple[int,...]) -> dict:
    coeff={}
    for j,(F,H,e) in enumerate(M.states):
        p=list(m)+[0]
        for a in F:p[DIAGONALS.index(a)]+=1
        for a in H:p[DIAGONALS.index(a)]-=1
        p[DIAGONALS.index(M.occurrence)]-=e
        if min(p)<0 or not survives(tuple(p)) or not conductor_order(tuple(p)):continue
        coeff[j]=tuple(p)
    d={j:{} for j in coeff}
    for j,p in coeff.items():
        for (i,q),v in M.d[j].items():
            pp=tuple(x+y for x,y in zip(p,q))
            if not survives(pp):continue
            check(i in coeff and pp[:9]==coeff[i][:9],'new_multidegree_closure',(m,j,i))
            put(d[j],i,v)
    K=full_endpoint_q_kernel(M,coeff,d,'source_relation_'+str(m))
    ids=[j for j in sorted(K['ids']) if M.degree[j]==4 and M.weight[j]<=3]
    polys=[]
    for j in ids:
        out={}
        for i,z in K['inclusion'][j].items():
            p=list(coeff[i]);p[9]=3-M.weight[i]
            put(out,(i,tuple(p)),z)
        polys.append(out)
    return {'coeff':coeff,'kernel':K,'ids':ids,'polys':polys}


def degree4_coordinates(v: dict, data: dict, M: Complex) -> list[int]:
    raw={}
    for (j,p),z in v.items():
        check(p[:9]==data['coeff'][j][:9] and p[9]==3-M.weight[j],
              'new_degree4_exact_grading',j)
        put(raw,(j,p[9]),z)
    v0=weighted_vector_apply(data['kernel']['full_basis_inverse'],raw,M.weight)
    check(all(j in data['ids'] for j,p in v0),'new_degree4_in_frame_kernel')
    c=[v0.get((j,3-M.weight[j]),0) for j in data['ids']]
    rr={}
    for z,w in zip(c,data['polys']):rr=add(rr,w,z)
    check(rr==v,'new_degree4_coordinate_reconstruction')
    return c


def map_from_coordinates(v: dict, descriptors: list, target_vectors: list) -> dict:
    out={}
    for j,z in v.items():
        typ,w,_=descriptors[j]
        out[w]=add(out.get(w,{}),target_vectors[j],z)
    return {w:c for w,c in out.items() if c}


def verify_source_map(f: dict, words: dict, M: Complex, label: str) -> None:
    for n in (1,2,3):
        for w in words[n]:
            rhs={}
            if n>1:
                for (v,p),z in word_differential(w).items():rhs=add(rhs,multiply(f.get(v,{}),p,z))
            check(apply(M.d,f.get(w,{}))==rhs,'new_resolved_source_chain_equation',(label,w))
            check(not restrict(f.get(w,{}),M.V) and not restrict(f.get(w,{}),M.Q),
                  'new_resolved_map_full_endpoint_Q_zero',(label,w))
            check(not restrict(apply(M.d,f.get(w,{})),M.V),
                  'new_resolved_map_endpoint_attachment_zero',(label,w))


def serialize_source_map(f: dict, M: Complex) -> list:
    return [{'source_word':[list(a) for a in w],'source_degree':sum(map(len,w))+2,
             'image':serialize_chain(v,M)} for w,v in sorted(f.items())]


def main_source_comparison(output: Path) -> dict:
    import time
    start=time.time();M=Complex();cases={d:{2:truncation_data(M,d,2)} for d in SHORT_ORDER}
    check([len(cases[d][2]['cycles']) for d in SHORT_ORDER]==[9,9,7,7,9,19],
          'new_reconstructed_sixty_target_lifts')
    # The infinite resolution is defined by the word formula; degrees 0..4
    # are enumerated for chain checks. Only degrees 1..3 enter any map to N.
    words={n:resolution_words(n) for n in range(5)}
    check([len(words[n]) for n in range(4)]==[1,6,24,92],'new_source_resolution_ranks')
    for n in range(1,5):
        for w in words[n]:check(not word_apply_d(word_differential(w)), 'new_word_resolution_d_squared',(n,w))
    # Explicit coefficient-base contraction, verified on finite controls;
    # its all-monomial proof is given independently in the proof document.
    monomials=[ZERO]
    for side in (sorted(MINUS),sorted(PLUS)):
        for a in side:
            for k in (1,2,3):monomials.append(monomial(*(['X'+a]*k)))
        for a,c in combinations(side,2):
            monomials.extend((monomial('X'+a,'X'+c),monomial('X'+a,'X'+a,'X'+c)))
        monomials.append(monomial(*('X'+a for a in side)))
    for n in range(4):
        for w in words[n]:
            for p in monomials:
                v={(w,p):1}
                lhs=add(word_apply_d(word_contract(v)),word_contract(word_apply_d(v)))
                rhs={} if n==0 and p==ZERO else v
                check(lhs==rhs,'new_word_resolution_contraction_control',(w,p))
    descriptors=[];vectors=[];case_offsets={};offset=0
    for a in SHORT_ORDER:
        case_offsets[a]=offset
        for k,v in enumerate(cases[a][2]['cycles']):
            descriptors.append((0,((a,),),k));vectors.append(v);offset+=1
    check(offset==60,'new_bottom_variable_count')
    extra={};extra_offsets={}
    for w in words[2]:
        m=[0]*9
        for block in w:
            for a in block:m[DIAGONALS.index(a)]+=1
        key=tuple(m)
        if key not in extra:extra[key]=generic_component(M,key)
        data=extra[key];extra_offsets[w]=(len(vectors),key)
        for k,v in enumerate(data['polys']):descriptors.append((1,w,k));vectors.append(v)
    check(len(vectors)==348,'new_total_comparison_unknowns')
    # All linear equations: dY=0 already solved in the sixty-variable basis.
    # The first equations are dA=F(dP1); the second are F(dP2)=0.
    colseq=[];strict_cols=[]
    for j,(typ,w,k) in enumerate(descriptors):
        col={};v=vectors[j]
        if typ==0:
            for ri,r in enumerate(words[2]):
                rhs={}
                for (ww,p),z in word_differential(r).items():
                    if ww==w:rhs=add(rhs,multiply(v,p,z))
                for (i,p),z in rhs.items():put(col,(0,ri,i,p),-z)
            strict_cols.append(dict(col))
        else:
            ri=words[2].index(w)
            for (i,p),z in apply(M.d,v).items():put(col,(0,ri,i,p),z)
            for si,r in enumerate(words[3]):
                for (ww,p),z in word_differential(r).items():
                    if ww!=w:continue
                    for (i,pp),c in multiply(v,p,z).items():put(col,(1,si,i,pp),c)
        colseq.append(col)
    rows=sorted({r for col in colseq for r in col})
    equations=[{j:c[r] for j,c in enumerate(colseq) if r in c} for r in rows]
    sol=sparse_solve(equations,len(vectors),'coherent_conductor_ideal_source')
    strict_rows=sorted({r for col in strict_cols for r in col})
    strict_eq=[{j:c[r] for j,c in enumerate(strict_cols) if r in c} for r in strict_rows]
    ss=sparse_solve(strict_eq,60,'strict_conductor_ideal_source')
    check((len(ss['basis']),len(sol['basis']))==(16,40),'new_strict_and_resolved_ranks')
    for i,v in enumerate(sol['basis']):verify_source_map(map_from_coordinates(v,descriptors,vectors),words,M,str(i))
    for i,v in enumerate(ss['basis']):verify_source_map(map_from_coordinates(v,descriptors,vectors),words,M,'strict'+str(i))
    # Degree +1 comparison homotopies have no target columns: N4 at a
    # generator's single occurrence degree is zero; all other targets >4.
    for a in SHORT_ORDER:
        c,_=occurrence_component(M,a,True)
        check(not any(M.degree[j]>=4 for j in c),'new_no_source_map_chain_homotopies',a)
    Y=[[v.get(j,0) for v in sol['basis']] for j in range(60)]
    yy=integer_diagonalize(Y,'resolved_generator_evaluation')
    check(yy['rank']==34 and all(x==1 for x in yy['diagonal']), 'new_generator_evaluation_rank_and_saturation')
    # Natural source reflection and published target reflection.
    action={}
    for j,(typ,w,k) in enumerate(descriptors):
        sw,sg=word_reflect(w);v={key:sg*z for key,z in polygon_action(M,vectors[j],0,1).items()}
        if typ==0:
            a=sw[0][0];c=cycle_coordinates(v,cases[a][2],M);off=case_offsets[a]
        else:
            off,key=extra_offsets[sw];c=degree4_coordinates(v,extra[key],M)
        action[j]={off+i:z for i,z in enumerate(c) if z}
    for n in (1,2,3):
        for w in words[n]:
            sw,sg=word_reflect(w)
            lhs={}
            for (v,p),z in word_differential(w).items():
                vv,vg=word_reflect(v);pp=[0]*10;pp[9]=p[9]
                for k,a in enumerate(DIAGONALS):pp[DIAGONALS.index(polygon_diagonal(a,0,1))]=p[k]
                put(lhs,(vv,tuple(pp)),z*vg)
            check(lhs=={k:sg*v for k,v in word_differential(sw).items()},'new_source_reflection_chain_equation',w)
    for j in action:check(int_apply(action,action[j])=={j:1},'new_comparison_reflection_square',j)
    Scols=[]
    for k,v in enumerate(sol['basis']):
        av=int_apply(action,v);Scols.append(sparse_coordinates(av,sol,'resolved_reflect'+str(k)))
    S=dense_columns(Scols,40);invs=fixed_lattice(S,'resolved_source_invariants')
    Sstrict=dense_columns([sparse_coordinates(int_apply(action,v),ss,'strict_reflect'+str(k))
                           for k,v in enumerate(ss['basis'])],16)
    invstrict=fixed_lattice(Sstrict,'strict_source_invariants')
    # The six higher-only maps form kernel of generator evaluation.
    high_basis=[{i:z for i,z in enumerate(col) if z} for col in zip(*yy['kernel'])]
    Sh=[]
    for k,v in enumerate(high_basis):
        av={i:z for i,z in enumerate([sum(S[i][j]*v.get(j,0) for j in v) for i in range(40)]) if z}
        cv=[sum(yy['right_inverse'][i][j]*av.get(j,0) for j in av) for i in range(40)]
        check(not any(cv[:34]),'new_higher_only_reflection_closed',k);Sh.append(cv[34:])
    Sh=dense_columns(Sh,6);ih=fixed_lattice(Sh,'higher_only_source_invariants')
    embedding=dense_columns([sparse_coordinates(v,sol,'strict_in_resolved'+str(i))
                             for i,v in enumerate(ss['basis'])],40)
    er=integer_diagonalize(embedding,'strict_source_inclusion')
    check(er['rank']==16 and all(x==1 for x in er['diagonal']),'new_strict_inclusion_saturated')
    # Test the invariant image, including its integral index.
    image_basis=dense_product(Y,[row[:34] for row in yy['right']])
    _,bottom_reflection=reflection_matrix(M,cases,2)
    image_action_full=dense_product(yy['left'],dense_product(bottom_reflection,image_basis))
    check(not any(v for row in image_action_full[34:] for v in row),
          'new_generator_image_reflection_stable')
    image_action=image_action_full[:34]
    image_fixed=fixed_lattice(image_action,'generator_image_invariants')
    fixed_to_image=dense_product(yy['left'],dense_product(Y,invs['kernel']))[:34]
    image_fixed_coordinates=dense_product(image_fixed['right_inverse'],fixed_to_image)
    check(not any(v for row in image_fixed_coordinates[:image_fixed['rank']] for v in row),
          'new_fixed_source_map_has_fixed_generator_image')
    fixed_image_reduction=integer_diagonalize(image_fixed_coordinates[image_fixed['rank']:],
                                            'fixed_source_to_fixed_generator_image')
    # Reconstruct all three occurrence-mark targets and transport every fixed
    # resolved map, with the natural exterior action on the source words.
    def transport_map(f,rot=0,refl=0):
        out={}
        for w,v in f.items():
            blocks=[[polygon_diagonal(a,rot,refl) for a in block] for block in w]
            sw=tuple(tuple(sorted(block)) for block in blocks)
            sg=__import__('math').prod(list_parity(block) for block in blocks)
            out[sw]=add(out.get(sw,{}),polygon_action(M,v,rot,refl),sg)
        return {w:v for w,v in out.items() if v}
    orbit_models=[M,Complex('15'),Complex('13')]
    fixed_families=[]
    for k,col in enumerate(zip(*invs['kernel'])):
        coord={}
        for i,z in enumerate(col):coord=add(coord,sol['basis'][i],z)
        f=map_from_coordinates(coord,descriptors,vectors)
        check(transport_map(f,0,1)==f,'new_fixed_map_literal_reflection',k)
        family=[]
        for rot,model in enumerate(orbit_models):
            g=transport_map(f,rot,0)
            verify_source_map(g,words,model,'fixed_orbit_'+str((k,rot)))
            family.append(g)
        check(transport_map(f,3,0)==f,'new_map_rotation_cubed',k)
        for rot in range(3):
            check(transport_map(family[rot],0,1)==family[(-rot)%3],
                  'new_map_orbit_reflection_relation',(k,rot))
        fixed_families.append([serialize_source_map(g,M) for g in family])
    # Explicit source-defined scalar polynomial lift of sigma_alt.
    scalar={'02':('14',-1),'04':('25',-1),'13':('25',1),
            '15':('03',1),'24':('03',-1),'35':('14',1)}
    for a,(l,sg) in scalar.items():
        multidegree=[0]*9;multidegree[DIAGONALS.index(a)]+=1;multidegree[DIAGONALS.index(l)]+=1
        evaluated_component=generic_component(M,tuple(multidegree))
        check(not evaluated_component['ids'],'new_sigma_image_has_no_degree_four_boundaries',(a,l))
    evaluated=[]
    for k,v in enumerate(sol['basis']):
        f=map_from_coordinates(v,descriptors,vectors);z={}
        for a,(l,sg) in scalar.items():z=add(z,multiply(f.get(((a,),),{}),monomial('X'+l),sg))
        check(not apply(M.d,z),'new_source_sigma_image_is_cycle',k)
        check(not restrict(z,M.V) and not restrict(z,M.Q),'new_source_sigma_preserves_frame',k)
        evaluated.append(z)
    erows=sorted({row for c in evaluated for row in c})
    es=sparse_solve([{j:c[r] for j,c in enumerate(evaluated) if r in c} for r in erows],40,'source_sigma_evaluation')
    check(es['rank']==34,'new_source_sigma_same_kernel_as_generator_readout')
    # A concrete strict map from one actual marked-gallery pair.
    F=('03','13','35');E=('13','35')
    raw=add(unit(M.index[F,F,0]),multiply(unit(M.index[E,E,0]),monomial('beta')),-1)
    gallery={((a,),):multiply(raw,monomial('X'+a)) for a in sorted(MINUS)}
    verify_source_map(gallery,words,M,'explicit_gallery_conductor_map')
    sigmag={}
    for a,(l,sg) in scalar.items():sigmag=add(sigmag,multiply(gallery.get(((a,),),{}),monomial('X'+l),sg))
    # Symmetrize as a sum, not averaging; natural action exchanges inputs.
    gallery_s={}
    for w,v in gallery.items():
        sw,sg=word_reflect(w);gallery_s[sw]={k:sg*z for k,z in polygon_action(M,v,0,1).items()}
    gallery_invariant={w:add(gallery.get(w,{}),gallery_s.get(w,{})) for w in set(gallery)|set(gallery_s)}
    verify_source_map(gallery_invariant,words,M,'explicit_invariant_gallery_map')
    # Examples chosen by exact sparsity of the constructed solution bases.
    def size(f):return sum(len(v) for v in f.values())
    resolved_maps=[map_from_coordinates(v,descriptors,vectors) for v in sol['basis']]
    nonstrict=[(size(f),i) for i,f in enumerate(resolved_maps) if any(len(w)>1 for w in f)]
    ix=min(nonstrict)[1]
    higher_maps=[]
    for hc in high_basis:
        vv={}
        for i,z in hc.items():vv=add(vv,sol['basis'][i],z)
        ff=map_from_coordinates(vv,descriptors,vectors)
        check(all(len(w)>1 for w in ff),'new_higher_only_map_bottom_zero')
        verify_source_map(ff,words,M,'higher_only')
        higher_maps.append(ff)
    hi=min(range(6),key=lambda i:size(higher_maps[i]))
    # Certificates record only checked scope; no physical selector is set.
    cert={'schema':'marici.branchA.conductor_ideal_source_relations.v1',
          'scope':'source module I in homological degree 3, occurrence-degree preserving, total regulator-normal grade 3, coefficient target N inside IC_beta with complete endpoint/Q frame',
          'repository_commit':COMMIT,
          'source_word_resolution_ranks':[len(words[n]) for n in range(5)],
          'source_basis':{str(n):[list(w) for w in words[n]] for n in (1,2,3)},
          'source_differentials':{str(n):[{'word':list(w),'boundary':[{'word':list(v),'coefficient':list(p),'integer':z} for (v,p),z in word_differential(w).items()]} for w in words[n]] for n in (1,2,3)},
          'target_states':[[j,list(F),list(H),e,M.degree[j]] for j,(F,H,e) in enumerate(M.states)],
          'target_differential':serialize_full_matrix(M.d),
          'target_generator_lift_basis':[{'input':list(w),'image':serialize_chain(v,M)} for (_,w,k),v in zip(descriptors[:60],vectors[:60])],
          'higher_source_mapping_basis':[{'input':list(w),'image':serialize_chain(v,M)} for (_,w,k),v in zip(descriptors[60:],vectors[60:])],
          'counts':{'independent_six_generator_lifts':60,'strict_source_maps':16,'resolved_source_maps':40,
                    'resolved_bottom_image_rank':34,'higher_only_maps':6,'strict_symmetry_fixed_rank':invstrict['fixed_rank'],
                    'resolved_symmetry_fixed_rank':invs['fixed_rank'],'higher_only_symmetry_fixed_rank':ih['fixed_rank'],
                    'fixed_generator_image_rank':image_fixed['fixed_rank'],
                    'fixed_generator_evaluation_diagonal':fixed_image_reduction['diagonal'],
                    'coherent_unknowns':len(vectors),'coherent_equations':len(rows),'coherent_equation_rank':sol['rank']},
          'strict_equations':[[[j,v] for j,v in sorted(r.items())] for r in strict_eq],
          'coherent_equations':[[[j,v] for j,v in sorted(r.items())] for r in equations],
          'strict_solution':ss,'coherent_solution':sol,
          'strict_to_resolved_inclusion':embedding,
          'bottom_evaluation_matrix':Y,'bottom_evaluation_reduction':yy,
          'reflection':S,'strict_reflection':Sstrict,'higher_only_reflection':Sh,
          'fixed_resolved_basis':invs,'fixed_strict_basis':invstrict,'fixed_higher_only_basis':ih,
          'generator_image_reflection':image_action,'fixed_generator_image_basis':image_fixed,
          'invariant_generator_evaluation_reduction':fixed_image_reduction,
          'full_D3_resolved_map_families':fixed_families,
          'resolved_map_basis':[serialize_source_map(f,M) for f in resolved_maps],
          'higher_only_map_basis':[serialize_source_map(f,M) for f in higher_maps],
          'source_sigma_coefficients':scalar,'source_sigma_images':[serialize_chain(v,M) for v in evaluated],
          'examples':{'strict_gallery_source_map':serialize_source_map(gallery,M),
                      'strict_gallery_sigma_image':serialize_chain(sigmag,M),
                      'invariant_gallery_source_map':serialize_source_map(gallery_invariant,M),
                      'coherent_nonstrict_map':serialize_source_map(resolved_maps[ix],M),
                      'higher_only_map':serialize_source_map(higher_maps[hi],M)},
          'physical_conductor_morse_identification':False,
          'exact_checks':sum(COUNTS.values()),'verification_counts':dict(sorted(COUNTS.items())),
          'references':['https://arxiv.org/abs/0704.3631','https://stacks.math.columbia.edu/tag/0A8H','https://stacks.math.columbia.edu/tag/0643']}
    text=json.dumps(cert,indent=2,sort_keys=True)+'\n';output.parent.mkdir(parents=True,exist_ok=True);output.write_text(text)
    print(json.dumps({'output':str(output),'certificate_sha256':sha256(text.encode()).hexdigest(),
                      'counts':cert['counts'],'exact_checks':cert['exact_checks'],'seconds':round(time.time()-start,3)},indent=2))
    return cert

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('branch_a_conductor_ideal_source_relations_certificate.json'))
    main_source_comparison(parser.parse_args().output)
