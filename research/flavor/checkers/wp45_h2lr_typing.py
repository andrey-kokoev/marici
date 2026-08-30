"""WP45: the H2LR typing packet - capstone certificate for the flavor
lens-readout package.

Package under test (brief work package 6):
  carrier  F       = {(Y_u, Y_d)} / U(3)^3   (physical flavor quotient)
  lens     K       = sparse nine-link chart: 9 edge magnitudes + loop holonomy
  readout  O       = 17 weak-basis invariants (6 masses, 6 |V|, 3 angles, 2 ratios)
  pairing  (Y_u,Y_d) -> observables17, factorizing through the WP44 law

Each equivalence class of the brief is tested for what descends:
  G1 full U(3)^3 quotient: random (Q_L, Q_u, Q_d) leaves obs17 invariant;
  G2 chart groupoid (diagonal rephasings + row/col permutations): invariant;
  G3 fiber compatibility: all fitted sheets land on the same physical point
     (per-observable pull vs experimental sigma bounded);
  G4 CP conjugation: masses/|V| identical, angles reflected;
  G5 pairing factorization: the WP44 gap-cancelled law re-verified on the
     Hd_01=0 family (readout sees magnitude skeleton + weak-basis invariants);
  G6 lens coordinate vs readout: the loop phase phi (Yukawa-triangle angle)
     varies across charts of the same physical point while its CKM image
     gamma is fit-fixed; phi is lens data, gamma is readout (WP11 restated
     in typing language).

Reads: results/wp20_valley_audit.json, results/wp44_singlet_cancellation.json
Writes: results/wp45_h2lr_typing.json
Run: ./.venv/Scripts/python checkers/wp45_h2lr_typing.py
"""
import json, math, os, sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wp7_ensemble as wp7

MASSES2 = {'u': 7.04e-6**2, 'c': 3.56e-3**2, 't': 0.967**2}
ANG = slice(12, 15)

def fold(p):
    p = abs(p) % math.pi
    return math.pi - p if p > math.pi/2 else p

def angdiff(a, b):
    return abs((a - b + 180.0) % 360.0 - 180.0)

def ran_unitary(rng):
    z = rng.standard_normal((3, 3)) + 1j*rng.standard_normal((3, 3))
    q, r = np.linalg.qr(z)
    return q @ np.diag(np.sign(np.diag(r)))

def obs_diff(o1, o2):
    # per-coordinate RELATIVE comparison: ratios over the tiny light masses
    # (ys/yud etc.) make absolute error the wrong metric for invariance.
    idx = list(range(12)) + [15, 16]
    lin = max(abs(o1[k] - o2[k])/max(abs(o2[k]), 1e-300) for k in idx)
    ang = max(angdiff(o1[k], o2[k]) for k in range(12, 15))
    return float(lin), float(ang)

def sheet(r):
    mu, md = r['member']; s_, i, j = r['phase_edge']
    th = np.array(r['log_mags'] + [r['phi_raw']])
    Yu, Yd = wp7.build_texture(mu, md, s_, (i, j), th)
    return Yu, Yd, th

