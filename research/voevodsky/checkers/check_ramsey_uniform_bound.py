"""Finite controls for a classical HJ-based all-pattern effective-bound proof."""
from copy import deepcopy
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from research.voevodsky.ramsey_forcing import (
    ForcingResourceError, certify_word_length, forcing_bound,
    find_certificate, line_certificate, search_word_length)
from research.voevodsky.ramsey_certificate import verify

ATTEMPT = 'research/voevodsky/contracts/ramsey-uniform-bound-attempt.v1.json'
PROOF = 'research/voevodsky/ramsey-uniform-forcing-bound-v1.md'
FIXTURE = 'research/voevodsky/results/ramsey-marked-patch-fixture-v1.json'


def oracle_lines(k, n):
    """Independent subset-of-variable-positions enumeration, not production templates."""
    words = list(product(range(k), repeat=n))
    lookup = {word: i for i, word in enumerate(words)}
    lines = []
    for size in range(1, n + 1):
        for variable in combinations(range(n), size):
            fixed = [i for i in range(n) if i not in variable]
            for letters in product(range(k), repeat=len(fixed)):
                base = dict(zip(fixed, letters))
                lines.append(tuple(lookup[tuple(letter if i in variable else base[i] for i in range(n))]
                                   for letter in range(k)))
    return words, lines


def has_line(colors, lines):
    return any(len({colors[i] for i in line}) == 1 for line in lines)


def labelled(points):
    return [{'label': str(i), 'point': list(p)} for i, p in enumerate(points)]


def lattice_instance(points, n, r, coloring):
    m = max(abs(x) for p in points for x in p)
    radius = n * m
    return {'N': radius, 'r': r, 'pattern': labelled(points),
            'coloring': [{'point': list(p), 'color': coloring(p)}
                         for p in product(range(-radius, radius + 1), repeat=3) if sum(p) % 2 == 0]}


