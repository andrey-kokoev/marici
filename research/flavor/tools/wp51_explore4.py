"""WP51 explore 4: pin A2_u cross coeff, t-valley, identify constants."""
import sys, os
import mpmath
from mpmath import mp, mpf, sqrt, cos, sin, pi, nstr
mp.dps = 50
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wp51_analytic import F_classes, TH12, TH13, TH23, DELTA, R0, YU2, YC2, YT2
from sympy import nsimplify, Rational

FU_MASS = 1 - YC2/YT2
FC_MASS = 1 - YU2/YT2
FT_MASS = 1 - YU2/YC2
S12, CD, SD = TH12, cos(DELTA), sin(DELTA)

def H(a, s13, s23):
    return F_classes(s13, s23)[a]/({'u': FU_MASS, 'c': FC_MASS, 't': FT_MASS}[a]) - 1

def rich(f, eps0, n=7, lev=3):
    xs = [eps0/2**k for k in range(n)]
    g = [f(x)/x**2 for x in xs]
    for _ in range(lev):
        g = [(4*g[i+1]-g[i])/3 for i in range(len(g)-1)]
    return g[-1]

print("=== u-class rays ===")
rays = [R0, 2*R0, 3*R0, 4*R0, 6*R0, 8*R0]
A2u = [rich(lambda e: H('u', r*e, e), mpf('0.04')) for r in rays]
for r, au in zip(rays, A2u):
    print("r=%s: A2u=%s" % (nstr(r/R0, 4), nstr(au, 18)))
# quadratic fit on all 6, report residual
M = mpmath.matrix([[1, float(r), float(r)**2] for r in rays])
cf = mpmath.qr_solve(M, mpmath.matrix([float(x) for x in A2u]))[0]
res = [sum(cf[i]*float(r)**i for i in range(3)) - float(x) for r, x in zip(rays, A2u)]
print("fit: a=%s b=%s c=%s maxres=%s" % (nstr(cf[0],18), nstr(cf[1],18), nstr(cf[2],18), nstr(max(abs(x) for x in res),3)))
b = mpf(str(cf[1]))
print("b candidates:")
for tag, val in [("sqrt3", sqrt(3)), ("1/(2*s12)", 1/(2*S12)),
                 ("1/(2*s12*cd)", 1/(2*S12*CD)), ("2*cd/s12", 2*CD/S12),
                 ("1/(s12+...)", None)]:
    if val is not None:
        print("  %s = %s  diff %s" % (tag, nstr(val,18), nstr(b-val,4)))
print("  nsimplify(b, [s12, cd, sd]):", nsimplify(mpmath.nstr(b, 30), [mpmath.nstr(S12,30), mpmath.nstr(CD,30), mpmath.nstr(SD,30)]))

print("=== t-valley fine scan ===")
eps = mpf('1e-4')
rs = [mpf('0.082') + mpf('0.001')*i for i in range(17)]
Ts = [H('t', r*eps, eps) for r in rs]
for r, t in zip(rs, Ts):
    print("r=%s T=%s" % (r, nstr(t, 14)))
# quadratic fit around min
i0 = min(range(len(Ts)), key=lambda i: Ts[i])
rf = [float(rs[i]) for i in (i0-1, i0, i0+1)]
Tf = [float(Ts[i]) for i in (i0-1, i0, i0+1)]
import numpy as np
qc = np.polyfit(rf, Tf, 2)
rstar = -qc[1]/(2*qc[0])
print("valley r* = %.10f  T(r*) = %.10e  curvature K = %.6f" % (rstar, qc[2]-qc[1]**2/(4*qc[0]), qc[0]))
print("s12*cos(delta) = %.10f ; s12 = %.10f ; R0 = %.10f" % (float(S12*CD), float(S12), float(R0)))
print("T(R0) = %s" % nstr(H('t', R0*eps, eps), 18))
print("R0^2/c12^2 = %s" % nstr(R0**2/(1-S12**2), 18))
print("(R0/c12)^2 vs -T(R0): diff %s" % nstr(R0**2/(1-S12**2) + H('t', R0*eps, eps), 6))
