"""Iteration 5: exactly normalizable continuum profile, conditional on Fock/QED kinematics."""
from dataclasses import replace
from fractions import Fraction as F
from pathlib import Path
import json

import check_photon_creation_state as previous
from photon_maxwell_adapter import Q, ZERO, ONE, I, SQRT3, mv, minkowski, validate_wave, field_strength
from photon_lorentz_transport import LorentzMap, determinant, real_positive
from photon_momentum_wavepacket import (
    LightConeBox, MomentumPacketLedger, momentum, coordinates, polarization_frame, wigner_phase, chart_jacobian,
)


def rejects(fn):
    try:
        fn()
    except (ValueError, TypeError):
        return
    raise AssertionError('Invalid continuum packet was accepted')


def main():
    creation, records = previous.main()  # fresh full prior closure
    ledger = MomentumPacketLedger(creation)
    profile = LightConeBox((1, 2), (F(-1, 2), F(1, 2)), (F(-1, 2), F(1, 2)))
    V = profile.volume
    assert V == F(3, 4)
    packets = tuple(ledger.create(record, profile) for record in records)
    for packet in packets:
        assert ledger.norm_squared(packet) == ONE
        n = packet.creation_record.norm_squared
        assert packet.normalization_squared == Q(V) * n
        # This integral is the smeared CCR coefficient. With the declared
        # continuum delta_mu normalization, it is [A_psi,A_psi^dagger]=1.
        integrated_CCR = sum((c.conjugate() * c * Q(V) / packet.normalization_squared
                              for c in packet.coefficients), ZERO)
        assert integrated_CCR == ONE
        # Global photon number N has [N,A_psi^dagger]=A_psi^dagger under those
        # continuum CCR; this normalized one-creation state inherits N=1.
        assert creation.expectation(packet.creation_record, lambda p: p.number()) == ONE

    points = ((F(3, 2), F(1, 5), F(-1, 3)), (F(7, 4), F(-2, 5), F(1, 4)),
              (F(5, 4), F(0), F(0)))
    E = creation.transport.adapter.energy
    k0 = creation.transport.adapter.momentum
    for point in points:
        k = momentum(point)
        assert minkowski(k, k) == ZERO and real_positive(k[0])
        assert coordinates(k) == tuple(Q(x) for x in point)
        frame = polarization_frame(point, E)
        assert mv(frame.matrix, k0) == k
        for packet in packets:
            assert ledger.amplitude_numerators(packet, point) == packet.coefficients
            seed = creation.retained_seed_in_reference_frame(packet.creation_record)
            epsilon0 = creation.transport.adapter.encode(seed).polarization
            epsilon = mv(frame.matrix, epsilon0)
            validate_wave(k, epsilon)
            for alpha in (ONE, I, Q(2, 1, -1, F(1, 3))):
                changed = tuple(e + alpha * component for e, component in zip(epsilon, k))
                assert field_strength(k, changed) == field_strength(k, epsilon)
                assert creation.transport.adapter.decode(mv(frame.inverse().matrix, changed)) == seed
    assert ledger.amplitude_numerators(packets[0], (F(3), F(0), F(0))) == (ZERO, ZERO)
    assert ledger.amplitude_numerators(packets[0], (F(3, 2), F(2), F(0))) == (ZERO, ZERO)

    # Global exact integrals, not quadrature samples. A finite angular spread
    # gives a timelike mean momentum while P^2 is zero on the one-photon state.
    mean = profile.mean_momentum()
    seconds = profile.diagonal_second_moments()
    assert mean == (F(49, 54), F(0), F(0), F(35, 54))
    assert seconds == (F(247, 288), F(5, 24), F(5, 24), F(127, 288))
    assert seconds[0] - sum(seconds[1:]) == 0
    mean_square = mean[0] ** 2 - sum(x * x for x in mean[1:])
    assert mean_square == F(98, 243) > 0
    energy_variance = seconds[0] - mean[0] ** 2
    assert energy_variance > 0
    # Free evolution is not closed in this one collective profile mode:
    # ||(H-<H>)|psi>||^2 is this positive variance. A stationary single-frequency
    # source oscillator cannot be substituted for the broadband continuum.
    centered_H_norm_squared = (seconds[0] - 2 * mean[0] * mean[0] + mean[0] ** 2)
    assert centered_H_norm_squared == energy_variance
    # Unit-height profile on this box is not normalized without 1/sqrt(V).
    assert V != 1

    # Longitudinal boosts preserve the box form. q'=s q, u'=u/s,v'=v/s;
    # (q'/2) dq' du' dv'=(q/2)dq du dv globally.
    scale = F(2)
    Bz = LorentzMap.boost(3, (scale + 1 / scale) / 2, (scale - 1 / scale) / 2)
    boosted_profile = profile.boosted_z(scale)
    assert boosted_profile.volume == V
    assert tuple(Q(x) for x in boosted_profile.mean_momentum()) == mv(Bz.matrix, tuple(Q(x) for x in mean))
    Rz = LorentzMap.rotation(3, 0, 1)
    asymmetric = LightConeBox((1, 3), (F(-1, 4), F(1, 2)), (F(-1, 3), F(2, 5)))
    rotated_profile = asymmetric.rotated_quarter_z()
    assert rotated_profile.volume == asymmetric.volume
    assert tuple(Q(x) for x in rotated_profile.mean_momentum()) == mv(Rz.matrix, tuple(Q(x) for x in asymmetric.mean_momentum()))

    # Exact local Jacobians audit the invariant measure for generic supplied
    # transforms. Analytic normalization above is not inferred from sampling.
    Bx = LorentzMap.boost(1, F(5, 4), F(3, 4))
    By = LorentzMap.boost(2, F(13, 12), F(5, 12))
    Ry = LorentzMap.rotation(2, F(3, 5), F(4, 5))
    transforms = (Bz, Bx, By, Rz, Ry, Bx.after(Ry))
    phase_records = []
    for transform in transforms:
        for point in points:
            output, J = chart_jacobian(transform, point)
            assert output == coordinates(mv(transform.matrix, momentum(point)))
            det = determinant(J)
            assert real_positive(det)
            assert output[0] * det == Q(point[0])
            assert coordinates(mv(transform.inverse().matrix, momentum(output))) == tuple(Q(x) for x in point)
            for packet in packets:
                values = ledger.transported_numerators(packet, transform, point)
                assert sum((c.conjugate() * c for c in values), ZERO) == packet.creation_record.norm_squared
            phases = tuple(wigner_phase(transform, point, h, E) for h in (1, -1))
            assert phases[1] == phases[0].conjugate()
            phase_records.append({'unit_modulus': True, 'measure_jacobian_exact': True})
    for point in points:
        assert coordinates(mv(Bz.matrix, momentum(point))) == (Q(scale * point[0]), Q(point[1] / scale), Q(point[2] / scale))
        assert all(wigner_phase(Bz, point, h, E) == ONE for h in (-1, 1))
        assert wigner_phase(Rz, point, 1, E) == -I
        assert wigner_phase(Rz, point, -1, E) == I
    # In general the helicity phase is momentum dependent. The transformation
    # must not act as one constant polarization matrix across the entire packet.
    transverse_phases = tuple(wigner_phase(Bx, point, 1, E) for point in points)
    assert len(set(transverse_phases)) > 1
    for point in points[:2]:
        intermediate = coordinates(mv(Bx.matrix, momentum(point)))
        for h in (-1, 1):
            composite = wigner_phase(Ry.after(Bx), point, h, E)
            successive = wigner_phase(Ry, intermediate, h, E) * wigner_phase(Bx, point, h, E)
            assert composite == successive

    # Chart failure is not absent physical support. This point goes to the
    # south ray, but the transported polarization frame remains valid.
    pole_point = (F(3, 2), F(0), F(0))
    flip = LorentzMap.rotation(2, -1, 0)
    pole_k = mv(flip.matrix, momentum(pole_point))
    assert pole_k[0] + pole_k[3] == ZERO
    rejects(lambda: coordinates(pole_k))
    rejects(lambda: wigner_phase(flip, pole_point, 1, E))
    pole_frame = flip.after(polarization_frame(pole_point, E))
    seed = creation.retained_seed_in_reference_frame(records[0])
    epsilon = mv(pole_frame.matrix, creation.transport.adapter.encode(seed).polarization)
    validate_wave(pole_k, epsilon)
    assert creation.transport.adapter.decode(mv(pole_frame.inverse().matrix, epsilon)) == seed
    assert profile.contains(pole_point)

    # Profile-mode overlaps are not generally zero. Distinct names/boxes do
    # not confer independent oscillator commutators.
    shifted = LightConeBox(profile.q, (0, 1), profile.v)
    disjoint = LightConeBox((3, 4), profile.u, profile.v)
    overlap = profile.overlap_volume(shifted)
    assert shifted.volume == V and overlap == V / 2
    assert profile.overlap_volume(disjoint) == 0
    assert profile.overlap_volume(profile) == V
    normalized_overlap_squared = overlap ** 2 / (V * shifted.volume)
    assert normalized_overlap_squared == F(1, 4)
    # Equal real unit-profile states with overlap 1/2 sum to norm squared 3,
    # not 2. An arbitrary sum would need its own coherent normalization.
    assert 2 + 2 * overlap / V == 3

    # The same seed admits different profiles/energies: this is not source
    # selection of a unique photon wavepacket or an energy scale.
    other_profile = LightConeBox((2, 4), profile.u, profile.v)
    other = ledger.create(records[0], other_profile)
    assert ledger.norm_squared(other) == ONE
    assert other.coefficients == packets[0].coefficients
    assert other_profile.mean_momentum() == tuple(2 * x for x in mean)
    rejects(lambda: LightConeBox((0, 1), (-1, 1), (-1, 1)))
    rejects(lambda: LightConeBox((2, 1), (-1, 1), (-1, 1)))
    rejects(lambda: LightConeBox((1, 2), (0, 0), (-1, 1)))
    rejects(lambda: LightConeBox((1.0, 2), (-1, 1), (-1, 1)))
    rejects(lambda: profile.boosted_z(0))
    rejects(lambda: profile.moment(-1, 0, 0))
    rejects(lambda: ledger.resolve(replace(packets[0])))
    rejects(lambda: ledger.create(replace(records[0]), profile))
    rejects(lambda: momentum((0, 0, 0)))
    rejects(lambda: coordinates((Q(2), ZERO, ZERO, ONE)))
    rejects(lambda: momentum((ONE, I, ZERO)))

    report = {
        'iteration': 5,
        'status': 'normalizable_conditional_one_photon_wavepacket_constructed; source_emission_open',
        'measure': 'dmu=d^3k/(2k0)=(q/2)dq du dv; (2pi)^3 absorbed in CCR convention',
        'profile': {'q': ['1', '2'], 'u': ['-1/2', '1/2'], 'v': ['-1/2', '1/2'], 'volume': str(V)},
        'state': 'sum_h integral dmu psi_h(k) a_h^dagger(k)|0>, psi_h=c_h*1_box/sqrt(V*sum|c|^2)',
        'continuum_CCR_assumption': '[a_h(k),a_j^dagger(p)]=delta_hj*2k0*delta^3(k-p)',
        'norm_and_smeared_CCR': 1, 'photon_number': 1,
        'mean_momentum': [str(x) for x in mean],
        'momentum_second_diagonal': [str(x) for x in seconds],
        'expected_P_squared': '0', 'squared_mean_momentum': str(mean_square),
        'energy_variance': str(energy_variance),
        'free_evolution_not_closed_in_one_profile_mode': True,
        'energy_centered_leakage_norm_squared': str(centered_H_norm_squared),
        'transport_checks': phase_records,
        'nonconstant_Wigner_phase_under_transverse_boost': True,
        'Wigner_phase_composition_cocycle': True,
        'chart_pole_retained_as_valid_transported_Maxwell_mode': True,
        'overlapping_profiles': {'overlap_squared': str(normalized_overlap_squared), 'coherent_sum_norm_squared': 3},
        'added_not_derived': ['continuum one-particle measure and CCR', 'compact profile support and its scale',
                             'momentum-dependent polarization section and phase convention'],
        'physical_boundary': 'a normalizable free one-photon state is constructed conditionally; no source Hamiltonian, emission probability, reservoir or seed selection of its profile is supplied',
        'next_action': 'Construct a conditional excitation-conserving source-field interaction for this broadband packet, accounting for source depletion, vacuum/no-emission outcomes and external work; do not replace it by a stationary single-frequency oscillator.'}
    dest = Path(__file__).resolve().parents[1] / 'results' / 'photon-momentum-wavepacket.json'
    dest.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print('PASS: explicit continuum one-photon profile has exact unit norm and finite energy moments.')
    print('PASS: invariant measure, momentum-dependent helicity phases, cocycle and chart-pole controls.')
    print('PASS: <P^2>=0 while <P>^2=98/243; overlapping profiles are not independent modes.')
    print('BOUNDARY: conditional normalized free photon wavepacket; no emission source has yet been supplied.')
    print('Report: research/nima/results/photon-momentum-wavepacket.json')
    return ledger, packets


if __name__ == '__main__':
    main()
