"""Exact regression/oracle checks for supplied certificates, not Ramsey existence."""
from copy import deepcopy
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from research.voevodsky.ramsey_certificate import CertificateError, region_size, verify

SCOPE = 'D3-labelled-homothety-verifier-v1'
IMPLEMENTATION = 'research/voevodsky/ramsey_certificate.py'
PROOF = 'research/voevodsky/ramsey-certificate-interface-v1.md'
CONTRACT = 'research/voevodsky/contracts/ramsey-tetrahedral-octahedral-conjecture-net.v1.json'
T = [(0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1)]
O = [(0, 0, 0), (2, 0, 0), (1, 1, 0), (1, -1, 0), (1, 0, 1), (1, 0, -1)]


def domain(n):
    # Independent brute-force domain oracle; no production membership helper.
    return [p for p in product(range(-n, n + 1), repeat=3) if sum(p) % 2 == 0]


def fixture(name, template, n, a=(0, 0, 0), m=1, r=2, q=0):
    image = [tuple(a[j] + m * p[j] for j in range(3)) for p in template]
    chosen = set(image)
    instance = {
        'N': n, 'r': r,
        'pattern': [{'label': str(i), 'point': list(p)} for i, p in enumerate(template)],
        'coloring': [{'point': list(p), 'color': q if p in chosen else (q + 1) % r} for p in domain(n)],
    }
    certificate = {'a': list(a), 'm': m, 'color': q,
                   'image': [{'label': str(i), 'point': list(p)} for i, p in enumerate(image)]}
    return {'name': name, 'instance': instance, 'certificate': certificate}


