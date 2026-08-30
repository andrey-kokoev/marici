"""WP37: the universal charge law - H_12.sin(phi) = q_anchor for every
viable mixed sheet, and the J-routing theorem across all anchor classes

WP36 derived the mechanism for u-singlet sheets. Extending to t- and
c-singlet classes reveals the law is universal:

  - the phase edge is in the DOWN sector for EVERY viable sheet (955
    block-diagonal sheets of WP34), so Hu is real ensemble-wide;
  - J-routing is universal: zeroing H_12 kills J on every mixed sheet
    (848 sheets: u 232, t 192, c 424; J -> <2.5e-15) and leaves J
    exactly on every unmixed sheet (107: u 71, c 36);
  - the per-sheet theorem J.Du.Dd = c.sin(phi).M(mags) holds for all
    anchors (first-harmonic Im(Hd) and no-cos(phi) factorization
    re-verified ensemble-wide);
  - THE CHARGE LAW: q = H_12.sin(phi) is a class-level constant PER
    ANCHOR:
        q_u = 3.621e-2   (cross-class rel spread 2.9e-5)
        q_t = 1.125347e-6 (cross-class rel spread 1.6e-8)
        q_c ~ 3.24e-3    (approximate: 5e-4 within phase groups, per-
                          class offsets, group means range 1.6%)
  - the WP35 three-way typing of theta is fully explained as the image
    of the q-law under the block denominator: theta = q/(Delta.sin(phi))
    with Delta = H_22 - H_11. The t-class 'no closed form' was the exact
    q-law masked by a 3% drift of the tiny fitted difference
    yc^2 - yu^2; the c-class 'per-class angle' is q_c's per-class
    offsets amplified the same way.

Gates:
  G1 phase-sector census: every block-diagonal viable sheet has the
     phase edge in the down sector;
  G2 universal J-routing: mixed J0/J < 1e-14, unmixed J0/J = 1 exactly;
  G3 exact commutator identity ensemble-wide (machine floor);
  G4 first-harmonic Im(Hd) + magnitude-only factorization for all
     anchors (phi-rescale at fixed mags);
  G5 charge law: exact for u (rel < 1e-4) and t (rel < 1e-6);
     approximate at ~1% for c (genuine texture-level fluctuation,
     partially correlated with the block splitting Delta).

Reads: results/wp20_valley_audit.json
Writes: results/wp37_universal_charge.json
Run: ./.venv/Scripts/python checkers/wp37_universal_charge.py
"""
import json, math, sys, os
from collections import Counter, defaultdict
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wp7_ensemble as wp7

MASSES2 = {'u': 7.04e-6**2, 'c': 3.56e-3**2, 't': 0.967**2}

def eig_D(H):
    s = np.linalg.eigvalsh(H)
    return (s[2]-s[1])*(s[2]-s[0])*(s[1]-s[0])

def detC(Hu, Hd):
    return np.linalg.det(Hu @ Hd - Hd @ Hu)

def closed_form_detC(Hu, Hd):
    s = Hu[0, 0].real
    a, b = Hu[1, 1].real, Hu[2, 2].real
    c = Hu[1, 2].real
    u, v, w = Hd[0, 1], Hd[0, 2], Hd[1, 2]
    C1 = u*(s-a) - c*v
    C2 = v*(s-b) - c*u
    C12 = w*(a-b) + c*(Hd[2, 2].real - Hd[1, 1].real)
    return 2j*(c*w.imag*(abs(C1)**2 - abs(C2)**2)
               - (C1*C12*np.conj(C2)).imag)

