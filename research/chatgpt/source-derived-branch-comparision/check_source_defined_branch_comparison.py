#!/usr/bin/env python3
"""Exact checks for the polynomial conductor-road comparison.

Standard library only. All arithmetic is integral. Polynomial generators are
untruncated sparse symbols; a finite collection of degrees is tested. The
accompanying proof establishes the identities at every degree and over every
commutative coefficient ring. No source repository is modified.
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


def main(output: Path, max_degree: int) -> None:
    if max_degree < 1:
        raise ValueError('max_degree must be positive')
    bs=basis(max_degree)
    for k in bs:
        v=one(k)
        check(all(degree(t)==degree(k)-1 for t in differential(k)), 'differential_degree')
        check(lift(differential,differential(k))=={}, 'd_squared')
        check(lift(projection,differential(k))==lift(differential,projection(k)), 'comparison_chain_map')
        lhs=add(lift(differential,homotopy(k)), lift(homotopy,differential(k)))
        check(lhs==add(v,scale(projection(k),-1)), 'integral_branch_contraction')
        check(lift(homotopy,homotopy(k))=={}, 'homotopy_squared')
        check(all(t[2]==k[2] for t in homotopy(k)), 'branch_degree_filtration_preserved')
        for g in (rotation,reflection):
            check(lift(g,differential(k))==lift(differential,g(k)), 'source_dihedral_chain_covariance')
            check(lift(projection,g(k))==lift(g,projection(k)), 'comparison_dihedral_covariance')
            check(lift(homotopy,g(k))==lift(g,homotopy(k)), 'R_linear_homotopy_dihedral_covariance')
        r2=lift(rotation,rotation(k))
        check(lift(rotation,r2)==v, 'rotation_cubed')
        check(lift(reflection,reflection(k))==v, 'reflection_squared')
        check(lift(reflection,lift(rotation,reflection(k)))==r2, 'dihedral_relation')
        check(readout(differential(k))==0, 'readout_kills_boundaries')
        for b in ('x','y'):
            mul=lambda t: branch_multiply(t,b)
            check(lift(mul,differential(k))==lift(differential,mul(k)), 'A_linear_differential')
            # x and y act by zero on the target complex C_R.
            check(lift(projection,mul(k))=={}, 'A_linear_comparison')
    primitive={('s','x',0):1, ('q','',0):1}
    check(lift(differential,primitive)=={}, 'physical_unit_is_cycle')
    check(readout(primitive)==1, 'physical_unit_readout')
    for n in range(1,max_degree+1):
        for b in ('x','y'):
            witness={('a',b,n):1}
            check(lift(differential,witness)=={('s',b,n):1}, 'explicit_polynomial_boundary')
    # Explicit integral reduction for cycles, not just rational rank tests.
    for k in range(-3,4):
        for common in range(-2,3):
            for q1 in range(-2,3):
                for q2 in range(-2,3):
                    c,w=cycle_from_data(k,common,q1,q2,{1:2, max_degree:3},{2:-1})
                    check(lift(differential,c)=={}, 'arbitrary_cycle_test')
                    check(add(c,scale(primitive,-k))==lift(differential,w), 'integral_cycle_normal_form')
    # This map is R-linear and equivariant, but the constant inclusion and
    # ambient homotopy are not A-linear. Record rather than conceal this.
    s0=('s','x',0)
    left=lift(homotopy,branch_multiply(s0,'x'))
    right=lift(lambda k:branch_multiply(k,'x'),homotopy(s0))
    check(left!=right, 'ambient_homotopy_not_A_linear_control')
    # Keeping only the old scalar diagonal relation is not A-linear after
    # upgrading the sheets to the full normalization module.
    diag_image=differential(('a','c',0))
    check(lift(lambda k:branch_multiply(k,'x'),diag_image)=={('s','x',1):1}, 'constant_only_diagonal_not_A_linear')
    # Removing the degree-two polynomial witnesses changes the answer.
    check(projection(('s','x',1))=={}, 'negative_control_truncated_source_loses_class')
    # Its class would be nonzero without matching node polynomial generators.
    check(all(('s','x',1) not in differential(k) for k in basis(0)), 'negative_control_no_boundary_in_constants_only_node')
    # In the original kernel Q, common-normalized pairs are distinct.
    common_pair={('s','x',0):1, ('s','y',0):1}
    shifted_pair=add(common_pair,{('s','x',1):1})
    check(lift(differential,common_pair)==lift(differential,shifted_pair)=={}, 'old_Q_pairs_are_cycles')
    check(lift(differential,node(1,{},{}))==common_pair, 'common_unit_is_relative_boundary')
    check(lift(differential,node(1,{1:1},{}))==shifted_pair, 'polynomial_common_unit_is_relative_boundary')
    # Check the source matrices are recovered exactly at polynomial degree zero.
    ordered={0:[('o','',0)],1:[('s','x',0),('s','y',0)]+[('q','',j) for j in range(3)],
             2:[('a','c',0)]+[('t','',j) for j in range(3)],3:[('z','',0)]}
    matrices={str(n):[[differential(c).get(r,0) for c in ordered[n]] for r in ordered[n-1]] for n in (1,2,3)}
    check(matrices['1']==[[1,-1,-1,-1,-1]], 'source_d1_exact_match')
    check(matrices['2']==[[1,0,0,0],[1,0,0,0],[0,1,0,-1],[0,-1,1,0],[0,0,-1,1]], 'source_d2_exact_match')
    check(matrices['3']==[[0],[1],[1],[1]], 'source_d3_exact_match')
    result={
        'status':'verified_endpoint_coefficient_comparison',
        'source_repository':'andrey-kokoev/marici', 'source_commit':COMMIT,
        'source_file_blobs':SOURCES, 'source_matrices':matrices,
        'max_polynomial_degree_tested':max_degree,
        'checks':dict(sorted(COUNTS.items())), 'total_checks':sum(COUNTS.values()),
        'comparison':'P_R -> C_R by conductor evaluation on both normalization branches and on the node; identity on road and conductor modules',
        'kernel':'[J --identity--> J] in homological degrees 2,1; J=xR[x] direct-sum yR[y]',
        'cohomological_warning':'All model degrees in this certificate are homological.',
        'homology':{'1':'R_or', 'other':'0'},
        'positive_branch_modes':'retained as cochains; canonically exact in the relative endpoint comparison',
        'common_conductor_unit':'a relative boundary, not the physical unit',
        'physical_unit':'((1,0);(1,0,0))',
        'equivariance':'strict D3 at coefficient-complex level; no averaging',
        'A_linearity':'comparison is A-linear; acyclic kernel contraction is A-linear; the displayed ambient splitting/homotopy is only R-linear',
        'global_claim':'No identification with all filtered support-PC/Q/Cartier physical functors is asserted.',
        'proof_scope':'Finite exact tests accompany an all-degree algebraic proof; no proof-assistant certification and no execution of the source integration checker.'
    }
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','total_checks','kernel','homology','global_claim')},indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('source_defined_branch_comparison_certificate.json'))
    parser.add_argument('--max-degree',type=int,default=12)
    args=parser.parse_args()
    main(args.output,args.max_degree)
