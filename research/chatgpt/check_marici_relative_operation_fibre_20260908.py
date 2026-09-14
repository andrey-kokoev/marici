#!/usr/bin/env python3
"""Integral finite audit of the native mixed-operation homotopy fibre.

No network, external package, repository modification, or numerical rank tests.
The all-degree conclusions use the explicit proofs and the stated flag-complex
presentation theorem, not extrapolation from the finite verification window.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations, product
from math import comb
from pathlib import Path
import hashlib
import json

CHECKS: Counter[str] = Counter()
PLUS = (0, 1, 2)
MINUS = (3, 4, 5)
LABELS = ((1, 3), (1, 5), (3, 5), (0, 2), (0, 4), (2, 4))
NAMES = ('xi13', 'xi15', 'xi35', 'eta02', 'eta04', 'eta24')
Word = tuple[tuple[int, ...], ...]
Poly = dict[Word, int]


def check(value: bool, kind: str, detail=None) -> None:
    if not value:
        raise AssertionError((kind, detail))
    CHECKS[kind] += 1


def pm(n: int) -> int:
    return -1 if n % 2 else 1


def put(d: dict, key, value: int) -> None:
    if value:
        d[key] = d.get(key, 0) + value
        if not d[key]:
            del d[key]


def add(*ds: dict) -> dict:
    out = {}
    for d in ds:
        for key, value in d.items():
            put(out, key, value)
    return out


def scale(d: dict, c: int) -> dict:
    return {key: value*c for key, value in d.items() if value*c}


def subsets(items: tuple[int, ...]):
    for k in range(len(items)+1):
        yield from combinations(items, k)


def sign(seq: tuple[int, ...]) -> int:
    return pm(sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i+1, len(seq))))


def sheet(i: int) -> int:
    return 0 if i < 3 else 1


def flat(w: Word) -> tuple[int, ...]:
    return tuple(i for block in w for i in block)


def degree(w: Word) -> int:
    return sum(map(len, w))


def monomial(seq: tuple[int, ...]) -> Poly:
    """Normal form in the free product of the two exterior algebras."""
    blocks = []
    coefficient = 1
    start = 0
    while start < len(seq):
        end = start+1
        while end < len(seq) and sheet(seq[end]) == sheet(seq[start]):
            end += 1
        run = seq[start:end]
        if len(set(run)) != len(run):
            return {}
        coefficient *= sign(run)
        blocks.append(tuple(sorted(run)))
        start = end
    return {tuple(blocks): coefficient}


def mul(a: Poly, b: Poly) -> Poly:
    out = {}
    for w, aw in a.items():
        for v, bv in b.items():
            for t, c in monomial(flat(w)+flat(v)).items():
                put(out, t, aw*bv*c)
    return out


def bracket(a: Poly, b: Poly) -> Poly:
    if not a or not b:
        return {}
    p = degree(next(iter(a)))
    q = degree(next(iter(b)))
    return add(mul(a, b), scale(mul(b, a), -pm(p*q)))


def exterior_image(a: Poly) -> dict:
    out = {}
    for w, c in a.items():
        seq = flat(w)
        if len(set(seq)) == len(seq):
            put(out, tuple(sorted(seq)), c*sign(seq))
    return out


@lru_cache(None)
def words(n: int, first: int = -1) -> tuple[Word, ...]:
    if n == 0:
        return ((),)
    ans = []
    for s in (0, 1):
        if first >= 0 and first != s:
            continue
        for k in range(1, min(3, n)+1):
            for block in combinations(PLUS if s == 0 else MINUS, k):
                ans.extend((block,)+w for w in words(n-k, 1-s))
    return tuple(ans)


def md(w: Word) -> tuple[int, ...]:
    seq = flat(w)
    return tuple(seq.count(i) for i in range(6))


MIXED = tuple(J for J in subsets(tuple(range(6)))
              if any(i < 3 for i in J) and any(i >= 3 for i in J))


@lru_cache(None)
def generator(J: tuple[int, ...]) -> Poly:
    """Nested-commutator representative with minimum positive label as root."""
    root = min(i for i in J if i < 3)
    out = {((root,),): 1}
    for i in reversed(tuple(j for j in J if j != root)):
        out = bracket({((i,),): 1}, out)
    return out


@lru_cache(None)
def tensor_words(n: int):
    if n == 0:
        return ((),)
    return tuple((J,)+w for J in MIXED if len(J) <= n for w in tensor_words(n-len(J)))


@lru_cache(None)
def tensor_image(w) -> Poly:
    if not w:
        return {(): 1}
    return mul(generator(w[0]), tensor_image(w[1:]))


def factor_md(w, E):
    seq = tuple(i for J in w for i in J)+E
    return tuple(seq.count(i) for i in range(6))


def factor_images(n: int):
    for k in range(min(6, n)+1):
        for E in combinations(range(6), k):
            for w in tensor_words(n-k):
                yield (w, E), mul(tensor_image(w), monomial(E))


@lru_cache(None)
def grouped_factor_images(n: int):
    groups = defaultdict(list)
    for label, value in factor_images(n):
        groups[factor_md(*label)].append((label,value))
    return dict(groups)


@lru_cache(None)
def reduction_table(n: int, multidegree: tuple[int, ...]):
    """Unimodular column elimination, recording inverse coordinates."""
    rows = {}
    for label, value in grouped_factor_images(n).get(multidegree, ()):
        v = dict(value)
        coord = {label: 1}
        while v:
            pivot = min(v)
            a = v[pivot]
            if pivot not in rows:
                check(abs(a) == 1, 'unit_pivot', (n, multidegree, pivot, a))
                rows[pivot] = (scale(v, a), scale(coord, a))
                break
            row, old_coord = rows[pivot]
            v = add(v, scale(row, -a))
            coord = add(coord, scale(old_coord, -a))
        check(bool(v), 'factor_column_independent', (n, label))
    return rows


def decode(v: Poly) -> dict:
    if not v:
        return {}
    first = next(iter(v))
    rows = reduction_table(degree(first), md(first))
    remaining = dict(v)
    out = {}
    while remaining:
        pivot = min(remaining)
        a = remaining[pivot]
        check(pivot in rows, 'factor_decomposition_exists', pivot)
        row, coord = rows[pivot]
        remaining = add(remaining, scale(row, -a))
        out = add(out, scale(coord, a))
    return out


def encode(v: dict) -> Poly:
    out = {}
    for (w, E), a in v.items():
        out = add(out, scale(mul(tensor_image(w), monomial(E)), a))
    return out


def coproduct(a: Poly) -> dict:
    """Graded coproduct with each degree-one occurrence primitive."""
    out = {}
    for w, c in a.items():
        seq = flat(w)
        for mask in range(1 << len(seq)):
            left = tuple(seq[k] for k in range(len(seq)) if (mask >> k) & 1)
            right = tuple(seq[k] for k in range(len(seq)) if not (mask >> k) & 1)
            inversions = sum(not ((mask >> i) & 1) and ((mask >> j) & 1)
                             for i in range(len(seq)) for j in range(i+1, len(seq)))
            for l, al in monomial(left).items():
                for r, ar in monomial(right).items():
                    put(out, (l, r), c*al*ar*pm(inversions))
    return out


def act(a: Poly, permutation: tuple[int, ...]) -> Poly:
    out = {}
    for w, c in a.items():
        out = add(out, scale(monomial(tuple(permutation[i] for i in flat(w))), c))
    return out


def dihedral():
    ans = []
    for r, reflect in product(range(3), (False, True)):
        p = []
        for a, b in LABELS:
            image = tuple(sorted((((1-a if reflect else a)+2*r) % 6,
                                  ((1-b if reflect else b)+2*r) % 6)))
            p.append(LABELS.index(image))
        ans.append(tuple(p))
    return tuple(ans)


def face(D: tuple[int, ...]) -> bool:
    return not D or all(i < 3 for i in D) or all(i >= 3 for i in D)


def cells():
    """Product CW cells: J=nonbase coordinates; D=disk coordinates."""
    return tuple((J, D) for J in subsets(tuple(range(6))) for D in subsets(J) if face(D))


def cell_d(cell):
    J, D = cell
    return {(J, tuple(j for j in D if j != i)): pm(J.index(i)-D.index(i)) for i in D}


def apply(table, v: dict):
    out = {}
    for key, value in v.items():
        out = add(out, scale(table.get(key, {}), value))
    return out


def alpha(J, D):
    return pm(sum(J.index(i) for i in D))


def contraction(cell):
    J, D = cell
    if not J:
        return {}
    if not D:
        ref = min(i for i in J if i >= 3) if any(i >= 3 for i in J) else min(J)
        return {(J, (ref,)): alpha(J, (ref,))}
    root = min(i for i in J if sheet(i) == sheet(D[0]))
    if root in D:
        return {}
    enlarged = tuple(sorted(D+(root,)))
    return {(J, enlarged): alpha(J, D)*alpha(J, enlarged)}


def homology_projection(cell):
    J, D = cell
    if not J:
        return {(): 1}
    if J in MIXED and len(D) == 1 and D[0] < 3:
        return {J: alpha(J, D)}
    return {}


def homology_inclusion(J):
    if not J:
        return {((), ()): 1}
    a = min(i for i in J if i < 3)
    b = min(i for i in J if i >= 3)
    return {(J, (a,)): alpha(J, (a,)), (J, (b,)): -alpha(J, (b,))}


def cell_action(cell, permutation):
    J, D = cell
    image_J = tuple(sorted(permutation[i] for i in J))
    image_D = tuple(sorted(permutation[i] for i in D))
    # Only swapping two odd-dimensional circle coordinates changes product orientation.
    circle = tuple(i for i in J if i not in D)
    s = sign(tuple(permutation[i] for i in circle))
    return {(image_J, image_D): s}


def record_poly(a):
    return [{'word': [[NAMES[i] for i in block] for block in w], 'coefficient': c}
            for w, c in sorted(a.items())]


def record_relative(a):
    return [{'factors': [[NAMES[i] for i in J] for J in w],
             'exterior_tail': [NAMES[i] for i in E], 'coefficient': c}
            for (w, E), c in sorted(a.items())]


def main(output: Path, max_degree: int) -> None:
    if not 2 <= max_degree <= 7:
        raise ValueError('--max-degree must lie between 2 and 7')
    permutations = dihedral()
    all_cells = cells()
    d = {c: cell_d(c) for c in all_cells}
    h = {c: contraction(c) for c in all_cells}
    p = {c: homology_projection(c) for c in all_cells}
    inclusion = {J: homology_inclusion(J) for J in ((),)+MIXED}
    check(len(all_cells) == 368, 'moment_angle_cell_count')
    check(Counter(map(len, MIXED)) == {2:9, 3:18, 4:15, 5:6, 6:1}, 'generator_census')
    for c in all_cells:
        check(not apply(d, d[c]), 'cell_d_squared', c)
        lhs = add(apply(d, h[c]), apply(h, d[c]))
        rhs = add({c:1}, scale(apply(inclusion, p[c]), -1))
        check(lhs == rhs, 'integral_cell_contraction', c)
        check(not apply(p, d[c]), 'homology_projection_chain_map', c)
    for J, v in inclusion.items():
        check(not apply(d, v), 'explicit_mixed_cycle', J)
        check(apply(p, v) == {J:1}, 'primitive_cycle_coordinate', J)
    for permutation in permutations:
        action = {c:cell_action(c, permutation) for c in all_cells}
        for c in all_cells:
            check(apply(d, action[c]) == apply(action, d[c]), 'dihedral_cell_chain_map', (c,permutation))
        for J in MIXED:
            image = apply(p, apply(action, inclusion[J]))
            Jnew = tuple(sorted(permutation[i] for i in J))
            # Product-CW convention differs from nested-commutator convention by
            # an explicit degree/sign rebase. Record the computed action, not an
            # assumed global equivariant wedge splitting.
            check(len(image) == 1 and Jnew in image and abs(image[Jnew]) == 1,
                  'dihedral_mixed_cycle_orientation', (J,permutation,image))
            expected_sign = sign(tuple(permutation[i] for i in J))*(-1 if permutation[0] >= 3 else 1)
            check(image[Jnew] == expected_sign, 'cell_and_operation_orientation_match', (J,permutation))

    generator_records = []
    for J in MIXED:
        g = generator(J)
        check(bool(g), 'relative_generator_nonzero', J)
        check(not exterior_image(g), 'relative_generator_maps_zero', J)
        expected = {}
        for w, c in g.items():
            put(expected, (w,()), c); put(expected, ((),w), c)
        check(coproduct(g) == expected, 'relative_generator_primitive', J)
        generator_records.append({'support':[NAMES[i] for i in J], 'degree':len(J),
                                  'native_word_expansion':record_poly(g)})

    factor_table = []
    for n in range(max_degree+1):
        native = words(n)
        mds = sorted(set(md(w) for w in native))
        total_rank = 0
        for k in mds:
            rows = reduction_table(n,k)
            expected = sum(md(w) == k for w in native)
            check(len(rows) == expected, 'full_integral_factor_rank', (n,k))
            total_rank += len(rows)
        check(total_rank == len(native), 'all_native_words_factored', n)
        factor_table.append({'degree':n,'native_rank':len(native),
                             'relative_tensor_rank':len(tensor_words(n)),
                             'full_factor_rank':total_rank})

    action_records = []
    for permutation in permutations:
        for J in MIXED:
            g_image = act(generator(J),permutation)
            coordinates = decode(g_image)
            check(encode(coordinates) == g_image, 'relative_action_reconstructs', (J,permutation))
            check(all(not E for w,E in coordinates), 'relative_action_has_no_exterior_tail', (J,permutation))
            Jnew = tuple(sorted(permutation[i] for i in J))
            expected_sign = sign(tuple(permutation[i] for i in J))*(-1 if permutation[0] >= 3 else 1)
            check(coordinates.get(((Jnew,),()),0) == expected_sign,
                  'relative_indecomposable_action', (J,permutation))
            action_records.append({'permutation':list(permutation),'support':list(J),
                                   'relative_expression':record_relative(coordinates)})
    for p1,p2 in product(permutations,repeat=2):
        composition = tuple(p1[p2[i]] for i in range(6))
        check(composition in permutations, 'source_group_closed')
        for J in MIXED:
            check(act(act(generator(J),p2),p1) == act(generator(J),composition),
                  'exact_dihedral_composition', (J,p1,p2))

    reflection = permutations[1]
    J = (0,1,3,4)
    expected = add(scale(generator(J),-1), bracket(generator((1,3)),generator((0,4))))
    check(act(generator(J),reflection) == expected, 'reflection_has_quadratic_correction')
    check(bool(bracket(generator((1,3)),generator((0,4)))), 'reflection_correction_nonzero')

    endpoint_records = []
    for i,j in product(PLUS,MINUS):
        g = generator((i,j))
        for last in (i,j):
            result = mul(g, {((last,),):1})
            expected = {((last,),(j if last==i else i,),(last,)):1}
            check(result == expected, 'mixed_operation_on_endpoint_channel', (i,j,last))
            check(all(sheet(w[-1][-1]) == sheet(last) for w in result), 'endpoint_label_retained')
            check(not exterior_image(result), 'endpoint_action_lost_in_exterior_quotient')
            endpoint_records.append({'generator':[NAMES[i],NAMES[j]],'channel_seed':NAMES[last],
                                     'nonzero_result':record_poly(result)})

    basics = tuple((i,j) for i in PLUS for j in MINUS)
    bracket_pivots = {}
    for a,b in combinations(basics,2):
        result = bracket(generator(a),generator(b))
        check(bool(result), 'nonlinear_whitehead_detector_nonzero', (a,b))
        decoded = decode(result)
        expected = {((a,b),()):1, ((b,a),()):-1}
        check(decoded == expected, 'whitehead_primitive_word_coordinates', (a,b))
        bracket_pivots[(a,b)] = decoded
    check(len(bracket_pivots)==36, 'whitehead_detector_rank_36')

    # Independent all-degree rank recurrence, up to a finite audit window.
    tensor_ranks=[1]
    gcounts={2:9,3:18,4:15,5:6,6:1}
    native_ranks=[]
    for n in range(21):
        if n:
            tensor_ranks.append(sum(c*tensor_ranks[n-d] for d,c in gcounts.items() if d<=n))
        numerator=comb(3,n) if n<=3 else 0
        native_ranks.append(numerator+sum(c*native_ranks[n-d] for d,c in ((1,3),(2,3),(3,1)) if d<=n))
        factored=sum(comb(6,k)*tensor_ranks[n-k] for k in range(min(6,n)+1))
        check(factored==native_ranks[n], 'independent_hilbert_identity', n)
    for n in range(max_degree+1):
        check(native_ranks[n]==len(words(n)), 'native_recurrence_matches_words', n)
        check(tensor_ranks[n]==len(tensor_words(n)), 'relative_recurrence_matches_words', n)

    output_data={
      'status':'explicit_coefficient_operation_fibre_and_nonlinear_realization',
      'date':'2026-09-08',
      'source_commit':'d1947b67a60d3e88ba77f4ca60ea02c2a306ee61',
      'complex':'two disjoint filled 2-simplices on the two occurrence triples',
      'native_ring':'C[x1,x2,x3,y1,y2,y3]/(xi*yj)',
      'topological_realization':{
          'DJ':'BT3 wedge BT3', 'base':'BT6',
          'moment_angle_fibre':'(D2)^3 x T3 union T3 x (D2)^3',
          'homotopy_type':'Sigma(T3 smash T3)',
          'sphere_multiplicities':{'3':9,'4':18,'5':15,'6':6,'7':1},
          'cell_count':len(all_cells),
          'cell_ranks':dict(sorted(Counter(len(J)+len(D) for J,D in all_cells).items())),
          'nonlinear_whitehead_free_subgroup_pi5_rank':36,
          'linear_hurewicz_kills_these_36':True,
      },
      'relative_hopf_subalgebra':{
          'definition':'{h: (id tensor rho)Delta(h)=h tensor 1}',
          'algebra':'free associative algebra on 49 displayed primitive generators',
          'generator_degrees':gcounts,
          'ordinary_kernel_is_not_this_unital_subalgebra':True,
          'ordinary_kernel':'two-sided ideal generated by its positive-degree part; already generated as an ideal by nine quadratic commutators',
          'hilbert_series':'1/(1-9*z^2-18*z^3-15*z^4-6*z^5-z^6)',
          'factorization':'native Yoneda algebra = relative algebra tensor exterior-six as graded modules; not an algebra tensor product',
      },
      'explicit_generators':generator_records,
      'factor_rank_table':factor_table,
      'exact_dihedral_generator_actions':action_records,
      'endpoint_action_witnesses':endpoint_records,
      'source_dihedral_permutations':[list(p) for p in permutations],
      'checks':dict(sorted(CHECKS.items())),
      'exact_assertions':sum(CHECKS.values()),
      'finite_word_factor_window':max_degree,
      'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'scope':[
          'The topological coefficient realization is canonical from the labelled simplicial complex. It is not identified with the physical source or the previous additive Tor-cone infinity-groupoid.',
          'The 368 cells belong to this separate coefficient realization; no cells are added to the 215-state physical target.',
          'No conormal factor, Rees parameter, endpoint gluing class, or physical Q-connector is changed.',
          'All-degree freeness uses the explicit induced-subcomplex calculation and Vylegzhanin Theorem 1.1; finite factor tests independently verify the stated window.',
          'The wedge decomposition is an ordinary homotopy equivalence; no equivariant wedge splitting is asserted.',
          'Primitive nested-commutator signs and actual source dihedral transformations are retained. They need decomposable corrections beyond signed permutation of indecomposables.',
          'No new prime torsion or RH criterion is asserted.',
      ],
    }
    output.write_text(json.dumps(output_data,indent=2)+'\n')
    print(json.dumps({k:output_data[k] for k in ('status','exact_assertions','factor_rank_table','topological_realization')},indent=2))


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('marici_relative_operation_fibre_certificate_20260908.json'))
    parser.add_argument('--max-degree',type=int,default=6)
    args=parser.parse_args()
    main(args.output,args.max_degree)
