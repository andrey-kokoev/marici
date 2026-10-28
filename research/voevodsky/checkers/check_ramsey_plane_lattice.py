"""Exact controls for the written all-index plane-lattice and parity proofs."""
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ATTEMPT = 'research/voevodsky/contracts/ramsey-plane-lattice-attempt.v1.json'
PROOF = 'research/voevodsky/ramsey-plane-lattice-realization-v1.md'
NORMALS = ((1, 1, 1), (-1, -1, 1), (-1, 1, -1), (1, -1, -1))
P = (-1, 1, 1)
B = (0, 0, 0, -1)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def in_lattice(v):
    return len(v) == 3 and all(Q(x).denominator == 1 for x in v) and sum(v) % 2 == 0


def forward(v, p=P, scale=2):
    return tuple(p[j] + scale * v[j] for j in range(3))


def levels(v):
    return tuple(Q(dot(s, v), 2) for s in NORMALS)


def inverse(t):
    assert len(t) == 4 and sum(t) == 0
    return (t[0] + t[3], t[0] + t[2], t[0] + t[1])


def solve(rows, rhs):
    """Independent exact Gaussian solution of three source-plane equations."""
    a = [[Q(x) for x in row] + [Q(value)] for row, value in zip(rows, rhs)]
    for j in range(3):
        pivot = next(i for i in range(j, 3) if a[i][j])
        a[j], a[pivot] = a[pivot], a[j]
        divisor = a[j][j]
        a[j] = [x / divisor for x in a[j]]
        for i in range(3):
            if i != j:
                factor = a[i][j]
                a[i] = [x - factor * y for x, y in zip(a[i], a[j])]
    return tuple(row[3] for row in a)


def chamber(k):
    q = -sum(k)
    assert q in (1, 2, 3)
    result = {}
    for selected in combinations(range(4), q):
        lam = tuple(int(i in selected) for i in range(4))
        result[lam] = inverse(tuple(k[i] + lam[i] for i in range(4)))
    return result


def squared_distance(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b))


