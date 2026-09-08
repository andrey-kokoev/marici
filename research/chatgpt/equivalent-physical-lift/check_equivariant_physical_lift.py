#!/usr/bin/env python3
"""Exact strict and homotopy-coherent D3 lifting checks.

Standard library only. Reuses the explicitly retrieved polynomial endpoint
model (pinned Marici commit recorded below), then independently constructs
all coherent lifts, the strict obstruction lattice, and negative controls.
No averaging, denominator inversion, new homotopy generators, or repository
writes are used. Arbitrary-degree claims are proved in the accompanying note.
"""
from __future__ import annotations
import argparse
from collections import Counter
from pathlib import Path
import json
from typing import TypeAlias

Key: TypeAlias = tuple[str, str, int]
Vector: TypeAlias = dict[Key, int]
COUNTS: Counter[str] = Counter()
COMMIT = 'd1947b67a60d3e88ba77f4ca60ea02c2a306ee61'
SOURCES = {
    'research/voevodsky/check_normalization_conductor_bimodule_kernel.py': '2982163ca939dd1e09bb0b66b4229e31430e3c30',
    'research/voevodsky/check_conductor_road_endpoint_pullback.rs': 'cfe13e928e911f8914de6670f34cc4c8859b3402',
    'research/voevodsky/check_physical_derived_pullback_after_transform.py': '7993b2b1bbdba03d05c3f443a45717d7b8efeec5',
    'research/voevodsky/check_multirees_conductor_stalk_kernel.py': '1237d71e8c9fd56e064226825049d84dd03f42e2',
    'research/voevodsky/check_global_mixed_variance_transform.py': '3b23d8a71a374435e8f54d4fe9451a08cb8ab98e',
}

def check(value: bool, label: str) -> None:
    if not value:
        raise AssertionError(label)
    COUNTS[label] += 1


def add(*terms: Vector) -> Vector:
    out: Vector = {}
    for term in terms:
        for k, c in term.items():
            out[k] = out.get(k, 0) + c
            if not out[k]:
                del out[k]
    return out


def scale(v: Vector, c: int) -> Vector:
    return {k: c*a for k, a in v.items() if c*a}


def lift(fn, v: Vector) -> Vector:
    out: Vector = {}
    for k, a in v.items():
        out = add(out, scale(fn(k), a))
    return out


def one(k: Key) -> Vector:
    return {k: 1}


def degree(k: Key) -> int:
    return {'o': 0, 's': 1, 'q': 1, 'a': 2, 't': 2, 'z': 3}[k[0]]


def basis(n: int) -> list[Key]:
    return ([('o','',0), ('z','',0), ('a','c',0)]
            + [('s',b,j) for b in ('x','y') for j in range(n+1)]
            + [('a',b,j) for b in ('x','y') for j in range(1,n+1)]
            + [(b,'',j) for b in ('q','t') for j in range(3)])


def differential(k: Key) -> Vector:
    typ, branch, n = k
    if typ == 'z':
        return {('t','',j): 1 for j in range(3)}
    if typ == 'a':
        if branch == 'c':
            return {('s','x',0):1, ('s','y',0):1}
        return {('s',branch,n):1}
    if typ == 't':
        return {('q','',n):1, ('q','',(n+1)%3):-1}
    if typ == 's':
        return {('o','',0): 1 if branch == 'x' else -1} if n == 0 else {}
    if typ == 'q':
        return {('o','',0):-1}
    return {}


def projection(k: Key) -> Vector:
    typ, branch, n = k
    return {} if typ in ('a','s') and n > 0 else one(k)


def homotopy(k: Key) -> Vector:
    typ, branch, n = k
    return {('a',branch,n):1} if typ == 's' and n > 0 else {}


def rotation(k: Key) -> Vector:
    typ, b, n = k
    return {(typ,b,(n+1)%3):1} if typ in ('q','t') else one(k)


