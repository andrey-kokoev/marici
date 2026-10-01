"""Iteration 9: all-orders source-flip heralding in a declared soluble control."""
from dataclasses import replace
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

import check_photon_local_quantum_dynamics as previous
from photon_maxwell_adapter import Q, ZERO, ONE, I, SQRT3, SeedMaxwellAdapter
from photon_creation_state import FockPolynomial, VACUUM, FOCK_ZERO
from photon_local_current import LocalDipoleCurrent
from photon_local_quantum_dynamics import SourceFieldState, LocalModalCoupling
from photon_coherent_herald import CoherentHeraldModel


def rejects(fn):
    try:
        fn()
    except (ValueError, TypeError):
        return
    raise AssertionError('Unsupported exact-source claim accepted')


def main():
    currents = previous.main()
    adapter = SeedMaxwellAdapter(currents[0].packets)
    seed = tuple((x + x.conjugate()) / 2 for x in currents[0].seed_coefficients)
    assert seed == adapter.seed_from_coordinates(ONE, ZERO)
    assert seed == (ONE, -ONE, Q(F(1, 2)), -ONE, ONE, Q(F(-1, 2)))
    current = LocalDipoleCurrent.from_seed(adapter, seed, envelope='gaussian')
    assert current.dipole == (SQRT3, ZERO, ZERO)
    assert current.gaussian_norm_over_pi() == Q(F(1, 2))
    model = CoherentHeraldModel(current, F(1, 10))
    assert model.source_gap == 0

    # Free-field linear observables have central commutators. X^2=1 makes the
    # source-controlled commutator a COMMON scalar, so nested commutators vanish.
    # Two canonical oscillators test the identity; this does not identify the
    # complete radiated packet with an exact-momentum/helicity oscillator.
    zs = ((ONE, I), (I, Q(2)), (ONE + I, SQRT3))
    states = []
    for occupation in ((0, 0), (1, 0), (0, 1), (2, 3), (5, 0)):
        p = FockPolynomial(((occupation, ONE),))
        states.extend((SourceFieldState(p, FOCK_ZERO), SourceFieldState(FOCK_ZERO, p)))
    for za in zs:
        A = LocalModalCoupling(za, za).full
        for zb in zs:
            B = LocalModalCoupling(zb, zb).full
            scalar = sum((a.conjugate() * b - a * b.conjugate() for a, b in zip(za, zb)), ZERO)
            for state in states:
                commutator = A(B(state)) - B(A(state))
                assert commutator == state.scaled(scalar)
                assert A(commutator) == (A(B(A(state))) - B(A(A(state))))

    # Independently compare displacement Taylor coefficients with normal-ordered
    # coherent-state coefficients through order twelve. No Fock cutoff is used:
    # each finite polynomial is an exact coefficient of an infinite series.
    # Here the single test oscillator represents abstract b_psi algebra only.
    quadrature = LocalModalCoupling((I, ZERO), (I, ZERO))
    e0 = SourceFieldState(FOCK_ZERO, VACUUM)
    power = e0
    for order in range(13):
        expected = SourceFieldState(FOCK_ZERO, FOCK_ZERO)
        for pairs in range(order // 2 + 1):
            photons = order - 2 * pairs
            coefficient = Q(F(-1, 2) ** pairs / (factorial(pairs) * factorial(photons)))
            p = FockPolynomial((((photons, 0), coefficient),))
            expected = expected + (SourceFieldState(p, FOCK_ZERO) if photons % 2 else SourceFieldState(FOCK_ZERO, p))
        assert power.scaled(F(1, factorial(order))) == expected
        power = quadrature.full(power).scaled(-I)

    # Factorial Fock norms reproduce Poisson weights without normalizing a
    # truncated series. The actual full distribution includes exp(-mu).
    rational_amplitude = F(1, 10)
    check_model = CoherentHeraldModel(current, rational_amplitude ** 2)
    for photons in range(13):
        coefficient = rational_amplitude ** photons / factorial(photons)
        p = FockPolynomial((((photons, 0), Q(coefficient)),))
        assert p.inner(p) == Q(check_model.number_weight(photons))
        if photons:
            assert photons * check_model.number_weight(photons) == check_model.mean_photon_number * check_model.number_weight(photons - 1)
        if photons % 2 == 0:
            assert check_model.number_weight(photons, source_flip=True) == 0
        else:
            assert check_model.number_weight(photons, source_flip=True) > 0
    assert model.number_weight(0, source_flip=True) == 0
    assert model.number_weight(2, source_flip=True) == 0
    assert model.number_weight(3, source_flip=True) == F(1, 6000)

    # Analytic geometric bound covers every omitted odd photon number. Its term
    # ratio proof is valid for all m>=1; rational fixtures audit implementation.
    for mu in (F(1, 100), F(1, 10), F(1, 2), F(1)):
        candidate = CoherentHeraldModel(current, mu)
        tail_bound = (mu * mu / 6) / (1 - mu * mu / 20)
        for m in range(1, 30):
            assert mu * mu / ((2 * m + 2) * (2 * m + 3)) <= mu * mu / 20
        partial_tail = sum((mu ** (2 * m) / factorial(2 * m + 1) for m in range(1, 30)), F(0))
        assert 0 < partial_tail < tail_bound
        assert candidate.infidelity_upper_bound() == tail_bound / (1 + tail_bound)
    certificate = model.certification(F(1, 500), F(9, 100))
    assert certificate['infidelity_upper_bound'] == F(10, 6007)
    assert certificate['herald_probability_lower_bound'] == F(9, 100)
    assert certificate['herald_probability_upper_bound'] == F(1, 10)
    assert not certificate['exact_single_photon']
    high_fidelity = check_model.certification(F(1, 50000), F(99, 10000))
    assert high_fidelity['infidelity_upper_bound'] < F(1, 50000)
    rejects(lambda: model.certification(0, F(1, 100)))
    rejects(lambda: model.certification(F(1, 1000), F(9, 100)))
    rejects(lambda: model.certification(F(1, 500), F(1, 2)))
    rejects(lambda: CoherentHeraldModel(currents[0], F(1, 10)))  # circular complex dipole is not X*j_real
    rejects(lambda: CoherentHeraldModel(replace(current, dipole=(ZERO,) * 3), F(1, 10)))
    rejects(lambda: CoherentHeraldModel(current, 0))
    rejects(lambda: CoherentHeraldModel(current, 0.1))
    rejects(lambda: model.number_weight(-1))

    report = {
        'iteration': 9,
        'status': 'exact conditional-displacement control model and all-orders herald infidelity bound constructed',
        'seed_packet_order': ['AB', 'BC', 'CA', 'BA', 'AD', 'DB'],
        'real_seed_vector': ['1', '-1', '1/2', '-1', '1', '-1/2'],
        'seed_relation': '(g_plus+g_minus)/2, a linear polarization in the retained seed plane',
        'declared_model': {'source_gap': '0, a degenerate control qubit rather than an excited energy reservoir',
                           'current': 'j_hat=X*j_real with X^2=1 and a smooth conserved real current',
                           'unitary': 'S=exp(i common_phase)*exp[X*(a_dagger(alpha)-a(alpha))]',
                           'supplied_gain': 'mu=||alpha||^2=lambda^2*N_source'},
        'photon_statistics': {'unconditional': 'Poisson(mu)', 'source_flip_probability': '(1-exp(-2mu))/2',
                              'conditional_flip_state': '(|alpha>-|-alpha>)/sqrt(2*(1-exp(-2mu)))',
                              'conditional_single_photon_fidelity': 'mu/sinh(mu)',
                              'exact_one_photon_for_positive_mu': False},
        'certified_operating_points': [
            {'mu': '1/10', 'single_photon_infidelity_upper_bound': '10/6007 < 1/500',
             'source_flip_probability_interval': ['9/100', '1/10']},
            {'mu': '1/100', 'single_photon_infidelity_upper_bound': '< 1/50000',
             'source_flip_probability_interval': ['99/10000', '1/100']}],
        'work_ledger': 'the degenerate source supplies no gap energy; mean outgoing field energy mu*<omega> comes from external control',
        'boundaries': ['an explicitly changed zero-gap real-current model, NOT a solution of the positive-gap circular-source dynamics',
                       'no destructive photon counter is treated as leaving an available photon',
                       'an exact single-photon output needs an additional justified number-selective instrument or different dynamics',
                       'physical scales, source implementation and readout are imported assumptions, not consequences of the packet incidence data'],
        'next_action': 'Consolidate an end-to-end output contract distinguishing exact ideal one-photon construction, local approximate heralded production, and any additional number-selective measurement assumptions.'}
    path = Path(__file__).resolve().parents[1] / 'results' / 'photon-coherent-herald.json'
    path.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print('PASS: real two-packet seed drives an exact conditional-displacement model with a declared degenerate control qubit.')
    print('PASS: source-flip herald selects odd photon number; full conditional one-photon fidelity is mu/sinh(mu), not one.')
    print('PASS: mu=1/10 certifies infidelity <0.002 and herald probability at least 0.09, without a photon-number cutoff.')
    print('BOUNDARY: this is a driven zero-gap control model, not autonomous photon production or the unresolved gapped-source solution.')
    print('Report: research/nima/results/photon-coherent-herald.json')
    return model


if __name__ == '__main__':
    main()
