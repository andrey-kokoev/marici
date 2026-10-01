"""Iteration 1: explicit six-slot two-packet candidate, not a photon claim.

Construct the conjugate cyclic eigendirections of the actual glued incidence.
Check their retained support, an invariant inner product, and the obstruction
that a C3 character cannot distinguish helicity one from helicity four.
No spacetime metric, null momentum, Maxwell equation or EM coupling is inferred.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import json

import check_whole_seed_occurrence_spectrum as source_audit
import check_natural_tower_return as algebra
import check_record4_spectral_promotion as complex_algebra
from check_triangle_half_phase import TwoPacket
from check_spectral_successor_many_many import apply as complex_apply

Z = (F(0), F(0))
ONE = (F(1), F(0))
OMEGA = (F(-1, 2), F(1, 2))  # -1/2+i sqrt(3)/2, not a frequency


@dataclass(frozen=True)
class TwoPacketVector:
    packets: tuple
    coefficients: tuple  # Q(i sqrt(3)), in exactly the packet order
    incidence_eigenvalue: tuple


def scalar_power(z, exponent):
    if exponent < 0:
        # Only unit-modulus characters are used here.
        assert complex_algebra.znorm(z) == 1
        return scalar_power(complex_algebra.zconj(z), -exponent)
    value = ONE
    for _ in range(exponent):
        value = complex_algebra.zmul(value, z)
    return value


def scalar_times(z, vector):
    return tuple(complex_algebra.zmul(z, x) for x in vector)


def vector_add(a, b):
    return tuple(complex_algebra.zadd(x, y) for x, y in zip(a, b))


def inner(a, b):
    result = Z
    for x, y in zip(a, b):
        result = complex_algebra.zadd(result, complex_algebra.zmul(complex_algebra.zconj(x), y))
    return result


def validate_candidate(candidate, packets, K):
    if candidate.packets != packets or len(candidate.coefficients) != len(packets):
        raise ValueError('Candidate must retain this exact ordered two-packet registry')
    if not any(z != Z for z in candidate.coefficients):
        raise ValueError('Zero vector is not a mode candidate')
    if complex_apply(complex_algebra.zreal(K), candidate.coefficients) != scalar_times(
            candidate.incidence_eigenvalue, candidate.coefficients):
        raise ValueError('Not an eigendirection of the actual glued incidence')


def main():
    # Fresh previous-closure verification; use its existing projectors, not an
    # independently fitted operator with a desired photon-like eigenvalue.
    fixture = source_audit.main()
    packets = tuple(TwoPacket(label, s, t) for label, s, t in fixture['packets'])
    assert tuple(p.label for p in packets) == ('AB', 'BC', 'CA', 'BA', 'AD', 'DB')
    K = fixture['continuation']
    omega_squared = scalar_power(OMEGA, 2)
    plus = (ONE, (F(-1), F(0)), complex_algebra.zscale(omega_squared, -1),
            (F(-1), F(0)), ONE, omega_squared)
    minus = tuple(complex_algebra.zconj(z) for z in plus)
    candidates = (TwoPacketVector(packets, plus, OMEGA),
                  TwoPacketVector(packets, minus, complex_algebra.zconj(OMEGA)))
    assert plus != minus
    for candidate in candidates:
        validate_candidate(candidate, packets, K)
        vector = candidate.coefficients
        assert all(complex_algebra.znorm(z) == 1 for z in vector)
        assert inner(vector, vector) == (F(6), F(0))
        first = complex_apply(complex_algebra.zreal(K), vector)
        second = complex_apply(complex_algebra.zreal(K), first)
        assert complex_apply(complex_algebra.zreal(K), second) == vector
        assert first != vector and second != vector
        # The old zero sector is an observation kernel, not this candidate.
        assert complex_apply(complex_algebra.zreal(fixture['zero_projector']), vector) == (Z,) * 6
        selected = []
        for d, eigenvalue, projector in fixture['nonzero_modes']:
            if d == -3:
                E = tuple(tuple((a, b) for a, b in zip(row_a, row_b))
                          for row_a, row_b in zip(*projector))
                projected = complex_apply(E, vector)
                assert projected == (vector if eigenvalue == candidate.incidence_eigenvalue else (Z,) * 6)
                selected.append(eigenvalue)
            else:
                # Different field, even sector: each rational coefficient
                # separately annihilates this odd-sector vector.
                for part in projector:
                    assert complex_apply(complex_algebra.zreal(part), vector) == (Z,) * 6
        assert len(selected) == 2

    # Rational real-plane frame plus = u+i sqrt(3) w. This identifies a plane,
    # not yet a physical polarization space or a plane in spacetime.
    u = tuple(z[0] for z in plus)
    w = tuple(z[1] for z in plus)
    U = tuple((a, b) for a, b in zip(u, w))  # six by two
    assert source_audit.rank(U) == 2
    T = ((F(-1, 2), F(1, 2)), (F(-3, 2), F(-1, 2)))
    I2 = ((F(1), F(0)), (F(0), F(1)))
    assert algebra.mm(K, U) == algebra.mm(U, T)
    assert algebra.mm(T, algebra.mm(T, T)) == I2
    assert algebra.add(algebra.add(algebra.mm(T, T), T), I2) == ((F(0), F(0)),) * 2

    # Raw counting norm is not conserved, even in this cyclic plane.
    mixed = vector_add(plus, minus)
    before = inner(mixed, mixed)
    after = inner(complex_apply(complex_algebra.zreal(K), mixed),
                  complex_apply(complex_algebra.zreal(K), mixed))
    assert before == (F(18), F(0)) and after == (F(12), F(0))
    assert inner(plus, minus) == (F(3), F(-1))
    G0 = algebra.mm(algebra.transpose(U), U)
    assert G0 == ((F(9, 2), F(1, 2)), (F(1, 2), F(1, 2)))
    # Explicit finite-group averaging of the declared counting metric gives a
    # positive invariant metric on the plane. It is NOT a derived physical energy.
    G = ((F(0), F(0)),) * 2
    power = I2
    for _ in range(3):
        G = algebra.add(G, algebra.mm(algebra.transpose(power), algebra.mm(G0, power)))
        power = algebra.mm(T, power)
    G = algebra.scale(G, F(1, 3))
    assert G == ((F(3), F(0)), (F(0), F(1)))
    assert algebra.mm(algebra.transpose(T), algebra.mm(G, T)) == G
    plus_coordinates = (ONE, (F(0), F(1)))
    minus_coordinates = (ONE, (F(0), F(-1)))
    G_complex = complex_algebra.zreal(G)
    assert inner(plus_coordinates, complex_apply(G_complex, plus_coordinates)) == (F(6), F(0))
    assert inner(plus_coordinates, complex_apply(G_complex, minus_coordinates)) == Z

    # Decisive false-positive control: even AFTER declaring this C3 step to be
    # a rotation through 2pi/3, charges/helicities 1,4,7 have identical characters.
    for h in (1, 4, 7, -2):
        assert scalar_power(OMEGA, h) == OMEGA
        assert scalar_power(OMEGA, -h) == complex_algebra.zconj(OMEGA)
    sixth_root = (F(1, 2), F(1, 2))  # exp(i*pi/3)
    assert scalar_power(sixth_root, 2) == OMEGA
    assert scalar_power(sixth_root, 6) == ONE
    assert scalar_power(sixth_root, 1) != scalar_power(sixth_root, 4)
    # Nothing in the three-step incidence observation chooses between these
    # inequivalent continuous lifts. Counting a phase pair is not a spin proof.

    def reject(candidate):
        try:
            validate_candidate(candidate, packets, K)
        except ValueError:
            return
        raise AssertionError('Invalid packet mode accepted')

    reject(TwoPacketVector(packets[::-1], plus, OMEGA))
    reject(TwoPacketVector(packets, (Z,) * 6, OMEGA))
    reject(TwoPacketVector(packets, plus, ONE))
    local_only = plus[:3] + (Z,) * 3
    reject(TwoPacketVector(packets, local_only, OMEGA))

    def encode_z(z):
        return {'real': str(z[0]), 'imaginary_sqrt3_coefficient': str(z[1])}

    report = {
        'iteration': 1,
        'objective': 'construct a photon-producing vector of retained two-endpoint packets',
        'status': 'explicit_seed_candidate_constructed; photon_identification_open',
        'packet_order': [p.label for p in packets],
        'candidate_plus': {'formula': '(1,-1,-omega^2,-1,1,omega^2)',
                           'coefficients': [encode_z(z) for z in plus], 'eigenvalue': encode_z(OMEGA)},
        'candidate_minus': {'formula': 'complex conjugate of candidate_plus',
                            'coefficients': [encode_z(z) for z in minus]},
        'passed': ['actual glued-incidence eigendirections', 'all six original packet identities retained',
                   'exact period three', 'matches existing whole-seed spectral projectors',
                   'distinct from the zero-incidence sector', 'positive C3-invariant plane metric constructed'],
        'metric_boundary': {'counting_norm_of_test_superposition_before': 18,
                           'counting_norm_after_one_incidence_step': 12,
                           'averaged_plane_metric': [[3, 0], [0, 1]],
                           'physical_energy_metric_not_established': True},
        'photon_gates': {
            'two_conjugate_phase_modes': 'constructed',
            'continuous_spacetime_helicity_plus_minus_one': 'open; C3 also admits plus/minus four',
            'null_four_momentum_and_massless_dispersion': 'not supplied',
            'transverse_polarization_modulo_gauge': 'not supplied',
            'electromagnetic_current_coupling_or_Ward_readout': 'not supplied',
            'physical_preparation_of_packet_coefficients': 'not supplied'},
        'next_action': 'Construct an explicit conditional map from this plane to a null-momentum Maxwell polarization quotient, and enumerate which data that map adds rather than derives.',
        'not_claimed': ['a photon has been produced', 'incidence phase is physical time or spatial rotation',
                        'a zero incidence eigenvalue is a particle mass', 'a two-packet means a two-photon state']}
    dest = Path(__file__).resolve().parents[1] / 'results' / 'photon-two-packet-candidate.json'
    dest.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print('PASS: explicit candidate (1,-1,-omega^2,-1,1,omega^2) and its conjugate on the six actual two-packets.')
    print('PASS: incidence eigenmode/projector closure and positive averaged metric on the oscillatory plane.')
    print('OBSTRUCTION: the same C3 data fit helicities +/-1 and +/-4; no mass shell, gauge quotient or EM coupling supplied.')
    print('Report: research/nima/results/photon-two-packet-candidate.json')
    return candidates


if __name__ == '__main__':
    main()
