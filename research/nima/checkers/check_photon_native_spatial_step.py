"""Attach the retained phase clock and test native spatial readout/paths."""
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path
import json
import sympy as s

import check_photon_two_packet_candidate as seed_check
import check_retained_rotor_history_clock as clock_check
from photon_native_spatial_step import (REGISTRY, VERTICES, SEED, U, W,
    PLANE_STEP, COMPATIBLE_FRAME, ClockedHistory, RetainedPath, coordinates,
    continuation_matrix, contrast_reader, mv, mm, transpose)
from check_triangle_half_phase import TwoPacket


def rejects(fn):
    try:
        fn()
    except ValueError:
        return
    raise AssertionError('Invalid native continuation accepted')


def main():
    seed_check.main()
    clock_check.main()  # fresh unit-rate clock and retained-lift checks
    # Identify q=sqrt(3)*a, p=b in the existing adjoint rotor module. This
    # explicitly fixes the factor of TWO between rotor-clock and spatial angle.
    a, b, theta = s.symbols('a b theta', real=True)
    E1 = s.Matrix(2, 2, clock_check.source.E1)
    E2 = s.Matrix(2, 2, clock_check.source.E2)
    J = s.Matrix(2, 2, clock_check.source.J)
    rotor = s.cos(theta) * s.eye(2) + s.sin(theta) * J
    Q = s.sqrt(3) * a * E1 + b * E2
    evolved = s.simplify(rotor * Q * rotor.T)
    aq = s.simplify(s.trace(E1 * evolved) / (2 * s.sqrt(3)))
    bp = s.simplify(s.trace(E2 * evolved) / 2)
    assert s.trigsimp(aq - (a * s.cos(2 * theta) + b * s.sin(2 * theta) / s.sqrt(3))) == 0
    assert s.trigsimp(bp - (b * s.cos(2 * theta) - s.sqrt(3) * a * s.sin(2 * theta))) == 0
    bridge_step = s.Matrix([aq, bp]).subs(theta, s.pi / 3)
    assert s.simplify(bridge_step - s.Matrix(PLANE_STEP) * s.Matrix([a, b])) == s.zeros(2, 1)
    assert rotor.subs(theta, s.pi) == -s.eye(2)
    assert rotor.subs(theta, 2 * s.pi) == s.eye(2)
    assert s.simplify(evolved.subs(theta, s.pi) - Q) == s.zeros(2)
    # A wrong identification theta=2*pi/3 gives K^2, not K.
    assert s.simplify(s.Matrix([aq, bp]).subs(theta, 2 * s.pi / 3)
                      - s.Matrix(PLANE_STEP) ** 2 * s.Matrix([a, b])) == s.zeros(2, 1)
    G = s.diag(3, 1)
    assert s.Matrix(PLANE_STEP).T * G * s.Matrix(PLANE_STEP) == G

    # Compare the earlier compatible frame to the ACTUAL endpoint readout.
    basis = tuple(zip(U, W))
    native_frame = mm(contrast_reader(), basis)
    assert native_frame == ((F(0), F(0)), (F(-3), F(1)), (F(1), F(1)))
    Rabc = ((0, 1, 0), (0, 0, -1), (-1, 0, 0))
    assert mm(Rabc, COMPATIBLE_FRAME) == mm(COMPATIBLE_FRAME, PLANE_STEP)
    assert mm(transpose(COMPATIBLE_FRAME), COMPATIBLE_FRAME) == ((F(2), F(0)), (F(0), F(2, 3)))
    native_gram = mm(transpose(native_frame), native_frame)
    assert native_gram == ((F(10), F(-2)), (F(-2), F(2)))
    assert mm(transpose(PLANE_STEP), mm(native_gram, PLANE_STEP)) != native_gram
    assert mm(Rabc, native_frame) != mm(native_frame, PLANE_STEP)
    # Thus the earlier rotation adapter is not the native endpoint-position
    # contrast. Its valid intertwining equation cannot prove equality of maps.

    initial = ClockedHistory.initial()
    history = initial
    rows = []
    states = []
    plane_coordinates = (F(1), F(0))
    for n in range(7):
        states.append(history)
        coeffs = history.summary()
        assert coordinates(coeffs) == plane_coordinates
        # Exact rational recurrence, independently of path extension.
        expected = SEED
        for _ in range(n):
            expected = mv(continuation_matrix(), expected)
        assert coeffs == expected
        assert history.clock_over_pi == F(n, 3)
        for record in history.paths:
            assert len(record.packets) == n + 1
            net = record.continuation_displacement
            assert sum(x * x for x in net) in (0, 8)
            if n:
                increments = [tuple(VERTICES[q.target][j] - VERTICES[p.target][j] for j in range(3))
                              for p, q in zip(record.packets, record.packets[1:])]
                assert tuple(sum(v[j] for v in increments) for j in range(3)) == net
                assert all(sum(x * x for x in step) == 8 for step in increments)
        spatial = history.spatial_contrast()
        rows.append({'updates': n, 'clock_over_pi': str(history.clock_over_pi),
                     'packet_coefficients': [str(x) for x in coeffs],
                     'target_amplitudes': [str(x) for x in history.target_amplitudes()],
                     'spatial_amplitude_contrast': [str(x) for x in spatial],
                     'spatial_contrast_squared_norm': str(sum(x * x for x in spatial)),
                     'retained_paths': len(history.paths),
                     'retained_counting_norm_squared': str(history.retained_counting_norm())})
        history = history.advance()
        plane_coordinates = mv(PLANE_STEP, plane_coordinates)
    assert [state.spatial_contrast() for state in states[:4]] == [(0, -3, 1), (0, 0, -2), (0, 3, 1), (0, -3, 1)]
    assert states[3].summary() == states[6].summary() == initial.summary()
    assert states[3].paths != initial.paths and states[6].paths != states[3].paths
    assert states[3].clock_over_pi == 1 and states[6].clock_over_pi == 2
    assert states[1].retained_counting_norm() != initial.retained_counting_norm()
    assert len(states[1].paths) == 10
    first_AB = [p for p in states[1].paths if p.packets[0].label == 'AB']
    assert {p.packets[-1].label for p in first_AB} == {'BC', 'BA'}
    assert len({p.continuation_displacement for p in first_AB}) == 2
    after_return = {tuple(p.label for p in row.packets): row for row in states[3].paths}
    closed = after_return[('AB', 'BC', 'CA', 'AB')]
    open_path = after_return[('AB', 'BC', 'CA', 'AD')]
    assert closed.continuation_displacement == (0, 0, 0)
    assert open_path.continuation_displacement == (-2, 0, 2)
    assert closed.coefficient == open_path.coefficient == 1

    # All 24 endpoint relabellings transport the whole registry/readout, not
    # just the six coefficients in a fixed slot set. Only two preserve that set.
    original_edges = {(p.source, p.target) for p in REGISTRY}
    automorphisms = []
    labels = tuple(VERTICES)
    xyz = tuple(VERTICES[v] for v in labels)
    for perm in permutations(range(4)):
        rename = {labels[i]: labels[perm[i]] for i in range(4)}
        registry = tuple(TwoPacket(p.label, rename[p.source], rename[p.target]) for p in REGISTRY)
        R = tuple(tuple(sum(F(xyz[perm[k]][i] * xyz[k][j], 4) for k in range(4)) for j in range(3)) for i in range(3))
        assert s.Matrix(R).T * s.Matrix(R) == s.eye(3)
        assert continuation_matrix(registry) == continuation_matrix()
        assert contrast_reader(registry) == mm(R, contrast_reader())
        sign = (-1) ** sum(perm[i] > perm[j] for i in range(4) for j in range(i + 1, 4))
        assert s.Matrix(R).det() == sign
        assert (sign * s.Matrix(R)).det() == 1  # alternative area action
        if {(p.source, p.target) for p in registry} == original_edges:
            automorphisms.append(rename)
    assert len(automorphisms) == 2
    rejects(lambda: RetainedPath((REGISTRY[0], REGISTRY[4]), F(1)))
    rejects(lambda: ClockedHistory(1, initial.paths))
    rejects(lambda: coordinates((F(1),) * 6))

    report = {
        'status': 'clock attachment and native spatial continuation checked; no unique translating excitation established',
        'clock_bridge': {'coordinates': 'q=sqrt(3)*a, p=b in the existing adjoint rotor',
                        'clock': 'T-T0=theta', 'one_K_update': 'Delta T=pi/3, spatial phase increment 2*pi/3',
                        'lift_policy': 'specified positive pi/3 rotor segment; endpoint data alone do not select winding',
                        'after_three_updates': 'coefficient/contrast return; rotor -I; clock advanced pi; histories differ',
                        'after_six_updates': 'rotor +I; clock advanced 2*pi; histories still differ'},
        'spatial_readout': {'native': 'sum_i r_i sum_(p.target=i) c_p; signed amplitude contrast, not position/Born mean',
                           'cycle': [[0, -3, 1], [0, 0, -2], [0, 3, 1]],
                           'squared_norm_cycle': [10, 4, 10],
                           'earlier_rotation_adapter': 'compatible but different map; not the native endpoint contrast'},
        'retained_transport': {'one_step_extensions': 10,
                               'AB_successors': ['BC', 'BA'],
                               'three_update_same_summary_witnesses': {'closed': 'AB BC CA AB', 'open': 'AB BC CA AD'},
                               'net_displacement_bound': 'squared distance <=8 in the fixed tetrahedron at every depth',
                               'path_length': '2*sqrt(2)*n for n appended edges, distinct from net displacement',
                               'probability_warning': 'prefix extension copies amplitudes and is not unitary in retained counting norm'},
        'symmetry': {'whole_registry_relabellings_checked': 24, 'unchanged_seed_automorphisms': 2},
        'history_samples': rows,
        'next_gate': 'Determine whether the native spatial carrier remains this fixed tetrahedron or supplies distinct spatial placements for retained extensions; do not insert translation or a Born/route-selection law by fiat.'}
    dest = Path(__file__).resolve().parents[1] / 'results' / 'photon-native-spatial-step.json'
    dest.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print('PASS: existing angular clock attached to K with Delta T=pi/3; adjoint spatial phase is twice rotor phase.')
    print('PASS: native endpoint contrast cycles (0,-3,1) -> (0,0,-2) -> (0,3,1); not the earlier rigid-rotation adapter.')
    print('PASS: equal three-step coefficient summaries retain different clocks and open/closed paths.')
    print('BOUNDARY: branching motion is confined to the fixed tetrahedral carrier; no unique translating photon or Born dynamics derived.')
    print('Report: research/nima/results/photon-native-spatial-step.json')


if __name__ == '__main__':
    main()
