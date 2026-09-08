#!/usr/bin/env python3
"""Branch A: full conductor-square completion and marked D03 support test.

Standalone standard-library verifier. No network, companion files, or cached
certificates are used. Polynomial coefficients retain all nine occurrences,
beta, both normalization sheets, all 430 target states, and source relations.
Shared arithmetic and target-construction routines are copied with provenance
from branch_a_normalization_sheet_extension_obstructions_checker.py. All inputs
and new maps are reconstructed; no prior certificate is treated as a proof.
"""
from __future__ import annotations
import argparse
from collections import Counter
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
from fractions import Fraction

DIAGONALS=('02','03','04','13','14','15','24','25','35')
PLUS=frozenset(('13','15','35'))
MINUS=frozenset(('02','04','24'))
SHORT=PLUS|MINUS
LONG=('03','14','25')
SHORT_ORDER=tuple(sorted(SHORT))
VARIABLES=tuple('X'+d for d in DIAGONALS)+('beta',)
ZERO=(0,)*10
COUNTS=Counter()
COMMIT='d1947b67a60d3e88ba77f4ca60ea02c2a306ee61'

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

def serialize_chain(v: dict, M: Complex) -> list:
    return [{'state_index':j,'face':list(M.states[j][0]),'marks':list(M.states[j][1]),
             'occurrence_partner':M.states[j][2],'integer':c,'exponents':list(p)}
            for (j,p),c in sorted(v.items())]

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

def fixed_lattice(S: list[list[int]], label: str) -> dict:
    n=len(S); diff=[[S[i][j]-int(i==j) for j in range(n)] for i in range(n)]
    out=integer_diagonalize(diff,label)
    out['fixed_rank']=n-out['rank']
    check(dense_product(S,out['kernel'])==out['kernel'],'fixed_lattice_exact_action',label)
    return out

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

def serialize_map(mp,M):
    return [{'source':sid,'image':serialize_chain(v,M)}
            for sid,v in sorted(mp.items(),key=lambda item:repr(item[0]))]

def serialize_source(src):
    return [{'id':sid,'degree':g['degree'],'weight':g['weight'],
             'differential':[[dest,p,c] for (dest,p),c in sorted(g['d'].items(),key=lambda item:repr(item[0]))]}
            for sid,g in sorted(src.items(),key=lambda item:repr(item[0]))]

# ---- New audit: the resolved four-corner square and actual spatial carriers ----

def constant_conductor_symbol(v):
    """Realize K/(K intersect I C) inside C/I C, without dropping state labels."""
    return {(j,p):c for (j,p),c in v.items() if conductor_order(p)==0}


def scale(v,n):
    return {k:n*c for k,c in v.items() if n*c}


def cone_source(P,B,k):
    """Homological Cone(k): B_n plus P_{n-1}, d(b,p)=(db+kp,-dp)."""
    out={}
    for sid,g in B.items():
        out['B',sid]={'degree':g['degree'],'weight':g['weight'],
            'd':{(('B',q),m):c for (q,m),c in g['d'].items()}}
    for sid,g in P.items():
        d={(('P',q),m):-c for (q,m),c in g['d'].items()}
        for (q,m),c in k.get(sid,{}).items():put(d,(('B',q),m),c)
        out['P',sid]={'degree':g['degree']+1,'weight':g['weight'],'d':d}
    return out


def differential(source):
    return {sid:g['d'] for sid,g in source.items()}


def chain_map_check(src,dst,mp,label):
    for sid,g in src.items():
        check(apply(differential(dst),mp.get(sid,{}))==apply(mp,g['d']),
              'new_source_chain_map',(label,sid))
        for (tid,p),c in mp.get(sid,{}).items():
            check(dst[tid]['degree']==g['degree'],'new_source_map_degree',(label,sid,tid))
            check(tuple(a+b for a,b in zip(dst[tid]['weight'],p[:9]))==g['weight'],
                  'new_source_map_occurrence_weight',(label,sid,tid))


def serial_polynomial_map(mp):
    return [[sid,[[tid,p,c] for (tid,p),c in sorted(col.items(),key=lambda x:repr(x[0]))]]
            for sid,col in sorted(mp.items(),key=lambda x:repr(x[0]))]