def main():
    net = json.loads((ROOT / CONTRACT).read_text(encoding='utf-8'))
    templates = {'tetrahedron': [list(p) for p in T], 'octahedron': [list(p) for p in O]}
    assert all(net['candidate_space'][key] == value for key, value in templates.items())
    assert next(n for n in net['nodes'] if n['id'] == 'finite-certificate-interface')['scope_id'] == SCOPE
    domain_sizes = {n: len(domain(n)) for n in range(9)}
    assert all(region_size(n) == count for n, count in domain_sizes.items())
    fixtures = [
        fixture('tetrahedron', T, 1),
        fixture('octahedron_three_colors', O, 2, r=3, q=2),
        fixture('translated_dilated_tetrahedron', T, 2, a=(-2, 0, 0), m=2),
        fixture('dilated_octahedron', O, 4, m=2),
        fixture('template_and_translation_outside_region', [(x + 100, y, z) for x, y, z in T], 1, a=(-100, 0, 0)),
        fixture('singleton_radius_zero', [(4, 0, 0)], 0, a=(-4, 0, 0), r=1),
        fixture('arbitrary_noncell_pattern', [(0, 0, 0), (2, 0, 0), (1, 1, 0)], 2),
    ]
    reordered = deepcopy(fixtures[0])
    reordered['name'] = 'reordered_records'
    for key in ('pattern', 'coloring'):
        reordered['instance'][key].reverse()
    reordered['certificate']['image'].reverse()
    fixtures.append(reordered)
    for case in fixtures:
        before = deepcopy(case)
        assert verify(case['instance'], case['certificate']) is True
        assert case == before, 'verifier mutated supplied records'

    base = fixtures[0]
    rejected = []

    def reject(name, edit, reason):
        pair = [deepcopy(base['instance']), deepcopy(base['certificate'])]
        edit(pair)
        try:
            verify(*pair)
        except CertificateError as error:
            assert str(error) == reason, (name, str(error), reason)
            rejected.append({'name': name, 'reason': reason})
        else:
            raise AssertionError('invalid certificate accepted: ' + name)

    reject('nonobject instance', lambda p: p.__setitem__(0, None), 'instance.keys')
    reject('extra instance key', lambda p: p[0].update(history=[]), 'instance.keys')
    for value in [True, -1, 1.0, '1']:
        reject('invalid radius ' + repr(value), lambda p, v=value: p[0].update(N=v), 'N.integer')
    for value in [False, 0, 2.0, '2']:
        reject('invalid color count ' + repr(value), lambda p, v=value: p[0].update(r=v), 'r.integer')
    reject('empty pattern', lambda p: p[0].update(pattern=[]), 'pattern.nonempty_list')
    reject('duplicate pattern label', lambda p: p[0]['pattern'][1].update(label='0'), 'pattern.duplicate_label')
    reject('duplicate pattern point', lambda p: p[0]['pattern'][1].update(point=[0, 0, 0]), 'pattern.duplicate_point')
    reject('empty label', lambda p: p[0]['pattern'][0].update(label=''), 'pattern.label')
    reject('noninteger pattern coordinate', lambda p: p[0]['pattern'][0].update(point=[0.0, 0, 0]), 'pattern.integer_coordinates')
    reject('boolean pattern coordinate', lambda p: p[0]['pattern'][0].update(point=[False, 0, 0]), 'pattern.integer_coordinates')
    reject('odd-sum pattern point', lambda p: p[0]['pattern'][0].update(point=[1, 0, 0]), 'pattern.lattice')
    reject('wrong coordinate dimension', lambda p: p[0]['pattern'][0].update(point=[0, 0]), 'pattern.triple')
    reject('missing coloring site', lambda p: p[0]['coloring'].pop(), 'coloring.incomplete_domain')
    reject('duplicate coloring site', lambda p: p[0]['coloring'].append(deepcopy(p[0]['coloring'][0])), 'coloring.duplicate_point')
    reject('coloring outside box', lambda p: p[0]['coloring'][0].update(point=[4, 0, 0]), 'coloring.outside_region')
    reject('coloring outside lattice', lambda p: p[0]['coloring'][0].update(point=[1, 0, 0]), 'coloring.lattice')
    reject('out-of-range input color', lambda p: p[0]['coloring'][0].update(color=2), 'coloring.color_range')
    reject('boolean input color', lambda p: p[0]['coloring'][0].update(color=True), 'coloring.color.integer')
    reject('nonobject certificate', lambda p: p.__setitem__(1, []), 'certificate.keys')
    reject('unverified native history', lambda p: p[1].update(history=[]), 'certificate.keys')
    for value in [0, -1, True, 1.0, '1']:
        reject('invalid scale ' + repr(value), lambda p, v=value: p[1].update(m=v), 'scale.integer')
    reject('odd-sum translation', lambda p: p[1].update(a=[1, 0, 0]), 'translation.lattice')
    reject('noninteger translation', lambda p: p[1].update(a=[0, 0.0, 0]), 'translation.integer_coordinates')
    reject('out-of-range certificate color', lambda p: p[1].update(color=2), 'certificate.color_range')
    reject('boolean certificate color', lambda p: p[1].update(color=False), 'certificate.color.integer')
    reject('wrong common color', lambda p: p[1].update(color=1), 'image.not_monochromatic')
    reject('empty image', lambda p: p[1].update(image=[]), 'image.nonempty_list')
    reject('missing image label', lambda p: p[1]['image'].pop(), 'image.labels')
    reject('changed image label', lambda p: p[1]['image'][0].update(label='other'), 'image.labels')
    reject('duplicate image label', lambda p: p[1]['image'][1].update(label='0'), 'image.duplicate_label')
    reject('collapsed image points', lambda p: p[1]['image'][1].update(point=[0, 0, 0]), 'image.duplicate_point')
    reject('not a common homothety', lambda p: p[1]['image'][0].update(point=[-1, -1, 0]), 'image.not_declared_homothety')

    def mixed(pair):
        for row in pair[0]['coloring']:
            if row['point'] == [0, 0, 0]:
                row['color'] = 1
    reject('one image vertex has another color', mixed, 'image.not_monochromatic')

    def outside(pair):
        pair[1]['a'] = [2, 0, 0]
        for row, p in zip(pair[1]['image'], T):
            row['point'] = [p[0] + 2, p[1], p[2]]
    reject('exact homothety outside region', outside, 'image.outside_region')

    # Full oracle comparison for all 8192 binary L_1 colorings and the four
    # admissible unit-scale translations of this fixed oriented template.
    points = domain(1)
    indices = {p: i for i, p in enumerate(points)}
    candidates = []
    for a in product((-1, 0), repeat=3):
        if sum(a) % 2:
            continue
        image = [tuple(a[j] + p[j] for j in range(3)) for p in T]
        assert set(image) <= set(points)
        for q in (0, 1):
            cert = {'a': list(a), 'm': 1, 'color': q,
                    'image': [{'label': str(i), 'point': list(p)} for i, p in enumerate(image)]}
            candidates.append((cert, [indices[p] for p in image], q))
    assert len(points) == 13 and len(candidates) == 8
    comparisons = accepted = 0
    instance = deepcopy(base['instance'])
    for bits in range(1 << len(points)):
        palette = [(bits >> i) & 1 for i in range(len(points))]
        instance['coloring'] = [{'point': list(p), 'color': palette[i]} for i, p in enumerate(points)]
        for cert, image_indices, q in candidates:
            expected = all(palette[i] == q for i in image_indices)
            try:
                actual = verify(instance, cert)
            except CertificateError:
                actual = False
            assert actual == expected, (bits, cert)
            comparisons += 1
            accepted += int(actual)
    assert comparisons == 65536
    sources = [IMPLEMENTATION, PROOF, str(Path(__file__).relative_to(ROOT)).replace('\\', '/')]
    result = {
        'schema': 'marici.ramsey-certificate-interface.verification.v1',
        'status': 'passed', 'scope_id': SCOPE, 'outcome': '++',
        'verification_level': 'written predicate proof and exact executable regressions; not kernel verified',
        'domain_count_checks': domain_sizes,
        'accepted_fixtures': fixtures,
        'rejected_controls': rejected,
        'oracle': {'binary_colorings': 8192, 'unit_scale_placements': 4,
                   'certificate_comparisons': comparisons, 'accepted': accepted},
        'template_bindings': templates,
        'source_sha256': {p: sha256((ROOT / p).read_bytes()).hexdigest() for p in sources},
        'uniform_existence_proved': False, 'native_source_admitted': False,
        'native_histories_verified': False, 'root_resolved': False,
    }
    target = ROOT / 'research/voevodsky/results/ramsey-certificate-interface-v1.json'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'status': 'passed', 'scope_id': SCOPE,
                      'accepted_fixtures': len(fixtures), 'rejected_controls': len(rejected),
                      'oracle_comparisons': comparisons, 'root_resolved': False}))


if __name__ == '__main__':
    main()
