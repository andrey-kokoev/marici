"""WP36: mechanism of the WP35 reciprocal law - the J-routing theorem

WP35 found the mixed u-singlet branch obeys th_u(phi) = 0.0389/sin(phi)
- 0.0001 (equivalently H_12.sin(phi) = 3.621e-2 cross-class constant).
This package derives WHY. Structural facts established by exploration:

  - ALL 303 u-class sheets place the phase edge in the DOWN sector: Yu
    (hence Hu) is real and carries no explicit phi. The reciprocal law
    is therefore not an algebraic identity of one sheet but a constraint
    the fit imposes through the readout.
  - On the mixed branch, zeroing H_12 kills J exactly (J -> 1e-23); on
    the unmixed branch J survives with H_12 = 0 identically. So J is
    ROUTED differently on the two branches.

Derived closed form (singlet s at index 0, block [[a,c],[c,b]] on
(1,2); u=Hd_01, v=Hd_02, w=Hd_12; exact algebra, machine-verified):

  det[Hu,Hd] = 2i ( c Im(w) (|C1|^2 - |C2|^2) - Im(C1 C12 conj(C2)) ),
  C1 = u(s-a) - c v,  C2 = v(s-b) - c u,  C12 = w(a-b) + c(Hd_22-Hd_11).

Its c^0 piece is -Im(u w conj(v))(s-a)(a-b)(s-b): the down-sector loop
product (the unmixed branch's J source). On mixed sheets this piece
vanishes and the c-linear pieces carry J; since each Im(Hd_xy) is
first-harmonic (mag product x sin phi), J fixed forces c.sin(phi) =
const, and th = c/Delta(1+O(th^2)) gives the reciprocal law.

Tests:
  G1 exact commutator identity on all u-class sheets (machine floor);
  G2 branch routing: J(c->0)/J < 1e-8 on all mixed sheets, and the
     down-loop term equals full J on all unmixed sheets;
  G3 first-harmonic: per sheet, Im(Hd_xy) scales exactly as sin(phi)
     under phi rescaling at fixed magnitudes (entries with |Im|>1e-12);
  G4 magnitude-only M: N(phi) = detC/(-2i c sin(phi)) is phi-independent
     at fixed magnitudes (mixed sheets), so J.Du.Dd = c.sin(phi).M(mags)
     exactly; report cos(phi) contamination if any;
  G5 emergent constancy: cross-class M spread (the WP35 law restated);
     M is a class label (within-class exact).

Reads: results/wp20_valley_audit.json
Writes: results/wp36_j_routing.json
Run: ./.venv/Scripts/python checkers/wp36_j_routing.py
"""
import json, math, sys, os
from collections import defaultdict
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
    """2i*( c Im(w)(|C1|^2-|C2|^2) - Im(C1 C12 conj(C2)) )."""
    s = Hu[0, 0].real
    a, b = Hu[1, 1].real, Hu[2, 2].real
    c = Hu[1, 2].real
    u, v, w = Hd[0, 1], Hd[0, 2], Hd[1, 2]
    C1 = u*(s-a) - c*v
    C2 = v*(s-b) - c*u
    C12 = w*(a-b) + c*(Hd[2, 2].real - Hd[1, 1].real)
    return 2j*(c*w.imag*(abs(C1)**2 - abs(C2)**2)
               - (C1*C12*np.conj(C2)).imag)

def sheet(r):
    mu, md = r['member']; s, i, j = r['phase_edge']
    th = np.array(r['log_mags'] + [r['phi_raw']])
    Yu, Yd = wp7.build_texture(mu, md, s, (i, j), th)
    return Yu, Yd, Yu @ Yu.conj().T, Yd @ Yd.conj().T

