"""WP49 pass 6: evaluate the purity law at the MEASURED point.

Builds the synthetic exact point (Hu = diag(yu2,yc2,yt2),
Hd = V_true.diag(yd2,ys2,yb2).V_true^+) and runs the per-anchor canonical
pipeline (WP44 convention) to (a) map the permuted-frame monomial indices to
true CKM elements, (b) evaluate C_class at the measured data via the
certified inversion d0 = sum um.lam, d1 = (beta.d0-e3)/(e1p.d0-e2+beta).

Measured inputs: OBS17 central values (wp7_ensemble); missing moduli by
unitarity (|Vud|, |Vcs|, |Vtb| = 1).
"""
import math, sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../checkers')
import wp7_ensemble as wp7

YU2, YC2, YT2 = 7.04e-6**2, 3.56e-3**2, 0.967**2
YD2, YS2, YB2 = 1.54e-5**2, 3.06e-4**2, 1.630e-2**2

# true CKM from OBS17 central values (standard parametrization free: use moduli + gamma)
Vus, Vub, Vcb = 0.22517, 0.003763, 0.04189
Vcd, Vtd, Vts = 0.22503, 0.00863, 0.04117
gam = math.radians(66.4)
Vud = math.sqrt(1 - Vus**2 - Vub**2)
Vcs = math.sqrt(1 - Vcd**2 - Vcb**2)
Vtb = 1.0
# build a unitary-consistent V: use Wolfenstein-ish closure via rows
V = np.array([
    [Vud, Vus, Vub*complex(math.cos(-gam), math.sin(-gam))],
    [-Vcd, Vcs, Vcb],
    [Vtd*complex(math.cos(math.pi), 0), -Vts, Vtb],
], complex)
# orthogonalize rows crudely is skipped: moduli are measured, phases only in (0,2),(2,0)
lam = np.array([YD2, YS2, YB2])
Hu_f = np.diag([YU2, YC2, YT2]).astype(complex)
Hd_f = V @ np.diag(lam) @ V.conj().T

for anchor, k in (('u', 0), ('c', 1), ('t', 2)):
    blk = [x for x in range(3) if x != k]
    # WP44 frame: try blk and blk[::-1], prefer first with |Hd_01|<1e-10;
    # synthetic point is generic, so just take natural blk order
    P = np.zeros((3, 3)); P[0, k] = 1; P[1, blk[0]] = 1; P[2, blk[1]] = 1
    HuC = P @ Hu_f @ P.T; Hd = P @ Hd_f @ P.T
    eu, Uu = np.linalg.eigh(HuC); ed, Ud = np.linalg.eigh(Hd)
    oe = np.argsort(eu); Uu = Uu[:, oe]; eu = eu[oe]
    od = np.argsort(ed); Ud = Ud[:, od]; ed = ed[od]
    Vc = Uu.conj().T @ Ud; Va = np.abs(Vc)
    print(f'anchor {anchor}: permuted |Vc| rows:')
    for row in Va:
        print('   ', ' '.join(f'{x:.5f}' for x in row))
    print('   true |V| singlet row:', ' '.join(f'{x:.5f}' for x in np.abs(V[k])))
    # inversion inputs: singlet row at sorted position k
    um = Va[k, :]**2
    e1, e2, e3 = ed.sum(), ed[0]*ed[1]+ed[0]*ed[2]+ed[1]*ed[2], ed[0]*ed[1]*ed[2]
    d0 = float((um*ed).sum())
    beta = float(e3*(um/ed).sum())
    e1p = e1 - d0
    d1 = (beta*d0 - e3)/(e1p*d0 - e2 + beta)
    # NOTE: d1 formula assumes the family (Hd_01 = 0); synthetic point is
    # generic, so this d1 is the FAMILY-PRESENTATION value at measured data.
    p0 = float(np.prod(d0 - ed)); p1 = float(np.prod(d1 - ed))
    v2 = p0/(d1 - d0); w2 = p1/(d0 - d1)
    s = eu[k]  # singlet eigenvalue ~ anchor mass^2
    nonsing = sorted(eu, key=lambda x: abs(x - s))[1:]
    blockgap = abs(nonsing[1] - nonsing[0])
    Dd = (ed[2]-ed[1])*(ed[2]-ed[0])*(ed[1]-ed[0])
    z = -(Vc[0,0]*Vc[0,2].conjugate())/(Vc[1,0]*Vc[1,2].conjugate())
    g2 = abs(math.atan2(z.imag, z.real)); sg = math.sin(g2)
    if anchor == 'u':
        scale2, V3 = YT2, Va[0,0]*Va[0,2]*Va[1,0]
    elif anchor == 'c':
        scale2, V3 = YT2, Va[0,0]*Va[1,0]*Va[1,2]
    else:
        scale2, V3 = YC2, Va[0,0]*Va[1,0]*Va[1,2]**2*sg
    C = blockgap*Dd*V3/(scale2*v2*math.sqrt(w2))
    print(f'   d0={d0:.6e} d1={d1:.6e} v2={v2:.6e} w2={w2:.6e}')
    print(f'   C_{anchor}(measured) = {C:.10f}')
