"""Offline source-bound audit and exact rational controls, not Hodge truth.
PDF pages were located with pnpm pdf:search. Imported theorems are not certified.
"""
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]
CONTRACT = ROOT / 'research/conjecture_net/contracts/hodge-literature-boundary-audit.v1.json'
NOTE = ROOT / 'research/voevodsky/hodge-literature-boundary-audit-v1.md'
OUT = ROOT / 'research/voevodsky/results/hodge-literature-boundary-audit-v1.json'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def local(name):
    path = (ROOT / name).resolve()
    require(path.is_relative_to(ROOT), 'source path escapes repository')
    return path


def load(path):
    return json.loads(path.read_text(encoding='utf-8'))


def source_paths():
    c = load(CONTRACT)
    manifest = load(local(c['source_snapshot']))
    return {c['source_snapshot']} | {r['pdf'] for r in manifest['sources']} | {
        page['path'] for r in manifest['sources'] for page in r['pages']
    } | {r['path'] for r in manifest['search_observations']}


def validate_audit(c):
    require(c['schema'] == 'marici.hodge-literature-boundary-audit.v1' and c['node'] == 'literature-boundary-audit', 'audit identity')
    require(c['resolution_kind'] == 'dated_source_specific_boundary_audit_with_discriminant_controls', 'audit result binding')
    require(c['known_case_policy']['integral_counterexamples_are_rational_counterexamples'] is False and
            c['known_case_policy']['singular_or_nonprojective_examples_are_admitted'] is False, 'classical scope restriction')
    require(len(c['boundary']) == 7 and all(v is False for v in c['boundary'].values()), 'audit promoted to verdict')
    require(c['recommended_family'] == 'nonsplit-unitary-sixfolds', 'shortlist binding')
    require(len(c['shortlist']) == 2, 'shortlist census')
    a, b = c['shortlist']
    require((a['dimension'], a['codimension'], a['discriminant'], a['split_discriminant'], a['signature']) ==
            (6, 3, -3, -1, [3, 3]) and a['hermitian_diagonal'] == [1, 1, 1, -1, -1, -3], 'sixfold discriminant scope')
    require((b['dimension'], b['codimension'], b['discriminant'], b['split_discriminant']) == (8, 4, 1, 1), 'reserve scope')
    for f in c['shortlist']:
        require('unresolved_in_reviewed_sources' in f['status'] and f['field'] == 'Q(i)' and
                f['weil_space_dimension_Q'] == 2 and f['weil_hodge_type'] == [f['codimension']] * 2, 'unreviewed family status')


def validate_sources(c):
    manifest = load(local(c['source_snapshot']))
    require(manifest['schema'] == 'marici.hodge-literature-source-snapshot.v1', 'snapshot schema')
    records = {r['id']: r for r in manifest['sources']}
    require(set(records) == {'deligne-clay', 'markman-2502.03415v2', 'markman-2509.23403v2', 'hermitian-2609.14169v1'}, 'reviewed source census')
    for record in records.values():
        require(sha256(local(record['pdf']).read_bytes()).hexdigest() == record['sha256'], 'PDF source drift')
        require(local(record['pdf']).read_bytes().startswith(b'%PDF'), 'not a PDF')
        for page in record['pages']:
            require(sha256(local(page['path']).read_bytes()).hexdigest() == page['sha256'], 'page source drift')
    for record in manifest['search_observations']:
        require(sha256(local(record['path']).read_bytes()).hexdigest() == record['sha256'], 'query snapshot drift')
    require({q['id'] for q in c['citations']} == {'rational-target', 'divisor-boundary', 'integral-failure',
            'weil-known-cases', 'abelian-low-dimension', 'higher-genus-limit', 'maximal-degeneration-necessity', 'source-sign-slip'}, 'citation inventory')
    for quote in c['citations']:
        pages = {p['pdf_page']: p for p in records[quote['source']]['pages']}
        text = local(pages[quote['pdf_page']]['path']).read_text(encoding='utf-8')
        require(quote['quote'] in ' '.join(text.split()), 'citation does not occur: ' + quote['id'])


def multiply(a, b):
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def transpose(a):
    return list(map(list, zip(*a)))


