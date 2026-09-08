#!/usr/bin/env python3
"""First-conductor symbol lifting and transported dihedral selection.

Standalone Python 3 standard-library checker. Reconstructs the full signed
regulator complex and its complete endpoint/Q frame. Computes the actual
first-conductor associated-grade cycle spaces, their quadratic obstruction,
the uniquely liftable sublattices, and the symmetry action on those lattices.
No physical conductor--Morse map is assigned or inferred from signatures.

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


def main_symbol_lifting(output: Path) -> dict:
    M=Complex(); cases={};result={}
    for a in SHORT_ORDER:
        allcoeff,dd=occurrence_component(M,a,True)
        check(all(M.degree[j]<=3 for j in allcoeff),'no_conductor_relative_degree_four',a)
        top=[j for j in allcoeff if M.degree[j]==3]
        check(all(conductor_order(allcoeff[j])==1 for j in top),
              'every_top_coefficient_has_exact_conductor_order_one',a)
        check(all(1<=conductor_order(p)<=2 for j in top
                  for i,p in apply(M.d,{(j,tuple(list(allcoeff[j][:9])+[3-M.weight[j]])):1})),
              'top_differential_has_no_conductor_order_above_two',a)
        case={k:truncation_data(M,a,k) for k in (1,2,3,4)}
        cases[a]=case
        first=case[1]; full=case[4]
        rows=sorted(j for j,p in allcoeff.items() if M.degree[j]==2 and conductor_order(p)==2)
        obstruction=[]
        columns=[]
        for v in first['cycles']:
            dv=apply(M.d,v)
            check(all(conductor_order(p)==2 for j,p in dv),'first_symbol_defect_exactly_quadratic',a)
            col=[0]*len(rows)
            for (j,p),z in dv.items():
                check(p[:9]==allcoeff[j][:9] and p[9]==3-M.weight[j],
                      'quadratic_obstruction_literal_monomials',(a,j))
                col[rows.index(j)]+=z
            columns.append(col)
        obstruction=dense_columns(columns,len(rows))
        red=integer_diagonalize(obstruction,a+'_quadratic_obstruction')
        check(all(v==1 for v in red['diagonal']),'quadratic_obstruction_saturated_image',a)
        embedding=dense_columns([cycle_coordinates(v,first,M) for v in full['cycles']],len(first['tops']))
        check(not any(v for row in dense_product(obstruction,embedding) for v in row),
              'every_full_lift_satisfies_quadratic_equations',a)
        coords=dense_product(red['right_inverse'],embedding)
        check(not any(v for row in coords[:red['rank']] for v in row),
              'full_lifts_in_integral_obstruction_kernel',a)
        kernel_change=coords[red['rank']:]
        kr=integer_diagonalize(kernel_change,a+'_kernel_image_completeness')
        check(len(kernel_change)==len(full['tops'])==kr['rank'] and all(v==1 for v in kr['diagonal']),
              'full_lifts_equal_entire_integral_obstruction_kernel',a)
        transitions={}
        for hi,lo in ((3,2),(4,3)):
            matrix=dense_columns([cycle_coordinates(v,case[lo],M) for v in case[hi]['cycles']],
                                 len(case[lo]['tops']))
            rr=integer_diagonalize(matrix,f'{a}_I{hi}_to_I{lo}')
            check(rr['rank']==len(matrix)==len(matrix[0]) and all(v==1 for v in rr['diagonal']),
                  'higher_conductor_orders_unique_unimodular_lift',(a,hi,lo))
            transitions[f'{hi}_to_{lo}']=matrix
        primary=primary_fibre(full['kernel']['d'],M,a)
        result[a]={
          'first_symbol_rank':len(first['tops']),'full_lift_rank':len(full['tops']),
          'quadratic_obstruction_rank':red['rank'],
          'full_top_coefficient_order':1,'possible_correction_order_two_top_states':0,
          'first_symbol_basis':[serialize_chain(v,M) for v in first['cycles']],
          'full_lift_basis':[{'coordinate':j,'minimal_regulator_grade':M.weight[j],
                              'cycle':serialize_chain(v,M)} for j,v in zip(full['tops'],full['cycles'])],
          'quadratic_target_basis':[{'state':j,'label':list(M.states[j]),
                'coefficient':list(allcoeff[j][:9]) + [3-M.weight[j]]} for j in rows],
          'quadratic_obstruction_matrix':obstruction,
          'quadratic_unimodular_reduction':red,
          'independent_obstruction_rows':red['right_inverse'][:red['rank']],
          'first_symbol_embedding':embedding,
          'image_to_obstruction_kernel_basis_change':kernel_change,
          'higher_jet_transitions':transitions,
          'truncation_ranks':{str(k):len(case[k]['tops']) for k in case},
          'full_normal_form':serialize_normal_form(full['nf'],M.weight),
          'first_jet_normal_form':serialize_normal_form(first['nf'],M.weight),
          'primary_fibre_reduction_verified':True}
    sums={k:sum(v[k] for v in result.values())
          for k in ('first_symbol_rank','full_lift_rank','quadratic_obstruction_rank')}
    check(sums=={'first_symbol_rank':134,'full_lift_rank':60,'quadratic_obstruction_rank':74},
          'complete_six_direction_lifting_counts')
    labels1,S1=reflection_matrix(M,cases,1)
    labels4,S4=reflection_matrix(M,cases,4)
    fixed1=fixed_lattice(S1,'first_jet_reflection')
    fixed4=fixed_lattice(S4,'full_lift_reflection')
    check((fixed1['fixed_rank'],fixed4['fixed_rank'])==(59,25),'integral_reflection_fixed_ranks')
    visible=[i for i,(a,j) in enumerate(labels4) if M.weight[j]==3]
    hidden=[i for i in range(60) if i not in visible]
    check(not any(S4[i][j] for i in visible for j in hidden) and
          not any(S4[i][j] for i in hidden for j in visible),
          'reflection_respects_visible_and_primary_comparison_direct_summands')
    Sv=[[S4[i][j] for j in visible] for i in visible]
    Sh=[[S4[i][j] for j in hidden] for i in hidden]
    fv=fixed_lattice(Sv,'visible_reflection');fh=fixed_lattice(Sh,'primary_comparison_reflection')
    check((len(visible),len(hidden),fv['fixed_rank'],fh['fixed_rank'])==(36,24,16,9),
          'equivariant_forgetting_ranks')
    # Assemble the leading-symbol injection and the actual obstruction.
    E=[[0]*60 for _ in range(134)];O=[[0]*134 for _ in range(74)]
    off1=off4=offo=0
    for a in SHORT_ORDER:
        ee=result[a]['first_symbol_embedding'];oo=result[a]['independent_obstruction_rows']
        for i,row in enumerate(ee):
            for j,z in enumerate(row):E[off1+i][off4+j]=z
        for i,row in enumerate(oo):
            for j,z in enumerate(row):O[offo+i][off1+j]=z
        off1+=len(ee);off4+=len(ee[0]);offo+=len(oo)
    check(dense_product(S1,E)==dense_product(E,S4),'first_symbol_embedding_reflection_naturality')
    Oinv=dense_product(O,fixed1['kernel'])
    oi=integer_diagonalize(Oinv,'quadratic_obstruction_on_invariant_symbols')
    check(oi['rank']==34,'independent_invariant_quadratic_constraints')
    # Genuine D3 transport acts on the three occurrence-labelled complexes.
    models={c:Complex(c) for c in ('35','15','13')}
    for c,model in models.items():
        for r,s in ((1,0),(0,1)):
            cc=polygon_diagonal(c,r,s);target=models[cc]
            for j in range(430):
                image=polygon_action(model,unit(j),r,s)
                check(apply(target.d,image)==polygon_action(model,model.d[j],r,s),
                      'full_polynomial_D3_transport_chain_equation',(c,r,s,j))
                check(bool(restrict(image,target.V))==(j in model.V),
                      'transport_retains_full_endpoint_support',(c,j))
                check(bool(restrict(image,target.Q))==(j in model.Q),
                      'transport_retains_full_Q_support',(c,j))
        for j in range(430):
            v=unit(j)
            rr=polygon_action(model,polygon_action(model,polygon_action(model,v,1),1),1)
            ss=polygon_action(model,polygon_action(model,v,0,1),0,1)
            srs=polygon_action(model,polygon_action(model,polygon_action(model,v,0,1),1),0,1)
            check(rr==v and ss==v and srs==polygon_action(model,v,2),
                  'full_D3_group_relations',(c,j))
    invariant_orbit_basis=[]
    for k in range(fixed4['fixed_rank']):
        vv=combine_global(M,cases,4,[row[k] for row in fixed4['kernel']])
        check(polygon_action(M,vv,0,1)==vv,'fixed_cycle_reflection_exact',k)
        orbit={c:polygon_action(M,vv,r) for r,c in enumerate(('35','15','13'))}
        for c,w in orbit.items():
            check(not apply(models[c].d,w),'transported_invariant_cycle_closed',(k,c))
            check(not restrict(w,models[c].V) and not restrict(w,models[c].Q),
                  'transported_invariant_cycle_complete_frame_zero',(k,c))
            for r,s in ((1,0),(0,1)):
                cc=polygon_diagonal(c,r,s)
                check(polygon_action(M,w,r,s)==orbit[cc],
                      'entire_marked_orbit_is_D3_invariant',(k,c,r,s))
        invariant_orbit_basis.append({c:serialize_chain(v,M) for c,v in orbit.items()})
    # A first-order symbol which does NOT lift, and a primitive which does.
    edge=('02','04');vertex=('02','03','04')
    bad=multiply(add(unit(M.index[vertex,vertex,0]),
                     multiply(unit(M.index[edge,edge,0]),monomial('beta')),-1),monomial('X02'))
    bad_d=apply(M.d,bad)
    check(len(bad)==2 and len(bad_d)==5 and all(conductor_order(p)==2 for j,p in bad_d),
          'two_term_nonliftable_symbol_quadratic_defect')
    detector=(M.index[edge,('02',),0],monomial('beta','beta','X02','X04'))
    check(bad_d.get(detector)==-1,'explicit_quadratic_nonlift_detector')
    goodedge=('13','35');goodvertex=('03','13','35')
    good=multiply(add(unit(M.index[goodvertex,goodvertex,0]),
                      multiply(unit(M.index[goodedge,goodedge,0]),monomial('beta')),-1),monomial('X02'))
    check(not apply(M.d,good),'two_term_liftable_symbol')
    invgood=add(good,polygon_action(M,good,0,1))
    check(len(invgood)==4 and not apply(M.d,invgood) and polygon_action(M,invgood,0,1)==invgood,
          'primitive_four_term_invariant_lift')
    check(not restrict(invgood,M.V) and not restrict(invgood,M.Q),
          'four_term_invariant_full_frame_zero')
    check(any(abs(z)==1 and p[9]==0 for (j,p),z in invgood.items()),
          'four_term_invariant_visible_mod_beta')
    # The actual source symbol: y0=X03, y1=X14, y2=X25 in zero-based labels.
    sigma_coeff={'02':(-1,'14'),'04':(-1,'25'),'13':(1,'25'),
                 '15':(1,'03'),'24':(-1,'03'),'35':(1,'14')}
    for r,s in ((1,0),(0,1)):
        for d,(sg,l) in sigma_coeff.items():
            check(sigma_coeff[polygon_diagonal(d,r,s)]==(sg,polygon_diagonal(l,r,s)),
                  'source_alternating_symbol_D3_covariance',(r,s,d))
    weighted_bad=multiply(bad,monomial('X14'),-1)
    check(apply(M.d,weighted_bad)==multiply(bad_d,monomial('X14'),-1)
          and bool(apply(M.d,weighted_bad)),
          'actual_source_long_coefficient_does_not_remove_obstruction')
    # Multiplication by each source long coefficient is injective on the
    # coefficient chains: the monomial ideal involves only short variables.
    for a in SHORT_ORDER:
        sg,long=sigma_coeff[a]
        for k,v in enumerate(cases[a][4]['cycles']):
            weighted=multiply(v,monomial('X'+long),sg)
            check(len(weighted)==len(v) and bool(weighted) and not apply(M.d,weighted),
                  'source_long_coefficients_preserve_all_lift_directions',(a,k))
    # Exact equivariant defect of the first-symbol obstruction sequence.
    # 0 -> lift lattice -> first-symbol lattice -> quadratic image -> 0.
    section=[[0]*74 for _ in range(134)]
    aoff=boff=0
    for direction in SHORT_ORDER:
        rd=result[direction]['quadratic_unimodular_reduction']
        n=result[direction]['first_symbol_rank'];rr=rd['rank']
        for i in range(n):
            for j in range(rr):section[aoff+i][boff+j]=rd['right'][i][j]
        aoff+=n;boff+=rr
    check(dense_product(O,section)==dense_identity(74),'quadratic_image_integral_section')
    SO=dense_product(dense_product(O,S1),section)
    check(dense_product(SO,SO)==dense_identity(74),'quadratic_image_reflection_square')
    check(dense_product(SO,O)==dense_product(O,S1),'quadratic_obstruction_equivariant')
    fo=fixed_lattice(SO,'quadratic_image_invariants')
    check(fo['fixed_rank']==34,'quadratic_image_invariant_rank')
    oc=dense_product(fo['right_inverse'],Oinv)
    check(not any(z for row in oc[:fo['rank']] for z in row),
          'invariant_symbols_have_invariant_quadratic_obstruction')
    invariant_obstruction=oc[fo['rank']:]
    io=integer_diagonalize(invariant_obstruction,'invariant_obstruction_in_saturated_target')
    check(Counter(io['diagonal'])=={1:33,2:1},'one_index_two_equivariant_defect')
    # An actual primitive invariant quadratic defect with no invariant preimage.
    def inverse_unimodular(matrix,label):
        rr=integer_diagonalize(matrix,label)
        check(rr['rank']==len(matrix) and all(v==1 for v in rr['diagonal']),
              'matrix_for_inverse_is_unimodular',label)
        inv=dense_product(rr['right'],rr['left'])
        check(dense_product(matrix,inv)==dense_identity(len(matrix)),
              'unimodular_inverse_literal_check',label)
        return inv
    ui=inverse_unimodular(io['left'],'invariant_target_row_basis')
    parity_index=io['diagonal'].index(2)
    target_coord=[[row[parity_index]] for row in ui]
    parity_defect=dense_product(fo['kernel'],target_coord)
    ordinary_preimage=dense_product(section,parity_defect)
    twice_preimage=dense_product(fixed1['kernel'],
                                [[row[parity_index]] for row in io['right']])
    check(dense_product(O,ordinary_preimage)==parity_defect,
          'primitive_parity_defect_has_ordinary_preimage')
    check(dense_product(SO,parity_defect)==parity_defect,
          'primitive_parity_defect_is_invariant')
    check(dense_product(O,twice_preimage)==[[2*row[0]] for row in parity_defect]
          and dense_product(S1,twice_preimage)==twice_preimage,
          'twice_parity_defect_has_integral_invariant_preimage')
    ed=integer_diagonalize(E,'full_lift_first_symbol_left_inverse')
    check(ed['rank']==60 and all(v==1 for v in ed['diagonal']),
          'full_lift_first_symbol_embedding_saturated')
    left_inverse=dense_product(ed['right'],ed['left'][:60])
    symmetry_difference=[[u[0]-v[0]] for u,v in zip(dense_product(S1,ordinary_preimage),ordinary_preimage)]
    parity_lift=dense_product(left_inverse,symmetry_difference)
    check(dense_product(E,parity_lift)==symmetry_difference,
          'parity_preimage_symmetry_defect_is_full_lift')
    check(dense_product(S4,parity_lift)==[[-row[0]] for row in parity_lift],
          'parity_lift_is_reflection_anticocycle')
    transformed=dense_product(fixed4['left'],parity_lift)
    parity_coordinates=[i for i,v in enumerate(fixed4['diagonal'])
                        if transformed[i][0]%v]
    check(bool(parity_coordinates), 'parity_lift_not_an_integral_reflection_coboundary')
    check(all(parity_lift[i][0]==0 for i in visible),
          'parity_lifting_defect_lies_entirely_in_primary_homotopy_directions')
    parity_chain=combine_global(M,cases,4,[row[0] for row in parity_lift])
    check(bool(parity_chain) and not apply(M.d,parity_chain),
          'parity_lifting_defect_full_polynomial_cycle')
    check(all(p[9]>=1 for j,p in parity_chain),
          'parity_lifting_defect_has_termwise_beta_factor')
    parity_primary_homotopy={}
    for (j,p),value in parity_chain.items():
        qq=list(p);qq[9]-=1
        put(parity_primary_homotopy,(j,tuple(qq)),value)
    check(not apply(M.d,parity_primary_homotopy)
          and multiply(parity_primary_homotopy,monomial('beta'))==parity_chain,
          'parity_defect_ordinary_supported_nullhomotopy')
    check(not restrict(parity_primary_homotopy,M.V) and not restrict(parity_primary_homotopy,M.Q),
          'parity_defect_homotopy_preserves_endpoint_Q_but_changes_primary_comparison')
    parity_audit={
      'quadratic_image_reflection':SO,'quadratic_image_fixed_lattice':fo,
      'invariant_obstruction_matrix':invariant_obstruction,
      'invariant_obstruction_normal_form':io,
      'invariant_quotient':'Z/2',
      'primitive_invariant_quadratic_defect':[row[0] for row in parity_defect],
      'ordinary_first_symbol_preimage':[row[0] for row in ordinary_preimage],
      'invariant_first_symbol_preimage_of_twice_defect':[row[0] for row in twice_preimage],
      'reflection_defect_full_lift_coordinates':[row[0] for row in parity_lift],
      'reflection_coboundary_obstructing_coordinates':parity_coordinates,
      'reflection_defect_full_chain':serialize_chain(parity_chain,M),
      'ordinary_supported_primary_changing_homotopy':serialize_chain(parity_primary_homotopy,M),
      'scope':'index-two defect in invariant preimages of quadratic obstruction; not a selected physical class or integer torsion in the lift lattice'}

    matrix_hash=sha256(json.dumps({'O':O,'E':E,'S1':S1,'S4':S4},sort_keys=True).encode()).hexdigest()
    certificate={
      'schema':'marici.branchA.conductor_symbol_lifting_and_symmetry.v1',
      'date':'2026-09-07','coefficient_scope':'first six short occurrence weights; conductor-valued; regulator grade 3; integral unit-normalized beta family',
      'physical_Delta_J_selected':False,
      'source_commit':COMMIT,
      'repo_inputs':[
          {'path':'research/voevodsky/check_absolute_unlocalized_support_pc.rs',
           'blob':'b967151cb0ee822e2361b9334a4ab26082c12682'},
          {'path':'src/ledger/20260814-93 Alternating Fusion Normalization-Conductor Square.md',
           'blob':'840258522d45e450e4f1e8bb927d9aae58c75566'}],
      'counts':sums,
      'source_states':[[j,list(F),list(H),e,M.degree[j],M.weight[j]] for j,(F,H,e) in enumerate(M.states)],
      'full_source_differential':serialize_full_matrix(M.d),
      'directions':result,
      'combined_first_symbol_embedding':E,'combined_independent_obstruction_matrix':O,
      'symmetry':{
          'group':'D3 of order 6: r(v)=v+2, s(v)=2-v mod6',
          'top_signs':{'rotation':1,'reflection':-1},
          'supported_source_p_e_action':'trivial; beta fixed',
          'occurrence_mark_orbit':['35','15','13'],
          'first_symbol_coordinate_labels':labels1,'first_symbol_reflection':S1,
          'full_lift_coordinate_labels':labels4,'full_lift_reflection':S4,
          'first_symbol_fixed_lattice':fixed1,'full_lift_fixed_lattice':fixed4,
          'invariant_obstruction_reduction':oi,
          'visible_coordinate_indices':visible,'primary_homotopy_coordinate_indices':hidden,
          'visible_fixed_lattice':fv,'primary_homotopy_fixed_lattice':fh,
          'full_equivariant_orbit_cycle_basis':invariant_orbit_basis},
      'equivariant_quadratic_defect':parity_audit,
      'source_alternating_symbol_coefficients':sigma_coeff,
      'source_symbol_status':'prescribed conormal signs, long coefficients and polarity do not specify a target chain-valued first symbol',
      'examples':{
          'nonliftable_first_symbol':serialize_chain(bad,M),
          'quadratic_defect':serialize_chain(bad_d,M),
          'nonlift_detector':{'row':detector[0],'monomial':list(detector[1]),'value':-1},
          'liftable_first_symbol':serialize_chain(good,M),
          'reflection_invariant_lift':serialize_chain(invgood,M)},
      'comparison_matrix_sha256':matrix_hash,
      'proof_sources':['https://stacks.math.columbia.edu/tag/0A8H','https://stacks.math.columbia.edu/tag/0117'],
      'exact_checks':sum(COUNTS.values()),'verification_counts':dict(sorted(COUNTS.items()))}
    text=json.dumps(certificate,indent=2,sort_keys=True)+'\n'
    output.parent.mkdir(parents=True,exist_ok=True);output.write_text(text,encoding='utf-8')
    print(json.dumps({'certificate':str(output),'sha256':sha256(text.encode()).hexdigest(),
          'matrix_sha256':matrix_hash,'checks':certificate['exact_checks'],'counts':sums,
          'fixed_ranks':[fixed1['fixed_rank'],fixed4['fixed_rank']],
          'invariant_obstruction_rank':oi['rank'],
          'invariant_obstruction_diagonal':dict(Counter(oi['diagonal'])),
          'equivariant_visible_primary_homotopy_ranks':[fv['fixed_rank'],fh['fixed_rank']],
          'invariant_quadratic_defect_cokernel':'Z/2'},indent=2))
    return certificate


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name(
        'branch_a_conductor_symbol_lifting_and_symmetry_certificate.json'))
    main_symbol_lifting(parser.parse_args().output)
