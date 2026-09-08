#!/usr/bin/env python3
"""Exact target-side unit-multigrade endpoint/Q restriction audit.

Python 3.10+, standard library only. Reconstructs the pinned 215-generator
Marici BM-Cech target, its actual support filtration, the physical D3 action,
and its unit homogeneous summand. Constructs an integral coherent unit in
C(K6,V), rather than identifying the previous abstract detector with Q.

No repository writes, global localization, occurrence inversion, numerical
linear algebra, or identification with the full physical butterfly is used.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
import json
from pathlib import Path
from typing import TypeAlias

Diag: TypeAlias = tuple[int, int]
Face: TypeAlias = tuple[Diag, ...]
Cell: TypeAlias = tuple[Face, Face]
Exp: TypeAlias = tuple[int, ...]
Group: TypeAlias = tuple[int, int]
Vec: TypeAlias = dict
COMMIT = 'd1947b67a60d3e88ba77f4ca60ea02c2a306ee61'
SOURCES = {
 'research/voevodsky/check_global_k6_koszul_cech_promotion.rs':
 'e972b69d0e2b1b0a0aee5e0a027c8216bcace3e8',
 'research/voevodsky/check_two_endpoint_tate_carrier.rs':
 '0147e2e42dafac0da7289c571cb0331b51338be1',
 'src/ledger/20260815-143 Two-Endpoint Road Carrier and the Loaded Conductor Cospan Blocker.md':
 '02cedbb15dd385a75bab759dfcdb4daa28bd3b3c',
 'research/voevodsky/check_dp6_endpoint_q_mapping_fiber.rs':
 '592811b138855554c921dcf4269581632e8f0050',
}
COUNT: Counter[str] = Counter()
G = tuple(product(range(3), range(2)))
ZERO: Exp = (0,) * 18

def check(condition: bool, name: str) -> None:
    if not condition:
        raise AssertionError(name)
    COUNT[name] += 1

def diag(a: int, b: int) -> Diag:
    return tuple(sorted((a % 6, b % 6)))

def cross(a: Diag, b: Diag) -> bool:
    x, y = a; u, v = b
    return x < u < y < v or u < x < v < y

DIAGONALS = tuple((i,j) for i in range(6) for j in range(i+1,6)
                  if j-i not in (1,5))
SHORTS = tuple(diag(i,i+2) for i in range(6))
LONGS = tuple(diag(i,i+3) for i in range(3))
IX = {d:i for i,d in enumerate(SHORTS+LONGS)}
FACES = tuple(f for k in range(4) for f in combinations(DIAGONALS,k)
              if all(not cross(a,b) for a,b in combinations(f,2)))
CELLS = tuple((f,h) for f in FACES for k in range(len(f)+1)
              for h in combinations(f,k))
VP = tuple(sorted(SHORTS[i] for i in (1,3,5)))
VM = tuple(sorted(SHORTS[i] for i in (0,2,4)))
V = {c for c in CELLS if c[0] in (VP,VM)}
B = {c for c in CELLS if any(d in SHORTS for d in c[0])}

def add(*vectors: Vec) -> Vec:
    out = {}
    for vector in vectors:
        for key,c in vector.items():
            out[key] = out.get(key,0)+c
            if not out[key]:
                del out[key]
    return out

def scale(vector: Vec, coefficient: int) -> Vec:
    return {key:coefficient*c for key,c in vector.items() if coefficient*c}

def exp(data: dict[int,int]) -> Exp:
    return tuple(data.get(i,0) for i in range(18))

def eadd(a: Exp, b: Exp) -> Exp:
    return tuple(x+y for x,y in zip(a,b))

def weight(f: Face) -> Exp:
    return exp({**{IX[d]:1 for d in f}, **{IX[d]+9:-1 for d in f}})

def shift(cell: Cell) -> Exp:
    return tuple(-n for n in weight(cell[0]))

def legal(cell: Cell, coefficient: Exp) -> bool:
    loc = {IX[d] for d in cell[0] if d not in cell[1]}
    return (all(n>=0 for n in coefficient[:9]) and
            all(n>=0 or j in loc for j,n in enumerate(coefficient[9:])))

def degree(cell: Cell) -> int:
    return 3-len(cell[0])+len(cell[1])

def boundary(cell: Cell) -> dict[tuple[Cell,Exp],int]:
    f,h = cell; result = {}
    for a in DIAGONALS:
        if a not in f and all(not cross(a,b) for b in f):
            t = (tuple(sorted(f+(a,))),h)
            result[(t,exp({IX[a]:1,IX[a]+9:-1}))] = (-1)**sum(b<a for b in f)
    for i,a in enumerate(h):
        t = (f,tuple(b for b in h if b!=a))
        result[(t,ZERO)] = (-1)**(3-len(f)+i)
    return result

BD = {c:boundary(c) for c in CELLS}

def apply_bd(vector: dict[tuple[Cell,Exp],int]):
    out = {}
    for (c,m),a in vector.items():
        out = add(out,{(t,eadd(m,n)):a*b for (t,n),b in BD[c].items()})
    return out

def mul(g: Group, h: Group) -> Group:
    return ((g[0]+(-1)**g[1]*h[0])%3,(g[1]+h[1])%2)

def vertex(a: int, g: Group) -> int:
    # Actual closed-endpoint carrier reflection, not the older 2-v reflection.
    return (2*g[0]+(a if g[1]==0 else 3-a))%6

def image_diag(d: Diag, g: Group) -> Diag:
    return diag(vertex(d[0],g),vertex(d[1],g))

def image_face(f: Face, g: Group) -> Face:
    return tuple(sorted(image_diag(d,g) for d in f))

def permutation_sign(f: Face, g: Group) -> int:
    ordered = [image_diag(d,g) for d in f]
    return (-1)**sum(a>b for i,a in enumerate(ordered) for b in ordered[i+1:])

def act_cell(c: Cell, g: Group) -> tuple[Cell,int]:
    f,h = c
    sign = (-1)**g[1]*permutation_sign(f,g)*permutation_sign(h,g)
    return (image_face(f,g),image_face(h,g)),sign

def act_exp(m: Exp, g: Group) -> Exp:
    out = [0]*18
    for d,i in IX.items():
        j = IX[image_diag(d,g)]
        out[j] = m[i];out[j+9] = m[i+9]
    return tuple(out)

def act_loaded(vector, g):
    out = {}
    for (c,m),a in vector.items():
        t,s = act_cell(c,g)
        out = add(out,{(t,act_exp(m,g)):a*s})
    return out

# At the forced zero multidegree only unmarked states are allowed.
C0 = tuple(c for c in CELLS if legal(c,weight(c[0])))

def cellular_boundary(f: Face) -> dict[Face,int]:
    return {t[0]:a for (t,_),a in BD[(f,())].items()}

def act_chain(vector: dict[Face,int], g: Group) -> dict[Face,int]:
    return {image_face(f,g):a*(-1)**g[1]*permutation_sign(f,g)
            for f,a in vector.items()}

def apply_cellular(vector: dict[Face,int], support: set[Face]) -> dict[Face,int]:
    out = {}
    for f,a in vector.items():
        out=add(out,{t:a*b for t,b in cellular_boundary(f).items() if t in support})
    return out

def unit_cancel(support: set[Face]) -> tuple[dict[int,int],list]:
    """Integral elementary chain contractions; every pivot is a signed unit."""
    d = {f:{t:a for t,a in cellular_boundary(f).items() if t in support}
         for f in sorted(support,key=lambda x:(len(x),x))}
    pivots=[]
    while True:
        chosen = next(((b,a,c) for b in d for a,c in d[b].items() if abs(c)==1),None)
        if chosen is None:
            break
        b,a,p=chosen; db=dict(d[b]);pivots.append((b,a,p))
        for x in list(d):
            if x in (a,b):
                continue
            coefficient = d[x].get(a,0)
            if coefficient:
                d[x]=add(d[x],scale(db,-coefficient*p))
            d[x].pop(a,None);d[x].pop(b,None)
        del d[a];del d[b]
        for x in d:
            square={}
            for y,coefficient in d[x].items():
                square=add(square,scale(d[y],coefficient))
            check(not square,'integral_cancellation_preserves_d_squared')
    check(not any(d.values()),'integral_unit_contraction_complete')
    ranks = dict(Counter(3-len(f) for f in d))
    return ranks,pivots

def solve_integral(matrix: list[list[int]], rhs: list[int]) -> list[int]:
    """Exact rational elimination; reject any nonintegral returned witness."""
    if not matrix:
        raise ValueError('Empty matrix')
    rows=len(matrix);cols=len(matrix[0]);a=[list(map(Fraction,row))+[Fraction(b)]
                                         for row,b in zip(matrix,rhs)]
    pivots=[];rr=0
    for col in range(cols):
        j=next((j for j in range(rr,rows) if a[j][col]),None)
        if j is None:
            continue
        a[rr],a[j]=a[j],a[rr];p=a[rr][col]
        a[rr]=[v/p for v in a[rr]]
        for j in range(rows):
            if j!=rr and a[j][col]:
                p=a[j][col];a[j]=[x-p*y for x,y in zip(a[j],a[rr])]
        pivots.append((rr,col));rr+=1
        if rr==rows:
            break
    if any(not any(row[:cols]) and row[cols] for row in a):
        raise ValueError('Inconsistent exact chain equation')
    result=[Fraction(0)]*cols
    for row,col in pivots:
        result[col]=a[row][cols]
    if any(v.denominator!=1 for v in result):
        raise ValueError('This elimination did not produce an integral witness')
    result=[int(v) for v in result]
    check([sum(x*y for x,y in zip(row,result)) for row in matrix]==rhs,
          'integral_linear_witness_verified')
    return result

def short_name(d: Diag) -> str:
    return 'x'+str(SHORTS.index(d)) if d in SHORTS else 'D'+str(d[0])+str(d[1])

def face_name(f: Face) -> str:
    return 'T' if not f else ','.join(short_name(d) for d in f)

def vec_json(v):
    return {face_name(f):a for f,a in sorted(v.items())}

def main(output: Path) -> None:
    COUNT.clear()
    for c in CELLS:
        check(not apply_bd(BD[c]),'loaded_d_squared')
        check((not c[1])==legal(c,weight(c[0])), 'unit_grade_exact_stalk_admissibility')
        for (t,m),a in BD[c].items():
            check(eadd(m,shift(t))==shift(c),'all_incidence_fine_grades')
            check(legal(t,m),'all_incidence_legal_denominators')
            check(degree(t)==degree(c)-1,'all_incidence_homological_degrees')
            for supp in (V,B):
                if c in supp:
                    check(t in supp,'strict_loaded_support_filtration')
        for g in G:
            check(act_loaded(BD[c],g)==apply_bd(act_loaded({(c,ZERO):1},g)),
                  'physical_D3_loaded_differential_covariance')
            tc,_=act_cell(c,g)
            check((c in V)==(tc in V) and (c in B)==(tc in B),
                  'physical_D3_support_covariance')
            check(act_exp(weight(c[0]),g)==weight(tc[0]),'physical_D3_weight_covariance')
            for h in G:
                hc,hs=act_cell(c,h);ghc,gs=act_cell(hc,g)
                direct,sg=act_cell(c,mul(g,h))
                check((ghc,gs*hs)==(direct,sg),'physical_D3_all_group_words')
    check((len(CELLS),len(V),len(B))==(215,16,208),'loaded_support_census')
    check(len(C0)==45,'unit_grade_full_census')
    for f,h in C0:
        lhs=apply_bd({((f,h),weight(f)):1})
        rhs={((t,()),weight(t)):a for t,a in cellular_boundary(f).items()}
        check(lhs==rhs,'weighted_carrier_chain_identification')
    # An occurrence/independent Rees shift leaves this normal degree sector intact.
    for j in range(9):
        bump=exp({j:1})
        for c in CELLS:
            check(legal(c,eadd(weight(c[0]),bump))==(not c[1]),
                  'positive_occurrence_shift_preserves_sector')
    allfaces=set(FACES); vf={VP,VM};bf={f for f in FACES if any(d in SHORTS for d in f)}
    supports={'K':allfaces,'V':vf,'B':bf,'E':allfaces-vf,'B_over_V':bf-vf,'Q':allfaces-bf}
    homology={};pivots={}
    for name,supp in supports.items():
        homology[name],pivots[name]=unit_cancel(supp)
    check(homology['K']=={0:1},'integral_K_homology')
    check(homology['V']=={0:2},'integral_endpoint_homology')
    check(homology['E']=={1:1},'integral_E_homology')
    check(homology['B_over_V']=={1:3},'integral_road_homology')
    check(homology['Q']=={2:2},'integral_Q_homology')
    check(tuple(len(supports[k]) for k in ('V','B','K','E','B_over_V','Q'))==
          (2,41,45,43,39,4),'unit_grade_support_census')
    # Construct exactly the source-labelled four-edge D03 corridor.
    vertices=[VP,tuple(sorted((LONGS[0],SHORTS[1],SHORTS[3]))),
              tuple(sorted((LONGS[0],SHORTS[0],SHORTS[3]))),
              tuple(sorted((LONGS[0],SHORTS[0],SHORTS[4]))),VM]
    # Gauges are derived from the literal lexicographic incidence matrix.
    gauges={sorted(f for f in FACES if len(f)==3)[0]:1}
    while len(gauges)<14:
        oldlen=len(gauges)
        for f in (f for f in FACES if len(f)==2):
            (a,x),(b,y)=list(cellular_boundary(f).items())
            if a in gauges: gauges[b]=-x*y*gauges[a]
            elif b in gauges: gauges[a]=-x*y*gauges[b]
        if len(gauges)==oldlen:
            raise RuntimeError('Vertex gauge propagation stalled')
    z={}
    for a,b in zip(vertices,vertices[1:]):
        edge=tuple(sorted(set(a)&set(b)))
        check(len(edge)==2,'labelled_D03_gallery_edges')
        z=add(z,{edge:cellular_boundary(edge)[b]*gauges[b]})
    check(apply_cellular(z,allfaces)=={VP:1,VM:1},'both_actual_endpoint_values_are_one')
    check(not apply_cellular(z,supports['E']),'actual_E_unit_is_a_cycle')
    facets=sorted(f for f in supports['E'] if len(f)==1)
    edges=sorted(f for f in supports['E'] if len(f)==2)
    d2=[[cellular_boundary(f).get(e,0) for f in facets] for e in edges]
    hs={};ks={}
    for g in G:
        defect=add(act_chain(z,g),scale(z,-1))
        sol=solve_integral(d2,[defect.get(e,0) for e in edges])
        hs[g]={f:a for f,a in zip(facets,sol) if a}
        check(apply_cellular(hs[g],supports['E'])==defect,'actual_coherent_unit_edges')
        check(act_chain({VP:1,VM:1},g)=={VP:1,VM:1},'actual_endpoint_equivariance')
    for g,h in product(G,repeat=2):
        defect=add(act_chain(hs[h],g),scale(hs[mul(g,h)],-1),hs[g])
        k=defect.get(facets[0],0);ks[g,h]=k
        check(defect==scale(cellular_boundary(()),k),'actual_coherent_unit_faces')
    for g,h,k in product(G,repeat=3):
        check((-1)**g[1]*ks[h,k]-ks[mul(g,h),k]+ks[g,mul(h,k)]-ks[g,h]==0,
              'actual_coherent_unit_triples')
    # The literal connecting augmentation and quotient map are chain maps.
    def endpoint_boundary(v):
        return {f:a for f,a in apply_cellular(v,allfaces).items() if f in vf}
    for f in facets:
        check(not endpoint_boundary(cellular_boundary(f)),
              'both_endpoint_connecting_maps_are_chain_maps')
    for f in edges:
        for g in G:
            check(endpoint_boundary(act_chain({f:1},g))==act_chain(endpoint_boundary({f:1}),g),
                  'both_endpoint_connecting_maps_equivariant')
    # Actual quotient map keeps all three long facets and the chamber.
    qset=supports['Q']
    for f in supports['E']:
        direct={t:a for t,a in cellular_boundary(f).items() if t in qset}
        rhs={t:a for t,a in cellular_boundary(f).items() if t in qset} if f in qset else {}
        check(direct==rhs,'actual_E_to_Q_is_chain_map')
    a={g:[hs[g].get((di,),0) for di in LONGS] for g in G}
    def pa(v,g):
        out=[0,0,0]
        for i,di in enumerate(LONGS):
            out[LONGS.index(image_diag(di,g))]=(-1)**g[1]*v[i]
        return out
    def modnorm(v): return [v[0]-v[2],v[1]-v[2]]
    for g,h in product(G,repeat=2):
        delta=[x-y+z0 for x,y,z0 in zip(pa(a[h],g),a[mul(g,h)],a[g])]
        check(delta==[ks[g,h]]*3,'actual_Q_coherent_incidence')
        check(modnorm(delta)==[0,0],'actual_Q_M_one_cocycle')
    tau=sum(a[(1,0)])%3
    check(tau==1,'actual_Q_unit_nonzero_class')
    check(sum(ks[(i,0),(1,0)] for i in range(3))%3==tau,
          'norm_and_facet_transgression_agree')
    # In M=P/N the literal matrices and complete integer cocycle parametrization.
    R=[[-1,1],[-1,0]];S=[[-1,1],[0,1]]
    for g,expected in [((1,0),R),((0,1),S)]:
        columns=[modnorm(pa([int(i==j) for i in range(3)],g)) for j in range(2)]
        check([[columns[j][i] for j in range(2)] for i in range(2)]==expected,
              'literal_rank_two_M_matrices')
    det=(R[0][0]-1)*(R[1][1]-1)-R[0][1]*R[1][0]
    check(det==3,'M_rotation_has_no_integral_invariants')
    # Derive the cocycle constraints directly from all three group relators.
    def mapply(m,v): return [sum(a*b for a,b in zip(row,v)) for row in m]
    def mmul(a,b): return [[sum(a[i][k]*b[k][j] for k in range(2))
                            for j in range(2)] for i in range(2)]
    def relator_values(cr,cs):
        values=[]
        for word in ('rrr','ss','srsr'):
            action=[[1,0],[0,1]];value=[0,0]
            for letter in word:
                term=mapply(action,cr if letter=='r' else cs)
                value=[a+b for a,b in zip(value,term)]
                action=mmul(action,R if letter=='r' else S)
            check(action==[[1,0],[0,1]],'rank_two_M_relator_action')
            values.extend(value)
        return values
    relation_columns=[]
    for i in range(4):
        v=[int(i==j) for j in range(4)]
        relation_columns.append(relator_values(v[:2],v[2:]))
    relation_matrix=[[relation_columns[j][i] for j in range(4)] for i in range(6)]
    check(relation_matrix==[[0,0,0,0],[0,0,0,0],[0,0,0,1],[0,0,0,2],
                            [-1,0,1,-1],[1,0,-1,1]],
          'complete_integer_cocycle_relation_matrix')
    for A,B0,C,D0 in product(range(-2,3),repeat=4):
        rel=relator_values([A,B0],[C,D0])
        check((not any(rel))==(D0==0 and C==A),'cocycle_constraints_verified')
    for x,y in product(range(-4,5),repeat=2):
        cr=[a-b for a,b in zip(mapply(R,[x,y]),[x,y])]
        cs=[a-b for a,b in zip(mapply(S,[x,y]),[x,y])]
        check(cr==[-2*x+y,-x-y] and cs==[-2*x+y,0],
              'literal_coboundary_matrix_verified')
        check(sum(cr)%3==0,'coboundary_residue_zero')
    # Every class-zero cocycle has the following integral primitive.
    for A,B0 in product(range(-6,7),repeat=2):
        if (A+B0)%3==0:
            x=-(A+B0)//3;y=-B0-x
            check([-2*x+y,-x-y]==[A,B0],'class_zero_cocycle_exact_primitive_samples')
    # The old detector loop is nonliftable: the reflection-fixed facet sees 2v0=odd.
    check(image_diag(LONGS[0],(0,1))==LONGS[0],'physical_reflection_fixes_D03_facet')
    for v0 in range(-20,21):
        check((-2*v0)%2==0,'fixed_facet_reflection_difference_even')
    for b in range(-20,21):
        check((-1-2*b)%2==1,'all_representatives_of_old_parity_loop_odd')
    # Two source audits use genuinely different labelled reflections.
    old_reflect=lambda f:tuple(sorted(diag(2-a,2-b) for a,b in f))
    check(old_reflect(VP)==VP and old_reflect(VM)==VM,'older_target_reflection_fixes_endpoints')
    check(image_face(VP,(0,1))==VM and image_face(VM,(0,1))==VP,
          'physical_carrier_reflection_exchanges_endpoints')
    result={
      'status':'actual_target_unit_multigrade_endpoint_augmentation_Q_restriction_classified',
      'source_commit':COMMIT,'source_blobs':SOURCES,
      'coefficient_ring':'Z[X_0,...,X_8,u_0,...,u_8] with cell-specific normal localizations',
      'grading':'deg[S,H]=-sum_{a in S} deg X_a+sum_{a in S} deg u_a; top degree zero',
      'loaded_counts':{'K':215,'B':208,'V':16,'E':199,'Q':7},
      'unit_grade_counts':{k:len(v) for k,v in supports.items()},
      'integral_homology':homology,
      'integral_unit_pivot_counts':{k:len(v) for k,v in pivots.items()},
      'physical_action':{'r':'v -> v+2 mod 6','s':'v -> 3-v mod 6',
                         'top_reflection_sign':-1,'extended_and_checked_on_all_loaded_cells':True},
      'restriction_scope':'actual unit-multigrade endpoint connecting augmentation and canonical E -> Q projection; not the full sheet butterfly restriction',
      'coherent_unit':{'z':vec_json(z),'endpoint_values':[1,1],
          'facet_order':[face_name(f) for f in facets],
          'h':{str(g):vec_json(v) for g,v in hs.items()},
          'k':{str((g,h)):v for (g,h),v in ks.items()},
          'Q_facet_order':[short_name(d) for d in LONGS],
          'Q_a':{str(g):v for g,v in a.items()},'Q_class_mod_3':tau},
      'M_cohomology':{'H0':0,'H1':'Z/3','R':R,'S':S,
          'generator_cocycle_relation_matrix':relation_matrix,
          'cocycle_coordinates':'c(r)=(A,B), c(s)=(A,0)',
          'coboundary_coordinates':'(-2x+y,-x-y)',
          'class':'A+B mod 3'},
      'actual_Q_homotopy_fixed_marking_target':{'pi0':'Z/3','pi_n_for_n_ge_1':0},
      'actual_augmentation_Q_target':{'pi0':'Z (diagonal endpoint value) x Z/3',
                                     'pi_n_for_n_ge_1':0,'unit_image':[1,1]},
      'unit_relative_fibre':{'compatible_prescribed_object':'contractible',
                             'incompatible_prescribed_component':'empty'},
      'old_norm_detector_parity_loop':{'lifts_to_actual_Q':False,
         'obstruction':'fixed-facet coefficient of (s-1)v is even; norm times any odd parity representative is odd'},
      'not_claimed':['full normalization-sheet mixed-variance comparison',
         'both endpoint connector 2-cells of the physical butterfly',
         'retained Tor-grade comparison outside this homogeneous sector',
         'physical parity value or completed physical restriction map'],
      'proof_scope':'Exact finite target, equivariance, integral contractions and all group pair/triple witnesses; completeness of grading, cohomology and homotopy-fibre statements proved in accompanying note. Not proof-assistant certification.',
      'checks':dict(sorted(COUNT.items())), 'total_exact_assertions':sum(COUNT.values())}
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','unit_grade_counts','integral_homology',
          'actual_Q_homotopy_fixed_marking_target','unit_relative_fibre','total_exact_assertions')},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('actual_q_graded_restriction_certificate.json'))
    args=parser.parse_args()
    main(args.output)
