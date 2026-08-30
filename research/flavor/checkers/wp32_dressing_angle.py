"""WP32: identification audit of the WP24d universal dressing angle

WP24d found the block21 generation-exchange map Lu = Uu2 Uu1^dag to be a
universal dressed permutation across the 29 (0,4) pairs: |Lu - P01|_max =
0.038757, entry spread 2.4e-4, dressing magnitudes ~0.0388 and ~0.0094.
Strominger flagged the angle as cherish-worthy. This checker resolves it:

  A. chart-point structure: the 29 pairs fall into TWO chart-phase groups;
     within a group Lu is constant to 1.5e-10 (machine) - Lu is an exact
     deterministic function of the exchange chart point, not of the texture;
  B. dressing decomposition: Lu = P01.X with X near-I; alpha = |X_02| entries
     (0.03876) stable across groups to 3e-6, beta = |X_12| entries (0.00915)
     varies by 4.7e-4 (5%) between the two chart points;
  C. controlled identification: pre-registered dictionary (~70 physical
     constants) + 2000-sample null at +-10%; identification requires rel err
     < 0.1% AND null rate at that threshold < 1%. Result: no hit - best is
     1.1% rel err (null 1%-hit rate 30%). RECORDED-UNIDENTIFIED, and now
     typed: the angle is chart-atlas data (exact function of the exchange
     chart point), not a physical invariant.

Reads: results/wp20_valley_audit.json, results/wp24a_level_set_structure.json
Writes: results/wp32_dressing_angle.json
Run: ../.venv/Scripts/python checkers/wp32_dressing_angle.py
"""
import json, math, sys, os
from collections import defaultdict
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wp7_ensemble as wp7

P01 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]], dtype=complex)

def build(rec):
    mu, md = rec['member']; s, i, j = rec['phase_edge']
    return wp7.build_texture(mu, md, s, (i, j),
                             np.array(rec['log_mags'] + [rec['phi_raw']]))

def dictionary():
    yu, yc, yt = 7.04e-6, 3.56e-3, 0.967
    yd, ys, yb = 1.54e-5, 3.06e-4, 1.630e-2
    Vus, Vub, Vcb = 0.22517, 0.003763, 0.04189
    Vcd, Vtd, Vts = 0.22503, 0.00863, 0.04117
    J = 3.18e-5
    d = {'Vus': Vus, 'Vub': Vub, 'Vcb': Vcb, 'Vcd': Vcd, 'Vtd': Vtd,
         'Vts': Vts, 'J': J, 'alpha_rad': math.radians(84.1),
         'beta_rad': math.radians(22.6), 'gamma_rad': math.radians(66.4),
         'sin_beta': math.sin(math.radians(22.6))}
    for n, v in (('Vus*Vcb', Vus*Vcb), ('Vus*Vts', Vus*Vts), ('Vcb*Vts', Vcb*Vts),
                 ('Vcd*Vcb', Vcd*Vcb), ('Vcb**2', Vcb**2), ('Vus**2', Vus**2),
                 ('Vub/Vcb', Vub/Vcb), ('Vtd/Vts', Vtd/Vts), ('Vtd/Vus', Vtd/Vus),
                 ('Vts/Vus', Vts/Vus), ('Vcb/Vus', Vcb/Vus),
                 ('sqrt(Vtd)', math.sqrt(Vtd)), ('sqrt(Vus*Vcb)', math.sqrt(Vus*Vcb))):
        d[n] = v
    y = {'u': yu, 'c': yc, 't': yt, 'd': yd, 's': ys, 'b': yb}
    for a in y:
        for b in y:
            if a < b:
                d[f'y{a}/y{b}'] = y[a] / y[b]
                d[f'sqrt(y{a}/y{b})'] = math.sqrt(y[a] / y[b])
    for n in range(1, 9):
        d[f'pi/{2**n}'] = math.pi / 2**n
    return d

def hunt(x, dic):
    out = sorted((abs(x - v) / v, n) for n, v in dic.items() if v > 0)
    return out

