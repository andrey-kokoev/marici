"""WP51 explore 1: why is F near 1? Dial the flavor hierarchy.

Synthetic exact point: Hu = diag(yu2,yc2,yt2), Hd = V.diag(lam).V^+ with V
the STANDARD parametrization (th12, th13, th23, delta) matched to OBS17.
F_class via the WP49 family-presentation pipeline (invert_down + c_value).

Dials (rho -> 0): th13 (Vub), th23 (Vcb), yd2, yu2, and the joint strict
limit (th13, th23, yd2, yu2 -> 0 together). Report F-1 vs rho log-slopes
and the strict-limit value of F per class.
"""
import math, sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../checkers')
import wp49_purity_derivation as w49

YU2, YC2, YT2 = 7.04e-6**2, 3.56e-3**2, 0.967**2
YD2, YS2, YB2 = 1.54e-5**2, 3.06e-4**2, 1.630e-2**2
TH12, TH13, TH23 = 0.22517, 0.003763, 0.04189  # sin values
DELTA = math.radians(66.4)

def std_V(s12, s13, s23, dl):
    c12, c13, c23 = (math.sqrt(1-x*x) for x in (s12, s13, s23))
    ed = complex(math.cos(dl), math.sin(dl))
    return np.array([
        [c12*c13, s12*c13, s13*ed.conjugate()],
        [-s12*c23 - c12*s23*s13*ed, c12*c23 - s12*s23*s13*ed, s23*c13],
        [s12*s23 - c12*c23*s13*ed, -c12*s23 - s12*c23*s13*ed, c23*c13]], complex)

def F_classes(V, lam, ups):
    Hu_f = np.diag(ups).astype(complex)
    Hd_f = V @ np.diag(lam) @ V.conj().T
    out = {}
    for anchor, kp in (('u', 0), ('c', 1), ('t', 2)):
        blk = [x for x in range(3) if x != kp]
        P = np.zeros((3, 3)); P[0, kp] = 1; P[1, blk[0]] = 1; P[2, blk[1]] = 1
        HuC = P @ Hu_f @ P.T; Hd = P @ Hd_f @ P.T
        eu, Uu = np.linalg.eigh(HuC)
        oe = np.argsort(eu); Uu = Uu[:, oe]; eu = eu[oe]
        ed, Ud = np.linalg.eigh(Hd)
        od = np.argsort(ed); Ud = Ud[:, od]; ed = ed[od]
        Vc = Uu.conj().T @ Ud
        um = np.abs(Vc[kp, :])**2
        d0, d1, d2, v2, w2 = w49.invert_down(um, ed)
        out[anchor] = w49.c_value(anchor, eu, ed, Vc, v2, w2, eu[kp])
    return out

base_lam = np.array([YD2, YS2, YB2])
base_ups = np.array([YU2, YC2, YT2])
V0 = std_V(TH12, TH13, TH23, DELTA)
F0 = F_classes(V0, base_lam, base_ups)
print('F at measured point:', {a: f'{F0[a]:.10f}' for a in 'uct'},
      ' F-1:', {a: f'{F0[a]-1:+.3e}' for a in 'uct'})

rhos = [1.0, 0.5, 0.25, 0.1, 0.03, 0.01]
def dial(name, rho):
    s12, s13, s23 = TH12, TH13, TH23
    lam = base_lam.copy(); ups = base_ups.copy()
    if name == 'th13': s13 = TH13*rho
    elif name == 'th23': s23 = TH23*rho
    elif name == 'yd2': lam[0] = YD2*rho
    elif name == 'yu2': ups[0] = YU2*rho
    elif name == 'strict':
        s13, s23 = TH13*rho, TH23*rho
        lam[0] = YD2*rho; ups[0] = YU2*rho
    return F_classes(std_V(s12, s13, s23, DELTA), lam, ups)

for name in ('th13', 'th23', 'yd2', 'yu2', 'strict'):
    rows = []
    for rho in rhos:
        F = dial(name, rho)
        rows.append((rho, [F[a]-1 for a in 'uct']))
    print(f'--- dial {name}:')
    for a_i, a in enumerate('uct'):
        vals = [r[1][a_i] for r in rows]
        # log-log slope between successive points where sign stable
        sl = []
        for i in range(len(rows)-1):
            x0, x1 = rows[i][0], rows[i+1][0]
            y0, y1 = vals[i], vals[i+1]
            if abs(y0) > 1e-12 and abs(y1) > 1e-12 and y0*y1 > 0:
                sl.append(math.log(abs(y1/y0))/math.log(x1/x0))
        print(f'   {a}: F-1 = ' + ' '.join(f'{v:+.2e}' for v in vals) +
              ('  slopes ~ ' + ', '.join(f'{s:.2f}' for s in sl) if sl else ''))
