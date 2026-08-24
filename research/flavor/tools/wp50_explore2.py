"""WP50 explore 2: closing the complement inversion.

Certify per complement sheet:
  (b) x = |Hd_01|^2 from up-mass-basis data:
      Hm = V.diag(lam).V^+ (up-mass basis, physical), block rotation
      (ct,st) from Hu block, chat = HuC[1,2]/|HuC[1,2]|;
      x = ct^2.|Hm_01|^2 + st^2.|Hm_02|^2 + 2 ct st Re(chat.Hm_01*.Hm_02)
      (check BOTH sign/orientation conventions, report best)
  (c) general d1 quadratic: with v2 = K1 - x, w2 = d1.d2 - beta,
      L = d1(v2-x) + e1'x - K2, Ls chart: residual of
      L^2 + Ls^2 - 4.x.v2.w2 = 0 at chart d1 (algebra identity),
      then solve the quadratic given (x, Ls) and check the chart d1 is a
      root; report the second root and a physical root-selection rule.
      Family limit: d1 = K2/v2 vs WP49 linear formula.
  (d) Ls from J: mixed loop M = c.Hd_01.Hd_02* (c = HuC[1,2]);
      Im Tr[HuC,Hd]^3 = f . Im(M)? find exact f via per-sheet ratio;
      also Re(M) vs Tr(HuC.Hd^2)-type CP-even invariants.
  (e) WP48 chain q = J.blockgap.Dd/(v^2 sqrt(w^2)) on complement,
      guarding tiny v2/w2 (report stratum sizes).
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
err = {k: 0.0 for k in ('x', 'quad', 'fam', 'chain')}
roots_other = []
mix = []
strata = {'ok': 0, 'tiny_v2': 0, 'tiny_w2': 0}
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
    d0c, d1c, d2c = Hd[0,0].real, Hd[1,1].real, Hd[2,2].real
    xc, v2c, w2c = abs(Hd[0,1])**2, abs(Hd[0,2])**2, abs(Hd[1,2])**2
    loop = Hd[0,1]*Hd[1,2]*Hd[2,0]
    Lc, Ls = 2*loop.real, 2*loop.imag
    if fam:
        err['fam'] = max(err['fam'], abs((K2/K1)/d1c - 1))
        continue
    # (b) x from up-mass-basis data
    a_, b_, c_ = HuC[1,1].real, HuC[2,2].real, HuC[1,2]
    th2 = 0.5*math.atan2(2*c_.real, b_ - a_)
    ct, st = math.cos(th2), math.sin(th2)
    chat = c_/abs(c_)
    Hm = Vc @ np.diag(ed) @ Vc.conj().T  # up-mass basis (sorted)
    m01, m02 = Hm[kpos, (kpos+1)%3], Hm[kpos, (kpos+2)%3]
    # the two block rows of Hm in sorted order are the non-kpos rows;
    # rebuild in canonical (singlet-first) frame ordering:
    rows = [kpos] + [x for x in range(3) if x != kpos]
    HmC = Hm[np.ix_(rows, rows)]
    m01, m02 = HmC[0,1], HmC[0,2]
    # convention scan: Hd_flavor row0 = R row0 rotated: try 4 forms
    cands = {
        'A': ct**2*abs(m01)**2 + st**2*abs(m02)**2 + 2*ct*st*(chat*m01.conjugate()*m02).real,
        'B': st**2*abs(m01)**2 + ct**2*abs(m02)**2 - 2*ct*st*(chat*m01.conjugate()*m02).real,
        'C': ct**2*abs(m01)**2 + st**2*abs(m02)**2 - 2*ct*st*(chat*m01.conjugate()*m02).real,
        'D': st**2*abs(m01)**2 + ct**2*abs(m02)**2 + 2*ct*st*(chat*m01.conjugate()*m02).real,
    }
    bestc = min(cands, key=lambda z: abs(cands[z]/xc - 1) if xc > 0 else 0)
    if xc > 1e-300:
        err['x'] = max(err['x'], abs(cands[bestc]/xc - 1))
    x = cands[bestc]
    v2 = K1 - x
    # (c) quadratic residual at chart d1
    Lchart = d1c*(v2c - xc) + e1p*xc - K2
    err['quad'] = max(err['quad'], abs((Lchart - Lc)/max(abs(Lc), 1e-300)) if abs(Lc) > 0 else abs(Lchart))
    # solve quadratic for d1 given (x, v2, Ls): A2 d1^2 + A1 d1 + A0 = 0
    # [d1(v2-x) + e1'x - K2]^2 + Ls^2 = 4 x v2 (d1(e1'-d1) - beta)
    B1 = v2 - x; B0 = e1p*x - K2
    A2 = B1**2 + 4*x*v2; A1 = 2*B1*B0 - 4*x*v2*e1p; A0 = B0**2 + Ls**2 + 4*x*v2*beta
    disc = A1**2 - 4*A2*A0
    if disc >= 0:
        rts = [(-A1 + math.sqrt(disc))/(2*A2), (-A1 - math.sqrt(disc))/(2*A2)]
        d_near = min(rts, key=lambda z: abs(z - d1c))
        rel = abs(d_near/d1c - 1)
        err.setdefault('d1quad', 0.0)
        err['d1quad'] = max(err['d1quad'], rel)
        roots_other.append(abs(max(rts, key=lambda z: abs(z-d1c))/d1c - 1) if abs(d1c) > 0 else 0.0)
    # (d) mixed loop vs commutator
    C = HuC @ Hd - Hd @ HuC
    T3 = np.trace(C @ C @ C)
    M = c_*Hd[0,1]*Hd[0,2].conjugate()
    mix.append((T3, M, eu, ed, anchor, Ls, loop, c_))
    # (e) chain
    if v2c > 1e-40 and w2c > 1e-40:
        nonsing = sorted(eu, key=lambda z: abs(z - s))[1:]
        blockgap = abs(nonsing[1] - nonsing[0])
        Dd = (ed[2]-ed[1])*(ed[2]-ed[0])*(ed[1]-ed[0])
        q = abs(HuC[1,2])*math.sin(fold(th[-1]))
        q_chain = r['J']*blockgap*Dd/(v2c*math.sqrt(w2c))
        err['chain'] = max(err['chain'], abs(q_chain/q - 1))
        strata['ok'] += 1
    else:
        strata['tiny_v2' if v2c <= 1e-40 else 'tiny_w2'] += 1

print('family d1 = K2/K1 (WP49 linear) max rel err:', f"{err['fam']:.2e}")
print('(b) x inversion max rel err:', f"{err['x']:.2e}")
print('(c) det-identity residual at chart d1:', f"{err['quad']:.2e}",
      '; quadratic root match:', f"{err.get('d1quad', 0):.2e}",
      '; other-root rel distance: median', f"{np.median(roots_other):.2e}")
print('(e) chain on complement (guarded):', f"{err['chain']:.2e}", strata)
# (d) regressions
T3v = np.array([z[0] for z in mix])
Mv = np.array([z[1] for z in mix])
r1 = T3v/Mv
print('Tr[Hu,Hd]^3 / M: real part mean/std:', f"{r1.real.mean():.3e} {r1.real.std():.3e}",
      '; imag mean/std:', f"{r1.imag.mean():.3e} {r1.imag.std():.3e}")
