"""WP24d: block21 generation exchange (the (0,4) mechanism).

Generalizes WP24b to 4-edge u-sectors. For each same-physical-point block21
sheet pair:
  A. physical16 agreement.
  B. u-side: Hu2 = Lu Hu1 Lu^dag with Lu = Uu2 Uu1^dag (eigh-phase-free);
     structure of Lu (distance from P01; universality across the 29 (0,4)s).
  C. u-magnitude census: the eight values realizing the two sheets.
  D. d-side: |Hd2| = |Lu Hd1 Lu^dag| magnitude identity + D' phase solve +
     implied unitary W.
  E. coincident same-point block21 pairs (135): exchange signature census.

Run: ../.venv/Scripts/python checkers/wp24d_block21_exchange.py
"""
import json, math, sys
from collections import Counter, defaultdict

import numpy as np

sys.path.insert(0, 'checkers')
import wp7_ensemble as wp7
from wp18_branch_resolved_fibers import physical16

def build(rec):
    mu, md = rec['member']; s, i, j = rec['phase_edge']
    return wp7.build_texture(mu, md, s, (i, j),
                             np.array(rec['log_mags'] + [rec['phi_raw']]))

def frames(Y):
    return np.linalg.eigh(Y @ Y.conj().T)[1]

def main():
    w20 = json.load(open('results/wp20_valley_audit.json'))['records']
    w21 = json.load(open('results/wp21e_universal_factorization.json'))['census']
    w24 = json.load(open('results/wp24a_level_set_structure.json'))
    tex = defaultdict(list)
    for r in w20:
        key = f"{r['member'][0]}_{r['member'][1]}_{r['phase_edge'][0]}{r['phase_edge'][1]}{r['phase_edge'][2]}"
        tex[key].append(r)

    # same-point block21 pairs (from wp24c census logic, recomputed)
    pair04 = {p['texture'] for p in w24['pairs'] if p['pattern'] == [0, 4]}
    block21_multi = [k for k in tex
                     if w21[k]['factorization_type'] == 'block21' and len(tex[k]) >= 2]

    # find same-point pairs among block21 multi-minimum textures
    same_point = {}
    for k in block21_multi:
        recs = tex[k]
        p16 = [physical16(*build(r)) for r in recs]
        for i in range(len(recs)):
            for j in range(i + 1, len(recs)):
                d = max(abs(a - b) / max(abs(a), 1e-300)
                        for a, b in zip(p16[i], p16[j]))
                if d < 1e-7:
                    same_point.setdefault(k, []).append((i, j, d))
    rows04 = []
    Lu_set = []
    umag_set = Counter()
    for k in sorted(pair04):
        recs = sorted(tex[k], key=lambda r: r['phi_folded_deg'])
        r1, r2 = recs[0], recs[1]
        Yu1, Yd1 = build(r1); Yu2, Yd2 = build(r2)
        Hu1 = Yu1 @ Yu1.conj().T; Hu2 = Yu2 @ Yu2.conj().T
        Uu1, Uu2 = frames(Yu1), frames(Yu2)
        Lu = Uu2 @ Uu1.conj().T
        hu_def = float(np.abs(Hu2 - Lu @ Hu1 @ Lu.conj().T).max())
        Hd1 = Yd1 @ Yd1.conj().T; Hd2 = Yd2 @ Yd2.conj().T
        Hc = Lu @ Hd1 @ Lu.conj().T
        mag_def = float(np.abs(np.abs(Hd2) - np.abs(Hc)).max())
        # D' spanning-tree phase solve (as WP24b)
        rel = 1e-9 * max(1.0, float(np.abs(Hc).max()))
        d = np.ones(3, dtype=complex)
        fixed = {0}
        for _ in range(3):
            for (i, j) in ((0, 1), (0, 2), (1, 2)):
                if abs(Hc[i, j]) < rel:
                    continue
                rr = Hd2[i, j] / Hc[i, j]
                if i in fixed and j not in fixed:
                    d[j] = d[i] / rr; fixed.add(j)
                elif j in fixed and i not in fixed:
                    d[i] = rr * d[j]; fixed.add(i)
        d = d / np.abs(d)
        Dp = np.diag(d)
        dp_resid = float(np.abs(Hd2 - Dp @ Hc @ Dp.conj().T).max())
        W = np.linalg.solve(Dp @ Lu @ Yd1, Yd2)
        w_def = float(np.abs(W @ W.conj().T - np.eye(3)).max())
        # Lu structure: distance from P01
        P01 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]], dtype=complex)
        lu_p01 = float(np.abs(np.abs(Lu) - P01).max())
        d16 = max(abs(a - b) / max(abs(a), 1e-300)
                  for a, b in zip(physical16(Yu1, Yd1), physical16(Yu2, Yd2)))
        um1 = tuple(sorted(round(float(x), 6) for x in np.abs(Yu1[Yu1 != 0])))
        um2 = tuple(sorted(round(float(x), 6) for x in np.abs(Yu2[Yu2 != 0])))
        umag_set[(um1, um2)] += 1
        Lu_set.append(Lu)
        rows04.append(dict(texture=k, d16=d16, hu_defect=hu_def,
                           hd_mag_defect=mag_def, dprime_residual=dp_resid,
                           w_unitarity=w_def, lu_dist_from_P01=lu_p01,
                           phi1=r1['phi_folded_deg'], phi2=r2['phi_folded_deg']))

    # Lu universality: spread of Lu entries across the 29
    Lu_arr = np.array(Lu_set)
    lu_spread = float(np.abs(Lu_arr - Lu_arr.mean(axis=0)).max())

    # E. coincident same-point block21 pairs: phi jump census
    dphi_c = Counter()
    n_coinc = 0
    for k, prs in same_point.items():
        if k in pair04:
            continue
        n_coinc += 1
        recs = tex[k]
        for (i, j, d) in prs[:1]:
            dp = abs(recs[i]['phi_folded_deg'] - recs[j]['phi_folded_deg'])
            dphi_c[round(dp, 2)] += 1

    out = dict(
        purpose='WP24d block21 generation exchange certificates',
        n_04_pairs=len(rows04),
        A_physical16_max=max(r['d16'] for r in rows04),
        B_hu_conjugation_max=max(r['hu_defect'] for r in rows04),
        B_Lu_entry_spread_across_29=lu_spread,
        B_Lu_dist_from_P01_range=[min(r['lu_dist_from_P01'] for r in rows04),
                                  max(r['lu_dist_from_P01'] for r in rows04)],
        C_umag_value_sets={str(k): v for k, v in umag_set.items()},
        D_hd_mag_max=max(r['hd_mag_defect'] for r in rows04),
        D_dprime_resid_max=max(r['dprime_residual'] for r in rows04),
        D_w_unitarity_max=max(r['w_unitarity'] for r in rows04),
        E_same_point_block21_total=len(same_point),
        E_coincident_textures=n_coinc,
        E_coincident_dphi_census={str(k): v for k, v in dphi_c.items()},
        rows=rows04)
    with open('results/wp24d_block21_exchange.json', 'w') as f:
        json.dump(out, f, indent=1)
    print(json.dumps({k: v for k, v in out.items() if k != 'rows'}, indent=1))

if __name__ == '__main__':
    main()
