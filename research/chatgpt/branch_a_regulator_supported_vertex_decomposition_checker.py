#!/usr/bin/env python3
"""Regulator-supported map classification and the retained two-normal obstruction.

Self-contained; Python standard library only. Reconstructs the complete 430-state
coefficient complex. All calculations are exact over
  Z[beta,X02,X03,X04,X13,X14,X15,X24,X25,X35]/(X_even X_odd).
No X or beta inverse is used in a constructed map. Integer reductions compute
entire occurrence-weight-zero components, not bounded polynomial searches.
"""
from __future__ import annotations
import argparse
from collections import Counter
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path

DIAGONALS=('02','03','04','13','14','15','24','25','35')
PLUS=frozenset(('13','15','35'))
MINUS=frozenset(('02','04','24'))
SHORT=PLUS|MINUS
LONG=('03','14','25')
VARS=tuple('X'+d for d in DIAGONALS)+('beta',)
POS={v:i for i,v in enumerate(VARS)}
DPOS={d:i for i,d in enumerate(DIAGONALS)}
ZERO=(0,)*10
COUNTS=Counter()
REPOSITORY_COMMIT='d1947b67a60d3e88ba77f4ca60ea02c2a306ee61'

# The previous packet's first beta-annihilating primitive, in labelled form.
# Rows are (face, native marks, occurrence partner, beta exponent, coefficient).
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

def check(value: bool, family: str, detail='') -> None:
    if not value: raise AssertionError(f'{family}: {detail}')
    COUNTS[family]+=1

def put(d,k,c):
    if c:
        d[k]=d.get(k,0)+c
        if not d[k]: del d[k]

def add(a,b,scale=1):
    o=dict(a)
    for k,c in b.items(): put(o,k,scale*c)
    return o

def mono(*names):
    p=[0]*10
    for name in names: p[POS[name]]+=1
    return tuple(p)

def beta_power(n):
    if n<0: raise ValueError('negative beta power')
    return (0,)*9+(n,)

def pplus(p,q): return tuple(a+b for a,b in zip(p,q))

def survives(p):
    return not (any(p[DPOS[d]] for d in PLUS) and any(p[DPOS[d]] for d in MINUS))

def scale(a,p,sign=1):
    o={}
    for (j,q),c in a.items():
        r=pplus(p,q)
        if survives(r): put(o,(j,r),sign*c)
    return o

def beta_coefficient(a,k):
    o={}
    for (j,p),c in a.items():
        if p[9]==k: put(o,(j,p[:9]+(0,)),c)
    return o

def beta_one(a):
    o={}
    for (j,p),c in a.items(): put(o,(j,p[:9]+(0,)),c)
    return o

def divide_beta(a):
    # Exact factor extraction on the displayed divisible chains, not localization.
    o={}
    for (j,p),c in a.items():
        check(p[9]>0,'exact_beta_divisibility',j)
        put(o,(j,p[:9]+(p[9]-1,)),c)
    check(scale(o,mono('beta'))==a,'exact_beta_factorization')
    return o

def cross(a,b):
    x,y=map(int,a);v,w=map(int,b)
    return x<v<y<w or v<x<w<y

