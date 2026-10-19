"""Bind both proton spin-lift candidates to the existing raw mode extension.

Reconstruct the contact model's W_p and the source rotations of its 12 triangle
records. Verify (D_g tensor U_g) W_p = W_p U_g without selecting lift signs.
"""
from contextlib import redirect_stdout
from pathlib import Path
import hashlib
import io
import json
import sys

from check_predictive_pair_proton_spin_candidates import main as candidates_main

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OWNER = ROOT / 'research/voevodsky'
sys.path.insert(0, str(OWNER / 'checkers'))
from check_proton_electron_contact_binding import (
    A, CI, S3, S5, ZERO, ONE, I, norm, mm, adj, decode_matrix)
from check_native_operation_energy_lift import geo, SOURCE, verify


def main():
    checks = []
    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    with redirect_stdout(io.StringIO()):
        candidates_main()
    candidate_path = HERE.parent / 'results/predictive-pair-proton-spin-candidates.json'
    candidates = json.loads(candidate_path.read_text())
    raw = SOURCE.read_bytes()
    source = json.loads(raw)
    certificate, _ = verify(source)
    check('source/merkle-verified', certificate['verified'])
    geometry = source['objects'][source['objects'][source['root']]['geometry']]['payload']
    placements = sorted(geometry['triangles_and_transports'], key=lambda r: r['outer_arrow'])
    points = dict(geo.POINTS)
    check('frame/candidate-and-native-agree',
          tuple(points[k] for k in 'ABCD') == tuple(map(tuple, candidates['tetrahedron_frame'])))
    for face in ('ABC', 'ABD', 'ACD', 'BCD'):
        points['F_' + face] = geo.mean([points[k] for k in face])
    v = []
    for row in placements:
        f, a, b = (points[k] for k in row['triangle'])
        v.extend(A(f[j]) - A(a[j] + b[j])/2 + CI*S3*A(a[j] - b[j])/2 for j in range(3))
    check('embedding/contact-native-norm', len(v) == 36 and norm(v) == 80)
    v = tuple(x/(4*S5) for x in v)
    w = tuple(tuple(v[i]*A(s == j) for j in range(2)) for i in range(36) for s in range(2))
    check('embedding/72-row-isometry', len(w) == 72 and mm(adj(w), w) == I)
    rotations = [tuple(tuple(geo.F(x) for x in row) for row in p['rotation']) for p in placements]
    check('source/12-distinct-triangle-frames', len(rotations) == len(set(rotations)) == 12)
    variants = []
    for generator in candidates['generators']:
        index = generator['source_generator']
        permutation = tuple('ABCD'.index(label) for label in generator['vertex_permutation'])
        rotation = geo.rotation(permutation)
        destinations = tuple(rotations.index(geo.mm(rotation, r)) for r in rotations)
        check(f'raw/record-permutation/{index}', sorted(destinations) == list(range(12)))
        check(f'raw/spatial-orthogonal/{index}',
              geo.mm(geo.transpose(rotation), rotation) ==
              tuple(tuple(geo.F(i == j) for j in range(3)) for i in range(3)))
        # Same block action D_g as the existing native-operation energy checker.
        entries = [(3*dest+a, 3*t+b, A(rotation[a][b]))
                   for t,dest in enumerate(destinations) for a in range(3) for b in range(3)
                   if rotation[a][b]]
        moved = [ZERO]*36
        for i,j,value in entries:
            moved[i] += value*v[j]
        check(f'raw/retained-mode-invariant/{index}', tuple(moved) == v)
        for candidate in generator['candidates']:
            u = decode_matrix(candidate['matrix'])
            tag = f'{index}/{candidate["third_power"]}'
            # Sparse D_g tensor U_g acting on the full encoding, not only one
            # prepared logical vector. Each of W's two columns is checked.
            advanced = [[ZERO]*2 for _ in range(72)]
            for i,j,value in entries:
                for a in range(2):
                    for b in range(2):
                        for column in range(2):
                            advanced[2*i+a][column] += value*u[a][b]*w[2*j+b][column]
            advanced = tuple(map(tuple, advanced))
            check('binding/full-encoding-intertwiner/' + tag, advanced == mm(w, u))
            check('binding/recovered-logical-action/' + tag, mm(adj(w), advanced) == u)
            check('binding/encoded-metric-preserved/' + tag, mm(adj(advanced), advanced) == I)
            for arrow in generator['moving_correspondences']:
                check('binding/arrow/' + tag + '/' + arrow, advanced == mm(w, u))
            variants.append({'generator': index, 'arrows': generator['moving_correspondences'],
                             'third_power': candidate['third_power'],
                             'logical_action': candidate['matrix'],
                             'record_destinations': destinations})
    check('source/unchanged', SOURCE.read_bytes() == raw)
    files = [Path(__file__), SOURCE, candidate_path,
             OWNER / 'checkers/check_native_operation_energy_lift.py',
             OWNER / 'checkers/check_proton_electron_contact_binding.py']
    report = {'schema': 'marici.nima.predictive-pair-proton-spin-binding.v1',
              'verification_status': 'pass', 'binding_status': 'all-candidate-intertwiners-bound',
              'checks': checks, 'raw_dimension': 72, 'logical_dimension': 2, 'variants': variants,
              'law': '(D_g tensor U_g) W_p = W_p U_g',
              'scope': 'Existing 36-row native rotation with the declared spin extension. '
                       'Both signs verified, neither selected. No joint frame, preparation, '
                       'contact update, mediator dynamics or admission policy inferred.',
              'input_sha256': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in files}}
    output = HERE.parent / 'results/predictive-pair-proton-spin-binding.json'
    output.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(f'PASS: {len(checks)} exact proton raw-spin binding checks')
    print('All six requests intertwine the actual 72-row encoding for both lift signs.')
    print('Remaining: joint spin-frame/preparation and contact/mediator request semantics.')


if __name__ == '__main__':
    main()
