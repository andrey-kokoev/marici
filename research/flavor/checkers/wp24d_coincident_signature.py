"""WP24d addendum: signature census of the 135 coincident same-point block21
pairs, and identity probe for the dressed-permutation rotation angle.

Run: ../.venv/Scripts/python checkers/wp24d_coincident_signature.py
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

P01 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]], dtype=complex)
I3 = np.eye(3, dtype=complex)

def main():
    w20 = json.load(open('results/wp20_valley_audit.json'))['records']
    w21 = json.load(open('results/wp21e_universal_factorization.json'))['census']
    w24 = json.load(open('results/wp24a_level_set_structure.json'))
    tex = defaultdict(list)
    for r in w20:
        key = f"{r['member'][0]}_{r['member'][1]}_{r['phase_edge'][0]}{r['phase_edge'][1]}{r['phase_edge'][2]}"
        tex[key].append(r)
    pair04 = {p['texture'] for p in w24['pairs'] if p['pattern'] == [0, 4]}
    block21_multi = [k for k in tex
                     if w21[k]['factorization_type'] == 'block21' and len(tex[k]) >= 2]
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

    rows = []
    cls = Counter()
    for k, prs in sorted(same_point.items()):
        if k in pair04:
            continue
        recs = tex[k]
        i, j, d = prs[0]
        Yu1, Yd1 = build(recs[i]); Yu2, Yd2 = build(recs[j])
        Lu = frames(Yu2) @ frames(Yu1).conj().T
        dP = float(np.abs(np.abs(Lu) - P01).max())
        dI = float(np.abs(Lu - I3).max())
        um1 = tuple(sorted(round(float(x), 9) for x in np.abs(Yu1[Yu1 != 0])))
        um2 = tuple(sorted(round(float(x), 9) for x in np.abs(Yu2[Yu2 != 0])))
        dm1 = tuple(sorted(round(float(x), 9) for x in np.abs(Yd1[Yd1 != 0])))
        dm2 = tuple(sorted(round(float(x), 9) for x in np.abs(Yd2[Yd2 != 0])))
        lm = max(abs(a - b) for a, b in zip(recs[i]['log_mags'], recs[j]['log_mags']))
        umag_same = (um1 == um2); dmag_same = (dm1 == dm2)
        dphi = abs(recs[i]['phi_folded_deg'] - recs[j]['phi_folded_deg'])
        if umag_same and dmag_same:
            kind = 'near_duplicate' if lm < 1e-3 else 'same_mags_rotated'
        elif not umag_same:
            kind = 'exchange_like'
        else:
            kind = 'd_side_only'
        cls[kind] += 1
        rows.append(dict(texture=k, kind=kind, d16=d,
                         lu_dist_P01=dP, lu_dist_I=dI,
                         umag_same=umag_same, dmag_same=dmag_same,
                         logmag_maxdiff=lm, dphi_deg=dphi))

    # rotation-angle identity probe at the global best-fit point
    best = min(w20, key=lambda r: r['chi2_stored'])
    Yu, Yd = build(best)
    su2, Uu = np.linalg.eigh(Yu @ Yu.conj().T)
    sd2, Ud = np.linalg.eigh(Yd @ Yd.conj().T)
    yu, yc, yt = np.sqrt(su2); yd, ys, yb = np.sqrt(sd2)
    V = Uu.conj().T @ Ud
    target = 0.038757
    cands = {
        'Vcb': abs(V[1, 2]), 'Vts': abs(V[2, 1]), 'Vub': abs(V[0, 2]),
        'Vtd': abs(V[2, 0]), 'Vus*Vcb': abs(V[0, 1] * V[1, 2]),
        'yc/yt': yc / yt, 'sqrt(yc/yt)': math.sqrt(yc / yt),
        'ys/yb': ys / yb, 'Vus**2': abs(V[0, 1]) ** 2,
        'abs_V13/V23': abs(V[0, 2]) / abs(V[1, 2]),
        'abs_Vtd/Vts': abs(V[2, 0]) / abs(V[2, 2]),
        'yu/yc': yu / yc, 'sqrt(yu/yc)': math.sqrt(yu / yc),
        'sqrt(yu/yt)': math.sqrt(yu / yt),
    }
    ranked = sorted(((abs(v - target), nm, v) for nm, v in cands.items() if v),
                    key=lambda t: t[0])

    out = dict(
        purpose='WP24d addendum: coincident-pair signature census + rotation identity probe',
        classification_counts=dict(cls),
        rows=rows,
        best_fit_key=dict(member=best['member'], phase_edge=best['phase_edge'],
                          chi2=best['chi2_stored'], phi_deg=best['phi_folded_deg']),
        rotation_target=target,
        rotation_candidates_ranked=[dict(name=nm, value=v, absdiff=ad)
                                    for ad, nm, v in ranked[:8]],
        V_abs_bestfit=[[float(abs(V[a, b])) for b in range(3)] for a in range(3)],
        masses_bestfit=dict(yu=float(yu), yc=float(yc), yt=float(yt),
                            yd=float(yd), ys=float(ys), yb=float(yb)))
    json.dump(out, open('results/wp24d_coincident_signature.json', 'w'), indent=1)
    print('classification:', dict(cls))
    for kind in cls:
        ex = next(r for r in rows if r['kind'] == kind)
        print(f"  {kind}: e.g. {ex['texture']} d16={ex['d16']:.1e} dP01={ex['lu_dist_P01']:.4f} "
              f"dI={ex['lu_dist_I']:.4f} lm={ex['logmag_maxdiff']:.2e} dphi={ex['dphi_deg']:.3f}")
    print('rotation candidates (target 0.038757):')
    for ad, nm, v in ranked[:6]:
        print(f'  {nm:16s} {v:.6f}  |diff|={ad:.5f}')
    print('dphi by kind:')
    for kind in cls:
        ds = [r['dphi_deg'] for r in rows if r['kind'] == kind]
        print(f'  {kind}: n={len(ds)} max={max(ds):.3f}')

if __name__ == '__main__':
    main()
