"""WP50 explore 4: consolidated certification of the chart-complete inversion.

Universal (all strata): d0, beta, K1, K2.
x from up-mass block data - determine the SINGLE winning convention.
S2 linear d1 = (K2 - e1'.x)/(v2 - x); S2 loop dead check (L, Ls ~ 0).
S3 quadratic with x, Ls(chart): root match, second-root physicality
(w2 sign at the other root).
"""
import json, math, sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../checkers')
import wp7_ensemble as wp7

MASSES2 = {'u': 7.04e-6**2, 'c': 3.56e-3**2, 't': 0.967**2}
recs = json.load(open('results/wp20_valley_audit.json'))['records']
conv_win = {z: 0 for z in 'ABCD'}
err = {'x': 0.0, 's2d1': 0.0, 's2L': 0.0, 's3d1': 0.0, 's3det': 0.0}
s3_other = []
n = {1: 0, 2: 0, 3: 0}
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
    if abs(Hd[0,1]) < 1e-10:
        n[1] += 1
        continue
    # x via up-mass block data, 4 conventions
    a_, b_, c_ = HuC[1,1].real, HuC[2,2].real, HuC[1,2]
    th2 = 0.5*math.atan2(2*c_.real, b_ - a_)
    ct, st = math.cos(th2), math.sin(th2)
    chat = c_/abs(c_)
    Hm = Vc @ np.diag(ed) @ Vc.conj().T
    rows = [kpos] + [z for z in range(3) if z != kpos]
    HmC = Hm[np.ix_(rows, rows)]
    m01, m02 = HmC[0,1], HmC[0,2]
    cands = {
        'A': ct**2*abs(m01)**2 + st**2*abs(m02)**2 + 2*ct*st*(chat*m01.conjugate()*m02).real,
        'B': st**2*abs(m01)**2 + ct**2*abs(m02)**2 - 2*ct*st*(chat*m01.conjugate()*m02).real,
        'C': ct**2*abs(m01)**2 + st**2*abs(m02)**2 - 2*ct*st*(chat*m01.conjugate()*m02).real,
        'D': st**2*abs(m01)**2 + ct**2*abs(m02)**2 + 2*ct*st*(chat*m01.conjugate()*m02).real,
    }
    rel = {z: abs(v/xc - 1) for z, v in cands.items()}
    win = min(rel, key=rel.get)
    conv_win[win] += 1
    if rel[win] > 1e-9: continue
    x = cands[win]
    err['x'] = max(err['x'], rel[win])
    v2 = K1 - x
    if w2c < 1e-40:
        n[2] += 1
        d1 = (K2 - e1p*x)/(v2 - x)
        err['s2d1'] = max(err['s2d1'], abs(d1/d1c - 1))
        loop = Hd[0,1]*Hd[1,2]*Hd[2,0]
        err['s2L'] = max(err['s2L'], abs(loop))
        continue
    n[3] += 1
    loop = Hd[0,1]*Hd[1,2]*Hd[2,0]
    Lc, Ls = 2*loop.real, 2*loop.imag
    # det identity residual at chart d1
    Lpred = d1c*(v2c - xc) + e1p*xc - K2
    err['s3det'] = max(err['s3det'], abs(Lpred - Lc)/abs(Lc))
    # quadratic for d1 given x, Ls
    B1 = v2 - x; B0 = e1p*x - K2
    A2 = B1**2 + 4*x*v2; A1 = 2*B1*B0 - 4*x*v2*e1p; A0 = B0**2 + Ls**2 + 4*x*v2*beta
    disc = A1**2 - 4*A2*A0
    if disc < 0:
        err['s3d1'] = max(err['s3d1'], 1.0)
        continue
    rts = [(-A1 + math.sqrt(disc))/(2*A2), (-A1 - math.sqrt(disc))/(2*A2)]
    near = min(rts, key=lambda z: abs(z - d1c))
    far = max(rts, key=lambda z: abs(z - d1c))
    err['s3d1'] = max(err['s3d1'], abs(near/d1c - 1))
    # physicality of the far root: w2 = d1(e1p-d1) - beta there
    w2far = far*(e1p - far) - beta
    s3_other.append((abs(far/d1c - 1), w2far < 0, w2far/max(abs(w2c),1e-300)))
print('convention wins:', conv_win)
print('strata:', n)
print('x err:', f"{err['x']:.2e}")
print('S2 d1 linear:', f"{err['s2d1']:.2e}", ' S2 |loop| max:', f"{err['s2L']:.2e}")
print('S3 det identity:', f"{err['s3det']:.2e}", ' S3 d1 root:', f"{err['s3d1']:.2e}")
fr = np.array([z[0] for z in s3_other]); neg = sum(1 for z in s3_other if z[1])
print('S3 far-root rel distance median:', f'{np.median(fr):.2e}', '; far root w2<0 count:', neg, '/', len(s3_other))