def matrix_of_basis(basis,rows):
    return [[v.get(row,0) for v in basis] for row in rows]


def combine_basis(basis,coords):
    result={}
    for j,c in coords.items():result=add(result,basis[j],c)
    return result


def support_kernel(M,chains,allowed,label):
    equations={j:{key:c for key,c in v.items() if key[0] not in allowed}
               for j,v in enumerate(chains)}
    result=unit_kernel(equations,label=label)
    for coords in result['basis']:
        v=combine_basis(chains,coords)
        check(all(j in allowed for j,p in v),'spatial_kernel_has_declared_support',label)
    return result


def verify_subcomplex(M,ids,label):
    for j in ids:
        check(all(i in ids for i,p in M.d[j]),'source_defined_carrier_is_subcomplex',(label,j))


def run(output):
    A=ExtensionAudit();M=A.M
    # Reconstruct the extension lattice directly from ambient homotopies.
    # dH must be conductor-valued; closure then follows from the actual d^2=0.
    HH=A.hom(A.I,False,1,label='all_candidate_restriction_homotopies')
    check((len(HH['unknown']),HH['kernel']['rank'],len(HH['maps']))==(33,33,0),
          'restriction_homotopy_has_no_cycle_ambiguity')
    residual={j:{key:c for key,c in col.items() if conductor_order(key[2])==0}
              for j,col in HH['columns'].items()}
    ext=unit_kernel(residual,label='constant_conductor_part_of_dH')
    check((ext['rank'],len(ext['basis']))==(24,9),'nine_compatible_homotopies_reconstructed')
    hmaps=[HH['pack'](v) for v in ext['basis']]
    fmaps=[A.hom_differential(A.I,h,1) for h in hmaps]
    hchains=[]
    for j,(h,f) in enumerate(zip(hmaps,fmaps)):
        check(set(h)=={(0,SHORT_ORDER.index('35'))},'homotopy_only_on_actual_occurrence_generator',j)
        check(bool(f) and not A.hom_differential(A.I,f), 'nonzero_ideal_map_closes',j)
        A.verify_frame(h,False,('new_H',j));A.verify_frame(f,True,('new_f',j))
        U=next(iter(h.values()));hchains.append(U)
        check(all(conductor_order(p)==0 for i,p in U),'all_H_coefficients_are_conductor_constant',j)
        check(constant_conductor_symbol(apply(M.d,U))=={},'H_gives_closed_conductor_symbol',j)
    all_f={(sid,j,p) for f in fmaps for sid,col in f.items() for j,p in col}
    fcols={i:{(sid,j,p):c for sid,col in f.items() for (j,p),c in col.items()}
           for i,f in enumerate(fmaps)}
    check(unit_kernel(fcols,label='independence_of_nine_ideal_maps')['rank']==9,
          'nine_f_values_are_independent')
    check(not A.hom(A.I,True,1,label='relative_homotopies').get('unknown'),
          'no_relative_identifications_between_extension_classes')
    Qh=A.hom(A.Q,False,0,label='normalization_sheet_zero_maps')
    check(not Qh['maps'],'zero_normalization_maps_replayed')
    check(not A.hom(A.Q,False,1,label='normalization_sheet_higher_maps')['unknown'],
          'no_normalization_homotopy_slots')

    # Actual node R, both normalization sheets, single and doubled conductors.
    Rsrc={0:{'degree':0,'weight':(0,)*9,'d':{}}}
    k={sid:({(0,monomial('X'+SHORT_ORDER[sid[1]])):1} if sid[0]==0 else {})
       for sid in A.I}
    nu={0:{((0,0),ZERO):1,((0,1),ZERO):1}}
    t={sid:{((sid[0]+1,sid[1]),ZERO):(-1)**sid[0]} for sid in A.I}
    chain_map_check(A.I,Rsrc,k,'ideal_to_node')
    chain_map_check(Rsrc,A.Q,nu,'node_to_normalization')
    for sid,g in A.I.items():
        dt=add(apply(differential(A.Q),t[sid]),apply(t,g['d']))
        nk_minus_j=add(apply(nu,k[sid]),A.j[sid],-1)
        check(dt==nk_minus_j,'resolved_ideal_square_required_homotopy',sid)
    W=cone_source(A.I,Rsrc,k)
    E=cone_source(A.I,A.Q,A.j)
    A.verify_source(W,'single_conductor_resolution')
    A.verify_source(E,'doubled_conductor_resolution')
    incR={sid:{(('B',sid),ZERO):1} for sid in Rsrc}
    incQ={sid:{(('B',sid),ZERO):1} for sid in A.Q}
    Delta={}
    naive={}
    for sid,g in W.items():
        kind,old=sid
        if kind=='B':
            v={(('B',q),p):c for (q,p),c in nu[old].items()}
            Delta[sid]=dict(v);naive[sid]=dict(v)
        else:
            v={(('P',old),ZERO):1};naive[sid]=dict(v)
            for (q,p),c in t[old].items():put(v,(('B',q),p),c)
            Delta[sid]=v
    chain_map_check(W,E,Delta,'single_to_double_conductor_diagonal')
    chain_map_check(Rsrc,W,incR,'node_conductor_quotient')
    chain_map_check(A.Q,E,incQ,'normalization_conductor_quotient')
    check(apply(Delta,incR[0])==apply(incQ,nu[0]),'resolved_four_corner_square_commutes')
    failures=[]
    for sid,g in W.items():
        err=add(apply(differential(E),naive[sid]),apply(naive,g['d']),-1)
        if err:failures.append((sid,err))
    check(len(failures)==6,'naive_diagonal_has_six_missing_relation_columns')
    check(all(len(col)==1 and abs(next(iter(col.values())))==1 for sid,col in failures),
          'missing_diagonal_terms_are_primitive_not_torsion')

    # Identify the doubled-conductor cone with two full conductor resolutions.
    # The terminal ideal summand is preserved by every source differential.
    terminal={}
    for sid,g in sorted(A.I.items()):
        if sid[0]==0:terminal[sid]=0 if SHORT_ORDER[sid[1]] in PLUS else 1
        else:
            values={terminal[q] for q,p in g['d']}
            check(len(values)==1,'ideal_resolution_retains_terminal_sheet',sid)
            terminal[sid]=next(iter(values))
    W2={}
    for sheet in (0,1):
        for sid,g in W.items():
            W2[sheet,sid]={'degree':g['degree'],'weight':g['weight'],
              'd':{((sheet,q),p):c for (q,p),c in g['d'].items()}}
    split={};join={}
    for sid,g in E.items():
        kind,old=sid
        if kind=='P':tid=(terminal[old],('P',old));sg=1
        elif old[0]==0:tid=(old[1],('B',0));sg=1
        else:
            pid=(old[0]-1,old[1]);tid=(1-terminal[pid],('P',pid));sg=(-1)**pid[0]
        split[sid]={(tid,ZERO):sg};join[tid]={(sid,ZERO):sg}
    chain_map_check(E,W2,split,'doubled_conductor_split_into_actual_sheets')
    chain_map_check(W2,E,join,'doubled_conductor_split_inverse')
    for sid in E:check(apply(join,split[sid])=={(sid,ZERO):1},'double_split_left_inverse',sid)
    for sid in W2:check(apply(split,join[sid])=={(sid,ZERO):1},'double_split_right_inverse',sid)
    for sid in W:
        check(apply(split,Delta[sid])=={((0,sid),ZERO):1,((1,sid),ZERO):1},
              'resolved_diagonal_is_diagonal_on_every_relation',sid)

    # Explicit degreewise split Mayer--Vietoris sequence, without treating a
    # graded section as a chain map. Middle = Q direct-sum W; last map q-Delta(w).
    mid={}
    for tag,S in [('Q',A.Q),('W',W)]:
        for sid,g in S.items():
            mid[tag,sid]={'degree':g['degree'],'weight':g['weight'],
                'd':{((tag,q),p):c for (q,p),c in g['d'].items()}}
    aMV={0:{(('Q',(0,0)),ZERO):1,(('Q',(0,1)),ZERO):1,(('W',('B',0)),ZERO):1}}
    bMV={}
    for sid,g in mid.items():
        tag,old=sid
        bMV[sid]=incQ[old] if tag=='Q' else scale(Delta[old],-1)
    chain_map_check(Rsrc,mid,aMV,'MV_left_arrow')
    chain_map_check(mid,E,bMV,'MV_right_arrow')
    check(not apply(bMV,aMV[0]),'MV_composition_zero')
    section={}
    for sid,g in E.items():
        tag,old=sid
        if tag=='B':section[sid]={(('Q',old),ZERO):1}
        else:
            v={(('W',('P',old)),ZERO):-1}
            for (qid,p),c in t[old].items():put(v,(('Q',qid),p),-c)
            section[sid]=v
        check(apply(bMV,section[sid])=={(sid,ZERO):1},'MV_graded_right_section',sid)
    retract={sid:({(0,ZERO):1} if sid==('W',('B',0)) else {}) for sid in mid}
    for sid in mid:
        lhs=add(apply(aMV,retract[sid]),apply(section,bMV[sid]))
        check(lhs=={(sid,ZERO):1},'MV_degreewise_split_exactness',sid)
    check(not A.hom(Rsrc,False,label='node_maps_into_K')['maps'],'node_closed_maps_zero')
    check(not A.hom(Rsrc,False,1,label='node_homotopies_into_K')['unknown'],'node_homotopy_slots_zero')

    # Each previously constructed triple induces genuine cofiber maps, hence
    # conductor maps into L=K/N. Retain the minus sign of Cone(i f).
    completions=[]
    for n,(h,f) in enumerate(zip(hmaps,fmaps)):
        psiW={sid:scale(constant_conductor_symbol(h.get(sid[1],{})),-1)
              if sid[0]=='P' else {} for sid in W}
        psiE={sid:scale(constant_conductor_symbol(h.get(sid[1],{})),-1)
              if sid[0]=='P' else {} for sid in E}
        for name,S,psi in [('single',W,psiW),('double',E,psiE)]:
            defect=A.hom_differential(S,psi)
            check(all(not constant_conductor_symbol(v) for v in defect.values()),
                  'conductor_comparison_into_K_mod_N_is_chain_map',(n,name))
            # Stronger check in Cone(N->K): pair (-H,f) before taking quotient.
            partK={sid:scale(h.get(sid[1],{}),-1) if sid[0]=='P' else {} for sid in S}
            partN={sid:f.get(sid[1],{}) if sid[0]=='P' else {} for sid in S}
            for sid,g in S.items():
                lhsK=add(apply(M.d,partK[sid]),partN[sid])
                lhsN=scale(apply(M.d,partN[sid]),-1)
                check(lhsK==apply(partK,g['d']) and lhsN==apply(partN,g['d']),
                      'complete_target_cofiber_map_equation',(n,name,sid))
                check(not restrict(partK[sid],M.V) and not restrict(partN[sid],M.V)
                      and not restrict(partK[sid],M.Q) and not restrict(partN[sid],M.Q),
                      'cofiber_map_retains_all_endpoint_Q_components',(n,name,sid))
            check(all(not col for sid,col in psi.items() if sid[0]=='B'),
                  'conductor_comparison_zero_on_degree_zero_units',(n,name))
        for sid in W:
            check(constant_conductor_symbol(apply(psiE,Delta[sid]))==psiW[sid],
                  'single_double_conductor_diagonal_naturality',(n,sid))
        for sid in W:
            plus=constant_conductor_symbol(apply(psiE,join[(0,sid)]))
            minus=constant_conductor_symbol(apply(psiE,join[(1,sid)]))
            check(plus==psiW[sid] and not minus,
                  'upper_conductor_map_has_derived_positive_sheet_provenance',(n,sid))
        for sid in A.Q:check(not apply(psiE,incQ[sid]),'upper_vertical_square_zero',(n,sid))
        check(not apply(psiW,incR[0]),'lower_vertical_square_zero',n)
        completions.append({'homotopy':serialize_map(h,M),'ideal_map':serialize_map(f,M),
             'lower_conductor_comparison':serialize_map({s:v for s,v in psiW.items() if v},M),
             'upper_conductor_comparison':serialize_map({s:v for s,v in psiE.items() if v},M)})
    lowercols={j:{(sid,ti,p):c for sid,col in Wpsi.items() for (ti,p),c in col.items()}
               for j,Wpsi in enumerate([{sid:scale(constant_conductor_symbol(h.get(sid[1],{})),-1)
                                          if sid[0]=='P' else {} for sid in W} for h in hmaps])}
    check(unit_kernel(lowercols,label='lower_conductor_comparison_independence')['rank']==9,
          'all_nine_completions_still_independent')
    # A homotopy W[3]->L would require L_4 at occurrence zero on its unit,
    # or L_5 and above on its first relation terms. These groups vanish.
    check(not A.target_basis((0,)*9,4,False),'no_homotopy_on_lower_conductor_unit')
    check(max(M.degree.values())==4,'no_higher_target_homotopy_slots')

    # Actual reflection action. Rotation subsequently moves the occurrence
    # correction to 15 and 13; no averaging or new source character is inserted.
    def ext_coords(h):
        raw=A.raw_coordinates(HH,h)
        ans={j:raw.get(fr,0) for j,fr in enumerate(ext['free']) if raw.get(fr,0)}
        check(combine_basis(ext['basis'],ans)==raw,'extension_basis_coordinate_reconstruction')
        return ans
    Scols={j:ext_coords(A.reflect_map(h)) for j,h in enumerate(hmaps)}
    S=dense_columns([[Scols[j].get(i,0) for i in range(9)] for j in range(9)],9)
    check(dense_product(S,S)==dense_identity(9),'reflection_square_on_nine')
    fixed=fixed_lattice(S,'full_square_fixed_extensions')
    check(fixed['fixed_rank']==3,'three_equivariant_completions_remain')
    invariantH=[]
    for kcol in range(3):
        co={j:fixed['kernel'][j][kcol] for j in range(9) if fixed['kernel'][j][kcol]}
        U=combine_basis(hchains,co)
        check(polygon_action(M,U,0,1)==U,'explicit_fixed_H_chain',kcol)
        invariantH.append(U)

    # Transport the constructed comparisons over all three occurrence labels.
    orbit_models={o:(M if o=='35' else Complex(o)) for o in ('35','15','13')}
    relation_ids={tuple(r['name']):i for i,r in enumerate(A.presentation['relations'])}
    def transport_source_map(mp,rot,ref=0):
        out={}
        for (n,i),v in mp.items():
            if n==0:
                dest=SHORT_ORDER.index(polygon_diagonal(SHORT_ORDER[i],rot,ref));sg=1
            else:
                kind,a,c=A.presentation['relations'][i]['name']
                a=polygon_diagonal(a,rot,ref);c=polygon_diagonal(c,rot,ref);sg=1
                if kind=='K' and a>c:a,c,sg=c,a,-1
                dest=relation_ids[kind,a,c]
            out[n,dest]=add(out.get((n,dest),{}),polygon_action(M,v,rot,ref),sg)
        return out
    for rot in range(3):
        for ref in range(2):
            Mt=orbit_models[polygon_diagonal('35',rot,ref)]
            for sid in range(430):
                check(apply(Mt.d,polygon_action(M,unit(sid),rot,ref))
                      ==polygon_action(M,M.d[sid],rot,ref),
                      'entire_rotated_target_differential',(rot,ref,sid))
        for j,U in enumerate(invariantH):
            h={(0,SHORT_ORDER.index('35')):U}
            f=A.hom_differential(A.I,h,1)
            th=transport_source_map(h,rot);tf=transport_source_map(f,rot)
            Mt=orbit_models[polygon_diagonal('35',rot)]
            for sid,g in A.I.items():
                lhs=apply(Mt.d,th.get(sid,{}))
                for (sc,p),c in g['d'].items():lhs=add(lhs,multiply(th.get(sc,{}),p,c))
                check(lhs==tf.get(sid,{}),'all_rotated_restriction_homotopy_equations',(rot,j,sid))
            for mp in (th,tf):
                for sid,col in mp.items():
                    check(not restrict(col,Mt.V) and not restrict(col,Mt.Q)
                          and not restrict(apply(Mt.d,col),Mt.V),
                          'all_rotated_complete_endpoint_and_Q_frames',(rot,j,sid))

    # Apply the genuine, independently labelled D03 marked-gallery support.
    gallery_faces={('13','15','35'),('03','13','35'),('02','03','35'),
                   ('13','35'),('03','35')}
    carriers={
       'complete':set(range(430)),
       'short_facet_35':{j for j,(F,H,e) in enumerate(M.states) if '35' in F},
       'long_facet_03':{j for j,(F,H,e) in enumerate(M.states) if '03' in F},
       'marked_D03_gallery':{j for j,(F,H,e) in enumerate(M.states) if F in gallery_faces},
       'union_03_or_35':{j for j,(F,H,e) in enumerate(M.states) if '03' in F or '35' in F},
    }
    supports={}
    for label,ids in carriers.items():
        verify_subcomplex(M,ids,label)
        ker=support_kernel(M,hchains,ids,label)
        fixedKer=support_kernel(M,invariantH,ids,label+'_fixed')
        # A spatial comparison restricts BOTH f and H. Verify this directly,
        # including generator and relation images; do not infer from H alone.
        equation_cols={j:{('H',ti,p):c for (ti,p),c in hchains[j].items() if ti not in ids}
                       for j in range(9)}
        for j,f in enumerate(fmaps):
            for sid,col in f.items():
                for (ti,p),c in col.items():
                    if ti not in ids:put(equation_cols[j],('f',sid,ti,p),c)
        paired=unit_kernel(equation_cols,label='entire_source_comparison_support_'+label)
        check(len(paired['basis'])==len(ker['basis']),'f_and_H_support_agree',label)
        supports[label]={'target_states':len(ids),'rank':len(ker['basis']),
          'invariant_rank':len(fixedKer['basis']),
          'basis_coordinates':[sorted(v.items()) for v in ker['basis']],
          'unit_pivots':[[j,sorted(row.items())] for j,row in ker['pivots']],
          'full_equation_rank':paired['rank']}
    check([supports[x]['rank'] for x in carriers]==[9,2,0,0,2],
          'all_spatial_support_ranks')
    check(supports['marked_D03_gallery']['target_states']==64,'complete_native_gallery_retained')
    check(supports['short_facet_35']['invariant_rank']==0,'no_invariant_35_facet_extension')

    # Two short-facet maps displayed in a geometric basis, with no division.
    def basis(F):return unit(M.index[tuple(F),tuple(F),1])
    Ua=add(add(basis(('02','03','35')),basis(('02','25','35'))),
           multiply(basis(('02','35')),monomial('beta')),-1)
    Ub=add(add(multiply(basis(('35',)),monomial('beta','beta')),
               multiply(basis(('03','35')),monomial('beta'))),
               multiply(basis(('25','35')),monomial('beta')))
    for name,U in [('U02',Ua),('U35',Ub)]:
        h={(0,SHORT_ORDER.index('35')):U};co=ext_coords(h)
        check(combine_basis(hchains,co)==U,'displayed_35_basis_lifts',name)
        f=A.hom_differential(A.I,h,1)
        A.verify_frame(h,False,('displayed',name));A.verify_frame(f,True,('displayed',name))
        check(polygon_action(M,U,0,1)==scale(U,-1),'short_facet_reflection_is_minus_one',name)
    # Their D25 rows are distinct, making exclusion from a D03-only carrier
    # visible coefficient-by-coefficient.
    detection=[(M.index[('02','25','35'),('02','25','35'),1],ZERO),
               (M.index[('25','35'),('25','35'),1],monomial('beta'))]
    det=matrix_of_basis([Ua,Ub],detection)
    check(det==[[1,0],[0,1]],'D25_leakage_has_integral_identity_detector')

    # Reflection-fixed carriers are tested without silently changing source
    # parity. A deliberate sign twist changes -I to +I, an explicit control.
    check([polygon_action(M,U,0,1) for U in [Ua,Ub]]==[scale(U,-1) for U in [Ua,Ub]],
          'untwisted_reflection_control')
    check([scale(polygon_action(M,U,0,1),-1) for U in [Ua,Ub]]==[Ua,Ub],
          'sign_twist_would_change_the_parity_test')

    # Export complete data; mathematical digest excludes the execution counts.
    cert={
      'schema':'marici.branchA.full_conductor_square_and_d03_support.v1',
      'scope':{'ring':'Z[beta,X_d]/(X_minus*X_plus)',
        'source_placement':'I, R and normalization modules at homological degree 3',
        'occurrence_map_degree':[0]*9,'regulator_normal_output_grade':3,
        'target_K':'q=0, full endpoint components=0, incoming endpoint components=0',
        'target_N':'K intersect I*C_beta','target_L':'K/N, realized in C_beta/I*C_beta',
        'new_target_square':'K --id--> K, vertically to L --id--> L',
        'normalization_top_maps':'zero, as forced in the tested degree',
        'physical_six_functor_square_identified':False,
        'physical_Delta_J_selected':False,
        'marked_gallery_test':'ordinary support containment in the published two-edge D03 gallery',
        'no_claim_against_larger_or_extraordinary_correspondences':True},
      'sources':{'repository':'andrey-kokoev/marici','commit':COMMIT,
        'normalization_blob':'840258522d45e450e4f1e8bb927d9aae58c75566',
        'gallery_blob':'d9ac9420e7360013ff6acde34df51a4941b34101',
        'absolute_target_blob':'b967151cb0ee822e2361b9334a4ab26082c12682',
        'cone_reference':'https://stacks.math.columbia.edu/tag/014D',
        'hom_reference':'https://stacks.math.columbia.edu/tag/0A8H',
        'projective_reference':'https://stacks.math.columbia.edu/tag/064B'},
      'dimensions':{'target_states':430,'ideal_resolution_states':len(A.I),
        'normalization_resolution_states':len(A.Q),'single_conductor_states':len(W),
        'doubled_conductor_states':len(E),'coherent_extensions':9,'invariant_extensions':3,
        'full_square_additional_constraints':0,'marked_gallery_extensions':0,
        'short_facet_35_extensions':2,'short_facet_35_invariant_extensions':0,
        'naive_resolved_diagonal_defect_columns':6},
      'source_square':{'ideal':serialize_source(A.I),'node':serialize_source(Rsrc),
        'normalization':serialize_source(A.Q),'single_conductor':serialize_source(W),
        'double_conductor':serialize_source(E),'ideal_to_node':serial_polynomial_map(k),
        'ideal_to_normalization':serial_polynomial_map(A.j),
        'node_to_normalization':serial_polynomial_map(nu),
        'required_homotopy':serial_polynomial_map(t),'resolved_diagonal':serial_polynomial_map(Delta),
        'naive_defects':serial_polynomial_map(dict(failures)),
        'two_conductor_resolutions':serialize_source(W2),
        'double_conductor_sheet_split':serial_polynomial_map(split),
        'double_conductor_sheet_split_inverse':serial_polynomial_map(join),
        'MV_middle':serialize_source(mid),'MV_inclusion':serial_polynomial_map(aMV),
        'MV_quotient':serial_polynomial_map(bMV),'MV_graded_section':serial_polynomial_map(section),
        'MV_graded_retraction':serial_polynomial_map(retract)},
      'target':{'states':M.states,'differential':[[j,[[i,p,c] for (i,p),c in sorted(col.items())]]
                                               for j,col in M.d.items()]},
      'extension_equations':{'homotopy_cochains':len(HH['unknown']),
         'homotopy_differential_rank':HH['kernel']['rank'],
         'conductor_constant_defect_rank':ext['rank'],
         'basis':[sorted(v.items()) for v in ext['basis']]},
      'full_square_completions':completions,
      'reflection':{'matrix_on_nine':S,'fixed_basis':fixed['kernel'],
                    'fixed_homotopies':[serialize_chain(v,M) for v in invariantH],
                    'short_facet_matrix':[[-1,0],[0,-1]],
                    'source_sign_twist_added':False},
      'support_tests':supports,
      'examples':{'short_facet_U02':serialize_chain(Ua,M),'short_facet_U35':serialize_chain(Ub,M),
                  'unavoidable_D25_detector':det,
                  'D25_detection_rows':[[j,list(p)] for j,p in detection]},
    }
    digest=sha256(json.dumps(cert,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    cert['mathematical_sha256']=digest
    cert['verification']={'exact_checks':sum(COUNTS.values()),'by_family':dict(sorted(COUNTS.items()))}
    output.write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':'verified','exact_checks':sum(COUNTS.values()),
        'completion_rank':9,'invariant_rank':3,'marked_gallery_rank':0,
        'short_facet_rank':2,'short_facet_invariant_rank':0,
        'mathematical_sha256':digest,'certificate':str(output)},indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name(
        'branch_a_full_conductor_square_and_d03_support_certificate.json'))
    args=parser.parse_args()
    run(args.output)
