"""WP50 explore 1: complement-family chart entries vs physical invariants.

On complement sheets (Hd_01 != 0) the family inversion breaks: the loop
product L = 2 Re(Hd_01 Hd_12 Hd_02*) survives in det(Hd). Map out:

  T1 d0 = sum u.lam exact on complement?        (singlet spectral diagonal)
  T2 beta = e3.sum u/lam = M_00 exact?          ((0,0) minor)
  T3 K1 := |Hd_01|^2 + |Hd_02|^2 = beta + d0.e1' - e2 exact?
  T4 family d1 formula failure size on complement
  T5 chain q = J.blockgap.Dd/(v^2 sqrt(w^2)) on complement (WP48 G2 was
     family-only)
  T6 loop sine: Ls = 2 Im(Hd_01 Hd_12 Hd_02*) vs commutator invariant
     A = Im Tr[HuC,Hd]^3 - find the exact proportionality factor.
"""
import json, math, sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../checkers')
import wp7_ensemble as wp7

MASSES2 = {'u': 7.04e-6**2, 'c': 3.56e-3**2, 't': 0.967**2}

def fold(p):
    p = abs(p) % math.pi
    return math.pi - p if p > math.pi/2 else p

recs = json.load(open('results/wp20_valley_audit.json'))['records']
t1 = t2 = t3 = t5 = 0.0
fam_d1_err = 0.0
ratios = []
nf = nx = 0
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
    fam = abs(Hd[0, 1]) < 1e-10
    if fam:
        nf += 1
        continue
    nx += 1
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
    d0c, d1c, d2c = Hd[0,0].real, Hd[1,1].real, Hd[2,2].real
    xc, v2c, w2c = abs(Hd[0,1])**2, abs(Hd[0,2])**2, abs(Hd[1,2])**2
    loop = Hd[0,1]*Hd[1,2]*Hd[2,0]
    Lc, Ls = 2*loop.real, 2*loop.imag
    t1 = max(t1, abs(d0/d0c - 1))
    t2 = max(t2, abs(beta/(d1c*d2c - w2c) - 1))
    K1 = beta + d0*e1p - e2
    t3 = max(t3, abs(K1/(xc + v2c) - 1))
    d1fam = (beta*d0 - e3)/(e1p*d0 - e2 + beta)
    fam_d1_err = max(fam_d1_err, abs(d1fam/d1c - 1))
    # T5 chain on complement
    nonsing = sorted(eu, key=lambda x: abs(x - s))[1:]
    blockgap = abs(nonsing[1] - nonsing[0])
    Dd = (ed[2]-ed[1])*(ed[2]-ed[0])*(ed[1]-ed[0])
    q = HuC[1,2].real*0 + abs(HuC[1,2])*math.sin(fold(th[-1]))
    q_chain = r['J']*blockgap*Dd/(v2c*math.sqrt(w2c))
    t5 = max(t5, abs(q_chain/q - 1))
    # T6 commutator vs loop sine
    C = HuC @ Hd - Hd @ HuC
    A = (np.trace(C @ C @ C)).imag/6.0
    cc = HuC[1,2]
    factor = (cc*cc).imag  # candidate: Im(c^2) carries the Hu loop phase
    B = Ls*0.5*factor if abs(factor) > 0 else float('nan')
    ratios.append((A, Ls, cc, factor))

print(f'family {nf}, complement {nx}')
print(f'T1 d0 exact:        {t1:.2e}')
print(f'T2 beta=M00 exact:  {t2:.2e}')
print(f'T3 K1=x+v2 exact:   {t3:.2e}')
print(f'T4 family d1 fails: {fam_d1_err:.2e}')
print(f'T5 chain compl:     {t5:.2e}')
A = np.array([x[0] for x in ratios]); Ls = np.array([x[1] for x in ratios])
# regress A against Ls * candidate factors
for name, f in [('Im(c^2)', [ (x[3]) for x in ratios]),
                ('|c|^2',   [ abs(x[2])**2 for x in ratios]),
                ('1',       [ 1.0 for x in ratios])]:
    f = np.array(f, float)
    den = Ls*f
    ok = np.abs(den) > 1e-300
    if ok.sum() < 10: continue
    rr = A[ok]/den[ok]
    print(f'A / (Ls.{name}): mean {rr.mean():.6e} rel std {rr.std()/abs(rr.mean()):.2e}')