def determinant(a):
    a = [list(map(Q, row)) for row in a]
    result = Q(1)
    for i in range(len(a)):
        pivot = next((j for j in range(i, len(a)) if a[j][i]), None)
        if pivot is None:
            return Q(0)
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            result = -result
        v = a[i][i]
        result *= v
        for j in range(i + 1, len(a)):
            scale = a[j][i] / v
            a[j] = [x - scale * y for x, y in zip(a[j], a[i])]
    return result


def weil_forms(g):
    # Re and Im of wedge_j(dx_j+i dy_j), in the fixed rational marking.
    real, imaginary = {}, {}
    for choices in product((0, 1), repeat=g):
        simplex = tuple(2 * j + bit for j, bit in enumerate(choices))
        power = sum(choices) % 4
        (real if power % 2 == 0 else imaginary)[simplex] = 1 if power < 2 else -1
    return real, imaginary


def pullback_one_plus_i(form):
    # (1+i)*dx=dx-dy and (1+i)*dy=dx+dy; wedge in factor order.
    out = Counter()
    for simplex, coefficient in form.items():
        for choices in product((0, 1), repeat=len(simplex)):
            target = tuple(2 * (index // 2) + bit for index, bit in zip(simplex, choices))
            sign = (-1) ** sum(index % 2 == 0 and bit == 1 for index, bit in zip(simplex, choices))
            out[target] += coefficient * sign
    return {s: v for s, v in out.items() if v}


def wedge(a, b):
    out = Counter()
    for x, cx in a.items():
        for y, cy in b.items():
            if set(x) & set(y):
                continue
            sign = (-1) ** sum(i > j for i in x for j in y)
            out[tuple(sorted(x + y))] += sign * cx * cy
    return {s: v for s, v in out.items() if v}


def combine(a, b, sign=1):
    out = Counter(a)
    for s, v in b.items():
        out[s] += sign * v
    return {s: v for s, v in out.items() if v}


def report():
    c = load(CONTRACT)
    validate_audit(c)
    validate_sources(c)
    # Norm obstruction's finite lemma. Its use for all rationals is proved in note.
    require([(a, b) for a, b in product(range(3), repeat=2) if (a*a + b*b) % 3 == 0] == [(0, 0)], 'mod-3 descent lemma')
    ds = c['shortlist'][0]['hermitian_diagonal']
    h = [[d if i == j else 0 for j in range(6)] for i, d in enumerate(ds)]
    require(determinant(h) == -3 and sum(d > 0 for d in ds) == 3, 'hermitian discriminant')
    # An explicit isotropic K-plane; the written determinant/norm argument excludes dimension 3.
    w = [[int(i == j or i == j + 3) for j in range(2)] for i in range(6)]
    require(multiply(multiply(transpose(w), h), w) == [[0, 0], [0, 0]], 'isotropic two-plane')
    split = [[(1 if i < 3 else -1) if i == j else 0 for j in range(6)] for i in range(6)]
    lagrangian = [[int(i == j or i == j + 3) for j in range(3)] for i in range(6)]
    require(multiply(multiply(transpose(lagrangian), split), lagrangian) == [[0]*3 for _ in range(3)] and determinant(split) == -1, 'split positive control')
    b = [[1, 2, 0], [0, 1, 1], [0, 0, 3]]
    gram = [[0]*3 + row for row in b] + [list(row) + [int(i == j)*(i+2) for j in range(3)] for i, row in enumerate(transpose(b))]
    require(determinant(gram) == -determinant(b)**2, 'Lagrangian determinant sign')
    # Special product point: integral Riemann form E, complex structure J, K action T.
    E, J, T = ([[0]*12 for _ in range(12)] for _ in range(3))
    for j, d in enumerate(ds):
        E[2*j][2*j+1], E[2*j+1][2*j] = d, -d
        T[2*j][2*j+1], T[2*j+1][2*j] = -1, 1
        sign = 1 if d > 0 else -1
        J[2*j][2*j+1], J[2*j+1][2*j] = -sign, sign
    minus_identity = [[-int(i == j) for j in range(12)] for i in range(12)]
    require(multiply(J, J) == multiply(T, T) == minus_identity and multiply(J, T) == multiply(T, J), 'complex structure')
    require(multiply(multiply(transpose(J), E), J) == E and multiply(multiply(transpose(T), E), T) == E, 'polarization compatibility')
    require(multiply(E, J) == [[abs(ds[i//2]) * int(i == j) for j in range(12)] for i in range(12)], 'Riemann positivity')
    real, imaginary = weil_forms(6)
    require(len(real) == len(imaginary) == 32 and not set(real) & set(imaginary), 'two rational determinant generators')
    require(pullback_one_plus_i(real) == {s: 8*v for s, v in imaginary.items()} and
            pullback_one_plus_i(imaginary) == {s: -8*v for s, v in real.items()}, 'Weil representation character')
    # At the special product point both Weil generators are products of rational
    # (1,1) classes, hence algebraic by the imported Lefschetz theorem.
    r, im = {(): 1}, {}
    for j in range(3):
        a, b = 2*j, 2*(j+3)
        rj, sj = {(a, b): 1, (a+1, b+1): -1}, {(a, b+1): 1, (a+1, b): 1}
        for form in (rj, sj):
            pulled = Counter()
            for pair, v in form.items():
                mapped, coefficient = [], v
                for index in pair:
                    sign = 1 if ds[index//2] > 0 else -1
                    mapped.append(index+1 if index % 2 == 0 else index-1)
                    coefficient *= -sign if index % 2 == 0 else sign
                pulled[tuple(sorted(mapped))] += coefficient * (1 if mapped[0] < mapped[1] else -1)
            require(dict(pulled) == form, 'special point divisor Hodge type')
        r, im = combine(wedge(r, rj), wedge(im, sj), -1), combine(wedge(r, sj), wedge(im, rj))
    require(r == {s: -v for s, v in real.items()} and im == {s: -v for s, v in imaginary.items()}, 'special point algebraic Weil products')
    # Balanced signature gives type (3,3) on each conjugate determinant line.
    require((sum(d > 0 for d in ds), sum(d < 0 for d in ds)) == (3, 3), 'Weil Hodge bidegree')
    checks = dict.fromkeys([
        'four_dated_pdf_sources_and_eight_exact_page_citations_bound',
        'rational_integral_and_divisor_boundaries_separated',
        'reported_abelian_low_dimensional_and_split_weil_cases_excluded',
        'introductory_sign_slip_not_used_as_theorem',
        'mod_3_descent_lemma_separates_discriminant_minus_three_from_split',
        'lagrangian_determinant_sign_and_split_positive_control_verified',
        'nonsplit_lattice_has_explicit_isotropic_two_plane',
        'special_elliptic_product_has_compatible_positive_riemann_form',
        'two_rational_weil_generators_and_exact_isogeny_character_verified',
        'special_point_weil_generators_are_products_of_divisor_hodge_classes',
    ], True)
    sources = source_paths() | {p.relative_to(ROOT).as_posix() for p in (CONTRACT, NOTE, Path(__file__).resolve())}
    return {'schema': 'marici.hodge-literature-boundary-audit-result.v1', 'passed': True, 'checks': checks,
            'resolution_kind': c['resolution_kind'], 'recommended_family': c['recommended_family'],
            'verification_level': 'Exact source hashes/quotes and finite rational lattice/exterior controls; written determinant and norm proofs. Imported geometry and reported literature theorems, not proof-assistant certification or exhaustive status review.',
            'observed_utc': load(local(c['source_snapshot']))['observed_utc'],
            'hermitian_signature': [3, 3], 'discriminant_representative': -3,
            'K_witt_index_from_written_norm_proof': 2, 'monodromy_rank_Q_upper_bound': 4,
            'weil_class_Q_dimension': 2, 'weil_generators_terms_each': 32,
            'specific_candidate_selected': False, 'specific_alpha_selected': False,
            'Hodge_proved': False, 'Hodge_refuted': False, 'nonalgebraicity_established': False,
            'global_exhaustive_literature_status_certified': False,
            'source_sha256': {name: sha256(local(name).read_bytes()).hexdigest() for name in sorted(sources)}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'source_sha256'}, indent=2))
