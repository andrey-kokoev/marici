"""WP50: chart-complete down-sector inversion - the loop term is explicit.

WP49 inverted the down sector rationally on the WP44 family (Hd_01 = 0).
WP50 closes the complement. The 848 block-diagonal sheets split into THREE
strata by down-sector zero pattern in the canonical (singlet-first) frame:

  S1 chain-star    Hd_01 = 0 (394 sheets): WP49 linear inversion.
  S2 singlet-star  Hd_12 = 0 (282 sheets): loop EXACTLY dead (the loop
                   product contains Hd_12); linear inversion with x != 0.
  S3 triangle      all entries nonzero (172 sheets): loop alive; d1 solves
                   an explicit quadratic; S1 is its degenerate double-root
                   limit and continuity with that limit selects the root.

Universal (all strata, physical inputs only: down masses lam_j, singlet
CKM row u_j, up data):
  d0 = sum u.lam,  beta = e3.sum u/lam = M_00,
  K1 := |Hd_01|^2 + |Hd_02|^2 = beta + d0.e1' - e2,
  K2 := d0.beta - e3 = d1.|Hd_02|^2 + d2.|Hd_01|^2 - L,
  L = 2 Re(Hd_01 Hd_12 Hd_02*)  (the loop term, in det Hd).

Full-chart identity (every entry, not just moduli):
  Hd_flavor = Uu . (V_CKM . diag(lam) . V_CKM^+) . Uu^+,
with Uu the up-eigenvector matrix in the weak basis: every chart entry is
an explicit algebraic function of masses, CKM, and up-basis data.

Strata inversions for the moduli:
  S1: x = 0, d1 = K2/K1 (WP49), v2 = K1, w2 = d1.d2 - beta.
  S2: loop = 0 exactly; x from the chart identity; d1 = (K2 - e1'.x)/(v2 - x)
      linear; w2 = 0.
  S3: x from the chart identity; d1 is a root of
      [d1(v2-x) + e1'.x - K2]^2 = 4.x.v2.(d1(e1'-d1) - beta) - Ls^2,
      Ls = 2 Im(loop); the physical root is the one nearer the family-limit
      estimate d1^0 = K2/v2 (172/172); L = d1(v2-x) + e1'.x - K2;
      |Ls| = sqrt(4.x.v2.w2 - L^2); sign(Ls) is the CP orientation - the
      ONLY J-sensitive input. mu12 = |Hm_12|^2 (up-mass block-block
      modulus) identity: with psi = arg(HuC_12), th = atan2(2|c|, a-b)/2,
      Z = e^{-i.psi}.Hd_12,
      mu12 = [st.ct.(d2-d1) + (ct^2-st^2).Re Z]^2 + Im(Z)^2.

Boundary: the WP48 chain q = J.blockgap.Dd/(v2.sqrt(w2)) is an S1-chart
identity (8e-13). On S2/S3 the corresponding chain involves different edge
products (on S2 the up-down MIXED loop carries J, since w2 = 0 but J != 0);
those per-stratum chain monomials are open chart algebra. The physical
M-theorem (WP48, R-constancy) is unaffected.

Gates:
  G0 strata sizes 394/282/172;
  G1 universal identities (d0, beta, K1) max rel err < 1e-9 (848 sheets);
  G2 full-chart identity max entry dev < 1e-9 (848 sheets);
  G3 S1 linear d1 = K2/K1 max rel err < 1e-9;
  G4 S2 loop dead |loop|/max|Hd| < 1e-20 and linear d1 < 1e-9;
  G5 S3 det identity for L < 1e-9 and quadratic root match < 1e-9;
  G6 S3 branch rule on 100% of S3 sheets;
  G7 S3 mu12 identity < 1e-9.

Reads: results/wp20_valley_audit.json
Writes: results/wp50_complement_inversion.json
Run: ./.venv/Scripts/python checkers/wp50_complement_inversion.py
"""
import json, math, os, sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wp7_ensemble as wp7

MASSES2 = {'u': 7.04e-6**2, 'c': 3.56e-3**2, 't': 0.967**2}
KPOS = {'u': 0, 'c': 1, 't': 2}


