#!/usr/bin/env python3
"""First conductor-weight coherent primary lifts with the full endpoint/Q frame.

Standalone Python 3 standard-library exact checker. Reconstructs all 430
states, keeps coefficients in the conductor ideal, and computes every
occurrence-epsilon_d component for the six short coordinates. The refined
frame retains the whole endpoint packet and its incoming differential,
not only fully native endpoint-top quotients. Both the boundary homotopy
fibre and the primary homotopy fibre are explicitly contracted to their
strict-kernel models.

The finite matrices have entries in Z[beta] with no regulator truncation.
Every polynomial basis change and its inverse is verified. This tests a
specified coefficient frame, not a construction of physical Delta_J.
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
    def __init__(self) -> None:
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
                put(self.d[j],(self.index[F,H,0],monomial('X35')),
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
            p[DIAGONALS.index('35')]-=e
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
        p[DIAGONALS.index('35')]-=e
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


def main(output: Path) -> dict:
    M=Complex()
    results={};totals=Counter()
    sample_case=None
    # Independent zero-weight control in the same stronger endpoint/Q frame.
    c0,d0=occurrence_component(M,None,False)
    k0=full_endpoint_q_kernel(M,c0,d0,'zero_weight_control')
    n0=polynomial_normal_form(k0['ids'],k0['d'],M.weight,M.degree,'zero_weight_control')
    check(not any(M.degree[j]>=3 for j in n0['free']), 'zero_weight_control_no_top_free_class')
    check(not any(n>=3 for n,p,c in n0['torsion_blocks']), 'zero_weight_control_no_top_torsion')
    for a in ('02','04','24','13','15','35'):
        coeff,d=occurrence_component(M,a,True)
        kernel=full_endpoint_q_kernel(M,coeff,d,a)
        nf=polynomial_normal_form(kernel['ids'],kernel['d'],M.weight,M.degree,'full_endpoint_'+a)
        hd,hw,hdegree=supported_hom(kernel['d'],M)
        hnf=polynomial_normal_form(set(hd),hd,hw,hdegree,'full_endpoint_Hom_'+a)
        pf=primary_fibre(kernel['d'],M,a)
        tops=[j for j in nf['free'] if M.degree[j]==3]
        check(max(M.degree[j] for j in kernel['ids'])<=3,'relative_first_weight_no_degree_four',a)
        check(all(M.weight[j]<=3 for j in tops),'all_top_classes_have_recorded_grade_lifts',a)
        grade_rows=sorted(lo for hi,lo,sg,p in hnf['blocks'] if p and hdegree[lo]==0 and hw[lo]==2)
        check(all(p==1 for hi,lo,sg,p in hnf['blocks'] if p and hdegree[lo]==0),
              'ordinary_supported_degree_zero_only_beta_torsion',a)
        cols=[];cycle_data=[]
        for j in tops:
            raw=encode_cycle(M,coeff,kernel,nf,j)
            fixed=encode_cycle(M,coeff,kernel,nf,j,3)
            v={(2*i+1,3-M.weight[i]):q for i,q in nf['inclusion'][j].items()}
            check(not weighted_vector_apply(hd,v,hw),'all_top_cycles_give_supported_maps',(a,j))
            hc=weighted_vector_apply(hnf['projection'],v,hw)
            cols.append({i:q for (i,k),q in hc.items() if i in grade_rows and k==0})
            if M.weight[j]<3:
                u={(2*i,2-M.weight[i]):q for i,q in nf['inclusion'][j].items()}
                check(all(k>=0 for i,k in u),'invisible_class_homotopy_is_polynomial',(a,j))
                check(weighted_vector_apply(hd,u,hw)==v,
                      'invisible_class_explicit_ordinary_nullhomotopy',(a,j))
            cycle_data.append({'coordinate':j,'minimal_regulator_grade':M.weight[j],
                               'minimal_cycle':serialize_chain(raw,M),'grade_three_cycle':serialize_chain(fixed,M),
                               'ordinary_supported_coordinates':sorted(cols[-1].items())})
        forget=[[col.get(i,0) for col in cols] for i in grade_rows]
        fr,flog=saturated_integer_rank(forget,a+'_forget_primary_comparison')
        check(fr==6,'six_detectable_primary_preserving_directions',a)
        # Primary readout on the entire grade-preserving ordinary map group.
        primary_rows=sorted(lo for hi,lo,sg,p in nf['blocks']
                            if p==1 and M.degree[lo]==2 and M.weight[lo]==2)
        primary_cols=[]
        for j in grade_rows:
            pre={(i,hw[j]-hw[i]):q for i,q in hnf['inclusion'][j].items() if i%2==0}
            bottom={(i//2,k):q for (i,k),q in pre.items()}
            check(not weighted_vector_apply(kernel['d'],bottom,M.weight),
                  'ordinary_map_primary_is_cycle',(a,j))
            bc=weighted_vector_apply(nf['projection'],bottom,M.weight)
            primary_cols.append({i:q for (i,k),q in bc.items() if i in primary_rows and k==0})
        primary=[[col.get(i,0) for col in primary_cols] for i in primary_rows]
        pr,plog=saturated_integer_rank(primary,a+'_primary_readout')
        check(pr==6 and len(grade_rows)==12,'grade_preserving_supported_maps_and_primary_ranks',a)
        product=[[sum(primary[i][j]*forget[j][k] for j in range(len(grade_rows)))
                  for k in range(len(tops))] for i in range(len(primary_rows))]
        check(all(not v for row in product for v in row),'primary_readout_kills_difference_image',a)
        check(fr+pr==len(grade_rows),'ordinary_primary_sequence_exact_by_saturated_ranks',a)
        weights=Counter(M.weight[j] for j in tops)
        summary={'coefficient_component_states':len(coeff),'kernel_states':len(kernel['ids']),
                 'kernel_chain_ranks':dict(sorted(Counter(M.degree[j] for j in kernel['ids']).items())),
                 'kernel_free_homology':nf['free_ranks'],'kernel_torsion':nf['torsion_blocks'],
                 'top_minimal_regulator_grades':dict(sorted(weights.items())),
                 'primary_fixed_components_rank_at_grade_three':len(tops),
                 'ordinary_supported_map_rank_at_recorded_grade':len(grade_rows),
                 'forget_primary_comparison_image_rank':fr,
                 'forget_primary_comparison_kernel_rank':len(tops)-fr,
                 'ordinary_primary_image_rank':pr,'higher_primary_fixed_homotopy_groups':'zero'}
        totals['primary_fixed']+=len(tops)
        totals['ordinary_supported']+=len(grade_rows)
        totals['visible']+=fr
        totals['comparison_only']+=len(tops)-fr
        totals['primary_image']+=pr
        bf=kernel['boundary_fibre']
        results[a]={'summary':summary,
                    'coefficient_basis':[[j,list(p)] for j,p in sorted(coeff.items())],
                    'component_differential':serialize_weighted_matrix(d,M.weight),
                    'kernel_basis':serialize_weighted_matrix(kernel['inclusion'],M.weight),
                    'frame_state_coordinates':sorted(kernel['frame_ids']),
                    'frame_differential':serialize_weighted_matrix(kernel['frame_differential'],M.weight),
                    'full_basis_inclusion':serialize_weighted_matrix(kernel['full_basis_inclusion'],M.weight),
                    'full_basis_inverse':serialize_weighted_matrix(kernel['full_basis_inverse'],M.weight),
                    'boundary_fibre':{k:serialize_weighted_matrix(bf[k],bf['weight']) for k in ('d','p','i','h')},
                    'boundary_fibre_basis_weights':sorted(bf['weight'].items()),
                    'kernel_normal_form':serialize_normal_form(nf,M.weight),
                    'ordinary_Hom_normal_form':serialize_normal_form(hnf,hw),
                    'ordinary_Hom_basis':[[j,hdegree[j],hw[j]] for j in sorted(hd)],
                    'primary_fibre':serialize_primary(pf),
                    'primary_fixed_cycle_basis':cycle_data,
                    'forget_primary_matrix':forget,'forget_primary_unit_elimination':flog,
                    'primary_readout_matrix':primary,'primary_readout_unit_elimination':plog}
        if a=='02':sample_case=(coeff,kernel,nf,hd,hw,hnf,pf)
    check(dict(totals)=={'primary_fixed':60,'ordinary_supported':72,'visible':36,
                        'comparison_only':24,'primary_image':36},'six_direction_complete_totals')

    # Two direct marked-gallery examples in the 02 component.
    x=monomial('X02');be=monomial('beta')
    face=('03','13','35');edge=('13','35')
    Y=multiply({(M.index[face,face,0],ZERO):1,(M.index[edge,edge,0],be):-1},x)
    O=multiply({(M.index[face,('03','13'),1],ZERO):1,
                (M.index[edge,('13',),1],be):-1},x)
    BO=multiply(O,be)
    for name,v in [('Y02',Y),('O02',O),('beta_O02',BO)]:
        check(not apply(M.d,v),'two_term_gallery_witness_closed',name)
        check(not restrict(v,M.V) and not restrict(v,M.Q),
              'two_term_gallery_witness_full_endpoint_Q_zero',name)
        check(len(v)==2,'two_term_gallery_witness_length',name)
    # Replay the supplied nonzero primary/first primitive, without assigning
    # either deformation from a desired readout. The only division below
    # extracts a factor already present in every coefficient of dH.
    recorded_H={(M.index[F,H,e],monomial(*(['beta']*k))):v
                for F,H,e,k,v in H_INPUT}
    recorded_dH=apply(M.d,recorded_H)
    recorded_A={}
    for (j,p),v in recorded_dH.items():
        check(p[9]>0,'recorded_dH_has_termwise_beta_factor',j)
        q=list(p);q[9]-=1;put(recorded_A,(j,tuple(q)),v)
    check(recorded_A and not apply(M.d,recorded_A),'recorded_nonzero_primary_closed')
    check(apply(M.d,recorded_H)==multiply(recorded_A,be),'recorded_primitive_full_equation')
    base_A=multiply(recorded_A,x);base_H=multiply(recorded_H,x)
    for name,top in [('reference',base_H),('native_deformation',add(base_H,Y)),
                     ('primary_comparison_deformation',add(base_H,BO))]:
        check(apply(M.d,top)==multiply(base_A,be),'three_maps_same_nonzero_primary',name)
        check(restrict(top,M.V)==restrict(base_H,M.V) and
              restrict(top,M.Q)==restrict(base_H,M.Q),
              'three_maps_identical_full_endpoint_and_Q',name)
        check(all(p[9]+M.weight[j]==3 for j,p in top),
              'three_maps_same_recorded_regulator_grade',name)
    coeff,kernel,nf,hd,hw,hnf,pf=sample_case
    def coordinates(v:dict)->dict:
        raw={}
        for (j,p),z in v.items():
            check(p[:9]==coeff[j][:9],'sample_has_exact_occurrence_weight',j)
            put(raw,(j,p[9]),z)
        inv=kernel['full_basis_inverse']
        out=weighted_vector_apply(inv,raw,M.weight)
        check(all(j in kernel['ids'] for j,k in out),'sample_lies_in_full_frame_kernel')
        return out
    ycoords=coordinates(Y);ocoords=coordinates(O);bocoords=coordinates(BO)
    ynf=weighted_vector_apply(nf['projection'],ycoords,M.weight)
    onf=weighted_vector_apply(nf['projection'],ocoords,M.weight)
    bonf=weighted_vector_apply(nf['projection'],bocoords,M.weight)
    check(any(j in nf['free'] for j,k in ynf),'Y02_nonzero_full_frame_homology')
    check(any(j in nf['free'] for j,k in onf),'O02_nonzero_full_frame_homology')
    check(any(j in nf['free'] for j,k in bonf),'beta_O02_nonzero_primary_fixed_homology')
    ordinary_bo={(2*j+1,k):z for (j,k),z in bocoords.items()}
    ordinary_h={(2*j,k):z for (j,k),z in ocoords.items()}
    check(weighted_vector_apply(hd,ordinary_h,hw)==ordinary_bo,
          'beta_O02_ordinary_primitive_changes_primary_homotopy')
    # Pairs (0,beta O,0) and (0,beta O,O) have different primary comparisons.
    t0={(3*j+1,k):z for (j,k),z in bocoords.items()}
    t1=dict(t0)
    for (j,k),z in ocoords.items():put(t1,(3*j+2,k),z)
    check(not weighted_vector_apply(pf['d'],t0,pf['weight']) and
          not weighted_vector_apply(pf['d'],t1,pf['weight']),
          'both_primary_comparison_choices_are_closed')
    p0=weighted_vector_apply(pf['p'],t0,pf['weight'])
    p1=weighted_vector_apply(pf['p'],t1,pf['weight'])
    check(p0=={(5000+j,k):z for (j,k),z in bocoords.items()} and not p1,
          'primary_comparison_choice_detected_exactly')
    primitive=weighted_vector_apply(pf['h'],t1,pf['weight'])
    check(weighted_vector_apply(pf['d'],primitive,pf['weight'])==t1,
          'corrected_primary_choice_has_explicit_nullhomotopy')

    certificate={
      'schema':'marici.branchA.first_conductor_coherent_primary_lifts.v1',
      'repository_commit':COMMIT,
      'status':'exact_coefficient_calculation_with_full_endpoint_and_Q_frame',
      'physical_Delta_J_constructed':False,
      'ring':'R=Z[beta,X_d]/(X_even X_odd); Lambda=Z[beta]',
      'domain':'conductor-ideal-valued occurrence-epsilon_d components; higher lower-correction coefficients retained',
      'frame_definition':'N={v in I*C_beta: pi_Q(v)=0, pr_V(v)=0, pr_V(dv)=0}; actual frame C_I/N',
      'primary_source':'S_beta=(Re --beta--> Rp), degrees(e,p)=(3,2), normal weights(e,p)=(3,2)',
      'primary_fixed_fibre_projection':'(a,b,h) -> b-(-1)^n beta*h in homological degree n',
      'primary_fixed_homotopy':'(a,b,h) -> (h,0,0)',
      'not_first_conductor_quotient':'I/I^2 is not taken; all necessary higher-conductor-order coefficients are retained',
      'zero_weight_control':{'free':n0['free_ranks'],'torsion':n0['torsion_blocks'],'primary_fixed_H0':'zero'},
      'total_grade_preserving_ranks':dict(totals),
      'source_states':[[j,list(F),list(H),e,M.degree[j],M.weight[j]] for j,(F,H,e) in enumerate(M.states)],
      'source_differential':serialize_full_matrix(M.d),
      'directions':results,
      'direct_examples':{'Y02':serialize_chain(Y,M),'O02':serialize_chain(O,M),
                         'beta_O02':serialize_chain(BO,M),
                         'reference_nonzero_primary':serialize_chain(base_A,M),
                         'reference_primitive':serialize_chain(base_H,M),
                         'ordinary_beta_O02_nullhomotopy':'p -> O02, e -> 0',
                         'primary_fixed_beta_O02_coordinate':'beta*O02 !=0',
                         'comparison_corrected_beta_O02_coordinate':'beta*O02-beta*O02=0'},
      'proof_sources':['https://stacks.math.columbia.edu/tag/0A8H','https://stacks.math.columbia.edu/tag/014D',
                       'https://stacks.math.columbia.edu/tag/064B','https://stacks.math.columbia.edu/tag/0117'],
      'verification_counts':dict(sorted(COUNTS.items())), 'exact_checks':sum(COUNTS.values())}
    output.parent.mkdir(parents=True,exist_ok=True)
    text=json.dumps(certificate,indent=2,sort_keys=True)+'\n'
    output.write_text(text,encoding='utf-8')
    print(json.dumps({'certificate':str(output),'sha256':sha256(text.encode()).hexdigest(),
                       'exact_checks':certificate['exact_checks'],
                       'ranks':dict(totals),
                       'directions':{a:r['summary'] for a,r in results.items()}},indent=2,sort_keys=True))
    return certificate


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name(
        'branch_a_first_conductor_coherent_primary_lifts_certificate.json'))
    main(parser.parse_args().output)
