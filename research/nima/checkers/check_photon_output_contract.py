"""Iteration 10: check available-photon claims and consolidate output routes."""
from fractions import Fraction as F
from pathlib import Path
import json

import check_photon_coherent_herald as previous
from photon_maxwell_adapter import Q, ZERO, ONE, I, SQRT3
from photon_creation_state import FockPolynomial, VACUUM, FOCK_ZERO
from photon_output_contract import (ideal_total_number_qnd, destructive_exact_one,
                                   one_count_in_tap, production_contract)


def rejects(fn):
    try:
        fn()
    except (ValueError, TypeError):
        return
    raise AssertionError('Unsupported output-photon certificate accepted')


def main():
    model = previous.main()
    p_plus, p_minus = VACUUM.create(1), VACUUM.create(-1)
    coherent_one = p_plus + p_minus.scaled(I)
    three = FockPolynomial((((1, 2), ONE),))
    mixed_number = VACUUM + coherent_one + three.scaled(Q(2))
    states = [FOCK_ZERO, VACUUM, coherent_one, three, mixed_number]
    states += [FockPolynomial((((np, nm), ONE),)) for np in range(5) for nm in range(5)]
    for state in states:
        accepted, rejected = ideal_total_number_qnd(state)
        kept, other = accepted.branches[0], rejected.branches[0]
        assert kept + other == state
        assert kept.inner(other) == ZERO
        assert accepted.weight() + rejected.weight() == state.inner(state)
        assert ideal_total_number_qnd(kept)[0].branches[0] == kept
        assert ideal_total_number_qnd(other)[0].weight() == ZERO
        assert kept.number() == kept
        assert accepted.retains_exactly_one() == (accepted.weight() != ZERO)
        absorbed = destructive_exact_one(state)
        assert absorbed.weight() == accepted.weight()  # same event POVM, different instrument
        assert absorbed.photon_number_numerator() == ZERO
        assert not absorbed.retains_exactly_one()
        for other_state in states:
            # Off-diagonal matrix elements certify the same success effect,
            # not merely its probabilities on number basis vectors.
            destructive_other = destructive_exact_one(other_state)
            qnd_other = ideal_total_number_qnd(other_state)[0]
            assert sum((a.inner(b) for a, b in zip(absorbed.branches, destructive_other.branches)), ZERO) == kept.inner(qnd_other.branches[0])

    assert ideal_total_number_qnd(coherent_one)[0].branches[0] == coherent_one
    # A coherent sum of absorbing branches would be the wrong CP instrument.
    cancellation = p_plus - p_minus
    destroyed = destructive_exact_one(cancellation)
    assert destroyed.weight() == Q(2)
    assert sum(destroyed.branches, FOCK_ZERO) == FOCK_ZERO
    # Merely observing one photon in the first mode accepts extra photons in
    # unmonitored modes. The correct total-number test rejects this input.
    one_in_each = FockPolynomial((((1, 1), ONE),))
    assert dict(one_in_each.terms)[(1, 1)] == ONE
    assert ideal_total_number_qnd(one_in_each)[0].weight() == ZERO
    assert ideal_total_number_qnd(three)[0].weight() == ZERO
    odd_input = coherent_one + three
    assert all(sum(n) % 2 == 1 for n, _ in odd_input.terms)
    assert odd_input != ideal_total_number_qnd(odd_input)[0].branches[0]

    # A click in a tap is subtraction, not QND certification of a surviving
    # photon. For the already odd source-heralded input, an exact ONE tap count
    # leaves only even numbers of transmitted photons.
    for state in (p_plus, coherent_one, three, odd_input):
        tap = one_count_in_tap(state, F(3, 5), F(4, 5))
        assert tap.weight() != ZERO
        assert all(sum(n) % 2 == 0 for branch in tap.branches for n, _ in branch.terms)
        assert not tap.retains_exactly_one()
    assert one_count_in_tap(p_plus, F(3, 5), F(4, 5)).photon_number_numerator() == ZERO
    tap_three = one_count_in_tap(three, F(3, 5), F(4, 5))
    assert tap_three.photon_number_numerator() == 2 * tap_three.weight()
    assert one_count_in_tap(VACUUM, F(3, 5), F(4, 5)).weight() == ZERO
    for photons in range(1, 9):
        state = FockPolynomial((((photons, 0), ONE),))
        result = one_count_in_tap(state, F(3, 5), F(4, 5))
        # Exact binomial one-reflected-photon probability, with input Fock norm
        # explicitly divided out instead of confusing monomials with unit kets.
        assert result.weight() / state.inner(state) == Q(photons * F(16, 25) * F(9, 25) ** (photons - 1))

    source_contract = production_contract(model, 'source_only')
    exact_contract = production_contract(model, 'ideal_total_number_qnd', assume_ideal_total_number_qnd=True)
    counter_contract = production_contract(model, 'destructive_counter')
    assert not source_contract['exact_available_one_photon']
    assert source_contract['infidelity_upper_bound'] == F(10, 6007)
    assert exact_contract['exact_available_one_photon']
    assert exact_contract['infidelity_upper_bound'] == 0
    assert exact_contract['success_lower_bound'] == F(9, 100)
    assert exact_contract['success_upper_bound'] == F(1, 11)
    assert counter_contract['available_photons_after_count'] == 0
    assert not counter_contract['exact_available_one_photon']
    assert not any(c['apparatus_derived'] for c in (source_contract, exact_contract, counter_contract))
    rejects(lambda: production_contract(model, 'ideal_total_number_qnd'))
    rejects(lambda: production_contract(model, 'ideal_total_number_qnd', assume_ideal_total_number_qnd='yes'))
    rejects(lambda: production_contract(model, 'click_means_photon_left'))
    rejects(lambda: one_count_in_tap(p_plus, F(1, 2), F(1, 2)))

    # Endpoint-normalized one-photon state: the exact Gaussian radiation norm
    # was checked earlier. The number projector preserves the entire wavepacket,
    # not just its photon number, because it acts as identity on the N=1 sector.
    assert model.current.gaussian_norm_over_pi() == Q(F(1, 2))
    assert model.mean_photon_number == F(1, 10)
    k = (Q(F(5, 4)), Q(F(3, 4)), ZERO, ONE)
    epsilon = (ZERO, Q(F(4, 5)), I, Q(F(-3, 5)))
    reference = model.current.reduced_emission(k, epsilon)
    for gauge in (ZERO, ONE, I):
        shifted = tuple(e + gauge * p for e, p in zip(epsilon, k))
        reduced_formula = SQRT3 * (k[0] * shifted[1].conjugate() - k[1] * shifted[0].conjugate())
        assert model.current.reduced_emission(k, shifted) == reduced_formula == reference

    report = {
        'iteration': 10,
        'status': 'conditional output contracts and instrument distinctions checked',
        'packet_order': ['AB', 'BC', 'CA', 'BA', 'AD', 'DB'],
        'seed_vector': ['1', '-1', '1/2', '-1', '1', '-1/2'],
        'conditional_one_photon_state': 'a_dagger(psi)|vac>; psi_h(k)=sqrt(6/pi)*(omega*epsilon_h,x^*-k_x*epsilon_h,0^*)*exp(-omega^2) in the declared unit-width Gaussian model',
        'routes': {
            'source_only': {'available_output': 'odd coherent superposition', 'one_photon_infidelity_upper_bound': '10/6007',
                            'herald_probability_interval': ['9/100', '1/10'], 'exact_one_photon': False},
            'additional_ideal_total_number_QND': {'available_output': 'exact |1_psi>', 'joint_success_probability': 'mu*exp(-mu)',
                                                  'at_mu_1_over_10_probability_interval': ['9/100', '1/11'],
                                                  'extra_assumption': 'ideal total-field-number Lueders instrument, with no photon loss or mode information leakage',
                                                  'instrument_derived_from_seed': False},
            'absorbing_exact_one_counter': {'same_number_one_event_probability': True, 'available_output': 'vacuum'},
            'one_count_in_tap_after_source_herald': {'available_output': 'even photon numbers, not exactly one'}},
        'passed': ['QND projector/complement completeness and idempotence', 'one-sector coherence retained',
                   'absorbing and QND success effects agree but output photon numbers differ',
                   'environmental detector branches summed incoherently', 'total number includes other retained modes',
                   'tap one-count Kraus operators and binomial probabilities', 'unsupported exact-production claims rejected'],
        'boundaries': ['QND is a new mathematical assumption, not a constructed detector',
                       'two-mode tests audit universal number-instrument identities; a total continuum-number apparatus is not supplied',
                       'source gain/profile, quantization, external work and readout are not selected by seed incidence data',
                       'no autonomous or apparatus-calibrated exact photon production demonstrated'],
        'next_executable_gate': 'Quantify loss and false-herald sensitivity of the available-output contract before making apparatus-level performance claims.'}
    path = Path(__file__).resolve().parents[1] / 'results' / 'photon-output-contract.json'
    path.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print('PASS: ideal total-number QND preserves the one-photon wavepacket; its extra assumption is mandatory.')
    print('PASS: an absorbing one-count event has the same probability but leaves vacuum; a tap click is not QND.')
    print('PASS: conditional exact-output success is mu*exp(-mu), not deterministic transfer.')
    print('BOUNDARY: mathematical instrument contract, not a seed-derived or calibrated source/detector apparatus.')
    print('Report: research/nima/results/photon-output-contract.json')
    return model


if __name__ == '__main__':
    main()
