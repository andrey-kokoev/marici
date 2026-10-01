"""Iteration 2: exact conditional Maxwell realization; no seed-only photon claim."""
from fractions import Fraction as F
from pathlib import Path
import json

import check_photon_two_packet_candidate as seed_check
from photon_maxwell_adapter import (
    Q, ZERO, ONE, SQRT3, I, ETA, SeedMaxwellAdapter, mv, mm, transpose, rank,
    minkowski, hermitian_physical, field_strength, maxwell_operator, validate_wave, rotation_z,
)


def rejects(fn):
    try:
        fn()
    except (ValueError, TypeError):
        return
    raise AssertionError('Invalid conditional Maxwell construction was accepted')


def main():
    candidates = seed_check.main()  # fresh exact source closure, not a cached report
    packets = candidates[0].packets
    adapter = SeedMaxwellAdapter(packets)
    seed_vectors = tuple(tuple(Q(r=a, t=b) for a, b in c.coefficients) for c in candidates)
    plus, minus = seed_vectors
    omega = Q(r=F(-1, 2), t=F(1, 2))
    samples = (ONE, SQRT3, I, I * SQRT3, Q(2, 3, 5, 7), Q(F(2, 7), F(-1, 5), 3, F(1, 11)))
    assert SQRT3 * SQRT3 == Q(3) and I * I == Q(-1)
    for a in samples:
        assert a * a.inverse() == ONE
        assert a.conjugate().conjugate() == a
        for b in samples:
            assert a * b == b * a
            assert (a * b).conjugate() == a.conjugate() * b.conjugate()
            for c in samples:
                assert a * (b + c) == a * b + a * c
                assert (a * b) * c == a * (b * c)

    k = adapter.momentum
    assert k == (ONE, ZERO, ZERO, ONE)
    assert minkowski(k, k) == ZERO
    E = ((ZERO, ZERO), (SQRT3, ZERO), (ZERO, -ONE), (ZERO, ZERO))
    pullback = mm(transpose(E), mm(ETA, E))
    assert pullback == ((Q(-3), ZERO), (ZERO, Q(-1)))
    M = maxwell_operator(k)
    assert rank(M) == 1  # 3-dimensional transverse solution space
    assert mv(M, k) == (ZERO,) * 4
    assert mm(M, E) == ((ZERO, ZERO),) * 4
    assert rank(tuple(tuple(row) + (k[i],) for i, row in enumerate(E))) == 3
    # The independent transverse columns plus one gauge direction exhaust the
    # Maxwell kernel. Quotienting the gauge line leaves exactly two dimensions.

    waves = tuple(adapter.encode(seed) for seed in seed_vectors)
    expected = ((ZERO, SQRT3, -I * SQRT3, ZERO), (ZERO, SQRT3, I * SQRT3, ZERO))
    assert tuple(w.polarization for w in waves) == expected
    assert all(w.packets == packets for w in waves)
    assert hermitian_physical(expected[0], expected[0]) == Q(6)
    assert hermitian_physical(expected[1], expected[1]) == Q(6)
    assert hermitian_physical(expected[0], expected[1]) == ZERO

    u = adapter.seed_from_coordinates(ONE, ZERO)
    w = adapter.seed_from_coordinates(ZERO, ONE)
    general = adapter.seed_from_coordinates(Q(2, 1, -3, F(1, 2)), Q(-1, 2, 1, 3))
    gauges = (ZERO, Q(F(3, 7)), I, Q(1, 2, 3, -1))
    for seed in seed_vectors + (u, w, general):
        original = adapter.encode(seed)
        assert adapter.decode(original.polarization) == seed
        base_F = field_strength(k, original.polarization)
        assert any(entry != ZERO for row in base_F for entry in row)
        for gauge in gauges:
            shifted = adapter.encode(seed, gauge)
            assert adapter.decode(shifted.polarization) == seed
            assert field_strength(k, shifted.polarization) == base_F
            assert hermitian_physical(shifted.polarization, shifted.polarization) == hermitian_physical(
                original.polarization, original.polarization)
        k_lower = tuple(sign * entry for sign, entry in zip((1, -1, -1, -1), k))
        assert tuple(sum((k_lower[mu] * base_F[mu][nu] for mu in range(4)), ZERO)
                     for nu in range(4)) == (ZERO,) * 4
        lower_F = mm(ETA, mm(base_F, ETA))
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    assert k_lower[a] * lower_F[b][c] + k_lower[b] * lower_F[c][a] + k_lower[c] * lower_F[a][b] == ZERO
    assert adapter.decode(k) == (ZERO,) * 6  # pure gauge is the zero quotient class

    # Continuous SO(2) action is DECLARED by the spacetime-vector adapter. Its
    # derivative assigns helicity using U(R_theta)=exp(-i*h*theta).
    Jz = ((ZERO,) * 4, (ZERO, ZERO, -ONE, ZERO),
          (ZERO, ONE, ZERO, ZERO), (ZERO,) * 4)
    rotations = ((ONE, ZERO), (ZERO, ONE), (Q(F(-1, 2)), SQRT3 / 2),
                 (Q(F(1, 2)), SQRT3 / 2), (Q(F(3, 5)), Q(F(4, 5))))
    for wave, helicity in zip(waves, (-1, 1)):
        epsilon = wave.polarization
        assert mv(Jz, epsilon) == tuple(-I * helicity * x for x in epsilon)
        for c, s in rotations:
            R = rotation_z(c, s)
            assert mm(transpose(R), mm(ETA, R)) == ETA
            assert mv(R, k) == k
            assert mv(R, epsilon) == tuple((c - I * helicity * s) * x for x in epsilon)
    for c, s in rotations:
        R = rotation_z(c, s)
        continuous_seed_action = ((c, s / SQRT3), (-SQRT3 * s, c))
        assert mm(R, E) == mm(E, continuous_seed_action)
        for d, t in rotations:
            assert mm(R, rotation_z(d, t)) == rotation_z(c * d - s * t, s * d + c * t)
    T = ((Q(F(-1, 2)), Q(F(1, 2))), (Q(F(-3, 2)), Q(F(-1, 2))))
    assert mm(rotation_z(Q(F(-1, 2)), SQRT3 / 2), E) == mm(E, T)
    assert mv(rotation_z(Q(F(-1, 2)), SQRT3 / 2), waves[0].polarization) == tuple(omega * x for x in waves[0].polarization)

    # Spin-four alias still agrees at the seed's C3 angle but does NOT extend
    # through this selected vector representation at pi/3.
    tau = Q(r=F(1, 2), t=F(1, 2))
    assert omega ** 4 == omega
    rotated = mv(rotation_z(Q(F(1, 2)), SQRT3 / 2), waves[0].polarization)
    assert rotated == tuple(tau * x for x in waves[0].polarization)
    assert rotated != tuple((tau ** 4) * x for x in waves[0].polarization)

    # A conserved-current pairing is gauge invariant only after conservation
    # has been declared. This is a kinematic Ward check, not a derived charge.
    conserved_currents = ((ONE, ZERO, ZERO, ONE), (ZERO, ONE, ZERO, ZERO),
                          (ZERO, ZERO, ONE, ZERO), (Q(2), Q(3), Q(5), Q(2)))
    for current in conserved_currents:
        assert minkowski(k, current) == ZERO
        for seed in seed_vectors:
            reference = minkowski(current, adapter.encode(seed).polarization)
            for gauge in gauges:
                assert minkowski(current, adapter.encode(seed, gauge).polarization) == reference
    nonconserved = (ONE, ZERO, ZERO, ZERO)
    assert minkowski(nonconserved, adapter.encode(plus, ONE).polarization) != minkowski(
        nonconserved, adapter.encode(plus).polarization)

    # Energy is an independent input: the SAME seed coefficients work at two
    # distinct positive null momenta. No seed frequency-to-energy law was used.
    second = SeedMaxwellAdapter(packets, F(7, 3))
    assert second.encode(plus).seed_coefficients == waves[0].seed_coefficients
    assert second.momentum != k
    assert second.encode(plus).polarization == waves[0].polarization
    assert second.decode(second.encode(plus, I).polarization) == plus

    rejects(lambda: adapter.encode((ZERO,) * 6))
    rejects(lambda: adapter.encode((ONE,) + (ZERO,) * 5))
    rejects(lambda: adapter.encode(plus[:-1]))
    rejects(lambda: adapter.decode((ZERO, ZERO, ZERO, ONE)))
    rejects(lambda: validate_wave(k, k))
    rejects(lambda: validate_wave((ZERO,) * 4, expected[0]))
    timelike = (Q(2), ZERO, ZERO, ONE)
    assert minkowski(timelike, timelike) == Q(3)
    assert mv(maxwell_operator(timelike), expected[0]) != (ZERO,) * 4
    rejects(lambda: validate_wave(timelike, expected[0]))
    rejects(lambda: SeedMaxwellAdapter(packets[::-1]))
    rejects(lambda: SeedMaxwellAdapter(packets, 0))
    rejects(lambda: SeedMaxwellAdapter(packets, -1))
    rejects(lambda: SeedMaxwellAdapter(packets, 0.1))
    rejects(lambda: rotation_z(1, 1))
    rejects(lambda: Q(0.1))

    report = {
        'iteration': 2,
        'status': 'conditional_Maxwell_adapter_verified; seed_only_photon_identification_open',
        'seed_order': [p.label for p in packets],
        'encoding': 'a*u+b*w -> epsilon=(0,sqrt(3)*a,-b,0)+alpha*k',
        'momentum': 'k=(E,0,0,E), supplied rational E>0; eta=diag(1,-1,-1,-1)',
        'helicity_convention': 'active R_z(theta), U=exp(-i*h*theta)',
        'candidate_mapping': {'g_plus': 'sqrt(3)*(0,1,-i,0), helicity -1',
                              'g_minus': 'sqrt(3)*(0,1,+i,0), helicity +1'},
        'exact_gates_passed': ['null nonzero momentum under the declared adapter',
                               'transversality', 'gauge-invariant field strength',
                               'free Maxwell and Bianchi equations', 'two-dimensional transverse gauge quotient',
                               'gauge-invariant decode to the original six coefficients',
                               'pullback transverse metric diag(3,1)', 'declared continuous rotation helicities +/-1',
                               'C3 incidence intertwiner', 'conditional conserved-current Ward pairing'],
        'added_not_derived': ['Minkowski spacetime and vector representation', '+z null momentum and energy',
                             'embedding and polarization orientation', 'gauge equivalence epsilon~epsilon+alpha*k',
                             'free Maxwell equation as physical target', 'conserved-current input'],
        'hostile_controls': ['spin-four alias fails the added pi/3 action', 'timelike momentum fails Maxwell gate',
                             'zero momentum', 'pure gauge or zero polarization', 'off-plane seed',
                             'nontransverse polarization', 'nonconserved-current gauge dependence',
                             'same seed at distinct supplied energies', 'wrong manifest and inexact inputs'],
        'open_gates': ['source selection of this spacetime adapter', 'Lorentz/gauge transport beyond the fixed +z frame',
                       'seed-derived electromagnetic charge/current coupling', 'quantized one-photon creation or physical preparation'],
        'next_action': 'Construct and test Lorentz/gauge transport of the adapted packet beyond the fixed null frame, retaining the seed identity and separating imported spacetime action from source derivation.'}
    dest = Path(__file__).resolve().parents[1] / 'results' / 'photon-maxwell-adapter.json'
    dest.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print('PASS: explicit conditional seed-to-Maxwell quotient map, with exact inverse on gauge classes.')
    print('PASS: nullness, transverse metric, Maxwell/Bianchi equations, helicity rotations and conditional Ward pairing.')
    print('BOUNDARY: spacetime, momentum, vector action and gauge law are added inputs; photon production is not derived.')
    print('Report: research/nima/results/photon-maxwell-adapter.json')
    return adapter, waves


if __name__ == '__main__':
    main()
