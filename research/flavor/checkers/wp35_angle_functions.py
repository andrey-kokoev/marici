"""WP35: the exact chart functions theta(phase) for u/t-singlet classes,
and what the c-singlet angle is data OF

WP34 found the block mixing angle th_mix exactly chart-phase determined
for u-singlet sheets (within-phase spread 3.9e-8) and t-singlet sheets
(1.1e-9), but NOT for c-singlet sheets (3.8e-3 cross-class). This package
extracts and types the chart functions:

  1. u-class splits into UNMIXED sheets (th = 0 exactly, fully diagonal
     Hu: 6 phase groups, 82 classes) and MIXED sheets (7 phase groups,
     232 classes). The mixed branch obeys the reciprocal law
         th_u(phi) = 0.038891/sin(phi) - 0.000126   (max resid 2.8e-6,
     all 7 mixed groups, cross-class); equivalently sin(th)*sin(phi) is
     constant at 0.0387566 +/- 5e-8 for the three high-phi groups. The
     WP33 'dressing class constant' 0.038769 was the sin(phi)~1 limit of
     this law, not a high-phase special value.
  2. t-class: th_t(phi) is exactly phase-determined (1.1e-9 cross-class)
     but no pre-registered closed form is exact (best: a/sin(phi)+b at
     max resid 2.9e-4); the 4-group table is recorded as the law.
  3. c-class: the angle is PER-CLASS phase data. Within one texture
     class th varies smoothly with phi (within-class raw spread 6.1e-5
     is fully accounted by slope ~ -1e-4/deg acting on the fit phi
     jitter of +-0.15 deg; linear-in-phi residuals <= 2e-5 = record
     noise), while across classes at FIXED phi theta varies by 3.8e-3.
     The c-angle therefore carries magnitude-valley information beyond
     the loop phase; the u/t-angles do not.

Pre-registered typing: 'phase law' (exact closed form in phi alone,
cross-class), 'empirical phase law' (phase-determined, no exact form),
'per-class phase law' (class-normalized), 'unmixed' (th=0 exactly).
No physical-invariant claim anywhere; all quantities are chart-atlas
data of the sparse texture presentation.

Reads: results/wp20_valley_audit.json
Writes: results/wp35_angle_functions.json
Run: ./.venv/Scripts/python checkers/wp35_angle_functions.py
"""
import json, math, sys, os
from collections import defaultdict
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wp7_ensemble as wp7

MASSES2 = {'u': 7.04e-6**2, 'c': 3.56e-3**2, 't': 0.967**2,
           'd': 1.54e-5**2, 's': 3.06e-4**2, 'b': 1.630e-2**2}

def sheet(rec):
    mu, md = rec['member']; s, i, j = rec['phase_edge']
    Yu, _ = wp7.build_texture(mu, md, s, (i, j),
                              np.array(rec['log_mags'] + [rec['phi_raw']]))
    Hu = Yu @ Yu.conj().T
    off, k = min((max(abs(Hu[k, j]) for j in range(3) if j != k), k)
                 for k in range(3))
    blk = [x for x in range(3) if x != k]
    th = abs(0.5 * math.atan2(2 * Hu[blk[0], blk[1]].real,
                              Hu[blk[1], blk[1]].real - Hu[blk[0], blk[0]].real))
    th_mix = min(th, math.pi / 2 - th)
    slot = float(Hu[k, k].real)
    anchor = min(MASSES2, key=lambda m: abs(slot / MASSES2[m] - 1))
    return dict(off=float(off), im=float(abs(Hu.imag).max()),
                theta_mix=th_mix, anchor=anchor)

FORMS = {
    'a*sin(phi)+b': lambda p: np.sin(p),
    'a*sin(phi/2)+b': lambda p: np.sin(p / 2),
    'a*cos(phi)+b': lambda p: np.cos(p),
    'a*tan(phi/2)+b': lambda p: np.tan(p / 2),
    'a*phi+b': lambda p: p,
    'a*sin(phi)cos(phi)+b': lambda p: np.sin(p) * np.cos(p),
    'a*tan(phi)+b': lambda p: np.tan(p),
    'a*sin(phi)**2+b': lambda p: np.sin(p)**2,
    'a/sin(phi)+b': lambda p: 1 / np.sin(p),
    'a*cot(phi)+b': lambda p: 1 / np.tan(p),
    'a/tan(phi/2)+b': lambda p: 1 / np.tan(p / 2),
    'a/sin(phi)**2+b': lambda p: 1 / np.sin(p)**2,
}

