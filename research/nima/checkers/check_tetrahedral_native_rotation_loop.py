"""Native tetrahedral route amplitudes, without a spinor/Pauli/quaternion input.

Dependency-free exact arithmetic. Exit zero means the audit passed, NOT that
the conjectured physical spinor selection survived. See scientific_disposition.
"""
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import hashlib
import json

from check_twelve_triangle_positive_geometry import (
    I, POINTS, ONE, ZERO, OMEGA, compose, rotation, mean, transpose, mm,
    zadd, zmul, zconj, zscale, znorm, zmv, zmm, zreal, projector,
)

ROOT = Path(__file__).resolve().parents[1]
SEEDS = ((1, 2, 0, 3), (3, 0, 2, 1))


def inner(v, w):
    out = ZERO
    for a, b in zip(v, w):
        out = zadd(out, zmul(zconj(a), b))
    return out


def apply(a, v):
    return tuple(inner(tuple(map(zconj, row)), v) for row in a)


def mscale(a, s):
    return tuple(tuple(zmul(s, z) for z in row) for row in a)


def outer(v, w, denominator):
    return tuple(tuple(zscale(zmul(a, zconj(b)), 1/denominator) for b in w) for a in v)


def zpower(z, n):
    out = ONE
    for _ in range(n):
        out = zmul(out, z)
    return out


def matrix_defect_norm(a, b):
    return sum(znorm(zadd(x, zscale(y, -1))) for ra, rb in zip(a, b) for x, y in zip(ra, rb))


