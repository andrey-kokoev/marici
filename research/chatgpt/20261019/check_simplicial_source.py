#!/usr/bin/env python3
"""Exact finite certificates for the source-circle simplicial-group model.

Uses only the standard library. It verifies finite instances of identities,
not the Milnor realization theorem or all homotopy groups. The all-word
Moore-boundary obstruction is proved in the accompanying note; its integer
coefficient matrices are independently reconstructed here from the face maps.
"""
from __future__ import annotations

import argparse
import json
import random
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
from typing import Callable, Iterable

Word = tuple[int, ...]
Poly = dict[tuple[int, ...], int]
COUNTS: Counter[str] = Counter()


def check(name: str, value: bool) -> None:
    COUNTS[name] += 1
    if not value:
        raise AssertionError(name)


def reduce_word(letters: Iterable[int]) -> Word:
    result: list[int] = []
    for a in letters:
        if a == 0:
            continue
        if result and result[-1] == -a:
            result.pop()
        else:
            result.append(a)
    return tuple(result)


def inverse(w: Word) -> Word:
    return tuple(-a for a in reversed(w))


def multiply(*words: Word) -> Word:
    return reduce_word(a for w in words for a in w)


def commutator(a: Word, b: Word) -> Word:
    return multiply(a, b, inverse(a), inverse(b))


def word_power(w: Word, k: int) -> Word:
    v = w if k >= 0 else inverse(w)
    return multiply(*(v for _ in range(abs(k))))


def on_word(w: Word, generator_image: Callable[[int], Word]) -> Word:
    return multiply(*(generator_image(a) if a > 0 else inverse(generator_image(-a)) for a in w))


def face_generator(n: int, i: int, j: int) -> Word:
    if not (n >= 1 and 0 <= i <= n and 1 <= j <= n):
        raise ValueError((n, i, j))
    # j is the number of zero vertices in the monotone surjection [n] -> [1].
    k = j - 1 if i < j else j
    return (k,) if 1 <= k < n else ()


def degeneracy_generator(n: int, i: int, j: int) -> Word:
    if not (n >= 1 and 0 <= i <= n and 1 <= j <= n):
        raise ValueError((n, i, j))
    return (j + 1 if i < j else j,)


def face(n: int, i: int, w: Word) -> Word:
    if not (n >= 1 and 0 <= i <= n):
        raise ValueError((n, i))
    return on_word(w, lambda j: face_generator(n, i, j))


def degeneracy(n: int, i: int, w: Word) -> Word:
    if not (n >= 0 and 0 <= i <= n):
        raise ValueError((n, i))
    return on_word(w, lambda j: degeneracy_generator(n, i, j))


def exponents(w: Word, n: int) -> tuple[int, ...]:
    result = [0] * n
    for j in w:
        result[abs(j)-1] += 1 if j > 0 else -1
    return tuple(result)


def poly_multiply(a: Poly, b: Poly, degree: int = 2) -> Poly:
    result: Counter[tuple[int, ...]] = Counter()
    for u, x in a.items():
        for v, y in b.items():
            if len(u) + len(v) <= degree:
                result[u+v] += x*y
    return {m: c for m, c in result.items() if c}


def magnus2(w: Word) -> Poly:
    result: Poly = {(): 1}
    for a in w:
        j = abs(a)
        factor = {(): 1, (j,): 1} if a > 0 else {(): 1, (j,): -1, (j,j): 1}
        result = poly_multiply(result, factor)
    return result


def chi(w: Word) -> int:
    if exponents(w, 2) != (0,0):
        raise ValueError('chi is used only on the commutator subgroup of F2')
    return magnus2(w).get((1,2), 0)


