"""Exact rational enclosures for pi and exp(-pi*q).

This is infrastructure for the theta kappa_3 cell certificate.  It uses only
fractions; generated bounds do not depend on binary floating point.
"""
from fractions import Fraction
from functools import lru_cache


def atan_unit_interval(inv: int, terms: int) -> tuple[Fraction, Fraction]:
    """Enclose atan(1/inv) by consecutive alternating partial sums."""
    x = Fraction(1, inv)
    total = Fraction(0)
    partials = []
    for k in range(terms + 1):
        total += (-1 if k & 1 else 1) * x ** (2 * k + 1) / (2 * k + 1)
        if k >= terms - 1:
            partials.append(total)
    return min(partials), max(partials)


@lru_cache(maxsize=None)
def pi_interval(terms: int = 24) -> tuple[Fraction, Fraction]:
    """Machin enclosure: pi = 16 atan(1/5) - 4 atan(1/239)."""
    a0, a1 = atan_unit_interval(5, terms)
    b0, b1 = atan_unit_interval(239, terms)
    return 16 * a0 - 4 * b1, 16 * a1 - 4 * b0


@lru_cache(maxsize=None)
def exp_neg_point(x: Fraction, terms: int = 18) -> tuple[Fraction, Fraction]:
    """Enclose exp(-x), x>=0, by range reduction and alternating Taylor."""
    if x < 0:
        raise ValueError("x must be nonnegative")
    m = 1
    while x > Fraction(m, 2):
        m *= 2
    r = x / m
    total = Fraction(1)
    lo = hi = total
    factorial = 1
    power = Fraction(1)
    for k in range(1, terms + 1):
        factorial *= k
        power *= r
        total += (-1 if k & 1 else 1) * power / factorial
        if k == terms - 1:
            lo = hi = total
        elif k == terms:
            lo, hi = min(lo, total), max(hi, total)
    # Positive interval powering is inclusion monotone.
    return lo ** m, hi ** m


@lru_cache(maxsize=None)
def exp_neg_pi_q(q: Fraction, terms: int = 18) -> tuple[Fraction, Fraction]:
    """Enclose exp(-pi*q) for rational q>=0."""
    if q < 0:
        raise ValueError("q must be nonnegative")
    p0, p1 = pi_interval()
    # exp(-x) reverses endpoint order.
    lo, _ = exp_neg_point(p1 * q, terms)
    _, hi = exp_neg_point(p0 * q, terms)
    return lo, hi


def theta_moment_interval(s: Fraction, j: int, cutoff: int) -> tuple[Fraction, Fraction]:
    """Enclose sum_{n>=1} n^(2j) exp(-pi*s*n^2) by a geometric tail."""
    lo = Fraction(0)
    hi = Fraction(0)
    for n in range(1, cutoff + 1):
        a, b = exp_neg_pi_q(s * n * n)
        factor = n ** (2 * j)
        lo += factor * a
        hi += factor * b

    n = cutoff + 1
    first_lo, first_hi = exp_neg_pi_q(s * n * n)
    first_hi *= n ** (2 * j)
    # Consecutive term ratios decrease after the cutoff for the cutoffs used
    # by the certificate.  Bound the first ratio outward.
    _, decay_hi = exp_neg_pi_q(s * (2 * n + 1))
    ratio_hi = Fraction((n + 1) ** (2 * j), n ** (2 * j)) * decay_hi
    if ratio_hi >= 1:
        raise ValueError("cutoff precedes geometric-tail monotonicity")
    return lo, hi + first_hi / (1 - ratio_hi)


def main() -> None:
    p0, p1 = pi_interval()
    # Classical independent coarse bounds bracket the Machin enclosure.
    assert Fraction(333, 106) < p0 < p1 < Fraction(355, 113)
    for q in (Fraction(1, 10), Fraction(7, 10), Fraction(28, 10), Fraction(63, 10)):
        lo, hi = exp_neg_pi_q(q)
        assert 0 < lo < hi < 1
    moments = [theta_moment_interval(Fraction(7, 10), j, 4) for j in range(5)]
    assert all(0 < lo < hi for lo, hi in moments)
    print({"pi_width": str(p1 - p0), "sample_count": 4,
           "moment_intervals": 5, "passed": True})


if __name__ == "__main__":
    main()
