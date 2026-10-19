"""Exact candidate spin lifts of actual proton source generators.

An explicit regular-tetrahedron frame realizes the source metric. The two
lifts per rotation are enumerated, not selected as physical proton dynamics.
No cross-species spin-frame alignment or contact update is inferred.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OWNER = ROOT / 'research/voevodsky'
sys.path.insert(0, str(OWNER / 'checkers'))
from check_proton_electron_contact_binding import A, CI, I, ZERO, ONE, S2, pauli, mm, adj, add, scale, outer, kron, act
from check_pentachoron_cycle_transport import power


def main():
    checks = []
    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    source_path = OWNER / 'inputs/relative-proton.json'
    source = json.loads(source_path.read_text())
    points = ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1))
    affine = ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1))
    columns = tuple(tuple(points[j][i] - points[0][i] for i in range(3)) for j in range(1, 4))
    gram = [[sum(x*y for x, y in zip(a,b)) for b in columns] for a in columns]
    check('frame/source-metric-realized', gram == source['metric'])
    quaternions = set(tuple(F(sign if i == k else 0) for i in range(4))
                      for k in range(4) for sign in (-1, 1))
    quaternions.update(tuple(F(sign, 2) for sign in signs) for signs in product((-1, 1), repeat=4))
    def spin(q):
        return add(scale(A(q[0]), I), scale(-CI, pauli(tuple(A(x) for x in q[1:]))))
    def vector(v):
        return pauli(tuple(A(x) for x in v))
    candidates = []
    singlet = (ZERO, ONE / S2, -ONE / S2, ZERO)
    for index, generator in enumerate(source['generators']):
        permutation = []
        for v in affine:
            target = tuple(sum(F(x)*y for x,y in zip(row,v)) + F(t)
                           for row,t in zip(generator['matrix'], generator['translation']))
            permutation.append(affine.index(target))
        found = []
        for quaternion in sorted(quaternions):
            u = spin(quaternion)
            if all(mm(mm(u, vector(v)), adj(u)) == vector(points[permutation[i]])
                   for i,v in enumerate(points)):
                found.append((quaternion, u))
        check(f'lift/exactly-two/{index}', len(found) == 2)
        check(f'lift/opposite-signs/{index}', found[0][1] == scale(A(-1), found[1][1]))
        records = []
        for quaternion, u in found:
            check(f'lift/unitary/{index}', mm(adj(u), u) == I)
            check(f'lift/determinant-one/{index}', u[0][0]*u[1][1]-u[0][1]*u[1][0] == ONE)
            cube = power(u, 3)
            check(f'lift/central-third-power/{index}', cube in (I, scale(A(-1), I)))
            check(f'contact/proton-only-changes-singlet/{index}',
                  outer(act(kron(u, I), singlet)) != outer(singlet))
            check(f'contact/common-rotation-preserves-singlet/{index}',
                  act(kron(u, u), singlet) == singlet)
            records.append({'quaternion': list(map(str, quaternion)),
                            'matrix': [[z.record() for z in row] for row in u],
                            'third_power': '+I' if cube == I else '-I'})
        check(f'lift/both-return-signs/{index}', {r['third_power'] for r in records} == {'+I', '-I'})
        candidates.append({'source_generator': index,
                           'vertex_permutation': ['ABCD'[i] for i in permutation],
                           'moving_correspondences': ['ABCD'[i] + 'ABCD'[j]
                                                     for i,j in enumerate(permutation) if i != j],
                           'candidates': records})
    check('binding/six-original-moving-correspondences',
          {a for row in candidates for a in row['moving_correspondences']} ==
          {'AB', 'BC', 'CA', 'AD', 'DB', 'BA'})
    files = [Path(__file__), source_path, OWNER / 'checkers/check_proton_electron_contact_binding.py',
             OWNER / 'checkers/check_electron_pairing_coupling.py']
    report = {'schema': 'marici.nima.predictive-pair-proton-spin-candidates.v1',
              'verification_status': 'pass', 'binding_status': 'candidate-lifts-not-selected',
              'checks': checks, 'tetrahedron_frame': points, 'generators': candidates,
              'unresolved': ['choice of lift signs for amplitude-level histories',
                            'relative proton/electron spin-frame identification',
                            'intertwiner from the geometric schedule to the 72-row proton extension',
                            'relative-position and mediator update under arrow requests',
                            'physical preparation and operation-admission policy'],
              'scope': 'Source-metric faithful SO(3) realization and its two SU(2) lifts per generator. '
                       'The tetrahedral frame is declared; no physical common spin frame is derived. '
                       'Common-rotation singlet invariance does not assert that the electron request '
                       'equals the proton lift. No joint restricted graph computed.',
              'input_sha256': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in files}}
    output = HERE.parent / 'results/predictive-pair-proton-spin-candidates.json'
    output.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(f'PASS: {len(checks)} exact source-proton spin-candidate checks')
    print('Two opposite lifts per generator; all six arrow correspondences recovered.')
    print('Proton-only rotations change the singlet; common rotations preserve it.')
    print('No physical lift/frame selection or relative-contact update supplied.')


if __name__ == '__main__':
    main()
