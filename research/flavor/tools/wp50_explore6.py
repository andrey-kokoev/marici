"""WP50 explore 6: complex-frame mu12 certificate + S3 branch rule.

True block eigenbasis for Hermitian [[a,c],[c*,b]], c = |c|.exp(i.psi):
col1 = (ct, st.e^{i.psi}), col2 = (-st, ct.e^{i.psi}) embedded with singlet.
Then mu12 = [st.ct.(d2-d1) + (ct^2-st^2).Re(Z)]^2 + Im(Z)^2, Z = e^{i.psi}.Hd_12.
Certificate: physical |HmC_12|^2 (eigh) vs formula. Branch rule: is the
chart d1 root always the quadratic root nearer to the family-limit
estimate d1^0 = K2/v2?
"""
import json, math, sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../checkers')
import wp7_ensemble as wp7

MASSES2 = {'u': 7.04e-6**2, 'c': 3.56e-3**2, 't': 0.967**2}
recs = json.load(open('results/wp20_valley_audit.json'))['records']
cert_mu12 = 0.0
branch = {'near_d10': 0, 'far_d10': 0}
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
    psi = math.atan2(c_.imag, c_.real)
    th2 = 0.5*math.atan2(2*abs(c_), a_ - b_)
    ct, st = math.cos(th2), math.sin(th2)
    # complex-frame check: U columns (singlet, v1, v2)
    eps = 1j
    U = np.array([[1, 0, 0],
                  [0, ct, -st],
                  [0, st*complex(math.cos(-psi), math.sin(-psi)),
                   ct*complex(math.cos(-psi), math.sin(-psi))]], complex)
    X = U.conj().T @ Hd @ U
    # X should be diagonal in the block up to eigh agreement; check offdiag of X.Hu:
    Yh = U.conj().T @ HuC @ U
    frame_err = abs(Yh[1,2])
    Z = complex(math.cos(-psi), math.sin(-psi))*Hd[1,2]
    mu12_pred = (st*ct*(d2c-d1c) + (ct**2-st**2)*Z.real)**2 + Z.imag**2
    mu12_eigh = abs(X[1,2])**2
    cert_mu12 = max(cert_mu12, abs(mu12_pred/mu12_eigh - 1), frame_err/max(eu))
    # branch rule
    x = ct**2*abs((U.conj().T @ Hd)[0,1])**2 + 0  # not needed; use K1 split via x formula:
    chat = c_/abs(c_)
    Hm = Vc @ np.diag(ed) @ Vc.conj().T
    rows = [kpos] + [z for z in range(3) if z != kpos]
    HmC = Hm[np.ix_(rows, rows)]
    m01, m02 = HmC[0,1], HmC[0,2]
    x = ct**2*abs(m01)**2 + st**2*abs(m02)**2 - 2*ct*st*(chat*m01.conjugate()*m02).real
    v2 = K1 - x
    loop = Hd[0,1]*Hd[1,2]*Hd[2,0]
    Ls = 2*loop.imag
    B1 = v2 - x; B0 = e1p*x - K2
    A2 = B1**2 + 4*x*v2; A1 = 2*B1*B0 - 4*x*v2*e1p; A0 = B0**2 + Ls**2 + 4*x*v2*beta
    disc = A1**2 - 4*A2*A0
    if disc < 0: continue
    rts = [(-A1 + math.sqrt(disc))/(2*A2), (-A1 - math.sqrt(disc))/(2*A2)]
    d10 = K2/v2
    near_chart = min(rts, key=lambda z: abs(z - d1c))
    near_d10 = min(rts, key=lambda z: abs(z - d10))
    branch['near_d10' if abs(near_chart - near_d10) < 1e-30*max(1,abs(d1c)) or near_chart is near_d10 else 'far_d10'] += 1
print('S3 complex-frame mu12 certificate + HuC block diag err:', f'{cert_mu12:.2e}')
print('branch rule (chart root == root nearer K2/v2):', branch)
