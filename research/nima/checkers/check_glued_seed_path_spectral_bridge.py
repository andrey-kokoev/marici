"""Full glued endpoint composition, including cross-triangle continuations.

Reuse the existing typed path-set composer. Spectral coordinates are the direct
sum of the two local three-slot decompositions, NOT the previous tensor carrier.
Numerical payloads use a declared free bilinear path-algebra extension.
"""
from itertools import product
from fractions import Fraction as F
from pathlib import Path
import json
from check_indexed_path_synthesis import compose, source, target
import check_record4_spectral_promotion as sp
import check_spectral_successor_many_many as rec
import check_spectral_invariant_path_algebra as alg


def zero(n):
    return tuple(tuple(rec.Z for _ in range(n)) for _ in range(n))


def identity(n):
    return tuple(tuple(rec.ONE if i == j else rec.Z for j in range(n)) for i in range(n))


def vector_sum(vectors, n):
    total = (rec.Z,) * n
    for vector in vectors:
        total = tuple(sp.zadd(a, b) for a, b in zip(total, vector))
    return total


def word(path):
    return tuple(edge[2] for edge in path)


def main():
    words = alg.WORDS
    labels = tuple(e for triangle in words for e in triangle)
    index = {label: i for i, label in enumerate(labels)}
    context = {label: side for side, triangle in enumerate(words) for label in triangle}
    registry = {e: (e[0], e[1]) for e in labels}
    split_registry = {e: ((context[e], s), (context[e], t)) for e, (s, t) in registry.items()}

    def primitive_paths(endpoints):
        # These are retained formal occurrences, not allocated execution IDs.
        return {((s, t, label),) for label, (s, t) in endpoints.items()}

    glued1, split1 = primitive_paths(registry), primitive_paths(split_registry)
    glued2, split2 = compose(glued1, glued1), compose(split1, split1)
    by_word = {word(p): p for p in glued2}
    split_words = {word(p) for p in split2}
    all_words = set(by_word)
    cross = all_words - split_words
    assert len(glued1) == len(split1) == 6
    assert len(glued2) == 10 and len(split2) == 6
    assert cross == {('AB', 'BA'), ('BA', 'AB'), ('CA', 'AD'), ('DB', 'BC')}
    assert all(context[a] != context[b] for a, b in cross)
    assert all(context[a] == context[b] for a, b in split_words)
    assert {(source(by_word[w]), target(by_word[w])) for w in cross} == {
        ('A', 'A'), ('B', 'B'), ('C', 'D'), ('D', 'C')}
    # The original triangles remain paths, while mixed paths are genuinely new
    # relative to the disjoint/context-separated language.
    glued3 = compose(glued2, glued1)
    assert glued3 == compose(glued1, glued2)
    assert all(triangle in {word(p) for p in glued3} for triangle in words)
    counts = []
    g, u = glued1, split1
    for length in range(1, 7):
        counts.append({'length': length, 'glued': len(g), 'unglued': len(u)})
        assert all(len(p) == length for p in g | u)
        assert {word(p) for p in u} <= {word(p) for p in g}
        assert len(u) == 6
        if length > 1:
            assert len(g) > len(u)
        # Whole retained words, not just endpoints, recover the source records.
        for p in g:
            assert all(registry[e[2]] == e[:2] for e in p)
        g, u = compose(g, glued1), compose(u, split1)

    # Existing ledger supplies all local modes plus recoverable root histories.
    ledger = sp.SpectralLedger()
    roots = tuple(ledger.record4(tuple(sp.TwoPacket(e, *registry[e]) for e in triangle)) for triangle in words)
    modes = tuple(tuple(ledger.promote(root, mode) for mode in rec.MODES) for root in roots)
    channels = tuple((side, mode) for side in range(2) for mode in rec.MODES)
    projectors = {}
    for side, family in enumerate(modes):
        for mode_record in family:
            matrix = [list(row) for row in zero(6)]
            for i, j in product(range(3), repeat=2):
                matrix[3 * side + i][3 * side + j] = mode_record.projector[i][j]
            projectors[side, mode_record.mode] = tuple(tuple(row) for row in matrix)
            assert tuple(p.label for p in ledger.deconstruct(mode_record)) == words[side]
    summed = zero(6)
    for key, P in projectors.items():
        summed = sp.zmadd(summed, P)
        assert sp.dagger(P) == P and sp.zmm(P, P) == P and sp.ztrace(P) == rec.ONE
        for other, Q in projectors.items():
            if key != other:
                assert sp.zmm(P, Q) == zero(6)
    assert summed == identity(6)
    output_words = tuple(sorted(all_words))

    def encode(vector):
        if len(vector) != 6:
            raise ValueError('Six primitive-occurrence coefficients required')
        return tuple((key, rec.apply(projectors[key], vector)) for key in channels)

    def decode(components):
        if tuple(key for key, _ in components) != channels:
            raise ValueError('Incomplete or reordered mode family')
        for key, v in components:
            if len(v) != 6 or rec.apply(projectors[key], v) != v:
                raise ValueError('Incorrect spectral component')
        return vector_sum((v for _, v in components), 6)

    def path_product(x, y):
        return tuple(sp.zmul(x[index[a]], y[index[b]]) for a, b in output_words)

    def spectral_product(x, y, same_context_only=False, same_mode_only=False):
        return vector_sum((path_product(v, w) for a, v in x for b, w in y
                           if (not same_context_only or a[0] == b[0])
                           and (not same_mode_only or a[1] == b[1])), 10)

    basis = tuple(tuple(rec.ONE if i == j else rec.Z for j in range(6)) for i in range(6))
    encoded = tuple(encode(v) for v in basis)
    primitive_products = []
    failures_same_mode = 0
    for i, j in product(range(6), repeat=2):
        direct = path_product(basis[i], basis[j])
        assert decode(encoded[i]) == basis[i] and decode(encoded[j]) == basis[j]
        assert spectral_product(encoded[i], encoded[j]) == direct
        primitive_products.append(direct)
        if spectral_product(encoded[i], encoded[j], same_mode_only=True) != direct:
            failures_same_mode += 1
    # Each admitted word is produced by one primitive basis-pair. The linear
    # extension of composition has rank ten, although a single pair x,y only
    # produces a constrained bilinear output.
    output_basis = tuple(tuple(rec.ONE if i == j else rec.Z for j in range(10)) for i in range(10))
    assert all(v in primitive_products for v in output_basis)
    assert sum(v != (rec.Z,) * 10 for v in primitive_products) == 10
    assert failures_same_mode > 0

    # Hostile at the actual seam: native word AB,BA cannot be represented by
    # disallowing cross-context spectral operand pairs. No new scalar is fitted.
    x, y = basis[index['AB']], basis[index['BA']]
    full = path_product(x, y)
    expected = tuple(rec.ONE if w == ('AB', 'BA') else rec.Z for w in output_words)
    assert full == expected
    assert spectral_product(encode(x), encode(y), same_context_only=True) == (rec.Z,) * 10
    assert spectral_product(encode(x), encode(y), same_mode_only=True) != full

    mixed = tuple((F(i - 2, 7), F(i % 3 - 1, 5)) for i in range(6))
    other = tuple((F(2 * i + 1, 11), F(i % 2, 3)) for i in range(6))
    full = path_product(mixed, other)
    assert spectral_product(encode(mixed), encode(other)) == full
    local = spectral_product(encode(mixed), encode(other), same_context_only=True)
    assert all(local[k] == full[k] for k, w in enumerate(output_words) if w in split_words)
    assert all(local[k] == rec.Z for k, w in enumerate(output_words) if w in cross)
    rec.reject(lambda: decode(encode(mixed)[:-1]))

    # Retain output coefficients by actual word and recover both primitive
    # parents/endpoint rows using the exact source registry.
    output_records = tuple((w, by_word[w], ((w[0],), (w[1],)), value) for w, value in zip(output_words, full))
    for w, p, parents, value in output_records:
        assert word(p) == w and parents[0] + parents[1] == w
        assert compose({((registry[w[0]][0], registry[w[0]][1], w[0]),)},
                       {((registry[w[1]][0], registry[w[1]][1], w[1]),)}) == {p}
        assert value == sp.zmul(mixed[index[w[0]]], other[index[w[1]]])
    # Two-step paths are NOT inputs to the existing three-packet triangle
    # promotion; no fictitious new eigenmode or 9-dimensional closure is added.
    for p in glued2:
        packets = tuple(sp.TwoPacket(e[2], e[0], e[1]) for e in p)
        rec.reject(lambda packets=packets: ledger.record4(packets))

    report = {
        'status': 'passed',
        'source_operation': 'existing endpoint pullback path composition on actual six arrows',
        'length_two_domains': {'glued': 10, 'unglued': 6, 'new_cross_context': sorted(cross)},
        'path_counts': counts,
        'spectral_input': 'six-dimensional direct sum; six rank-one local modes with history windows',
        'spectral_output': 'ten-dimensional retained length-two path coefficient carrier',
        'all_36_basis_pair_reconstruction_squares_commute': True,
        'local_only_policy_loses_cross_context_paths': True,
        'same_mode_only_policy_not_lossless': True,
        'three_slot_adapter_rejects_all_two_step_outputs': True,
        'interpretation': 'Complete local modes represent inputs losslessly if endpoint path composition is separately retained; they are not a closed successor format.',
        'assumptions': ['free complex coefficient extension of the retained path category'],
        'not_claimed': ['physical selection of a traversal schedule', 'path counts as energy or probabilities',
                        'autonomous spectral successor after composition', 'closure in the old nine-dimensional tensor carrier'],
    }
    dest = Path(__file__).resolve().parents[1] / 'results' / 'glued-seed-path-spectral-bridge.json'
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print('PASS: glued seed has 10 two-step words versus 6 unglued; four cross-context words retained.')
    print('PASS: complete local spectral modes reconstruct all 36 input-basis products into the ten-path carrier.')
    print('PASS: context-only and same-mode-only restrictions lose information; full histories remain recoverable.')
    print('BOUNDARY: existing three-slot promotion does not accept these outputs; no physical response was selected.')
    print('Report: research/nima/results/glued-seed-path-spectral-bridge.json')


if __name__ == '__main__':
    main()
