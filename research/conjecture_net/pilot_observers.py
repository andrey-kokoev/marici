"""Uniform mathematical probes from the pilot's native flip and coordinate marking.

Uses no kernel vector, target state, fitting input or physical detector model.
The probe constructor is a declared analytical extension, not a source-only
selection theorem or authorization to perform these measurements physically.
"""
from fractions import Fraction as F
from itertools import product
from check_structural_pilot_transport import identity, zeros, add, scale, complex_mul
from check_pilot_capabilities import tensor


AXES = ('X', 'Y', 'Z')


def factor_generators():
    # X is the native Bool flip. Z is the signed delta-coordinate marking.
    x = ([[F(0), F(1)], [F(1), F(0)]], zeros(2))
    z = ([[F(1), F(0)], [F(0), F(-1)]], zeros(2))
    xz = complex_mul(x, z)
    # Multiplication by i: i(A+iB)=-B+iA.
    y = (scale(-1, xz[1]), xz[0])
    return {'I': (identity(2), zeros(2)), 'X': x, 'Y': y, 'Z': z}


def spectral_effect(operator, sign):
    if sign not in (-1, 1):
        raise ValueError('spectral outcome sign must be +/-1')
    real, imag = operator
    return scale(F(1, 2), add(identity(len(real)), scale(sign, real))), scale(F(sign, 2), imag)


def product_probes():
    generators = factor_generators()
    return {(a, b): {(s, t): tensor(spectral_effect(generators[a], s), spectral_effect(generators[b], t))
                     for s, t in product((-1, 1), repeat=2)}
            for a, b in product(AXES, repeat=2)}