def main():
    attempt = json.loads((ROOT / ATTEMPT).read_text(encoding='utf-8'))
    net = json.loads((ROOT / 'research/voevodsky/contracts/ramsey-tetrahedral-octahedral-conjecture-net.v1.json').read_text(encoding='utf-8'))
    node = next(n for n in net['nodes'] if n['id'] == attempt['id'])
    assert (node['scope_id'], node['statement']) == (attempt['scope_id'], attempt['statement'])
    cases = [(1, 3, 1, True), (2, 1, 1, True), (4, 1, 1, True), (6, 1, 1, True),
             (2, 2, 1, False), (2, 2, 2, True), (2, 3, 2, False), (2, 3, 3, True),
             (3, 2, 1, False), (3, 2, 2, False), (4, 2, 1, False), (4, 2, 2, False)]
    word_results = []
    for k, r, n, expected in cases:
        result = certify_word_length(k, r, n)
        assert result['forces'] is expected
        words, lines = oracle_lines(k, n)
        assert len(lines) == (k + 1) ** n - k ** n
        if not expected:
            assert len(result['counterexample']) == len(words)
            assert not has_line(result['counterexample'], lines)
        word_results.append(result)
    oracle_colorings = 0
    for k, r, n in [(2, 2, 2), (2, 3, 3)]:
        words, lines = oracle_lines(k, n)
        for colors in product(range(r), repeat=len(words)):
            assert has_line(colors, lines)
            oracle_colorings += 1
    assert oracle_colorings == 6577
    assert search_word_length(2, 2)['n'] == 2
    assert search_word_length(2, 3)['n'] == 3
    for r in range(2, 7):
        words, lines = oracle_lines(2, r - 1)
        assert not has_line([sum(word) for word in words], lines)
    binary_patterns = [[(0, 0, 0), (1, 1, 0)], [(-1, -1, 0), (1, 0, 1)]]
    lattice_cases = 0
    for pattern in binary_patterns:
        for r in range(1, 4):
            bound = forcing_bound(labelled(pattern), r)
            assert bound['B'] == r * max(abs(x) for p in pattern for x in p)
            for coefficients in product(range(r), repeat=3):
                for offset in range(r):
                    color = lambda p, c=coefficients, b=offset, r=r: (sum(x * y for x, y in zip(c, p)) + b) % r
                    instance = lattice_instance(pattern, bound['n'], r, color)
                    answer = find_certificate(instance, bound['n'])
                    assert answer is not None and verify(instance, answer['certificate']) is True
                    lattice_cases += 1
    assert lattice_cases == 196
    for name in ('tetrahedron', 'octahedron'):
        template = net['candidate_space'][name]
        bound = forcing_bound(labelled(template), 1)
        assert bound['n'] == 1
        instance = lattice_instance(template, 1, 1, lambda _: 0)
        assert find_certificate(instance, 1) is not None
    assert forcing_bound(labelled([(0, 0, 0)]), 17)['B'] == 0
    singleton = lattice_instance([(0, 0, 0)], 1, 17, lambda _: 11)
    assert find_certificate(singleton, 1)['certificate']['color'] == 11
    fixture = json.loads((ROOT / FIXTURE).read_text(encoding='utf-8'))
    projected = line_certificate(fixture['instance'], [None, None], 0)
    assert projected['certificate'] == fixture['certificate']
    assert verify(fixture['instance'], projected['certificate']) is True
    for name in ('tetrahedron', 'octahedron'):
        template = net['candidate_space'][name]
        instance = lattice_instance(template, 3, 2, lambda p: p[0] % 2)
        q = template[1][0] % 2
        assert line_certificate(instance, [None, 1, None], q)['certificate']['m'] == 2
    # Noninjective whole-word encoding is explicit; individual line images remain distinct.
    a, b = binary_patterns[0]
    assert a != b and tuple(x + y for x, y in zip(a, b)) == tuple(x + y for x, y in zip(b, a))
    rejected = []

    def reject(name, fn, error=ValueError):
        try:
            fn()
        except error:
            rejected.append(name)
        else:
            raise AssertionError('control accepted: ' + name)

    instance = fixture['instance']
    reject('no variable positions', lambda: line_certificate(instance, [0, 0], 0))
    reject('out-of-alphabet fixed letter', lambda: line_certificate(instance, [None, 4], 0))
    reject('boolean fixed letter', lambda: line_certificate(instance, [None, True], 0))
    reject('wrong homogeneous color', lambda: line_certificate(instance, [None, None], 1))
    reject('projected line outside finite region', lambda: line_certificate(instance, [None, None, None], 0))
    partial = deepcopy(instance)
    partial['coloring'].pop()
    reject('partial lattice coloring', lambda: find_certificate(partial, 2))
    reject('whole word cube outside region', lambda: find_certificate(instance, 3))
    reject('zero alphabet size', lambda: certify_word_length(0, 2, 1))
    reject('boolean color count', lambda: certify_word_length(2, True, 1))
    reject('negative word length', lambda: certify_word_length(2, 2, -1))
    reject('large finite enumeration is a resource refusal', lambda: certify_word_length(4, 2, 3), ForcingResourceError)
    refused_templates = []
    for name in ('tetrahedron', 'octahedron'):
        reject(name + ' numeric bound not fabricated after refusal',
               lambda name=name: forcing_bound(labelled(net['candidate_space'][name]), 2), ForcingResourceError)
        refused_templates.append(name)
    sources = [ATTEMPT, PROOF, FIXTURE, 'research/voevodsky/ramsey_forcing.py',
               'research/voevodsky/ramsey_certificate.py',
               'research/voevodsky/checkers/check_ramsey_uniform_bound.py']
    result = {
        'schema': 'marici.ramsey-uniform-bound.verification.v1', 'status': 'passed',
        'scope_id': attempt['scope_id'], 'outcome': '++',
        'verification_level': 'written classical Hales-Jewett-based effective-bound proof and exact finite controls; not native forcing or kernel verified',
        'bound': attempt['candidate_bound'], 'classical_dependency': attempt['termination_dependency'],
        'abstract_algorithm_total_using_classical_HJ': True,
        'classical_HJ_independently_proved_here': False,
        'word_length_cases': word_results, 'independent_word_colorings_checked': oracle_colorings,
        'two_point_affine_lattice_coloring_cases': lattice_cases,
        'one_color_tetrahedron_octahedron_cases': 2,
        'marked_patch_fixture_projection_accepted': True,
        'mixed_fixed_variable_projection_cases': 2,
        'rejected_controls': rejected,
        'practical_two_color_numeric_bounds_not_computed': refused_templates,
        'whole_word_encoder_injective': False,
        'native_forcing_derivation_proved': False,
        'root_resolved': False,
        'source_sha256': {p: sha256((ROOT / p).read_bytes()).hexdigest() for p in sources},
    }
    target = ROOT / 'research/voevodsky/results/ramsey-uniform-bound-v1.json'
    target.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k not in ('source_sha256', 'word_length_cases')}))


if __name__ == '__main__':
    main()
