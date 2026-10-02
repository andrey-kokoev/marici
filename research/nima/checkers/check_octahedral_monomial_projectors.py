"""Exact octahedral instance of the three-stage monomial-projector theorem.

Arithmetic is rational or Q(i*sqrt(3)). The declared quarter-turn and face-cycle
seeds generate the spatial rotation group; no particle or mass data are used.
Sparse operator products and factored rank-one idempotence avoid a dense cubic
72-by-72 complex multiplication. Generated reports go to ignored results/.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import json

from check_twelve_triangle_positive_geometry import (
    I, C, ONE, ZERO, OMEGA, dot, sub, cross, det, inv, mean, boundary,
    mm, mv, transpose, projector, zadd, zmul, zconj, zscale, znorm, zmv, zmm,
)

ROOT = Path(__file__).resolve().parents[1]
QUARTER = ((F(0), F(-1), F(0)), (F(1), F(0), F(0)),
           (F(0), F(0), F(1)))
AXES = tuple(tuple(F(i == j) for i in range(3)) for j in range(3))


def closure(generators):
    seen = {I}
    frontier = [I]
    while frontier:
        current = frontier.pop()
        for generator in generators:
            candidate = mm(generator, current)
            if candidate not in seen:
                seen.add(candidate)
                frontier.append(candidate)
    return sorted(seen)


def sparse_product(a, b):
    """Matrices use (output row, input column) keys."""
    by_row = defaultdict(list)
    for (k, j), value in b.items():
        by_row[k].append((j, value))
    out = {}
    for (i, k), value in a.items():
        for j, other in by_row[k]:
            key = (i, j)
            out[key] = zadd(out.get(key, ZERO), zmul(value, other))
    return {key: value for key, value in out.items() if value != ZERO}


def sparse_adjoint(a):
    return {(j, i): zconj(value) for (i, j), value in a.items()}


def sparse_apply(a, v):
    out = [ZERO] * len(v)
    for (i, j), value in a.items():
        out[i] = zadd(out[i], zmul(value, v[j]))
    return tuple(out)


def operators(rotations, reference):
    vectors = [zmv(r, reference) for r in rotations]
    u = tuple(z for v in vectors for z in v)
    norm = sum(znorm(z) for z in u)
    local = {}
    for x, v in enumerate(vectors):
        p = projector(v)
        assert zmm(p, p) == p
        for i, j in product(range(3), repeat=2):
            if p[i][j] != ZERO:
                local[3*x+i, 3*x+j] = p[i][j]
    alignment = {}
    for x, rx in enumerate(rotations):
        for z, rz in enumerate(rotations):
            block = mm(rx, transpose(rz))
            for i, j in product(range(3), repeat=2):
                if block[i][j]:
                    alignment[3*x+i, 3*z+j] = (block[i][j]/len(rotations), F(0))
    collective = {(i, j): zscale(zmul(a, zconj(b)), 1/norm)
                  for i, a in enumerate(u) for j, b in enumerate(u)
                  if a != ZERO and b != ZERO}
    return vectors, u, norm, local, alignment, collective


def main():
    group = closure((QUARTER, C))
    assert len(group) == 24
    assert mm(mm(QUARTER, QUARTER), mm(QUARTER, QUARTER)) == I
    assert mm(mm(C, C), C) == I
    for r in group:
        assert det(r) == 1 and mm(transpose(r), r) == I
        assert all(sum(v != 0 for v in row) == 1 for row in r)
        assert all(sum(v != 0 for v in col) == 1 for col in transpose(r))
    assert all(mm(r, s) in group for r in group for s in group)

    # Faithful action on the four cube body-diagonal lines identifies S4.
    diagonals = [(F(1), F(a), F(b)) for a, b in product((-1, 1), repeat=2)]
    actions = set()
    for r in group:
        images = [mv(r, d) for d in diagonals]
        actions.add(tuple(diagonals.index(tuple(t/v[0] for t in v)) for v in images))
    assert actions == set(permutations(range(4)))

    # Stabilizer of one UNORIENTED axis: order eight, not a normal subgroup.
    e1 = AXES[0]
    negative_e1 = tuple(-a for a in e1)
    stabilizer = [r for r in group if mv(r, e1) in (e1, negative_e1)]
    assert len(stabilizer) == 8
    chi = lambda h: h[0][0]
    assert Counter(chi(h) for h in stabilizer) == {F(1): 4, F(-1): 4}
    assert all(mm(a, b) in stabilizer and chi(mm(a, b)) == chi(a)*chi(b)
               for a in stabilizer for b in stabilizer)
    q = ((F(1), F(0), F(0)), (F(0), F(0), F(-1)), (F(0), F(1), F(0)))
    s = ((F(-1), F(0), F(0)), (F(0), F(1), F(0)), (F(0), F(0), F(-1)))
    assert closure((q, s)) == stabilizer
    assert mm(s, s) == I and mm(mm(s, q), s) == transpose(q)
    assert mm(q, q) != I and mm(mm(q, q), mm(q, q)) == I
    assert any(mm(mm(a, h), transpose(a)) not in stabilizer
               for a in group for h in stabilizer)
    representatives = [next(r for r in group if mv(r, e1) == axis) for axis in AXES]
    for a in group:
        induced = [[F(0)]*3 for _ in range(3)]
        for i, t in enumerate(representatives):
            at = mm(a, t)
            choices = [(j, mm(transpose(tj), at))
                       for j, tj in enumerate(representatives)
                       if mm(transpose(tj), at) in stabilizer]
            assert len(choices) == 1
            j, h = choices[0]
            induced[j][i] = chi(h)
        assert tuple(map(tuple, induced)) == a
    unsigned = {tuple(tuple(abs(v) for v in row) for row in r) for r in group}
    assert len(unsigned) == 6  # Axis permutation image S3, not the spatial S4.
    assert len([r for r in group if tuple(tuple(abs(v) for v in row) for row in r) == I]) == 4
    # Two face 120-degree rotations alone need not generate the full group.
    face_only = closure((C, mm(mm(QUARTER, C), transpose(QUARTER))))
    assert len(face_only) == 12

    points = {}
    for axis, name in zip(AXES, ('x', 'y', 'z')):
        points['p'+name] = axis
        points['n'+name] = tuple(-v for v in axis)
    vertex_names = {v: k for k, v in points.items()}
    original = dict(points)
    for signs in product(('p', 'n'), repeat=3):
        face = tuple(sign+axis for sign, axis in zip(signs, ('x', 'y', 'z')))
        points['F_'+'_'.join(sorted(face))] = mean([points[k] for k in face])
    reference = ('F_px_py_pz', 'px', 'py')
    x0 = transpose(tuple(points[k] for k in reference))
    a0 = mm(mm(x0, C), inv(x0))
    coefficients = (ONE, OMEGA, zmul(OMEGA, OMEGA))
    v0 = zmv(x0, coefficients)
    assert all(z != ZERO for z in v0)
    assert v0 == ((F(-1, 6), F(1, 2)), (F(-1, 6), F(-1, 2)), (F(1, 3), F(0)))
    assert sum(znorm(z) for z in v0) == F(5, 3)
    triangles = []
    rows = []
    volume = F(0)
    for r in group:
        face = [vertex_names[mv(r, axis)] for axis in AXES]
        centre = 'F_'+'_'.join(sorted(face))
        tri = (centre, face[0], face[1])
        triangles.append(tri)
        x = transpose(tuple(points[k] for k in tri))
        assert x == mm(r, x0)
        normal = cross(sub(points[tri[1]], points[centre]), sub(points[tri[2]], points[centre]))
        assert dot(normal, points[centre]) > 0
        assert all(dot(normal, sub(p, points[centre])) <= 0 for p in points.values())
        cell_volume = det(x)/6
        assert cell_volume == F(1, 18)
        volume += cell_volume
        a = mm(mm(x, C), inv(x))
        v = zmv(x, coefficients)
        assert a == mm(mm(r, a0), transpose(r)) and mm(mm(a, a), a) == I
        assert zmv(a, v) == tuple(zmul(OMEGA, z) for z in v)
        assert zmv(transpose(r), v) == v0
        rows.append({'triangle': tri, 'outer_arrow': face[:2],
                     'rotation': [[str(v) for v in row] for row in r],
                     'origin_cone_volume': str(cell_volume)})
    edges = {tuple(sorted((a, b))) for t in triangles for a, b in zip(t, t[1:]+t[:1])}
    outer = {(t[1], t[2]) for t in triangles}
    expected_outer = {(a, b) for a in original for b in original if dot(original[a], original[b]) == 0}
    assert len(set(triangles)) == 24 and outer == expected_outer and len(outer) == 24
    assert boundary(triangles) == {} and volume == F(4, 3)
    assert (len(points), len(edges), len(triangles)) == (14, 36, 24)
    assert len(points)-len(edges)+len(triangles) == 2

    vectors, u, norm, local, alignment, collective = operators(group, v0)
    assert len(u) == 72 and norm == 40
    assert [len(a) for a in (local, alignment, collective)] == [216, 1728, 5184]
    for a in (local, alignment, collective):
        assert sparse_adjoint(a) == a
    assert sparse_product(local, local) == local
    assert sparse_product(alignment, alignment) == alignment
    assert sparse_product(alignment, local) == collective
    assert sparse_product(local, alignment) == collective
    assert sparse_apply(alignment, u) == u and sparse_apply(local, u) == u
    # Exact factored idempotence: N=uu*/norm and u*u=norm imply N^2=N.
    assert sparse_apply(collective, u) == u
    assert sum(collective[i, i][0] for i in range(72)) == 1
    assert sum(local[i, i][0] for i in range(72)) == 24
    assert sum(alignment[i, i][0] for i in range(72)) == 3
    # Verify dense N feedback after alignment explicitly; N R L=N follows.
    assert sparse_product(collective, alignment) == collective

    stages = [{((stage, j), ((stage+1) % 3, i)): value
               for (i, j), value in a.items()}
              for stage, a in enumerate((local, alignment, collective))]
    arrows = set().union(*stages)
    assert len(arrows) == 7128
    assert len({port for arrow in arrows for port in arrow}) == 216
    used = set()
    weight_sum = ZERO
    cycles = 0
    for closing, value in stages[2].items():
        k, i = closing[0][1], closing[1][1]
        middle = [b for b in range(72) if (b, i) in local and (k, b) in alignment]
        assert len(middle) == 1
        b = middle[0]
        weight = zmul(zmul(local[b, i], alignment[k, b]), value)
        assert weight == (znorm(collective[k, i]), F(0)) and weight[0] > 0
        weight_sum = zadd(weight_sum, weight)
        used.update((((0, i), (1, b)), ((1, b), (2, k)), closing))
        cycles += 1
    assert used == arrows and cycles == 5184 and weight_sum == ONE
    assert len({(a[1], b[1]) for a, b in arrows}) == 5184
    identity = {(i, i): ONE for i in range(72)}
    assert sparse_product(identity, sparse_product(alignment, local)) == collective
    assert len(local)+len(alignment)+len(identity) == 2016

    # Negative controls: missing support, discarded signs, phase and geometry.
    _, _, _, thin_l, thin_r, thin_n = operators(group, (ONE, ZERO, ZERO))
    assert [len(a) for a in (thin_l, thin_r, thin_n)] == [24, 1728, 576]
    assert sparse_product(thin_r, thin_l) == thin_n
    unsigned_group = [tuple(tuple(abs(v) for v in row) for row in r) for r in group]
    _, _, _, _, unsigned_r, _ = operators(unsigned_group, v0)
    assert sparse_product(unsigned_r, local) != sparse_product(local, unsigned_r)
    opposite = tuple(zscale(z, (-1)**x) for x, v in enumerate(vectors) for z in v)
    assert sparse_apply(local, opposite) == opposite
    assert sparse_apply(collective, opposite) == (ZERO,)*72
    bad = list(triangles)
    a, b, c = bad[0]
    bad[0] = (a, c, b)
    assert len(boundary(bad)) == 3
    flat = {k: (p[0], p[1], F(0)) for k, p in points.items()}
    assert all(det(transpose(tuple(flat[k] for k in t))) == 0 for t in triangles)

    report = {
        'status': 'passed', 'arithmetic': 'Q and Q(i*sqrt(3))',
        'group': {'order': 24, 'identified_as': 'S4 by faithful action on four body-diagonal lines',
                  'seeds': ['quarter-turn about z', 'cyclic coordinate rotation'],
                  'stabilizer_order': 8, 'stabilizer': 'D8 (order eight)',
                  'stabilizer_normal': False, 'induced_sign_action_exact': True,
                  'unsigned_axis_action_order': 6, 'unsigned_axis_kernel_order': 4},
        'geometry': {'vertices': 14, 'edges': 36, 'triangles': 24, 'outer_directed_edges': 24,
                     'boundary_zero': True, 'euler_characteristic': 2,
                     'volume': str(volume), 'each_cone_volume': '1/18', 'supporting_planes': True},
        'selected_vector': [[str(a), str(b)] for a, b in v0],
        'assembled_squared_norm': str(norm),
        'projectors': {'ranks': [24, 3, 1], 'commuting_intersection_exact': True,
                       'collective_formula': 'u u_dagger / 40',
                       'collective_idempotence': 'exact rank-one norm factorization'},
        'net': {'stage_supports': [216, 1728, 5184], 'typed_arrow_union': 7128,
                'typed_ports': 216, 'closed_cycles': cycles, 'positive_cycle_weights': True,
                'cycle_weight_sum': '1', 'cycles_cover_all_arrows': True,
                'identity_feedback_arrows': 2016, 'identified_stage_union': 5184},
        'controls': {'face_cycles_only_group_order': len(face_only),
                     'zero_coordinate_supports': [24, 1728, 576],
                     'discarding_transport_signs_breaks_commutation': True,
                     'alternating_phases_preserve_local_selection_but_cancel_collectively': True,
                     'flipped_triangle_boundary_edges': 3, 'flat_volume': '0'},
        'triangles_and_transports': rows,
        'scope': 'Declared octahedral seeds, Cartesian monomial basis and three materialized stages. '
                 'No minimality, stagewise spatial embedding, phase-locking dynamics or particle/mass identification.'}
    out = ROOT/'results'
    out.mkdir(exist_ok=True)
    (out/'octahedral-monomial-projectors.json').write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    arrow_rows = [{'source': list(a), 'target': list(b), 'weight': [str(z[0]), str(z[1])]}
                  for stage in stages for (a, b), z in sorted(stage.items())]
    (out/'octahedral-7128-arrows.json').write_text(json.dumps(arrow_rows, separators=(',', ':'))+'\n', encoding='utf-8')
    names = list(points)
    obj = ['# Octahedron with eight face centroids and 24 oriented triangles']
    obj += ['v '+' '.join(str(float(v)) for v in points[k]) for k in names]
    obj += ['f '+' '.join(str(names.index(k)+1) for k in t) for t in triangles]
    (out/'octahedral-positive-geometry.obj').write_text('\n'.join(obj)+'\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in report.items() if k != 'triangles_and_transports'}, indent=2))


if __name__ == '__main__':
    main()
