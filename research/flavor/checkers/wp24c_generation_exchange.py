"""WP24c: generation-exchange deck involution on the readout covering.

Tests, for the full WP15b viable ensemble (WP20 audit records):

1. Every same-texture minimum pair with physical16 agreement (<1e-7 rel)
   is a generation-exchange (sheet) pair; census by class.
2. Diagonal class: the fiber over the best-fit point is 2-fold for every
   texture -- for the 38 single-minimum textures the partner sheet is
   recovered by refit (u-swapped start), certified by chi2 and physical16.
3. Sheet phase census: folded phi of both sheets per diagonal texture and
   cluster assignment against the WP21d2/WP24a centers.

Run:  ../.venv/Scripts/python checkers/wp24c_generation_exchange.py
"""
import json, math, sys
from collections import defaultdict

import numpy as np
from scipy.optimize import least_squares

sys.path.insert(0, 'checkers')
import wp7_ensemble as wp7
from wp18_branch_resolved_fibers import physical16

CENTERS = [23.15067360649863, 43.1729, 46.9071, 68.3880, 89.5723]
CENTERS = json.load(open('results/wp24a_level_set_structure.json'))['cluster_centers_deg']

def cluster_of(phi_deg, tol=3.0):
    d = [abs(phi_deg - c) for c in CENTERS]
    k = int(np.argmin(d))
    return k if d[k] < tol else None

def build(rec):
    mu, md = rec['member']; s, i, j = rec['phase_edge']
    return wp7.build_texture(mu, md, s, (i, j),
                             np.array(rec['log_mags'] + [rec['phi_raw']]))

def p16(rec):
    return physical16(*build(rec))

def rel16(a, b):
    return max(abs(x - y) / max(abs(x), 1e-300) for x, y in zip(a, b))

def main():
    w20 = json.load(open('results/wp20_valley_audit.json'))['records']
    w21 = json.load(open('results/wp21e_universal_factorization.json'))['census']
    w24 = json.load(open('results/wp24a_level_set_structure.json'))

    tex = defaultdict(list)
    for r in w20:
        key = f"{r['member'][0]}_{r['member'][1]}_{r['phase_edge'][0]}{r['phase_edge'][1]}{r['phase_edge'][2]}"
        tex[key].append(r)

    # ---- 1. same-point pair census across all multi-minimum textures ----
    pair_census = defaultdict(lambda: dict(multi=0, same_point=0, distinct=0,
                                           max_rel16_same=0.0))
    for key, recs in tex.items():
        if len(recs) < 2:
            continue
        cls = w21[key]['factorization_type']
        pair_census[cls]['multi'] += 1
        p16s = [p16(r) for r in recs]
        same = False
        for i in range(len(recs)):
            for j in range(i + 1, len(recs)):
                d = rel16(p16s[i], p16s[j])
                if d < 1e-7:
                    same = True
                    pair_census[cls]['max_rel16_same'] = max(
                        pair_census[cls]['max_rel16_same'], d)
        pair_census[cls]['same_point' if same else 'distinct'] += 1

    # ---- 2. diagonal-class sheet census with partner recovery ----
    diag = sorted(k for k in tex if w21[k]['factorization_type'] == 'diagonal')
    sheets = {}
    n_recovered = 0
    max_refit_rel16 = 0.0
    for key in diag:
        recs = tex[key]
        entry = dict(n_stored=len(recs),
                     stored_phi=sorted(round(r['phi_folded_deg'], 6) for r in recs),
                     stored_chi2=[r['chi2_stored'] for r in recs])
        if len(recs) == 1:
            r = recs[0]
            mu, md = r['member']; s, i, j = r['phase_edge']
            lm = np.array(r['log_mags'])
            lm_sw = lm.copy(); lm_sw[0], lm_sw[1] = lm[1], lm[0]

            def resid(th):
                Yu, Yd = wp7.build_texture(mu, md, s, (i, j), th)
                o = wp7.observables17(Yu, Yd)
                o = np.where(np.isfinite(o), o, 1.0e6)
                return (o - wp7.CENTRAL) / wp7.SIGMA

            rng = np.random.default_rng(7)
            best = None
            for t in range(6):
                s0 = (np.concatenate([lm_sw, [r['phi_raw']]]) if t == 0 else
                      np.concatenate([lm_sw + rng.normal(0, 0.5, 9),
                                      [r['phi_raw'] + rng.normal(0, 0.2)]]))
                sol = least_squares(resid, s0, method='lm', ftol=1e-13,
                                    xtol=1e-13, gtol=1e-13, max_nfev=1200)
                chi2 = float(2 * sol.cost)
                if chi2 < 4.0:
                    dist = np.linalg.norm(sol.x[:9] - lm)
                    if dist > 1.0 and (best is None or chi2 < best[0]):
                        best = (chi2, dist, sol.x)
            if best is not None:
                chi2, dist, x = best
                phi_fold = math.degrees(wp7.fold_phi(float(x[-1])))
                Yu, Yd = wp7.build_texture(mu, md, s, (i, j), x)
                d16 = rel16(p16(r), physical16(Yu, Yd))
                max_refit_rel16 = max(max_refit_rel16, d16)
                entry['recovered_partner'] = dict(
                    chi2=chi2, lm_dist=dist, phi_folded_deg=phi_fold,
                    physical16_rel_diff=d16,
                    same_physical_point=bool(d16 < 1e-7))
                n_recovered += 1
        sheets[key] = entry

    # cluster span per diagonal texture (stored + recovered)
    span = defaultdict(int)
    for key, e in sheets.items():
        phis = list(e['stored_phi'])
        if 'recovered_partner' in e:
            phis.append(e['recovered_partner']['phi_folded_deg'])
        cls_set = {cluster_of(p) for p in phis}
        cls_set.discard(None)
        span[tuple(sorted(cls_set))] += 1

    out = dict(
        purpose='WP24c generation-exchange deck involution on the readout covering',
        magic_log_ratio=dict(value=6.218726,
                             identified_as='ln(yc/yu) at the best-fit point',
                             check=math.log(3.5600000000e-03 / 7.0907399438e-06)),
        same_point_pair_census={k: v for k, v in pair_census.items()},
        diagonal_class=dict(
            n_textures=len(diag),
            n_stored_two_minima=sum(1 for e in sheets.values() if e['n_stored'] == 2),
            n_partner_recovered=n_recovered,
            max_refit_physical16_rel_diff=max_refit_rel16,
            cluster_span_census={str(k): v for k, v in span.items()}),
        sheets=sheets,
    )
    with open('results/wp24c_generation_exchange.json', 'w') as f:
        json.dump(out, f, indent=1)
    print(json.dumps({k: v for k, v in out.items() if k != 'sheets'}, indent=1))

if __name__ == '__main__':
    main()
