"""Framed certificate action laws plus actual source subdivision covariance."""
from copy import deepcopy
from hashlib import sha256
from itertools import permutations, product
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from research.voevodsky.ramsey_certificate import verify
from research.voevodsky.ramsey_transport import (
    verify_framed, transport, check_transport, transformation, compose, inverse)

ATTEMPT = 'research/voevodsky/contracts/ramsey-reference-covariance-attempt.v1.json'
PROOF = 'research/voevodsky/ramsey-reference-covariance-v1.md'
JS = 'research/voevodsky/checkers/check_ramsey_transport_geometry.mjs'
IDENTITY = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
T = [(0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1)]
O = [(0, 0, 0), (2, 0, 0), (1, 1, 0), (1, -1, 0), (1, 0, 1), (1, 0, -1)]


def fixture(points, radius, m=1, center=(0, 0, 0), reference='full'):
    image = [tuple(center[j] + m * s[j] for j in range(3)) for s in points]
    selected = set(image)
    coloring = []
    for v in product(range(-radius, radius + 1), repeat=3):
        if sum(v) % 2:
            continue
        p = tuple(center[j] + v[j] for j in range(3))
        coloring.append({'point': list(p), 'color': 2 if p in selected else 0})
    ref = None if reference == 'none' else {'label': 'declared-frame', 'point': [center[0] + 2, center[1], center[2]],
                                          'direction': [1, 1, 0] if reference == 'full' else None}
    instance = {'N': radius, 'r': 3, 'center': list(center),
                'pattern': [{'label': str(i), 'point': list(s)} for i, s in enumerate(points)],
                'coloring': coloring, 'reference': ref}
    certificate = {'a': list(center), 'm': m, 'color': 2,
                   'image': [{'label': str(i), 'point': list(p)} for i, p in enumerate(image)]}
    return instance, certificate