class Model:
    def __init__(self,mode):
        if mode not in ('family','central','one'): raise ValueError(mode)
        self.mode=mode
        self.faces=[F for n in range(4) for F in combinations(DIAGONALS,n)
                    if all(not cross(a,b) for a,b in combinations(F,2))]
        self.triangles=[F for F in self.faces if len(F)==3]
        self.states=[(F,H,e) for F in self.faces for n in range(len(F)+1)
                     for H in combinations(F,n) for e in (0,1)]
        self.idx={s:j for j,s in enumerate(self.states)}
        self.deg={j:3-len(F)+len(H)+e for j,(F,H,e) in enumerate(self.states)}
        self.V={j for j,(F,H,e) in enumerate(self.states) if frozenset(F) in (PLUS,MINUS)}
        self.B={j for j,(F,H,e) in enumerate(self.states) if set(F)&SHORT}
        self.Q=set(range(len(self.states)))-self.B
        self.vertex={j for j,(F,H,e) in enumerate(self.states) if len(F)==3}
        fs=set(self.faces);self.d={}
        for j,(F,H,e) in enumerate(self.states):
            c=[]
            for a in DIAGONALS:
                FF=tuple(sorted(F+(a,)))
                if a not in F and FF in fs:
                    c.append((self.idx[FF,H,e],mono('X'+a),(-1)**sum(b<a for b in F)))
            if mode!='central':
                for k,a in enumerate(H):
                    p=mono('beta','X'+a) if mode=='family' else mono('X'+a)
                    c.append((self.idx[F,H[:k]+H[k+1:],e],p,(-1)**(3-len(F)+k)))
            if e:c.append((self.idx[F,H,0],mono('X35'),(-1)**(3-len(F)+len(H))))
            self.d[j]=c
        check(Counter(map(len,self.faces))=={0:1,1:9,2:21,3:14},'source_face_census')
        check((len(self.states),len(self.V),len(self.B),len(self.Q))==(430,32,416,14),'full_support_counts')
        for j in range(430):
            b=self.basis(j)
            check(not self.boundary(self.boundary(b)),'full_d_squared_'+mode,j)
            check(all(self.deg[i]==self.deg[j]-1 for i,p,c in self.d[j]),'full_degree_'+mode,j)
            if j in self.V:check(all(i in self.V for i,p,c in self.d[j]),'endpoint_subcomplex_'+mode,j)
            if j in self.B:check(all(i in self.B for i,p,c in self.d[j]),'short_subcomplex_'+mode,j)
    def basis(self,j): return {(j,ZERO):1}
    def boundary(self,a):
        o={}
        for (j,p),c in a.items():
            for i,q,v in self.d[j]:
                r=pplus(p,q)
                if survives(r):put(o,(i,r),c*v)
        return o
    def project(self,a,ids): return {key:c for key,c in a.items() if key[0] in ids}
    def quotient_boundary(self,a,ids): return self.project(self.boundary(a),ids)
    def occurrence_homotopy(self,a):
        o={}
        for (j,p),c in a.items():
            F,H,e=self.states[j]
            if not e:put(o,(self.idx[F,H,1],p),c*(-1)**(3-len(F)+len(H)))
        return o
    def replace_native35(self,a):
        o={}
        for (j,p),c in a.items():
            F,H,e=self.states[j]
            if '35' not in H:put(o,(j,p),c)
            elif not e:put(o,(self.idx[F,tuple(d for d in H if d!='35'),1],pplus(p,mono('beta'))),c)
        return o

def fmap_add(f,g,sign=1): return (add(f[0],g[0],sign),add(f[1],g[1],sign))
def fmap_scale(f,p,sign=1):return (scale(f[0],p,sign),scale(f[1],p,sign))
def hom_d(M,f,k=0):
    # f(p) has degree 2-k, f(e) degree 3-k, de=beta*p.
    return (M.boundary(f[0]),add(M.boundary(f[1]),scale(f[0],mono('beta')),-((-1)**k)))
def is_zero_map(f):return not f[0] and not f[1]

def int_apply(mat,v):
    o={}
    for j,c in v.items():
        for i,k in mat[j].items():put(o,i,c*k)
    return o

def integer_retract(original,degree):
    # Integral algebraic cancellation, retaining all three contraction matrices.
    d={j:dict(c) for j,c in original.items()}
    proj={j:{j:1} for j in d};inc={j:{j:1} for j in d};h={j:{} for j in d}
    active=set(d);pivots=[]
    while True:
        pivot=None
        for hi in sorted(active,key=lambda j:(-degree[j],j)):
            for lo,c in sorted(d[hi].items()):
                if abs(c)==1:pivot=(lo,hi,c);break
            if pivot:break
        if pivot is None:break
        lo,hi,c=pivot;rest={i:a for i,a in d[hi].items() if i!=lo};ih=inc[hi]
        for j,v in list(proj.items()):
            a=v.get(lo,0)
            if a:h[j]=add(h[j],ih,c*a)
            proj[j]=add({i:b for i,b in v.items() if i not in (lo,hi)},rest,-c*a)
        for j in sorted(active-{lo,hi}):
            a=d[j].get(lo,0)
            if a:inc[j]=add(inc[j],ih,-c*a)
            d[j]=add({i:b for i,b in d[j].items() if i not in (lo,hi)},rest,-c*a)
        for j in (lo,hi):del d[j];del inc[j]
        active-={lo,hi};pivots.append(pivot)
    check(all(not c for c in d.values()),'integral_reduction_residual_zero')
    for j,c in original.items():
        check(not int_apply(original,c),'component_d_squared',j)
        check(not int_apply(proj,c),'component_projection_chain',j)
        check(add(int_apply(original,h[j]),int_apply(h,c))==add({j:1},int_apply(inc,proj[j]),-1),'complete_contraction_identity',j)
    for j,v in inc.items():
        check(not int_apply(original,v),'residual_cycle',j)
        check(int_apply(proj,v)=={j:1},'retraction_identity',j)
    return {'p':proj,'i':inc,'h':h,'pivots':pivots,'residual':sorted(d),
            'homology':dict(sorted(Counter(degree[j] for j in d).items()))}

