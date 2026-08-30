"""WP51 analytic: exact structure of F-1 per purity class (mpmath 50 dps).

F_class(s12,s13,s23,delta; masses) recomputed exactly in mpmath.
Extract: strict-limit constants, quadratic forms in (s13,s23) for u,c,
ratio-valley structure for t. Identify coefficients via nsimplify.
"""
import sys
from mpmath import (mp, mpf, mpc, sqrt, sin, cos, atan2, fabs, pi, identify,
                    nstr)
from sympy import nsimplify
mp.dps = 50

YU2, YC2, YT2 = mpf('7.04e-6')**2, mpf('3.56e-3')**2, mpf('0.967')**2
YD2, YS2, YB2 = mpf('1.54e-5')**2, mpf('3.06e-4')**2, mpf('1.630e-2')**2
TH12, TH13, TH23 = mpf('0.22517'), mpf('0.003763'), mpf('0.04189')
DELTA = mpf('66.4')*pi/180
R0 = TH13/TH23
LAM = (YD2, YS2, YB2)
UPS = (YU2, YC2, YT2)

def std_V(s12, s13, s23, dl):
    c12 = sqrt(1-s12*s12); c13 = sqrt(1-s13*s13); c23 = sqrt(1-s23*s23)
    ed = mpc(cos(dl), sin(dl))
    return [[c12*c13, s12*c13, s13*ed.conjugate()],
            [-s12*c23 - c12*s23*s13*ed, c12*c23 - s12*s23*s13*ed, s23*c13],
            [s12*s23 - c12*c23*s13*ed, -c12*s23 - s12*c23*s13*ed, c23*c13]]

def invert_down(um, ed):
    e1 = ed[0]+ed[1]+ed[2]
    e2 = ed[0]*ed[1]+ed[0]*ed[2]+ed[1]*ed[2]
    e3 = ed[0]*ed[1]*ed[2]
    d0 = um[0]*ed[0]+um[1]*ed[1]+um[2]*ed[2]
    beta = e3*(um[0]/ed[0]+um[1]/ed[1]+um[2]/ed[2])
    e1p = e1 - d0
    d1 = (beta*d0 - e3)/(e1p*d0 - e2 + beta)
    v2 = (d0-ed[0])*(d0-ed[1])*(d0-ed[2])/(d1-d0)
    w2 = (d1-ed[0])*(d1-ed[1])*(d1-ed[2])/(d0-d1)
    return v2, w2

def F_classes(s13, s23, s12=TH12, dl=DELTA, lam=LAM, ups=UPS):
    V = std_V(s12, s13, s23, dl)
    A = [[fabs(x) for x in row] for row in V]
    den = V[1][0]*V[1][2].conjugate()
    if den != 0:
        z = -(V[0][0]*V[0][2].conjugate())/den
        sg = sin(fabs(atan2(z.imag, z.real)))
    else:
        sg = mpf('0')
    yu2, yc2, yt2 = ups
    ed = lam
    Dd = (ed[2]-ed[1])*(ed[2]-ed[0])*(ed[1]-ed[0])
    out = {}
    for anchor, kp in (('u', 0), ('c', 1), ('t', 2)):
        um = [A[kp][0]**2, A[kp][1]**2, A[kp][2]**2]
        v2, w2 = invert_down(um, ed)
        if anchor == 'u':
            bg, sc, V3 = yt2-yc2, yt2, A[0][0]*A[0][2]*A[1][0]
        elif anchor == 'c':
            bg, sc, V3 = yt2-yu2, yt2, A[0][0]*A[1][0]*A[1][2]
        else:
            bg, sc, V3 = yc2-yu2, yc2, A[0][0]*A[1][0]*A[1][2]**2*sg
        out[anchor] = bg*Dd*V3/(sc*v2*sqrt(w2))
    return out

def rich(f, eps0, n=7, p=2):
    """f(eps) ~ A*eps^p + B*eps^{p+2} + ...; return refined estimates of A."""
    xs = [eps0/2**k for k in range(n)]
    g = [f(x)/x**p for x in xs]
    for _ in range(3):
        g = [(4*g[i+1]-g[i])/3 for i in range(len(g)-1)]
    return g

def show(tag, x, d=25):
    print("%s = %s" % (tag, nstr(x, d)))

print("=== sanity: F at measured point ===")
F0 = F_classes(TH13, TH23)
for a in 'uct':
    show("F_%s - 1" % a, F0[a]-1, 12)

print("=== u-class strict-limit constant ===")
for e in ('1e-3', '1e-5', '1e-7'):
    Fu = F_classes(R0*mpf(e), mpf(e))['u']
    show("eps=%s F_u" % e, Fu, 20)
show("1 - yc2/yt2", 1-YC2/YT2, 20)
show("F_u(1e-7) - (1-yc2/yt2)", F_classes(R0*mpf('1e-7'), mpf('1e-7'))['u'] - (1-YC2/YT2), 8)

print("=== c-class: y-only direction (s13=0) ===")
est = rich(lambda e: F_classes(mpf('0'), e)['c'] - 1, mpf('0.04'))
show("A2_c_y (expect 1/2)", est[-1], 30)
show("nsimplify", nsimplify(est[-1]), 10)

print("=== c-class: x-only direction (s23=0) ===")
g2 = rich(lambda e: F_classes(e, mpf('0'))['c'] - 1, mpf('0.04'))
show("A2_c_x", g2[-1], 30)
g4 = rich(lambda e: F_classes(e, mpf('0'))['c'] - 1, mpf('0.04'), p=4)
show("A4_c_x (if A2=0)", g4[-1], 20)

print("=== c-class: diagonal (s13=R0*s23) ===")
gd = rich(lambda e: F_classes(R0*e, e)['c'] - 1, mpf('0.04'))
show("A2_c_diag", gd[-1], 30)
A, C = g2[-1], est[-1]
B = (gd[-1] - A*R0**2 - C)/R0
show("B_c (cross coeff)", B, 25)
print("  nsimplify A:", nsimplify(A), " B:", nsimplify(B), " C:", nsimplify(C))

print("=== A2_c_y raw convergence (no Richardson) ===")
for e in ('1e-2', '1e-3', '1e-4', '1e-5'):
    ee = mpf(e)
    show("eps=%s (F_c-1)/eps^2" % e, (F_classes(mpf('0'), ee)['c']-1)/ee**2, 22)

print("=== A2_c_y mass dependence ===")
for tag, lam2, ups2 in [
    ("base", LAM, UPS),
    ("ys2 x4", (YD2, 4*YS2, YB2), UPS),
    ("yd2 /100", (YD2/100, YS2, YB2), UPS),
    ("yu2 ->0", LAM, (mpf('1e-30'), YC2, YT2)),
    ("yc2 x4", LAM, (YU2, 4*YC2, YT2)),
    ("yb2 x4", (YD2, YS2, 4*YB2), UPS),
]:
    est = rich(lambda e: F_classes(mpf('0'), e, lam=lam2, ups=ups2)['c'] - 1, mpf('0.04'))
    show("A2_c_y %s" % tag, est[-1], 22)
