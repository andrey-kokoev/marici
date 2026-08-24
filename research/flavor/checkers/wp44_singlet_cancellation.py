"""WP44: the singlet-gap cancellation - charge constants are block-gap x down data.

WP43 reduced the three anchor constants to C = Du Dd (CKM monomial)/(scale^2 M)
with M the WP36 magnitude-only chart function. WP44 derives M in closed form on
the family of sheets whose down sector, in the up-canonical frame (singlet at
index 0), has Hd_01 = 0 (block swap allowed):

  M = |Hd_02|^2 |Hd_12| |chi_block(s)|,
  chi_block(s) = (s - lam_b1)(s - lam_b2) = c^2 - (s-a)(s-b),

the up-block characteristic polynomial evaluated at the singlet. Derivation:
with u = Hd_01 = 0, WP36's exact commutator form gives
det[Hu,Hd]/(2i c sin(phi)) = |v|^2 (Im w/sin phi)[c^2 - (s-a)(s-b)].

Since Du = (lam_t-lam_c)(lam_t-lam_u)(lam_c-lam_u) and chi_block(s) carries the
two singlet-to-block gaps, Du/chi_block(s) = block gap EXACTLY. Therefore on
this family the up-singlet drops out of the charge constants entirely:

  C_anchor = (block gap) Dd (CKM monomial) / (scale^2 |Hd_02|^2 |Hd_12|)

one universal law; the class enters only via (scale, CKM monomial, block gap).

Also on this family the down eigenvectors have exact profiles
  v(lambda) ~ (Hd_02/(lambda - Hd_00), Hd_12/(lambda - Hd_11), 1),
so the entire readout (CKM included) is closed-form chart algebra.

Gates:
  G1 M-anatomy: max |M/(|Hd02|^2|Hd12|chiB) - 1| < 1e-9 on family sheets;
  G2 gap-cancelled C per anchor class, max rel err < 1e-9;
  G3 eigenvector profiles reproduce |Ud| < 1e-9 on family sheets;
  G4 unique-matching down graphs: det Hd = (matching product)^2 < 1e-9;
  G5 boundary null: on complement u-sheets no universal quadratic
     M/chiB = Q(|Hd_01|,|Hd_02|,|Hd_12|,Re cross terms) exists
     (global 6-basis lstsq max residual > 1e-3).

Reads: results/wp20_valley_audit.json
Writes: results/wp44_singlet_cancellation.json
Run: ./.venv/Scripts/python checkers/wp44_singlet_cancellation.py
"""
import json, math, os, sys
from itertools import permutations

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wp7_ensemble as wp7

MASSES2 = {'u': 7.04e-6**2, 'c': 3.56e-3**2, 't': 0.967**2}

def fold(p):
    p = abs(p) % math.pi
    return math.pi - p if p > math.pi/2 else p

def matchings(dslots):
    out = []
    have = set(dslots)
    for cols in permutations(range(3)):
        if all((r_, c_) in have for r_, c_ in enumerate(cols)):
            out.append(cols)
    return out