def matrix_rank(a: list[list[int]], columns: int | None = None) -> int:
    if not a:
        return 0
    m = [[Fraction(x) for x in row] for row in a]
    cols = len(m[0]) if columns is None else columns
    row = 0
    for col in range(cols):
        pivot = next((r for r in range(row, len(m)) if m[r][col]), None)
        if pivot is None:
            continue
        m[row], m[pivot] = m[pivot], m[row]
        z = m[row][col]
        m[row] = [v/z for v in m[row]]
        for r in range(len(m)):
            if r != row and m[r][col]:
                z = m[r][col]
                m[r] = [v-z*w for v,w in zip(m[r], m[row])]
        row += 1
        if row == len(m):
            break
    return row


def determinant3(a: list[list[int]]) -> int:
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def simplicial_checks(max_degree: int) -> None:
    for n in range(1, max_degree+1):
        for j in range(1, n+1):
            w = (j,)
            if n >= 2:
                for a in range(n+1):
                    for b in range(a+1, n+1):
                        check('face_face', face(n-1,a,face(n,b,w)) == face(n-1,b-1,face(n,a,w)))
            for a in range(n+1):
                for b in range(a,n+1):
                    check('degeneracy_degeneracy',
                          degeneracy(n+1,a,degeneracy(n,b,w)) == degeneracy(n+1,b+1,degeneracy(n,a,w)))
            for b in range(n+1):
                for a in range(n+2):
                    lhs = face(n+1,a,degeneracy(n,b,w))
                    if a < b:
                        rhs = degeneracy(n-1,b-1,face(n,a,w))
                    elif a == b or a == b+1:
                        rhs = w
                    else:
                        rhs = degeneracy(n-1,b,face(n,a-1,w))
                    check('face_degeneracy', lhs == rhs)


def moore_project(n: int, w: Word) -> Word:
    v = w
    for i in range(n):
        correction = degeneracy(n-1,i,face(n,i,v))
        v = multiply(v, inverse(correction))
        for k in range(i+1):
            check('moore_projection_faces', face(n,k,v) == ())
    return v


