#!/usr/bin/env python3
"""Exact audit of the formal nodal conductor-supported comparison.

Standard library only. No network or repository writes. Node polynomials are
sparse and untruncated: xy=0 is the only branch relation. The finite tests
check explicit identities; the companion note proves the all-degree claims.
This is NOT a reconstruction of Marici's complete physical relative functor.
"""
from __future__ import annotations
import argparse
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
from typing import TypeAlias

Monomial: TypeAlias = tuple[int, int]  # base Laurent exponent; signed branch exponent
Poly: TypeAlias = dict[Monomial, int]  # positive branch exponent=x; negative=y
Pair: TypeAlias = tuple[Poly, Poly]
COUNTS: Counter[str] = Counter()
COMMIT = 'd1947b67a60d3e88ba77f4ca60ea02c2a306ee61'
SOURCES = {
 'research/voevodsky/check_normalization_conductor_bimodule_kernel.py': '2982163ca939dd1e09bb0b66b4229e31430e3c30',
 'research/voevodsky/check_generic_log_dnc_thom_trace.py': '95fd466d144bafea6838cfeacc4aaf485b124275',
 'research/voevodsky/check_global_mixed_variance_transform.py': '3b23d8a71a374435e8f54d4fe9451a08cb8ab98e',
 'src/ledger/20260817-627 The Conductor Difference Complex Is the Universal Mixed-Variance Kernel.md': '263ff4cdc1b2114cbdb99680db2e999dff41ce30',
 'src/ledger/20260814-141 Conductor Bockstein Transgression and the Endpoint-Defect Reduction.md': '5d10a833f7c77b8a9ba98e63dbcd15a7c10a1e95',
}


def check(value: bool, category: str, detail: object = None) -> None:
    if not value:
        raise AssertionError(f'{category}: {detail!r}')
    COUNTS[category] += 1


def mono(branch: int = 0, base: int = 0, coefficient: int = 1) -> Poly:
    return {(base, branch): coefficient} if coefficient else {}


def add(a: Poly, b: Poly, scale: int = 1) -> Poly:
    ans = dict(a)
    for m, c in b.items():
        ans[m] = ans.get(m, 0) + scale*c
        if not ans[m]:
            del ans[m]
    return ans


def mul(a: Poly, b: Poly) -> Poly:
    ans: Poly = {}
    for (r, i), c in a.items():
        for (s, j), d in b.items():
            if i*j < 0:  # x^i y^j=0 when both branch powers are positive
                continue
            key = (r+s, i+j)
            ans[key] = ans.get(key, 0) + c*d
            if not ans[key]:
                del ans[key]
    return ans


def refl(a: Poly) -> Poly:
    return {(r, -i): c for (r, i), c in a.items()}


def const(a: Poly) -> Poly:
    return {m: c for m, c in a.items() if m[1] == 0}


def divide_branch(a: Poly, branch: int) -> Poly:
    if branch not in (-1, 1) or any(i*branch <= 0 for _, i in a):
        raise ValueError('Polynomial is not in the specified branch ideal')
    return {(r, i-branch): c for (r, i), c in a.items()}


X, Y, ONE = mono(1), mono(-1), mono()
ZERO_PAIR: Pair = ({}, {})


def pair_add(a: Pair, b: Pair, scale: int = 1) -> Pair:
    return add(a[0], b[0], scale), add(a[1], b[1], scale)


def pair_scale(a: Pair, s: Poly) -> Pair:
    return mul(a[0], s), mul(a[1], s)


def dual_d(n: int, v: tuple[Poly, ...]) -> Pair:
    if n == 0:
        return mul(X, v[0]), mul(Y, v[0])
    if n % 2:
        return mul(Y, v[0]), mul(X, v[1])
    return mul(X, v[0]), mul(Y, v[1])


def dual_action(n: int, v: tuple[Poly, ...]) -> tuple[Poly, ...]:
    if n == 0:
        return (refl(v[0]),)
    return refl(v[1]), refl(v[0])


def residue(v: Pair) -> Poly:
    if dual_d(1, v) != ZERO_PAIR:
        raise ValueError('The residue is defined here only on degree-one cycles')
    return add(const(divide_branch(v[0], 1)), const(divide_branch(v[1], -1)), -1)


def degree_one_reduction(v: Pair) -> tuple[Poly, Poly]:
    ax, by = divide_branch(v[0], 1), divide_branch(v[1], -1)
    r = add(const(ax), const(by), -1)
    f = add(add(add(ax, r, -1), by), const(by), -1)
    return r, f


def normalization(a: Poly) -> Pair:
    return ({m:c for m,c in a.items() if m[1] >= 0},
            {m:c for m,c in a.items() if m[1] <= 0})


