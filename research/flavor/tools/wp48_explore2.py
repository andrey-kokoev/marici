"""WP48 pass 2: q as an exact physical-invariant monomial per class.

WP43/44 chain: M = Du Dd V3/(scale^2 C)?? -- test the exact closed forms:
  q = c.sin(phi) = J.Du.Dd/M  (exact per sheet)
  on family: M = v^2.w.chiB (exact), Du/chiB = blockgap (exact)
  => q = J.Dd.blockgap/(v^2.w)   [fixed: v^2 = |Hd02|^2, w = |Hd12|]
Then test the monomial hypothesis:
  q ?= C_class . J . scale^2 / Vmon  per anchor class
with C_u=0.9993729706, C_c=1.0008814042, C_t=0.9920333163 and the WP44-coded
(scale2, Vmon) per class.
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
chain_err = 0.0; mono_err = {'u':0.0,'c':0.0,'t':0.0}; nmono = {'u':0,'c':0,'t':0}
rows = []
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
    s = HuC[0,0].real; c = HuC[1,2].real
    eu, Uu = np.linalg.eigh(HuC); ed, Ud = np.linalg.eigh(Hd)
    oe = np.argsort(eu); Uu = Uu[:, oe]; eu = eu[oe]
    od = np.argsort(ed); Ud = Ud[:, od]; ed = ed[od]
    yu2, yc2, yt2 = eu
    Du = (yt2-yc2)*(yt2-yu2)*(yc2-yu2)
    Dd = (ed[2]-ed[1])*(ed[2]-ed[0])*(ed[1]-ed[0])
    sphi = math.sin(fold(th[-1]))
    q = c*sphi
    nonsing = sorted(eu, key=lambda x: abs(x-s))[1:]
    blockgap = abs(nonsing[1]-nonsing[0])
    v2 = abs(Hd[0,2])**2; w = abs(Hd[1,2])
    q_exact = r['J']*blockgap*Dd/(v2*w)
    chain_err = max(chain_err, abs(q_exact/q - 1))
    Vc = Uu.conj().T @ Ud; V = np.abs(Vc)
    z = -(Vc[0,0]*Vc[0,2].conjugate())/(Vc[1,0]*Vc[1,2].conjugate())
    gam = abs(math.atan2(z.imag, z.real))
    if anchor == 'u':
        scale2, Vmon = yt2, V[1,2]*math.sin(gam)
    elif anchor == 'c':
        scale2, Vmon = yt2, V[0,2]*math.sin(gam)
    else:
        scale2, Vmon = yc2, V[0,2]/V[1,2]
    q_mono = CCLASS[anchor]*r['J']*scale2/Vmon
    mono_err[anchor] = max(mono_err[anchor], abs(q_mono/q - 1))
    nmono[anchor] += 1
    rows.append({'anchor':anchor,'q':q,'q_mono':q_mono,'gamma':math.degrees(gam),
                 'phi_deg':r['phi_folded_deg'],'J':r['J']})

print(f'CHAIN (fixed) q = J.blockgap.Dd/(v^2.w): max rel err {chain_err:.3e}')
for a in 'uct':
    print(f'MONOMIAL {a}: n={nmono[a]}  max |q_mono/q - 1| = {mono_err[a]:.3e}')
# residual structure of the monomial per class
for a in 'uct':
    rr = [x for x in rows if x['anchor']==a]
    if not rr: continue
    res = np.array([x['q_mono']/x['q'] for x in rr])
    print(f'  {a}: q_mono/q mean={res.mean():.9f} std={res.std():.2e} min={res.min():.9f} max={res.max():.9f}')