def main():
    group, front = {tuple(range(4))}, [tuple(range(4))]
    while front:
        q = front.pop()
        for s in SEEDS:
            p = compose(s, q)
            if p not in group:
                group.add(p)
                front.append(p)
    rotations = [rotation(p) for p in sorted(group)]
    assert len(rotations) == 12
    zero = rotations.index(I)
    x0 = transpose((mean([POINTS[a] for a in 'ABC']), POINTS['A'], POINTS['B']))
    v0 = zmv(x0, (ONE, OMEGA, zmul(OMEGA, OMEGA)))
    norm = inner(v0, v0)
    assert norm == (F(20, 3), F(0))
    n = norm[0]
    vs = [zmv(r, v0) for r in rotations]
    ps = [projector(v) for v in vs]
    transports, selected = {}, {}
    for y, x in product(range(12), repeat=2):
        transports[y, x] = mm(rotations[y], transpose(rotations[x]))
        selected[y, x] = zmm(zmm(ps[y], zreal(transports[y, x])), ps[x])
        assert selected[y, x] == outer(vs[y], vs[x], n)
        assert apply(selected[y, x], vs[x]) == vs[y]
    # The path law is derived before taking any scalar return amplitude.
    for z, y, x in product(range(12), repeat=3):
        assert mm(transports[z, y], transports[y, x]) == transports[z, x]
        assert zmm(selected[z, y], selected[y, x]) == selected[z, x]
    for x in range(12):
        assert transports[x, x] == I and selected[x, x] == ps[x]
    axes = {label: tuple(tuple(F((1 if i == axis else -1) if i == j else 0)
                              for j in range(3)) for i in range(3))
            for axis, label in enumerate(('x', 'y', 'z'))}
    assert all(h in rotations and mm(h, h) == I for h in axes.values())
    half_expectations = {label: zscale(inner(v0, zmv(h, v0)), 1/n) for label, h in axes.items()}
    assert half_expectations == {'x': (F(-13, 15), F(0)),
                                 'y': (F(-1, 15), F(0)), 'z': (F(-1, 15), F(0))}

    def path_for(labels):
        r, path = I, [zero]
        for label in labels:
            r = mm(axes[label], r)
            path.append(rotations.index(r))
        return path

    def route(path, line_maps=selected, vectors=vs):
        rigid, coherent, bare = zreal(I), ps[path[0]], vectors[path[0]]
        bargmann = ONE
        for x, y in zip(path, path[1:]):
            rigid = zmm(zreal(transports[y, x]), rigid)
            coherent = zmm(line_maps[y, x], coherent)
            bare = apply(ps[y], bare)
            bargmann = zmul(bargmann, zscale(inner(vectors[y], vectors[x]), 1/n))
        start, end = path[0], path[-1]
        a_rigid = zscale(inner(vectors[end], apply(rigid, vectors[start])), 1/n)
        a_coherent = zscale(inner(vectors[end], apply(coherent, vectors[start])), 1/n)
        a_bare = zscale(inner(vectors[end], bare), 1/n)
        assert a_bare == bargmann
        return a_rigid, a_coherent, a_bare

    loops = []
    for a, b in permutations(axes, 2):
        # Chronological a,b,a^-1,b^-1. For these vector matrices a^-1=a.
        labels = (a, b, a, b)
        path = path_for(labels)
        assert path[0] == path[-1]
        rigid, coherent, bare = route(path)
        predicted_bare = zmul(zpower(half_expectations[a], 2), zpower(half_expectations[b], 2))
        assert rigid == coherent == ONE
        assert bare == predicted_bare and bare[1] == 0 and bare[0] > 0
        assert bare[0] == (F(1, 50625) if set((a, b)) == {'y', 'z'} else F(169, 50625))
        doubled = route(path_for(labels + labels))
        assert doubled == (ONE, ONE, zmul(bare, bare))
        loops.append({'axes': [a, b], 'rigid_amplitude': rigid,
                      'selected_transport_amplitude': coherent, 'bare_projection_amplitude': bare,
                      'bare_projection_phase_sign': 1, 'double_projection_amplitude': doubled[2]})

    # A real oddball: a different loop has a negative projection amplitude.
    # This demonstrates that a minus sign alone is not spinorial transport.
    triangles = []
    for labels in permutations(axes):
        path = path_for(labels)
        assert path[0] == path[-1]
        rigid, coherent, bare = route(path)
        assert rigid == coherent == ONE and bare == (F(-13, 3375), F(0))
        triangles.append({'axes': labels, 'bare_projection_amplitude': bare})
    triangle_path = path_for(('x', 'y', 'z'))
    shortcut_path = [triangle_path[0], triangle_path[2], triangle_path[3]]
    shortcut = route(shortcut_path)
    assert shortcut == (ONE, ONE, (F(1, 225), F(0)))
    # Projective phases on this V4 orbit are a scalar coboundary, not a
    # nontrivial multiplier commutator: all axes have overlap phase -1.
    v4 = [I] + list(axes.values())
    overlap_phase = {I: 1, **{h: -1 for h in axes.values()}}
    multiplier = {(a, b): overlap_phase[a] * overlap_phase[b] * overlap_phase[mm(a, b)]
                  for a, b in product(v4, repeat=2)}
    assert -1 in multiplier.values()
    assert all(multiplier[a, b] == multiplier[b, a] for a, b in product(v4, repeat=2))

    # Vertex-frame gauge phases telescope; they cannot manufacture a closed-loop sign.
    phases = [zscale(zpower(OMEGA, j % 3), (-1)**j) for j in range(12)]
    gvs = [tuple(zmul(phases[j], z) for z in v) for j, v in enumerate(vs)]
    assert all(projector(v) == p for v, p in zip(gvs, ps))
    gauge_maps = {(y, x): mscale(t, zmul(phases[y], zconj(phases[x])))
                  for (y, x), t in selected.items()}
    for labels in [('x', 'y', 'x', 'y'), ('x', 'y', 'z')]:
        path = path_for(labels)
        assert route(path, gauge_maps, gvs) == route(path)
    # In contrast, inserting one independent edge sign changes the amplitude
    # while breaking the native composition cell; no physical rule sources it.
    path = path_for(('x', 'y', 'x', 'y'))
    bad = dict(selected)
    bad[path[1], path[0]] = mscale(bad[path[1], path[0]], (F(-1), F(0)))
    injected = route(path, bad)[1]
    defect = matrix_defect_norm(zmm(bad[path[2], path[1]], bad[path[1], path[0]]),
                               bad[path[2], path[0]])
    assert injected == (F(-1), F(0)) and defect == 4

    # Audit the declared SCC scalar reductions against the actual calculations.
    diagram_path = ROOT / 'contracts' / 'tetrahedral-native-rotation-loop.json'
    diagram = json.loads(diagram_path.read_text(encoding='utf-8'))
    tokens = {a['id']: a['map_token'] for a in diagram['arrows']}
    assert tokens['native_commutator'] == tokens['identity'] == 'scalar:+1'
    assert tokens['spinorial_requirement'] == 'scalar:-1'
    assert all(row['selected_transport_amplitude'] == ONE for row in loops)
    # A physical rotation path is additional input to this endpoint model.
    # The proof T_zy T_yx=T_zx handles arbitrary lengths, not just sampled loops.
    sources = [Path(__file__), Path(__file__).with_name('check_twelve_triangle_positive_geometry.py'),
               Path(__file__).with_name('check_triangle_half_phase.py'), diagram_path]
    report = {
        'status': 'passed',
        'scientific_disposition': 'native_transport_spinor_selection_conjecture_falsified_in_the_declared_model',
        'physical_disposition': 'not_tested_no_independent_physical_rotation_interaction_or_readout',
        'coherence_obligation': 'route compatibility before physical readout descent',
        'arithmetic': 'Q(i*sqrt(3)); exact fractions; no Pauli, quaternion or spinor input',
        'source_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
        'reference_squared_norm': n,
        'native_laws': {'relative_transport': 'F_yx=r_y r_x^T',
                        'selected_transport': 'T_yx=P_y F_yx P_x=v_y v_x*/(20/3)',
                        'composition': 'F_zy F_yx=F_zx; T_zy T_yx=T_zx; T_xx=P_x',
                        'checked_triples_per_law': 1728,
                        'all_closed_selected_routes': 'identity on their selected line by telescoping'},
        'categorical_contract': {'path': str(diagram_path.relative_to(ROOT)),
                                 'native_vs_spinorial_scalar_residual': 2,
                                 'expected_failed_cell': 'native_spinorial_return'},
        'half_turn_expectations_on_reference': half_expectations,
        'commutator_loops': loops,
        'projection_only_triangles': triangles,
        'projection_shortcut_amplitude': shortcut[2],
        'projection_V4_multiplier_class': 'scalar coboundary; commuting multiplier ratio +1',
        'hostiles': {'vertex_rephasing_preserves_closed_amplitudes': True,
                     'injected_edge_sign_return': injected,
                     'injected_edge_sign_composition_defect_squared_norm': defect,
                     'negative_projection_triangle_not_spinorial_commutator': True},
        'first_missing_physical_object': 'Independently specified interaction producing rotation-path-dependent amplitudes for this excitation, with a coherent reference/readout.',
        'scope': 'The existing finite endpoint/filter model does not select the extra physical factor. This is not a universal prohibition of spinorial realizations or a laboratory test.',
    }
    out = ROOT / 'results' / 'tetrahedral-native-rotation-loop.json'
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(report, indent=2, default=str) + '\n', encoding='utf-8')
    print('AUDIT PASS; NATIVE SPINOR-SELECTION CONJECTURE FAILS in the declared endpoint model.')
    print('1728 frame and 1728 selected-line composition triples: all close.')
    print('Six half-turn commutators: coherent return +1; projection-only phase +1.')
    print('Projection triangle: -13/3375; shortcut +1/225. A minus sign alone is not spin.')
    print('Inserted sign gives -1 but composition defect norm squared 4; physical interaction absent.')


if __name__ == '__main__':
    main()
