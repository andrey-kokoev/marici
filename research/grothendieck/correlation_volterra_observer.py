"""Volterra realization on labelled, piecewise-constant edge signals.

The parameter orders source events; it is not physical time. Mixtures must be
observed routewise before addition. This module does not extract labels from theta.
"""
from fractions import Fraction


def advance(state, duration, first, second):
    """Exact constant-panel flow for A_i'=first_i, B_i'=second_i A_i.

    Rational inputs produce rational outputs. State is (A, B), each length six.
    Simultaneous channels include the half-panel cross term.
    """
    dt = Fraction(duration)
    if dt < 0:
        raise ValueError('Panel duration must be nonnegative')
    a, b = map(tuple, state)
    first, second = tuple(map(Fraction, first)), tuple(map(Fraction, second))
    if any(len(v) != 6 for v in (a, b, first, second)):
        raise ValueError('Expected six coordinates per channel')
    return (
        tuple(a[i] + dt * first[i] for i in range(6)),
        tuple(b[i] + dt * second[i] * a[i]
              + dt * dt * first[i] * second[i] / 2 for i in range(6)),
    )


def observe(panels):
    """Panels are (duration, six first-channel values, six second values)."""
    state = ((Fraction(0),) * 6, (Fraction(0),) * 6)
    for duration, first, second in panels:
        state = advance(state, duration, first, second)
    return state


def concatenate(prefix, suffix, suffix_second_mass):
    """Chen law for independently reset blocks, preserving prefix memory."""
    a, b = prefix
    c, d = suffix
    if any(len(v) != 6 for v in (a, b, c, d, suffix_second_mass)):
        raise ValueError('Expected six coordinates per channel')
    return (tuple(x+y for x, y in zip(a, c)),
            tuple(b[i]+d[i]+a[i]*suffix_second_mass[i] for i in range(6)))