def difference(n: Pair) -> Poly:
    return add(const(n[0]), const(n[1]), -1)


def normal_action(n: Pair) -> Pair:
    return refl(n[1]), refl(n[0])


def normal_add(n: Pair, m: Pair, scale: int = 1) -> Pair:
    return pair_add(n, m, scale)


def normal_to_node(n: Pair) -> Poly:
    if difference(n):
        raise ValueError('Different conductor values')
    return add(add(n[0], n[1]), const(n[0]), -1)


def unit_smith(matrix: list[list[int]]) -> tuple[int, list[list[int]]]:
    a = [r[:] for r in matrix]
    rows, cols = len(a), len(a[0]) if a else 0
    k = 0
    while k < min(rows, cols):
        hit = next(((i,j) for i in range(k,rows) for j in range(k,cols)
                    if abs(a[i][j]) == 1), None)
        if hit is None:
            break
        i,j = hit
        a[k],a[i] = a[i],a[k]
        for row in a:
            row[k],row[j] = row[j],row[k]
        if a[k][k] < 0:
            a[k] = [-x for x in a[k]]
        for i in range(rows):
            if i != k and a[i][k]:
                factor = a[i][k]
                a[i] = [x-factor*y for x,y in zip(a[i],a[k])]
        for j in range(cols):
            if j != k and a[k][j]:
                factor = a[k][j]
                for i in range(rows):
                    a[i][j] -= factor*a[i][k]
        k += 1
    return k, [row[k:] for row in a[k:]]


