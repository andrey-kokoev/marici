"""Arb certification of separated pieces of the first-zero Hilbert residual.

This does not yet enclose the removable interval [13,15] or infinite tail.
Requires python-flint.
"""
from flint import acb, arb, ctx
ctx.dps = 40


def Xi(x):
    s = acb('0.5') + acb(1j) * x
    return acb('0.5') * s * (s-1) * (acb.pi() ** (-s/2)) * (s/2).gamma() * s.zeta()

rho = acb.zeta_zero(1)
t = rho.imag

def f(x, analytic):
    y = Xi(x)
    # Xi is real on the real axis; y*y is the analytic continuation whose
    # restriction equals |Xi|^2.
    return y*y * (2*t)/(x*x-t*t)

neg = acb.integral(f, arb(0), arb(13), abs_tol=arb('1e-25'), eval_limit=100000)
pos = acb.integral(f, arb(15), arb(50), abs_tol=arb('1e-25'), eval_limit=100000)
print('t =', t)
print('integral[0,13] =', neg)
print('integral[15,50] =', pos)
assert neg.real.upper() < arb('-0.15')
assert abs(neg.imag).upper() < arb('1e-20')
assert pos.real.lower() > 0
assert pos.real.upper() < arb('1e-5')
print('CERTIFIED separated-piece signs and margins; central/tail enclosure remains.')
