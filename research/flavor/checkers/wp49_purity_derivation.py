"""WP49: the purity numbers are explicit functions of physical data.

WP48 closed the M-theorem M = Du.Dd.V3/(C_class.scale^2) with three pure
numbers C_u = 0.9993729702, C_c = 1.0008809, C_t = 0.9920333163 certified
only as ensemble constants. WP49 derives them. On the WP44 family
(Hd_01 = 0) the down sector inverts EXACTLY and RATIONALLY from physical
inputs alone (down masses lam_j and the singlet CKM row moduli u_j):

  d0   = sum_j u_j lam_j                        (spectral diagonal)
  beta = e3 . sum_j u_j / lam_j                 ((0,0) minor / resolvent)
  d1   = (beta.d0 - e3)/(e1'.d0 - e2 + beta)    (linear: cubic terms cancel)
  d2   = e1' - d1
  v^2  = p(d0)/(d1 - d0),  w^2 = p(d1)/(d0 - d1),  p(x) = prod_j(x - lam_j)

so C_class = blockgap.Dd.V3/(scale^2.v^2.sqrt(w^2)) is an explicit algebraic
function of masses and CKM data. Certified at machine precision on all 394
family sheets. Evaluated at the measured point (OBS17 central values) the
same function reproduces the WP48 fitted constants within fit slack:
  C_u dev 1.7e-5, C_c dev 3.6e-6, C_t dev 5.5e-4.
The c-class deviation sits at the scale of the WP48 c-purity residual
(1.4e-6), indicating that residual is fit offset, not structure.

Implementation note: the singlet CKM row must be read at the eigen-SORTED
position k (u -> 0, c -> 1, t -> 2); a flavor-index row lookup silently
picks the wrong row on permuted sheets. Two constructions are cross-checked
here: (a) the exact frame whose first basis vector is e_0
(UuC = [[1,0,0],[0,ct,-st],[0,st,ct]], singlet row = Ud[0,:] manifestly);
(b) np.linalg.eigh(HuC) with the sorted singlet row. On the certified
ensemble they agree to 2.4e-13 in d0 (gate G4), so no eigh contamination
materializes; the exact frame is retained as the convention-explicit form.

Boundary: the d1 formula assumes the family (Hd_01 = 0); complement-family
inversion needs the loop term (WP48 boundary, still open). The purities are
NOT simple CKM monomials (WP44 negative control stands). Why the derived
algebraic function evaluates within 1e-2 of 1 for all three anchors is the
residue question, left open.

Gates:
  G1_{u,c,t}: inversion (d0,d1,d2,v2,w2) max rel err < 1e-10 (family);
  G2_{u,c,t}: C pipeline vs chart max rel err < 1e-10;
  G3_{u,c,t}: measured-point C within 5e-4 (u), 1e-4 (c), 2e-2 (t) of the
              WP48 fitted constants;
  G4: cross-frame consistency - d0 from the eigh sorted singlet row
      agrees with the exact-frame/chart value to < 1e-10.

Reads: results/wp20_valley_audit.json, results/wp48_m_theorem.json
Writes: results/wp49_purity_derivation.json
Run: ./.venv/Scripts/python checkers/wp49_purity_derivation.py
"""
import json, math, os, sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wp7_ensemble as wp7

MASSES2 = {'u': 7.04e-6**2, 'c': 3.56e-3**2, 't': 0.967**2}
KPOS = {'u': 0, 'c': 1, 't': 2}


def invert_down(um, ed):
    """Exact rational family down-sector inversion from physical inputs."""
    e1 = float(ed.sum())
    e2 = float(ed[0]*ed[1] + ed[0]*ed[2] + ed[1]*ed[2])
    e3 = float(ed[0]*ed[1]*ed[2])
    d0 = float((um*ed).sum())
    beta = e3*float((um/ed).sum())
    e1p = e1 - d0
    d1 = (beta*d0 - e3)/(e1p*d0 - e2 + beta)
    d2 = e1p - d1
    v2 = float(np.prod(d0 - ed))/(d1 - d0)
    w2 = float(np.prod(d1 - ed))/(d0 - d1)
    return d0, d1, d2, v2, w2


