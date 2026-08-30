"""WP39: the charge-CKM ratio descends - kappa_u = q_u/V_ub is a function
of the physical readout, not of the chart.

WP38 found q_u = kappa_u * V_ub exactly per sheet (bulk 9.2e-9). This
package determines WHAT kappa_u is:

  1. NOT a texture-algebra identity: random log-mag perturbations
     (eps=0.01, no refit) drift kappa at ~4x the perturbation size.
  2. A readout function: refitting the same texture against shifted
     central values moves kappa linearly with the physical shift over
     three decades (Vub central +1e-5..+1e-3 -> kappa slope
     -0.442 +/- 0.3%). kappa = F(physical point).
  3. The fitted ensemble's sheet-to-sheet physical scatter lies in
     ker(dF): kappa is constant at 1e-8 while fitted Vub scatters at
     3.3e-5 - so q_u/V_ub descends to a well-defined function on the
     physical quotient near the fitted point, even though q_u itself
     is chart data (WP11 consistent).
  4. Same-point pair: texture [417,482] d12 has TWO fitted sheets with
     identical mass spectra and identical CKM matrices (<1e-6) but
     different anchor partitions (u-singlet vs c-singlet) and charges
     differing by the anchor ratio 11.15 - the concrete illustration
     that the charge expression is per-anchor chart data while its
     ratio with V_ub is physical.

Gates:
  G1 bulk law: bulk max dev < 1e-7, <= 1 outlier (WP38 regression);
  G2 not-algebraic: eps=0.01 perturbation drift of kappa > 1e-3;
  G3 refit linearity: kappa response slope across 1e-5/1e-4/1e-3
     shifts constant within 1%;
  G4 same-point pair: max |dV| < 1e-6 and mass spectra match < 1e-5
     rel, q ratio in [11.0, 11.3];
  G5 physics response: |kappa(refit Vub+1e-3) - kappa0| > 100 * bulk.

Reads: results/wp20_valley_audit.json
Writes: results/wp39_kappa_descent.json
Run: ./.venv/Scripts/python checkers/wp39_kappa_descent.py
"""
import json, math, os, sys

import numpy as np
from scipy.optimize import least_squares

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wp7_ensemble as wp7

MASSES2 = {'u': 7.04e-6**2, 'c': 3.56e-3**2, 't': 0.967**2}
CENT = np.array([c for _, c, _ in wp7.OBS17])
SIG = np.array([s for _, _, s in wp7.OBS17])
NAMES = [n for n, _, _ in wp7.OBS17]

def fold(p):
    p = abs(p) % math.pi
    return math.pi - p if p > math.pi/2 else p

def sheet_data(mu, md, s_, ij, th):
    Yu, Yd = wp7.build_texture(mu, md, s_, ij, th)
    Hu = Yu @ Yu.conj().T
    off, k = min((max(abs(Hu[a, b]) for b in range(3) if b != a), a)
                 for a in range(3))
    blk = [x for x in range(3) if x != k]
    t = abs(0.5*math.atan2(2*Hu[blk[0], blk[1]].real,
                           Hu[blk[1], blk[1]].real - Hu[blk[0], blk[0]].real))
    t = min(t, math.pi/2 - t)
    if off > 1e-8 or t <= 1e-9:
        return None
    anchor = min(MASSES2, key=lambda m: abs(Hu[k, k].real/MASSES2[m]-1))
    Hd = Yd @ Yd.conj().T
    eu, Uu = np.linalg.eigh(Hu); ed, Ud = np.linalg.eigh(Hd)
    Uu = Uu[:, np.argsort(eu)]; Ud = Ud[:, np.argsort(ed)]
    V = np.abs(Uu.conj().T @ Ud)
    q = Hu[blk[0], blk[1]].real*math.sin(fold(th[-1]))
    return dict(anchor=anchor, V=V, q=q, kappa=q/V[0, 2],
                meigs=np.sort(eu), off=off)

