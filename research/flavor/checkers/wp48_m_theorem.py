"""WP48: the exact M-theorem - class-constancy of the pairing modulus derived.

Strominger's open question (comm 2026-08-24): is the WP36 G5 ensemble law
"M class-constant" derivable symbolically inside the fit manifold?

Answer: YES. Per sheet, exact (WP36 G4): q := c.sin(phi) = J.Du.Dd/M.
WP48 certifies the M-theorem:

  M = Du.Dd.V3_class / (C_class . scale^2_class),

equivalently q = C_class . scale^2 . J / V3_class, with per-class pure numbers
  C_u = 0.9993729702, C_c = 1.0008809, C_t = 0.9920333163
constant across ALL 848 block-diagonal sheets (WP44 family AND complement).
Closed forms (using J = V3.Vmon exactly):
  u: q = C_u . yt^2 . |Vcb| . sin(gamma)
  c: q = C_c . yt^2 . |Vub| . sin(gamma)
  t: q = C_t . yc^2 . |Vub| / |Vcb|

Corollary (class-constancy derived): q is a pure number times a physical
CKM/mass monomial, so its ensemble spread is exactly the chi^2 slack of the
physical monomial - measured monomial ranges match the WP36/46 q-spreads
(u 3.9e-5 vs 2.9e-5; c 1.1e-2 vs 1.1e-2; t 1.2e-8 vs 1.3e-8). The emergent
law is the fit-pinning of physical inputs through an exact map.

New exact lemma (family): with Hd_01 = 0 the down characteristic polynomial
inverts: |Hd_02|^2 = (T - d0.S)/(d1 - d0), |Hd_12|^2 = (d1.S - T)/(d1 - d0),
S = d0d1+d0d2+d1d2 - e2, T = d0d1d2 - e3 (down diagonals + down masses only).

Boundary: the complement-family constancy (3.5e-12 u, 2.8e-11 t, 1.4e-6 c) is
a PARAMETER-FREE prediction of the family-fitted C; its chart-algebra
derivation (loop-product term) is open. The c-class residual 1.4e-6 exceeds
u/t levels; C_class values remain WP44-certified point numbers.

Gates:
  G1 lemma max rel err < 1e-9 (family);
  G2 chain q = J.blockgap.Dd/(|Hd02|^2 |Hd12|) max rel err < 1e-9 (family);
  G3 R = q.V3/(J.scale^2) per-class family rel std < 1e-7 (u), 1e-5 (c), 1e-9 (t);
  G4 complement prediction with family-frozen C: max |R/C - 1| < 1e-8 (u),
     5e-5 (c), 1e-9 (t);
  G5 spread budget: q rel range / monomial rel range in [0.3, 3] per class (family).

Reads: results/wp20_valley_audit.json
Writes: results/wp48_m_theorem.json
Run: ./.venv/Scripts/python checkers/wp48_m_theorem.py
"""
import json, math, os, sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wp7_ensemble as wp7

MASSES2 = {'u': 7.04e-6**2, 'c': 3.56e-3**2, 't': 0.967**2}

def fold(p):
    p = abs(p) % math.pi
    return math.pi - p if p > math.pi/2 else p

