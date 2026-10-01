"""Iteration 4: conditional one-photon creation, not an apparatus claim."""
from dataclasses import replace
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

import check_photon_lorentz_transport as previous
from photon_maxwell_adapter import Q, ZERO, ONE, I, SQRT3, mv, mm
from photon_lorentz_transport import IDENTITY, LorentzMap, PhotonTransportLedger, real_positive
from photon_creation_state import (
    HELICITIES, FockPolynomial, VACUUM, FOCK_ZERO, creation_combination, PhotonCreationLedger,
)


def rejects(fn):
    try:
        fn()
    except (ValueError, TypeError):
        return
    raise AssertionError('Invalid one-photon construction was accepted')


def main():
    transport, origins = previous.main()  # fresh Lorentz/Maxwell/seed closure
    quantum = PhotonCreationLedger(transport, 'declared-normalized-two-helicity-oscillator-fixture')
    assert VACUUM.inner(VACUUM) == ONE
    assert all(VACUUM.annihilate(h) == FOCK_ZERO for h in HELICITIES)
    basis = tuple(FockPolynomial(((occupation, ONE),)) for occupation in product(range(5), repeat=2))
    mixed_polynomial = FockPolynomial((((0, 0), ONE), ((1, 0), I), ((0, 2), SQRT3),
                                       ((2, 1), Q(F(2, 3), F(1, 5), -1, 2))))
    for polynomial in basis + (mixed_polynomial,):
        for h in HELICITIES:
            assert polynomial.create(h).number() - polynomial.number().create(h) == polynomial.create(h)
            assert polynomial.annihilate(h).number() - polynomial.number().annihilate(h) == polynomial.annihilate(h).scaled(-ONE)
            for g in HELICITIES:
                # Exact finite-support CCR with unrestricted output occupation.
                commutator = polynomial.create(g).annihilate(h) - polynomial.annihilate(h).create(g)
                assert commutator == (polynomial if h == g else FOCK_ZERO)
                assert polynomial.create(h).create(g) == polynomial.create(g).create(h)
                assert polynomial.annihilate(h).annihilate(g) == polynomial.annihilate(g).annihilate(h)
            for other in basis[:6] + (mixed_polynomial,):
                assert polynomial.inner(other.create(h)) == polynomial.annihilate(h).inner(other)
    # The tested occupation boundary is not an implementation cutoff.
    high = FockPolynomial((((20, 0), ONE),))
    assert high.create(1).terms == (((21, 0), ONE),)
    assert high.create(1).annihilate(1) - high.annihilate(1).create(1) == high

    records = tuple(quantum.create_one(wave) for wave in origins)
    # Prior plus/minus name incidence characters, not physical helicity signs.
    assert records[0].coefficients == (ZERO, ONE)  # g_plus -> h=-1
    assert records[1].coefficients == (ONE, ZERO)  # g_minus -> h=+1
    assert records[2].coefficients == (ONE, ONE)
    general_seed = transport.adapter.seed_from_coordinates(Q(2, 1, -1, F(1, 2)), Q(-3, F(2, 5), 2, -1))
    general_wave = transport.start(general_seed)
    general_record = quantum.create_one(general_wave)
    records += (general_record,)
    for record in records:
        rho = quantum.density(record)
        assert sum((rho[i][i] for i in range(2)), ZERO) == ONE
        assert tuple(tuple(x.conjugate() for x in row) for row in zip(*rho)) == rho
        assert mm(rho, rho) == rho
        for i in range(2):
            assert rho[i][i] == ZERO or real_positive(rho[i][i])
        assert quantum.expectation(record, lambda p: p) == ONE
        assert quantum.expectation(record, lambda p: p.number()) == ONE
        assert quantum.expectation(record, lambda p: p.number().number()) == ONE
        assert quantum.retained_seed_in_reference_frame(record) == record.wave.origin.seed_coefficients
        assert quantum.deconstruct(record) == (record.wave, record.reference_frame, record.coefficients, record.norm_squared)
        # In the declared fixed-mode fixture P^mu=k^mu N. This verifies a
        # massless one-photon LABEL, not a seed-derived dispersion relation.
        p_mean = tuple(quantum.expectation(record, lambda p, component=k: p.number().scaled(component))
                       for k in record.wave.momentum)
        assert p_mean == record.wave.momentum
        mass_square = sum((Q(sign) * quantum.expectation(record,
                            lambda p, component=k: p.number().number().scaled(component * component))
                           for sign, k in zip((1, -1, -1, -1), record.wave.momentum)), ZERO)
        assert mass_square == ZERO
        # Repeated creation has the correct bosonic factorial norm and two
        # photons, not another normalized one-photon state.
        twice = creation_combination(record.numerator, record.coefficients)
        assert twice.inner(twice) == 2 * record.norm_squared * record.norm_squared
        assert twice.number() == twice.scaled(Q(2))
    assert quantum.expectation(records[0], lambda p: p.helicity()) == Q(-1)
    assert quantum.expectation(records[1], lambda p: p.helicity()) == ONE
    assert quantum.expectation(records[2], lambda p: p.helicity()) == ZERO
    assert quantum.expectation(records[2], lambda p: p.helicity().helicity()) == ONE
    assert records[2].numerator.helicity() != FOCK_ZERO  # zero mean does not mean spin zero

    # Gauge representatives give the same creation coefficients and density.
    gauges = (ONE, I, Q(F(2, 3), F(-1, 5), 3, 1))
    for record in records:
        for alpha in gauges:
            changed = quantum.create_one(transport.regauge(record.wave, alpha))
            assert changed.coefficients == record.coefficients
            assert changed.norm_squared == record.norm_squared
            assert quantum.density(changed) == quantum.density(record)
            assert changed.label != record.label
            assert changed.wave.label != record.wave.label
    # Normalization is intentionally many-to-one. Retaining the raw amplitude
    # and origin is not a claim that the quantum density reveals that scale.
    scale = Q(2) + I
    scaled_seed = tuple(scale * x for x in origins[2].origin.seed_coefficients)
    scaled = quantum.create_one(transport.start(scaled_seed))
    assert quantum.density(scaled) == quantum.density(records[2])
    assert scaled.norm_squared == 5 * records[2].norm_squared
    assert quantum.retained_seed_in_reference_frame(scaled) == scaled_seed
    assert quantum.retained_seed_in_reference_frame(scaled) != quantum.retained_seed_in_reference_frame(records[2])

    # Phase action on creation states in a fixed polarization frame matches the
    # classical helicity transport. A co-transported frame keeps the coefficients.
    c, s = Q(F(1, 2)), SQRT3 / 2
    R = LorentzMap.rotation(3, c, s)
    for record in records:
        rotated_wave = transport.transport(record.wave, R)
        moving_frame = quantum.create_one(rotated_wave)
        fixed_frame = quantum.create_one(rotated_wave, record.reference_frame)
        assert moving_frame.coefficients == record.coefficients
        assert fixed_frame.numerator == record.numerator.phase_rotate(c, s)
        assert fixed_frame.norm_squared == record.norm_squared
        assert quantum.expectation(fixed_frame, lambda p: p.number()) == ONE
    fixed_linear = quantum.create_one(transport.transport(origins[2], R), LorentzMap(IDENTITY))
    assert quantum.density(fixed_linear) != quantum.density(records[2])
    assert VACUUM.phase_rotate(c, s) == VACUUM
    assert mixed_polynomial.phase_rotate(c, s).inner(mixed_polynomial.phase_rotate(c, s)) == mixed_polynomial.inner(mixed_polynomial)

    # Null little-group translations act trivially, even relative to a fixed
    # frame; there is no third/longitudinal creation mode.
    null_map = LorentzMap.null_rotation(F(2, 3), F(-3, 5))
    for record in records:
        changed = quantum.create_one(transport.transport(record.wave, null_map), record.reference_frame)
        assert changed.coefficients == record.coefficients
        assert quantum.density(changed) == quantum.density(record)

    # A supplied boost relabels this abstract normalized oscillator fixture.
    # No continuum delta normalization or fixed-box boost covariance is claimed.
    boost = LorentzMap.boost(1, F(5, 4), F(3, 4))
    for record in records:
        moved = quantum.create_one(transport.transport(record.wave, boost))
        assert moved.coefficients == record.coefficients
        assert quantum.expectation(moved, lambda p: p.number()) == ONE
        assert moved.wave.momentum != record.wave.momentum
        rejects(lambda record=record, moved=moved: quantum.create_one(moved.wave, record.reference_frame))

    # Creation is not an isometry on all Fock inputs or a supplied deterministic
    # apparatus channel: a^dagger maps |0> to norm 1 but |1> to norm sqrt(2).
    assert VACUUM.create(1).inner(VACUUM.create(1)) == ONE
    assert VACUUM.create(1).create(1).inner(VACUUM.create(1).create(1)) == Q(2)
    foreign_quantum = PhotonCreationLedger(transport, 'another-declared-mode-fixture')
    foreign_record = foreign_quantum.create_one(origins[0])
    foreign_transport = PhotonTransportLedger(transport.adapter)
    foreign_wave = foreign_transport.start(origins[0].origin.seed_coefficients)
    rejects(lambda: quantum.resolve(replace(records[0])))
    rejects(lambda: quantum.resolve(foreign_record))
    rejects(lambda: quantum.create_one(foreign_wave))
    rejects(lambda: quantum.create_one(replace(origins[0])))
    rejects(lambda: quantum.create_one(origins[0], IDENTITY))
    rejects(lambda: PhotonCreationLedger(transport, ''))
    rejects(lambda: FockPolynomial((((-1, 0), ONE),)))
    rejects(lambda: FockPolynomial((((1, 0, 0), ONE),)))
    rejects(lambda: FockPolynomial((((1, 0), 0.1),)))
    rejects(lambda: VACUUM.create(0))
    rejects(lambda: creation_combination(VACUUM, (ONE,)))
    rejects(lambda: VACUUM.phase_rotate(1, 1))
    rejects(lambda: quantum.expectation(records[0], lambda p: ONE))

    report = {
        'iteration': 4,
        'status': 'conditional_one_photon_creation_state_constructed; physical_source_and_seed_selection_open',
        'seed_to_creation': 'v=a*u+b*w; beta=(a+i*b/sqrt(3))/2, alpha=(a-i*b/sqrt(3))/2; C(v)=beta*a_+^dagger+alpha*a_-^dagger',
        'normalized_state': 'C(v)|0>/sqrt(|beta|^2+|alpha|^2)',
        'packet_dictionary': {'g_plus': 'a_-^dagger|0>', 'g_minus': 'a_+^dagger|0>'},
        'passed': ['exact untruncated finite-support bosonic CCR', 'creation/annihilation adjointness under factorial metric',
                   'one-photon number and zero number variance', 'pure normalized two-helicity density',
                   'massless momentum label in the declared fixed-mode model', 'gauge-independent creation coefficients',
                   'fixed-frame helicity phase covariance and moving-frame coefficient preservation',
                   'null little-group translations trivial on the state', 'two-photon bosonic factorial norm',
                   'retained origin recovery distinguished from density-only information'],
        'added_not_derived': ['vacuum and bosonic Fock/CCR algebra', 'normalized two-mode one-particle fixture',
                             'identification of seed lines with the helicity creation operators',
                             'four-momentum operator P^mu=k^mu N within this mode fixture'],
        'physical_boundaries': ['creation operator is not a unitary apparatus protocol',
                                'a sharp momentum ket is not normalized in infinite volume',
                                'boost comparisons here relabel abstract mode fixtures, not a fixed finite box',
                                'normalization removes amplitude scale/global phase from the physical ray',
                                'no seed-derived electromagnetic source, emission probability or supplied energy reservoir'],
        'next_action': 'Replace the fixed normalized oscillator fixture by an explicitly normalizable momentum-profile one-photon wavepacket and audit its measure/frame/gauge normalization before proposing an emission source.'}
    dest = Path(__file__).resolve().parents[1] / 'results' / 'photon-creation-state.json'
    dest.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print('PASS: explicit packet-to-creation map yields exactly one photon in the declared bosonic mode model.')
    print('PASS: exact CCR, normalization, gauge/helicity covariance and bosonic two-photon control.')
    print('BOUNDARY: normalized fixed-mode quantum constructor, not seed-derived field quantization or an emission apparatus.')
    print('Report: research/nima/results/photon-creation-state.json')
    return quantum, records


if __name__ == '__main__':
    main()