def main():
    w20 = json.load(open('results/wp20_valley_audit.json'))['records']
    rng = np.random.default_rng(20260824)

    # single pass: anchor, obs17, pulls, phi, and WP44-family data
    rows = []
    for r in w20:
        Yu, Yd, th = sheet(r)
        Hu = Yu @ Yu.conj().T
        off, k = min((max(abs(Hu[a, b]) for b in range(3) if b != a), a)
                     for a in range(3))
        blk = [x for x in range(3) if x != k]
        t = abs(0.5*math.atan2(2*Hu[blk[0], blk[1]].real,
                               Hu[blk[1], blk[1]].real - Hu[blk[0], blk[0]].real))
        t = min(t, math.pi/2 - t)
        if off > 1e-8 or t <= 1e-9:
            continue
        anchor = min(MASSES2, key=lambda m: abs(Hu[k, k].real/MASSES2[m]-1))
        obs = wp7.observables17(Yu, Yd)
        rows.append(dict(r=r, Yu=Yu, Yd=Yd, Hu=Hu, k=k, blk=blk,
                         anchor=anchor, obs=obs,
                         phi=float(r['phi_folded_deg'])))

    # G1 + G2 + G4 on a seeded sample.  Invariance gates need masses from a
    # direct SVD of Y: forming H = Y Y^dagger first (as observables17 does)
    # costs eps*||H||/lambda_min ~ 2e-6 relative on the lightest masses, which
    # is a float64 algorithm floor, not an invariance violation.  SVD of Y
    # directly gives eps*sigma_max/sigma_min ~ 1e-11.
    def obs_precise(Au, Ad):
        o = wp7.observables17(Au, Ad).copy()
        su = np.linalg.svd(Au, compute_uv=False)   # descending
        sd = np.linalg.svd(Ad, compute_uv=False)
        yu, yc, yt = su[::-1]; yd, ys, yb = sd[::-1]
        o[0:6] = [yu, yc, yt, yd, ys, yb]
        o[15] = yu / yd
        o[16] = ys / ((yu + yd) / 2.0)
        return o
    g1 = g2 = g4 = 0.0
    sample = rng.choice(len(rows), size=25, replace=False)
    for idx in sample:
        x = rows[int(idx)]
        Yu, Yd = x['Yu'], x['Yd']
        o0 = obs_precise(Yu, Yd)
        QL, Qu, Qd = (ran_unitary(rng) for _ in range(3))
        o1 = obs_precise(QL @ Yu @ Qu.conj().T, QL @ Yd @ Qd.conj().T)
        d = obs_diff(o0, o1); g1 = max(g1, d[0], d[1]*1e-2)  # angles deg-scaled
        D1 = np.diag(np.exp(1j*rng.uniform(0, 2*math.pi, 3)))
        D2 = np.diag(np.exp(1j*rng.uniform(0, 2*math.pi, 3)))
        D3 = np.diag(np.exp(1j*rng.uniform(0, 2*math.pi, 3)))
        P = np.eye(3)[list(rng.permutation(3))]
        o2 = obs_precise(P @ D1 @ Yu @ D2, P @ D1 @ Yd @ D3)
        d = obs_diff(o0, o2); g2 = max(g2, d[0], d[1]*1e-2)
        o3 = obs_precise(Yu.conj(), Yd.conj())
        idx = list(range(12)) + [15, 16]
        lin = max(abs(o3[k] - o0[k])/max(abs(o0[k]), 1e-300) for k in idx)
        ang = max(angdiff(o3[k], -o0[k]) for k in range(12, 15))
        g4 = max(g4, float(lin), float(ang)*1e-2)

    # G3 fiber compatibility: pull vs experimental sigma
    pull = 0.0
    for x in rows:
        p = abs(x['obs'] - wp7.CENTRAL)/wp7.SIGMA
        pull = max(pull, float(p[:12].max()), float(p[15:].max()),
                   float(max(angdiff(x['obs'][i], wp7.CENTRAL[i])
                             for i in range(12, 15))/wp7.SIGMA[12]))

    # G5 pairing factorization (WP44 law, recomputed on the family)
    g5 = 0.0
    n5 = 0
    for x in rows:
        k, blk = x['k'], x['blk']
        Hd0 = x['Yd'] @ x['Yd'].conj().T
        covered = False
        for blko in (blk, blk[::-1]):
            P = np.zeros((3, 3)); P[0, k] = 1; P[1, blko[0]] = 1; P[2, blko[1]] = 1
            HuC = P @ x['Hu'] @ P.T; Hd = P @ Hd0 @ P.T
            if abs(Hd[0, 1]) < 1e-10:
                covered = True
                break
        if not covered:
            continue
        s = HuC[0,0].real; c = HuC[1,2].real
        eu, Uu = np.linalg.eigh(HuC); ed, Ud = np.linalg.eigh(Hd)
        oe = np.argsort(eu); Uu = Uu[:, oe]; eu = eu[oe]
        od = np.argsort(ed); Ud = Ud[:, od]; ed = ed[od]
        yu2, yc2, yt2 = eu
        Du = (yt2-yc2)*(yt2-yu2)*(yc2-yu2)
        Dd = (ed[2]-ed[1])*(ed[2]-ed[0])*(ed[1]-ed[0])
        detC = np.linalg.det(HuC @ Hd - Hd @ HuC)
        J = abs(detC/(-2j*Du*Dd))
        sphi = math.sin(fold(x['r']['phi_raw']))
        q_obs = c*sphi
        M43 = J*Du*Dd/q_obs
        nonsing = sorted(eu, key=lambda v: abs(v-s))[1:]
        chiB = abs((s-nonsing[0])*(s-nonsing[1]))
        v02, w12 = abs(Hd[0,2]), abs(Hd[1,2])
        g5 = max(g5, abs(v02*v02*w12*chiB/M43 - 1))
        n5 += 1

    # G6 lens coordinate vs readout
    phis = np.array([x['phi'] for x in rows])
    gams = np.array([x['obs'][14] for x in rows])
    g6_ratio = float(phis.std()/gams.std())

    gates = {
        'G1_quotient_canonicity': dict(value=float(g1), passed=bool(g1 < 1e-8)),
        'G2_chart_groupoid': dict(value=float(g2), passed=bool(g2 < 1e-8)),
        'G3_fiber_compatibility_max_pull_sigma': dict(
            value=float(pull), passed=bool(pull < 5.0)),
        'G4_CP_conjugation': dict(value=float(g4), passed=bool(g4 < 1e-8)),
        'G5_pairing_factorization': dict(
            value=dict(n_family=n5, max_rel_err=float(g5)),
            passed=bool(n5 > 300 and g5 < 1e-9)),
        'G6_lens_vs_readout': dict(
            value=dict(phi_std_deg=float(phis.std()),
                       gamma_std_deg=float(gams.std()), ratio=g6_ratio),
            passed=bool(g6_ratio > 5.0)),
    }
    result = dict(
        purpose=__doc__.strip().split('\n')[0],
        package=dict(carrier='{(Y_u,Y_d)}/U(3)^3',
                     lens='9 edge magnitudes + loop holonomy (sparse chart)',
                     readout='observables17 (weak-basis invariants)',
                     pairing='WP44 gap-cancelled law'),
        gates=gates,
        gates_passed=sum(g['passed'] for g in gates.values()))
    with open('results/wp45_h2lr_typing.json', 'w') as f:
        json.dump(result, f, indent=1)
    print(f"gates: {result['gates_passed']} / {len(gates)}")
    for name, g in gates.items():
        print(f"  {name}: passed={g['passed']}  value={json.dumps(g['value'])[:200]}")

if __name__ == '__main__':
    main()
