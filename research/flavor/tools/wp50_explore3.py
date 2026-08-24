"""WP50 explore 3: three chart strata; per-stratum inversion and chain.

Strata by down-sector zero pattern in the canonical frame:
  S1 chain-star  Hd_01 = 0 (family, 394): WP49 linear inversion.
  S2 singlet-star Hd_12 = 0 (282): loop dead, d1.d2 = beta, d1+d2 = e1';
     d1,d2 = roots of z^2 - e1'.z + beta; v2 = (K2 - d2.K1)/(d1 - d2),
     x = K1 - v2 (K1, K2 as before). Check swap ambiguity resolution.
  S3 generic triangle (172): loop alive.

Chain variants: regress q = |HuC_12|.sin(phi) against J.blockgap.Dd divided
by candidate edge-product denominators per stratum:
  S1: v2.sqrt(w2) [WP48 known]; S2: candidates x.sqrt(v2), sqrt(x).v2,
      x.v2, sqrt(x.v2); S3: same candidates + loop corrections.
J-loop regressions on S3: J.Du.Dd vs Im(mixed M = c.Hd_01.Hd_02*) and
vs Ls/2, scanning mass-factor normalizations.
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
s2_err = {'quad': 0.0, 'v2': 0.0, 'x': 0.0, 'swap': 0}
chains = {1: [], 2: [], 3: []}
jreg = []
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
        if best is None or abs(Hd[0, 1]) < abs(best[1][0, 1]): best = (HuC, Hd)
    HuC, Hd = best
    s = HuC[0, 0].real
    eu, Uu = np.linalg.eigh(HuC); ed, Ud = np.linalg.eigh(Hd)
    oe = np.argsort(eu); Uu = Uu[:, oe]; eu = eu[oe]
    od = np.argsort(ed); Ud = Ud[:, od]; ed = ed[od]
    Vc = Uu.conj().T @ Ud
    kpos = {'u': 0, 'c': 1, 't': 2}[anchor]
    um = np.abs(Vc[kpos, :])**2
    e1, e2, e3 = ed.sum(), ed[0]*ed[1]+ed[0]*ed[2]+ed[1]*ed[2], ed[0]*ed[1]*ed[2]
    d0 = float((um*ed).sum()); beta = float(e3*(um/ed).sum())
    e1p = e1 - d0
    K1 = beta + d0*e1p - e2
    K2 = d0*beta - e3
    d0c, d1c, d2c = Hd[0,0].real, Hd[1,1].real, Hd[2,2].real
    xc, v2c, w2c = abs(Hd[0,1])**2, abs(Hd[0,2])**2, abs(Hd[1,2])**2
    nonsing = sorted(eu, key=lambda z: abs(z - s))[1:]
    blockgap = abs(nonsing[1] - nonsing[0])
    Dd = (ed[2]-ed[1])*(ed[2]-ed[0])*(ed[1]-ed[0])
    Du = (eu[2]-eu[1])*(eu[2]-eu[0])*(eu[1]-eu[0])
    q = abs(HuC[1,2])*math.sin(fold(th[-1]))
    J = r['J']
    num = J*blockgap*Dd
    if abs(Hd[0,1]) < 1e-10:
        stratum = 1
    elif w2c < 1e-40:
        stratum = 2
    else:
        stratum = 3
    if stratum == 1:
        chains[1].append(q*v2c*math.sqrt(w2c)/num)
        continue
    if stratum == 2:
        # singlet-star inversion: d1,d2 roots of z^2 - e1p z + beta
        disc = e1p**2 - 4*beta
        rts = [(e1p + math.sqrt(disc))/2, (e1p - math.sqrt(disc))/2]
        # two assignments; select by x-split positivity
        best_asg = None
        for d1, d2 in ((rts[0], rts[1]), (rts[1], rts[0])):
            if abs(d1 - d2) < 1e-300: continue
            v2 = (K2 - d2*K1)/(d1 - d2)
            x = K1 - v2
            score = min(v2, x)
            if best_asg is None or score > best_asg[0]:
                best_asg = (score, d1, d2, v2, x)
        score, d1, d2, v2, x = best_asg
        s2_err['quad'] = max(s2_err['quad'], abs(d1/d1c - 1))
        s2_err['v2'] = max(s2_err['v2'], abs(v2/v2c - 1))
        s2_err['x'] = max(s2_err['x'], abs(x/xc - 1))
        if abs(d1/d1c - 1) > 1e-8: s2_err['swap'] += 1
        for name, den in [('x.sqrt(v2)', xc*math.sqrt(v2c)), ('sqrt(x).v2', math.sqrt(xc)*v2c),
                          ('x.v2', xc*v2c), ('sqrt(x.v2)', math.sqrt(xc*v2c)),
                          ('v2.sqrt(x)', v2c*math.sqrt(xc))]:
            chains[2].append((name, q*den/num))
        continue
    # S3 generic
    loop = Hd[0,1]*Hd[1,2]*Hd[2,0]
    M = HuC[1,2]*Hd[0,1]*Hd[0,2].conjugate()
    jreg.append({'JDD': J*Du*Dd, 'imM': M.imag, 'reM': M.real, 'Ls2': loop.imag,
                 'q': q, 'v2': v2c, 'w2': w2c, 'x': xc, 'num': num,
                 'bg': blockgap, 'Du': Du, 'J': J, 'Dd': Dd})
    for name, den in [('v2.sqrt(w2)', v2c*math.sqrt(w2c)), ('x.sqrt(w2)', xc*math.sqrt(w2c)),
                      ('sqrt(x).v2', math.sqrt(xc)*v2c)]:
        chains[3].append((name, q*den/num))

print('S2 singlet-star inversion: d1 quad', f"{s2_err['quad']:.2e}",
      'v2', f"{s2_err['v2']:.2e}", 'x', f"{s2_err['x']:.2e}", 'swaps', s2_err['swap'])
for st in (1, 2, 3):
    if st == 1:
        vals = chains[1]
        print(f'S1 q.v2.sqrt(w2)/num: mean {np.mean(vals):.6f} relstd {np.std(vals)/abs(np.mean(vals)):.2e} n={len(vals)}')
    else:
        by = {}
        for name, v in chains[st]: by.setdefault(name, []).append(v)
        n = len(chains[st])//len(by)
        for name, vals in by.items():
            m = np.mean(vals)
            print(f'S{st} q.{name}/num: mean {m:.6f} relstd {np.std(vals)/abs(m):.2e} n={n}')
# J regression on S3
jr = jreg
for key in ('imM', 'reM', 'Ls2'):
    rr = np.array([z['JDD']/z[key] if abs(z[key]) > 1e-300 else float('nan') for z in jr])
    rr = rr[~np.isnan(rr)]
    print(f'S3 J.Du.Dd / {key}: mean {rr.mean():.4e} relstd {rr.std()/abs(rr.mean()):.2e} n={len(rr)}')
# and J*blockgap*Dd vs q.v2.sqrt(w2) already above; check q vs Ls:
rr = np.array([z['JDD']/(z['q']*z['v2']*math.sqrt(z['w2'])) for z in jr])
print('S3 J.Du.Dd/(q.v2.sqrt(w2)): mean', f'{rr.mean():.4e}', 'relstd', f'{rr.std()/abs(rr.mean()):.2e}')
