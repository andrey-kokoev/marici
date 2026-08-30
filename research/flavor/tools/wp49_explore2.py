"""WP49 pass 2: exact physical inversion of the down sector, then C.

Exact chain (all physical inputs: down masses lam, singlet CKM row um = |V[k,m]|^2):
  d0 = sum_m um.lam_m            (spectral diagonal identity)
  beta = e3 . sum_m um/lam_m     (resolvent 00-minor constant term)
  e1.x^2 - (e1'.d0 - e2 + beta).x - (e3 - beta.d0) = 0,  roots = {d1, d2}
  v^2 = p(d0)/(d1-d0),  w^2 = p(d1)/(d0-d1),  p(l) = prod(l - lam)
  C = blockgap.Dd.V3/(scale^2 . v^2 . sqrt(w^2))
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
d0_err = 0.0; dq_err = 0.0; C_err_best = 0.0
branch_same = 0.0; n = 0; npos = 0
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
    if abs(Hd[0,1]) > 1e-10: continue
    s = HuC[0,0].real
    eu, Uu = np.linalg.eigh(HuC); ed, Ud = np.linalg.eigh(Hd)
    oe = np.argsort(eu); Uu = Uu[:, oe]; eu = eu[oe]
    od = np.argsort(ed); Ud = Ud[:, od]; ed = ed[od]
    yu2, yc2, yt2 = eu
    Du = (yt2-yc2)*(yt2-yu2)*(yc2-yu2)
    Dd = (ed[2]-ed[1])*(ed[2]-ed[0])*(ed[1]-ed[0])
    Vc = Uu.conj().T @ Ud; V = np.abs(Vc)
    um = V[0, :]**2  # canonical row 0 = singlet flavor row
    e1, e2, e3 = ed.sum(), ed[0]*ed[1]+ed[0]*ed[2]+ed[1]*ed[2], ed[0]*ed[1]*ed[2]
    d0 = float((um*ed).sum())
    beta = float(e3*(um/ed).sum())
    e1p = e1 - d0
    # quadratic e1 x^2 - (e1p.d0 - e2 + beta) x - (e3 - beta.d0) = 0
    A2, B2, C2 = e1, -(e1p*d0 - e2 + beta), -(e3 - beta*d0)
    disc = B2*B2 - 4*A2*C2
    if disc < 0: continue
    roots = [(-B2 + math.sqrt(disc))/(2*A2), (-B2 - math.sqrt(disc))/(2*A2)]
    d0c, d1c, d2c = Hd[0,0].real, Hd[1,1].real, Hd[2,2].real
    n += 1
    d0_err = max(d0_err, abs(d0/d0c - 1))
    dq_err = max(dq_err, min(abs(roots[0]/d1c-1)+abs(roots[1]/d2c-1),
                             abs(roots[1]/d1c-1)+abs(roots[0]/d2c-1)))
    # C per branch (d1 = root), compare with chart C
    nonsing = sorted(eu, key=lambda x: abs(x-s))[1:]
    blockgap = abs(nonsing[1]-nonsing[0])
    z = -(Vc[0,0]*Vc[0,2].conjugate())/(Vc[1,0]*Vc[1,2].conjugate())
    gam = abs(math.atan2(z.imag, z.real)); sg = math.sin(gam)
    if anchor == 'u':
        scale2, V3 = yt2, V[0,0]*V[0,2]*V[1,0]
    elif anchor == 'c':
        scale2, V3 = yt2, V[0,0]*V[1,0]*V[1,2]
    else:
        scale2, V3 = yc2, V[0,0]*V[1,0]*V[1,2]**2*sg
    v2c, w2c = abs(Hd[0,2])**2, abs(Hd[1,2])**2
    C_chart = blockgap*Dd*V3/(scale2*v2c*math.sqrt(w2c))
    p0 = np.prod(d0 - ed)
    Cs = []
    for d1 in roots:
        v2 = p0/(d1 - d0); w2 = np.prod(d1 - ed)/(d0 - d1)
        if v2 <= 0 or w2 <= 0:
            Cs.append(None); continue
        npos += 1
        Cs.append(blockgap*Dd*V3/(scale2*v2*math.sqrt(w2)))
    good = [x for x in Cs if x is not None]
    if good:
        C_err_best = max(C_err_best, min(abs(x/C_chart - 1) for x in good))
        if len(good) == 2:
            branch_same = max(branch_same, abs(good[0]/good[1] - 1))

print(f'family sheets: {n}')
print(f'd0 = sum um.lam   max rel err: {d0_err:.3e}')
print(f'd1,d2 quadratic   max rel err: {dq_err:.3e}')
print(f'C physical-pipeline (best branch) max rel err: {C_err_best:.3e}')
print(f'branch asymmetry of C (two positive branches): {branch_same:.3e}')