def main():
    attempt = json.loads((ROOT / ATTEMPT).read_text(encoding='utf-8'))
    assert [(c['id'], c['scope_id'], c['intent']) for c in attempt['claims']] == [
        ('plane-lattice-realization', 'D3-four-plane-chambers-geometric-realization-v1', 'prove'),
        ('fixed-scale-cell-forcing', 'D3-binary-unit-cell-forcing-v1', 'reject')]
    assert attempt['bounds'] == {'triple_plane_indices': [-2, 2], 'chamber_indices': [-2, 2], 'vertex_box': [-3, 3]}
    assert attempt['normals'] == [list(s) for s in NORMALS]
    assert attempt['offset'] == list(P) and attempt['plane_index_offsets'] == list(B)
    assert all(sum(s[j] for s in NORMALS) == 0 for j in range(3))
    assert all(dot(a, b) == (3 if i == j else -1)
               for i, a in enumerate(NORMALS) for j, b in enumerate(NORMALS))
    assert all(dot(s, P) == 1 + 4 * B[i] for i, s in enumerate(NORMALS))
    triple_checks = 0
    for selected in combinations(range(4), 3):
        for hs in product(range(-2, 3), repeat=3):
            u = solve([NORMALS[i] for i in selected], [1 + 4 * h for h in hs])
            all_h = tuple((dot(s, u) - 1) / 4 for s in NORMALS)
            assert all(h.denominator == 1 for h in all_h) and sum(all_h) == -1
            assert tuple(all_h[i] for i in selected) == hs
            v = tuple((u[j] - P[j]) / 2 for j in range(3))
            assert in_lattice(v) and forward(v) == u
            t = tuple(all_h[i] - B[i] for i in range(4))
            assert levels(v) == t and inverse(t) == v
            triple_checks += 1
    vertex_checks = 0
    for v in product(range(-3, 4), repeat=3):
        if in_lattice(v):
            t = levels(v)
            assert all(x.denominator == 1 for x in t) and inverse(t) == v
            vertex_checks += 1
    nearest = {v for v in product(range(-2, 3), repeat=3)
               if v != (0, 0, 0) and in_lattice(v) and dot(v, v) <= 2}
    assert len(nearest) == 12 and all(dot(v, v) == 2 for v in nearest)
    cell_counts, face_checks, parity_checks = Counter(), 0, 0
    for k in product(range(-2, 3), repeat=4):
        q = -sum(k)
        if q not in (1, 2, 3):
            continue
        cell = chamber(k)
        vertices = list(cell.values())
        assert len(vertices) == (6 if q == 2 else 4) and all(in_lattice(v) for v in vertices)
        pairs = Counter(squared_distance(a, b) for a, b in combinations(vertices, 2))
        assert pairs == (Counter({2: 12, 4: 3}) if q == 2 else Counter({2: 6}))
        for lam, v in cell.items():
            assert levels(v) == tuple(k[i] + lam[i] for i in range(4))
        faces = []
        for i, side in product(range(4), (0, 1)):
            face = {v for lam, v in cell.items() if lam[i] == side}
            if len(face) != 3:
                continue
            assert all(squared_distance(a, b) == 2 for a, b in combinations(face, 2))
            adjacent = list(k)
            adjacent[i] += 1 if side else -1
            other = chamber(tuple(adjacent))
            opposite_face = {v for lam, v in other.items() if lam[i] == 1 - side}
            assert face == opposite_face
            faces.append(face)
            face_checks += 1
        assert len(faces) == (8 if q == 2 else 4)
        # This supplements, not replaces, the written proof for all integer k.
        assert {int(v[0]) % 2 for v in vertices} == {0, 1}
        cell_counts[q] += 1
        parity_checks += 1
    net = json.loads((ROOT / 'research/voevodsky/contracts/ramsey-tetrahedral-octahedral-conjecture-net.v1.json').read_text(encoding='utf-8'))
    templates = {name: net['candidate_space'][name] for name in ('tetrahedron', 'octahedron')}
    assert set(chamber((0, -1, -1, -1)).values()) == {tuple(v) for v in templates['tetrahedron']}
    assert set(chamber((0, -1, -1, 0)).values()) == {tuple(v) for v in templates['octahedron']}
    for template in templates.values():
        assert template
        assert {2 * v[0] % 2 for v in template} == {0}
    # Endpoints homogeneous, intermediate subdivision vertex not homogeneous.
    assert (0 % 2, 1 % 2, 2 % 2) == (0, 1, 0)
    assert (1, 1, 0) in nearest and (2, 2, 0) not in nearest
    rejected = []
    for name, p, scale in [('wrong affine offset', (0, 0, 0), 2), ('wrong affine scale', P, 1)]:
        valid = all((dot(s, forward(v, p=p, scale=scale)) - 1) % 4 == 0
                    for v in [(0, 0, 0), (1, 1, 0)] for s in NORMALS)
        assert not valid
        rejected.append(name)
    assert not in_lattice((1, 0, 0))
    rejected.extend(['odd-sum lattice vertex', 'nearest-neighbor unit-axis substitution'])
    assert squared_distance((0, 0, 0), (2, 2, 0)) == 8
    rejected.append('scale-two image called an elementary cell')
    assert rejected == attempt['controls']
    sources = [ATTEMPT, PROOF, attempt['source'],
               str(Path(__file__).resolve().relative_to(ROOT)).replace('\\', '/')]
    result = {
        'schema': 'marici.ramsey-plane-lattice.verification.v1', 'status': 'passed',
        'verification_level': 'written all-index proofs and exact rational/integer controls; not kernel verified',
        'outcomes': {claim['id']: {'scope_id': claim['scope_id'], 'outcome': '++' if claim['intent'] == 'prove' else '-+'}
                     for claim in attempt['claims']},
        'triple_intersections_checked': triple_checks,
        'lattice_vertices_checked': vertex_checks,
        'chambers_by_q': dict(sorted(cell_counts.items())),
        'shared_triangular_facets_checked': face_checks,
        'parity_split_chambers_checked': parity_checks,
        'nearest_neighbor_count': len(nearest),
        'template_bindings': templates,
        'rejected_controls': rejected,
        'fixed_scale_counterexample': 'c(v)=v1 mod 2; written proof covers every chamber',
        'dilations_are_cell_automorphisms': False,
        'homogeneous_template_implies_homogeneous_subdivision': False,
        'native_source_operations_admitted': False,
        'dilation_allowing_pilot_refuted': False,
        'uniform_Ramsey_bound_proved': False,
        'root_resolved': False,
        'source_sha256': {p: sha256((ROOT / p).read_bytes()).hexdigest() for p in sources},
    }
    target = ROOT / 'research/voevodsky/results/ramsey-plane-lattice-v1.json'
    target.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'source_sha256'}))


if __name__ == '__main__':
    main()
