"""Iteration 6: conditional driven emission, including source and work ledger."""
from dataclasses import replace
from fractions import Fraction as F
from pathlib import Path
import json

import check_photon_momentum_wavepacket as previous
from photon_maxwell_adapter import Q, ZERO, ONE, I, SQRT3, mv, mm
from photon_source_emission import (
    MatchedPulse, PhotonEmissionLedger, AffineFrequencyPhase, free_operator_phase,
    matching_drive_phase, dagger, norm, expectation,
)


def rejects(fn):
    try:
        fn()
    except (ValueError, TypeError):
        return
    raise AssertionError('Invalid emission model was accepted')


def matrix_sum(a, b):
    return tuple(tuple(x + y for x, y in zip(r, s)) for r, s in zip(a, b))


def main():
    packet_ledger, packets = previous.main()  # fresh continuum and all prior closures
    emitter = PhotonEmissionLedger(packet_ledger)
    I3 = tuple(tuple(ONE if i == j else ZERO for j in range(3)) for i in range(3))
    I2 = ((ONE, ZERO), (ZERO, ONE))
    excitation = ((ZERO, ZERO, ZERO), (ZERO, ONE, ZERO), (ZERO, ZERO, ONE))
    number = ((ZERO, ZERO, ZERO), (ZERO, ZERO, ZERO), (ZERO, ZERO, ONE))
    source_excitation = ((ZERO, ZERO, ZERO), (ZERO, ONE, ZERO), (ZERO, ZERO, ZERO))
    profiles = packets
    pulses = (MatchedPulse(1, 0), MatchedPulse(0, 1), MatchedPulse(F(3, 5), F(4, 5)),
              MatchedPulse(F(1, 2), SQRT3 / 2, I), MatchedPulse(0, -1, Q(F(3, 5)) + I * Q(F(4, 5))))
    outcomes = []
    for pulse in pulses:
        U = pulse.unitary()
        assert mm(dagger(U), U) == mm(U, dagger(U)) == I3
        assert mm(excitation, U) == mm(U, excitation)
        K0, K1 = pulse.kraus()
        assert matrix_sum(mm(dagger(K0), K0), mm(dagger(K1), K1)) == I2
        for packet in profiles:
            event = emitter.emit(packet, pulse, gap=F(1), duration=F(3, 2))
            p0, p1 = emitter.probabilities(event)
            assert p0 == pulse.cosine ** 2 and p1 == pulse.sine ** 2 and p0 + p1 == ONE
            assert expectation(event.joint_output, excitation) == ONE
            assert expectation(event.joint_output, number) == p1
            assert expectation(event.joint_output, source_excitation) == p0
            assert emitter.field_density(event) == ((p0, ZERO), (ZERO, p1))
            assert emitter.source_density(event) == ((p1, ZERO), (ZERO, p0))
            audit = emitter.energy_audit(event)
            assert audit['final_free_energy'] - audit['initial_free_energy'] == audit['mean_external_work']
            assert audit['TPM_work_second_moment'] - audit['mean_external_work'] ** 2 == audit['TPM_work_variance']
            if p1 == ZERO:
                rejects(lambda event=event: emitter.herald_packet(event))
            else:
                heralded = emitter.herald_packet(event)
                assert heralded.profile_parent is packet and heralded.emission is event
                assert heralded.schrodinger_free_phase == AffineFrequencyPhase(-event.duration, 0)
                assert packet_ledger.norm_squared(heralded.profile_parent) == ONE
                # An optional fixed end-time precompensation can target the
                # unevolved profile, but is additional coherent drive data.
                assert heralded.schrodinger_free_phase.times(AffineFrequencyPhase(event.duration, 0)) == AffineFrequencyPhase(0, 0)
            for rate, derivative in ((Q(F(2, 3)), ZERO), (Q(F(-1, 5)), Q(F(3, 7)))):
                delta = Q(packet.profile.mean_momentum()[0] - event.gap)
                expected_power = 2 * rate * pulse.sine * pulse.cosine * delta
                assert emitter.instantaneous_power(event, rate, derivative) == expected_power
                # d/dt[c^2 Omega+s^2 <omega>] with theta_dot=g.
                direct_derivative = -2 * pulse.cosine * rate * pulse.sine * event.gap + 2 * pulse.sine * rate * pulse.cosine * packet.profile.mean_momentum()[0]
                assert expected_power == direct_derivative
            outcomes.append({'cosine': [str(x) for x in pulse.cosine.parts],
                             'sine': [str(x) for x in pulse.sine.parts],
                             'source_and_field_probabilities_sum_to_one': True})

    packet = packets[0]
    full = emitter.emit(packet, MatchedPulse(0, 1), gap=F(1), duration=F(2))
    assert full.joint_output == (ZERO, ZERO, -I)
    assert emitter.probabilities(full) == (ZERO, ONE)
    assert emitter.source_density(full) == ((ONE, ZERO), (ZERO, ZERO))
    assert emitter.herald_packet(full).profile_parent is packet
    audit = emitter.energy_audit(full)
    assert audit['initial_free_energy'] == ONE
    assert audit['final_free_energy'] == Q(F(49, 54))
    assert audit['mean_external_work'] == Q(F(-5, 54))
    assert audit['TPM_work_variance'] == Q(F(799, 23328))

    # Matching the source gap to mean photon energy does not close the energy
    # ledger. The exact full-continuum commutator norm remains the variance.
    mean_energy = packet.profile.mean_momentum()[0]
    matched_mean = emitter.emit(packet, MatchedPulse(0, 1), gap=mean_energy)
    matched_audit = emitter.energy_audit(matched_mean)
    assert matched_audit['mean_external_work'] == ZERO
    assert matched_audit['free_commutator_on_excited_vacuum_norm_squared'] == Q(F(799, 23328))
    assert matched_audit['TPM_work_variance'] == Q(F(799, 23328))
    for gap in (F(1, 2), F(1), mean_energy, F(2)):
        event = emitter.emit(packet, MatchedPulse(0, 1), gap=gap)
        info = emitter.energy_audit(event)
        assert info['free_commutator_on_excited_vacuum_norm_squared'] == info['packet_energy_variance'] + Q(mean_energy - gap) ** 2
    positive_work = emitter.energy_audit(emitter.emit(packet, MatchedPulse(0, 1), gap=F(1, 2)))
    assert positive_work['mean_external_work'] == Q(F(11, 27))

    # The ground source plus field vacuum stays dark for every control pulse.
    for pulse in pulses:
        dark = emitter.emit(packet, pulse, source_input=(ONE, ZERO))
        assert dark.joint_output == (ONE, ZERO, ZERO)
        assert emitter.probabilities(dark) == (ONE, ZERO)
        assert emitter.energy_audit(dark)['mean_external_work'] == ZERO
        rejects(lambda dark=dark: emitter.herald_packet(dark))
    # A source superposition produces vacuum/one-photon coherence. It is wrong
    # to replace every unconditional field output by the diagonal excited-source mixture.
    coherent = emitter.emit(packet, MatchedPulse(F(3, 5), F(4, 5)), source_input=(Q(F(3, 5)), Q(F(4, 5))))
    rho = emitter.field_density(coherent)
    assert rho[0][1] != ZERO and rho[1][0] == rho[0][1].conjugate()
    assert rho[0][0] + rho[1][1] == ONE
    assert expectation(coherent.joint_output, excitation) == Q(F(16, 25))
    assert emitter.probabilities(coherent)[1] == Q(F(256, 625))
    # Kraus sum reproduces the source reduced density including coherences.
    source_rho = ((ZERO, ZERO), (ZERO, ZERO))
    for K in coherent.pulse.kraus():
        branch = mv(K, coherent.source_input)
        source_rho = matrix_sum(source_rho, tuple(tuple(x * y.conjugate() for y in branch) for x in branch))
    assert source_rho == emitter.source_density(coherent)

    # A full transfer twice is absorption/re-excitation, not two emissions from
    # an undepleted source. The exact joint unitary retains both directions.
    Ufull = MatchedPulse(0, 1).unitary()
    twice = mv(Ufull, full.joint_output)
    assert twice == (ZERO, -ONE, ZERO)
    assert expectation(twice, number) == ZERO and expectation(twice, source_excitation) == ONE
    reverse = MatchedPulse(0, -1).unitary()
    assert mv(reverse, full.joint_output) == (ZERO, ONE, ZERO)

    # The spectral precompensation is required in the Schrödinger picture.
    # Exact affine phases avoid numerically rounding continuum exponentials.
    identity_phase = AffineFrequencyPhase(0, 0)
    for t in (F(0), F(1, 3), F(2), F(7, 5)):
        for gap in (F(1), mean_energy):
            free = free_operator_phase(t, gap)
            control = matching_drive_phase(t, gap)
            assert free.times(control) == identity_phase
            if t:
                assert free != identity_phase  # an unshaped stationary coupling does not cancel
    # Drive shape and source gap are not selected by the seed. Same packet,
    # different pulse area: probabilities change without changing its shape.
    partial = emitter.emit(packet, MatchedPulse(F(3, 5), F(4, 5)))
    assert emitter.probabilities(partial)[1] == Q(F(16, 25))
    assert emitter.herald_packet(partial).profile_parent is emitter.herald_packet(full).profile_parent
    assert emitter.deconstruct(full) == (packet, (ZERO, ONE), full.pulse, F(1), F(2))

    foreign = PhotonEmissionLedger(packet_ledger)
    foreign_event = foreign.emit(packet, MatchedPulse(0, 1))
    rejects(lambda: emitter.resolve(foreign_event))
    rejects(lambda: emitter.resolve(replace(full)))
    rejects(lambda: emitter.emit(replace(packet), MatchedPulse(0, 1)))
    rejects(lambda: emitter.emit(packet, MatchedPulse(0, 1), gap=0))
    rejects(lambda: emitter.emit(packet, MatchedPulse(0, 1), duration=0))
    rejects(lambda: emitter.emit(packet, MatchedPulse(0, 1), source_input=(ONE, ONE)))
    rejects(lambda: emitter.emit(packet, MatchedPulse(0, 1), source_input=(ONE,)))
    rejects(lambda: MatchedPulse(1, 1))
    rejects(lambda: MatchedPulse(0, 1, Q(2)))
    rejects(lambda: MatchedPulse(0.1, 1))
    rejects(lambda: AffineFrequencyPhase(0.1, 0))
    rejects(lambda: emitter.instantaneous_power(full, I))

    report = {
        'iteration': 6,
        'status': 'conditional_driven_emission_constructed; local_source_realization_and_seed_selection_open',
        'interaction_picture': 'V_I(t)=g(t)[zeta sigma_- A_psi^dagger+conjugate(zeta) sigma_+ A_psi]',
        'schrodinger_coupling_phase': 'exp[-i(omega-Omega)t]',
        'initial_excited_vacuum_output': 'cos(theta)|e,0>-i zeta sin(theta)|g,psi> in the interaction picture',
        'physical_output_at_T': 'photon profile exp(-i omega T) psi(k); optional exp(+i omega T) precompensation is extra drive data',
        'pulse_area': 'theta=integral g(t)dt; a theta=pi/2 matched pulse gives complete transfer',
        'probability_controls': outcomes,
        'full_transfer': {'emission_probability': 1, 'source_ground_probability': 1,
                          'gap': '1', 'mean_photon_energy': '49/54', 'mean_external_work': '-5/54',
                          'TPM_work_variance': '799/23328'},
        'matched_mean_gap_control': {'mean_work': '0', 'free_commutator_norm_squared': '799/23328',
                                    'energy_conservation_not_established': True},
        'passed': ['Hermitian matched-control unitary', 'total excitation conservation', 'source depletion',
                   'vacuum/no-emission branch retained', 'complete vacuum/one-packet source instrument',
                   'ground-vacuum dark control', 'coherent-source field coherence', 'reabsorption/reversal',
                   'mean energy and work-moment ledger', 'instantaneous power identity',
                   'spectral drive compensation and outgoing free phase retained'],
        'not_claimed': ['a local electromagnetic current realizes the engineered global form factor',
                        'autonomous energy conservation of source plus field',
                        'closed source recoil or angular-momentum budget', 'pulse/coupling/gap from the seed',
                        'a laboratory apparatus or measured emission probability'],
        'next_action': 'Audit whether the global mode-matched coupling can arise from a conserved local source current, and whether the compact momentum top-hat requires noncompact source support or approximation.'}
    dest = Path(__file__).resolve().parents[1] / 'results' / 'photon-source-emission.json'
    dest.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print('PASS: conditional source-field unitary emits the normalized packet with probability sin^2(theta).')
    print('PASS: full pulse depletes the source; no-emission, coherent-source, dark and reabsorption controls pass.')
    print('PASS: exact drive/work ledger; mean-gap matching still leaves nonzero broadband energy commutator.')
    print('BOUNDARY: engineered mode-matched interaction, not yet a local source derived from packet data.')
    print('Report: research/nima/results/photon-source-emission.json')
    return emitter, full


if __name__ == '__main__':
    main()
