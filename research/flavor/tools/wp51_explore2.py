"""WP51 explore 2: remaining mass dials + coefficient identification."""
import math, sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wp51_explore import (std_V, F_classes, base_lam, base_ups,
                          TH12, TH13, TH23, DELTA, YU2, YC2, YT2, YD2, YS2, YB2)

def F_at(s12=TH12, s13=TH13, s23=TH23, dl=DELTA, lam=None, ups=None):
    return F_classes(std_V(s12, s13, s23, dl),
                     base_lam if lam is None else lam,
                     base_ups if ups is None else ups)

def show(tag, F):
    print(tag + ": " + "  ".join("%s=%+.6e" % (a, F[a]-1) for a in 'uct'))

# 1. remaining mass dials
print("=== yc2 dial ===")
for f in [0.0, 0.5, 2.0, 4.0]:
    u = base_ups.copy(); u[1] = YC2*f
    show("yc2 x%.2f" % f, F_at(ups=u))
print("=== ys2 dial ===")
for f in [0.0, 0.5, 2.0, 4.0]:
    l = base_lam.copy(); l[1] = YS2*f
    show("ys2 x%.2f" % f, F_at(lam=l))
print("=== yt2 dial ===")
for f in [0.25, 0.5, 2.0]:
    u = base_ups.copy(); u[2] = YT2*f
    show("yt2 x%.2f" % f, F_at(ups=u))
print("=== yb2 dial ===")
for f in [0.25, 0.5, 2.0]:
    l = base_lam.copy(); l[2] = YB2*f
    show("yb2 x%.2f" % f, F_at(lam=l))

# 2. th23 fine dial: Delta/Vcb^2 ratios
print("=== th23 fine: Delta/Vcb^2 ===")
for rho in [1.0, 0.5, 0.25, 0.1]:
    th = TH23*rho
    F = F_at(s23=th)
    v = math.sin(th)**2
    print("rho=%.2f: " % rho + "  ".join("%s: D=%+.8e D/Vcb2=%+.6f" % (a, F[a]-1, (F[a]-1)/v) for a in 'uct'))

# 3. th13 fine dial for u class: residual after removing th13 dependence
print("=== th13 fine (u,c) ===")
for rho in [1.0, 0.5, 0.25, 0.1]:
    F = F_at(s13=TH13*rho)
    print("rho=%.2f: " % rho + "  ".join("%s=%+.8e" % (a, F[a]-1) for a in 'uc'))

# 4. t-class 2D grid
print("=== t grid: rows s23 factor, cols s13 factor ===")
for fr23 in [1.0, 0.7, 0.5, 0.3]:
    row = []
    for fr13 in [1.0, 0.7, 0.5, 0.3, 0.1]:
        row.append(F_at(s13=TH13*fr13, s23=TH23*fr23)['t']-1)
    print("r23=%.2f: " % fr23 + " ".join("%+.5e" % x for x in row))

# 5. candidate formula checks at base
V = std_V(TH12, TH13, TH23, DELTA)
Vub, Vcb, Vus, Vcd = abs(V[0][2]), abs(V[1][2]), abs(V[0][1]), abs(V[1][0])
Vtd, Vts = abs(V[2][0]), abs(V[2][1])
base = F_at()
print("=== candidates at base ===")
print("Du=%+.6e" % (base['u']-1))
print("  -0.348*Vcb^2      = %+.6e" % (-0.348*Vcb**2))
print("  -Vcb^2*Vus^2*? : Vcb^2=%.4e Vus^2=%.4e" % (Vcb**2, Vus**2))
print("Dc=%+.6e ; 0.5*Vcb^2=%+.6e ; ratio=%.6f" % (base['c']-1, 0.5*Vcb**2, (base['c']-1)/Vcb**2))
print("Dt=%+.6e" % (base['t']-1))
print("  -(Vub/Vcb)^2          = %+.6e" % (-(Vub/Vcb)**2))
print("  -(Vub/Vcb)^2(1+Vus^2) = %+.6e" % (-(Vub/Vcb)**2*(1+Vus**2)))
print("  -(Vtd/Vts)^2          = %+.6e" % (-(Vtd/Vts)**2))
print("  -(Vub/Vts)^2          = %+.6e" % (-(Vub/Vts)**2))
print("  Vtd=%.6e Vts=%.6e Vtd/Vts=%.6f" % (Vtd, Vts, Vtd/Vts))
