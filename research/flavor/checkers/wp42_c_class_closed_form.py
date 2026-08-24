"""WP42: the c-anchor class is exact too - and an erratum to WP38/WP41.

WP38 reported the c-anchor class as "genuinely ~1% texture-fluctuating in
all ratios"; the WP41 ledger repeated this. Both were artifacts of testing
incomplete monomials. With the full monomial the c-class is exact:

  q_c = C_c * y_t^2 * |V_ub| * sin(gamma),   C_c = 1.000881(1)

constant across all 424 c-anchor sheets with total spread 1.3e-5 (181
sheets within 1e-9 of the median). The old q_c/Vub ratio scatters 7.6e-3
because y_t^2*sin(gamma) scatters that much across the fitted ensemble;
the monomial absorbs it.

Note: two interactive exploratory runs during this package produced a
spurious non-integer c-gradient (y_s^0.72 y_b^-0.72 ...). Root cause: a
Python loop variable shadowed the phase-edge index, corrupting refits.
Published checkers wp40/wp41 use literal/parameter indices and are
unaffected (verified by reading the code).

Gates:
  G1 ensemble: C_c = q_c/(y_t^2 |V_ub| sin gamma) constant over all
     c-sheets: max dev < 1.3e-5, >= 150 sheets within 1e-9;
  G2 gradient: refit-gradient of ln q_c on two distinct c-textures gives
     y_t +2, Vub +1, gamma +gamma*cot(gamma) (tol 2%), all others < 0.02;
  G3 erratum evidence: old denominator q_c/|V_ub| has bulk dev > 1e-3
     while the full monomial has < 1.3e-5;
  G4 same-point pair: q_u/q_c from the two monomials equals the direct
     charge ratio to < 1e-5;
  G5 C_c is a true constant: its refit-gradient is < 2e-3 everywhere.

Reads: results/wp20_valley_audit.json
Writes: results/wp42_c_class_closed_form.json
Run: ./.venv/Scripts/python checkers/wp42_c_class_closed_form.py
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

def analyze(mu, md, ps, pj, th):
    Yu, Yd = wp7.build_texture(mu, md, ps, pj, th)
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
    yt2 = max(eu); vub = abs(V[0, 2]); vcb = abs(V[1, 2])
    return dict(anchor=anchor, q=q, yt2=yt2, vub=vub, vcb=vcb, gamma=gam,
                Cc=q/(yt2*vub*math.sin(gam)))

def obs17(mu, md, ps, pj, th):
    Yu, Yd = wp7.build_texture(mu, md, ps, pj, th)
    with np.errstate(all='ignore'):
        return wp7.observables17(Yu, Yd)

def refit(mu, md, ps, pj, th0, C2):
    def resid(th):
        o = obs17(mu, md, ps, pj, th)
        o = np.where(np.isfinite(o), o, 1.0e6)
        return (o - C2)/SIG
    return least_squares(resid, th0, method='trf', xtol=1e-14,
                         ftol=1e-14, gtol=1e-14, max_nfev=200000).x

def gradient(mu, md, ps, pj, th0, val_fn):
    obs0 = obs17(mu, md, ps, pj, th0)
    v0 = val_fn(th0)
    eps = 1e-3
    R = np.zeros((17, 17)); rv = np.zeros(17)
    for k in range(17):
        C2 = CENT.copy(); C2[k] *= (1 + eps)
        th1 = refit(mu, md, ps, pj, th0, C2)
        o1 = obs17(mu, md, ps, pj, th1)
        R[:, k] = (o1/obs0 - 1)/eps
        rv[k] = (val_fn(th1)/v0 - 1)/eps
    R10 = R[PIDX, :]
    g10, _, rank, _ = np.linalg.lstsq(R10.T, rv, rcond=None)
    resid = float(np.linalg.norm(R10.T @ g10 - rv)/np.linalg.norm(rv))
    return {PHYS[k]: float(g10[k]) for k in range(10)}, resid

def main():
    w20 = json.load(open('results/wp20_valley_audit.json'))['records']
    sheets = []
    for r in w20:
        mu, md = r['member']; ps, pi, pj = r['phase_edge']
        th = np.array(r['log_mags'] + [r['phi_raw']])
        a = analyze(mu, md, ps, (pi, pj), th)
        if a:
            a.update(member=r['member'], pe=r['phase_edge'], th=th)
            sheets.append(a)

    csheets = [a for a in sheets if a['anchor'] == 'c']
    Cc = np.array([a['Cc'] for a in csheets])
    med = float(np.median(Cc))
    dev = np.abs(Cc - med)/med
    g1 = bool(dev.max() < 1.3e-5 and (dev < 1e-9).sum() >= 150)

    # G3 erratum evidence
    oldr = np.array([a['q']/a['vub'] for a in csheets])
    omed = float(np.median(oldr))
    odev = np.sort(np.abs(oldr - omed)/omed)
    g3 = bool(odev[-2] > 1e-3 and dev.max() < 1.3e-5)

    # G2 gradients on two distinct c-textures
    seen = []
    for a in csheets:
        key = (tuple(a['member']), tuple(a['pe']))
        if key not in [k for k, _ in seen]:
            seen.append((key, a))
    picks = [seen[0][1], seen[len(seen)//2][1]]
    grads = []
    ok = True
    for a in picks:
        mu, md = a['member']; ps, pi, pj = a['pe']
        pred = {'y_t': 2.0, 'Vub': 1.0,
                'gamma': a['gamma']/math.tan(a['gamma'])}
        qval = lambda th: abs(analyze(mu, md, ps, (pi, pj), th)['q'])
        g, res = gradient(mu, md, ps, (pi, pj), a['th'], qval)
        grads.append(dict(member=a['member'], gradient=g, resid=res,
                          predicted=pred))
        ok = ok and res < 1e-2 and all(
            abs(g[k]-v) < 0.02*max(1.0, abs(v)) for k, v in pred.items()) \
            and all(abs(g[k]) < 0.02 for k in PHYS if k not in pred)
    g2 = bool(ok)

    # G4 same-point pair consistency
    pair = [a for a in sheets if a['member'] == [417, 482]
            and a['pe'] == ['d', 1, 2]]
    ush = next(a for a in pair if a['anchor'] == 'u')
    csh = next(a for a in pair if a['anchor'] == 'c')
    Cu = 0.9993729706375574
    qr_direct = ush['q']/csh['q']
    qr_mono = (Cu*ush['yt2']*ush['vcb']*math.sin(ush['gamma'])) / \
              (csh['Cc']*csh['yt2']*csh['vub']*math.sin(csh['gamma']))
    g4 = bool(abs(qr_direct/qr_mono - 1) < 1e-5)

    # G5 C_c constancy under physical moves (on the first c-texture)
    a = picks[0]
    mu, md = a['member']; ps, pi, pj = a['pe']
    Cval = lambda th: analyze(mu, md, ps, (pi, pj), th)['Cc']
    gC, resC = gradient(mu, md, ps, (pi, pj), a['th'], Cval)
    g5 = bool(max(abs(v) for v in gC.values()) < 2e-3)

    gates = {
        'G1_c_ensemble': dict(value=dict(C_c=med, max_dev=float(dev.max()),
                                         n=int(len(Cc)),
                                         n_within_1e_9=int((dev < 1e-9).sum())),
                              passed=bool(g1)),
        'G2_c_gradient': dict(value=grads, passed=bool(g2)),
        'G3_erratum_evidence': dict(value=dict(old_q_over_Vub_bulk_dev=float(odev[-2]),
                                               new_monomial_max_dev=float(dev.max())),
                                    passed=bool(g3)),
        'G4_same_point_pair': dict(value=dict(q_u_over_q_c_direct=float(qr_direct),
                                              q_u_over_q_c_monomials=float(qr_mono)),
                                   passed=bool(g4)),
        'G5_C_c_constant': dict(value=dict(gradient_C_c=gC, resid=resC),
                                passed=bool(g5)),
    }
    result = dict(
        purpose=__doc__.strip().split('\n')[0],
        closed_form="q_c = C_c * y_t^2 * |V_ub| * sin(gamma)",
        C_c=med, max_dev=float(dev.max()),
        erratum=("WP38/WP41 'c-class fluctuates ~1%' superseded: artifact of "
                 "incomplete monomials; c-class is exact at 1.3e-5"),
        gates=gates,
        gates_passed=sum(g['passed'] for g in gates.values()))
    with open('results/wp42_c_class_closed_form.json', 'w') as f:
        json.dump(result, f, indent=1)
    print(f"gates: {result['gates_passed']} / {len(gates)}")
    for name, g in gates.items():
        print(f"  {name}: passed={g['passed']}  value={g['value']}")

if __name__ == '__main__':
    main()
