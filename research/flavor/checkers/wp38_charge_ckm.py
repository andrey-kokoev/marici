"""WP38: charge-to-CKM identification - the exact law q_u = kappa_u * V_ub.

WP37 established the charge law q_anchor = H_12.sin(phi) per anchor class
(exact for u/t, ~1% approximate for c). This package asks whether the
charge constants are CKM-composite. Findings:

  - u-class: q_u = kappa_u * V_ub EXACTLY per sheet, kappa_u =
    9.678574167082195; 231/232 sheets within 1e-8 of the median, one
    outlier at 3.4e-6 (class 394_348_d02). This sharpens WP37's
    'class constant at 2.9e-5' into an exact per-sheet CKM
    proportionality. The residual does not correlate with chi2
    (fit noise excluded).
  - t-class: q_t constant at 1e-8; every CKM element is equally
    constant within the class, so CKM tracking is unresolvable.
  - c-class: ALL candidate ratios (const, Vub, Vcb, Vtd) scatter at
    ~1% - the c charge is genuinely approximate, no hidden exact law.
  - M (the WP36 magnitude factor in J.Du.Dd = c.sin(phi).M) is NOT an
    edge-magnitude monomial: log-log regression over 232 sheets gives
    all exponents ~0, consistent with M proportional to Du.Dd.
  - kappa_u is dimensionally yukawa^2 in scan units but equals 9.68 >
    y_t^2 = 0.935, so no pure-Yukawa monomial can express it; a
    bounded exponent search over Yukawa/CKM factors yields only
    multiple-comparison-grade hits (best: yt^-1.Vus^-1.5 at 8.4e-6,
    rejected as numerology). kappa_u's derivation stays OPEN.

Gates:
  G1 u-law exactness: bulk max dev < 1e-7 (allowing <= 1 outlier < 1e-5);
  G2 outlier chi2-independence: |corr(dev, chi2)| < 0.5;
  G3 t-class constancy: max dev of q_t < 1e-7;
  G4 c-class genuine approximation: >30% of sheets deviate >1e-4 for
     every candidate ratio;
  G5 M-not-monomial: all regression exponents < 0.05 in abs value.

Reads: results/wp20_valley_audit.json
Writes: results/wp38_charge_ckm.json
Run: ./.venv/Scripts/python checkers/wp38_charge_ckm.py
"""
import json, math, os, sys
from collections import Counter, defaultdict

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wp7_ensemble as wp7

MASSES2 = {'u': 7.04e-6**2, 'c': 3.56e-3**2, 't': 0.967**2}

def eig_D(H):
    s = np.linalg.eigvalsh(H)
    return (s[2]-s[1])*(s[2]-s[0])*(s[1]-s[0])

def ckm(Yu, Yd):
    Hu = Yu @ Yu.conj().T; Hd = Yd @ Yd.conj().T
    eu, Uu = np.linalg.eigh(Hu); ed, Ud = np.linalg.eigh(Hd)
    Uu = Uu[:, np.argsort(eu)]; Ud = Ud[:, np.argsort(ed)]
    return np.abs(Uu.conj().T @ Ud)