def main():
    attempt = json.loads((ROOT / ATTEMPT).read_text(encoding='utf-8'))
    net = json.loads((ROOT / 'research/voevodsky/contracts/ramsey-tetrahedral-octahedral-conjecture-net.v1.json').read_text(encoding='utf-8'))
    node = next(n for n in net['nodes'] if n['id'] == attempt['id'])
    assert (node['scope_id'], node['statement']) == (attempt['scope_id'], attempt['statement'])
    matrices = [[[signs[i] if j == p[i] else 0 for j in range(3)] for i in range(3)]
                for p in permutations(range(3)) for signs in product((-1, 1), repeat=3)]
    assert len(matrices) == 48
    palettes = [list(p) for p in permutations(range(3))]
    translations = [[0, 0, 0], [2, 0, 0], [-1, 1, 0]]
    cases = [fixture(T, 1), fixture(O, 2, center=(-1, 1, 0), reference='point'),
             fixture(T, 2, m=2, center=(2, 0, 0), reference='none')]
    action_cases = inverse_cases = 0
    for instance, certificate in cases:
        before = deepcopy((instance, certificate))
        identity = transformation(IDENTITY, [0, 0, 0], [0, 1, 2])
        assert transport(instance, certificate, identity) == before
        for qi, q in enumerate(matrices):
            for b in translations:
                for pi, palette in enumerate(palettes):
                    g = transformation(q, b, palette)
                    moved, witness = transport(instance, certificate, g)
                    assert verify_framed(moved, witness) is True
                    # Independent offset oracle: recover it from the first
                    # transformed image and transformed template, not the code formula.
                    s = moved['pattern'][0]['point']
                    p = witness['image'][0]['point']
                    assert witness['a'] == [p[j] - witness['m'] * s[j] for j in range(3)]
                    assert (instance, certificate) == before
                    if pi == qi % len(palettes):
                        assert check_transport(instance, certificate, g, moved, witness) is True
                        assert transport(moved, witness, inverse(g)) == before
                        inverse_cases += 1
                    action_cases += 1
    assert action_cases == 2592 and inverse_cases == 432

    # Tiny region, but nonzero template and scale two: exercises the offset
    # correction under all 48^2 matrix compositions without a huge color table.
    group_instance, group_certificate = fixture([(2, 0, 0)], 0, m=1)
    group_certificate.update(a=[-4, 0, 0], m=2)
    group_certificate['image'][0]['point'] = [0, 0, 0]
    group_instance['coloring'][0]['color'] = 2
    assert verify_framed(group_instance, group_certificate)
    composition_cases = 0
    for i, q1 in enumerate(matrices):
        inner = transformation(q1, translations[i % 3], palettes[i % 6])
        intermediate = transport(group_instance, group_certificate, inner)
        assert compose(inverse(inner), inner) == transformation(IDENTITY, [0, 0, 0], [0, 1, 2])
        for j, q2 in enumerate(matrices):
            outer = transformation(q2, translations[(j + 1) % 3], palettes[(j + 1) % 6])
            sequential = transport(*intermediate, outer)
            direct = transport(group_instance, group_certificate, compose(outer, inner))
            assert sequential == direct
            composition_cases += 1
    assert composition_cases == 2304

    base, cert = fixture(T, 2, m=2)
    g = transformation(IDENTITY, [2, 0, 0], [1, 2, 0])
    moved, witness = transport(base, cert, g)
    assert witness['a'] == [-2, 0, 0]  # not the point g(a)=[2,0,0]
    rejected = []

    def reject(name, fn):
        try:
            fn()
        except ValueError:
            rejected.append(name)
        else:
            raise AssertionError('invalid transport accepted: ' + name)

    naive = deepcopy(witness)
    naive['a'] = [2, 0, 0]
    reject('offset transported as a point', lambda: verify_framed(moved, naive))
    wrong_region = deepcopy(moved)
    wrong_region['center'] = [0, 0, 0]
    reject('translated region reset to original center', lambda: verify_framed(wrong_region, witness))
    erased = deepcopy(moved)
    erased.pop('reference')
    reject('reference context erased', lambda: verify_framed(erased, witness))
    wrong_reference = deepcopy(moved)
    wrong_reference['reference']['point'] = [6, 0, 0]
    assert verify_framed(wrong_reference, witness)  # valid is not the specified transport
    reject('wrong valid reference accepted as same transport', lambda: check_transport(base, cert, g, wrong_reference, witness))
    wrong_direction = deepcopy(moved)
    wrong_direction['reference']['direction'] = [3, 1, 0]
    assert verify_framed(wrong_direction, witness)
    reject('direction translated like a point', lambda: check_transport(base, cert, g, wrong_direction, witness))
    wrong_label = deepcopy(moved)
    wrong_label['reference']['label'] = 'another-frame'
    reject('reference label silently changed', lambda: check_transport(base, cert, g, wrong_label, witness))
    zero_direction = deepcopy(moved)
    zero_direction['reference']['direction'] = [0, 0, 0]
    reject('zero orientation', lambda: verify_framed(zero_direction, witness))
    wrong_palette, wrong_q = deepcopy((moved, witness))
    undo = inverse(g)['colors']
    for row in wrong_palette['coloring']:
        row['color'] = undo[row['color']]
    wrong_q['color'] = undo[wrong_q['color']]
    assert verify_framed(wrong_palette, wrong_q)
    reject('valid geometry with wrong palette map', lambda: check_transport(base, cert, g, wrong_palette, wrong_q))
    reject('nonbijective palette', lambda: transformation(IDENTITY, [0, 0, 0], [0, 0, 1]))
    reject('boolean palette entry', lambda: transformation(IDENTITY, [0, 0, 0], [False, 1, 2]))
    reject('wrong palette size', lambda: transport(base, cert, transformation(IDENTITY, [0, 0, 0], [0, 1])))
    reject('odd-sum translation', lambda: transformation(IDENTITY, [1, 0, 0], [0, 1, 2]))
    reject('shear is not a signed coordinate permutation', lambda: transformation([[1, 1, 0], [0, 1, 0], [0, 0, 1]], [0, 0, 0], [0, 1, 2]))
    reject('boolean matrix entry', lambda: transformation([[True, 0, 0], [0, 1, 0], [0, 0, 1]], [0, 0, 0], [0, 1, 2]))
    partial = deepcopy(moved)
    partial['coloring'].pop()
    reject('partial moved coloring', lambda: verify_framed(partial, witness))
    odd_center = deepcopy(moved)
    odd_center['center'] = [1, 0, 0]
    reject('center outside D3', lambda: verify_framed(odd_center, witness))
    changed_image = deepcopy(witness)
    changed_image['image'][0]['label'] = 'unknown'
    reject('source vertex label changed', lambda: verify_framed(moved, changed_image))
    # Correct recentering does not recenter the template. A tempting double
    # shift is rejected by the independent original verifier.
    wrong_local = {'N': base['N'], 'r': base['r'], 'pattern': deepcopy(moved['pattern']),
                   'coloring': [{'point': [x - y for x, y in zip(row['point'], moved['center'])], 'color': row['color']} for row in moved['coloring']]}
    for row in wrong_local['pattern']:
        row['point'] = [x - y for x, y in zip(row['point'], moved['center'])]
    local_cert = deepcopy(witness)
    local_cert['a'] = [x - y for x, y in zip(witness['a'], moved['center'])]
    for row in local_cert['image']:
        row['point'] = [x - y for x, y in zip(row['point'], moved['center'])]
    reject('template incorrectly shifted during recentering', lambda: verify(wrong_local, local_cert))

    run = subprocess.run(['node', str(ROOT / JS)], cwd=ROOT, capture_output=True, text=True, check=True, timeout=90)
    assert json.loads(run.stdout)['status'] == 'passed'
    geometry_path = ROOT / 'research/voevodsky/results/ramsey-transport-geometry-v1.json'
    geometry = json.loads(geometry_path.read_text(encoding='utf-8'))
    assert (geometry['macroCarrierMatrices'], geometry['fixedSubdivisionMatrices'], geometry['subdivisionChangingMatrices']) == (48, 16, 32)
    assert (geometry['macroNeighborChecks'], geometry['primitiveNeighborChecks']) == (768, 384)
    assert not geometry['full48NativePrimitiveSymmetryClaimed'] and not geometry['nativePacketCovarianceProved']
    sources = dict(geometry['sourceHashes'])
    for relative in [ATTEMPT, PROOF, 'research/voevodsky/ramsey_transport.py',
                     'research/voevodsky/ramsey_certificate.py', 'research/voevodsky/checkers/check_ramsey_reference_covariance.py']:
        sources[relative] = sha256((ROOT / relative).read_bytes()).hexdigest()
    for relative, digest in sources.items():
        p = (ROOT / relative).resolve()
        assert p.is_relative_to(ROOT) and sha256(p.read_bytes()).hexdigest() == digest
    result = {
        'schema': 'marici.ramsey-reference-covariance.verification.v1', 'status': 'passed',
        'scope_id': attempt['scope_id'], 'outcome': '++',
        'verification_level': 'written certificate-relation action proof and exact finite/source-geometry controls; not native packet covariance or kernel verified',
        'framed_transport_cases': action_cases, 'inverse_roundtrips': inverse_cases,
        'matrix_composition_cases': composition_cases,
        'rejected_controls': rejected,
        'correct_offset_law': 'a_prime=Q*a+(1-m)*b when S_prime=Q*S+b',
        'macro_carrier_matrices': 48, 'fixed_subdivision_matrices': 16,
        'macro_neighbor_checks': 768, 'primitive_neighbor_checks': 384,
        'reference_free_unique_selector_proved': False,
        'full48_fixed_native_subdivision_covariance_proved': False,
        'native_packet_covariance_proved': False, 'root_resolved': False,
        'geometry_receipt': {'path': str(geometry_path.relative_to(ROOT)).replace('\\', '/'), 'sha256': sha256(geometry_path.read_bytes()).hexdigest()},
        'source_sha256': dict(sorted(sources.items())),
    }
    target = ROOT / 'research/voevodsky/results/ramsey-reference-covariance-v1.json'
    target.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k not in ('source_sha256', 'geometry_receipt')}))


if __name__ == '__main__':
    main()
