"""Iteration 7: local conserved source geometry and the top-hat obstruction.

The compact-support Fourier-analyticity argument is documented separately;
finite checks audit its target jump and explicit alternative source currents.
The radiation amplitude here is first order, not the prior Rabi unitary.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json

import check_photon_source_emission as previous
from photon_maxwell_adapter import Q, ZERO, ONE, I, SQRT3, mv, mm, transpose, minkowski
from photon_lorentz_transport import LorentzMap, real_positive
from photon_momentum_wavepacket import momentum, polarization_frame
from photon_local_current import LocalDipoleCurrent, dot, gaussian_odd_radial_moment


def rejects(fn):
    try:
        fn()
    except (ValueError, TypeError):
        return
    raise AssertionError('Invalid local transition current was accepted')


def main():
    emitter, emission = previous.main()  # fresh prior chain, not reuse of its emission law
    packet_ledger = emitter.packets
    creation = packet_ledger.creation
    adapter = creation.transport.adapter
    seed_plus = creation.retained_seed_in_reference_frame(emission.packet.creation_record)
    seed_minus = tuple(z.conjugate() for z in seed_plus)
    general = adapter.seed_from_coordinates(ONE + I, Q(2))
    seeds = (seed_plus, seed_minus, general)
    currents = tuple(LocalDipoleCurrent.from_seed(adapter, seed, envelope=kind)
                     for seed in seeds for kind in ('compact_bump', 'gaussian'))
    basis = tuple(tuple(ONE if i == j else ZERO for j in range(4)) for i in range(4))
    momenta = basis + tuple(tuple(a + b for a, b in zip(basis[i], basis[j])) for i, j in combinations(range(4), 2))
    momenta += ((Q(3), ONE, Q(-2), ZERO), (Q(2), ONE, ONE, ONE))
    spacetime_points = ((F(1, 3), F(1, 4), F(-1, 5), F(2, 7)),
                        (F(-2, 5), F(1, 2), F(1, 3), F(-1, 4)), (F(0),) * 4)
    boosts = (LorentzMap.boost(1, F(5, 4), F(3, 4)), LorentzMap.rotation(2, F(3, 5), F(4, 5)))
    for current in currents:
        assert current.packets == adapter.packets
        assert adapter.coordinates(current.seed_coefficients)
        for point in spacetime_points:
            assert current.reduced_divergence(point) == ZERO
            sample = current.sample(point)
            assert sample.exponent is not None
            # Complex transition matrix elements become a Hermitian quantum
            # source current via sigma_- j_ge + sigma_+ conjugate(j_ge).
            for component in sample.coefficients:
                operator = ((ZERO, component), (component.conjugate(), ZERO))
                assert tuple(tuple(x.conjugate() for x in row) for row in transpose(operator)) == operator
        d = current.dipole
        M = ((ZERO,) + d,) + tuple((-d[i],) + (ZERO,) * 3 for i in range(3))
        assert transpose(M) == tuple(tuple(-x for x in row) for row in M)
        for k in momenta:
            J = current.reduced_fourier_current(k)
            k_lower = tuple(sign * x for sign, x in zip((1, -1, -1, -1), k))
            assert mv(transpose(M), k_lower) == J
            assert minkowski(k, J) == ZERO  # off shell as well as on shell
            for L in boosts:
                new_k = mv(L.matrix, k)
                new_M = mm(L.matrix, mm(M, transpose(L.matrix)))
                new_lower = tuple(sign * x for sign, x in zip((1, -1, -1, -1), new_k))
                assert mv(transpose(new_M), new_lower) == mv(L.matrix, J)
        if current.envelope == 'compact_bump':
            for point in ((1, 0, 0, 0), (0, -1, 0, 0), (0, 0, 2, 0), (0, 0, 0, -3)):
                assert current.sample(point).exponent is None
                assert current.sample(point).coefficients == (ZERO,) * 4
                assert current.reduced_divergence(point) == ZERO
        # Omitting the compensating charge density is not a conserved current.
        k = (Q(2), ONE, ZERO, ONE)
        J = current.reduced_fourier_current(k)
        bad = (ZERO,) + J[1:]
        assert minkowski(k, bad) != ZERO

    directions = ((ZERO, ZERO, ONE), (ZERO, ZERO, -ONE), (ONE, ZERO, ZERO),
                  (Q(F(3, 5)), ZERO, Q(F(4, 5))))
    plus_source = currents[0]
    assert plus_source.dipole == (SQRT3, -I * SQRT3, ZERO)
    assert plus_source.angular_intensity(directions[0], -1) == Q(6)
    assert plus_source.angular_intensity(directions[0], 1) == ZERO
    assert plus_source.angular_intensity(directions[1], 1) == Q(6)
    assert plus_source.angular_intensity(directions[1], -1) == ZERO
    assert plus_source.angular_intensity(directions[2], -1) == Q(F(3, 2))
    assert plus_source.angular_intensity(directions[2], 1) == Q(F(3, 2))
    for current in currents:
        D = dot(tuple(z.conjugate() for z in current.dipole), current.dipole)
        for n in directions:
            total = sum((current.angular_intensity(n, h) for h in (-1, 1)), ZERO)
            longitudinal = dot(n, current.dipole)
            assert total == D - longitudinal.conjugate() * longitudinal
            for h in (-1, 1):
                intensity = current.angular_intensity(n, h)
                assert intensity == ZERO or real_positive(intensity)
                assert intensity == current.angular_intensity(tuple(-x for x in n), -h)
        for point in ((F(3, 2), F(1, 5), F(-1, 3)), (F(5, 4), F(0), F(0)), (F(2), F(1), F(0))):
            k = momentum(point)
            frame = polarization_frame(point, adapter.energy)
            n = tuple(x / k[0] for x in k[1:])
            for h in (-1, 1):
                epsilon = mv(frame.matrix, (ZERO, SQRT3, I * h * SQRT3, ZERO))
                amplitude = current.reduced_emission(k, epsilon)
                assert amplitude.conjugate() * amplitude / 6 == k[0] ** 2 * current.angular_intensity(n, h)
                for alpha in (ONE, I, Q(1, 2, -1, 3)):
                    shifted = tuple(e + alpha * p for e, p in zip(epsilon, k))
                    assert current.reduced_emission(k, shifted) == amplitude

    # The target jump is exactly present on a nonsingular ray: q=1 is the lower
    # band edge, u=v=0. No finite sample alone proves analyticity; the separate
    # Fourier argument excludes this target for compact spacetime currents.
    target = emission.packet
    assert target.coefficients != (ZERO, ZERO)
    for denominator in (10, 100, 1000, 10000):
        inside = (1 + F(1, denominator), F(0), F(0))
        outside = (1 - F(1, denominator), F(0), F(0))
        assert packet_ledger.amplitude_numerators(target, inside) == target.coefficients
        assert packet_ledger.amplitude_numerators(target, outside) == (ZERO, ZERO)
    # These two limits are incompatible with the continuity/analyticity of the
    # on-shell Fourier amplitude of a compact spacetime transition current.

    # Gaussian alternative has an exact analytically integrated radiation norm.
    # Its Fourier envelope is RESCALED to ftilde(0)=1 for the following formula;
    # the position-space sample above omits that common source normalization.
    gaussians = tuple(c for c in currents if c.envelope == 'gaussian')
    for current in gaussians:
        a = current.widths[0] ** 2 + current.widths[1] ** 2
        D = dot(tuple(x.conjugate() for x in current.dipole), current.dipole)
        radial3 = gaussian_odd_radial_moment(3, a)
        radial5 = gaussian_odd_radial_moment(5, a)
        # Angular integral: 8*pi*D/3. The invariant measure contributes 1/2.
        norm_over_pi = Q(F(4, 3) * radial3) * D
        assert norm_over_pi == current.gaussian_norm_over_pi()
        assert real_positive(norm_over_pi)
        assert radial5 / radial3 == 2 / a
        # <omega>^2=9*pi/(16a); pi<22/7 certifies positive variance.
        assert 2 / a - 9 * F(22, 7) / (16 * a) > 0
    assert gaussians[0].gaussian_norm_over_pi() == ONE
    assert gaussians[1].gaussian_norm_over_pi() == ONE
    # Each helicity has half the integrated probability for this parity-even
    # electric source envelope; angular helicity purity at +z is not global.
    # Six axis directions integrate every degree<=2 spherical polynomial
    # exactly after division by six. Certify that rule on its monomials before
    # using it on the quadratic intensity; this is not an angular quadrature
    # approximation for the present polynomial.
    axes = tuple(tuple(Q(sign if i == axis else 0) for i in range(3))
                 for axis in range(3) for sign in (-1, 1))
    for i in range(3):
        assert sum((n[i] for n in axes), ZERO) == ZERO
        for j in range(3):
            assert sum((n[i] * n[j] for n in axes), ZERO) / 6 == Q(F(int(i == j), 3))
    for current in gaussians:
        angular_means = tuple(sum((current.angular_intensity(n, h) for n in axes), ZERO) / 6
                              for h in (1, -1))
        D = dot(tuple(z.conjugate() for z in current.dipole), current.dipole)
        assert angular_means == (D / 3, D / 3)
        integrated_helicity_fractions = tuple(x / sum(angular_means, ZERO) for x in angular_means)
        assert integrated_helicity_fractions == (Q(F(1, 2)), Q(F(1, 2)))

    # Compact smooth bump alternative: derivative ratios and support are exact.
    # Its Fourier transform is not artificially clipped, and rapid decay gives
    # a finite nonzero radiation norm, as proved in the accompanying note.
    # Numerical source normalization is intentionally not fabricated here.
    assert plus_source.sample((0, 0, 0, 0)).exponent == -4
    assert any(x != ZERO for x in plus_source.sample(spacetime_points[0]).coefficients)
    rejects(lambda: LocalDipoleCurrent.from_seed(adapter, seed_plus, widths=(0, 1, 1, 1)))
    rejects(lambda: LocalDipoleCurrent.from_seed(adapter, seed_plus, envelope='hard_spacetime_box'))
    rejects(lambda: LocalDipoleCurrent.from_seed(adapter, (ZERO,) * 6))
    rejects(lambda: LocalDipoleCurrent.from_seed(adapter, (ONE,) * 6))
    rejects(lambda: LocalDipoleCurrent.from_seed(adapter, seed_plus, widths=(1.0, 1, 1, 1)))
    rejects(lambda: plus_source.angular_intensity((ONE, ONE, ZERO), 1))
    rejects(lambda: plus_source.angular_intensity(directions[0], 0))
    rejects(lambda: plus_source.gaussian_norm_over_pi())
    rejects(lambda: plus_source.sample((0.1, 0, 0, 0)))
    rejects(lambda: gaussian_odd_radial_moment(2, F(2)))

    report = {
        'iteration': 7,
        'status': 'local_conserved_transition_current_constructed; exact_top_hat_excluded_for_compact_spacetime_sources',
        'current': 'M^{0i}=d_i f, M^{i0}=-d_i f, j^mu=partial_nu M^{nu mu}',
        'packet_to_dipole': 'v=a*u+b*w -> d=(sqrt(3)*a,-b,0)',
        'reduced_Fourier_current': 'J=(k_vec.d, omega*d); actual jtilde=-i*ftilde*J',
        'passed': ['identically conserved position-space current in the declared envelope family',
                   'off-shell Ward identity and gauge-independent radiation amplitude',
                   'antisymmetric-tensor Lorentz covariance', 'Hermitian transition-current completion',
                   'compact bump support controls', 'source dipole angular/helicity radiation pattern',
                   'exact Gaussian radiation normalization and second energy moment'],
        'top_hat_obstruction': {
            'argument': 'compact spacetime transition current has analytic on-shell Fourier amplitude; cannot equal a nonzero compact momentum top-hat',
            'finite_checker_scope': 'audits the target jump; Fourier analyticity proof is analytic, not certified by finite samples'},
        'alternatives': {
            'compact_bump': 'smooth current with bounded spacetime support; Fourier radiation is broad, normalizable, not top-hat',
            'gaussian': 'rapidly localized, not compact; Fourier-normalized radiation norm is 2*pi*|d|^2/(3*(tau^2+ell^2)^2)',
            'unit_width_circular_candidate': {'radiation_norm': 'pi', 'mean_energy': '3*sqrt(pi)/(4*sqrt(2))',
                                            'second_energy_moment': '1', 'integrated_helicity_probabilities': ['1/2', '1/2']}},
        'important_boundaries': ['first-order quantum transition amplitude, not the iteration-6 exact global-control unitary',
                                 'a classical prescribed current would generate a coherent field rather than deterministic one-photon emission',
                                 'local dipole radiation changes the chosen profile and correlates helicity with direction',
                                 'source dynamics, coupling strength, recoil and exact multiphoton probabilities remain open'],
        'next_action': 'Audit quantum source dynamics and photon-number contamination for the new local-current coupling; distinguish a controlled one-excitation approximation from the exact local interaction.'}
    dest = Path(__file__).resolve().parents[1] / 'results' / 'photon-local-current.json'
    dest.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print('PASS: local antisymmetric-tensor transition current is conserved and supplies gauge-invariant radiation.')
    print('PASS: Gaussian norm is exact; compact smooth bump is a distinct broad-spectrum alternative.')
    print('OBSTRUCTION: a compact spacetime current cannot have the requested exact momentum top-hat amplitude.')
    print('BOUNDARY: first-order local-source construction, not inherited unit-probability emission or global helicity purity.')
    print('Report: research/nima/results/photon-local-current.json')
    return currents


if __name__ == '__main__':
    main()