def main():
    w20 = json.load(open('results/wp20_valley_audit.json'))['records']
    rows = []
    for r in w20:
        mu, md = r['member']; s_, i, j = r['phase_edge']
        th = np.array(r['log_mags'] + [r['phi_raw']])
        Yu, Yd = wp7.build_texture(mu, md, s_, (i, j), th)
        Hu = Yu @ Yu.conj().T
        off, k = min((max(abs(Hu[a, b]) for b in range(3) if b != a), a)
                     for a in range(3))
        if off > 1e-8:
            continue
        blk = [x for x in range(3) if x != k]
        t = abs(0.5*math.atan2(2*Hu[blk[0], blk[1]].real,
                               Hu[blk[1], blk[1]].real - Hu[blk[0], blk[0]].real))
        t = min(t, math.pi/2 - t)
        if t <= 1e-9:
            continue
        anchor = min(MASSES2, key=lambda m: abs(Hu[k, k].real/MASSES2[m]-1))
        V = ckm(Yu, Yd)
        q = Hu[blk[0], blk[1]].real*math.sin(math.radians(r['phi_folded_deg']))
        Hd = Yd @ Yd.conj().T
        key = (f"{r['member'][0]}_{r['member'][1]}_"
               f"{r['phase_edge'][0]}{r['phase_edge'][1]}{r['phase_edge'][2]}")
        rows.append(dict(key=key, anchor=anchor, q=q, V=V,
                         Du=eig_D(Hu), Dd=eig_D(Hd), J=r['J'],
                         c=Hu[blk[0], blk[1]].real,
                         sp=math.sin(r['phi_raw']),
                         log_mags=r['log_mags'],
                         chi2=r['chi2_recomputed'],
                         phi=r['phi_folded_deg']))

    out = {}
    # ---- G1/G2: u-class exact CKM law
    u = [x for x in rows if x['anchor'] == 'u']
    kv = np.array([x['q']/x['V'][0, 2] for x in u])
    med = float(np.median(kv))
    dev = np.abs(kv - med)/med
    order = np.argsort(dev)
    bulk_max = float(dev[order[-2]]) if len(dev) > 1 else float(dev.max())
    n_out = int((dev > 1e-6).sum())
    outliers = [dict(key=u[i]['key'], dev=float(dev[i]), phi=u[i]['phi'])
                for i in np.where(dev > 1e-6)[0]]
    chi = np.array([x['chi2'] for x in u])
    corr_chi = float(np.corrcoef(dev, chi)[0, 1])
    kappa_u = med
    out['u_law'] = dict(kappa_u=kappa_u, n=len(u), bulk_max_dev=bulk_max,
                        n_outliers_gt_1e6=n_out, outliers=outliers,
                        corr_dev_chi2=corr_chi)
    g1 = bulk_max < 1e-7 and n_out <= 1
    g2 = abs(corr_chi) < 0.5

    # ---- G3: t-class constancy (tracking unresolvable)
    trows = [x for x in rows if x['anchor'] == 't']
    qt = np.array([x['q'] for x in trows])
    t_dev = float((np.abs(qt - np.median(qt))/np.median(qt)).max())
    vub_t = np.array([x['V'][0, 2] for x in trows])
    vub_t_dev = float((np.abs(vub_t - np.median(vub_t))/np.median(vub_t)).max())
    out['t_class'] = dict(q_median=float(np.median(qt)), q_max_dev=t_dev,
                          Vub_max_dev=vub_t_dev, n=len(trows))
    g3 = t_dev < 1e-7

    # ---- G4: c-class genuine approximation
    crows = [x for x in rows if x['anchor'] == 'c']
    c_stats = {}
    for name, idx in [('const', None), ('Vub', (0, 2)), ('Vcb', (1, 2)),
                      ('Vtd', (2, 0))]:
        vv = np.array([x['q']/(x['V'][idx] if idx else 1.0) for x in crows])
        dv = np.abs(vv - np.median(vv))/np.median(vv)
        c_stats[name] = dict(median=float(np.median(vv)),
                             frac_dev_gt_1e4=float((dv > 1e-4).mean()),
                             max_dev=float(dv.max()))
    out['c_class'] = c_stats
    g4 = all(s['frac_dev_gt_1e4'] > 0.3 for s in c_stats.values())

    # ---- G5: M not a monomial (u-class)
    X = np.array([np.array(x['log_mags']) for x in u])
    M = np.array([abs(x['J']*x['Du']*x['Dd']/(x['c']*x['sp'])) for x in u])
    logM = np.log(M)
    A = np.column_stack([X, np.ones(len(u))])
    coef, _, _, _ = np.linalg.lstsq(A, logM, rcond=None)
    resid = logM - A @ coef
    out['M_regression'] = dict(
        exponents=[float(c) for c in coef[:-1]],
        max_abs_exponent=float(np.abs(coef[:-1]).max()),
        resid_max=float(np.abs(resid).max()),
        resid_rms=float(np.sqrt((resid**2).mean())))
    g5 = out['M_regression']['max_abs_exponent'] < 0.05

    gates = {
        'G1_u_law_exact': dict(value=dict(kappa_u=kappa_u,
                                          bulk_max_dev=bulk_max,
                                          n_outliers=n_out),
                               passed=bool(g1)),
        'G2_chi2_independence': dict(value=dict(corr=corr_chi),
                                     passed=bool(g2)),
        'G3_t_const': dict(value=out['t_class'], passed=bool(g3)),
        'G4_c_approximate': dict(value=c_stats, passed=bool(g4)),
        'G5_M_not_monomial': dict(value=out['M_regression'],
                                  passed=bool(g5)),
    }
    result = dict(
        purpose=__doc__.strip().split('\n')[0],
        n_sheets=len(rows), u_law=out['u_law'], t_class=out['t_class'],
        c_class=out['c_class'], M_regression=out['M_regression'],
        gates=gates,
        gates_passed=sum(g['passed'] for g in gates.values()))
    with open('results/wp38_charge_ckm.json', 'w') as f:
        json.dump(result, f, indent=1)
    print(f"gates: {result['gates_passed']} / {len(gates)}")
    for name, g in gates.items():
        print(f"  {name}: passed={g['passed']}")
    print(f"  kappa_u = {kappa_u:.10f}  bulk_max_dev={bulk_max:.2e}  "
          f"outliers={n_out}")
    print(f"  t const max dev {t_dev:.2e}; c frac>1e-4 "
          f"{min(s['frac_dev_gt_1e4'] for s in c_stats.values()):.2f}")

if __name__ == '__main__':
    main()