def main():
    recs = json.load(open('results/wp20_valley_audit.json'))['records']
    n = {1: 0, 2: 0, 3: 0}
    g1 = g2 = g3 = g4 = g4l = g5 = g5q = g7 = 0.0
    g6_bad = 0
    for r in recs:
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
        Hd0 = Yd @ Yd.conj().T
        best = None
        for blko in (blk, blk[::-1]):
            P = np.zeros((3, 3)); P[0, k] = 1; P[1, blko[0]] = 1; P[2, blko[1]] = 1
            HuC = P @ Hu @ P.T; Hd = P @ Hd0 @ P.T
            if best is None or abs(Hd[0, 1]) < abs(best[1][0, 1]):
                best = (HuC, Hd)
        HuC, Hd = best
        s = HuC[0, 0].real
        eu, Uu = np.linalg.eigh(HuC)
        oe = np.argsort(eu); Uu = Uu[:, oe]; eu = eu[oe]
        ed, Ud = np.linalg.eigh(Hd)
        od = np.argsort(ed); Ud = Ud[:, od]; ed = ed[od]
        Vc = Uu.conj().T @ Ud
        ksing = int(np.argmin(np.abs(eu - s)))
        um = np.abs(Vc[ksing, :])**2
        e1 = float(ed.sum())
        e2 = float(ed[0]*ed[1] + ed[0]*ed[2] + ed[1]*ed[2])
        e3 = float(ed[0]*ed[1]*ed[2])
        d0 = float((um*ed).sum())
        beta = float(e3*(um/ed).sum())
        e1p = e1 - d0
        K1 = beta + d0*e1p - e2
        K2 = d0*beta - e3
        d0c, d1c, d2c = Hd[0, 0].real, Hd[1, 1].real, Hd[2, 2].real
        xc, v2c, w2c = abs(Hd[0, 1])**2, abs(Hd[0, 2])**2, abs(Hd[1, 2])**2
        g1 = max(g1, abs(d0/d0c - 1),
                 abs(beta/(d1c*d2c - w2c) - 1),
                 abs(K1/(xc + v2c) - 1))
        # full-chart identity
        Hm = Vc @ np.diag(ed) @ Vc.conj().T
        rows = [ksing] + [z for z in range(3) if z != ksing]
        HmC = Hm[np.ix_(rows, rows)]
        Ub = Uu[:, rows]
        Hd_rec = Ub @ HmC @ Ub.conj().T
        scale = max(abs(Hd).max(), 1e-300)
        g2 = max(g2, abs(Hd_rec - Hd).max()/scale)
        x = abs(sum(HmC[0, jj]*Ub[1, jj].conjugate() for jj in range(3)))**2
        v2 = K1 - x
        if abs(Hd[0, 1]) < 1e-10:
            n[1] += 1
            g3 = max(g3, abs((K2/K1)/d1c - 1))
        elif w2c < 1e-40:
            n[2] += 1
            loop = Hd[0, 1]*Hd[1, 2]*Hd[2, 0]
            g4l = max(g4l, abs(loop)/scale)
            d1 = (K2 - e1p*x)/(v2 - x)
            g4 = max(g4, abs(d1/d1c - 1))
        else:
            n[3] += 1
            loop = Hd[0, 1]*Hd[1, 2]*Hd[2, 0]
            Lc, Ls = 2*loop.real, 2*loop.imag
            Lpred = d1c*(v2c - xc) + e1p*xc - K2
            g5 = max(g5, abs(Lpred - Lc)/max(abs(Lc), 1e-300))
            B1 = v2 - x; B0 = e1p*x - K2
            A2 = B1**2 + 4*x*v2
            A1 = 2*B1*B0 - 4*x*v2*e1p
            A0 = B0**2 + Ls**2 + 4*x*v2*beta
            disc = A1**2 - 4*A2*A0
            if disc < 0:
                g5q = 1.0
                continue
            rts = [(-A1 + math.sqrt(disc))/(2*A2), (-A1 - math.sqrt(disc))/(2*A2)]
            near = min(rts, key=lambda z: abs(z - d1c))
            g5q = max(g5q, abs(near/d1c - 1))
            d10 = K2/v2
            if min(rts, key=lambda z: abs(z - d10)) is not near:
                g6_bad += 1
            # mu12 identity (complex frame)
            a_, b_, c_ = HuC[1, 1].real, HuC[2, 2].real, HuC[1, 2]
            psi = math.atan2(c_.imag, c_.real)
            th2 = 0.5*math.atan2(2*abs(c_), a_ - b_)
            ct, st = math.cos(th2), math.sin(th2)
            Z = complex(math.cos(-psi), math.sin(-psi))*Hd[1, 2]
            mu12_pred = (st*ct*(d2c - d1c) + (ct**2 - st**2)*Z.real)**2 + Z.imag**2
            ephase = complex(math.cos(-psi), math.sin(-psi))
            U = np.array([[1, 0, 0], [0, ct, -st],
                          [0, st*ephase, ct*ephase]], complex)
            X = U.conj().T @ Hd @ U
            g7 = max(g7, abs(mu12_pred/abs(X[1, 2])**2 - 1))

    out = {'purpose': __doc__.splitlines()[0], 'strata': n,
           'universal_max_rel_err': g1, 'chart_identity_max_dev': g2,
           's1_linear_d1_err': g3, 's2_loop_dead': g4l, 's2_linear_d1_err': g4,
           's3_det_identity_err': g5, 's3_quadratic_root_err': g5q,
           's3_branch_rule_violations': g6_bad, 's3_mu12_err': g7,
           'gates': {}, 'gates_passed': 0}
    out['gates']['G0'] = bool(n == {1: 394, 2: 282, 3: 172})
    out['gates']['G1'] = bool(g1 < 1e-9)
    out['gates']['G2'] = bool(g2 < 1e-9)
    out['gates']['G3'] = bool(g3 < 1e-9)
    out['gates']['G4'] = bool(g4l < 1e-20 and g4 < 1e-9)
    out['gates']['G5'] = bool(g5 < 1e-9 and g5q < 1e-9)
    out['gates']['G6'] = bool(g6_bad == 0)
    out['gates']['G7'] = bool(g7 < 1e-9)
    out['gates_passed'] = sum(1 for v in out['gates'].values() if v)
    out['gates_total'] = len(out['gates'])
    json.dump(out, open('results/wp50_complement_inversion.json', 'w'), indent=1)
    print(json.dumps(out, indent=1))
    sys.exit(0 if out['gates_passed'] == out['gates_total'] else 1)


if __name__ == '__main__':
    main()