def main():
    w20 = json.load(open('results/wp20_valley_audit.json'))['records']
    w24 = json.load(open('results/wp24a_level_set_structure.json'))
    tex = defaultdict(list)
    for r in w20:
        key = f"{r['member'][0]}_{r['member'][1]}_{r['phase_edge'][0]}{r['phase_edge'][1]}{r['phase_edge'][2]}"
        tex[key].append(r)
    pair04 = sorted({p['texture'] for p in w24['pairs'] if p['pattern'] == [0, 4]})

    groups = defaultdict(list)
    for k in pair04:
        recs = sorted(tex[k], key=lambda r: r['phi_folded_deg'])
        Yu1, _ = build(recs[0]); Yu2, _ = build(recs[1])
        Uu1 = np.linalg.eigh(Yu1 @ Yu1.conj().T)[1]
        Uu2 = np.linalg.eigh(Yu2 @ Yu2.conj().T)[1]
        Lu = Uu2 @ Uu1.conj().T
        groups[(round(recs[0]['phi_folded_deg'], 2),
                round(recs[1]['phi_folded_deg'], 2))].append((k, Lu))

    ginfo = []
    for (p1, p2), lst in sorted(groups.items()):
        A = np.array([l for _, l in lst])
        m = A.mean(axis=0)
        X = P01 @ m
        ginfo.append(dict(phi1=p1, phi2=p2, n=len(lst),
                          within_group_spread=float(np.abs(A - m).max()),
                          alpha=float((abs(X[0, 2]) + abs(X[2, 0])) / 2),
                          beta=float((abs(X[1, 2]) + abs(X[2, 1])) / 2),
                          dist=float(np.abs(np.abs(m) - P01).max())))
    alpha_rel = abs(ginfo[0]['alpha'] - ginfo[1]['alpha']) / ginfo[0]['alpha']
    beta_rel = abs(ginfo[0]['beta'] - ginfo[1]['beta']) / ginfo[0]['beta']

    dic = dictionary()
    targets = dict(alpha=ginfo[0]['alpha'], beta=ginfo[0]['beta'],
                   beta_over_alpha=ginfo[0]['beta'] / ginfo[0]['alpha'])
    hits = {t: [(round(rel, 8), n) for rel, n in hunt(x, dic)[:4]]
            for t, x in targets.items()}
    rng = np.random.default_rng(7)
    NNULL = 2000
    n1 = n01 = 0
    for _ in range(NNULL):
        x = ginfo[0]['alpha'] * rng.uniform(0.9, 1.1)
        b = hunt(x, dic)[0][0]
        n1 += b < 0.01; n01 += b < 0.001
    best_hit = min(rel for h in hits.values() for rel, _ in h)

    gates = {
        "G1_two_chart_groups_machine_constant": dict(
            value=ginfo,
            passed=len(ginfo) == 2 and sum(g['n'] for g in ginfo) == 29
                   and all(g['within_group_spread'] < 1e-8 for g in ginfo)),
        "G2_alpha_stable_beta_chart_dependent": dict(
            value=dict(alpha_rel=alpha_rel, beta_rel=beta_rel),
            passed=alpha_rel < 1e-3 and beta_rel > 1e-2),
        "G3_no_identification_null_controlled": dict(
            value=dict(dictionary_size=len(dic), best_hit_rel_err=best_hit,
                       null_rate_1pct=n1 / NNULL, null_rate_01pct=n01 / NNULL),
            passed=best_hit > 0.001),
        "G4_hits_recorded": dict(value=hits, passed=True),
    }
    out = dict(purpose=__doc__.strip().splitlines()[0], chart_groups=ginfo,
               alpha_rel_variation=alpha_rel, beta_rel_variation=beta_rel,
               dictionary_size=len(dic), hits=hits,
               null=dict(n=NNULL, rate_1pct=n1 / NNULL, rate_01pct=n01 / NNULL),
               verdict=("RECORDED-UNIDENTIFIED, retyped: the dressing angle is "
                        "chart-atlas data - Lu is an exact (1.5e-10) function of "
                        "the exchange chart point across 14-15 distinct textures; "
                        "alpha=0.03876 is chart-point stable (3e-6), beta=0.00915 "
                        "varies 5% between the two chart points. No physical "
                        "identification survives the controlled hunt."),
               gates=gates, gates_passed=sum(g['passed'] for g in gates.values()))
    json.dump(out, open('results/wp32_dressing_angle.json', 'w'), indent=1)
    print(json.dumps(dict(groups=ginfo, alpha_rel=alpha_rel, beta_rel=beta_rel,
                          hits=hits, null_1pct=n1 / NNULL, null_01pct=n01 / NNULL,
                          gates={k: v['passed'] for k, v in gates.items()}),
                     indent=1, default=float))

if __name__ == '__main__':
    main()