def main():
    w20 = json.load(open('results/wp20_valley_audit.json'))['records']
    cov = {'u': [0, 0], 'c': [0, 0], 't': [0, 0]}
    errM = {'u': 0.0, 'c': 0.0, 't': 0.0}
    errC = {'u': 0.0, 'c': 0.0, 't': 0.0}
    errP = 0.0
    errG4 = 0.0; n_g4 = 0
    cvals = {'u': [], 'c': [], 't': []}
    compl_basis, compl_y = [], []
    for r in w20:
        mu, md = r['member']; s_, i, j = r['phase_edge']
        th = np.array(r['log_mags'] + [r['phi_raw']])
        Yu, Yd = wp7.build_texture(mu, md, s_, (i, j), th)
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
        Hd0 = Yd @ Yd.conj().T
        covered = False
        for blko in (blk, blk[::-1]):
            P = np.zeros((3, 3)); P[0, k] = 1; P[1, blko[0]] = 1; P[2, blko[1]] = 1
            HuC = P @ Hu @ P.T; Hd = P @ Hd0 @ P.T
            if abs(Hd[0, 1]) < 1e-10:
                covered = True
                break
        s = HuC[0,0].real; c = HuC[1,2].real
        eu, Uu = np.linalg.eigh(HuC); ed, Ud = np.linalg.eigh(Hd)
        oe = np.argsort(eu); Uu = Uu[:, oe]; eu = eu[oe]
        od = np.argsort(ed); Ud = Ud[:, od]; ed = ed[od]
        yu2, yc2, yt2 = eu
        Du = (yt2-yc2)*(yt2-yu2)*(yc2-yu2)
        Dd = (ed[2]-ed[1])*(ed[2]-ed[0])*(ed[1]-ed[0])
        detC = np.linalg.det(HuC @ Hd - Hd @ HuC)
        J = abs(detC/(-2j*Du*Dd))
        sphi = math.sin(fold(th[-1]))
        M43 = J*Du*Dd/(c*sphi)
        nonsing = sorted(eu, key=lambda x: abs(x-s))[1:]
        chiB = abs((s-nonsing[0])*(s-nonsing[1]))
        blockgap = abs(nonsing[1]-nonsing[0])
        Vc = Uu.conj().T @ Ud; V = np.abs(Vc)
        z = -(Vc[0,0]*Vc[0,2].conjugate())/(Vc[1,0]*Vc[1,2].conjugate())
        gam = abs(math.atan2(z.imag, z.real))
        if anchor == 'u':
            V3 = V[0,0]*V[0,2]*V[1,0]; scale2, Vmon = yt2, V[1,2]*math.sin(gam)
        elif anchor == 'c':
            V3 = V[0,0]*V[1,0]*V[1,2]; scale2, Vmon = yt2, V[0,2]*math.sin(gam)
        else:
            V3 = V[0,0]*V[1,0]*V[1,2]**2*math.sin(gam)
            scale2, Vmon = yc2, V[0,2]/V[1,2]
        C_dir = (c*sphi)/(scale2*Vmon)
        cnt_key = anchor
        if not covered:
            cov[cnt_key][0] += 1
            if anchor == 'u':
                u_, v_, w_ = Hd[0,1], Hd[0,2], Hd[1,2]
                compl_basis.append([abs(u_)**2, abs(v_)**2, abs(w_)**2,
                                    (u_*v_.conjugate()).real,
                                    (u_*w_.conjugate()).real,
                                    (v_*w_.conjugate()).real])
                compl_y.append(M43/chiB)
            continue
        cov[cnt_key][0] += 1; cov[cnt_key][1] += 1
        v02, w12 = abs(Hd[0,2]), abs(Hd[1,2])
        errM[anchor] = max(errM[anchor], abs(v02*v02*w12*chiB/M43 - 1))
        C_gap = blockgap*Dd*V3/(scale2*v02*v02*w12)
        errC[anchor] = max(errC[anchor], abs(C_gap/C_dir - 1))
        cvals[anchor].append(C_gap)
        # G3: eigenvector profiles
        d0, d1 = Hd[0,0].real, Hd[1,1].real
        for e in range(3):
            x = np.array([Hd[0,2]/(ed[e]-d0), Hd[1,2]/(ed[e]-d1), 1.0])
            x = x/np.linalg.norm(x)
            for comp in range(3):
                denom = abs(Ud[comp, e])
                if denom > 1e-12:
                    errP = max(errP, abs(abs(x[comp])/denom - 1))
        # G4: unique perfect matching
        dslots = wp7.mask_slots(md)
        ms = matchings(dslots)
        if len(ms) == 1:
            us = wp7.mask_slots(mu)
            dmags = {slot: m for slot, m in
                     zip(dslots, np.exp(th[:9])[len(us):])}
            prod2 = float(np.prod([dmags[(r_, c_)]**2
                                   for r_, c_ in enumerate(ms[0])]))
            n_g4 += 1
            errG4 = max(errG4, abs(np.linalg.det(Hd)/prod2 - 1))

    # G5 boundary null on complement u-sheets
    B = np.array(compl_basis); Y = np.array(compl_y)
    coef, _, rank, _ = np.linalg.lstsq(B, Y, rcond=None)
    g5_resid = float(np.abs(B @ coef/Y - 1).max())

    gates = {
        'G1_M_anatomy': dict(value={a: float(errM[a]) for a in errM},
                             passed=bool(max(errM.values()) < 1e-9)),
        'G2_gap_cancelled_constants': dict(
            value={a: float(errC[a]) for a in errC},
            passed=bool(max(errC.values()) < 1e-9)),
        'G3_eigenvector_profiles': dict(value=float(errP),
                                        passed=bool(errP < 1e-9)),
        'G4_unique_matching_determinant': dict(
            value=dict(n=n_g4, max_rel_err=float(errG4)),
            passed=bool(n_g4 > 0 and errG4 < 1e-9)),
        'G5_boundary_null': dict(
            value=dict(n_complement_u=len(compl_y), basis_rank=int(rank),
                       max_rel_residual=g5_resid),
            passed=bool(g5_resid > 1e-3)),
    }
    result = dict(
        purpose=__doc__.strip().split('\n')[0],
        family="Hd_01 = 0 in the up-canonical frame (block swap allowed)",
        coverage={a: dict(total=cov[a][0], covered=cov[a][1]) for a in cov},
        law="C_anchor = (block gap) Dd (CKM monomial)/(scale^2 |Hd02|^2 |Hd12|)",
        constants={a: float(np.median(v)) for a, v in cvals.items()},
        gates=gates,
        gates_passed=sum(g['passed'] for g in gates.values()))
    with open('results/wp44_singlet_cancellation.json', 'w') as f:
        json.dump(result, f, indent=1)
    print(f"gates: {result['gates_passed']} / {len(gates)}")
    for name, g in gates.items():
        print(f"  {name}: passed={g['passed']}  value={json.dumps(g['value'])[:220]}")
    print('constants:', {a: round(v, 10) for a, v in result['constants'].items()})
    print('coverage:', result['coverage'])

if __name__ == '__main__':
    main()