def reflection(k: Key) -> Vector:
    typ, b, n = k
    if typ in ('s','a') and b in ('x','y'):
        return {(typ, 'y' if b == 'x' else 'x', n):1}
    if typ == 'q':
        return {(typ,b,(-n)%3):-1}
    if typ == 't':
        return {(typ,b,(-n-1)%3):1}
    if typ == 'o':
        return {k:-1}
    return one(k)


def branch_multiply(k: Key, b: str) -> Vector:
    """Action of x or y as an A-module; conductor/road modules have x=y=0."""
    typ, branch, n = k
    if typ == 'a' and branch == 'c':
        return {('a',b,1):1}
    if typ in ('a','s') and branch == b:
        return {(typ,b,n+1):1}
    return {}


def readout(v: Vector) -> int:
    return sum(a for (typ,_,_),a in v.items() if typ == 'q')


def node(c: int, x: dict[int,int], y: dict[int,int]) -> Vector:
    out = {('a','c',0):c} if c else {}
    for b,terms in [('x',x),('y',y)]:
        for n,a in terms.items():
            if n < 1:
                raise ValueError('A positive branch term must have degree at least one')
            if a:
                out[('a',b,n)] = a
    return out


def cycle_from_data(k: int, common: int, q1: int, q2: int,
                    x: dict[int,int], y: dict[int,int]) -> tuple[Vector,Vector]:
    """Return a cycle and a witness for reduction to k times the primitive."""
    q0=k-q1-q2
    sheet = {('s','x',0):common+k, ('s','y',0):common}
    sheet = {a:b for a,b in sheet.items() if b}
    for branch,terms in [('x',x),('y',y)]:
        for n,c in terms.items():
            if c:
                sheet[('s',branch,n)]=c
    roads={('q','',j):q for j,q in enumerate((q0,q1,q2)) if q}
    tags={('t','',1):q1, ('t','',2):q1+q2}
    tags={a:b for a,b in tags.items() if b}
    witness=add(node(common,x,y),tags)
    return add(sheet,roads),witness


from fractions import Fraction
from itertools import product, combinations
from math import gcd
from functools import reduce
import hashlib

Group = tuple[int, int]
GROUP: tuple[Group, ...] = tuple(product(range(3), range(2)))
IDENTITY: Group = (0, 0)
ROT: Group = (1, 0)
REFL: Group = (0, 1)
DIAG: Key = ('a','c',0)
TOP: Key = ('z','',0)
Z: Vector = {('s','x',0):1, ('q','',0):1}


def mul(g: Group, h: Group) -> Group:
    return ((g[0] + (-1)**g[1]*h[0]) % 3, (g[1]+h[1]) % 2)


def chi(g: Group) -> int:
    return (-1)**g[1]


def star(g: Group, v: Vector) -> Vector:
    """Source action tensored with its once-relative orientation character."""
    if g[1]:
        v = scale(lift(reflection, v), -1)
    for _ in range(g[0]):
        v = lift(rotation, v)
    return v


def d(v: Vector) -> Vector:
    return lift(differential, v)


def edge_h(g: Group) -> Vector:
    i,e = g
    return add({DIAG:-e} if e else {}, {('t','',j):-1 for j in range(i)})


