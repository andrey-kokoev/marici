"""Declared Q^2 loom prototype: exact tetrahedral surface-weight obstruction.

No face weight, flat-filling requirement or particle assignment is inferred.
"""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
from itertools import product
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve()
FIXTURE = ROOT / 'research/strominger/inputs/fiber-loom-tetrahedron-v1.json'
PACKET = ROOT / 'research/strominger/fiber-loom-tetrahedron.md'
MODEL = ROOT / 'research/strominger/scc-models/fiber-loom-tetrahedron-v1.json'
BASE = HERE.with_name('check_carrier_particle_circuits.py')
COMPILER = ROOT / 'research/aspect/scc/categorical_compiler.py'
OUT = ROOT / 'research/strominger/results/fiber-loom-tetrahedron'


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


base, compiler = load('loom_matrix_base', BASE), load('loom_scc', COMPILER)
I = [[1, 0], [0, 1]]
ZERO = [[0, 0], [0, 0]]


def minus(a, b):
    return [[x - y for x, y in zip(r, s)] for r, s in zip(a, b)]


def digest(value):
    return sha256(json.dumps(value, sort_keys=True, default=str).encode()).hexdigest()


def diagram(name, left, right, rank, required=True):
    return {'id': name, 'objects': [{'id': 'Q2_surface_state'}],
        'arrows': [{'id': side, 'source': 'Q2_surface_state', 'target': 'Q2_surface_state',
                    'evaluated_map': value, 'map_token': digest(value)} for side, value in (('left', left), ('right', right))],
        'cells': [{'id': 'required_filling', 'kind': 'evaluated_surface_composite_equality', 'routes': [['left'], ['right']], 'threshold': 'exact_zero'}] if required else [],
        'obstructions': [], 'claims': [],
        'higher_coherence': [{'id': 'tetrahedral_filling', 'degree': 3,
            'state': 'verified' if rank == 0 else 'falsified',
            'witness': {'kind': 'owner_computed_surface_weight_residual', 'matrix': minus(left, right), 'rank': rank}}] if required else [],
        'scope': 'Declared abelian surface-weight realization only; no native higher morphism or P/N/E admission'}


