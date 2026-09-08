#!/usr/bin/env python3
"""First-conductor-degree endpoint/Q-fixed deformations in the full regulator family.

Self-contained, Python standard library only. No companion input files are read.
Reconstructs the 430-state differential over
 Z[beta,X02,X03,X04,X13,X14,X15,X24,X25,X35]/(X_even X_odd).
Computes entire occurrence components over Z[beta], rather than beta truncations.
The proof of the unbounded negative-sheet sector uses the explicit component
stabilization and polynomial basis described in the accompanying proof file.
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



def component(M, weight):
    """Return the full fine-occurrence component, with arbitrary beta powers."""
    if len(weight)!=9: raise ValueError('Expected nine occurrence weights')
    coeff={}
    for j,(F,H,e) in enumerate(M.states):
        p=list(weight)+[0]
        for a in F:p[DPOS[a]]+=1
        for a in H:p[DPOS[a]]-=1
        p[DPOS['35']]-=e
        if min(p[:9])>=0 and survives(p):coeff[j]=tuple(p)
    d={j:{} for j in coeff}
    for j,p in coeff.items():
        for i,q,c in M.d[j]:
            total=pplus(p,q)
            if not survives(total): continue
            check(i in coeff and total[:9]==coeff[i][:9], 'component_closed_under_d',j)
            put(d[j],(i,total[9]),c)
    return coeff,d


def polynomial_apply(matrix, vector):
    out={}
    for (j,k),c in vector.items():
        for (i,l),v in matrix[j].items():put(out,(i,k+l),c*v)
    return out


def at_beta(matrix,value):
    out={j:{} for j in matrix}
    for j,col in matrix.items():
        for (i,k),c in col.items():put(out[j],i,c*value**k)
    return out


def endpoint_zero_complex(M, coeff, d):
    """K consists of chains with zero endpoint component and zero endpoint boundary.

    Each incoming endpoint column has at most one endpoint row, with coefficient
    +/-1 in a homogeneous component. Hence an explicit saturated kernel basis
    suffices; no rational nullspace algorithm is used.
    """
    E=set(coeff)-M.V
    alpha_rows={}
    for j in sorted(E):
        terms=[(i,k,c) for (i,k),c in d[j].items() if i in M.V]
        check(len(terms)<=1,'endpoint_column_at_most_one_row',j)
        for i,k,c in terms:
            check(k==0 and abs(c)==1,'endpoint_kernel_integral_unit',j)
            alpha_rows.setdefault(i,{})[j]=c
    pivots={min(col) for col in alpha_rows.values()}
    inc={j:{j:1} for j in sorted(E-pivots)}
    for row,col in alpha_rows.items():
        p=min(col);unit=col[p]
        for j,c in col.items():
            if j!=p:inc[j][p]=-unit*c
    kd={j:{} for j in inc}
    for j,col in inc.items():
        out={}
        for a,c in col.items():
            for (i,k),v in d[a].items():put(out,(i,k),c*v)
        check(all(i in E for i,k in out),'kernel_d_has_zero_endpoint',j)
        for (i,k),c in out.items():
            if i in inc:put(kd[j],(i,k),c)
        back={}
        for (i,k),c in kd[j].items():
            for a,v in inc[i].items():put(back,(a,k),c*v)
        check(out==back,'kernel_d_reconstructs_full_boundary',j)
    for j in kd:
        check(not polynomial_apply(kd,kd[j]),'kernel_polynomial_d_squared',j)
    return kd,inc,alpha_rows


def flatten_int_matrix(m):
    return [[j,i,c] for j,col in sorted(m.items()) for i,c in sorted(col.items())]


def flatten_beta_matrix(m):
    return [[j,i,c,k] for j,col in sorted(m.items()) for (i,k),c in sorted(col.items())]


def chain_json(chain,M):
    return [{'state':j,'face':list(M.states[j][0]),'marks':list(M.states[j][1]),
             'occurrence_partner':M.states[j][2],'degree':M.deg[j],
             'coefficient':c,'exponents':list(p)} for (j,p),c in sorted(chain.items())]


def retract_json(red):
    return {'homology':red['homology'],'residual':red['residual'],
            'unit_pivots':red['pivots'],'projection':flatten_int_matrix(red['p']),
            'inclusion':flatten_int_matrix(red['i']), 'homotopy':flatten_int_matrix(red['h'])}


def map_json(f,M):return {'p':chain_json(f[0],M),'e':chain_json(f[1],M)}


def factor_occurrence(chain,name):
    k=POS[name];out={}
    for (j,p),c in chain.items():
        check(p[k]>0,'displayed_occurrence_factor_exists',(name,j))
        q=list(p);q[k]-=1;put(out,(j,tuple(q)),c)
    check(scale(out,mono(name))==chain,'displayed_occurrence_factor_reconstructs',name)
    return out


def normal_rescale(chain,M):
    """Polynomial comparison C_beta -> C_1; no beta inverse is computed."""
    return {(j,pplus(p,beta_power(len(M.states[j][1])))):c
            for (j,p),c in chain.items()}


def main(output):
    M=Model('family');M1=Model('one')
    all_ids=set(range(430));beta=mono('beta');x=mono('X02');x35=mono('X35')
    for j in range(430):
        base=M.basis(j)
        check(M1.boundary(normal_rescale(base,M))==normal_rescale(M.boundary(base),M),
              'polynomial_normal_rescaling_chain_identity',j)
        check(add(M.boundary(M.occurrence_homotopy(base)),
                  M.occurrence_homotopy(M.boundary(base)))==scale(base,x35),
              'full_occurrence_multiplication_homotopy',j)
        check(all(k[9]+len(M.states[i][1])==len(M.states[j][1]) for i,k,c in M.d[j]),
              'regulator_normal_grade_preserved_by_differential',j)

    # Reproduce the previous weight-zero restriction without reusing its verdict.
    c0,d0=component(M,(0,)*9)
    k0,i0,a0=endpoint_zero_complex(M,c0,d0)
    r0=integer_retract(at_beta(k0,1),M.deg)
    check(not any(M.deg[j]==4 for j in c0),'zero_weight_no_degree_four')
    check(not any(M.deg[j]==3 for j in r0['residual']),
          'zero_weight_endpoint_zero_generic_cycle_kernel_zero')

    w=(1,0,0,0,0,0,0,0,0)
    coeff,d=component(M,w)
    kd,inc,alpha=endpoint_zero_complex(M,coeff,d)
    red=integer_retract(at_beta(kd,1),M.deg)
    check(red['homology']=={3:9},'complete_negative_component_generic_homology')
    check(Counter(M.deg[j] for j in coeff)=={0:4,1:29,2:69,3:56},
          'full_X02_component_ranks')
    check(Counter(M.deg[j] for j in kd)=={0:3,1:25,2:63,3:50},
          'endpoint_zero_X02_component_ranks')
    check(not any(M.deg[j]==4 for j in coeff),'negative_component_no_degree_four')

    pivots=[j for j in red['residual'] if M.deg[j]==3]
    cycles=[];precycles=[];generic_vectors=[];native_degrees=[]
    for j in pivots:
        vector=int_apply(inc,red['i'][j])
        N=max(len(M.states[a][1]) for a in vector)
        cycle={(a,pplus(coeff[a],beta_power(N-len(M.states[a][1])))):c
               for a,c in vector.items()}
        check(not M.boundary(cycle),'full_polynomial_cycle_equation',j)
        check(not M.project(cycle,M.V),'cycle_endpoints_strictly_zero',j)
        check(not M.project(cycle,M.Q),'cycle_Q_strictly_zero',j)
        check(all(a in M.B-M.V for a,p in cycle),'cycle_in_actual_short_support',j)
        check(not M.project(M.boundary(M.project(cycle,all_ids-M.V)),M.V),
              'actual_endpoint_connector_of_cycle_zero',j)
        check(all(coeff[a][:9]==mono('X02')[:9] for a in vector),
              'cycle_uniform_conductor_coefficient',j)
        pre=factor_occurrence(cycle,'X02')
        check(all(p[:9]==(0,)*9 for a,p in pre),'precycle_has_no_occurrence_coefficient',j)
        check(all(any(p[DPOS[a]] for a in PLUS) for state,p in M.boundary(pre)),
              'precycle_boundary_in_positive_sheet_ideal',j)
        for neg in sorted(MINUS):
            check(not M.boundary(scale(pre,mono('X'+neg))),
                  'cycle_for_each_negative_conductor_coordinate',(j,neg))
        check(normal_rescale(cycle,M)==scale(beta_one(cycle),beta_power(N)),
              'generic_lift_polynomial_basis_identity',j)
        cycles.append(cycle);precycles.append(pre);generic_vectors.append(vector);native_degrees.append(N)
    pivot_matrix=[[C.get((j,x),0) for C in cycles] for j in pivots]
    check(pivot_matrix==[[int(i==j) for j in range(9)] for i in range(9)],
          'nine_cycle_polynomial_coordinate_matrix_identity')
    check(sum(map(len,cycles))==34,'complete_basis_term_count')

    # Every nonnegative occurrence weight supported positively on the negative
    # sheet has the same complex. Exhaust all seven negative support patterns
    # and all eight long-variable support patterns. The formula for exponents
    # proves stability for higher powers; no degree truncation is being used.
    negative=tuple(sorted(MINUS));long=tuple(LONG)
    stabilization=[]
    for nmask in range(1,8):
        for lmask in range(8):
            ww=[0]*9
            for i,a in enumerate(negative):ww[DPOS[a]]=(nmask>>i)&1
            for i,a in enumerate(long):ww[DPOS[a]]=(lmask>>i)&1
            cc,dd=component(M,tuple(ww))
            check(set(cc)==set(coeff),'all_negative_sector_state_patterns_identical',(nmask,lmask))
            check(dd==d,'all_negative_sector_differentials_identical',(nmask,lmask))
            stabilization.append({'weight':ww,'active_states':len(cc)})
    high=[0]*9
    for a,power in [('02',7),('04',2),('24',5),('03',4),('14',3),('25',9)]:high[DPOS[a]]=power
    ch,dh=component(M,tuple(high))
    check(set(ch)==set(coeff) and dh==d,'high_power_stabilization_control_not_completeness_proof')

    # Distinguished two-term central-flip cycle; both cells occur in the
    # actual D03 first-flip gallery, no synthetic support state is introduced.
    face=('03','13','35');edge=('13','35')
    ft=M.idx[face,face,0];eg=M.idx[edge,edge,0]
    U={(ft,ZERO):1,(eg,beta):-1};Y=scale(U,x)
    sample_index=next(i for i,C in enumerate(cycles) if C==Y)
    check(len(Y)==2 and not M.boundary(Y),'distinguished_two_term_cycle')
    check(not M.project(Y,M.V) and not M.project(Y,M.Q),'distinguished_full_frame_zero')
    check(len(M.boundary(U))==5,'five_unmultiplied_defect_terms')
    for pos in sorted(PLUS):
        check(not scale(Y,mono('X'+pos)),'sample_positive_sheet_annihilator',pos)

    # A genuine quotient onto the native maximal top and its independent
    # occurrence partner detects the state cycle and the supported map class.
    ft4=M.idx[face,face,1]
    for j in range(430):
        lhs=M.project(M.boundary(M.basis(j)),{ft,ft4})
        rhs=scale(M.basis(ft),x35,-1) if j==ft4 else {}
        check(lhs==rhs,'complete_nonendpoint_vertex_quotient_chain_map',j)
    check(M.project(Y,{ft,ft4})=={(ft,x):1},'primitive_state_detector_X02')
    supported=({},Y)
    check(is_zero_map(hom_d(M,supported)),'distinguished_supported_map_closed')
    check(hom_d(M,(Y,{}),-1)==fmap_scale(supported,beta),
          'supported_beta_annihilator_explicit_homotopy')

    # Verify the monomial ideal descriptions against every occurrence support
    # and beta present/absent. The proof uses the normal form in the two-sheet
    # ring, so arbitrary powers follow from the same support conditions.
    for mask in range(1<<9):
        p=tuple((mask>>i)&1 for i in range(9))+(0,)
        if not survives(p):continue
        for bk in (0,1):
            q=p[:9]+(bk,)
            image=scale(Y,q)
            pos=any(p[DPOS[a]] for a in PLUS)
            check((not image)==pos,'full_state_annihilator_support_audit',(mask,bk))
            det=M.project(image,{ft,ft4})
            det_mod={key:c for key,c in det.items()
                     if key[1][POS['X35']]==0 and key[1][POS['beta']]==0}
            check((not det_mod)==(pos or bk>0),'supported_annihilator_support_audit',(mask,bk))

    # Replay the recorded primary and first primitive from labelled chains.
    H={(M.idx[F,Hm,e],beta_power(k)):c for F,Hm,e,k,c in H_INPUT}
    A=divide_beta(M.boundary(H))
    reference=(scale(A,x),scale(H,x))
    check(bool(reference[0]),'reference_primary_is_nonzero')
    check(is_zero_map(hom_d(M,reference)),'reference_supported_map_chain_equation')
    modifications=[]
    for i,C in enumerate(cycles):
        difference=({},C);modified=fmap_add(reference,difference)
        check(is_zero_map(hom_d(M,modified)),'same_primary_modification_is_chain_map',i)
        check(modified[0]==reference[0],'same_primary_is_literal',i)
        for ids,name in [(M.V,'endpoint'),(M.Q,'Q')]:
            check(tuple(M.project(a,ids) for a in modified)==tuple(M.project(a,ids) for a in reference),
                  'full_'+name+'_components_identical',i)
        check(hom_d(M,(C,{}),-1)==fmap_scale(difference,beta),
              'all_nine_supported_beta_primitives',i)
        modifications.append(modified)

    # Retain the original packet's regulator-normal grade: |h_native|=1,
    # |beta|=1, |h_occurrence|=0; the source p,e have grades 2,3.
    def reggrade(chain):
        grades={p[9]+len(M.states[j][1]) for j,p in chain}
        if len(grades)>1:raise AssertionError('Inhomogeneous regulator-normal grade')
        return next(iter(grades)) if grades else None
    check(reggrade(reference[0])==2 and reggrade(reference[1])==3,
          'recorded_source_packet_regulator_grades')
    grade3_cycles=[];grade3_maps=[];grade3_boundaries=[]
    primitive_grade3=[]
    for i,C in enumerate(cycles):
        check(reggrade(C)==native_degrees[i], 'cycle_regulator_degree',i)
        CG=scale(C,beta_power(3-native_degrees[i]))
        grade3_cycles.append(CG)
        FG=fmap_add(reference,({},CG));grade3_maps.append(FG)
        check(reggrade(FG[0])==2 and reggrade(FG[1])==3,
              'all_modified_maps_keep_packet_regulator_grades',i)
        check(is_zero_map(hom_d(M,FG)), 'graded_modified_map_chain_equation',i)
        if native_degrees[i]==2:
            check(hom_d(M,(C,{}),-1)==({},CG), 'three_graded_ordinary_homotopy_boundaries',i)
            grade3_boundaries.append(i)
        elif native_degrees[i]==3: primitive_grade3.append(i)
        else:raise AssertionError('Unexpected regulator grade')
    check((len(primitive_grade3),len(grade3_boundaries))==(6,3),
          'fixed_regulator_grade_nonzero_supported_classes_six')
    for i in primitive_grade3:
        F,Hm,e=M.states[pivots[i]]
        check(len(F)==3 and Hm==F and e==0, 'six_native_top_class_detectors',i)
        for j,C in enumerate(grade3_cycles):
            value=beta_coefficient(C,0).get((pivots[i],x),0)
            check(value==int(i==j),'six_graded_supported_classes_independent',(i,j))

    # Negative first-conductor symbols remain as 27 independent cycle
    # coordinates before ordinary supported-map homotopies. At the regulator
    # grade of the original packet, eighteen supported classes remain.
    first_symbols=[]
    for a in negative:
        for i,U0 in enumerate(precycles):
            C=scale(U0,mono('X'+a))
            check(not M.boundary(C),'all_twenty_seven_first_degree_cycles',(a,i))
            read=[C.get((j,mono('X'+a)),0) for j in pivots]
            check(read==[int(k==i) for k in range(9)],'first_symbol_coordinate_matrix',(a,i))
            first_symbols.append({'negative_normal':a,'basis_index':i,
                                  'pivot_state':pivots[i],'top_coefficient':1})

    # The independent occurrence partner is retained, including its beta factor.
    relations=[]
    for native in (284,316,428):
        i=pivots.index(native);occ=native-5;j=pivots.index(occ)
        check(M.replace_native35(cycles[i])==scale(cycles[j],beta),
              'native_occurrence_replacement_keeps_beta',native)
        relations.append({'native_basis':i,'occurrence_basis':j,'factor':'beta'})

    # Exact normal form for arbitrary polynomial cycle coefficients. These
    # checks are controls; completeness is certified by the generic integral
    # reduction and the identity coordinate minor above.
    test={}
    for i,C in enumerate(cycles):test=add(test,scale(C,beta_power(i+2)),(-1)**i)
    check(not M.boundary(test),'high_beta_polynomial_cycle_control')
    recovered={}
    for i,j in enumerate(pivots):
        for (state,p),c in test.items():
            if state==j:
                check(p[:9]==x[:9],'coordinate_control_occurrence_weight')
                recovered=add(recovered,scale(cycles[i],beta_power(p[9])),c)
    check(recovered==test,'polynomial_coordinate_reconstruction_control')

    body={
      'schema':'marici.branch_a.first_conductor_degree_framed_deformations.v1',
      'date':'2026-09-07','repository_commit':REPOSITORY_COMMIT,
      'coefficient_ring':'Z[beta,X02,X03,X04,X13,X14,X15,X24,X25,X35]/(X_even*X_odd)',
      'scope':'unit-normalized coefficient family; negative-sheet nonnegative occurrence cone; no geometric beta=0 purity theorem',
      'variables':list(VARS),
      'state_basis':[{'index':j,'face':list(F),'marks':list(Hm),'occurrence_partner':e,'degree':M.deg[j]}
                     for j,(F,Hm,e) in enumerate(M.states)],
      'full_differential':[[j,i,c,list(p)] for j,col in M.d.items() for i,p,c in col],
      'support_counts':{'full':430,'endpoints':32,'short_boundary':416,'Q':14},
      'weight_zero':{'kernel_ranks':dict(Counter(M.deg[j] for j in k0)),
                     'beta_one_homology':r0['homology'],'polynomial_degree_three_cycle_kernel':0},
      'first_negative_weight':{'weight':list(w),'component_ranks':dict(Counter(M.deg[j] for j in coeff)),
                              'kernel_ranks':dict(Counter(M.deg[j] for j in kd)),
                              'coefficient_monomials':[[j,list(p)] for j,p in sorted(coeff.items())],
                              'component_differential':flatten_beta_matrix(d),
                              'endpoint_kernel_inclusion':flatten_int_matrix(inc),
                              'endpoint_attachment_rows':[[i,j,c] for i,col in sorted(alpha.items()) for j,c in sorted(col.items())],
                              'endpoint_kernel_differential':flatten_beta_matrix(kd),
                              'integral_generic_reduction':retract_json(red)},
      'polynomial_cycle_basis':[chain_json(C,M) for C in cycles],
      'coefficient_free_precycles':[chain_json(U0,M) for U0 in precycles],
      'precycle_boundaries':[chain_json(M.boundary(U0),M) for U0 in precycles],
      'basis_native_degrees':native_degrees,'coordinate_rows':pivots,'coordinate_matrix':pivot_matrix,
      'negative_sector_stabilization_cases':stabilization,
      'negative_sector_cycle_module':'I_minus^9 over Z[beta,X02,X04,X24,X03,X14,X25]',
      'negative_sector_state_boundaries_degree_four':0,
      'original_packet_regulator_frame':{'primary_grade':2,'primitive_grade':3,
                'grade_three_cycle_basis':[chain_json(C,M) for C in grade3_cycles],
                'ordinary_homotopy_boundary_indices':grade3_boundaries,
                'primitive_supported_class_indices':primitive_grade3,
                'fixed_occurrence_class_rank':6,'all_negative_first_conductor_class_rank':18,
                'strict_primary_homotopy_fixed_pointwise_may_retain_three_extra_classes':True},
      'negative_sector_supported_difference_classes':'(I_minus/beta*I_minus)^9',
      'distinguished_sample':{'basis_index':sample_index,'cycle':chain_json(Y,M),
                              'unmultiplied_defect':chain_json(M.boundary(U),M),
                              'state_annihilator':['X13','X15','X35'],
                              'supported_map_annihilator':['beta','X13','X15','X35'],
                              'vertex_quotient_states':[ft,ft4],'vertex_quotient_differential':'-X35',
                              'projected_Hom_differentials':[['-X35','-beta'],['beta','-X35']]},
      'same_primary_example':{'reference':map_json(reference,M),
                              'modified':map_json(modifications[sample_index],M),
                              'difference':map_json(supported,M),
                              'primary_chain_identical':True,'endpoint_components_identical':True,
                              'complete_Q_components_identical':True,
                              'short_boundary_filling_pointwise_identical':False},
      'first_conductor_symbol_coordinates':first_symbols,
      'native_occurrence_replacement_relations':relations,
      'physical_Delta_J_identified':False,
      'check_counts':dict(sorted(COUNTS.items())), 'exact_checks':sum(COUNTS.values()),
    }
    canonical=json.dumps(body,sort_keys=True,separators=(',',':')).encode()
    body['content_sha256']=sha256(canonical).hexdigest()
    output=Path(output)
    output.write_text(json.dumps(body,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps({'certificate':output.name,'exact_checks':body['exact_checks'],
                      'zero_weight_endpoint_fixed_cycles':0,'negative_first_weight_basis_rank':9,
                      'negative_first_conductor_symbols':27,
                      'regulator_grade_preserving_nonzero_supported_classes':6,
                      'sample_supported_annihilator':body['distinguished_sample']['supported_map_annihilator'],
                      'content_sha256':body['content_sha256']},indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',default='branch_a_first_conductor_degree_framed_deformations_certificate.json')
    args=parser.parse_args()
    main(args.output)
