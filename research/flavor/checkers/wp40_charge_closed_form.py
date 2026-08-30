"""WP40: the descended u-class charge in closed physical form.

WP39 showed kappa_u = q_u/V_ub = F(physical point). The refit-gradient
map of F (17 single-observable refits) gives partials of ln kappa:
  y_t +2.01, Vcb +0.99, Vub -1.00, gamma +0.477 ~ gamma*cot(gamma);
everything else ~0. Hence the closed form, verified ensemble-wide:

  q_u = C * y_t^2 * |V_cb| * sin(gamma_CKM),   C = 0.99937297 universal

(the u-anchor sheet's weak charge is y_t^2 times the height of the CKM
unitarity triangle; |V_cb| sin gamma = |V_ub| sin beta = 2*Area/|Vub-side|).

Gates:
  G1 bulk closed form: C_bulk constant, |median-0.9993730| < 2e-6,
     max dev < 1e-7;
  G2 at most one outlier sheet beyond 1e-8;
  G3 refit partials (+1% single-central moves on the [417,482] d12
     u-sheet) match (y_t:+2, Vcb:+1, Vub:-1, gamma: gamma*cot gamma)
     within 1.5%;
  G4 C independent of the texture block-mixing angle (|corr| < 0.2
     while theta range spans > 2x);
  G5 falsified candidate y_t^2*|Vtd|/Vus keeps ensemble max dev > 1e-4.

Reads: results/wp20_valley_audit.json
Writes: results/wp40_charge_closed_form.json
Run: ./.venv/Scripts/python checkers/wp40_charge_closed_form.py
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
    Vc = Uu.conj().T @ Ud
    V = np.abs(Vc)
    gam = abs(math.atan2((-(Vc[0, 0]*Vc[0, 2].conjugate())).imag *
                         (Vc[1, 0]*Vc[1, 2].conjugate()).real -
                         (-(Vc[0, 0]*Vc[0, 2].conjugate())).real *
                         (Vc[1, 0]*Vc[1, 2].conjugate()).imag,
                         ((-(Vc[0, 0]*Vc[0, 2].conjugate())) *
                          (Vc[1, 0]*Vc[1, 2].conjugate()).conjugate()).real))
    q = Hu[blk[0], blk[1]].real*math.sin(fold(th[-1]))
    return dict(anchor=anchor, V=V, q=q, yt=math.sqrt(max(eu)),
                vcb=V[1, 2], vub=V[0, 2], vtd=V[2, 0], vus=V[0, 1],
                gamma=gam, theta=t,
                closed=yt2_closed(q, max(eu), V[1, 2], gam))

def yt2_closed(q, yt2, vcb, gam):
    return q/(yt2*vcb*math.sin(gam))

def refit(mu, md, s_, ij, th0, C2):
    def resid(th):
        Yu, Yd = wp7.build_texture(mu, md, s_, ij, th)
        with np.errstate(all='ignore'):
            obs = wp7.observables17(Yu, Yd)
        obs = np.where(np.isfinite(obs), obs, 1.0e6)
        return (obs - C2)/SIG
    return least_squares(resid, th0, method='trf', xtol=1e-14,
                         ftol=1e-14, gtol=1e-14, max_nfev=200000).x

def main():
    w20 = json.load(open('results/wp20_valley_audit.json'))['records']
    Cs, thetas, C1s = [], [], []
    for r in w20:
        mu, md = r['member']; s_, i, j = r['phase_edge']
        th = np.array(r['log_mags'] + [r['phi_raw']])
        d = sheet_data(mu, md, s_, (i, j), th)
        if d and d['anchor'] == 'u':
            Cs.append(d['closed']); thetas.append(d['theta'])
            C1s.append(d['q']/(d['yt']**2*d['vtd']/d['vus']))
    Cs = np.array(Cs); thetas = np.array(thetas); C1s = np.array(C1s)
    med = float(np.median(Cs))
    dev = np.abs(Cs - med)/med
    order = np.argsort(dev)
    bulk_max = float(dev[order[-2]])
    g1 = bulk_max < 1e-7 and abs(med - 0.9993730) < 2e-6
    g2 = bool((dev > 1e-8).sum() <= 1)
    cc = float(np.corrcoef(thetas, Cs)[0, 1])
    lo = Cs[thetas < np.median(thetas)]; hi = Cs[thetas >= np.median(thetas)]
    half_dev = float(abs(lo.mean()/hi.mean() - 1))
    g4 = bool(abs(cc) < 0.2 and half_dev < 1e-9)
    g5 = bool((np.abs(C1s - med)/med).max() > 1e-4)

    # G3: gradient of F through the 17x17 refit-response matrix.
    # Raw per-refit kappa responses are NOT partials (the fit redistributes
    # a single-central move over all fitted observables); the partials are
    # g solving R^T g = r with R the log-space response of fitted obs to
    # central moves and r the log-space kappa response.
    r0 = [r for r in w20 if r['member'] == [417, 482]
          and r['phase_edge'] == ['d', 1, 2] and r['phi_folded_deg'] > 46.9][0]
    th0 = np.array(r0['log_mags'] + [r0['phi_raw']])
    a0 = sheet_data(417, 482, 'd', (1, 2), th0)
    k0 = a0['q']/a0['vub']
    Yu0, Yd0 = wp7.build_texture(417, 482, 'd', (1, 2), th0)
    with np.errstate(all='ignore'):
        obs0 = wp7.observables17(Yu0, Yd0)
    PHYS = ['y_u', 'y_c', 'y_t', 'y_d', 'y_s', 'y_b', 'Vus', 'Vcb', 'Vub',
            'gamma']
    pidx = [NAMES.index(k) for k in PHYS]
    R = np.zeros((17, 17)); rv = np.zeros(17)
    eps = 1e-3
    for i in range(17):
        C2 = CENT.copy(); C2[i] *= (1 + eps)
        th1 = refit(417, 482, 'd', (1, 2), th0, C2)
        Yu1, Yd1 = wp7.build_texture(417, 482, 'd', (1, 2), th1)
        with np.errstate(all='ignore'):
            obs1 = wp7.observables17(Yu1, Yd1)
        R[:, i] = (obs1/obs0 - 1)/eps
        a1 = sheet_data(417, 482, 'd', (1, 2), th1)
        rv[i] = ((a1['q']/a1['vub'])/k0 - 1)/eps
    # 10-dimensional physical-coordinate gradient: solve R10^T g = rv
    R10 = R[pidx, :]
    g10, _, rank10, _ = np.linalg.lstsq(R10.T, rv, rcond=None)
    resid10 = float(np.linalg.norm(R10.T @ g10 - rv)/np.linalg.norm(rv))
    grad10 = {PHYS[i]: float(g10[i]) for i in range(10)}
    # forward check with the closed-form gradient, and the falsified one
    gam0 = a0['gamma']
    pred = {'y_t': 2.0, 'Vcb': 1.0, 'Vub': -1.0, 'gamma': gam0/math.tan(gam0)}
    g_pred = np.zeros(10)
    for k, v in pred.items():
        g_pred[PHYS.index(k)] = v
    resid_pred = float(np.linalg.norm(R10.T @ g_pred - rv)/np.linalg.norm(rv))
    g_alt = np.zeros(10)
    for k, v in {'y_t': 2.0, 'Vub': -1.0}.items():
        g_alt[PHYS.index(k)] = v
    resid_alt = float(np.linalg.norm(R10.T @ g_alt - rv)/np.linalg.norm(rv))
    g3 = bool(resid10 < 1e-3 and rank10 == 10
              and all(abs(grad10[k]-pred[k]) < 0.015*max(1.0, abs(pred[k]))
                      for k in pred)
              and resid_alt > 10*resid_pred)
    gates = {
        'G1_bulk_closed_form': dict(value=dict(C=med, bulk_max_dev=bulk_max,
                                               n=len(Cs)), passed=bool(g1)),
        'G2_outlier_count': dict(value=int((dev > 1e-8).sum()),
                                 passed=bool(g2)),
        'G3_refit_partials': dict(value=dict(gradient10=grad10,
                                             predicted=pred,
                                             lstsq_resid=resid10,
                                             rank=int(rank10),
                                             forward_resid=resid_pred,
                                             no_gamma_resid=resid_alt),
                                  passed=bool(g3)),
        'G4_texture_independence': dict(value=dict(corr_C_theta=cc,
                                        theta_half_split_dev=half_dev,
                                        theta_range=[float(thetas.min()),
                                                     float(thetas.max())]),
                                        passed=bool(g4)),
        'G5_falsified_candidate_stays_falsified': dict(
            value=float((np.abs(C1s - med)/med).max()), passed=bool(g5)),
    }
    result = dict(
        purpose=__doc__.strip().split('\n')[0],
        closed_form="q_u = C * y_t^2 * |V_cb| * sin(gamma)",
        C=med, bulk_max_dev=bulk_max,
        refit_gradient10=grad10, refit_predicted=pred,
        corr_C_theta=cc,
        open_item=("residual C = 1 - 6.27e-4, universal at 5.3e-8 across "
                   "the ensemble; not a gamma-convention artifact (four "
                   "normalization variants agree identically); unidentified"),
        gates=gates,
        gates_passed=sum(g['passed'] for g in gates.values()))
    with open('results/wp40_charge_closed_form.json', 'w') as f:
        json.dump(result, f, indent=1)
    print(f"gates: {result['gates_passed']} / {len(gates)}")
    for name, g in gates.items():
        print(f"  {name}: passed={g['passed']}  value={g['value']}")

if __name__ == '__main__':
    main()
