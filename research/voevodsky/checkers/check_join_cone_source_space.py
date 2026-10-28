"""Exact elementary checks for the join/cone candidate-space ledger note.

Checks the declared geometry, not its identification with the WG source.
"""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]


def simplex(vertices):
    return {frozenset(c) for k in range(len(vertices) + 1) for c in combinations(vertices, k)}


def main():
    left, right = simplex(('A', 'B')), simplex(('C', 'D'))
    joined = {a | b for a in left for b in right}
    assert joined == simplex(('A', 'B', 'C', 'D'))
    f_vector = [sum(len(face) == k for face in joined) for k in range(1, 5)]
    assert f_vector == [4, 6, 4, 1]
    cone = {frozenset()}  # augmented empty simplex, not the void complex
    for vertex in ('A', 'B', 'C', 'D'):
        cone |= {face | {vertex} for face in cone}
    assert cone == joined

    # N_i.x <= 1 is a rational rescaling of the viewer's regular tetrahedron.
    normals = [(1, 1, 1), (-1, -1, 1), (-1, 1, -1), (1, -1, -1)]
    length = Q(3)
    # Linear forms use coefficient order (constant,x,y,z,w).
    bary = [tuple([Q(1, 4)] + [Q(-x, 4) for x in n] + [-Q(1, 4) / length]) for n in normals]
    bary.append((Q(0), Q(0), Q(0), Q(0), 1 / length))
    vertices = [tuple([-Q(x) for x in n] + [Q(0)]) for n in normals] + [(Q(0), Q(0), Q(0), length)]
    assert tuple(sum(row[k] for row in bary) for k in range(5)) == (1, 0, 0, 0, 0)
    for j in range(4):
        recovered = tuple(sum(vertices[i][j] * bary[i][k] for i in range(5)) for k in range(5))
        assert recovered == tuple(int(k == j + 1) for k in range(5))
    for i, row in enumerate(bary):
        for j, vertex in enumerate(vertices):
            assert sum(a * b for a, b in zip(row, (Q(1),) + vertex)) == int(i == j)

    # Lift/projection polynomial coefficients in lambda: constant term and slope.
    for point in [(-1, -1, -1), (1, 1, -1), (1, -1, 1), (-1, 1, 1)]:
        for s in [Q(0), Q(1, 4), Q(1, 2), Q(1)]:
            constant = tuple((1 - s) * x for x in point)
            slope = (Q(0), Q(0), length * s)
            if s == 0:
                assert constant == point and slope == (0, 0, 0)
            if s == 1:
                assert constant == (0, 0, 0) and slope == (0, 0, length)
    arrows = {'AB', 'BC', 'CA', 'BA', 'AD', 'DB'}
    support = {frozenset(edge) for edge in arrows}
    assert {frozenset(edge) for edge in combinations('ABCD', 2)} - support == {frozenset('CD')}
    assert {'AB', 'BC', 'CA'} <= arrows and {'BA', 'AD', 'DB'} <= arrows
    result = {
        'passed': True,
        'scope': 'Declared finite simplicial joins, exact affine cone identities, and lift coefficients',
        'join_f_vector': f_vector,
        'cone_barycentric_identities': 'exact rational coefficient comparison',
        'base_fixed_under_lift': True,
        'common_apex': True,
        'source_incidence': 'declared six-arrow baseline, not a fresh native compiler check',
        'WG_source_space_identified': False,
        'visualization_accepted': False,
        'visualization_clone_disposition': 'removed at operator request',
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    target = ROOT / 'research/voevodsky/results/join-cone-source-space-v1.json'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