def dense_mul(A,B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]

def identity(n):return [[int(i==j) for j in range(n)] for i in range(n)]

def unit_smith(A):
    """Reduce by unimodular integer operations; require the entire remainder zero."""
    m=len(A);n=len(A[0]) if A else 0
    D=[row[:] for row in A];L=identity(m);R=identity(n);k=0;ops=[]
    while k<min(m,n):
        pair=next(((i,j) for i in range(k,m) for j in range(k,n) if abs(D[i][j])==1),None)
        if pair is None:break
        i,j=pair
        if i!=k:D[i],D[k]=D[k],D[i];L[i],L[k]=L[k],L[i];ops.append(['row_swap',i,k])
        if j!=k:
            for row in D:row[j],row[k]=row[k],row[j]
            for row in R:row[j],row[k]=row[k],row[j]
            ops.append(['column_swap',j,k])
        if D[k][k]==-1:
            D[k]=[-v for v in D[k]];L[k]=[-v for v in L[k]];ops.append(['row_sign',k])
        for i in range(m):
            if i==k:continue
            c=D[i][k]
            if c:
                D[i]=[a-c*b for a,b in zip(D[i],D[k])]
                L[i]=[a-c*b for a,b in zip(L[i],L[k])];ops.append(['row_add',i,k,-c])
        for j in range(n):
            if j==k:continue
            c=D[k][j]
            if c:
                for row in D:row[j]-=c*row[k]
                for row in R:row[j]-=c*row[k]
                ops.append(['column_add',j,k,-c])
        k+=1
    check(all(D[i][j]==int(i==j and i<k) for i in range(m) for j in range(n)),'unit_Smith_complete_diagonal')
    check(dense_mul(dense_mul(L,A),R)==D,'unit_Smith_witness_identity')
    return {'rank':k,'left':L,'right':R,'diagonal':D,'operations':ops}

def chain_json(c,M):
    return [{'state':j,'face':list(M.states[j][0]),'marks':list(M.states[j][1]),
             'occurrence_partner':M.states[j][2],'degree':M.deg[j],
             'coefficient':v,'exponents':list(p)} for (j,p),v in sorted(c.items())]
def map_json(f,M):return {'p':chain_json(f[0],M),'e':chain_json(f[1],M)}
def intmat_json(m):return [[j,i,c] for j,col in sorted(m.items()) for i,c in sorted(col.items())]
def retract_json(r):
    return {'homology':r['homology'],'residual':r['residual'],'unit_pivots':r['pivots'],
            'projection':intmat_json(r['p']),'inclusion':intmat_json(r['i']),'homotopy':intmat_json(r['h'])}

