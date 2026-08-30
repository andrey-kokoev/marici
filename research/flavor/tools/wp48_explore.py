"""WP48 exploration: what actually pins q = c.sin(phi) inside the fit manifold.

Chain under test (per sheet, exact):
  q = c.sin(phi) = J.Du.Dd/M  (WP36 G4)
  on the WP44 family (Hd_01 = 0 canonical): M = |v|^2|w||chiB|, Du/chiB = blockgap
  => q = J.blockgap.Dd/(|v||w|)
New lemma under test: with u = Hd_01 = 0 the down char poly gives
  |v|^2 = (T - d0.S)/(d1 - d0),  |w|^2 = (d1.S - T)/(d1 - d0),
  S = d0d1+d0d2+d1d2 - e2,  T = d0d1d2 - e3,
so q = Q(J, masses, d0, d1) EXACTLY - all chart freedom in q is two down row norms.
Then measure: within-valley vs cross-valley spread of q, d0, d1, gamma.
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
out = []
lem_err = 0.0; chain_err = 0.0; n_fam = 0
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
    eu = np.linalg.eigvalsh(HuC); ed = np.linalg.eigvalsh(Hd)
    yu2, yc2, yt2 = eu
    Du = (yt2-yc2)*(yt2-yu2)*(yc2-yu2)
    Dd = (ed[2]-ed[1])*(ed[2]-ed[0])*(ed[1]-ed[0])
    sphi = math.sin(fold(th[-1]))
    q = c*sphi
    M = r['J']*Du*Dd/q
    nonsing = sorted(eu, key=lambda x: abs(x-s))[1:]
    blockgap = abs(nonsing[1]-nonsing[0])
    row = {'anchor': anchor, 'fam': fam, 'q': q, 'M': M, 'J': r['J'],
           'gamma': r['ut_angles_deg']['gamma'], 'phi_deg': r['phi_folded_deg'],
           'orbit': r['orbit'], 'kind': r['valley_kind']}
    if fam:
        n_fam += 1
        d0, d1, d2 = Hd[0,0].real, Hd[1,1].real, Hd[2,2].real
        v2, w2 = abs(Hd[0,2])**2, abs(Hd[1,2])**2
        e2 = ed[0]*ed[1]+ed[0]*ed[2]+ed[1]*ed[2]; e3 = ed[0]*ed[1]*ed[2]
        S = d0*d1+d0*d2+d1*d2 - e2; T = d0*d1*d2 - e3
        v2p = (T - d0*S)/(d1 - d0); w2p = (d1*S - T)/(d1 - d0)
        lem_err = max(lem_err, abs(v2p/v2-1), abs(w2p/w2-1))
        q_exact = r['J']*blockgap*Dd/math.sqrt(v2*w2)
        chain_err = max(chain_err, abs(q_exact/q - 1))
        row.update(d0=d0, d1=d1, d2=d2, v2=v2, w2=w2, blockgap=blockgap, Dd=Dd)
    out.append(row)

print(f'sheets used: {len(out)}, family: {n_fam}')
print(f'LEMMA max rel err (|v|^2,|w|^2 from diagonals+masses): {lem_err:.3e}')
print(f'CHAIN max rel err (q = J.blockgap.Dd/(|v||w|)):       {chain_err:.3e}')

# spread analysis per anchor class
for anch in ('u','c','t'):
    rows = [x for x in out if x['anchor']==anch and x['fam']]
    if not rows: continue
    qs = np.array([x['q'] for x in rows])
    print(f"\nanchor {anch}: n={len(rows)}  q mean={qs.mean():.7e} rel spread={(qs.max()-qs.min())/qs.mean():.3e}")
    # valley clustering by phi at 0.05 deg
    rows.sort(key=lambda x: x['phi_deg'])
    valleys, cur = [], [rows[0]]
    for x in rows[1:]:
        if abs(x['phi_deg'] - cur[-1]['phi_deg']) < 0.05: cur.append(x)
        else: valleys.append(cur); cur=[x]
    valleys.append(cur)
    for v in valleys:
        if len(v) < 8: continue
        qv = np.array([x['q'] for x in v]); gv = np.array([x['gamma'] for x in v])
        d0v = np.array([x['d0'] for x in v]); d1v = np.array([x['d1'] for x in v])
        ph = np.array([x['phi_deg'] for x in v])
        def rs(a): 
            m=abs(a.mean()); return (a.max()-a.min())/m if m>0 else float('nan')
        cq = np.corrcoef(qv, gv)[0,1] if gv.std()>0 else float('nan')
        cphi = np.corrcoef(qv, ph)[0,1] if ph.std()>0 else float('nan')
        print(f"  valley phi~{ph.mean():7.3f} n={len(v):4d}  rs(q)={rs(qv):.2e} rs(d0)={rs(d0v):.2e} rs(d1)={rs(d1v):.2e} rs(gamma)={rs(gv):.2e} corr(q,gamma)={cq:+.3f} corr(q,phi)={cphi:+.3f}")