def main():
    recs = json.load(open('results/wp20_valley_audit.json'))['records']
    g1 = g2 = 0.0
    R = {'u': {'f': [], 'x': []}, 'c': {'f': [], 'x': []}, 't': {'f': [], 'x': []}}
    QS = {'u': [], 'c': [], 't': []}
    MN = {'u': [], 'c': [], 't': []}
    n_used = 0
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
        fam = abs(Hd[0, 1]) < 1e-10
        s = HuC[0, 0].real; c = HuC[1, 2].real
        eu, Uu = np.linalg.eigh(HuC); ed, Ud = np.linalg.eigh(Hd)
        oe = np.argsort(eu); Uu = Uu[:, oe]; eu = eu[oe]
        od = np.argsort(ed); Ud = Ud[:, od]; ed = ed[od]
        yu2, yc2, yt2 = eu
        Du = (yt2-yc2)*(yt2-yu2)*(yc2-yu2)
        Dd = (ed[2]-ed[1])*(ed[2]-ed[0])*(ed[1]-ed[0])
        sphi = math.sin(fold(th[-1]))
        q = c*sphi
        Vc = Uu.conj().T @ Ud; V = np.abs(Vc)
        z = -(Vc[0, 0]*Vc[0, 2].conjugate())/(Vc[1, 0]*Vc[1, 2].conjugate())
        gam = abs(math.atan2(z.imag, z.real))
        sg = math.sin(gam)
        if anchor == 'u':
            scale2, V3, mon = yt2, V[0, 0]*V[0, 2]*V[1, 0], V[1, 2]*sg
        elif anchor == 'c':
            scale2, V3, mon = yt2, V[0, 0]*V[1, 0]*V[1, 2], V[0, 2]*sg
        else:
            scale2, V3, mon = yc2, V[0, 0]*V[1, 0]*V[1, 2]**2*sg, V[0, 2]/V[1, 2]
        n_used += 1
        R[anchor]['f' if fam else 'x'].append(q*V3/(r['J']*scale2))
        if fam:
            QS[anchor].append(q)
            MN[anchor].append(mon)
            nonsing = sorted(eu, key=lambda x: abs(x-s))[1:]
            blockgap = abs(nonsing[1]-nonsing[0])
            v2, w2 = abs(Hd[0, 2])**2, abs(Hd[1, 2])**2
            d0, d1, d2 = Hd[0, 0].real, Hd[1, 1].real, Hd[2, 2].real
            e2 = ed[0]*ed[1]+ed[0]*ed[2]+ed[1]*ed[2]
            e3 = ed[0]*ed[1]*ed[2]
            S = d0*d1+d0*d2+d1*d2 - e2
            T = d0*d1*d2 - e3
            g1 = max(g1, abs((T-d0*S)/(d1-d0)/v2 - 1),
                     abs((d1*S-T)/(d1-d0)/w2 - 1))
            q_chain = r['J']*blockgap*Dd/(v2*math.sqrt(w2))
            g2 = max(g2, abs(q_chain/q - 1))

    C = {a: float(np.mean(R[a]['f'])) for a in 'uct'}
    out = {'purpose': __doc__.splitlines()[0], 'n_sheets': n_used,
           'C_class': C, 'lemma_max_rel_err': g1, 'chain_max_rel_err': g2,
           'per_class': {}, 'gates': {}, 'gates_passed': 0}
    ok = 0
    out['gates']['G1'] = bool(g1 < 1e-9)
    out['gates']['G2'] = bool(g2 < 1e-9)
    g3thr = {'u': 1e-7, 'c': 1e-5, 't': 1e-9}
    g4thr = {'u': 1e-8, 'c': 5e-5, 't': 1e-9}
    for a in 'uct':
        rf = np.array(R[a]['f']); rx = np.array(R[a]['x'])
        qs = np.array(QS[a]); mn = np.array(MN[a])
        g3 = float(rf.std()/rf.mean())
        g4 = float(np.abs(rx/C[a] - 1).max()) if len(rx) else 0.0
        g5 = float((qs.max()-qs.min())/qs.mean() / ((mn.max()-mn.min())/mn.mean()))
        out['per_class'][a] = {
            'n_family': int(len(rf)), 'n_complement': int(len(rx)),
            'R_family_rel_std': g3, 'complement_max_dev': g4,
            'q_rel_range': float((qs.max()-qs.min())/qs.mean()),
            'monomial_rel_range': float((mn.max()-mn.min())/mn.mean()),
            'spread_ratio': g5}
        out['gates'][f'G3_{a}'] = bool(g3 < g3thr[a])
        out['gates'][f'G4_{a}'] = bool(g4 < g4thr[a])
        out['gates'][f'G5_{a}'] = bool(0.3 < g5 < 3.0)
    out['gates_passed'] = sum(1 for v in out['gates'].values() if v)
    out['gates_total'] = len(out['gates'])
    json.dump(out, open('results/wp48_m_theorem.json', 'w'), indent=1)
    print(json.dumps(out, indent=1))
    sys.exit(0 if out['gates_passed'] == out['gates_total'] else 1)

if __name__ == '__main__':
    main()
