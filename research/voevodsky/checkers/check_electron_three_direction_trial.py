"""Source-bound three-real-direction spinor trial; never rewrites native outputs."""
from fractions import Fraction as F
from itertools import product, permutations
from pathlib import Path
import json

from check_electron_configuration_dimension_trial import (
    ROOT, BASE, STORE, digest, decode, density, real_rank, serial,
)
from check_electron_tetrahedral_spinor import adj, act, ident, sm, ma
from check_electron_charge_spin_frontier import ga, gs, gm, gc, gt, gmm, spin, G0, G1, GI

PREREQUISITE = BASE / 'results/electron-configuration-dimension-trial-v1.json'
OUT = BASE / 'results/electron-three-direction-trial-v1.json'
I = ident(2)
E = tuple(spin(tuple(F(int(k == j)) for k in range(4))) for j in (1, 2, 3))


def inner(x, y):
    return gt(gm(gc(a), b) for a, b in zip(x, y))


def flat(z):
    return [c for x in z for c in x]


def combine(coefficients, basis=E):
    result = sm(0, I)
    for c, matrix in zip(coefficients, basis):
        result = ma(result, sm(c, matrix))
    return result


def chart(t, negative=False):
    s = sum(x * x for x in t)
    q = ((1 - s) / (1 + s),) + tuple(2 * x / (1 + s) for x in t)
    return sm(-1 if negative else 1, spin(q))


