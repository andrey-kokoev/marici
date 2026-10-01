"""Finish the gap/counter-rotating audit begun in iteration 8."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

import check_photon_local_current as previous
from photon_maxwell_adapter import Q, ZERO, ONE, I, SQRT3, minkowski
from photon_creation_state import FockPolynomial, VACUUM, FOCK_ZERO
from photon_local_current import dot
from photon_local_quantum_dynamics import (SourceFieldState, LocalModalCoupling,
    free_action, modulated_current_sample, GaussianGapSpectrum)


def rejects(fn):
    try:
        fn()
    except (ValueError, TypeError):
        return
    raise AssertionError('Invalid quantum-source input accepted')


def main():
    currents = previous.main()
    gap = F(2, 3)
    point = (F(1, 3), F(1, 4), F(-1, 5), F(2, 7))
    for current in currents:
        lower = modulated_current_sample(current, gap, point)
        upper = modulated_current_sample(current, gap, point, raising=True)
        assert lower.time_phase_argument == -upper.time_phase_argument
        assert upper.coefficients == tuple(x.conjugate() for x in lower.coefficients)
        if current.envelope == 'gaussian':
            gradients = tuple(-x / w ** 2 for x, w in zip(point, current.widths))
        else:
            gradients = tuple(-2 * x / (w ** 2 * (1 - (x / w) ** 2) ** 2) for x, w in zip(point, current.widths))
        for sample, shift in ((lower, -I * gap), (upper, I * gap)):
            divergence = sample.coefficients[0] * (gradients[0] + shift) + dot(sample.coefficients[1:], gradients[1:])
            assert divergence == ZERO
        # Multiplying the old current by the source phase without differentiating
        # that phase in M violates conservation.
        base = current.sample(point)
        bad_divergence = base.coefficients[0] * (gradients[0] - I * gap) + dot(base.coefficients[1:], gradients[1:])
        assert bad_divergence != ZERO
        k = (Q(2), ONE, ZERO, ONE)
        J = current.reduced_fourier_current(k)
        assert minkowski(k, J) == ZERO
        bad_J = (J[0],) + tuple((k[0] - gap) * d for d in current.dipole)
        assert minkowski(k, bad_J) == gap * dot(k[1:], current.dipole) != ZERO
        if current.envelope == 'compact_bump':
            assert modulated_current_sample(current, gap, (2, 0, 0, 0)).coefficients == (ZERO,) * 4

    # The +z circular seed and its Hermitian conjugate supply opposite photon
    # helicities for source lowering/raising. Remove one COMMON coupling scale.
    k = (ONE, ZERO, ZERO, ONE)
    eps = tuple((ZERO, SQRT3, I * h * SQRT3, ZERO) for h in (1, -1))
    g = tuple(currents[0].reduced_emission(k, e) / 6 for e in eps)
    r = tuple(currents[2].reduced_emission(k, e) / 6 for e in eps)
    assert g == (ZERO, ONE) and r == (ONE, ZERO)
    interaction = LocalModalCoupling(g, r)
    z = SourceFieldState(FOCK_ZERO, FOCK_ZERO)
    e0 = SourceFieldState(FOCK_ZERO, VACUUM)
    g0 = SourceFieldState(VACUUM, FOCK_ZERO)
    states = []
    for np in range(3):
        for nm in range(3):
            p = FockPolynomial((((np, nm), ONE),))
            states.extend((SourceFieldState(p, FOCK_ZERO), SourceFieldState(FOCK_ZERO, p)))
    for coupling in (interaction, LocalModalCoupling((ONE + I, SQRT3), (I, Q(2)))):
        for state in states:
            assert coupling.rotating(state).excitation() == coupling.rotating(state.excitation())
            assert coupling.full(state).parity() == coupling.full(state.parity())
            for other in states:
                assert state.inner(coupling.full(other)) == coupling.full(state).inner(other)
    assert interaction.full(e0).excitation() == interaction.full(e0.excitation())
    assert interaction.full(g0).excitation() != interaction.full(g0.excitation())
    assert interaction.rotating(g0) == z
    assert interaction.full(g0) != z  # not a dark bare ground/vacuum under switching
    assert interaction.full(e0).inner(interaction.full(e0)) == ONE

    # Source and field resonance removes the rotating free-energy commutator,
    # not the counter-rotating one. Total energy of a time-independent complete
    # Hamiltonian is a different question from conservation of the free energy.
    H0 = lambda state: free_action(state, 1, (1, 1))
    for state in states:
        assert H0(interaction.rotating(state)) == interaction.rotating(H0(state))
    assert H0(interaction.counter(g0)) != interaction.counter(H0(g0))

    # No occupation cutoff: higher photons are actually retained. These are
    # leading short-time coefficients in a two-mode witness, NOT continuum
    # Gaussian multiphoton probabilities. H0 does not change the leading
    # maximal-photon-number terms at each Taylor order.
    full_H = lambda state: H0(state) + interaction.full(state)
    vpower, hpower = e0, e0
    probabilities = {}
    for order in range(1, 4):
        vpower = interaction.full(vpower)
        hpower = full_H(hpower)
        sector = vpower.photon_sector(order)
        assert sector == hpower.photon_sector(order)
        amplitude = sector.scaled((-I) ** order / factorial(order))
        probabilities[order] = amplitude.inner(amplitude)
        assert sector.parity() == sector.scaled(-ONE)
    assert probabilities == {1: ONE, 2: Q(F(1, 4)), 3: Q(F(1, 18))}
    assert vpower.photon_sector(3).excited == FOCK_ZERO
    assert vpower.photon_sector(3).ground != FOCK_ZERO
    # A source-ground herald retains this three-photon term.

    spectrum = GaussianGapSpectrum(1, 5, F(1, 5))
    for energy in (F(1, 1000), F(1, 5), F(1), F(3, 2), F(10)):
        assert spectrum.log_counter_ratio(energy) == -4 * spectrum.temporal_width ** 2 * spectrum.gap * energy
        assert spectrum.log_counter_ratio(energy) < 0
    certificate = spectrum.integrated_ratio_bound(F(1, 5))
    assert certificate['suppression_exponent'] == F(14964, 625)
    assert certificate['prefactor'] == F(390625, 100320256)
    assert 0 < certificate['ratio_upper_bound'] < F(1, 10 ** 12)
    rejects(lambda: GaussianGapSpectrum(0, 1, 1))
    rejects(lambda: GaussianGapSpectrum(1, 1.0, 1))
    rejects(lambda: spectrum.integrated_ratio_bound(1))
    rejects(lambda: spectrum.log_intensity(0))
    rejects(lambda: LocalModalCoupling((ONE,), (ONE, ONE)))
    rejects(lambda: modulated_current_sample(currents[0], -1, point))

    report = {
        'iteration_started': 8, 'completed_during': 9,
        'status': 'gap-current and quantum selection-rule audit passed',
        'exact_selection_rule': 'parity of N_gamma+|e><e|; excitation number is conserved only after deleting counter-rotating terms',
        'source_ground_herald': 'odd photon number, not exactly one',
        'modal_short_time_witness': {'P1_leading': '(lambda*t)^2', 'P2_leading': '(lambda*t)^4/4',
                                    'P3_leading': '(lambda*t)^6/18', 'scope': 'two-mode witness, not continuum probabilities'},
        'gaussian_first_order_ratio': {
            'log_pointwise_ratio': '-4*tau^2*Omega*omega after angular/helicity summation',
            'parameters': {'Omega': '1', 'tau': '5', 'ell': '1/5', 'integration_lower_bound_half_bandwidth': '1/5'},
            'integrated_counter_to_emission_ratio': '< 1e-12',
            'certificate': 'positive exponential Taylor sum through order 32; exact rational comparison',
            'scope': 'ratio of first-order channel weights from different initial source states; NOT all-orders multiphoton infidelity'},
        'boundaries': ['bare ground/vacuum switching excitation consumes external work; not instability of the interacting vacuum',
                       'no exact continuum Rabi transfer law established',
                       'effective local-density coupling is not a microscopic matter or apparatus derivation']}
    path = Path(__file__).resolve().parents[1] / 'results' / 'photon-local-quantum-dynamics.json'
    path.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print('PASS: source-gap derivative preserves current conservation; omitting it fails the Ward check.')
    print('PASS: full bilinear coupling preserves excitation parity, not excitation number; ground herald allows three photons.')
    print('PASS: Gaussian first-order counter/emission weight ratio certified below 1e-12 for declared parameters.')
    print('BOUNDARY: the modal witness and first-order ratio are not an all-orders continuum fidelity bound.')
    return currents


if __name__ == '__main__':
    main()
