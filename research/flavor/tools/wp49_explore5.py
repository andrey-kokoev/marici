"""WP49 pass 5: exact block-rotation Uu for the singlet row, then invert.

The eigh-based Uu carries O(1e-8) singlet-block contamination (the sheet
filter), amplified ~yb^2/yd^2 ~ 1e9 in d0 = sum um.lam. Replace Uu by the
EXACT block rotation: UuC = [[1,0,0],[0,ct,-st],[0,st,ct]] diagonalizing the
up block. Then um = |(UuC^+ Ud)[0,:]|^2 is contamination-free and
  d0 = sum um.lam,  beta = e3.sum(um/lam),
  d1 = (beta.d0 - e3)/(e1p.d0 - e2 + beta),  d2 = e1p - d1,
  v2 = p(d0)/(d1-d0),  w2 = p(d1)/(d0-d1)
are exact. C pipeline as before. Reports per-anchor max rel err of d0,d1,d2,
v2,w2,C vs chart, and um vs eigh-row deviation.
"""
import json, math, sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../checkers')
import wp7_ensemble as wp7

MASSES2 = {'u': 7.04e-6**2, 'c': 3.56e-3**2, 't': 0.967**2}

def fold(p):
    p = abs(p) % math.pi
    return math.pi - p if p > math.pi/2 else p

recs = json.load(open('results/wp20_valley_audit.json'))['records']
errs = {a: {'d0':0.0,'d1':0.0,'v2':0.0,'w2':0.0,'C':0.0} for a in 'uct'}
um_dev = 0.0; rot_err = 0.0; n = 0
for r in recs:
    mu, md = r['member']; s_, i, j = r['phase_edge']
    th = np.array(r['log_mags'] + [r['phi_raw']])
    Yu, Yd = wp7.build_texture(mu, md, s_, (i, j), th)
    Hu = Yu @ Yu.conj().T
    off, k = min((max(abs(Hu[a, b]) for b in range(3) if b != a), a) for a in range(3))
    if off > 1e-8: continue
    blk = [x for x in range(3) if x != k]
    t = abs(0.5*math.atan2(2*Hu[blk[0], blk[1]].real, Hu[blk[1], blk[1]].real - Hu[blk[0], blk[0]].real))
    t = min(t, math.pi/2 - t)
    if t <= 1e-9: continue
    anchor = min(MASSES2, key=lambda m: abs(Hu[k, k].real/MASSES2[m]-1))
    Hd0 = Yd @ Yd.conj().T
    best = None
    for blko in (blk, blk[::-1]):
        P = np.zeros((3, 3)); P[0, k] = 1; P[1, blko[0]] = 1; P[2, blko[1]] = 1
        HuC = P @ Hu @ P.T; Hd = P @ Hd0 @ P.T
        if best is None or abs(Hd[0,1]) < abs(best[1][0,1]): best = (HuC, Hd, P)
    HuC, Hd, P = best
    if abs(Hd[0,1]) > 1e-10: continue
    s = HuC[0,0].real
    # exact block rotation diagonalizing HuC's 2x2 block
    a_, b_, c_ = HuC[1,1].real, HuC[2,2].real, HuC[1,2].real
    th2 = 0.5*math.atan2(2*c_, b_ - a_)
    ct, st = math.cos(th2), math.sin(th2)
    UuC = np.array([[1,0,0],[0,ct,-st],[0,st,ct]], float)
    D = UuC.T @ HuC @ UuC
    rot_err = max(rot_err, abs(D[1,2]), abs(D[0,1]), abs(D[0,2]))
    # choose rotation orientation so that block eigen order matches eigh sort
    ed, Ud = np.linalg.eigh(Hd)
    od = np.argsort(ed); Ud = Ud[:, od]; ed = ed[od]
    VX = UuC.T @ Ud
    um = VX[0, :]**2
    # compare with eigh pipeline row k
    eu, Uu = np.linalg.eigh(HuC)
    oe = np.argsort(eu); Uu = Uu[:, oe]; eu = eu[oe]
    Vc = Uu.conj().T @ Ud
    um_eigh = np.abs(Vc[k, :])**2
    um_dev = max(um_dev, float(np.max(np.abs(um - um_eigh))))
    # inversion
    e1, e2, e3 = ed.sum(), ed[0]*ed[1]+ed[0]*ed[2]+ed[1]*ed[2], ed[0]*ed[1]*ed[2]
    d0 = float((um*ed).sum())
    beta = float(e3*(um/ed).sum())
    e1p = e1 - d0
    d1 = (beta*d0 - e3)/(e1p*d0 - e2 + beta)
    d2 = e1p - d1
    p0 = float(np.prod(d0 - ed)); p1 = float(np.prod(d1 - ed))
    v2 = p0/(d1 - d0); w2 = p1/(d0 - d1)
    d0c, d1c = Hd[0,0].real, Hd[1,1].real
    v2c, w2c = abs(Hd[0,2])**2, abs(Hd[1,2])**2
    yu2, yc2, yt2 = eu
    Du = (yt2-yc2)*(yt2-yu2)*(yc2-yu2)
    Dd = (ed[2]-ed[1])*(ed[2]-ed[0])*(ed[1]-ed[0])
    nonsing = sorted(eu, key=lambda x: abs(x-s))[1:]
    blockgap = abs(nonsing[1]-nonsing[0])
    z = -(Vc[0,0]*Vc[0,2].conjugate())/(Vc[1,0]*Vc[1,2].conjugate())
    gam = abs(math.atan2(z.imag, z.real)); sg = math.sin(gam)
    V = np.abs(Vc)
    if anchor == 'u':
        scale2, V3 = yt2, V[0,0]*V[0,2]*V[1,0]
    elif anchor == 'c':
        scale2, V3 = yt2, V[0,0]*V[1,0]*V[1,2]
    else:
        scale2, V3 = yc2, V[0,0]*V[1,0]*V[1,2]**2*sg
    C_chart = blockgap*Dd*V3/(scale2*v2c*math.sqrt(w2c))
    n += 1
    E = errs[anchor]
    E['d0'] = max(E['d0'], abs(d0/d0c - 1))
    E['d1'] = max(E['d1'], abs(d1/d1c - 1))
    E['v2'] = max(E['v2'], abs(v2/v2c - 1))
    E['w2'] = max(E['w2'], abs(w2/w2c - 1))
    E['C'] = max(E['C'], abs(blockgap*Dd*V3/(scale2*v2*math.sqrt(w2))/C_chart - 1))

print(f'sheets: {n}; block-rotation diag err {rot_err:.2e}; um vs eigh-row max dev {um_dev:.2e}')
for a in 'uct':
    print(a, {k: f'{v:.2e}' for k, v in errs[a].items()})
