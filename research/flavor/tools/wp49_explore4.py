"""WP49 pass 4: exact rational inversion, singlet row at sorted position k.

um = VC[k,:]^2 (singlet row after eigen-sort), then
  d0 = sum um.lam ; beta = e3.sum(um/lam) ; e1p = e1 - d0
  d1 = (beta.d0 - e3)/(e1p.d0 - e2 + beta) ; d2 = e1p - d1
  v^2 = p(d0)/(d1-d0) ; w^2 = p(d1)/(d0-d1)
C = blockgap.Dd.V3/(scale^2.v^2.sqrt(w^2))  -- and the swapped branch
  C_swap with (d1,v) <-> (d2,w) roles.
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
diag_err = {'d0':0.0,'d1':0.0,'d2':0.0}
C_err = {'u':0.0,'c':0.0,'t':0.0}; swap_needed = {'u':0,'c':0,'t':0}; nbad = 0
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
    um = V[k, :]**2
    e1, e2, e3 = ed.sum(), ed[0]*ed[1]+ed[0]*ed[2]+ed[1]*ed[2], ed[0]*ed[1]*ed[2]
    d0 = float((um*ed).sum())
    beta = float(e3*(um/ed).sum())
    e1p = e1 - d0
    d1 = (beta*d0 - e3)/(e1p*d0 - e2 + beta)
    d2 = e1p - d1
    p0 = float(np.prod(d0 - ed))
    d0c, d1c, d2c = Hd[0,0].real, Hd[1,1].real, Hd[2,2].real
    diag_err['d0'] = max(diag_err['d0'], abs(d0 - d0c)/(abs(d0c)+1e-300))
    diag_err['d1'] = max(diag_err['d1'], min(abs(d1-d1c), abs(d1-d2c))/(abs(d1c)+1e-300))
    diag_err['d2'] = max(diag_err['d2'], min(abs(d2-d2c), abs(d2-d1c))/(abs(d2c)+1e-300))
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
    # branch A: (v2,w2) from (d0,d1); branch B: swap d1<->d2 roles
    p1 = float(np.prod(d1 - ed)); p2 = float(np.prod(d2 - ed))
    out = []
    for dd, pp in ((d1, p1), (d2, p2)):
        v2 = p0/(dd - d0); w2 = pp/(d0 - dd)
        if v2 > 0 and w2 > 0:
            out.append(blockgap*Dd*V3/(scale2*v2*math.sqrt(w2)))
        else:
            out.append(None)
    errs = [abs(x/C_chart - 1) if x else 1e9 for x in out]
    bi = int(np.argmin(errs))
    if errs[bi] > 1e-6: nbad += 1
    if bi == 1: swap_needed[anchor] += 1
    C_err[anchor] = max(C_err[anchor], errs[bi])

print('diagonal max rel errs:', {k: f'{v:.2e}' for k, v in diag_err.items()})
print('sheets with C err > 1e-6 on best branch:', nbad)
for a in 'uct':
    print(f'{a}: pipeline C max rel err {C_err[a]:.3e}, swap-branch sheets: {swap_needed[a]}')
