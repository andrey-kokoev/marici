"""WP50 explore 5: S3 two-fold ambiguity resolution by mu12 = |HmC_12|^2.

HmC = UuC^T.Hd.UuC (up-mass basis, physical). At each quadratic root d1:
reconstruct w2 = d1(e1'-d1)-beta, L = B1.d1+B0, and the loop phase via
Hd_12 phase eta: mu12 = [st.ct.(d2-d1) + (ct^2-st^2).Re(Hd_12)]^2 + Im(Hd_12)^2.
But eta is free at the root; instead compare the mu12-CONSISTENT Re(Hd_12):
Re12 = (pm sqrt(mu12 - st^2.ct^2.(d2-d1)^2 ... )) - messy. Simpler: at each
root, compute the implied mixed-loop cosine and check |cos| <= 1, and
compare mu12 predicted from chart phases (certificate identity).
"""
import json, math, sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../checkers')
import wp7_ensemble as wp7

MASSES2 = {'u': 7.04e-6**2, 'c': 3.56e-3**2, 't': 0.967**2}
recs = json.load(open('results/wp20_valley_audit.json'))['records']
sel_margin = []
cert_mu12 = 0.0
n3 = 0
for r in recs:
    mu, md = r['member']; s_, i, j = r['phase_edge']
    th = np.array(r['log_mags'] + [r['phi_raw']])
    Yu, Yd = wp7.build_texture(mu, md, s_, (i, j), th)
    Hu = Yu @ Yu.conj().T
    off, k = min((max(abs(Hu[a, b]) for b in range(3) if b != a), a) for a in range(3))
    if off > 1e-8: continue
    blk = [x for x in range(3) if x != k]
    t = abs(0.5*math.atan2(2*Hu[blk[0], blk[1]].real, Hu[blk[1], blk[1]].real - Hu[blk[0], blk[0]].real))
    t = min(t, math.pi/2 - t)
    if t <= 1e-9: continue
    anchor = min(MASSES2, key=lambda m: abs(Hu[k, k].real/MASSES2[m]-1))
    Hd0 = Yd @ Yd.conj().T
    best = None
    for blko in (blk, blk[::-1]):
        P = np.zeros((3, 3)); P[0, k] = 1; P[1, blko[0]] = 1; P[2, blko[1]] = 1
        HuC = P @ Hu @ P.T; Hd = P @ Hd0 @ P.T
        if best is None or abs(Hd[0, 1]) < abs(best[1][0, 1]): best = (HuC, Hd)
    HuC, Hd = best
    if abs(Hd[0,1]) < 1e-10 or abs(Hd[1,2])**2 < 1e-40: continue
    n3 += 1
    s = HuC[0, 0].real
    eu, Uu = np.linalg.eigh(HuC); ed, Ud = np.linalg.eigh(Hd)
    oe = np.argsort(eu); Uu = Uu[:, oe]; eu = eu[oe]
    od = np.argsort(ed); Ud = Ud[:, od]; ed = ed[od]
    Vc = Uu.conj().T @ Ud
    kpos = {'u': 0, 'c': 1, 't': 2}[anchor]
    um = np.abs(Vc[kpos, :])**2
    e1, e2, e3 = ed.sum(), ed[0]*ed[1]+ed[0]*ed[2]+ed[1]*ed[2], ed[0]*ed[1]*ed[2]
    d0 = float((um*ed).sum()); beta = float(e3*(um/ed).sum())
    e1p = e1 - d0
    K1 = beta + d0*e1p - e2
    K2 = d0*beta - e3
    d1c, d2c = Hd[1,1].real, Hd[2,2].real
    xc, v2c, w2c = abs(Hd[0,1])**2, abs(Hd[0,2])**2, abs(Hd[1,2])**2
    a_, b_, c_ = HuC[1,1].real, HuC[2,2].real, HuC[1,2]
    th2 = 0.5*math.atan2(2*c_.real, b_ - a_)
    ct, st = math.cos(th2), math.sin(th2)
    chat = c_/abs(c_)
    Hm = Vc @ np.diag(ed) @ Vc.conj().T
    rows = [kpos] + [z for z in range(3) if z != kpos]
    HmC = Hm[np.ix_(rows, rows)]
    m01, m02 = HmC[0,1], HmC[0,2]
    x = ct**2*abs(m01)**2 + st**2*abs(m02)**2 - 2*ct*st*(chat*m01.conjugate()*m02).real
    v2 = K1 - x
    mu12 = abs(HmC[1,2])**2
    loop = Hd[0,1]*Hd[1,2]*Hd[2,0]
    Ls = 2*loop.imag
    # mu12 certificate: physical mu12 vs chart-rotation formula
    re12, im12 = Hd[1,2].real, Hd[1,2].imag
    mu12_pred = (st*ct*(d2c-d1c) + (ct**2-st**2)*re12)**2 + im12**2
    cert_mu12 = max(cert_mu12, abs(mu12/mu12_pred - 1))
    # quadratic roots
    B1 = v2 - x; B0 = e1p*x - K2
    A2 = B1**2 + 4*x*v2; A1 = 2*B1*B0 - 4*x*v2*e1p; A0 = B0**2 + Ls**2 + 4*x*v2*beta
    disc = A1**2 - 4*A2*A0
    if disc < 0: continue
    rts = [(-A1 + math.sqrt(disc))/(2*A2), (-A1 - math.sqrt(disc))/(2*A2)]
    # at each root, Im(Hd_12)^2 from mu12 must be >= 0:
    # mu12 = [st.ct.(d2-d1) + (ct^2-st^2).Re12]^2 + Im12^2 AND w2 = Re12^2+Im12^2
    # solve for Re12: let u = Re12; (st.ct.(d2-d1) + (ct2-st2).u)^2 + w2 - u^2 = mu12
    # linear-in-u after expansion: 2.st.ct.(d2-d1).(ct2-st2).u + st^2.ct^2.(d2-d1)^2
    #   + ((ct2-st2)^2 - 1).u^2 + w2 - mu12 = 0; use (ct2-st2)^2-1 = -4st^2ct^2... it's
    # quadratic in u; simpler: discriminant feasibility check via Im12^2 >= 0 at the
    # u that satisfies; brute: solve quadratic in u.
    def feasible(d1):
        d2 = e1p - d1
        w2 = d1*d2 - beta
        if w2 < 0: return False, None
        A = (ct**2-st**2)**2 - 1.0
        B = 2*st*ct*(d2-d1)*(ct**2-st**2)
        Cc = st**2*ct**2*(d2-d1)**2 + w2 - mu12
        dd = B**2 - 4*A*Cc
        if dd < 0: return False, None
        u = (-B + math.sqrt(dd))/(2*A) if abs(A) > 1e-300 else -Cc/B
        im2 = w2 - u*u
        return im2 >= -1e-30, (u, im2)
    ok_near, sol_near = feasible(min(rts, key=lambda z: abs(z-d1c)))
    ok_far, sol_far = feasible(max(rts, key=lambda z: abs(z-d1c)))
    sel_margin.append((ok_near, ok_far))
nn = len(sel_margin)
both = sum(1 for a, b in sel_margin if a and b)
near_only = sum(1 for a, b in sel_margin if a and not b)
far_only = sum(1 for a, b in sel_margin if b and not a)
print(f'S3 sheets {n3}; mu12 certificate: {cert_mu12:.2e}')
print(f'mu12 feasibility: near-only {near_only}, far-only {far_only}, both {both}, neither {nn-near_only-far_only-both}')