def main():
    w20 = json.load(open('results/wp20_valley_audit.json'))['records']
    # ---- G1: bulk u-class law
    ukap = []
    urecs = []
    for r in w20:
        mu, md = r['member']; s_, i, j = r['phase_edge']
        th = np.array(r['log_mags'] + [r['phi_raw']])
        d = sheet_data(mu, md, s_, (i, j), th)
        if d and d['anchor'] == 'u':
            ukap.append(d['kappa']); urecs.append(r)
    ukap = np.array(ukap)
    med = float(np.median(ukap))
    dev = np.abs(ukap - med)/med
    order = np.argsort(dev)
    bulk_max = float(dev[order[-2]])
    n_out = int((dev > 1e-6).sum())
    g1 = bulk_max < 1e-7 and n_out <= 1

    # ---- G2: perturbation drift (one sheet, no refit)
    r0 = [r for r in w20 if r['member'] == [417, 482]
          and r['phase_edge'] == ['d', 1, 2] and r['phi_folded_deg'] > 46.9][0]
    th0 = np.array(r0['log_mags'] + [r0['phi_raw']])
    rng = np.random.default_rng(42)
    drifts = []
    for _ in range(20):
        th2 = th0 + 0.01*rng.standard_normal(10)
        d = sheet_data(417, 482, 'd', (1, 2), th2)
        if d and d['anchor'] == 'u':
            drifts.append(abs(d['kappa']/med - 1))
    drift = float(np.median(drifts))
    g2 = drift > 1e-3

    # ---- G3/G5: refit against shifted Vub central
    idx = NAMES.index('Vub')
    a0 = sheet_data(417, 482, 'd', (1, 2), th0)
    k0, v0 = a0['kappa'], a0['V'][0, 2]
    slopes = []
    kap_move = 0.0
    for pct in [1e-5, 1e-4, 1e-3]:
        C2 = CENT.copy(); C2[idx] *= (1 + pct)
        def resid(th, C2=C2):
            Yu, Yd = wp7.build_texture(417, 482, 'd', (1, 2), th)
            with np.errstate(all='ignore'):
                obs = wp7.observables17(Yu, Yd)
            obs = np.where(np.isfinite(obs), obs, 1.0e6)
            return (obs - C2)/SIG
        s2 = least_squares(resid, th0, method='trf', xtol=1e-14,
                           ftol=1e-14, gtol=1e-14, max_nfev=200000)
        a = sheet_data(417, 482, 'd', (1, 2), s2.x)
        slopes.append((a['kappa']/k0 - 1)/pct)
        if abs(pct - 1e-3) < 1e-12:
            kap_move = abs(a['kappa']/k0 - 1)
    slopes = np.array(slopes)
    g3 = bool(np.ptp(slopes)/abs(slopes.mean()) < 0.01)
    g5 = kap_move > 100*bulk_max

    # ---- G4: same-physical-point pair
    recs = [r for r in w20 if r['member'] == [417, 482]
            and r['phase_edge'] == ['d', 1, 2]]
    pair = []
    for rr in recs:
        th = np.array(rr['log_mags'] + [rr['phi_raw']])
        d = sheet_data(417, 482, 'd', (1, 2), th)
        pair.append((rr, d))
    usheet = [p for p in pair if p[1]['anchor'] == 'u'][0]
    csheet = [p for p in pair if p[1]['anchor'] == 'c'][0]
    dV = float(np.abs(usheet[1]['V'] - csheet[1]['V']).max())
    dm = float(np.ptp(usheet[1]['meigs']/csheet[1]['meigs'])
               /np.mean(usheet[1]['meigs']/csheet[1]['meigs']))
    qratio = float(usheet[1]['q']/csheet[1]['q'])
    g4 = dV < 1e-6 and dm < 1e-5 and 11.0 < qratio < 11.3

    gates = {
        'G1_bulk_law': dict(value=dict(kappa=med, bulk_max_dev=bulk_max,
                                       n_outliers=n_out, n=len(ukap)),
                            passed=bool(g1)),
        'G2_not_algebraic': dict(value=dict(median_drift=drift,
                                            n_trials=len(drifts)),
                                 passed=bool(g2)),
        'G3_refit_linear': dict(value=dict(slopes=[float(s) for s in slopes]),
                                passed=bool(g3)),
        'G4_same_point_pair': dict(value=dict(dV_max=dV, dmass_rel=dm,
                                              q_ratio=qratio),
                                   passed=bool(g4)),
        'G5_physics_response': dict(value=dict(kappa_move=kap_move,
                                               bulk_max=bulk_max),
                                    passed=bool(g5)),
    }
    result = dict(
        purpose=__doc__.strip().split('\n')[0],
        kappa_u=med, bulk_max_dev=bulk_max, n_outliers=n_out,
        perturbation_drift=drift,
        refit_slopes=[float(s) for s in slopes],
        same_point_pair=dict(dV_max=dV, dmass_rel=dm, q_ratio=qratio,
                             kappa_u_sheet=float(usheet[1]['kappa']),
                             kappa_c_sheet=float(csheet[1]['kappa'])),
        gates=gates,
        gates_passed=sum(g['passed'] for g in gates.values()))
    with open('results/wp39_kappa_descent.json', 'w') as f:
        json.dump(result, f, indent=1)
    print(f"gates: {result['gates_passed']} / {len(gates)}")
    for name, g in gates.items():
        print(f"  {name}: passed={g['passed']}  value={g['value']}")

if __name__ == '__main__':
    main()