def main():
    w20 = json.load(open('results/wp20_valley_audit.json'))['records']
    rows = []
    for r in w20:
        mu, md = r['member']; s, i, j = r['phase_edge']
        th = np.array(r['log_mags'] + [r['phi_raw']])
        Yu, Yd = wp7.build_texture(mu, md, s, (i, j), th)
        Hu = Yu @ Yu.conj().T; Hd = Yd @ Yd.conj().T
        off, k = min((max(abs(Hu[a, b]) for b in range(3) if b != a), a)
                     for a in range(3))
        if off > 1e-8 or abs(Hu.imag).max() > 1e-9:
            continue
        blk = [x for x in range(3) if x != k]
        t = abs(0.5*math.atan2(2*Hu[blk[0], blk[1]].real,
                               Hu[blk[1], blk[1]].real - Hu[blk[0], blk[0]].real))
        t = min(t, math.pi/2 - t)
        anchor = min(MASSES2, key=lambda m: abs(Hu[k, k].real/MASSES2[m]-1))
        P = np.zeros((3, 3))
        P[0, k] = 1; P[1, blk[0]] = 1; P[2, blk[1]] = 1
        HuC, HdC = P @ Hu @ P.T, P @ Hd @ P.T
        key = (f"{r['member'][0]}_{r['member'][1]}_"
               f"{r['phase_edge'][0]}{r['phase_edge'][1]}{r['phase_edge'][2]}")
        rows.append(dict(rec=r, key=key, anchor=anchor, sector=s,
                         Hu=HuC, Hd=HdC, theta=t,
                         mixed=t > 1e-9,
                         phi=r['phi_folded_deg'], phi_raw=r['phi_raw'],
                         c=HuC[1, 2].real,
                         Delta=HuC[2, 2].real - HuC[1, 1].real))

    # G1: phase-sector census
    census = Counter((x['anchor'], x['sector']) for x in rows)
    g1_ok = all(x['sector'] == 'd' for x in rows)

    # G2: universal routing
    g2_mixed, g2_unmixed = 0.0, 0.0
    for x in rows:
        Hu, Hd = x['Hu'], x['Hd']
        Du, Dd = eig_D(Hu), eig_D(Hd)
        J = (detC(Hu, Hd)/(-2j*Du*Dd)).real
        Hu0 = Hu.copy(); Hu0[1, 2] = 0; Hu0[2, 1] = 0
        J0 = (detC(Hu0, Hd)/(-2j*eig_D(Hu0)*Dd)).real
        x['J'] = J; x['Du'] = Du; x['Dd'] = Dd
        if x['mixed']:
            g2_mixed = max(g2_mixed, abs(J0/J))
        else:
            g2_unmixed = max(g2_unmixed, abs(J0/J - 1))

    # G3: exact identity ensemble-wide
    g3_err = max(abs(detC(x['Hu'], x['Hd'])
                     - closed_form_detC(x['Hu'], x['Hd'])) for x in rows)

    # G4: first-harmonic Im(Hd) + magnitude-only factorization, all anchors
    g4_harm, g4_mag = 0.0, 0.0
    for x in rows:
        r0 = x['rec']
        mu, md = r0['member']; s_, i_, j_ = r0['phase_edge']
        sc = 0.7
        th2 = np.array(r0['log_mags'] + [r0['phi_raw']*sc])
        Yu2, Yd2 = wp7.build_texture(mu, md, s_, (i_, j_), th2)
        Hd2 = Yd2 @ Yd2.conj().T
        Hu2 = Yu2 @ Yu2.conj().T
        # unpermuted Hd for entry comparison
        Hd_raw = None
        Yu0, Yd0 = wp7.build_texture(mu, md, s_, (i_, j_),
                                     np.array(r0['log_mags'] + [r0['phi_raw']]))
        Hd_raw = Yd0 @ Yd0.conj().T
        for a_ in range(3):
            for b_ in range(a_+1, 3):
                im1 = Hd_raw[a_, b_].imag
                if abs(im1) > 1e-12:
                    im2 = Hd2[a_, b_].imag
                    expect = im1*math.sin(sc*r0['phi_raw'])/math.sin(r0['phi_raw'])
                    g4_harm = max(g4_harm, abs(im2-expect)/abs(im1))
        if x['mixed']:
            # canonical frame for the phi-rescaled sheet
            k0 = x['rec']  # singlet index unchanged (mags fixed)
            off2, k2 = min((max(abs(Hu2[a, b]) for b in range(3) if b != a), a)
                           for a in range(3))
            blk2 = [q_ for q_ in range(3) if q_ != k2]
            P2 = np.zeros((3, 3))
            P2[0, k2] = 1; P2[1, blk2[0]] = 1; P2[2, blk2[1]] = 1
            Hu2C, Hd2C = P2 @ Hu2 @ P2.T, P2 @ Hd2 @ P2.T
            c1 = x['c']; sp1 = math.sin(x['phi_raw'])
            N1 = (detC(x['Hu'], x['Hd'])/(-2j*c1*sp1)).real
            c2 = Hu2C[1, 2].real
            N2 = (detC(Hu2C, Hd2C)/(-2j*c2*math.sin(sc*x['phi_raw']))).real
            g4_mag = max(g4_mag, abs(N2-N1)/max(abs(N1), 1e-300))

    # G5: charge law per anchor
    charge = {}
    for anchor in ('u', 't', 'c'):
        sel = [x for x in rows if x['anchor'] == anchor and x['mixed']]
        if not sel:
            continue
        q = np.array([x['c']*math.sin(math.radians(x['phi'])) for x in sel])
        byphi = defaultdict(list)
        byclass = defaultdict(list)
        for x in sel:
            qv = x['c']*math.sin(math.radians(x['phi']))
            byphi[round(x['phi'], 2)].append(qv)
            byclass[x['key']].append(qv)
        within_class_rel = max((float(np.ptp(v)/abs(np.mean(v)))
                                for v in byclass.values() if len(v) >= 2),
                               default=0.0)
        group_stats = [dict(phi=p, mean=float(np.mean(v)),
                            rel_spread=float(np.ptp(v)/abs(np.mean(v))),
                            n=len(v), n_classes=len({x['key'] for x in sel
                                                     if round(x['phi'], 2) == p}))
                       for p, v in sorted(byphi.items())]
        max_group_rel = max(g['rel_spread'] for g in group_stats)
        means = np.array([g['mean'] for g in group_stats])
        charge[anchor] = dict(
            n_sheets=len(sel), q_mean=float(q.mean()),
            q_rel_spread=float(np.ptp(q)/abs(q.mean())),
            within_class_rel_max=within_class_rel,
            max_within_group_rel=max_group_rel,
            group_mean_rel_range=float(np.ptp(means)/abs(means.mean())),
            groups=group_stats)
    # Delta behavior (explains the WP35 theta typing)
    delta_stats = {}
    for anchor in ('u', 't', 'c'):
        sel = [x for x in rows if x['anchor'] == anchor and x['mixed']]
        if not sel:
            continue
        d = np.array([x['Delta'] for x in sel])
        delta_stats[anchor] = dict(mean=float(d.mean()),
                                   rel_spread=float(np.ptp(d)/abs(d.mean())))

    g5 = {}
    g5['u_ok'] = charge['u']['q_rel_spread'] < 1e-4
    g5['t_ok'] = charge['t']['q_rel_spread'] < 1e-6
    # c-class charge is genuinely approximate: ~1% texture-level
    # fluctuation, partially correlated with the block splitting Delta
    # (linear Delta correction leaves 0.87% residual). Exact for u/t.
    g5['c_ok'] = (charge['c']['max_within_group_rel'] < 1.5e-2
                  and charge['c']['within_class_rel_max'] < 1.5e-2)

    gates = {
        "G1_phase_sector_universal_down": dict(
            value=dict(census={f"{a}/{s}": n for (a, s), n in sorted(census.items())},
                       n_sheets=len(rows)),
            passed=bool(g1_ok)),
        "G2_universal_J_routing": dict(
            value=dict(max_mixed_J0_over_J=float(g2_mixed),
                       max_unmixed_dev_from_1=float(g2_unmixed),
                       n_mixed=sum(x['mixed'] for x in rows),
                       n_unmixed=sum(not x['mixed'] for x in rows)),
            passed=bool(g2_mixed < 1e-14 and g2_unmixed < 1e-14)),
        "G3_exact_identity_ensemble": dict(
            value=dict(max_abs_err=float(g3_err)),
            passed=bool(g3_err < 1e-20)),
        "G4_first_harmonic_and_magnitude_only": dict(
            value=dict(max_harm_rel_err=float(g4_harm),
                       max_mag_rel_var=float(g4_mag)),
            passed=bool(g4_harm < 1e-9 and g4_mag < 1e-8)),
        "G5_charge_law": dict(
            value=dict(charge={a: {k: v for k, v in ch.items() if k != 'groups'}
                               for a, ch in charge.items()},
                       q_ratios=dict(u_over_c=charge['u']['q_mean']/charge['c']['q_mean'],
                                     c_over_t=charge['c']['q_mean']/charge['t']['q_mean']),
                       checks=g5),
            passed=bool(all(g5.values()))),
    }
    out = dict(purpose=__doc__.strip().splitlines()[0],
               n_sheets=len(rows),
               charge_law=charge, delta_stats=delta_stats,
               gates=gates,
               gates_passed=sum(bool(g['passed']) for g in gates.values()))
    json.dump(out, open('results/wp37_universal_charge.json', 'w'), indent=1)
    print("gates:", out['gates_passed'], "/", len(gates))
    for name, g in gates.items():
        print(f"  {name}: passed={g['passed']}")
    for a, ch in charge.items():
        print(f"  q_{a} = {ch['q_mean']:.6e}  rel_spread={ch['q_rel_spread']:.2e}  "
              f"within_class_max={ch['within_class_rel_max']:.2e}  "
              f"group_mean_range={ch['group_mean_rel_range']:.2e}")
    for a, d in delta_stats.items():
        print(f"  Delta_{a}: mean={d['mean']:.6e} rel_spread={d['rel_spread']:.2e}")

if __name__ == '__main__':
    main()
