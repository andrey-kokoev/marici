"""WP48 pass 3: certify the exact physical monomial laws for q = c.sin(phi).

Theorem candidate (family): q = C_class . scale^2 . J / V3_class, i.e.
  u: q = C_u . yt^2 . |Vcb| . sin(gamma)
  c: q = C_c . yt^2 . |Vub| . sin(gamma)
  t: q = C_t . yc^2 . |Vub| / |Vcb|
with C_u=0.9993729706, C_c=1.0008814042, C_t=0.9920333163 (WP44 pure numbers).
Also: complement-family behavior of the same ratio (boundary test).
"""
import json, math, sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../checkers')
import wp7_ensemble as wp7

MASSES2 = {'u': 7.04e-6**2, 'c': 3.56e-3**2, 't': 0.967**2}
CCLASS = {'u': 0.9993729706, 'c': 1.0008814042, 't': 0.9920333163}

def fold(p):
    p = abs(p) % math.pi
    return math.pi - p if p > math.pi/2 else p

recs = json.load(open('results/wp20_valley_audit.json'))['records']
fam_err = {'u':0.0,'c':0.0,'t':0.0}; nfam={'u':0,'c':0,'t':0}
comp_ratio = {'u':[],'c':[],'t':[]}
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
    s = HuC[0,0].real; c = HuC[1,2].real
    eu, Uu = np.linalg.eigh(HuC); ed, Ud = np.linalg.eigh(Hd)
    oe = np.argsort(eu); Uu = Uu[:, oe]; eu = eu[oe]
    od = np.argsort(ed); Ud = Ud[:, od]; ed = ed[od]
    yu2, yc2, yt2 = eu
    sphi = math.sin(fold(th[-1]))
    q = c*sphi
    Vc = Uu.conj().T @ Ud; V = np.abs(Vc)
    z = -(Vc[0,0]*Vc[0,2].conjugate())/(Vc[1,0]*Vc[1,2].conjugate())
    gam = abs(math.atan2(z.imag, z.real))
    if anchor == 'u':
        law = CCLASS['u']*yt2*V[1,2]*math.sin(gam)
    elif anchor == 'c':
        law = CCLASS['c']*yt2*V[0,2]*math.sin(gam)
    else:
        law = CCLASS['t']*yc2*V[0,2]/V[1,2]
    if fam:
        fam_err[anchor] = max(fam_err[anchor], abs(law/q - 1))
        nfam[anchor] += 1
    else:
        comp_ratio[anchor].append(law/q)

for a in 'uct':
    print(f'FAMILY {a}: n={nfam[a]:4d}  max |law/q - 1| = {fam_err[a]:.3e}')
for a in 'uct':
    cr = np.array(comp_ratio[a])
    if len(cr):
        print(f'COMPLEMENT {a}: n={len(cr):4d}  law/q mean={cr.mean():.6f} rel std={cr.std()/abs(cr.mean()):.3e} range=[{cr.min():.4f},{cr.max():.4f}]')
