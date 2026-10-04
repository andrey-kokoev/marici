"""Independent Arb certificate for the unchanged-Evans Hilbert residual.

Uses the repository's existing python-flint installation read-only if it is
not on sys.path. No installers, child processes, or cross-owner writes.
Rational cell boundaries and a Cauchy interior-radius bound avoid reliance
on floating partition endpoints or an uncertified removable-point evaluation.

Run: python research/nima/checkers/check_unchanged_evans_rational_ball_certificate.py
Dependency: python-flint 0.9.0 (existing research/flavor/.venv site-packages).
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
try:
    import flint
except ModuleNotFoundError:
    sys.path.insert(0, str(ROOT / 'research/flavor/.venv/Lib/site-packages'))
    import flint
from flint import acb, arb, fmpq


def rational(q):
    q = Q(q)
    return arb(fmpq(q.numerator, q.denominator))


def interval(left, right):
    left, right = Q(left), Q(right)
    center = rational((left + right) / 2)
    radius = rational((right - left) / 2).upper()
    box = arb(center, radius)
    assert box.contains(rational(left)) and box.contains(rational(right))
    return box


def xi_s(s):
    return acb(QHALF) * s * (s - 1) * (acb.pi() ** (-s / 2)) * (s / 2).gamma() * s.zeta()


def xi_x(x):
    return xi_s(acb(QHALF, x))


def integral_cells(left, right, max_width, t):
    width = right - left
    ratio = width / max_width
    n = (ratio.numerator + ratio.denominator - 1) // ratio.denominator
    total = arb(0)
    for j in range(n):
        a = left + width * Q(j, n)
        b = left + width * Q(j + 1, n)
        x = interval(a, b)
        denominator = x*x - t*t
        assert denominator.upper() < 0 or denominator.lower() > 0
        density = abs(xi_x(x))**2
        total += density * (2*t/denominator) * rational(b-a)
    return total, n


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bits', type=int, default=160)
    parser.add_argument('--mesh', default='1/1000')
    args = parser.parse_args()
    flint.ctx.prec = args.bits
    global QHALF
    QHALF = rational(Q(1, 2))
    started = time.monotonic()
    rho = acb.zeta_zero(1)
    assert rho.real == QHALF
    t = rho.imag
    left, right, cutoff = Q(353, 25), Q(283, 20), Q(30)
    assert rational(left) < t and t < rational(right)
    print('Certified first zero:', rho, flush=True)

    # Exact rational partition; every cell is enclosed, without binary-float gaps.
    negative, n_left = integral_cells(Q(0), left, Q(args.mesh), t)
    positive, n_right = integral_cells(right, cutoff, Q(args.mesh), t)
    print('Negative compact integral:', negative, flush=True)
    print('Positive compact integral:', positive, flush=True)
    assert negative.upper() < 0
    # A ball may extend slightly below zero despite a nonnegative integrand;
    # only its certified upper bound is needed for the rejection test.

    # Cauchy derivative bound throughout [left,right], not only at its center.
    center = (left+right)/2
    outer_radius = Q(1, 8)
    inner_radius = (right-left)/2
    s_box = acb(interval(Q(1, 2)-outer_radius, Q(1, 2)+outer_radius),
                interval(center-outer_radius, center+outer_radius))
    function_bound = abs(xi_s(s_box)).upper()
    derivative_bound = function_bound / rational(outer_radius-inner_radius)
    kernel_ratio = 2*t.upper()/(rational(left)+t.lower())
    absolute_first_moment = ((t-rational(left))**2 + (rational(right)-t)**2)/2
    hole_bound = (kernel_ratio * derivative_bound**2 * absolute_first_moment).upper()
    finite = negative + positive + arb(0, hole_bound)

    # x >= X=30: Euler--Maclaurin with N=ceil(x) gives |zeta| <=4 sqrt(x+1).
    # Complex Stirling gives |Gamma(1/4+ix/2)| <= sqrt(2pi)*(x/2)^(-1/4)
    # *exp(-pi*x/4+1/(3x)). See the companion packet for both derivations.
    X = rational(cutoff)
    xi_constant = 8*(2*arb.pi()).sqrt()*(1+1/(4*X*X))**2*(1+1/X)*(2/(3*X)).exp()
    kernel_constant = 2*t.upper()/(1-(t.upper()/X)**2)
    assert xi_constant < 25
    assert kernel_constant < 40
    a = arb.pi()/2
    # 1000*x^(5/2) <= 1000*x^3/sqrt(X) on x>=X. Integrate by parts exactly.
    polynomial = X**3/a + 3*X**2/a**2 + 6*X/a**3 + 6/a**4
    tail_bound = (1000/X.sqrt() * (-a*X).exp() * polynomial).upper()
    full_upper = (finite.upper() + tail_bound).upper()
    assert tail_bound < rational(Q(1, 10**10))
    assert full_upper < 0

    # Hostile: a zero-adjoint claim must be rejected by this enclosure.
    full = finite + arb(0, tail_bound)
    assert not full.contains(arb(0))
    assert not (full.lower() <= 0 <= full.upper())
    # A loose bound which includes zero must NOT be accepted as rejection.
    loose = full + arb(0, arb(1))
    assert loose.contains(arb(0)) and not (loose.upper() < 0)

    source = Path(__file__).resolve()
    report = {
        'schema': 'marici.nima.unchanged-evans-rational-ball-certificate.v1',
        'status': 'certified_strictly_negative',
        'backend': {'python_flint': flint.__version__, 'precision_bits': args.bits,
                    'module_path': str(Path(flint.__file__).resolve())},
        'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
        'first_zero': str(rho),
        'partition': {'negative': ['0', str(left)], 'hole': [str(left), str(right)],
                      'positive': [str(right), str(cutoff)],
                      'maximum_cell_width': args.mesh,
                      'negative_cells': n_left, 'positive_cells': n_right,
                      'endpoints': 'exact rational; each Arb box contains both endpoints'},
        'negative_integral': str(negative), 'positive_integral': str(positive),
        'cauchy_outer_radius': str(outer_radius),
        'cauchy_interior_radius': str(outer_radius-inner_radius),
        'xi_derivative_bound': str(derivative_bound),
        'hole_absolute_bound': str(hole_bound),
        'finite_integral': str(finite),
        'xi_squared_envelope_constant': str(xi_constant),
        'adopted_xi_squared_constant': 25,
        'kernel_envelope_constant': str(kernel_constant),
        'adopted_kernel_constant': 40,
        'analytic_tail_bound': str(tail_bound),
        'complete_integral_enclosure': str(full),
        'complete_upper_bound': str(full_upper),
        'zero_excluded': True, 'loose_enclosure_rejected': True,
        'elapsed_seconds': time.monotonic()-started,
        'claim_boundary': 'Rejects the zero of this declared unchanged-Evans scalar Hilbert residual at the certified first zeta zero. Does not exclude modified histories or cancellations in a different independently specified full source adjoint.',
        'rh_proved': False,
    }
    target = ROOT / 'research/nima/results/unchanged-evans-rational-ball-certificate.json'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2), flush=True)


if __name__ == '__main__':
    main()