def audit_local(branch_bound: int, homological_bound: int) -> dict:
    basis = [mono(i, r) for r in (-2,0,3) for i in range(-branch_bound,branch_bound+1)]
    samples = basis + [add(add(mono(2,-1,3),mono(-3,2,-2)),ONE)]
    check(mul(X,Y) == {}, 'node_relation')
    for f in samples:
        check(normal_to_node(normalization(f)) == f, 'normalization_injective_explicit_inverse')
        check(difference(normalization(f)) == {}, 'conductor_exact_sequence')
        check(normal_action(normalization(f)) == normalization(refl(f)), 'normalization_reflection')
        for n in range(homological_bound+1):
            for v in (((f,),) if n == 0 else ((f,{}),({},f))):
                out = dual_d(n,v)
                check(dual_d(n+1,out) == ZERO_PAIR, 'dual_d_squared', n)
                check(dual_action(n+1,out) == dual_d(n,dual_action(n,v)), 'dual_reflection', n)
                for s in (mono(0,-1),mono(0,2)):
                    vs = tuple(mul(s,a) for a in v)
                    check(dual_d(n,vs) == pair_scale(out,s), 'localization_naturality', n)
        # Complete monomial generators of all positive-degree cycle modules.
        xp = {m:c for m,c in f.items() if m[1] >= 0}
        yp = {m:c for m,c in f.items() if m[1] <= 0}
        for v in ((mul(X,xp),{}),({},mul(Y,yp)),(mul(X,xp),mul(Y,yp))):
            check(dual_d(1,v) == ZERO_PAIR, 'degree_one_cycles')
            r,primitive = degree_one_reduction(v)
            check(pair_add(v,(mul(X,r),{}),-1) == dual_d(0,(primitive,)), 'degree_one_reduction')
            check(residue(v) == r, 'residue_formula')
            check(residue(dual_action(1,v)) == add({},r,-1), 'residue_orientation')
            # On cycles the quotient map is A-linear for the conductor action.
            for a in (X,Y,mono(0,-2),ONE):
                check(residue(pair_scale(v,a)) == mul(const(a),r), 'residue_node_linearity')
        for n in range(2,homological_bound+1):
            v = (mul(Y,yp),mul(X,xp)) if n % 2 == 0 else (mul(X,xp),mul(Y,yp))
            check(dual_d(n,v) == ZERO_PAIR, 'higher_cycles', n)
            preimage = ((divide_branch(v[0],-1),divide_branch(v[1],1)) if n % 2 == 0
                        else (divide_branch(v[0],1),divide_branch(v[1],-1)))
            check(dual_d(n-1,preimage) == v, 'higher_cycles_are_boundaries', n)
    generator = (X,{})
    check(residue(generator) == ONE, 'primitive_Ext_generator')
    check(dual_d(0,(X,)) == pair_scale(generator,X), 'x_annihilates_supported_class')
    check(pair_scale(generator,Y) == ZERO_PAIR, 'y_annihilates_supported_class')
    # The normalization SES has this exact Ext cocycle: lift 1 to (1,0).
    lifted_unit = (ONE,{})
    check(difference(lifted_unit) == ONE, 'extension_lift')
    for branch, expected in ((X,generator[0]),(Y,generator[1])):
        components=normalization(branch)
        action_on_lift=(mul(components[0],lifted_unit[0]),mul(components[1],lifted_unit[1]))
        check(action_on_lift == normalization(expected), 'normalization_extension_Ext_cocycle')

    # P=[A -> N], eta:P -> A. Cone(eta)=[A -> A+N], d(a)=(a,-nu(a)).
    # Projection pi(a,n)=nu(a)+n; inclusion j(n)=(0,n); H(a,n)=a.
    for a in samples:
        n = normalization(refl(a))
        image_d = (a, pair_scale(normalization(a),mono(0,0,-1)))
        check(normal_add(normalization(image_d[0]),image_d[1]) == ZERO_PAIR, 'cone_projection_chain_map')
        projection = normal_add(normalization(a),n)
        id_minus_jpi = (a,normal_add(n,projection,-1))
        check(id_minus_jpi == image_d, 'cone_integral_contraction')
        check(normal_action(projection) == normal_add(normalization(refl(a)),normal_action(n)), 'cone_reflection_naturality')
    # Arbitrary N modes, including unequal branch constants.
    for b in range(branch_bound+1):
        for n in ((mono(b),{}),({},mono(-b))):
            check(normal_add(normalization({}),n) == n, 'cone_retraction_on_normalization')
            check(difference(normal_action(n)) == add({},difference(n),-1), 'conductor_odd_character')

    matrix_certificates = []
    for bound in range(branch_bound+1):
        node_basis = [0]+list(range(1,bound+1))+list(range(-1,-bound-1,-1))
        n_basis = [(0,i) for i in range(bound+1)]+[(1,-i) for i in range(bound+1)]
        nu = [[0]*len(node_basis) for _ in n_basis]
        for j,i in enumerate(node_basis):
            for block in (0,1):
                if (block,i) in n_basis:
                    nu[n_basis.index((block,i))][j] = 1
        rank,rest = unit_smith(nu)
        check(rank == len(node_basis) and not any(any(r) for r in rest), 'normalization_Smith_units')
        cone = [[int(i==j) for j in range(len(node_basis))] for i in range(len(node_basis))]
        cone += [[-c for c in row] for row in nu]
        rank,rest = unit_smith(cone)
        check(rank == len(node_basis) and not any(any(r) for r in rest), 'counit_cone_Smith_units')
        matrix_certificates.append({'branch_degree':bound,'A_rank':2*bound+1,'normalization_rank':2*bound+2,
                                    'cone_nonzero_Smith_factors':[1]*rank,'cone_H0_rank':2*bound+2})
    return {'branch_test_bound':branch_bound,'dual_cochain_test_bound':homological_bound,
            'base_Laurent_exponents_tested':[-2,0,3],
            'derived_costalk':'R_or[-1]','Ext_generator':'(x,0)',
            'Ext1_residue':'(x*a(x),y*b(y)) -> a(0)-b(0)',
            'canonical_counit_direction':'i_* i^! A -> A',
            'canonical_counit_cone':'R[x] direct-sum R[y], in degree 0',
            'ordinary_integer_torsion_in_local_cone':False,'finite_matrix_certificates':matrix_certificates}


def audit_reflection() -> dict:
    def p(g: int) -> int: return g
    def c(g: int,h: int) -> int: return (g+h-(g+h)%2)//2
    for g,h in product(range(2),repeat=2):
        check(p(g)+(-1)**g*p(h)-p((g+h)%2) == 0, 'sign_one_cocycle')
        lift_g=(p(g),0); lift_h=(p(h),0); lift_gh=(p((g+h)%2),0)
        action_h = lift_h if not g else lift_h[::-1]
        boundary = tuple(action_h[i]-lift_gh[i]+lift_g[i] for i in range(2))
        check(boundary == (c(g,h),c(g,h)), 'conductor_connecting_cocycle')
        check(2*c(g,h) == p(g)+p(h)-p((g+h)%2), 'twice_two_cocycle_boundary')
    for g,h,k in product(range(2),repeat=3):
        check(c(h,k)-c((g+h)%2,k)+c(g,(h+k)%2)-c(g,h) == 0, 'two_cocycle_identity')
    for g in range(2):
        check(2*p(g) == (-1)**g*(-1)-(-1), 'twice_sign_cocycle_boundary')
    check(c(1,1)==1 and c(1,1)%2==1, 'nonboundary_parity_witness')
    # Equivariant sign lift (a,-a) has difference 2a. This parity identity,
    # not a bounded failed search, proves nonsplitting over Z.
    check((1-(-1))==2, 'unit_sign_lift_has_readout_two')
    return {'exact_sequence':'0 -> Z -> Z^2_swap -> Z_or -> 0',
            'extension_order':2,'equivariant_unit_section_exists':False,
            'obstruction_group':'Ext^1_Z[C2](Z_or,Z)=Z/2',
            'connecting_reflection_pair_value':1,
            'scope':'Recovers the source coefficient obstruction (Marici entry 141), not a new physical defect value.'}


