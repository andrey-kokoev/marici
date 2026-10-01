"""Iteration 3: Lorentz transport and null little-group action, conditionally."""
from dataclasses import replace
from fractions import Fraction as F
from pathlib import Path
import json

import check_photon_maxwell_adapter as previous
from photon_maxwell_adapter import (
    Q, ZERO, ONE, SQRT3, I, ETA, SeedMaxwellAdapter, mv, mm, transpose,
    minkowski, hermitian_physical, field_strength, maxwell_operator,
)
from photon_lorentz_transport import (
    IDENTITY, LorentzMap, PhotonTransportLedger, real_positive, determinant,
)


def rejects(fn):
    try:
        fn()
    except (ValueError, TypeError):
        return
    raise AssertionError('Invalid Lorentz transport was accepted')


def main():
    adapter, old_waves = previous.main()  # fresh candidate + Maxwell closure
    ledger = PhotonTransportLedger(adapter)
    plus, minus = (wave.seed_coefficients for wave in old_waves)
    mixed = tuple(a + b for a, b in zip(plus, minus))
    origins = tuple(ledger.start(seed) for seed in (plus, minus, mixed))
    k0 = adapter.momentum
    assert real_positive(Q(2) - SQRT3)
    assert real_positive(SQRT3 - ONE)
    assert not real_positive(SQRT3 - Q(2))
    assert not real_positive(ONE - SQRT3)
    assert not real_positive(ZERO)
    rejects(lambda: real_positive(I))

    rotations = (LorentzMap.rotation(1, 0, 1), LorentzMap.rotation(2, F(3, 5), F(4, 5)),
                 LorentzMap.rotation(3, F(1, 2), SQRT3 / 2))
    boosts = (LorentzMap.boost(1, F(5, 4), F(3, 4)),
              LorentzMap.boost(2, F(13, 12), F(5, 12)),
              LorentzMap.boost(3, 2, SQRT3))
    N = LorentzMap.null_rotation(F(2, 3), F(-3, 5))
    transforms = rotations + boosts + (N,)
    frame_reports = []
    currents = ((ONE, ZERO, ZERO, ONE), (ZERO, ONE, ZERO, ZERO),
                (ZERO, ZERO, ONE, ZERO), (Q(2), Q(3), Q(5), Q(2)))
    for transform in transforms:
        assert determinant(transform.matrix) == ONE
        assert transform.inverse().after(transform).matrix == IDENTITY
        assert transform.after(transform.inverse()).matrix == IDENTITY
        for origin in origins:
            transported = ledger.transport(origin, transform)
            assert transported.origin is origin.origin
            assert transported.origin.packets is origin.origin.packets
            assert ledger.decode(transported) == origin.origin.seed_coefficients
            assert minkowski(transported.momentum, transported.momentum) == ZERO
            assert real_positive(transported.momentum[0])
            assert hermitian_physical(transported.polarization, transported.polarization) == hermitian_physical(
                origin.polarization, origin.polarization)
            original_F = field_strength(origin.momentum, origin.polarization)
            transported_F = field_strength(transported.momentum, transported.polarization)
            assert transported_F == mm(transform.matrix, mm(original_F, transpose(transform.matrix)))
            assert maxwell_operator(transported.momentum) == mm(transform.matrix,
                mm(maxwell_operator(origin.momentum), transform.inverse().matrix))
            for current in currents:
                j = mv(transform.matrix, current)
                assert minkowski(transported.momentum, j) == ZERO
                assert minkowski(j, transported.polarization) == minkowski(current, origin.polarization)
            returned = ledger.transport(transported, transform.inverse())
            assert returned.momentum == origin.momentum and returned.polarization == origin.polarization
            assert returned.frame.matrix == IDENTITY
            assert ledger.decode(returned) == origin.origin.seed_coefficients
            assert returned.label != origin.label
            assert ledger.history(returned) == (origin, transported, returned)
            parent, operation, saved_transform, parameter = ledger.deconstruct(transported)
            assert parent is origin and operation == 'lorentz' and saved_transform is transform and parameter == ZERO
            alpha = Q(F(2, 7), F(1, 3), F(-1, 5), F(1, 11))
            # Gauge then transport equals transport then gauge at the level of
            # fields/frames, but the actual operation histories are retained.
            route1 = ledger.transport(ledger.regauge(origin, alpha), transform)
            route2 = ledger.regauge(transported, alpha)
            assert route1.momentum == route2.momentum
            assert route1.polarization == route2.polarization
            assert route1.frame == route2.frame
            assert route1.label != route2.label
            assert ledger.decode(route1) == ledger.decode(route2) == origin.origin.seed_coefficients
        frame_reports.append({'future_null_preserved': True, 'seed_round_trip': True,
                              'Maxwell_covariance': True, 'field_strength_tensor_covariance': True})

    # Composition in the declared Lorentz model; noncommuting transformations
    # must retain their order. Sequential and composite histories are different.
    for left in transforms[:4]:
        for right in transforms[3:6]:
            sequential = ledger.transport(ledger.transport(origins[0], right), left)
            direct = ledger.transport(origins[0], left.after(right))
            assert sequential.frame == direct.frame
            assert sequential.momentum == direct.momentum and sequential.polarization == direct.polarization
            assert len(ledger.history(sequential)) == 3 and len(ledger.history(direct)) == 2
    bx, by = boosts[:2]
    assert bx.after(by).matrix != by.after(bx).matrix
    assert ledger.transport(origins[0], bx.after(by)).momentum != ledger.transport(origins[0], by.after(bx)).momentum
    example = ledger.transport(origins[0], bx)
    assert example.momentum == (Q(F(5, 4)), Q(F(3, 4)), ZERO, ONE)

    # E(2) little group at k0: null translations are pure gauge. In this frame
    # N(a,b) eps = eps + (a eps_x+b eps_y)/E * k0 for transverse representatives.
    translations = ((Q(F(2, 3)), Q(F(-3, 5))), (ONE, ZERO), (ZERO, SQRT3))
    for a, b in translations:
        null_map = LorentzMap.null_rotation(a, b)
        assert mv(null_map.matrix, k0) == k0
        for origin in origins:
            alpha = (a * origin.polarization[1] + b * origin.polarization[2]) / adapter.energy
            translated = ledger.transport(origin, null_map)
            assert translated.polarization == tuple(e + alpha * k for e, k in zip(origin.polarization, k0))
            assert adapter.decode(translated.polarization) == origin.origin.seed_coefficients
            assert field_strength(k0, translated.polarization) == field_strength(k0, origin.polarization)
        for c, d in translations:
            assert null_map.after(LorentzMap.null_rotation(c, d)).matrix == LorentzMap.null_rotation(a + c, b + d).matrix
    c, s = Q(F(1, 2)), SQRT3 / 2
    R = LorentzMap.rotation(3, c, s)
    for a, b in translations:
        conjugated = R.after(LorentzMap.null_rotation(a, b)).after(R.inverse())
        assert conjugated.matrix == LorentzMap.null_rotation(c * a - s * b, s * a + c * b).matrix

    # Carry the stabilizer to a noncollinear boosted/rotated frame. Translation
    # remains gauge there, not a new physical polarization coordinate.
    frame = boosts[0].after(rotations[1]).after(boosts[2])
    transported_origins = tuple(ledger.transport(origin, frame) for origin in origins)
    for a, b in translations:
        little = frame.after(LorentzMap.null_rotation(a, b)).after(frame.inverse())
        for origin, moved in zip(origins, transported_origins):
            acted = ledger.transport(moved, little)
            assert acted.momentum == moved.momentum
            alpha = (a * origin.polarization[1] + b * origin.polarization[2]) / adapter.energy
            assert acted.polarization == tuple(e + alpha * k for e, k in zip(moved.polarization, moved.momentum))
            assert field_strength(acted.momentum, acted.polarization) == field_strength(moved.momentum, moved.polarization)
            assert ledger.decode(acted) == origin.origin.seed_coefficients
    little_R = frame.after(R).after(frame.inverse())
    for origin, moved, helicity in zip(origins[:2], transported_origins[:2], (-1, 1)):
        acted = ledger.transport(moved, little_R)
        phase = c - I * helicity * s
        assert acted.momentum == moved.momentum
        assert acted.polarization == tuple(phase * e for e in moved.polarization)
        assert ledger.decode(acted) == origin.origin.seed_coefficients  # uses the transported frame
        # A fixed frame instead records the expected helicity phase.
        fixed_frame_decode = adapter.decode(mv(frame.inverse().matrix, acted.polarization))
        assert fixed_frame_decode == tuple(phase * x for x in origin.origin.seed_coefficients)

    # Momentum alone does not identify a polarization frame. Same momentum can
    # hide a little-group rotation; for a linear polarization it is not gauge.
    original_mixed = transported_origins[2]
    rotated_mixed = ledger.transport(origins[2], frame.after(R))
    assert original_mixed.momentum == rotated_mixed.momentum
    assert field_strength(original_mixed.momentum, original_mixed.polarization) != field_strength(
        rotated_mixed.momentum, rotated_mixed.polarization)
    wrong_frame_decode = adapter.decode(mv(frame.inverse().matrix, rotated_mixed.polarization))
    assert wrong_frame_decode != mixed
    assert ledger.decode(rotated_mixed) == mixed

    # A frame change need not change the energy parameter of the origin record;
    # energies measured in the transported frame follow Lorentz transformation.
    different_energy = SeedMaxwellAdapter(adapter.packets, F(7, 3))
    other_ledger = PhotonTransportLedger(different_energy)
    other = other_ledger.start(plus)
    other_moved = other_ledger.transport(other, bx)
    assert other_moved.momentum == tuple(Q(F(7, 3)) * x for x in example.momentum)
    assert other_ledger.decode(other_moved) == plus

    reflection = tuple(tuple(Q(-1 if i == j == 1 else int(i == j)) for j in range(4)) for i in range(4))
    time_reversal_proper = tuple(tuple(Q((-1 if i in (0, 3) else 1) if i == j else 0)
                                        for j in range(4)) for i in range(4))
    assert determinant(reflection) == Q(-1)
    assert determinant(time_reversal_proper) == ONE
    rejects(lambda: LorentzMap(reflection))
    rejects(lambda: LorentzMap(time_reversal_proper))
    rejects(lambda: LorentzMap(tuple(tuple(2 * x for x in row) for row in IDENTITY)))
    rejects(lambda: LorentzMap(((ONE,),)))
    rejects(lambda: LorentzMap.boost(1, 1, 1))
    rejects(lambda: LorentzMap.boost(0, 1, 0))
    rejects(lambda: LorentzMap.rotation(3, I, SQRT3))
    # This complex pair satisfies c^2+s^2=1; it must still fail the real
    # spacetime gate rather than enter as a complexified Lorentz transform.
    assert Q(F(5, 4)) ** 2 + (I * Q(F(3, 4))) ** 2 == ONE
    rejects(lambda: LorentzMap.rotation(3, Q(F(5, 4)), I * Q(F(3, 4))))
    rejects(lambda: ledger.transport(replace(origins[0]), bx))
    rejects(lambda: ledger.decode(other))
    rejects(lambda: ledger.transport(origins[0], bx.matrix))
    rejects(lambda: ledger.regauge(origins[0], 0.1))
    rejects(lambda: ledger.decode(replace(example, frame=LorentzMap(IDENTITY))))

    report = {
        'iteration': 3,
        'status': 'conditional_Lorentz_gauge_transport_verified; seed_selection_and_quantized_creation_open',
        'implementation': 'photon_lorentz_transport.PhotonTransportLedger',
        'tested_frames': frame_reports,
        'exact_noncollinear_example': 'k=(1,0,0,1) -> (5/4,3/4,0,1) under a supplied x boost',
        'passed': ['proper orthochronous metric/inverse checks', 'future null momentum and transverse norm',
                   'Maxwell operator and field-strength tensor covariance', 'transported conserved-current pairing',
                   'frame-aware inverse decoding of the exact six seed coefficients',
                   'sequential/composite transport equality with distinct retained histories',
                   'Lorentz-gauge commuting square', 'null little-group translations act only by gauge',
                   'little-group E(2) composition and rotation conjugation',
                   'helicity rotation phases in a noncollinear transported frame'],
        'negative_controls': ['improper/time-reversing/non-Lorentz/complex maps', 'bad dimensions and boost data',
                              'unregistered or foreign transport records', 'inexact gauge input',
                              'same-momentum wrong-polarization-frame decode'],
        'physical_boundary': 'Lorentz structure and Maxwell vector representation remain imported; no packet-derived spacetime, charge, one-photon creation operator or apparatus supplied',
        'next_action': 'Construct the conditional one-photon creation-state map for the transported helicity pair, with explicit Fock/CCR and normalization assumptions, and separate that construction from actual preparation and seed selection.'}
    dest = Path(__file__).resolve().parents[1] / 'results' / 'photon-lorentz-transport.json'
    dest.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print('PASS: frame-aware Lorentz/gauge transport preserves the retained seed and Maxwell class.')
    print('PASS: null little-group translations are gauge; transported rotations carry helicities +/-1.')
    print('PASS: round trips, composition and wrong-frame/forged-record controls.')
    print('BOUNDARY: conditional covariant polarization family, not packet-derived photon production.')
    print('Report: research/nima/results/photon-lorentz-transport.json')
    return ledger, origins


if __name__ == '__main__':
    main()
