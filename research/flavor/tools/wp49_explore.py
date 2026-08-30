"""WP49 exploration: invert the down diagonals from physical data, derive C.

Family frame: Hd = [[d0,0,v],[0,d1,w],[v*,w*,d2]], eigen profile
  Ud_m ~ (v/(lam_m-d0), w/(lam_m-d1), 1).
Since Uu keeps the singlet axis, the singlet CKM row IS the Ud first row:
  |V_{0m}|^2 = A_m/(A_m+B_m+1), A_m = v^2/(lam_m-d0)^2, B_m = w^2/(lam_m-d1)^2,
with v^2 = p(d0)/(d1-d0), w^2 = p(d1)/(d0-d1), p(l) = prod(l - lam_m).
So (d0,d1) = G(down masses, singlet-row |V|) - physical data only.
Then C = blockgap.Dd.V3/(scale^2.v^2.w) is a physical-data function.
"""
import json, math, sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../checkers')
import wp7_ensemble as wp7

MASSES2 = {'u': 7.04e-6**2, 'c': 3.56e-3**2, 't': 0.967**2}

def fold(p):
    p = abs(p) % math.pi
    return math.pi - p if p > math.pi/2 else p

def vw2(d0, d1, lam):
    p0 = np.prod(d0 - lam); p1 = np.prod(d1 - lam)
    return p0/(d1 - d0), p1/(d0 - d1)

def vrow2(d0, d1, lam):
    v2, w2 = vw2(d0, d1, lam)
    A = v2/(lam - d0)**2; B = w2/(lam - d1)**2
    return A/(A + B + 1.0)

def solve_diagonals(lam, target, x0):
    """Newton on m=1,2 equations; return d0,d1 and residual on all 3."""
    x = np.array(x0, float)
    for _ in range(60):
        f = vrow2(x[0], x[1], lam)[1:3] - target[1:3]
        if np.max(np.abs(f)) < 1e-17: break
        # numeric jacobian
        J = np.zeros((2, 2))
        for k in range(2):
            h = 1e-9*max(1.0, abs(x[k]))
            xp = x.copy(); xp[k] += h
            J[:, k] = (vrow2(xp[0], xp[1], lam)[1:3] - vrow2(x[0], x[1], lam)[1:3])/h
        try:
            dx = np.linalg.solve(J, -f)
        except np.linalg.LinAlgError:
            return None, None
        x += dx
        if np.max(np.abs(dx)) < 1e-16*max(1.0, abs(x[0]), abs(x[1])): break
    resid = vrow2(x[0], x[1], lam) - target
    return x, resid

recs = json.load(open('results/wp20_valley_audit.json'))['records']
inv_err = 0.0; cons_resid = 0.0; cpipe_err = 0.0; n = 0; fails = 0
C_phys = {'u': [], 'c': [], 't': []}
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
    eu, Uu = np.linalg.eigh(HuC); ed, Ud = np.linalg.eigh(Hd)
    oe = np.argsort(eu); Uu = Uu[:, oe]; eu = eu[oe]
    od = np.argsort(ed); Ud = Ud[:, od]; ed = ed[od]
    yu2, yc2, yt2 = eu
    Du = (yt2-yc2)*(yt2-yu2)*(yc2-yu2)
    Dd = (ed[2]-ed[1])*(ed[2]-ed[0])*(ed[1]-ed[0])
    Vc = Uu.conj().T @ Ud; V = np.abs(Vc)
    # singlet row of CKM in the FLAVOR frame: row k of V corresponds to singlet
    # (canonical frame row 0 = flavor k). V rows are flavor rows already.
    target = V[k, :]**2
    d0c, d1c = Hd[0,0].real, Hd[1,1].real
    sol, resid = solve_diagonals(ed, target, (d0c, d1c))
    if sol is None:
        fails += 1; continue
    n += 1
    inv_err = max(inv_err, abs(sol[0]/d0c - 1), abs(sol[1]/d1c - 1))
    cons_resid = max(cons_resid, float(np.max(np.abs(resid))))
    # pipeline C from physical data only
    v2, w2 = vw2(sol[0], sol[1], ed)
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
    C_pipe = blockgap*Dd*V3/(scale2*v2*math.sqrt(w2))
    v2c, w2c = abs(Hd[0,2])**2, abs(Hd[1,2])**2
    C_chart = blockgap*Dd*V3/(scale2*v2c*math.sqrt(w2c))
    cpipe_err = max(cpipe_err, abs(C_pipe/C_chart - 1))
    C_phys[anchor].append(C_pipe)

print(f'family sheets: {n}, solver failures: {fails}')
print(f'inversion max rel err (d0,d1 from physical data): {inv_err:.3e}')
print(f'overdetermination residual (3rd equation):         {cons_resid:.3e}')
print(f'pipeline vs chart C max rel err:                   {cpipe_err:.3e}')
for a in 'uct':
    v = np.array(C_phys[a])
    if len(v):
        print(f'C_{a} from physical data: mean={v.mean():.10f} rel std={v.std()/v.mean():.2e} n={len(v)}')
