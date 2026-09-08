#!/usr/bin/env python3
"""Exact coherent endpoint/Q-frame calculation on the normalized beta family.

Standalone Python 3 standard-library checker. Reconstructs the full 430-state
complex, its 18-state chain-map boundary, the 448-state homotopy fibre and its
412-state strict-kernel retract. Computes integral polynomial normal forms of
entire occurrence-weight-zero complexes over Z[beta], not beta truncations.

The boundary retains the full Q quotient and TWO endpoint-top quotient
complexes, not a non-chain projection onto the entire endpoint packet. No
claim identifies this chosen frame with the unconstructed physical Delta_J.
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


def main(output: Path) -> dict:
    M=Complex()
    fibre=verify_fibre(M)
    coeff,d= M.occurrence_zero()
    all_ids=set(coeff)
    short_ids=all_ids&M.B
    kernel_ids=all_ids&M.kernel_ids
    frame_ids=all_ids&M.boundary_ids
    check((len(all_ids),len(short_ids),len(kernel_ids),len(frame_ids))==(231,224,222,9),
          'occurrence_zero_support_sizes')
    Cnf=polynomial_normal_form(all_ids,d,M.weight,M.degree,'C')
    Bnf=polynomial_normal_form(short_ids,d,M.weight,M.degree,'B')
    Knf=polynomial_normal_form(kernel_ids,d,M.weight,M.degree,'framed_kernel')
    check(Cnf['free_ranks']=={2:3,3:2} and Cnf['torsion_blocks']==[[1,1,6],[2,1,12]],
          'full_complex_homology_normal_form')
    check(Bnf['free_ranks']=={2:3,3:1} and Bnf['torsion_blocks']==[[1,1,8],[2,1,12],[2,2,1]],
          'short_boundary_homology_normal_form')
    check(Knf['free_ranks']=={2:4} and Knf['torsion_blocks']==[[1,1,8],[2,1,12]],
          'coherently_framed_homology_normal_form')

    # Actual attaching cycle and its recorded beta^2 primitive.
    beta=monomial('beta');beta2=monomial('beta','beta')
    top=M.index[(),(),0]
    phi={(top,beta):1}
    for l in LONG:phi[(M.index[(l,),(l,),0],ZERO)]=-1
    Psi={(M.index[F,F,0],monomial(*(['beta']*(3-len(F))))):(-1)**(len(F)*(len(F)+1)//2)
         for F in M.faces}
    Z={}
    for (j,p),c in Psi.items():
        F,H,e=M.states[j]
        if '35' not in H:put(Z,(j,p),c)
        else:
            HH=tuple(a for a in H if a!='35')
            pp=tuple(a+b for a,b in zip(p,beta))
            put(Z,(M.index[F,HH,1],pp),c)
    Zplus=add(Psi,Z,-1)
    chi=apply(M.d,phi)
    W=add(multiply(phi,beta2),Z,-1)
    check(not apply(M.d,Z) and not apply(M.d,Zplus),'structural_top_cycles_closed')
    check(apply(M.d,W)==multiply(chi,beta2),'recorded_beta_squared_primitive')
    check(not restrict(chi,M.boundary_ids),'chi_has_zero_joint_frame')
    check(restrict(Z,M.Q)==multiply(phi,beta2),'top_to_Q_beta_squared')
    check(not restrict(Zplus,M.Q),'positive_top_to_Q_zero')
    neg=M.index[tuple(sorted(MINUS)),tuple(sorted(MINUS)),0]
    pos=M.index[tuple(sorted(PLUS)),tuple(sorted(PLUS)),0]
    check(restrict(Z,M.end_top)==unit(neg) and restrict(Zplus,M.end_top)==unit(pos),
          'top_cycle_native_endpoint_matrix_identity')
    check(restrict(W,M.boundary_ids)=={(neg,ZERO):-1},'ordinary_primitive_changes_endpoint_top')

    def to_slice(v: dict) -> dict:
        out={}
        for (j,p),c in v.items():
            pp=list(p);pp[9]=0
            check(j in coeff and tuple(pp)==coeff[j],'witness_in_full_weight_zero_slice')
            put(out,(j,p[9]),c)
        return out
    chi_slice=to_slice(chi)
    chi_nf=weighted_vector_apply(Knf['projection'],chi_slice,M.weight)
    free_component={key:c for key,c in chi_nf.items() if key[0] in Knf['free']}
    detector_id=next(j for (j,p),c in sorted(free_component.items()) if p==0 and abs(c)==1)
    detector_sign=free_component[(detector_id,0)]
    detector={j:{0:detector_sign*Knf['projection'][j][detector_id]}
              for j in kernel_ids if Knf['projection'][j].get(detector_id)}
    # The displayed detector is a polynomial cochain and evaluates chi to one.
    for j in kernel_ids:
        val=0
        for i,c in d[j].items():
            if i in kernel_ids:val+=c*detector.get(i,{}).get(0,0)
        check(val==0,'free_chi_detector_annihilates_all_boundaries')
    value={}
    for (j,p),c in chi_slice.items():
        a=detector.get(j,{}).get(0,0)
        if a:put(value,p+M.weight[j]-M.weight[detector_id],a*c)
    check(value=={0:1},'free_chi_detector_value_one')
    chi_in_B=weighted_vector_apply(Bnf['projection'],chi_slice,M.weight)
    beta2_blocks={lo:(hi,sg) for hi,lo,sg,p in Bnf['blocks'] if p==2 and M.degree[lo]==2}
    detected_B={key:c for key,c in chi_in_B.items() if key[0] in beta2_blocks}
    check(len(detected_B)==1 and next(iter(detected_B.values())) in (1,-1)
          and next(iter(detected_B))[1]==0,'chi_ordinary_beta_squared_coordinate_is_primitive')
    check(not any(j in Bnf['free'] for j,p in chi_in_B),'chi_has_no_ordinary_free_component')

    # Hom(S_beta,K): p is degree 2, e degree 3. We use homological index -q
    # for the internal Hom, so its differential lowers degree by one.
    hom_ids={2*j+bit for j in kernel_ids for bit in (0,1)}
    hom_weight={2*j+bit:M.weight[j]-bit for j in kernel_ids for bit in (0,1)}
    hom_degree={2*j+bit:M.degree[j]-(2+bit) for j in kernel_ids for bit in (0,1)}
    hom_d={j:{} for j in hom_ids}
    for j in kernel_ids:
        for bit in (0,1):
            src=2*j+bit
            for i,c in d[j].items():
                if i in kernel_ids:put(hom_d[src],2*i+bit,c)
            if bit==0:
                put(hom_d[src],2*j+1,-((-1)**(2-M.degree[j])))
    Hnf=polynomial_normal_form(hom_ids,hom_d,hom_weight,hom_degree,'supported_framed_Hom')
    check(not Hnf['free_ranks'] and Hnf['torsion_blocks']==[[-2,1,8],[-1,1,24],[0,1,12]],
          'supported_framed_Hom_complete_cohomology')

    # Twelve maps, from actual nonendpoint vertices, form the entire H^0.
    gammas=[]
    torsion_zero={lo for hi,lo,sg,p in Hnf['blocks'] if p==1 and hom_degree[lo]==0}
    gamma_coordinates={}
    primary_coordinates={}
    primary_rows={lo for hi,lo,sg,p in Knf['blocks'] if p==1 and M.degree[lo]==2}
    for F in M.faces:
        if len(F)!=3 or frozenset(F) in (MINUS,PLUS):continue
        j=M.index[F,F,0]
        E=unit(j)
        dE=apply(M.d,E)
        BF={}
        for (i,p),c in dE.items():
            check(p[9]>=1,'vertex_lower_boundary_has_beta_factor')
            pp=list(p);pp[9]-=1;put(BF,(i,tuple(pp)),c)
        check(not apply(M.d,BF),'vertex_primary_closed')
        check(apply(M.d,E)==multiply(BF,beta),'vertex_supported_map_chain')
        check(not restrict(E,M.boundary_ids) and not restrict(BF,M.boundary_ids),
              'vertex_supported_map_joint_frame_zero')
        # beta times Gamma is boundary of the homotopy p |-> E.
        check(apply(M.d,E)==multiply(BF,beta),'vertex_beta_annihilating_homotopy_lower')
        v={}
        for (i,p),c in to_slice(BF).items():put(v,(2*i,p),c)
        put(v,(2*j+1,0),1)
        check(not weighted_vector_apply(hom_d,v,hom_weight),'vertex_full_Hom_cocycle')
        coords=weighted_vector_apply(Hnf['projection'],v,hom_weight)
        gamma_coordinates[j]={i:c for (i,p),c in coords.items() if i in torsion_zero and p==0}
        primary_nf=weighted_vector_apply(Knf['projection'],to_slice(BF),M.weight)
        primary_coordinates[j]={i:c for (i,p),c in primary_nf.items() if i in primary_rows and p==0}
        check(not any(i in Knf['free'] for i,p in primary_nf),'vertex_primary_has_no_free_homology_component')
        gammas.append({'face':list(F),'top_index':j,'lower':serialize_chain(BF,M),
                       'upper':serialize_chain(E,M)})
    check(len(gammas)==12,'twelve_nonendpoint_vertex_classes')
    # Show saturated spanning, not just twelve nonzero elements: integer determinant.
    rows=sorted(torsion_zero);cols=sorted(gamma_coordinates)
    matrix=[[gamma_coordinates[j].get(i,0) for j in cols] for i in rows]
    def det(a: list[list[int]]) -> int:
        a=[r[:] for r in a];n=len(a);prev=1;sign=1
        if not n:return 1
        for k in range(n-1):
            r=next((r for r in range(k,n) if a[r][k]),None)
            if r is None:return 0
            if r!=k:a[r],a[k]=a[k],a[r];sign=-sign
            p=a[k][k]
            for i in range(k+1,n):
                for j in range(k+1,n):
                    num=a[i][j]*p-a[i][k]*a[k][j]
                    check(num%prev==0,'fraction_free_determinant_division')
                    a[i][j]=num//prev
                a[i][k]=0
            prev=p
        return sign*a[-1][-1]
    determinant=det(matrix)
    check(abs(determinant)==1,'vertex_basis_unimodular_Hom_coordinates')
    primary_matrix=[[primary_coordinates[j].get(i,0) for j in cols] for i in sorted(primary_rows)]
    primary_determinant=det(primary_matrix)
    check(abs(primary_determinant)==1,'primary_map_isomorphism_onto_beta_torsion')
    # Source-cofibre argument is supported by the full kernel normal form:
    check(all(M.degree[j]<3 for j in Knf['free']), 'primary_fixed_H3_free_zero')
    check(all(n<3 for n,k,c in Knf['torsion_blocks']), 'primary_fixed_H3_torsion_zero')
    check(max(M.degree[j] for j in kernel_ids)==3,'primary_fixed_no_higher_chain_degrees')

    certificate={
        'schema':'marici.branchA.coherent_endpoint_q_primary_frame.v1',
        'repository_commit':COMMIT,
        'coefficient_ring':'R=Z[beta,X_d]/(X_even X_odd); Lambda=Z[beta]',
        'scope':'Full polynomial chain identities; homology and contractibility in complete occurrence-weight-zero component only.',
        'physical_Delta_J_identification':False,
        'frame':'full fourteen-state Q quotient plus two two-state fully native endpoint-top quotients',
        'full_counts':{'C':430,'endpoints':32,'Q':14,'endpoint_top_boundary':4,'joint_boundary':18,'homotopy_fibre':448,'strict_kernel':412},
        'weight_zero_counts':{'C':231,'B':224,'joint_boundary':9,'kernel':222,'supported_Hom':444},
        'weight_zero_homology':{
            'C':{'free':Cnf['free_ranks'],'torsion':Cnf['torsion_blocks']},
            'B':{'free':Bnf['free_ranks'],'torsion':Bnf['torsion_blocks']},
            'K':{'free':Knf['free_ranks'],'torsion':Knf['torsion_blocks']},
            'Hom_S_K_homological_index_minus_cohomological':{'free':Hnf['free_ranks'],'torsion':Hnf['torsion_blocks']}},
        'chi_framed_annihilator':'0 in Lambda; explicit split free coordinate',
        'chi_ordinary_short_annihilator':'(beta^2)',
        'supported_framed_H0':'(Lambda/(beta))^12',
        'primary_map_on_supported_H0':'injective into H2(K)[beta]',
        'primary_fixed_comparison_space':'every nonempty occurrence-zero fibre is contractible',
        'vertex_basis_determinant':determinant,
        'primary_map_determinant':primary_determinant,
        'frame_state_indices':sorted(M.boundary_ids),
        'source_states':[[j,list(F),list(H),e,M.degree[j]] for j,(F,H,e) in enumerate(M.states)],
        'source_differential':serialize_full_matrix(M.d),
        'frame_differential':serialize_full_matrix(M.d_boundary),
        'coherent_fibre':{k:serialize_full_matrix(v) for k,v in fibre.items()},
        'weight_zero_basis':[[j,list(p),M.weight[j],M.degree[j]] for j,p in sorted(coeff.items())],
        'polynomial_normal_forms':{'C':serialize_normal_form(Cnf,M.weight),
                                   'B':serialize_normal_form(Bnf,M.weight),
                                   'K':serialize_normal_form(Knf,M.weight),
                                   'supported_Hom':serialize_normal_form(Hnf,hom_weight)},
        'supported_Hom_basis':[[2*j+bit,j,'p' if bit==0 else 'e',hom_weight[2*j+bit],hom_degree[2*j+bit]]
                              for j in sorted(kernel_ids) for bit in (0,1)],
        'witnesses':{'phi':serialize_chain(phi,M),'chi':serialize_chain(chi,M),'W':serialize_chain(W,M),
                     'Z_minus':serialize_chain(Z,M),'Z_plus':serialize_chain(Zplus,M)},
        'free_chi_detector':{'target_basis_beta_weight':M.weight[detector_id],
                             'terms':[[j,c,M.weight[j]-M.weight[detector_id]]
                                      for j,col in sorted(detector.items()) for i,c in col.items()],
                             'value_on_chi':1},
        'nonendpoint_vertex_maps':gammas,
        'vertex_basis_Hom_coordinate_matrix':matrix,
        'primary_map_beta_torsion_coordinate_matrix':primary_matrix,
        'verification_counts':dict(sorted(COUNTS.items())),
        'exact_checks':sum(COUNTS.values()),
        'references':['https://stacks.math.columbia.edu/tag/014D',
                      'https://stacks.math.columbia.edu/tag/0A8H',
                      'https://stacks.math.columbia.edu/tag/0117']}
    output.parent.mkdir(parents=True,exist_ok=True)
    text=json.dumps(certificate,indent=2,sort_keys=True)+'\n'
    output.write_text(text,encoding='utf-8')
    print(json.dumps({'certificate':str(output),'sha256':sha256(text.encode()).hexdigest(),
                      'exact_checks':sum(COUNTS.values()),'homology':certificate['weight_zero_homology'],
                      'primary_fixed_space':certificate['primary_fixed_comparison_space']},indent=2,sort_keys=True))
    return certificate


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('branch_a_coherent_endpoint_q_primary_frame_certificate.json'))
    args=parser.parse_args()
    main(args.output)