def hunt(phi_deg, th):
    p = np.radians(np.asarray(phi_deg)); t = np.asarray(th)
    out = {}
    for name, f in FORMS.items():
        x = f(p)
        A = np.polyfit(x, t, 1)
        resid = t - (A[0] * x + A[1])
        ss = 1 - (resid**2).sum() / max(((t - t.mean())**2).sum(), 1e-300)
        out[name] = dict(r2=float(ss), max_resid=float(abs(resid).max()),
                         a=float(A[0]), b=float(A[1]))
    return out

def main():
    w20 = json.load(open('results/wp20_valley_audit.json'))['records']
    rows = []
    for r in w20:
        key = (f"{r['member'][0]}_{r['member'][1]}_"
               f"{r['phase_edge'][0]}{r['phase_edge'][1]}{r['phase_edge'][2]}")
        st = sheet(r)
        if st['off'] < 1e-8 and st['im'] < 1e-9:
            rows.append(dict(texture=key, phi=r['phi_folded_deg'],
                             theta=st['theta_mix'], anchor=st['anchor']))

    tables, hunts, nulls = {}, {}, {}
    rng = np.random.default_rng(23)
    u_split = dict(unmixed=[], mixed=[])
    for anchor in ('u', 't'):
        cls = [r for r in rows if r['anchor'] == anchor]
        byphi = defaultdict(list)
        for r in cls:
            byphi[round(r['phi'], 2)].append(r)
        tab = []
        for p, lst in sorted(byphi.items()):
            ths = [r['theta'] for r in lst]
            tab.append(dict(phi=p, theta=float(np.mean(ths)),
                            spread=float(np.ptp(ths)), n=len(lst),
                            n_classes=len({r['texture'] for r in lst})))
        tables[anchor] = tab
        if anchor == 'u':
            mixed = [t for t in tab if t['theta'] > 1e-9]
            u_split['unmixed'] = [t for t in tab if t['theta'] <= 1e-9]
            u_split['mixed'] = mixed
            hunts['u_mixed'] = hunt([t['phi'] for t in mixed],
                                    [t['theta'] for t in mixed])
            # pure-product diagnostic: sin(th)*sin(phi) constancy
            prod = [t['theta'] * math.sin(math.radians(t['phi']))
                    for t in mixed]
            hi = [x for x, t in zip(prod, mixed) if t['phi'] > 60]
            u_split['product_sin_th_sin_phi'] = dict(
                per_group=[dict(phi=t['phi'], prod=float(x))
                           for x, t in zip(prod, mixed)],
                spread_all=float(np.ptp(prod)),
                spread_high_phi=float(np.ptp(hi)) if len(hi) > 1 else None,
                mean_high_phi=float(np.mean(hi)) if hi else None)
        hunts[anchor] = hunt([t['phi'] for t in tab],
                             [t['theta'] for t in tab])
        ref = hunts['u_mixed'] if anchor == 'u' else hunts[anchor]
        best = max(h['r2'] for h in ref.values())
        n = 0
        th_arr = np.array([t['theta'] for t in
                           (u_split['mixed'] if anchor == 'u' else tab)])
        ph_arr = [t['phi'] for t in
                  (u_split['mixed'] if anchor == 'u' else tab)]
        for _ in range(1000):
            perm = rng.permutation(th_arr)
            if max(h['r2'] for h in hunt(ph_arr, list(perm)).values()) >= best:
                n += 1
        nulls[anchor] = n / 1000

    # c-class data typing: per-class phase law
    c = [r for r in rows if r['anchor'] == 'c']
    byclass = defaultdict(list)
    for r in c:
        byclass[r['texture']].append((r['phi'], r['theta']))
    raw_within = max((float(np.ptp([x[1] for x in v]))
                      for v in byclass.values() if len(v) >= 2), default=0.0)
    lin_resid, slopes = 0.0, []
    for v in byclass.values():
        if len(v) < 3:
            continue
        ph = np.array([x[0] for x in v]); th = np.array([x[1] for x in v])
        A = np.polyfit(ph, th, 1)
        lin_resid = max(lin_resid, float(abs(th - (A[0]*ph + A[1])).max()))
        slopes.append(float(A[0]))
    byphi_c = defaultdict(list)
    for r in c:
        byphi_c[round(r['phi'], 2)].append(r)
    cross = [dict(phi=p, spread=float(np.ptp([r['theta'] for r in lst])),
                  n_classes=len({r['texture'] for r in lst}))
             for p, lst in sorted(byphi_c.items()) if len(lst) >= 2]
    c_typing = dict(n_sheets=len(c), n_classes=len(byclass),
                    within_class_raw_spread=raw_within,
                    within_class_linear_fit_max_resid=lin_resid,
                    within_class_slope_per_deg=dict(
                        min=min(slopes, default=None),
                        max=max(slopes, default=None)),
                    max_cross_class_spread_at_fixed_phi=max(
                        (x['spread'] for x in cross), default=None),
                    phi_groups=cross,
                    typing='per-class phase law: theta smooth in phi within '
                           'class (raw spread = slope x fit phi-jitter), '
                           'class-dependent normalization across classes')

    exact_forms = {a: [n for n, h in hunts[a].items() if h['max_resid'] < 1e-6]
                   for a in hunts}
    best_forms = {a: min(hunts[a].items(), key=lambda kv: kv[1]['max_resid'])
                  for a in hunts}
    gates = {
        "G1_u_exact_per_phase_cross_class": dict(
            value=dict(max_spread=max(t['spread'] for t in tables['u']),
                       n_groups=len(tables['u']),
                       n_unmixed_groups=len(u_split['unmixed']),
                       n_mixed_groups=len(u_split['mixed'])),
            passed=bool(max(t['spread'] for t in tables['u']) < 1e-6)),
        "G2_t_exact_per_phase_cross_class": dict(
            value=dict(max_spread=max(t['spread'] for t in tables['t']),
                       n_groups=len(tables['t'])),
            passed=bool(max(t['spread'] for t in tables['t']) < 1e-6)),
        "G3_u_mixed_reciprocal_law": dict(
            value=dict(best_form=best_forms['u_mixed'][0],
                       max_resid=best_forms['u_mixed'][1]['max_resid'],
                       a=best_forms['u_mixed'][1]['a'],
                       b=best_forms['u_mixed'][1]['b'],
                       product=u_split['product_sin_th_sin_phi'],
                       null_rate_ge_best=nulls['u']),
            passed=bool(best_forms['u_mixed'][0] == 'a/sin(phi)+b'
                        and best_forms['u_mixed'][1]['max_resid'] < 5e-6)),
        "G4_t_phase_determined_no_exact_form": dict(
            value=dict(best_form=best_forms['t'][0],
                       max_resid=best_forms['t'][1]['max_resid'],
                       null_rate_ge_best=nulls['t']),
            passed=bool(best_forms['t'][1]['max_resid'] > 1e-5)),
        "G5_c_per_class_phase_law": dict(
            value=c_typing,
            passed=bool(c_typing['within_class_linear_fit_max_resid'] < 3e-5
                        and (c_typing['max_cross_class_spread_at_fixed_phi']
                             or 0) > 1e-4)),
    }
    out = dict(purpose=__doc__.strip().splitlines()[0],
               angle_tables=tables, u_branch_split=u_split,
               closed_form_hunts=hunts, null_rate_ge_best=nulls,
               exact_forms=exact_forms, c_class_typing=c_typing,
               gates=gates,
               gates_passed=sum(bool(g['passed']) for g in gates.values()))
    json.dump(out, open('results/wp35_angle_functions.json', 'w'), indent=1)
    print("gates:", out['gates_passed'], "/", len(gates))
    for a in ('u', 't'):
        print(f"== {a}-class angle table:")
        for t in tables[a]:
            print(f"  phi={t['phi']:7.2f}  theta={t['theta']:.8f}  "
                  f"spread={t['spread']:.1e}  n={t['n']:3d}  classes={t['n_classes']}")
    bf = best_forms['u_mixed']
    print(f"u mixed best: {bf[0]} max_resid={bf[1]['max_resid']:.2e} "
          f"a={bf[1]['a']:.6f} b={bf[1]['b']:.6f} null={nulls['u']}")
    print("u product sin(th)*sin(phi):",
          u_split['product_sin_th_sin_phi']['spread_all'],
          "high-phi:", u_split['product_sin_th_sin_phi']['spread_high_phi'])
    bf = best_forms['t']
    print(f"t best: {bf[0]} max_resid={bf[1]['max_resid']:.2e} null={nulls['t']}")
    print("c typing: raw within", c_typing['within_class_raw_spread'],
          "lin-resid", c_typing['within_class_linear_fit_max_resid'],
          "cross", c_typing['max_cross_class_spread_at_fixed_phi'])

if __name__ == '__main__':
    main()
