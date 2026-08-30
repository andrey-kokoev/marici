"""WP41: the t-anchor closed form and the nature of the u-class constant C.

WP40 gave q_u = C*y_t^2*|V_cb|*sin(gamma), C = 0.9993729706 universal.
Two questions remain:
  A. What is the t-anchor analog? Ensemble data cannot say (all CKM
     elements are collinear at 1e-8 across t-sheets). The refit-gradient
     of ln q_t over the 10-dim physical coordinate space identifies the
     CKM factor directly.
  B. Is C a function of the physical point? Refit-gradient of ln C:
     if every partial is ~0, C is a true constant of the construction,
     not a physical function in disguise.

Gates:
  G1 t-gradient: 10-dim refit-gradient of ln q_t on the reference
     t-sheet solves with resid < 1e-3, rank 10, and matches ONE candidate
     monomial gradient within 1.5% while the nearest rival fails at >10x
     residual;
  G2 t-ensemble: the identified form is constant over all t-sheets with
     bulk max dev < 1e-7;
  G3 C-constancy: 10-dim refit-gradient of ln C on the reference u-sheet
     has every partial < 2e-3;
  G4 u-form regression: q_u/(y_t^2 Vcb sin gamma) bulk max dev < 1e-7.

Reads: results/wp20_valley_audit.json
Writes: results/wp41_t_class_and_C_constant.json
Run: ./.venv/Scripts/python checkers/wp41_t_class_and_C_constant.py
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
PHYS = ['y_u', 'y_c', 'y_t', 'y_d', 'y_s', 'y_b', 'Vus', 'Vcb', 'Vub', 'gamma']
PIDX = [NAMES.index(k) for k in PHYS]

def fold(p):
    p = abs(p) % math.pi
    return math.pi - p if p > math.pi/2 else p

def analyze(mu, md, s_, ij, th):
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
    V = Uu.conj().T @ Ud
    z = -(V[0, 0]*V[0, 2].conjugate())/(V[1, 0]*V[1, 2].conjugate())
    gam = abs(math.atan2(z.imag, z.real))
    q = Hu[blk[0], blk[1]].real*math.sin(fold(th[-1]))
    return dict(anchor=anchor, q=q, yt2=max(eu), ec2=float(eu[1]),
                vcb=abs(V[1, 2]), vub=abs(V[0, 2]), vus=abs(V[0, 1]),
                gamma=gam, Cu=q/(max(eu)*abs(V[1, 2])*math.sin(gam)))

def obs17(mu, md, s_, ij, th):
    Yu, Yd = wp7.build_texture(mu, md, s_, ij, th)
    with np.errstate(all='ignore'):
        o = wp7.observables17(Yu, Yd)
    return o

def refit(mu, md, s_, ij, th0, C2):
    def resid(th):
        o = obs17(mu, md, s_, ij, th)
        o = np.where(np.isfinite(o), o, 1.0e6)
        return (o - C2)/SIG
    return least_squares(resid, th0, method='trf', xtol=1e-14,
                         ftol=1e-14, gtol=1e-14, max_nfev=200000).x

def gradient(mu, md, s_, ij, th0, val_fn, obs0):
    """10-dim physical gradient of ln val_fn by the 17-refit response."""
    R = np.zeros((17, 17)); rv = np.zeros(17)
    v0 = val_fn(th0)
    eps = 1e-3
    for i in range(17):
        C2 = CENT.copy(); C2[i] *= (1 + eps)
        th1 = refit(mu, md, s_, ij, th0, C2)
        o1 = obs17(mu, md, s_, ij, th1)
        R[:, i] = (o1/obs0 - 1)/eps
        rv[i] = (val_fn(th1)/v0 - 1)/eps
    R10 = R[PIDX, :]
    g10, _, rank10, _ = np.linalg.lstsq(R10.T, rv, rcond=None)
    resid = float(np.linalg.norm(R10.T @ g10 - rv)/np.linalg.norm(rv))
    return {PHYS[i]: float(g10[i]) for i in range(10)}, resid, int(rank10), R10, rv

def main():
    w20 = json.load(open('results/wp20_valley_audit.json'))['records']
    sheets = []
    for r in w20:
        mu, md = r['member']; s_, i, j = r['phase_edge']
        th = np.array(r['log_mags'] + [r['phi_raw']])
        a = analyze(mu, md, s_, (i, j), th)
        if a:
            a.update(member=r['member'], phase_edge=r['phase_edge'], th=th)
            sheets.append(a)

    # ---- G4: u-form regression
    uC = np.array([a['Cu'] for a in sheets if a['anchor'] == 'u'])
    medC = float(np.median(uC))
    devC = np.sort(np.abs(uC - medC)/medC)
    g4 = bool(devC[-2] < 1e-7)

    # ---- Part A: t-class gradient on a reference t-sheet
    tref = next(a for a in sheets if a['anchor'] == 't')
    mu, md = tref['member']; s_, i, j = tref['phase_edge']
    obs0 = obs17(mu, md, s_, (i, j), tref['th'])
    qval = lambda th: abs(analyze(mu, md, s_, (i, j), th)['q'])
    gt, rest, rankt, R10, rv = gradient(mu, md, s_, (i, j), tref['th'],
                                        qval, obs0)
    # candidate monomial gradients (in PHYS coordinates)
    gc = gt['gamma']/1.0
    cot_term = None
    gam0 = math.radians(obs0[NAMES.index('gamma')])
    cands = {
        'yc2*Vub/Vcb':      {'y_c': 2.0, 'Vub': 1.0, 'Vcb': -1.0},
        'yc2*Vub/Vcb*sinG': {'y_c': 2.0, 'Vub': 1.0, 'Vcb': -1.0,
                             'gamma': gam0/math.tan(gam0)},
        'yc2*Vus*Vcb':      {'y_c': 2.0, 'Vus': 1.0, 'Vcb': 1.0},
        'yc2*Vub':          {'y_c': 2.0, 'Vub': 1.0},
        'yt2*Vub/Vcb':      {'y_t': 2.0, 'Vub': 1.0, 'Vcb': -1.0},
        'yc2/Vcb':          {'y_c': 2.0, 'Vcb': -1.0},
        'yc2*Vus*Vub':      {'y_c': 2.0, 'Vus': 1.0, 'Vub': 1.0},
    }
    cand_resid = {}
    for name, gg in cands.items():
        gv = np.zeros(10)
        for k, v in gg.items():
            gv[PHYS.index(k)] = v
        cand_resid[name] = float(np.linalg.norm(R10.T @ gv - rv)
                                 /np.linalg.norm(rv))
    best = min(cand_resid, key=cand_resid.get)
    rivals = sorted(v for k, v in cand_resid.items() if k != best)
    tol_match = all(abs(gt[k]-v) < 0.015*max(1.0, abs(v))
                    for k, v in cands[best].items())
    g1 = bool(rest < 1e-3 and rankt == 10 and cand_resid[best] < 0.01
              and tol_match and rivals[0] > 10*cand_resid[best])

    # ---- G2: t-ensemble constancy of the identified form
    def tval(a, form):
        if form == 'yc2*Vub/Vcb':      return a['q']/(a['ec2']*a['vub']/a['vcb'])
        if form == 'yc2*Vub/Vcb*sinG': return a['q']/(a['ec2']*a['vub']/a['vcb']
                                                     *math.sin(a['gamma']))
        if form == 'yc2*Vus*Vcb':      return a['q']/(a['ec2']*a['vus']*a['vcb'])
        if form == 'yc2*Vub':          return a['q']/(a['ec2']*a['vub'])
        if form == 'yt2*Vub/Vcb':      return a['q']/(a['yt2']*a['vub']/a['vcb'])
        if form == 'yc2/Vcb':          return a['q']/(a['ec2']/a['vcb'])
        return a['q']/(a['ec2']*a['vus']*a['vub'])
    tvals = [tval(a, best) for a in sheets if a['anchor'] == 't']
    tvals = np.array(tvals, dtype=float)
    tmed = float(np.median(tvals))
    tdev = np.sort(np.abs(tvals - tmed)/abs(tmed))
    g2 = bool(tdev[-2] < 1e-7 if len(tdev) > 1 else tdev[-1] < 1e-7)

    # ---- Part B: is C a physical function? gradient of ln C_u
    uref = next(a for a in sheets if a['anchor'] == 'u'
                and a['member'] == [417, 482])
    mu, md = uref['member']; s_, i, j = uref['phase_edge']
    obs0u = obs17(mu, md, s_, (i, j), uref['th'])
    Cval = lambda th: analyze(mu, md, s_, (i, j), th)['Cu']
    gC, resC, rankC, _, _ = gradient(mu, md, s_, (i, j), uref['th'],
                                     Cval, obs0u)
    g3 = bool(max(abs(v) for v in gC.values()) < 2e-3)

    gates = {
        'G1_t_gradient': dict(value=dict(gradient=gt, resid=rest,
                                         rank=rankt, best=best,
                                         cand_resid=cand_resid),
                              passed=bool(g1)),
        'G2_t_ensemble': dict(value=dict(form=best, norm=tmed,
                                         bulk_max_dev=float(tdev[-2]),
                                         n=len(tvals)),
                              passed=bool(g2)),
        'G3_C_is_constant': dict(value=dict(gradient_C=gC, resid=resC),
                                 passed=bool(g3)),
        'G4_u_form_regression': dict(value=dict(C=medC,
                                                bulk_max_dev=float(devC[-2])),
                                     passed=bool(g4)),
    }
    result = dict(
        purpose=__doc__.strip().split('\n')[0],
        t_reference=dict(member=tref['member'], phase_edge=tref['phase_edge']),
        t_gradient=gt, t_best_form=best, t_candidate_residuals=cand_resid,
        t_norm=tmed, t_bulk_max_dev=float(tdev[-2]),
        C_gradient=gC, C_gradient_resid=resC,
        gates=gates,
        gates_passed=sum(g['passed'] for g in gates.values()))
    with open('results/wp41_t_class_and_C_constant.json', 'w') as f:
        json.dump(result, f, indent=1)
    print(f"gates: {result['gates_passed']} / {len(gates)}")
    for name, g in gates.items():
        print(f"  {name}: passed={g['passed']}  value={g['value']}")

if __name__ == '__main__':
    main()