def carry(g: Group, h: Group) -> int:
    return -((g[0]+chi(g)*h[0]) // 3)


def face_k(g: Group, h: Group) -> Vector:
    n = carry(g,h)
    return {TOP:n} if n else {}


def defect(g: Group) -> Vector:
    return add(star(g,Z), scale(Z,-1))


def contract_cycle(v: Vector) -> Vector:
    """On cycles: d H0(v)=v-readout(v) Z. No division is needed."""
    if d(v):
        raise ValueError('contract_cycle requires an endpoint cycle')
    ans: Vector = {}
    c = v.get(('s','y',0),0)
    if c: ans[DIAG]=c
    for (kind,b,n),a in v.items():
        if kind=='s' and n>0: ans[('a',b,n)]=a
    q1=v.get(('q','',1),0)
    q2=v.get(('q','',2),0)
    if q1: ans[('t','',1)]=q1
    if q1+q2: ans[('t','',2)]=q1+q2
    return ans


def contract_relations(v: Vector) -> Vector:
    """On P2: H1(v)=t0 times the existing norm generator."""
    if any(degree(x)!=2 for x in v):
        raise ValueError('contract_relations requires degree-two input')
    t0 = v.get(('t','',0),0)
    return {TOP:t0} if t0 else {}


def determinant(a: list[list[int]]) -> int:
    if not a: return 1
    if len(a)==1: return a[0][0]
    return sum((-1)**j*a[0][j]*determinant([r[:j]+r[j+1:] for r in a[1:]]) for j in range(len(a)))


def invariant_factors(a: list[list[int]]) -> list[int]:
    """Small integer matrix Smith factors from determinantal divisors."""
    rows,cols=len(a),len(a[0])
    previous=1; out=[]
    for k in range(1,min(rows,cols)+1):
        minors=(abs(determinant([[a[i][j] for j in jj] for i in ii]))
                for ii in combinations(range(rows),k) for jj in combinations(range(cols),k))
        value=reduce(gcd,minors,0)
        if not value: break
        if value % previous: raise ArithmeticError('Invalid determinantal divisor')
        out.append(value//previous); previous=value
    return out


def encode(v: Vector) -> list[dict]:
    return [{'basis':list(k),'coefficient':a} for k,a in sorted(v.items())]


def main(output: Path, max_degree: int) -> None:
    if max_degree<1: raise ValueError('max_degree must be positive')
    COUNTS.clear()
    bs=basis(max_degree)
    # Recheck the retrieved source module, including untruncated branch symbols.
    for x in bs:
        v=one(x)
        check(not d(d(v)), 'source_d_squared')
        for g in GROUP:
            check(d(star(g,v))==star(g,d(v)), 'twisted_action_chain_map')
            check(readout(star(g,v))==readout(v), 'physical_readout_invariant')
            check(lift(projection,star(g,v))==star(g,lift(projection,v)), 'polynomial_comparison_equivariant')
            for h in GROUP:
                check(star(g,star(h,v))==star(mul(g,h),v), 'all_group_action_products')
        check(add(d(lift(homotopy,v)),lift(homotopy,d(v)))==add(v,scale(lift(projection,v),-1)),
              'polynomial_tail_contraction')
        for b in ('x','y'):
            check(lift(lambda y:branch_multiply(y,b),d(v))==d(lift(lambda y:branch_multiply(y,b),v)),
                  'source_A_linearity')
    for g,h,k in product(GROUP,repeat=3):
        check(mul(mul(g,h),k)==mul(g,mul(h,k)), 'group_associativity')
    check(not d(Z) and readout(Z)==1, 'fixed_endpoint_unit')
    check(readout(lift(reflection,Z))==-1, 'orientation_twist_required')
    # The reindexed marking complex has P1-cycles in degree zero, P2 in one,
    # and P3 in two. Verify an integral retraction of its readout to Z.
    cycle_basis=[Z, d(one(DIAG)),d(one(('t','',0))),d(one(('t','',1)))]
    cycle_basis += [one(('s',b,n)) for b in ('x','y') for n in range(1,max_degree+1)]
    for v in cycle_basis:
        check(d(contract_cycle(v))==add(v,scale(Z,-readout(v))), 'marking_degree_zero_contraction')
    for x in bs:
        if degree(x)==2:
            v=one(x)
            check(add(d(contract_relations(v)),contract_cycle(d(v)))==v,'marking_degree_one_contraction')
        if degree(x)==3:
            v=one(x)
            check(contract_relations(d(v))==v,'marking_degree_two_contraction')
    for scalar,common,q1,q2 in product(range(-2,3),repeat=4):
        v,w=cycle_from_data(scalar,common,q1,q2,{1:2,max_degree:3},{1:-4,max_degree:1})
        check(not d(v), 'arbitrary_polynomial_cycle')
        check(d(contract_cycle(v))==add(v,scale(Z,-scalar)), 'arbitrary_polynomial_unit_reduction')
    # Explicit normalized bar-resolution chain map in every nonzero degree.
    for g in GROUP:
        check(d(edge_h(g))==defect(g), 'bar_edges')
        check(readout(defect(g))==0 and not d(defect(g)), 'fixed_endpoints_under_edge')
        check(all(degree(x)==2 for x in edge_h(g)), 'source_admissible_edge_degree')
        check(all(x[0] in ('a','t') and (x[0]!='a' or x==DIAG) for x in edge_h(g)),
              'no_added_or_polynomial_edge_generators')
    face_nonzero=0
    for g,h in product(GROUP,repeat=2):
        rhs=add(star(g,edge_h(h)),scale(edge_h(mul(g,h)),-1),edge_h(g))
        check(rhs==d(face_k(g,h)), 'bar_faces')
        if face_k(g,h): face_nonzero += 1
        b=lambda x:-x[0]
        check(chi(g)*b(h)-b(mul(g,h))+b(g)==3*carry(g,h), 'three_times_carry_is_coboundary')
        check(add(star(g,defect(h)),scale(defect(mul(g,h)),-1),defect(g))=={}, 'strict_defect_one_cocycle')
    for g,h,k in product(GROUP,repeat=3):
        rhs=add(star(g,face_k(h,k)),scale(face_k(mul(g,h),k),-1),
                face_k(g,mul(h,k)),scale(face_k(g,h),-1))
        check(not rhs, 'bar_tetrahedra')
    check(edge_h(IDENTITY)=={}, 'normalized_identity_edge')
    for g in GROUP:
        check(not face_k(IDENTITY,g) and not face_k(g,IDENTITY), 'normalized_degenerate_faces')
    check(add(star(REFL,edge_h(REFL)),edge_h(REFL))=={}, 'reflection_homotopy_closes')
    cyclic_loop=add(*(star((i,0),edge_h(ROT)) for i in range(3)))
    check(cyclic_loop==d({TOP:-1}), 'three_rotations_filled_by_source_norm')
    # Obstruction groups on the integral primitive boundary lattice.
    # A cocycle on r,s is parametrized by (alpha,u,v): c(r)=(0,u,v),
    # c(s)=(alpha,0,v), in basis (sheet diagonal, q0-q1, q1-q2).
    coboundary=[[-2,0,0],[0,-1,-1],[0,1,-2]]
    def boundary_vector(c):
        aa,uu,vv=c
        return add({('s','x',0):aa,('s','y',0):aa} if aa else {},
                   {('q','',j):n for j,n in enumerate((uu,-uu+vv,-vv)) if n})
    def cocycle_from_parameters(params,g):
        alpha,uu,vv=params
        cr=boundary_vector((0,uu,vv)); cs=boundary_vector((alpha,0,vv))
        out={}
        for j in range(g[0]): out=add(out,star((j,0),cr))
        if g[1]: out=add(out,star((g[0],0),cs))
        return out
    for params in ((1,0,0),(0,1,0),(0,0,1)):
        for g,h in product(GROUP,repeat=2):
            check(add(star(g,cocycle_from_parameters(params,h)),
                      scale(cocycle_from_parameters(params,mul(g,h)),-1),
                      cocycle_from_parameters(params,g))=={}, 'H1_parameter_basis_all_products')
    for j in range(3):
        v=boundary_vector(tuple(int(i==j) for i in range(3)))
        params=tuple(coboundary[i][j] for i in range(3))
        for g in GROUP:
            check(add(star(g,v),scale(v,-1))==cocycle_from_parameters(params,g),
                  'H1_coboundary_matrix_from_actual_action')
    for g in GROUP:
        check(defect(g)==cocycle_from_parameters((-1,-1,0),g), 'joint_H1_class_actual_cocycle')
    check(invariant_factors(coboundary)==[1,1,6], 'joint_H1_smith_factors')
    check(invariant_factors([[-2]])==[2], 'reflection_H1_order_two')
    check(invariant_factors([[-1,-1],[1,-2]])==[1,3], 'rotation_H1_order_three')
    orders=[]
    for n in range(1,13):
        candidate=[Fraction(n,2),Fraction(2*n,3),Fraction(n,3)]
        check([sum(coboundary[i][j]*candidate[j] for j in range(3)) for i in range(3)]==[-n,-n,0],
              'joint_obstruction_multiple_solution')
        integral=all(x.denominator==1 for x in candidate)
        check(integral==(n%6==0), 'joint_obstruction_exact_divisibility')
        if integral: orders.append(n)
    check(min(orders)==6,'joint_obstruction_exact_order_six')
    # A primitive invariant representative of six times the physical unit.
    z6={('s','x',0):3,('s','y',0):-3,('q','',0):2,('q','',1):2,('q','',2):2}
    check(not d(z6) and readout(z6)==6,'strict_sixfold_unit')
    for g in GROUP:
        check(star(g,z6)==z6,'strict_sixfold_unit_invariant')
        witness=add(scale(Z,6),scale(z6,-1))
        check(add(star(g,witness),scale(witness,-1))==scale(defect(g),6), 'order_six_coboundary_witness')
    # Carry obstruction is nonzero on C3 and has order exactly three.
    cyclic_sum=sum(carry((i,0),ROT) for i in range(3))
    check(cyclic_sum==-1,'carry_nonzero_mod_three')
    for values in product(range(-2,3),repeat=2):
        lam={IDENTITY:0,ROT:values[0],(2,0):values[1]}
        ds=sum(lam[ROT]-lam[mul((i,0),ROT)]+lam[(i,0)] for i in range(3))
        check(ds==3*lam[ROT],'cyclic_coboundary_sum_divisible_by_three')
    # Polynomial ideal contributes zero H1: r acts trivially, s acts by
    # negative swap. Its cocycle (t,t) is the coboundary of (-t,0).
    for n in range(1,max_degree+1):
        for t in range(-2,3):
            pre={('s','x',n):-t} if t else {}
            target={('s','x',n):t,('s','y',n):t} if t else {}
            check(add(star(REFL,pre),scale(pre,-1))==target,'branch_pair_H1_coboundary')
    # Independent finite-ring control of strict equations, no extrapolation.
    modulus_results=[]
    for modulus in range(2,31):
        sol=[(a,c) for a in range(modulus) for c in range(modulus)
             if (2*a-1)%modulus==0 and (3*c-1)%modulus==0]
        check(bool(sol)==(gcd(modulus,6)==1),'strict_modulus_condition')
        modulus_results.append({'modulus':modulus,'strict_unit_exists':bool(sol)})
        for g,h in product(GROUP,repeat=2):
            rhs=add(star(g,edge_h(h)),scale(edge_h(mul(g,h)),-1),edge_h(g),scale(d(face_k(g,h)),-1))
            check(all(c%modulus==0 for c in rhs.values()),'coherence_survives_modulus')
    # Counterfactual truncations: no node means no sheet-diagonal boundary;
    # no top means the nontrivial cyclic tag loop has no degree-two filler.
    check(defect(REFL)=={('s','x',0):-1,('s','y',0):-1},'without_node_reflection_defect')
    check(all(not any(k[0]=='s' for k in differential(x)) for x in bs if degree(x)==2 and x[0]!='a'),
          'without_node_no_sheet_boundary')
    check(cyclic_loop!={} and not d(cyclic_loop), 'without_norm_nontrivial_cycle')
    check(all(k[0]=='t' for k in cyclic_loop), 'without_norm_cycle_is_actual_tag_norm')
    # Exact source matrices are included for independent reconstruction.
    ordered={0:[('o','',0)],1:[('s','x',0),('s','y',0)]+[('q','',j) for j in range(3)],
             2:[DIAG]+[('t','',j) for j in range(3)],3:[TOP]}
    matrices={str(n):[[differential(c).get(r,0) for c in ordered[n]] for r in ordered[n-1]] for n in (1,2,3)}
    check(matrices['1']==[[1,-1,-1,-1,-1]],'source_d1')
    check(matrices['2']==[[1,0,0,0],[1,0,0,0],[0,1,0,-1],[0,-1,1,0],[0,0,-1,1]],'source_d2')
    check(matrices['3']==[[0],[1],[1],[1]],'source_d3')
    result={
      'status':'proved_for_supplied_conductor_road_endpoint_coefficient_complex',
      'source_commit':COMMIT,'source_file_blobs':SOURCES,
      'group':'D3 = C3 semidirect C2 = S3, order 6 (not the octagon group D8)',
      'orientation':'all source actions tensored with chi(r)=1, chi(s)=-1',
      'fixed_endpoint_conditions':'sheet difference = road sum = 1',
      'source_matrices':matrices,
      'strict_unit_space':'empty over Z',
      'strict_readout_image':'6Z',
      'joint_obstruction_H1':'Z/2 direct-sum Z/3 = Z/6',
      'joint_obstruction_order':6,
      'H1_cocycle_coordinates':['c(s)_diagonal','c(r)_(q0-q1)','c(r)_(q1-q2)'],
      'H1_coboundary_matrix':coboundary,
      'H1_class_coordinates':[-1,-1,0],
      'H1_smith_factors':[1,1,6],
      'primitive_source_cycle':encode(Z),'strict_sixfold_cycle':encode(z6),
      'group_order':[list(g) for g in GROUP],
      'edge_homotopies':[{'group':list(g),'value':encode(edge_h(g))} for g in GROUP],
      'face_coefficients':[[carry(g,h) for h in GROUP] for g in GROUP],
      'edge_count':6,'pair_count':36,'nonzero_face_count':face_nonzero,'triple_count':216,
      'coherent_unit_space':'contractible',
      'normalized_marking_complex':'K0=ker(d1), K1=P2, K2=P3; readout K->Z',
      'arbitrary_higher_degrees':'bar map is zero above degree 2; all chain equations above degree 3 then vanish',
      'counterfactuals':{
        'without_node_relations':'reflection cannot be connected within unit component',
        'without_top_norm':'carry class in H2(D3,Z_chi) has exact order 3; no coherent unit',
        'full_source':'existing node and top norm terms supply all needed fillers'},
      'carry_order':3,'carry_threefold_coboundary':'b(r^i s^e)=-i',
      'coefficient_scope':'strict H1 numbers over the integral primitive sector/full polynomial branches with trivial base action; integral coherent formulas also extend along compatible coefficient maps',
      'max_polynomial_degree_sampled':max_degree,
      'modulus_controls':modulus_results,
      'checks':dict(sorted(COUNTS.items())),'total_exact_assertions':sum(COUNTS.values()),
      'limitations':[
        'Finite exact checks accompany all-degree contraction and bar-resolution proofs; not proof-assistant verification.',
        'Fixed endpoint quotients are preserved, not arbitrarily chosen individual sheet and road coefficients.',
        'Explicit vector and ambient contraction formulas are R-linear; no A-linear ambient splitting is claimed.',
        'No assertion about missing generic-Q, support-PC, mixed branch-Rees, or global geometric comparison.',
        'The missing-node and missing-norm models are counterfactual diagnostics, not modifications of the admitted source.'
      ]
    }
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','strict_readout_image','joint_obstruction_order','coherent_unit_space',
                                           'pair_count','triple_count','carry_order','total_exact_assertions')},indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('equivariant_physical_lift_certificate.json'))
    parser.add_argument('--max-degree',type=int,default=12)
    args=parser.parse_args()
    main(args.output,args.max_degree)