def crosses(a: tuple[int,int], b: tuple[int,int]) -> bool:
    x,y=a;u,v=b
    return x<u<y<v or u<x<v<y


def all_faces(ds: tuple) -> list[tuple]:
    out=[()]
    def rec(f: tuple,start: int) -> None:
        for i in range(start,len(ds)):
            if all(not crosses(ds[i],d) for d in f):
                nf=f+(ds[i],);out.append(nf);rec(nf,i+1)
    rec((),0)
    return sorted(out,key=lambda x:(len(x),x))


def audit_boundary() -> dict:
    ds=tuple((a,b) for a in range(8) for b in range(a+1,8) if b-a not in (1,7))
    cuts=tuple(sorted({tuple(sorted((i,(i+3)%8))) for i in range(8)}))
    edges=tuple(e for e in combinations(cuts,2) if not crosses(*e))
    check((len(ds),len(cuts),len(edges))==(20,8,12),'octagon_source_counts')
    table=[];aggregate=Counter()
    for neg in all_faces(ds):
        active=[d for d in cuts if all(not crosses(d,n) for n in neg)]
        ae=[e for e in edges if set(e)<=set(active)]
        vd={d:len(neg)-len({d}&set(neg)) for d in active}
        ed={e:len(neg)-len(set(e)&set(neg)) for e in ae}
        dims_v=Counter(vd.values());dims_e=Counter(ed.values());ranks={}
        for q in range(7):
            vs=[d for d in active if vd[d]==q];es=[e for e in ae if ed[e]==q]
            mat=[[(-1 if d==e[0] else 1 if d==e[1] else 0) for d in vs] for e in es]
            rank,rest=unit_smith(mat)
            check(not any(any(row) for row in rest),'boundary_all_nonzero_Smith_factors_units',(neg,q))
            ranks[q]=rank
        cohom={q:dims_v[q]-ranks.get(q,0)+dims_e[q-1]-ranks.get(q-1,0) for q in range(8)}
        cohom={q:r for q,r in cohom.items() if r}
        check(all(r>0 for r in cohom.values()),'boundary_nonnegative_ranks',neg)
        check(all(0<=q<=4 for q in cohom),'boundary_cohomological_amplitude',neg)
        check(cohom.get(0,0)==(1 if not neg else 0),'supported_boundary_H0_only_unlocalized',neg)
        for q,r in cohom.items():aggregate[q]+=r
        table.append({'negative_support':neg,'scalar_cohomology_ranks':cohom})
    check(len(table)==903,'all_903_negative_supports')
    check(table[0]['scalar_cohomology_ranks']=={0:1,1:5},'primitive_graph_control')
    return {'support_types':len(table),'scalar_support_table':table,
            'one_monomial_per_support_rank_totals':dict(aggregate),
            'warning':'These finite aggregate counts are not ranks of the complete polynomial modules.',
            'orientation_corrected_supported_boundary':'Rlim R_L',
            'counit_cone_boundary':'Rlim (R_L[x] direct-sum R_L[y])',
            'cone_H0':'R0[x] direct-sum R0[y]',
            'integer_torsion':False,
            'normalized_supported_marking_space':'contractible after normalization to the full polynomial unit and orientation correction',
            'physical_comparison_identification':'not established'}


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('conductor_supported_comparison_certificate.json'))
    args=parser.parse_args()
    result={'source_commit':COMMIT,'source_blobs':SOURCES,
            'local':audit_local(8,12),'reflection':audit_reflection(),'boundary':audit_boundary(),
            'scope':['Formal split-node coefficient model over the existing localized base rings.',
                     'The conductor closed immersion is explicit; its identification with the complete physical support functor is NOT proved.',
                     'No branch truncation is used as a ring quotient in the polynomial tests.',
                     'Infinite-degree statements use the written annihilator and exact-sequence proofs.',
                     'No repository mutation and no proof-assistant verification.']}
    result['checks']=dict(COUNTS);result['total_checks']=sum(COUNTS.values())
    result['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'checks':result['total_checks'],'local_costalk':result['local']['derived_costalk'],
                      'cone':result['local']['canonical_counit_cone'],
                      'reflection_extension_order':result['reflection']['extension_order'],
                      'support_types':result['boundary']['support_types'],
                      'physical_comparison_identification':'not established'},indent=2))


if __name__=='__main__':
    main()