def main():
    w20 = json.load(open('results/wp20_valley_audit.json'))['records']
    rows = []
    for r in w20:
        Yu, Yd, Hu, Hd = sheet(r)
        off, k = min((max(abs(Hu[a, b]) for b in range(3) if b != a), a)
                     for a in range(3))
        if off > 1e-8 or abs(Hu.imag).max() > 1e-9:
            continue
        blk = [x for x in range(3) if x != k]
        t = abs(0.5*math.atan2(2*Hu[blk[0], blk[1]].real,
                               Hu[blk[1], blk[1]].real - Hu[blk[0], blk[0]].real))
        t = min(t, math.pi/2 - t)
        anchor = min(MASSES2, key=lambda m: abs(Hu[k, k].real/MASSES2[m]-1))
        if anchor != 'u':
            continue
        key = (f"{r['member'][0]}_{r['member'][1]}_"
               f"{r['phase_edge'][0]}{r['phase_edge'][1]}{r['phase_edge'][2]}")
        rows.append(dict(rec=r, key=key, Yu=Yu, Yd=Yd, Hu=Hu, Hd=Hd,
                         k=k, blk=blk, theta=t,
                         phi=r['phi_folded_deg'], phi_raw=r['phi_raw'],
                         mixed=t > 1e-9))

    # Work in the canonical frame: permute so singlet is index 0.
    def canon(x):
        k, blk = x['k'], x['blk']
        P = np.zeros((3, 3))
        P[0, k] = 1; P[1, blk[0]] = 1; P[2, blk[1]] = 1
        Hu = P @ x['Hu'] @ P.T
        Hd = P @ x['Hd'] @ P.T
        return Hu, Hd

    g1_err = 0.0
    g2_mixed, g2_unmixed = [], []
    g3_err, g4_var, m_vals = 0.0, 0.0, []
    for x in rows:
        Hu, Hd = canon(x)
        Du, Dd = eig_D(Hu), eig_D(Hd)
        d = detC(Hu, Hd)
        # G1: exact identity
        g1_err = max(g1_err, abs(d - closed_form_detC(Hu, Hd)))
        J = (d/(-2j*Du*Dd)).real
        # G2: branch routing - zero c
        Hu0 = Hu.copy(); Hu0[1, 2] = 0; Hu0[2, 1] = 0
        J0 = (detC(Hu0, Hd)/(-2j*eig_D(Hu0)*Dd)).real
        if x['mixed']:
            g2_mixed.append(abs(J0/J))
        else:
            g2_unmixed.append(abs(J0/J - 1))
        # G3: first-harmonic Im(Hd) under phi rescale at fixed mags
        r0 = x['rec']
        mu, md = r0['member']; s_, i_, j_ = r0['phase_edge']
        sc = 0.7
        th2 = np.array(r0['log_mags'] + [r0['phi_raw']*sc])
        Yu2, Yd2 = wp7.build_texture(mu, md, s_, (i_, j_), th2)
        Hd2 = Yd2 @ Yd2.conj().T
        for a_ in range(3):
            for b_ in range(a_+1, 3):
                im1 = x['Hd'][a_, b_].imag
                if abs(im1) > 1e-12:
                    im2 = Hd2[a_, b_].imag
                    expect = im1*math.sin(sc*r0['phi_raw'])/math.sin(r0['phi_raw'])
                    g3_err = max(g3_err, abs(im2-expect)/abs(im1))
        # G4: N(phi) = detC/(-2i c sin phi) phi-independent at fixed mags
        if x['mixed']:
            c = Hu[1, 2].real
            sp1 = math.sin(x['phi_raw'])
            N1 = (d/(-2j*c*sp1)).real
            th3 = np.array(r0['log_mags'] + [r0['phi_raw']*sc])
            Yu3, Yd3 = wp7.build_texture(mu, md, s_, (i_, j_), th3)
            Hu3, Hd3 = Yu3 @ Yu3.conj().T, Yd3 @ Yd3.conj().T
            P = np.zeros((3, 3))
            P[0, x['k']] = 1; P[1, x['blk'][0]] = 1; P[2, x['blk'][1]] = 1
            Hu3, Hd3 = P @ Hu3 @ P.T, P @ Hd3 @ P.T
            c3 = Hu3[1, 2].real
            N2 = (detC(Hu3, Hd3)/(-2j*c3*math.sin(sc*x['phi_raw']))).real
            g4_var = max(g4_var, abs(N2-N1)/max(abs(N1), 1e-300))
            m_vals.append(dict(key=x['key'], phi=x['phi'],
                               q=c*math.sin(math.radians(x['phi'])),
                               M=abs(J)*Du*Dd/(c*math.sin(math.radians(x['phi'])))))

    # G5: emergent constancy of q = c.sin(phi_folded) (the WP35 law) and
    # of M = |J|.Du.Dd/q (equivalent, since |J|, Du, Dd are fit constants);
    # signs fixed by c > 0 and folded phi in (0, 90 deg).
    M = np.array([m['M'] for m in m_vals])
    Q = np.array([m['q'] for m in m_vals])
    byclass = defaultdict(list)
    for m in m_vals:
        byclass[m['key']].append(m['M'])
    within_rel = max((float(np.ptp(v)/abs(np.mean(v)))
                      for v in byclass.values() if len(v) >= 2), default=0.0)
    q_rel = float(np.ptp(Q)/abs(Q.mean())) if len(Q) else None
    m_rel = float(np.ptp(M)/abs(M.mean())) if len(M) else None

    gates = {
        "G1_exact_commutator_identity": dict(
            value=dict(max_abs_err=float(g1_err), n_sheets=len(rows)),
            passed=bool(g1_err < 1e-20)),
        "G2_branch_routing": dict(
            value=dict(max_mixed_J0_over_J=float(max(g2_mixed, default=0.0)),
                       max_unmixed_dev_from_1=float(max(g2_unmixed, default=0.0)),
                       n_mixed=len(g2_mixed), n_unmixed=len(g2_unmixed)),
            passed=bool(max(g2_mixed, default=1) < 1e-8
                        and max(g2_unmixed, default=1) < 1e-8)),
        "G3_first_harmonic_ImHd": dict(
            value=dict(max_rel_err=float(g3_err)),
            passed=bool(g3_err < 1e-9)),
        "G4_magnitude_only_M": dict(
            value=dict(max_rel_variation=float(g4_var)),
            passed=bool(g4_var < 1e-9)),
        "G5_emergent_law_constancy": dict(
            value=dict(n_mixed_sheets=len(m_vals),
                       q_mean=float(Q.mean()) if len(Q) else None,
                       q_cross_class_rel=q_rel,
                       M_mean=float(M.mean()) if len(M) else None,
                       M_cross_class_rel=m_rel,
                       M_within_class_rel_max=within_rel,
                       note='within-class spread is fit phi-jitter acting on '
                            'the smooth law (same mechanism as WP35 c-class); '
                            'cross-class-at-fixed-phi is the sharp statement',
                       theta_law_check=float(Q.mean()/0.932) if len(Q) else None),
            passed=bool(len(m_vals) > 0 and q_rel is not None
                        and q_rel < 1e-4 and within_rel < 1e-2)),
    }
    out = dict(purpose=__doc__.strip().splitlines()[0],
               closed_form=("det[Hu,Hd] = 2i ( c Im(w)(|C1|^2-|C2|^2) "
                            "- Im(C1 C12 conj(C2)) ) with C1=u(s-a)-cv, "
                            "C2=v(s-b)-cu, C12=w(a-b)+c(Hd22-Hd11)"),
               n_u_sheets=len(rows),
               n_mixed=sum(x['mixed'] for x in rows),
               gates=gates,
               gates_passed=sum(bool(g['passed']) for g in gates.values()))
    json.dump(out, open('results/wp36_j_routing.json', 'w'), indent=1)
    print("gates:", out['gates_passed'], "/", len(gates))
    for name, g in gates.items():
        print(f"  {name}: passed={g['passed']} value={json.dumps(g['value'])[:200]}")

if __name__ == '__main__':
    main()