def c_value(anchor, eu, ed, Vc, v2, w2, s):
    """C_class = blockgap.Dd.V3/(scale^2.v^2.sqrt(w^2)) (WP44 conventions)."""
    yu2, yc2, yt2 = eu
    Dd = (ed[2]-ed[1])*(ed[2]-ed[0])*(ed[1]-ed[0])
    nonsing = sorted(eu, key=lambda x: abs(x - s))[1:]
    blockgap = abs(nonsing[1] - nonsing[0])
    V = np.abs(Vc)
    z = -(Vc[0, 0]*Vc[0, 2].conjugate())/(Vc[1, 0]*Vc[1, 2].conjugate())
    sg = math.sin(abs(math.atan2(z.imag, z.real)))
    if anchor == 'u':
        scale2, V3 = yt2, V[0, 0]*V[0, 2]*V[1, 0]
    elif anchor == 'c':
        scale2, V3 = yt2, V[0, 0]*V[1, 0]*V[1, 2]
    else:
        scale2, V3 = yc2, V[0, 0]*V[1, 0]*V[1, 2]**2*sg
    return blockgap*Dd*V3/(scale2*v2*math.sqrt(w2))


def main():
    recs = json.load(open('results/wp20_valley_audit.json'))['records']
    C_fit = json.load(open('results/wp48_m_theorem.json'))['C_class']
    errs = {a: {'d0': 0.0, 'd1': 0.0, 'd2': 0.0, 'v2': 0.0, 'w2': 0.0, 'C': 0.0}
            for a in 'uct'}
    eigh_d0_err = 0.0
    n = 0
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
        if abs(Hd[0, 1]) > 1e-10:
            continue
        s = HuC[0, 0].real
        # exact frame: first basis vector e_0, real rotation in the block
        a_, b_, c_ = HuC[1, 1].real, HuC[2, 2].real, HuC[1, 2].real
        th2 = 0.5*math.atan2(2*c_, b_ - a_)
        ct, st = math.cos(th2), math.sin(th2)
        UuC = np.array([[1, 0, 0], [0, ct, -st], [0, st, ct]], float)
        ed, Ud = np.linalg.eigh(Hd)
        od = np.argsort(ed); Ud = Ud[:, od]; ed = ed[od]
        um = np.abs((UuC.T @ Ud)[0, :])**2
        # eigh pipeline (negative control): sorted singlet row of Uu^+.Ud
        eu, Uu = np.linalg.eigh(HuC)
        oe = np.argsort(eu); Uu = Uu[:, oe]; eu = eu[oe]
        Vc = Uu.conj().T @ Ud
        um_eigh = np.abs(Vc[KPOS[anchor], :])**2
        # inversion from physical data vs chart entries
        d0, d1, d2, v2, w2 = invert_down(um, ed)
        d0x = invert_down(um_eigh, ed)[0]
        d0c, d1c, d2c = Hd[0, 0].real, Hd[1, 1].real, Hd[2, 2].real
        v2c, w2c = abs(Hd[0, 2])**2, abs(Hd[1, 2])**2
        C_inv = c_value(anchor, eu, ed, Vc, v2, w2, s)
        C_chart = c_value(anchor, eu, ed, Vc, v2c, w2c, s)
        n += 1
        E = errs[anchor]
        E['d0'] = max(E['d0'], abs(d0/d0c - 1))
        E['d1'] = max(E['d1'], abs(d1/d1c - 1))
        E['d2'] = max(E['d2'], abs(d2/d2c - 1))
        E['v2'] = max(E['v2'], abs(v2/v2c - 1))
        E['w2'] = max(E['w2'], abs(w2/w2c - 1))
        E['C'] = max(E['C'], abs(C_inv/C_chart - 1))
        eigh_d0_err = max(eigh_d0_err, abs(d0x/d0c - 1))

    # measured-point evaluation (OBS17 central values, wp7_ensemble)
    YU2, YC2, YT2 = 7.04e-6**2, 3.56e-3**2, 0.967**2
    YD2, YS2, YB2 = 1.54e-5**2, 3.06e-4**2, 1.630e-2**2
    Vus, Vub, Vcb = 0.22517, 0.003763, 0.04189
    Vcd, Vtd, Vts = 0.22503, 0.00863, 0.04117
    gam = math.radians(66.4)
    Vud = math.sqrt(1 - Vus**2 - Vub**2)
    Vcs = math.sqrt(1 - Vcd**2 - Vcb**2)
    Vm = np.array([
        [Vud, Vus, Vub*complex(math.cos(-gam), math.sin(-gam))],
        [-Vcd, Vcs, Vcb],
        [Vtd*complex(math.cos(math.pi), 0), -Vts, 1.0]], complex)
    lam = np.array([YD2, YS2, YB2])
    Hu_f = np.diag([YU2, YC2, YT2]).astype(complex)
    Hd_f = Vm @ np.diag(lam) @ Vm.conj().T
    C_meas = {}
    for anchor, kp in (('u', 0), ('c', 1), ('t', 2)):
        blk = [x for x in range(3) if x != kp]
        P = np.zeros((3, 3)); P[0, kp] = 1; P[1, blk[0]] = 1; P[2, blk[1]] = 1
        HuC = P @ Hu_f @ P.T; Hd = P @ Hd_f @ P.T
        eu, Uu = np.linalg.eigh(HuC)
        oe = np.argsort(eu); Uu = Uu[:, oe]; eu = eu[oe]
        ed, Ud = np.linalg.eigh(Hd)
        od = np.argsort(ed); Ud = Ud[:, od]; ed = ed[od]
        Vc = Uu.conj().T @ Ud
        um = np.abs(Vc[KPOS[anchor], :])**2
        # synthetic Hu is exactly diagonal: eigh singlet row is exact here.
        # The d1 formula assumes the family, so this is the FAMILY-
        # PRESENTATION value of C at the measured physical point.
        d0, d1, d2, v2, w2 = invert_down(um, ed)
        C_meas[anchor] = c_value(anchor, eu, ed, Vc, v2, w2, eu[KPOS[anchor]])

    dev = {a: abs(C_meas[a]/C_fit[a] - 1) for a in 'uct'}
    out = {'purpose': __doc__.splitlines()[0], 'n_family_sheets': n,
           'inversion_max_rel_err': errs, 'C_fit_wp48': C_fit,
           'C_measured_point': C_meas, 'measured_deviation': dev,
           'eigh_cross_frame_d0_max_rel_err': eigh_d0_err,
           'gates': {}, 'gates_passed': 0}
    for a in 'uct':
        E = errs[a]
        out['gates'][f'G1_{a}'] = bool(max(E[x] for x in ('d0', 'd1', 'd2', 'v2', 'w2')) < 1e-10)
        out['gates'][f'G2_{a}'] = bool(E['C'] < 1e-10)
    g3thr = {'u': 5e-4, 'c': 1e-4, 't': 2e-2}
    for a in 'uct':
        out['gates'][f'G3_{a}'] = bool(dev[a] < g3thr[a])
    out['gates']['G4'] = bool(eigh_d0_err < 1e-10)
    out['gates_passed'] = sum(1 for v in out['gates'].values() if v)
    out['gates_total'] = len(out['gates'])
    json.dump(out, open('results/wp49_purity_derivation.json', 'w'), indent=1)
    print(json.dumps(out, indent=1))
    sys.exit(0 if out['gates_passed'] == out['gates_total'] else 1)


if __name__ == '__main__':
    main()