def main(output):
    M=Model('family');M0=Model('central');M1=Model('one')
    beta=mono('beta');x35=mono('X35');all_ids=set(range(430))
    for j in range(430):
        v=M.basis(j)
        check(beta_coefficient(M.boundary(v),0)==M0.boundary(v),'central_base_change',j)
        check(beta_one(M.boundary(v))==M1.boundary(v),'beta_one_base_change',j)
        check(add(M.boundary(M.occurrence_homotopy(v)),M.occurrence_homotopy(M.boundary(v)))==scale(v,x35),'occurrence_multiplication_homotopy',j)
    Psi={(M.idx[F,F,0],beta_power(3-len(F))):(-1)**(len(F)*(len(F)+1)//2) for F in M.faces}
    Z=M.replace_native35(Psi)
    H={(M.idx[F,Hm,e],beta_power(b)):c for F,Hm,e,b,c in H_INPUT}
    A=divide_beta(M.boundary(H));G=add(H,Z)
    f03=(A,H);fmu=(A,G);D=({},Z)
    check(not M.boundary(Psi),'Psi_closed')
    check(not M.boundary(Z),'Z_closed')
    check(not M.boundary(A),'primary_closed')
    check(M.boundary(G)==scale(A,beta),'second_primitive_same_primary')
    check(is_zero_map(hom_d(M,f03)) and is_zero_map(hom_d(M,fmu)),'original_supported_maps')
    check(fmap_add(fmu,f03,-1)==D,'original_difference')
    check((len(A),len(H),len(G),len(Z))==(21,15,30,45),'original_packet_counts')

    vertices=[];gammas=[];tops=[];bottoms=[]
    for F in M.triangles:
        E=M.basis(M.idx[F,F,0]);B=divide_beta(M.boundary(E));gamma=(B,E)
        check(is_zero_map(hom_d(M,gamma)),'vertex_supported_chain_map',F)
        check(all(M.states[j][0]==F for C in gamma for j,p in C),'vertex_map_actual_support',F)
        check(hom_d(M,(E,{}),-1)==fmap_scale(gamma,beta),'beta_annihilating_homotopy',F)
        xh=(M.occurrence_homotopy(B),M.occurrence_homotopy(E))
        check(hom_d(M,xh,-1)==fmap_scale(gamma,x35),'X35_annihilating_homotopy',F)
        vertices.append(F);gammas.append(gamma);tops.append(E);bottoms.append(B)
    check(sum(len(c) for g in gammas for c in g)==56,'all_vertex_map_entries')

    # Every maximal vertex has a genuine two-row quotient, not an assumed
    # restriction of arbitrary cochains to the complete endpoint subcomplex.
    quotient_data=[]
    for F in vertices:
        lo=M.idx[F,F,0];hi=M.idx[F,F,1]
        for j in range(430):
            v=M.basis(j)
            expected=scale(M.basis(lo),x35,-1) if j==hi else {}
            actual=M.project(M.boundary(v),{lo,hi})
            check(actual==expected,'full_vertex_top_quotient_chain_map',(F,j))
        coeffs=[g[1].get((lo,ZERO),0) for g in gammas]
        check(coeffs==[int(F==Fj) for Fj in vertices],'independent_vertex_detectors',F)
        quotient_data.append({'face':list(F),'lower_state':lo,'upper_state':hi,'differential':'-X35'})

    active=[i for i,F in enumerate(vertices) if '35' not in F]
    neg=vertices.index(tuple(sorted(MINUS)));pos=vertices.index(tuple(sorted(PLUS)))
    E_sum={};B_sum={}
    for i in active:E_sum=add(E_sum,tops[i]);B_sum=add(B_sum,bottoms[i])
    check(beta_coefficient(Z,0)==E_sum,'nine_vertex_leading_cycle')
    U=divide_beta(add(Z,E_sum,-1))
    vertex_sum=(B_sum,E_sum)
    check(M.boundary(U)==add({},B_sum,-1),'normal_form_lower_correction')
    check(fmap_add(D,vertex_sum,-1)==hom_d(M,(U,{}),-1),'complete_vertex_normal_form')
    check(len(U)==36,'normal_form_homotopy_count')
    posocc=M.idx[tuple(sorted(PLUS)),('13','15'),1]
    check(M.project(U,M.V)==M.basis(posocc),'retained_positive_endpoint_homotopy')
    check(M.project(M.boundary(U),M.V)==add({},bottoms[neg],-1),'full_endpoint_boundary_of_homotopy')
    UE=M.project(U,all_ids-M.V);UV=M.project(U,M.V)
    connector=M.project(M.boundary(UE),M.V)
    check(add(connector,M.boundary(UV))==add({},bottoms[neg],-1),'both_endpoint_connector_corrections')
    check(len(connector)==6,'six_endpoint_connector_terms')
    qU={(M.idx[(),(),0],beta_power(2)):1}
    for l in LONG:qU[(M.idx[(l,),(l,),0],beta_power(1))]=-1
    check(M.project(U,M.Q)==qU,'full_Q_comparison_homotopy')
    check(not M.quotient_boundary(qU,M.Q),'Q_homotopy_cycle')
    check(M.project(Z,M.Q)==scale(qU,beta),'Q_difference_is_supported_Hom_boundary')
    check(all(not M.project(c,M.Q) for g in gammas for c in g),'vertex_maps_have_zero_Q')

    # Full occurrence-weight-zero component; beta is NOT truncated.
    coeff={}
    for j,(F,Hm,e) in enumerate(M.states):
        p=[0]*10
        for d in F:p[DPOS[d]]+=1
        for d in Hm:p[DPOS[d]]-=1
        p[DPOS['35']]-=e
        if min(p[:9])>=0 and survives(p):coeff[j]=tuple(p)
    check(Counter(M.deg[j] for j in coeff)=={0:8,1:59,2:108,3:56},'complete_homogeneous_ranks')
    check(not any(M.deg[j]==4 for j in coeff),'no_weight_zero_degree_four')
    def component(mod):
        d={j:{} for j in coeff}
        for j,p in coeff.items():
            for i,q,c in mod.d[j]:
                total=pplus(p,q)
                if not survives(total):continue
                check(i in coeff and total==coeff[i],'entire_homogeneous_component',j)
                put(d[j],i,c)
        return d
    d0=component(M0);d1=component(M1)
    # The entire polynomial Hom complex on this component, with beta unbounded.
    hbasis=[(kind,j) for kind in ('p','e') for j in sorted(coeff)]
    hidx={v:i for i,v in enumerate(hbasis)}
    hdegree={i:(2 if kind=='p' else 3)-M.deg[j] for i,(kind,j) in enumerate(hbasis)}
    hmatrix={i:{} for i in range(len(hbasis))}
    for aidx,(kind,j) in enumerate(hbasis):
        for k,pp,c in M.d[j]:
            total=pplus(coeff[j],pp)
            if not survives(total):continue
            check(k in coeff and total[:9]==coeff[k][:9], 'full_Hom_homogeneous_weight',aidx)
            put(hmatrix[aidx],(hidx[kind,k],total[9]),c)
        if kind=='p':
            put(hmatrix[aidx],(hidx['e',j],1),-((-1)**hdegree[aidx]))
        check(all(hdegree[k]==hdegree[aidx]+1 for k,b in hmatrix[aidx]),'full_Hom_degree',aidx)
    for aidx,col in hmatrix.items():
        square={}
        for (j,b),c in col.items():
            for (k,bb),cc in hmatrix[j].items():put(square,(k,b+bb),c*cc)
        check(not square,'full_polynomial_Hom_d_squared',aidx)
        # Reduction (F(p),F(e)) |-> F(e) mod beta is the purity comparison.
        lhs={}
        for (j,b),c in col.items():
            kind,target=hbasis[j]
            if kind=='e' and b==0:put(lhs,target,c)
        kind,source=hbasis[aidx]
        rhs=d0[source] if kind=='e' else {}
        check(lhs==rhs,'supported_Hom_to_central_cochain_comparison',aidx)
    check(Counter(hdegree.values())=={-1:56,0:164,1:167,2:67,3:8},'full_Hom_ranks')
    def vector(c):
        o={}
        for (j,p),v in c.items():
            check(j in coeff and p==coeff[j],'homogeneous_chain_coordinates',j)
            put(o,j,v)
        return o
    reductions={}
    supports={'full':all_ids,'vertices':M.vertex,'endpoints':M.V,
              'nonendpoint_vertices':M.vertex-M.V,'short_boundary':M.B,
              'Q':M.Q,'endpoint_quotient':all_ids-M.V,
              'short_endpoint_quotient':M.B-M.V}
    for name,ids in supports.items():
        dd={j:{i:c for i,c in col.items() if i in ids} for j,col in d0.items() if j in ids}
        rr=integer_retract(dd,M.deg);reductions[name]=rr
        expected=[M.idx[F,F,0] for F in vertices if M.idx[F,F,0] in ids]
        if name!='Q':
            check([j for j in rr['residual'] if M.deg[j]==3]==expected,'H3_exact_vertex_basis',name)
    check(reductions['full']['homology']=={1:6,2:21,3:14},'full_central_homology')
    check(reductions['endpoint_quotient']['homology']=={1:4,2:17,3:12},'endpoint_quotient_central_homology')
    rg=integer_retract(d1,M.deg)
    check(rg['homology'].get(3)==2,'beta_one_degree_three_homology',rg['homology'])
    h3g=[j for j in rg['residual'] if M.deg[j]==3]
    generic_cols=[int_apply(rg['p'],vector(beta_one(c))) for c in (Psi,Z)]
    gm=[[c.get(j,0) for c in generic_cols] for j in h3g]
    check(abs(gm[0][0]*gm[1][1]-gm[0][1]*gm[1][0])==1,'generic_cycle_basis_unimodular')
    def normal_scale(c):
        o={}
        for (j,p),v in c.items():put(o,(j,pplus(p,beta_power(len(M.states[j][1])))),v)
        return o
    for j in range(430):
        v=M.basis(j)
        check(M1.boundary(normal_scale(v))==normal_scale(M.boundary(v)),'generic_comparison_without_constructed_inverse',j)
    for name,c in [('Psi',Psi),('Z',Z)]:
        check(normal_scale(c)==scale(beta_one(c),beta_power(3)),'weighted_generic_basis_identity',name)
    eneg=M.idx[tuple(sorted(MINUS)),tuple(sorted(MINUS)),0]
    epos=M.idx[tuple(sorted(PLUS)),tuple(sorted(PLUS)),0]
    endpoint_matrix=[[c.get((j,ZERO),0) for c in (Psi,Z)] for j in (eneg,epos)]
    check(endpoint_matrix==[[1,1],[1,0]],'fixed_primary_endpoint_detection_matrix')

    # First Bockstein on ALL fourteen vertex classes.
    rc=reductions['full'];h2=[j for j in rc['residual'] if M.deg[j]==2]
    bcols=[int_apply(rc['p'],vector(B)) for B in bottoms]
    bock=[[col.get(j,0) for col in bcols] for j in h2]
    smith=unit_smith(bock)
    check(smith['rank']==12,'first_Bockstein_rank')
    indicator_no=[int(i in active) for i in range(14)]
    indicator_yes=[1-c for c in indicator_no]
    for v in (indicator_no,indicator_yes):
        check(dense_mul(bock,[[x] for x in v])==[[0] for _ in h2],'first_Bockstein_kernel_vectors')
    check([[v[i] for v in (indicator_no,indicator_yes)] for i in (neg,pos)]==[[1,0],[0,1]],'Bockstein_kernel_primitive_integral_basis')
    check(any(bock[j][neg] for j in range(len(h2))),'negative_endpoint_subtraction_Bockstein_nonzero')

    # Every nonzero Bockstein row is the signed difference on a genuine flip
    # edge. Exactly the flips changing the distinguished 35 mark are absent.
    adjacency={(i,j) for i in range(14) for j in range(i+1,14)
               if len(set(vertices[i])&set(vertices[j]))==2}
    edges=set();edge_rows=[]
    for k,row in enumerate(bock):
        nz=[(i,c) for i,c in enumerate(row) if c]
        if not nz:continue
        check(len(nz)==2 and sorted(c for i,c in nz)==[-1,1],'Bockstein_row_is_oriented_edge',k)
        i,j=sorted(i for i,c in nz)
        check((i,j) in adjacency,'Bockstein_edge_is_actual_flip',k)
        edges.add((i,j));edge_rows.append({'row':k,'vertices':[i,j],'signs':[row[i],row[j]]})
    retained={(i,j) for i,j in adjacency if ('35' in vertices[i])==('35' in vertices[j])}
    check(edges==retained,'exact_distinguished_mark_flip_graph')
    check((len(adjacency),len(edges),len(adjacency-edges))==(21,16,5),'flip_graph_counts')
    unseen=set(range(14));components=[]
    while unseen:
        seed=min(unseen);seen={seed};todo=[seed]
        while todo:
            i=todo.pop()
            for a,b in edges:
                j=b if a==i else (a if b==i else None)
                if j is not None and j not in seen:seen.add(j);todo.append(j)
        unseen-=seen;components.append(sorted(seen))
    check(sorted(map(len,components))==[5,9],'two_Bockstein_graph_components')
    check({frozenset(c) for c in components}=={frozenset(active),frozenset(set(range(14))-set(active))},'components_classified_by_occurrence_mark')

    individual_normal_forms={}
    for name,f in [('F03',f03),('Fmu',fmu)]:
        central=beta_coefficient(f[1],0)
        cc=[central.get((M.idx[F,F,0],ZERO),0) for F in vertices]
        norm=({},{} )
        for c,g in zip(cc,gammas):norm=fmap_add(norm,g,c)
        uu=divide_beta(add(f[1],norm[1],-1))
        check(fmap_add(f,norm,-1)==hom_d(M,(uu,{}),-1),'complete_individual_map_normal_form',name)
        individual_normal_forms[name]={'coefficients':cc,'homotopy':uu,'map':norm}
    ch=individual_normal_forms['F03']['coefficients'];cg=individual_normal_forms['Fmu']['coefficients']
    check([g-h for g,h in zip(cg,ch)]==indicator_no,'pair_class_difference_is_nine_vertex_indicator')
    check(dense_mul(bock,[[x] for x in ch])==dense_mul(bock,[[x] for x in cg]),'two_maps_have_same_primary_Bockstein')
    check(add(individual_normal_forms['Fmu']['homotopy'],individual_normal_forms['F03']['homotopy'],-1)==U,'pair_normal_form_homotopy_difference')

    # The canonical nonendpoint representative belongs to an explicit quotient
    # of the source-target problem. It is not a homotopy removing the endpoint
    # component of the original full-target map.
    mixed_active=[i for i in active if i!=neg]
    mix=({},{} )
    for i in mixed_active:mix=fmap_add(mix,gammas[i])
    check(len(mixed_active)==8,'eight_nonendpoint_vertex_components')
    check(all(not M.project(c,M.V) and not M.project(c,M.Q) for c in mix),'strict_nonendpoint_vertex_representative')
    check(is_zero_map(hom_d(M,mix)),'nonendpoint_vertex_sum_chain_map')
    projectE=lambda f:tuple(M.project(c,all_ids-M.V) for c in f)
    check(projectE(fmap_add(D,mix,-1))==projectE(hom_d(M,(U,{}),-1)),'endpoint_quotient_normal_form')
    # beta*Z still has eight nonzero vertex-top obstruction coordinates after
    # both physical endpoints are quotiented away.
    obstruction=[]
    for i in mixed_active:
        F=vertices[i];lo=M.idx[F,F,0]
        observed={(j,p):c for (j,p),c in scale(Z,beta).items() if j==lo}
        check(observed=={(lo,beta):1},'nonendpoint_two_normal_obstruction',F)
        # Every degree-four incoming column to the chosen row is -X35 times
        # its occurrence partner, already verified for all source columns.
        check(beta[POS['X35']]==0 and beta[POS['beta']]==1,'first_infinitesimal_obstruction_survives',F)
        obstruction.append({'face':list(F),'equation':'-X35*y = beta','test_quotient':'(X35,beta^2)','nonzero_rhs':'beta'})

    # Polynomial normal-form examples in arbitrarily selected beta degrees are
    # controls only; completeness follows from the exact central kernel and
    # the displayed factorization argument in the proof.
    for j in [j for j in coeff if M.deg[j]==3]:
        Utest={(j,pplus(coeff[j],beta_power(5))):1}
        f=hom_d(M,(Utest,{}),-1)
        check(is_zero_map(hom_d(M,f)),'unbounded_formula_homotopy_control',j)
        check(not beta_coefficient(f[1],0),'normal_form_boundary_readout_zero',j)

    body={
      'schema':'marici.branch_a.regulator_supported_vertex_decomposition.v1',
      'date':'2026-09-07',
      'coefficient_ring':'Z[beta,X02,X03,X04,X13,X14,X15,X24,X25,X35]/(X_even*X_odd)',
      'scope':'unit-normalized regulator coefficient family; no assertion of beta=0 geometric purity',
      'variables':list(VARS),'repository_commit':REPOSITORY_COMMIT,
      'support_counts':{'full':430,'endpoints':32,'short_boundary':416,'Q':14},
      'state_basis':[{'index':j,'face':list(F),'marks':list(Hm),'occurrence_partner':e,'degree':M.deg[j]} for j,(F,Hm,e) in enumerate(M.states)],
      'family_differential':[[j,i,c,list(p)] for j,col in M.d.items() for i,p,c in col],
      'vertex_faces':[list(F) for F in vertices],
      'vertex_supported_maps':[map_json(g,M) for g in gammas],
      'vertex_top_quotients':quotient_data,
      'cyclic_submodule':{'rank':14,'each_annihilator':['beta','X35'],'split_at_H0':True,'entire_full_ring_H0_classified':False},
      'packet':{name:chain_json(c,M) for name,c in [('A_beta',A),('H_beta',H),('G_beta',G),('Z_beta',Z),('Psi_beta',Psi),('normal_form_homotopy_U',U)]},
      'difference_vertex_coordinates':indicator_no,
      'normal_form':{'equation':'(0,Z_beta) - sum_{35 not in F} Gamma_F = delta(U,0)','U_terms':len(U),'retains_primary_pointwise':False},
      'normal_form_endpoint_terms':chain_json(UV,M),
      'normal_form_endpoint_connector':chain_json(connector,M),
      'normal_form_Q_terms':chain_json(qU,M),
      'central_homogeneous_coefficient_monomials':[[j,list(p)] for j,p in sorted(coeff.items())],
      'central_homogeneous_differential':intmat_json(d0),
      'homogeneous_supported_Hom_basis':[{'index':i,'source_generator':kind,'target_state':j,'cohomological_degree':hdegree[i]} for i,(kind,j) in enumerate(hbasis)],
      'homogeneous_supported_Hom_differential':[[j,i,c,b] for j,col in sorted(hmatrix.items()) for (i,b),c in sorted(col.items())],
      'central_support_reductions':{name:retract_json(r) for name,r in reductions.items()},
      'beta_one_reduction':retract_json(rg),
      'fixed_primary_cycle_module':{'basis':['Psi_beta','Z_beta'],'ring':'Z[beta]','endpoint_top_matrix':endpoint_matrix,'endpoint_zero_kernel':0},
      'homogeneous_supported_comparison_H0_rank':14,
      'homogeneous_endpoint_quotient_comparison_H0_rank':12,
      'first_Bockstein':{'target_residual_states':h2,'matrix':bock,'unit_smith':smith,'kernel_basis':[indicator_no,indicator_yes],'rank':12},
      'Bockstein_flip_graph':{'all_edges':[list(e) for e in sorted(adjacency)],'retained_edges':[list(e) for e in sorted(edges)],'omitted_edges':[list(e) for e in sorted(adjacency-edges)],'components':components,'oriented_rows':edge_rows},
      'individual_supported_map_normal_forms':{name:{'coefficients':d['coefficients'],'homotopy':chain_json(d['homotopy'],M),'map':map_json(d['map'],M)} for name,d in individual_normal_forms.items()},
      'endpoint_quotient_difference_vertex_faces':[list(vertices[i]) for i in mixed_active],
      'endpoint_quotient_difference_representative':map_json(mix,M),
      'two_normal_obstructions_after_endpoint_quotient':obstruction,
      'physical_Delta_J_identified':False,
      'check_counts':dict(sorted(COUNTS.items())),
      'exact_checks':sum(COUNTS.values()),
    }
    canonical=json.dumps(body,sort_keys=True,separators=(',',':')).encode()
    body['content_sha256']=sha256(canonical).hexdigest()
    output=Path(output);output.write_text(json.dumps(body,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'certificate':output.name,'exact_checks':body['exact_checks'],'H0_supported_weight_zero':14,
                      'fixed_primary_rank':2,'endpoint_relative_H0':12,'difference_mixed_coordinates':8,
                      'Bockstein_rank':12,'content_sha256':body['content_sha256']},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',default='branch_a_regulator_supported_vertex_decomposition_certificate.json')
    args=parser.parse_args();main(args.output)