def reduced_words(n: int, max_length: int) -> Iterable[Word]:
    yield ()
    last: list[Word] = [()]
    letters = tuple(range(1,n+1)) + tuple(range(-1,-n-1,-1))
    for _ in range(max_length):
        next_level = []
        for w in last:
            for a in letters:
                if not w or w[-1] != -a:
                    v = w+(a,)
                    next_level.append(v)
                    yield v
        last = next_level


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('source_closed_homotopy_results.json'))
    parser.add_argument('--max-degree', type=int, default=12)
    args = parser.parse_args()
    if not 3 <= args.max_degree <= 40:
        raise ValueError('max-degree must be between 3 and 40')
    simplicial_checks(args.max_degree)

    t = (1,)
    x, y = degeneracy(1,1,t), degeneracy(1,0,t)
    check('degree_two_names', x == (1,) and y == (2,))
    c = commutator(x,y)
    faces_c = [face(2,i,c) for i in range(3)]
    check('commutator_all_faces_trivial', faces_c == [(),(),()])
    check('commutator_nonempty_free_word', bool(c))
    check('primitive_detector', chi(c) == 1)
    for k in range(-20,21):
        check('powers_detected_integrally', chi(word_power(c,k)) == k)

    pairs = list(combinations(range(1,4),2))
    comms = [commutator((i,),(j,)) for i,j in pairs]
    face2_matrix = [[chi(face(3,i,w)) for w in comms] for i in range(4)]
    expected = [[0,0,1],[0,1,1],[1,1,0],[1,0,0]]
    check('degree_three_commutator_face_matrix', face2_matrix == expected)
    det = determinant3(face2_matrix[:3])
    check('integral_boundary_obstruction_unimodular', abs(det) == 1)

    # The same face maps force every degree-three Moore word to have zero
    # exponent vector before the class-two matrix argument applies.
    stacked = []
    for i in range(3):
        cols = [exponents(face(3,i,(j,)),2) for j in range(1,4)]
        stacked.extend([[cols[j][r] for j in range(3)] for r in range(2)])
    check('degree_three_abelian_exponents_vanish', matrix_rank(stacked) == 3)

    # Exact generators for the reverse inclusion Gamma_3(F2) <= d3(N3).
    # The normal closure of [c,x] and [c,y] is precisely Gamma_3(F2).
    boundary_seeds = [(1,3,2,-3,-1), (3,1,2,-1)]
    triple_targets = [commutator(c,x), commutator(c,y)]
    lower_central_lifts = []
    for seed, target in zip(boundary_seeds,triple_targets):
        lift = moore_project(3,seed)
        check('triple_commutator_exact_moore_lift',
              all(face(3,i,lift) == () for i in range(3))
              and face(3,3,lift) == target)
        lower_central_lifts.append({'input_word':list(seed),
                                   'moore_word':list(lift),
                                   'boundary':list(target)})

    # Finite regressions: projection produces actual nonabelian Moore words.
    samples = list(reduced_words(3,4))
    rng = random.Random(20261019)
    for _ in range(128):
        samples.append(reduce_word(rng.choice((1,2,3,-1,-2,-3)) for _ in range(14)))
    tested_boundary_count = 0
    nontrivial_boundaries = 0
    max_projected_word_length = 0
    for w in samples:
        v = moore_project(3,w)
        out = face(3,3,v)
        check('moore_boundary_is_cycle', all(face(2,i,out) == () for i in range(3)))
        check('moore_boundary_chi_zero', chi(out) == 0)
        tested_boundary_count += 1
        nontrivial_boundaries += bool(out)
        max_projected_word_length = max(max_projected_word_length,len(v))

    abelian_moore = []
    for n in range(1,args.max_degree+1):
        rows: list[list[int]] = []
        for i in range(n):
            cols = [exponents(face(n,i,(j,)),n-1) for j in range(1,n+1)]
            rows.extend([[cols[j][r] for j in range(n)] for r in range(n-1)])
        nullity = n-matrix_rank(rows)
        check('abelian_normalized_moore_rank', nullity == (1 if n == 1 else 0))
        abelian_moore.append({'degree':n,'normalized_rank':nullity})
    check('abelianization_erases_commutator', exponents(c,2) == (0,0))

    result = {
        'status':'pass',
        'model':'Milnor reduced free simplicial group on Delta[1]/boundary',
        'checks':dict(sorted(COUNTS.items())),
        'total_assertions':sum(COUNTS.values()),
        'simplicial_generator_checks_through_degree':args.max_degree,
        'degree_two_cycle':list(c),
        'cycle_faces':[list(v) for v in faces_c],
        'cycle_detector':chi(c),
        'class_two_degree_three_face_matrix':face2_matrix,
        'first_three_face_rows_determinant':det,
        'exact_lifts_of_normal_generators_for_Gamma3':lower_central_lifts,
        'tested_moore_boundaries':tested_boundary_count,
        'nonempty_boundary_words_among_tests':nontrivial_boundaries,
        'max_tested_projected_word_length':max_projected_word_length,
        'abelian_normalized_complex':abelian_moore,
        'proved_by_all_word_argument_in_note':
            'Z2 = Gamma2(F2), d3(N3) = Gamma3(F2). The two displayed exact lifts and the unimodular obstruction matrix certify both inclusions; thus pi2(G) = Z with primitive commutator generator.',
        'external_theorems_not_proved_by_script':[
            'Milnor realization |F[K]| ~ Omega Sigma |K| for connected reduced K',
            'Moore homotopy group formula',
            'Identification of a primitive pi_3(S^2) class with a Hopf map',
            'Dold-Kan/classifying-space identifications',
            'Homotopy fiber of the degree-one S^2 -> K(Z,2) class is S^3'
        ],
        'scope':'Finite exact checks and coefficient matrices. No proof-assistant compilation, no assertion that the intended T9 equals this loop model.'
    }
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
