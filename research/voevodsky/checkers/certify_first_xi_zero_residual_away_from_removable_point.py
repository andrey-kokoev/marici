"""Arb certification of the first-zero Hilbert residual.

The removable point is handled by an interval derivative bound.  The infinite
tail uses the deliberately coarse critical-line estimate
|Xi(x)| <= 100*x^3*exp(-pi*x/4), x>=50, obtained from the completed-Xi formula,
Euler--Maclaurin |zeta(1/2+ix)|<=x, and Stirling's gamma remainder bound.
Requires python-flint.
"""
from flint import acb, acb_series, arb, ctx
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

# Remove a symmetric epsilon-neighborhood of the certified first zero.
eps = arb('0.001')
left_end = t.lower() - eps
right_start = t.upper() + eps
central_left = acb.integral(f, arb(13), left_end, abs_tol=arb('1e-22'), eval_limit=100000)
central_right = acb.integral(f, right_start, arb(15), abs_tol=arb('1e-22'), eval_limit=100000)

# Xi(t)=0.  On |x-t|<=eps, the mean-value identity gives
# |Xi(x)/(x-t)| <= sup |Xi'|.  Arb series evaluation encloses that supremum.
x_box = arb(t.mid(), arb('0.0011'))
s = acb_series([acb('0.5') + acb(1j) * x_box, acb(1j)], 2)
xi_series = acb('0.5') * s * (s-1) * (acb.pi() ** (-s/2)) * (s/2).gamma() * s.zeta()
derivative_bound = abs(xi_series[1]).upper()
ratio_bound = (2 * t.upper()) / (2 * t.lower() - eps)
central_hole_bound = derivative_bound**2 * ratio_bound * eps**2
finite = neg + central_left + central_right + pos

# For x>=50, 2t/(x^2-t^2) <= 32/x^2 and the documented coarse completed-Xi
# estimate gives an integrand majorant 320000*x^4*exp(-pi*x/2).
# Integrate that elementary majorant exactly by four integrations by parts.
L = arb(50)
a = arb.pi()/2
poly_tail = L**4/a + 4*L**3/a**2 + 12*L**2/a**3 + 24*L/a**4 + 24/a**5
tail_bound = arb(320000) * (-a*L).exp() * poly_tail

print('t =', t)
print('integral[0,13] =', neg)
print('integral[13,t-eps] =', central_left)
print('integral[t+eps,15] =', central_right)
print('central hole absolute bound =', central_hole_bound)
print('integral[15,50] =', pos)
print('finite subtotal excluding hole =', finite)
print('infinite tail absolute bound =', tail_bound)
assert neg.real.upper() < arb('-0.15')
assert abs(neg.imag).upper() < arb('1e-20')
assert pos.real.lower() > 0
assert pos.real.upper() < arb('1e-5')
assert central_hole_bound < arb('3e-12')
assert tail_bound < arb('2e-22')
certified_upper = finite.real.upper() + central_hole_bound + tail_bound
assert certified_upper < arb('-0.15084')
print('certified full-integral upper bound =', certified_upper)
print('CERTIFIED full first-zero Evans residual is strictly negative.')
