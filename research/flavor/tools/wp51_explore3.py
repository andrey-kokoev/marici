"""WP51 explore 3: clean extraction with mass factors divided out.

H_u = F_u/(1-yc2/yt2) - 1,  H_c = F_c/(1-yu2/yt2) - 1,
H_t = F_t/(1-yu2/yc2) - 1 (scale-free => T(r,s12,delta)).
Rays s13 = r*s23; Richardson in eps^2. Identify coefficients.
"""
import sys, os
from mpmath import mp, mpf, sqrt, cos, sin, pi, nstr
mp.dps = 50
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wp51_analytic import (F_classes, TH12, TH13, TH23, DELTA, R0,
                           YU2, YC2, YT2)

FU_MASS = 1 - YC2/YT2
FC_MASS = 1 - YU2/YT2
FT_MASS = 1 - YU2/YC2

def H(a, s13, s23):
    F = F_classes(s13, s23)[a]
    return F/({'u': FU_MASS, 'c': FC_MASS, 't': FT_MASS}[a]) - 1

def rich(f, eps0, n=7, lev=3):
    xs = [eps0/2**k for k in range(n)]
    g = [f(x)/x**2 for x in xs]
    for _ in range(lev):
        g = [(4*g[i+1]-g[i])/3 for i in range(len(g)-1)]
    return g[-1]

print("=== A2(r) for u and c classes on rays s13=r*s23 ===")
rays = [mpf('0'), R0, 2*R0, 4*R0]
A2u, A2c = [], []
for r in rays:
    A2c.append(rich(lambda e: H('c', r*e, e), mpf('0.04')))
    A2u.append(rich(lambda e: H('u', r*e, e), mpf('0.04')))
for r, au, ac in zip(rays, A2u, A2c):
    print("r=%s: A2u=%s A2c=%s" % (nstr(r, 8), nstr(au, 20), nstr(ac, 20)))

# fit A2(r) = a + b r + c r^2 (4 points -> check residual with 4th)
def fit3(xs, ys):
    import mpmath
    M = mpmath.matrix([[1, x, x*x] for x in xs[:3]])
    cf = mpmath.lu_solve(M, mpmath.matrix(ys[:3]))
    res = sum(cf[i]*xs[3]**i for i in range(3)) - ys[3]
    return cf, res

for tag, A2 in (('u', A2u), ('c', A2c)):
    cf, res = fit3(rays, A2)
    print("A2_%s(r) = %s + %s r + %s r^2   (resid %s)" %
          (tag, nstr(cf[0], 20), nstr(cf[1], 20), nstr(cf[2], 20), nstr(res, 4)))

print("=== t-class scale-free check and valley ===")
def T(r, eps):
    return H('t', r*eps, eps)
for r in (R0, mpf('0.05'), mpf('0.15')):
    t1, t2 = T(r, mpf('1e-3')), T(r, mpf('1e-4'))
    print("r=%s: T(1e-3)=%s T(1e-4)=%s" % (r, nstr(t1, 15), nstr(t2, 15)))
