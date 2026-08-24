"""WP48 pass 4: purity ratio R = q.V3/(J.scale^2) constancy per class,
family vs complement; and spread budget: measured q-spread vs CKM-slack prediction.
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
R = {'u':{'f':[],'x':[]},'c':{'f':[],'x':[]},'t':{'f':[],'x':[]}}
MON = {'u':[],'c':[],'t':[]}   # physical monomial values per family sheet
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
        if best is None or abs(Hd[0,1]) < abs(best[1][0,1]): best = (HuC, Hd)
    HuC, Hd = best
    fam = abs(Hd[0,1]) < 1e-10
    c = HuC[1,2].real
    eu, Uu = np.linalg.eigh(HuC); ed, Ud = np.linalg.eigh(Hd)
    oe = np.argsort(eu); Uu = Uu[:, oe]; eu = eu[oe]
    od = np.argsort(ed); Ud = Ud[:, od]; ed = ed[od]
    yu2, yc2, yt2 = eu
    sphi = math.sin(fold(th[-1]))
    q = c*sphi
    Vc = Uu.conj().T @ Ud; V = np.abs(Vc)
    z = -(Vc[0,0]*Vc[0,2].conjugate())/(Vc[1,0]*Vc[1,2].conjugate())
    gam = abs(math.atan2(z.imag, z.real))
    sg = math.sin(gam)
    if anchor == 'u':
        scale2, V3, mon = yt2, V[0,0]*V[0,2]*V[1,0], V[1,2]*sg
    elif anchor == 'c':
        scale2, V3, mon = yt2, V[0,0]*V[1,0]*V[1,2], V[0,2]*sg
    else:
        scale2, V3, mon = yc2, V[0,0]*V[1,0]*V[1,2]**2*sg, V[0,2]/V[1,2]
    Rv = q*V3/(r['J']*scale2)
    R[anchor]['f' if fam else 'x'].append(Rv)
    if fam: MON[anchor].append(mon)

for a in 'uct':
    for g,lab in (('f','family'),('x','complement')):
        v = np.array(R[a][g])
        if len(v):
            print(f'{a} {lab:10s} n={len(v):4d}  R mean={v.mean():.10f} rel std={v.std()/v.mean():.3e} rel range={(v.max()-v.min())/v.mean():.3e}')
    m = np.array(MON[a])
    if len(m):
        qmean = np.array(R[a]['f']).mean()
        print(f'   monomial rel range={(m.max()-m.min())/m.mean():.3e}  (predicts q-spread at same level)')