def run(report):
    f = json.loads(FIXTURE.read_text(encoding='utf-8'))
    checks = report['checks']

    def check(name, value):
        checks[name] = bool(value)
        if not value:
            raise AssertionError(name)

    group = f['allowed_face_comparisons']
    names, faces, edges = list(group), f['faces'], f['edges']
    key = lambda matrix: tuple(tuple(row) for row in matrix)
    by_matrix = {key(value): name for name, value in group.items()}
    table = {(a, b): by_matrix[key(base.mm(group[a], group[b]))] for a in names for b in names}

    def multiply(*values):
        result = 'I'
        for value in values:
            result = table[result, value]
        return result

    check('all_edge_transports_invertible', base.rank(f['edge_transport']) == 2)
    check('all_allowed_face_maps_invertible_orthogonal_involutions', all(
        base.rank(value) == 2 and base.mm(base.transpose(value), value) == I and base.mm(value, value) == I for value in group.values()))
    check('surface_comparison_group_abelian', all(table[a, b] == table[b, a] for a in names for b in names))
    filling = f['mandatory_filling']

    def evaluate(face_names):
        left = group[multiply(*(face_names[face] for face in filling['left']))]
        right = group[multiply(*(face_names[face] for face in filling['right']))]
        defect = minus(left, right)
        rank = base.rank(defect)
        basis = [[int(i == j) for i in range(2)] for j in range(2) if left[j][j] == right[j][j]]
        holonomy = multiply(*(face_names[face] for face in filling['right']), *(face_names[face] for face in filling['left']))
        return {'face_names': face_names, 'left': left, 'right': right, 'defect': defect,
                'defect_rank': rank, 'admissible_dimension': 2 - rank,
                'admissible_basis': basis, 'holonomy': holonomy}

    census = [evaluate(dict(zip(faces, choice))) for choice in product(names, repeat=4)]
    distribution = Counter(str(case['admissible_dimension']) for case in census)
    check('all_256_assignments_match_predicted_census', len(census) == 256 and dict(distribution) == f['predictions']['all_256_face_assignments_by_admissible_dimension'])
    check('independent_character_count_matches_matrix_rank_in_every_case', all(
        len(case['admissible_basis']) == case['admissible_dimension'] and
        all(base.mv(case['defect'], v) == [0, 0] for v in case['admissible_basis']) for case in census))
    S, inverse = [[Q(1), Q(1)], [Q(0), Q(1)]], [[Q(1), Q(-1)], [Q(0), Q(1)]]
    metric = base.mm(base.transpose(inverse), inverse)
    check('basis_control_is_invertible', base.mm(S, inverse) == I)
    outcomes = {}
    for name, face_names in f['named_cases'].items():
        case = evaluate(face_names)
        check(name + '_predicted_admissible_dimension', case['admissible_dimension'] == f['predictions']['named_admissible_dimensions'][name])
        check(name + '_all_faces_still_locally_admissible', all(base.rank(group[x]) == 2 for x in face_names.values()))
        changed = {face: base.mm(base.mm(S, group[value]), inverse) for face, value in face_names.items()}
        left = base.mm(changed['023'], changed['012'])
        right = base.mm(changed['013'], changed['123'])
        changed_defect = minus(left, right)
        check(name + '_honest_basis_covariance', changed_defect == base.mm(base.mm(S, case['defect']), inverse) and base.rank(changed_defect) == case['defect_rank'])
        check(name + '_metric_transport_keeps_all_local_maps_orthogonal', all(base.mm(base.mm(base.transpose(value), metric), value) == metric for value in changed.values()))
        check(name + '_entire_surviving_basis_transports', all(base.mv(changed_defect, base.mv(S, v)) == [0, 0] for v in case['admissible_basis']))
        gauge_count, gauge_ok = 0, True
        for choice in product(names, repeat=6):
            b = dict(zip(edges, choice))
            transformed = {}
            for face in faces:
                i, j, k = face
                # All group elements are self-inverse. delta(b) times a.
                transformed[face] = multiply(b[j+k], b[i+k], b[i+j], face_names[face])
            h = multiply(*(transformed[face] for face in filling['right']), *(transformed[face] for face in filling['left']))
            gauge_ok = gauge_ok and h == case['holonomy']
            gauge_count += 1
        check(name + '_all_4096_edge_comparison_frames_keep_holonomy', gauge_count == 4096 and gauge_ok)
        d = diagram(name, case['left'], case['right'], case['defect_rank'])
        compiled = compiler.compile_diagram(d)
        check(name + '_SCC_full_fiber_cell_matches_actual_defect', compiled['passed'] == (case['defect_rank'] == 0))
        OUT.mkdir(parents=True, exist_ok=True)
        (OUT / (name + '-diagram.json')).write_text(json.dumps(d, indent=2, default=str) + '\n', encoding='utf-8')
        outcomes[name] = {**case, 'faces': {face: group[value] for face, value in face_names.items()},
                          'gauges_checked': gauge_count, 'transported_defect': changed_defect,
                          'compiled_cell': compiled}
    check('partial_obstruction_does_not_erase_surviving_sector', base.mv(outcomes['sector_filtered']['defect'], [1, 0]) == [0, 0] and base.mv(outcomes['sector_filtered']['defect'], [0, 1]) != [0, 0])
    check('blocked_case_has_no_nonzero_kernel', outcomes['fully_blocked']['defect_rank'] == 2)
    X, Z = [[0, 1], [1, 0]], group['Z']
    xz, zx = base.mm(X, Z), base.mm(Z, X)
    distinct = diagram('distinct_braids', xz, zx, base.rank(minus(xz, zx)), required=False)
    check('distinct_braids_not_rejected_without_a_comparison_obligation', xz != zx and compiler.compile_diagram(distinct)['passed'])
    report.update({'classification': 'prototype_higher_comparison_can_filter_or_block_a_fiber',
        'named_cases': outcomes, 'census': census, 'census_by_admissible_dimension': dict(distribution),
        'basis_change': S, 'transported_metric': metric,
        'distinct_braid_control': {'XZ': xz, 'ZX': zx, 'required_comparison': False},
        'growth_limit': 'None follows universally: all identity face data fill every finite complex, irrespective of size.',
        'native_disposition': 'NOT TESTED. Face maps and required flat filling are prototype inputs; actual P/N/E fittings and source-authorized higher comparisons are missing.'})


def main():
    paths = [HERE, FIXTURE, PACKET, MODEL, BASE, COMPILER]
    report = {'schema': 'marici.strominger.fiber-loom-tetrahedron.verification.v1',
        'recorded_at': datetime.now(timezone.utc).isoformat(), 'checks': {},
        'source_sha256': {p.relative_to(ROOT).as_posix(): sha256(p.read_bytes()).hexdigest() for p in paths}}
    try:
        run(report)
        report['status'] = 'pass'
    except Exception as error:
        report.update(status='fail', error=repr(error))
        raise
    finally:
        OUT.mkdir(parents=True, exist_ok=True)
        (OUT / 'verification.json').write_text(json.dumps(report, indent=2, default=str) + '\n', encoding='utf-8')
        print(json.dumps({'status': report['status'], 'classification': report.get('classification', 'execution_failure'),
                          'checks': len(report['checks']), 'census': report.get('census_by_admissible_dimension'),
                          'receipt': (OUT / 'verification.json').relative_to(ROOT).as_posix()}))


if __name__ == '__main__':
    main()
