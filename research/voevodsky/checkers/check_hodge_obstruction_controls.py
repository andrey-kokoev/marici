"""Finite Hodge-route controls. Imported cycle descriptions are not new proofs."""
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]

FIXTURES = ROOT / 'research/conjecture_net/contracts/hodge-control-fixtures.v1.json'
OUT = ROOT / 'research/voevodsky/results/hodge-obstruction-controls-v1.json'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def rank(matrix):
    a = [list(map(F, row)) for row in matrix]
    r = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        divisor = a[r][col]
        a[r] = [x / divisor for x in a[r]]
        for i in range(len(a)):
            if i != r:
                factor = a[i][col]
                a[i] = [x - factor * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def evaluate(data):
    require(data['schema'] == 'marici.hodge-control-fixtures.v1', 'fixture schema')
    p = data['projective_space']
    require(p['variety'] == 'P^4_C' and p['complex_dimension'] == 4 and p['codimension'] == 2, 'projective scope')
    require(p['cycle_class_columns'] == [[1]], 'projective cycle witness')
    q = data['quadric']
    require(q['complex_dimension'] == 4 and q['codimension'] == 2 and len(q['coordinates']) == 6, 'quadric scope')
    require(q['equation_terms'] == [[1, 0, 5], [-1, 1, 4], [1, 2, 3]], 'Plucker equation')
    hessian = [[0] * 6 for _ in range(6)]
    for coefficient, i, j in q['equation_terms']:
        hessian[i][j] += coefficient
        hessian[j][i] += coefficient
    require(rank(hessian) == 6, 'quadric singularity')
    planes = [set(q[key]) for key in ('plane_A_free_coordinates', 'plane_B_free_coordinates')]
    require(all(len(plane) == 3 and plane <= set(range(6)) for plane in planes), 'plane dimensions')
    for plane in planes:
        require(all(not {i, j} <= plane for _, i, j in q['equation_terms']), 'plane not on quadric')
    require(not planes[0] & planes[1], 'chosen planes not disjoint')
    partitions = sorted((a, b) for a in range(3) for b in range(a + 1))
    require(sorted(map(tuple, q['schubert_partitions'])) == partitions, 'Schubert census')
    require(Counter(sum(partition) for partition in partitions) == Counter({0: 1, 1: 1, 2: 2, 3: 1, 4: 1}), 'middle rank')
    normal = q['normal_sequence']
    require(normal == {'linear_normal_bundle_rank': 3, 'quadric_degree': 2}, 'normal sequence')
    # c2(O(1)^3/O(2)) = binom(3,2) - 2*3 + 4 = 1.
    self_intersection = 3 - 2 * 3 + 2 ** 2
    intersection = [[self_intersection, 0], [0, self_intersection]]
    require(q['intersection_matrix'] == intersection, 'plane intersection classes')
    require(q['hyperplane_square'] == [1, 1], 'hyperplane square class')
    primitive = q['primitive_algebraic_class']
    require(primitive == [1, -1] and sum(primitive) == 0, 'primitive algebraic control')
    obstruction = q['naive_divisor_only_obstruction_row']
    require(obstruction == [1, -1], 'divisor-only hostile')
    require(sum(x * y for x, y in zip(obstruction, q['hyperplane_square'])) == 0, 'hostile must kill divisor square')
    require(obstruction[0] != 0 and obstruction[1] != 0, 'hostile must fail on algebraic planes')
    require(sum(x * y for x, y in zip(obstruction, primitive)) == 2, 'primitive false positive')
    r = data['rationalization']
    generator, alpha = r['integral_cycle_image_generator'], r['integral_class']
    require(generator == 2 and alpha == 1 and alpha % generator != 0, 'integral diagnostic')
    require(F(r['rational_witness_coefficient']) * generator == alpha, 'rational witness')
    require(r['torsion_presentation_matrix'] == [[2, 0], [0, 3]], 'torsion diagnostic')
    require(rank(r['torsion_presentation_matrix']) == 2, 'torsion survives rationalization')
    return {
        'projective_space_cycle_span_rank': 1,
        'quadric_gradient_rank': 6, 'quadric_middle_cycle_span_rank': 2,
        'quadric_divisor_square_span_rank': 1,
        'quadric_algebraic_class_outside_divisor_span': [1, 0],
        'quadric_primitive_algebraic_class': primitive,
        'naive_obstruction_on_algebraic_basis': obstruction,
        'naive_obstruction_disposition': 'rejected_as_Hodge_obstruction',
        'rational_witness_for_integral_nonmember': r['rational_witness_coefficient'],
        'torsion_cokernel_dimension_over_Q': 2 - rank(r['torsion_presentation_matrix']),
        'general_algebraic_cycle_annihilation_proved': False,
        'Hodge_proved': False, 'Hodge_refuted': False,
        'scope': 'Finite exact controls with explicitly imported standard cycle descriptions; not a newly formalized Schubert or Lefschetz theorem.',
    }


def report():
    return {
        'schema': 'marici.hodge-obstruction-controls.v1', 'passed': True,
        'results': evaluate(json.loads(FIXTURES.read_text(encoding='utf-8'))),
        'source_sha256': {p.relative_to(ROOT).as_posix(): sha256(p.read_bytes()).hexdigest()
                          for p in (FIXTURES, Path(__file__).resolve())},
    }


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))