def determinant(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


def main():
    prior = json.loads(PREREQUISITE.read_text(encoding='utf-8'))
    assert prior['verification_passed'] and all(prior['checks'].values())
    pins = dict(prior['source_sha256'])
    pins[PREREQUISITE.relative_to(ROOT).as_posix()] = digest(PREREQUISITE)
    # Bind every owner-local Python module actually imported by this trial.
    import sys
    for module in tuple(sys.modules.values()):
        file = getattr(module, '__file__', None)
        if file:
            path = Path(file).resolve()
            if path.suffix == '.py' and path.parent == Path(__file__).resolve().parent:
                key = path.relative_to(ROOT).as_posix()
                if key in pins:
                    assert pins[key] == digest(path), f'Stale prerequisite: {key}'
                pins[key] = digest(path)
    assert all(digest(ROOT / file) == expected for file, expected in pins.items())
    store = json.loads(STORE.read_text(encoding='utf-8'))
    projectors = tuple(tuple(tuple(decode(z) for z in row) for row in p) for p in store['face_projectors'])

    # All-input identities: anti-Hermitian Clifford/quaternion generators imply
    # Re <Ea z,Eb z> = delta_ab and Re <z,Ea z> = 0 for every unit z.
    for a in range(3):
        assert adj(E[a]) == sm(-1, E[a])
        assert gmm(E[a], E[a]) == sm(-1, I)
        for b in range(3):
            assert ma(gmm(adj(E[a]), E[b]), gmm(adj(E[b]), E[a])) == sm(2 if a == b else 0, I)
    assert gmm(E[0], E[1]) == E[2]
    assert ma(gmm(E[0], E[1]), sm(-1, gmm(E[1], E[0]))) == sm(2, E[2])
    # Formal numerator identity (1-s)^2 + 4s = (1+s)^2.
    assert [a + b for a, b in zip([1, -2, 1], [0, 4, 0])] == [1, 2, 1]
    decoder = sm(F(1, 2), combine([1] * 4, tuple(gmm(p, p) for p in projectors)))
    assert decoder == I

    samples = ((G1, G0), (G0, G1), ((F(3, 5), F(0)), (F(0), F(4, 5))),
               ((F(6, 7), F(0)), (F(3, 7), F(2, 7))))
    local_frames = []
    for z in samples:
        assert inner(z, z) == G1
        frame = tuple(act(matrix, z) for matrix in E)
        assert all(inner(z, v)[0] == 0 for v in frame)
        assert tuple(tuple(inner(a, b)[0] for b in frame) for a in frame) == tuple(tuple(F(a == b) for b in range(3)) for a in range(3))
        assert real_rank(list(zip(*(flat(v) for v in frame)))) == 3
        vertical = tuple(gm(GI, x) for x in z)
        coefficients = tuple(inner(v, vertical)[0] for v in frame)
        assert sum(x * x for x in coefficients) == 1
        assert act(combine(coefficients), z) == vertical
        # A full state has a unique SU(2) matrix taking (1,0) to z.
        lift = ((z[0], gs(-1, gc(z[1]))), (z[1], gc(z[0])))
        assert act(lift, (G1, G0)) == z and gmm(adj(lift), lift) == I
        for t in product((F(-1), F(0), F(1, 2)), repeat=3):
            c = chart(t)
            assert gmm(adj(c), c) == I
            state = act(c, z)
            assert inner(state, state) == G1
            assert act(adj(c), state) == z
            # Scaled exact-field encoder K and decoder K*/2 retain full phase.
            blocks = tuple(act(p, state) for p in projectors)
            recovered = tuple(gs(F(1, 2), gt(act(projectors[j], blocks[j])[i] for j in range(4))) for i in range(2))
            assert recovered == state
            s = sum(x * x for x in t)
            if s:
                assert chart(tuple(-x / s for x in t), True) == c
        assert act(chart((F(0),) * 3, True), z) == tuple(gs(-1, x) for x in z)
        local_frames.append({'spinor': z, 'directions': frame, 'phase_direction_coefficients': coefficients})

    quaternions = {tuple(F(s if k == j else 0) for k in range(4)) for j in range(4) for s in (-1, 1)}
    quaternions.update(tuple(F(s, 2) for s in signs) for signs in product((-1, 1), repeat=4))
    for q in quaternions:
        u = spin(q)
        rotated = tuple(gmm(gmm(u, e), adj(u)) for e in E)
        coordinates = tuple(tuple(gt(gmm(adj(E[a]), rotated[b])[i][i] for i in range(2))[0] / 2 for b in range(3)) for a in range(3))
        for b in range(3):
            assert combine(tuple(coordinates[a][b] for a in range(3))) == rotated[b]
        assert all(sum(coordinates[k][a] * coordinates[k][b] for k in range(3)) == F(a == b) for a in range(3) for b in range(3))
        assert determinant(coordinates) == 1

    # Source-only direction pairs anticommute in every signed sector. A supplied
    # chart can instead provide coordinate-dependent transports with equal ends;
    # this explicitly extends the finite source action set, rather than hiding it.
    native_actions = {spin(q) for q in quaternions}
    grid = {t: chart(t) for t in product((F(-1), F(0), F(1)), repeat=3)}
    K = tuple(row for p in projectors for row in p)
    N = sm(F(1, 2), gmm(K, adj(K)))
    stored_N = [[G0 for _ in range(8)] for _ in range(8)]
    for arrow in store['arrows']:
        if arrow['stage'] == 'N':
            stored_N[arrow['target']][arrow['source']] = decode(arrow['weight'])
    assert N == tuple(map(tuple, stored_N))
    for c in grid.values():
        assert gmm(adj(c), c) == I
        ingress = gmm(K, c)
        egress = sm(F(1, 2), gmm(adj(c), adj(K)))
        assert gmm(egress, ingress) == I
        sustained = gmm(ingress, egress)
        assert sustained == N and gmm(sustained, sustained) == sustained

    sector_records = []
    origin = (F(0),) * 3
    for omitted in range(3):
        axes = tuple(a for a in range(3) if a != omitted)
        for signs in product((-1, 1), repeat=2):
            corner = list(origin)
            for axis, sign in zip(axes, signs):
                corner[axis] = F(sign)
            corner = tuple(corner)
            A, B = tuple(sm(sign, E[axis]) for axis, sign in zip(axes, signs))
            assert gmm(A, B) == sm(-1, gmm(B, A))
            assert gmm(adj(gmm(A, B)), gmm(B, A)) == sm(-1, I)
            ordered = []
            for order in (axes, tuple(reversed(axes))):
                current = list(origin)
                transport = I
                for axis in order:
                    previous = tuple(current)
                    current[axis] = corner[axis]
                    step = gmm(grid[tuple(current)], adj(grid[previous]))
                    transport = gmm(step, transport)
                assert transport == grid[corner]
                ordered.append(transport)
            assert ordered[0] == ordered[1]
            assert grid[corner] not in native_actions
            sector_records.append({'omitted_direction': omitted + 1, 'signed_axes': tuple(zip((a + 1 for a in axes), signs)),
                                   'supplied_corner_transport': grid[corner], 'native_order_comparison': '-I',
                                   'supplied_coordinate_orders_agree': True})
    assert len(sector_records) == 12
    for signs in product((-1, 1), repeat=3):
        for order in permutations(range(3)):
            current = list(origin)
            transport = I
            for axis in order:
                previous = tuple(current)
                current[axis] = F(signs[axis])
                step = gmm(grid[tuple(current)], adj(grid[previous]))
                transport = gmm(step, transport)
            assert transport == grid[tuple(map(F, signs))]
    native_grid_count = sum(c in native_actions for c in grid.values())
    assert native_grid_count == 15 and len(grid) - native_grid_count == 12

    loop = gmm(gmm(gmm(adj(E[1]), adj(E[0])), E[1]), E[0])
    assert loop == sm(-1, I)
    assert density(act(loop, samples[2])) == density(samples[2])
    assert act(loop, samples[2]) != samples[2]
    # Exact inverse paths recover; the arbitrary commutator loop is not identity.
    for e in E:
        assert gmm(adj(e), e) == I
    assert all(digest(ROOT / file) == expected for file, expected in pins.items())
    checks = {
        'prerequisite_passed_and_all_source_pins_fresh': True,
        'three_source_generators_are_antihermitian_and_square_to_minus_identity': True,
        'all_input_real_gram_identity_gives_three_independent_tangent_directions': True,
        'rational_three_coordinate_chart_has_exact_unitarity_identity': True,
        'sampled_two_chart_overlap_and_missing_antipode_are_retained': True,
        'all_sampled_chart_states_recover_through_existing_face_blocks': True,
        'phase_direction_is_in_the_three_frame_span_on_all_samples': True,
        'each_sample_has_unique_explicit_su2_lift_from_reference': True,
        'all_24_source_rotations_transport_the_frame_by_so3_matrices': True,
        'individual_inverse_transports_recover_exactly': True,
        'noncommuting_direction_operations_have_known_minus_identity_loop': True,
        'all_12_native_signed_direction_pairs_have_minus_identity_order_comparison': True,
        'all_12_supplied_coordinate_sector_orders_have_identical_endpoints': True,
        'supplied_coordinate_port_pairs_recover_and_satisfy_fourfold_identity': True,
        'all_8_supplied_three_coordinate_corners_have_six_agreeing_orders': True,
        'supplied_coordinate_model_explicitly_requires_non_native_rotations': True,
        'all_bound_source_inputs_unchanged': True,
    }
    report = {
        'schema': 'marici.electron-three-direction-trial.v1',
        'verification_passed': all(checks.values()), 'checks': checks,
        'interpretation': 'n=3 counts all local real directions of the declared normalized spinor, including phase. It does not include charge, position, momentum or internal particle structure.',
        'candidate': '[z; (E1 z, E2 z, E3 z)] on the normalized spinor sphere S3',
        'generators': E, 'sample_frames': local_frames,
        'chart': 'spin((1-|t|^2,2t1,2t2,2t3)/(1+|t|^2)) z; opposite chart has an overall minus sign; overlap t maps to -t/|t|^2.',
        'global_frame_boundary': 'S3 has a global three-frame supplied by the actual quaternion generators. One real coordinate chart still misses a point. The phase direction is a state-dependent combination of this frame, not globally one fixed generator.',
        'sector_boundary': 'Twelve finite coordinate-sector tests, recoverable linear port pairs and six-order comparisons at eight three-coordinate corners pass for SUPPLIED coordinate-dependent SU(2) transports. Twelve corner matrices lie outside the 24 native rotations. This is a conditional coordinate realization on the existing carrier, not a construction from the finite native generators alone, a complete higher capability complex, or a minimality proof.',
        'sector_records': sector_records,
        'supplied_transport': {'rule': 'T(target,source)=C(target) C(source)* for the rational chart C.',
                               'grid_vertices': len(grid), 'native_vertex_matrices': native_grid_count,
                               'additional_vertex_matrices': len(grid) - native_grid_count,
                               'ports': 'i=K C, o=C* K*/2; oi=I2, io=N, (io)^2=io. K=sqrt(2)J is the declared exact-field scaling of the native encoder.',
                               'boundary': 'Chart-edge transport is supplied, not the constant native generator on every parallel edge. Replacing the latter changes the capability/cost interface.'},
        'source_accounting': {'native_transfers': 144, 'candidate_three_products': [108, 432, 1296], 'candidate_sum': 1836,
                              'boundary': 'Choosing n=3 gives the same proposed sum as any three-direction packet. This is not an electron mass calculation or an electron/proton discriminator.'},
        'scope': 'Exact all-input matrix identities plus rational sampled chart/decoder/phase checks and all 24 finite source actions; not proof-assistant formalization or a physical particle assignment.',
        'source_sha256': pins,
    }
    OUT.write_text(json.dumps(serial(report), indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'verification_passed': report['verification_passed'], 'checks': checks, 'receipt': str(OUT.relative_to(ROOT))}, indent=2))


if __name__ == '__main__':
    main()
