"""Scratch validation for the rung-3 memory checker design (not a checker).

Validates every closed form / witness value / operator identity planned for
subsubleading_memory_exact_checks.py before the stable IDs are written.
"""
import sympy as sp

u, om, t, eps = sp.symbols("u om t eps")
z, zb = sp.symbols("z zb")
I = sp.I
pi = sp.pi

ok = []
def rep(name, cond, extra=""):
    ok.append(bool(cond))
    print(("PASS" if cond else "FAIL"), name, extra)

# ---------------- M1: witness F = (2+u)/(1+u^2)^2
F = (2 + u) / (1 + u ** 2) ** 2
I1i = sp.atan(u) + (2 * u - 1) / (2 * (1 + u ** 2))          # antiderivative
M1i = sp.atan(u) / 2 - (u + 2) / (2 * (1 + u ** 2))
I1 = lambda U: I1i.subs(u, U) + pi / 2
M1 = lambda U: M1i.subs(u, U) + pi / 4
rep("M1 cert I1", sp.simplify(sp.diff(I1i, u) - F) == 0)
rep("M1 cert M1", sp.simplify(sp.diff(M1i, u) - u * F) == 0)
I1inf = sp.integrate(F, (u, -sp.oo, sp.oo))
M1inf = sp.integrate(u * F, (u, -sp.oo, sp.oo))
rep("M1 I1(inf)=pi", I1inf == pi, f"= {I1inf}")
rep("M1 M1(inf)=pi/2", M1inf == pi / 2, f"= {M1inf}")
I2i = (u - sp.Rational(1, 2)) * sp.atan(u) + pi * u / 2 + 1 - pi / 4
rep("M1 I2 = U I1 - M1 identically",
    sp.simplify(sp.expand(I2i - (u * I1(u) - M1(u)))) == 0)
# drift control: I2(U) - U*I1(inf) -> -pi/2
drift_lim = sp.limit(sp.expand(I2i - u * pi), u, sp.oo)
rep("M1 drift: I2 - pi U -> -pi/2", drift_lim == -pi / 2, f"= {drift_lim}")
# falloff class: u^3 F -> 1
rep("M1 falloff u^3 F -> 1", sp.limit(u ** 3 * F, u, sp.oo) == 1)

# drift-free witness F0 = d/du[2u/(1+u^2)^2]
R0 = 2 * u / (1 + u ** 2) ** 2
F0 = sp.diff(R0, u)
rep("M1.6 I1(inf)=0", sp.integrate(F0, (u, -sp.oo, sp.oo)) == 0)
M1_0 = u * R0 + 1 / (1 + u ** 2)   # int u F0 from -inf (rational!)
rep("M1.6 cert", sp.simplify(sp.diff(M1_0, u) - u * F0) == 0)
rep("M1.6 M1_0(-inf)=0", sp.limit(M1_0, u, -sp.oo) == 0)
I2_0 = sp.integrate(u ** 2 * F0, (u, -sp.oo, sp.oo))
rep("M1.6 I2(inf) = -2 pi", I2_0 == -2 * pi, f"= {I2_0}")

# ---------------- M2: Gaussian witness F = u exp(-u^2)
Fg = u * sp.exp(-u ** 2)
mu = {n: sp.integrate(u ** n * Fg, (u, -sp.oo, sp.oo)) for n in range(6)}
print("gaussian moments:", mu)
Fhat = I * om * sp.sqrt(pi) / 2 * sp.exp(-om ** 2 / 4)
s1 = sp.series(Fhat, om, 0, 6).removeO().expand()
s2 = sum((I * om) ** n * mu[n] / sp.factorial(n) for n in range(6)).expand()
rep("M2.1 series match through om^5", sp.simplify(s1 - s2) == 0)
P2 = lambda f: sp.simplify(f + om * sp.diff(f, om))
P3 = lambda f: sp.simplify(2 * f + om * sp.diff(f, om))
a, b, c0, c1 = sp.symbols("a b c0 c1")
lad = P3(P2(a / om ** 2 + b / om + c0 + c1 * om))
rep("M2.2 packet ladder -> 2 c0 + 6 c1 om", sp.simplify(lad - 2 * c0 - 6 * c1 * om) == 0,
    f"= {lad}")
FPR = lambda f: sp.simplify(sp.diff(f + om * sp.diff(f, om), om))  # d_om(1+om d_om)
fpr_series = FPR(a / om + c0 + c1 * om)
rep("M2.3 FPR ladder kills a/om, c0; extracts 2 c1", sp.simplify(fpr_series - 2 * c1) == 0,
    f"= {fpr_series}")
comp = FPR(P3(P2(a / om ** 2 + b / om + c0 + c1 * om)))
rep("M2.4 composite extracts 12 c1", sp.simplify(comp - 12 * c1) == 0, f"= {comp}")

# ---------------- M3: witness C = u^3 (1-u)^3 on [0,1]
C = u ** 3 * (1 - u) ** 3
N = sp.diff(C, u)
iC = sp.integrate(C, (u, 0, 1))
iuC = sp.integrate(u * C, (u, 0, 1))
N1 = sp.integrate(u * N, (u, 0, 1))
N2 = sp.integrate(u ** 2 * N, (u, 0, 1)) / 2
rep("M3.1 half int u^2 N = -1/280", N2 == sp.Rational(-1, 280), f"= {N2}")
rep("M3.1 -int u C = -1/280", -iuC == sp.Rational(-1, 280))
rep("M3.3 int C = 1/140, N1 = -1/140", iC == sp.Rational(1, 140) and N1 == sp.Rational(-1, 140))
r = sp.symbols("r")
Da0 = (3 * N2 - 1 * N1) / (2 * r)
rep("M3.3 Da0 = -1/(560 r)", sp.simplify(Da0 - sp.Rational(-1, 560) / r) == 0, f"= {Da0}")
I2w = sp.integrate(C, (u, 0, u))                     # I_2 primitive on [0,1]
I3w = sp.integrate(I2w, (u, 0, u))
I3after = sp.Rational(1, 280) + (u - 1) / 140        # for U >= 1
rep("M3.4 I3(1) = 1/280", sp.simplify(I3w.subs(u, 1) - sp.Rational(1, 280)) == 0)
fp_combo = I3after - u * sp.Rational(1, 140) + u ** 2 / 2 * 0
rep("M3.4 FP[I3] = -1/280 = N2", sp.simplify(fp_combo - sp.Rational(-1, 280)) == 0)
# FPR t-hat linear: d/du [I3 - u I2 + u^2/2 I1] = u^2/2 N
I1w = C
combo = I3w - u * I2w + u ** 2 / 2 * I1w
rep("M7.6 d/du combo = u^2/2 N", sp.simplify(sp.diff(combo, u) - u ** 2 / 2 * N) == 0)

# ---------------- M7: spin calculus (G24 conventions)
sq2 = sp.sqrt(2)
Q = (1 + z * zb) / sq2

def eth(f, s):
    return sp.simplify(Q * (sp.diff(f, z) + s * zb / (1 + z * zb) * f))

def ethb(f, s):
    return sp.simplify(Q * (sp.diff(f, zb) - s * z / (1 + z * zb) * f))

def ethn(f, s, n):   # eth^n starting at spin s
    for i in range(n):
        f = eth(f, s + i)
    return sp.simplify(f)

def ethbn(f, s, n):
    for i in range(n):
        f = ethb(f, s - i)
    return sp.simplify(f)

def xhat(i):
    return [(z + zb) / (1 + z * zb), -I * (z - zb) / (1 + z * zb),
            (1 - z * zb) / (1 + z * zb)][i]

Y10 = xhat(2)
Y11 = (xhat(0) + I * xhat(1)) / 1
Y22 = (xhat(0) + I * xhat(1)) ** 2
Y21 = (xhat(0) + I * xhat(1)) * xhat(2)
Y20 = xhat(2) ** 2 - sp.Rational(1, 3) * sum(xhat(i) ** 2 for i in range(3))
Y32 = (xhat(0) + I * xhat(1)) ** 2 * xhat(2)
Y33 = (xhat(0) + I * xhat(1)) ** 3

def lam(a, l):  # (l-s)(l+s+1)/2 with s=a
    return sp.Rational((l - a) * (l + a + 1), 2)

def lam_bar(a, l):  # (l+s)(l-s+1)/2
    return sp.Rational((l + a) * (l - a + 1), 2)

tests = [(Y11, 1), (Y10, 1), (Y22, 2), (Y21, 2), (Y20, 2), (Y32, 3), (Y33, 3)]
allgood = True
for Y, l in tests:
    for s in range(-min(l, 2), min(l, 2) + 1):
        if s >= 0:
            Ys = ethn(Y, 0, s)
        else:
            Ys = ethbn(Y, 0, -s)
        e1 = sp.simplify(ethb(eth(Ys, s), s + 1) + lam(s, l) * Ys)   # b d + (l-s)(l+s+1)/2
        e2 = sp.simplify(eth(ethb(Ys, s), s - 1) + lam_bar(s, l) * Ys)
        if e1 != 0 or e2 != 0:
            allgood = False
            print("  eigen FAIL", l, s, sp.sstr(e1)[:80], sp.sstr(e2)[:80])
rep("M7.1 G24 (2.15a/b) on l=1,2,3 harmonics", allgood)

# eth^4 on _{-2}Y vs _{+2}Y, ratio = (l-1)l(l+1)(l+2)/4
for Y, l in [(Y22, 2), (Y21, 2), (Y32, 3), (Y33, 3)]:
    Ym2 = ethbn(Y, 0, 2)
    Yp2 = ethn(Y, 0, 2)
    e4 = ethn(Ym2, -2, 4)
    ratio = sp.simplify(e4 / Yp2)
    Lam = sp.Rational((l - 1) * l * (l + 1) * (l + 2), 4)
    rep(f"M7.2 eth^4 eigenvalue l={l}", ratio == Lam, f"ratio = {ratio}, Lambda = {Lam}")

# D_z^4 T2 = P^6 eth^4(P^{-2} T2)
Gam = -2 * zb / (1 + z * zb)
P = sq2 / (1 + z * zb)
def Dz(f, s):
    return sp.diff(f, z) - s * Gam * f
T2 = (z ** 3 + z * zb) / (1 + z * zb) ** 3
lhs = T2
for s in (2, 3, 4, 5):
    lhs = sp.simplify(Dz(lhs, s))
rhs = sp.simplify(P ** 6 * ethn(sp.simplify(P ** -2 * T2), 2, 4))
rep("M7.4 D_z^4 T2 = P^6 eth^4(P^-2 T2)", sp.simplify(lhs - rhs) == 0)

# sigma commutation: sigma(eth_s f) = ethb_{-s} sigma(f)
SIG = [(z, zb), (zb, z)]
def sigma(e):
    return e.subs(SIG, simultaneous=True).subs(I, -I)
ftest = (z ** 2 + zb) / (1 + z * zb) ** 2
rep("M4.3 sigma(eth_s f) = ethb_-s sigma(f)",
    sp.simplify(sigma(eth(ftest, 1)) - ethb(sigma(ftest), -1)) == 0)

# ---------------- M4: divergence-free X from chi, parity
eps_up_zzb = -I / (2 / (1 + z * zb) ** 2)   # epsilon^{z zb} = -i/gamma
gmet = 2 / (1 + z * zb) ** 2
for chi_idx, chi in enumerate([(z * zb) / (1 + z * zb), (z + zb) / (1 + z * zb) + z * zb / (1 + z * zb) ** 2]):
    Xz_up = sp.simplify(eps_up_zzb * sp.diff(chi, zb))
    Xzb_up = sp.simplify(-eps_up_zzb * sp.diff(chi, z))
    div = sp.simplify(sp.diff(Xz_up, z) + Gam * Xz_up
                      + sp.diff(Xzb_up, zb) + (-2 * z / (1 + z * zb)) * Xzb_up)
    rep(f"M4.1 D_A X^A = 0 (chi witness)", div == 0)
    rep("M4.1b reality sigma(X^z) = X^zb",
        sp.simplify(sigma(Xz_up) - Xzb_up) == 0)
    X_z = sp.simplify(gmet * Xzb_up)       # X_z = gamma X^zb
    X_zb = sp.simplify(gmet * Xz_up)       # X_zb = gamma X^z
    Gamz = -2 * zb / (1 + z * zb)          # Gamma^z_zz
    Gamb = -2 * z / (1 + z * zb)           # Gamma^zb_zbzb
    YE_zz = sp.simplify(sp.diff(X_z, z) - Gamz * X_z)        # D_z X_z
    YE_zbzb = sp.simplify(sp.diff(X_zb, zb) - Gamb * X_zb)   # D_zb X_zb
    rep("M4.2 sigma(YE_zz) = YE_zbzb (electric even)",
        sp.simplify(sigma(YE_zz) - YE_zbzb) == 0)
    # magnetic: X'^A = d^A chi (gradient), YM_zz = i D_z X'_z
    gmet_inv = sp.simplify(1 / gmet)
    Xpz_up = sp.simplify(gmet_inv * sp.diff(chi, zb))
    Xpzb_up = sp.simplify(gmet_inv * sp.diff(chi, z))
    Xp_z = sp.simplify(gmet * Xpzb_up)
    Xp_zb = sp.simplify(gmet * Xpz_up)
    YM_zz = sp.simplify(I * (sp.diff(Xp_z, z) - Gamz * Xp_z))
    YM_zbzb = sp.simplify(I * (sp.diff(Xp_zb, zb) - Gamb * Xp_zb))
    # note: traceless Hessians vanish for l <= 1 scalars (eth^2 0Y_1m = 0),
    # so nontriviality is only asserted for the l=2-containing witness
    if chi_idx == 1:
        rep("M4.2 YE nonzero (l=2 witness)", sp.simplify(YE_zz) != 0)
        rep("M4.2 YM nonzero (l=2 witness)", sp.simplify(YM_zz) != 0)
    rep("M4.2 sigma(YM_zz) = -YM_zbzb (magnetic odd)",
        sp.simplify(sigma(YM_zz) + YM_zbzb) == 0)

# ---------------- M6: pseudo-flux scaling
# G24 (3.14)-(3.16): F^nonrad = -3 d/du(m sigma)  [bilinear m*sigma -> O(eps^2)]
#                    F^rad    = -3i d/du(sigma Im[eth^2 barsigma])  [quadratic -> O(eps^2)]
#                    F_{2,0}  = -3 sigma^2 barsigma_dot  [cubic -> O(eps^3)]
# sig_field carries spin +2 (so barsigma spin -2 and eth^2 barsigma is spin 0).
mv = sp.Symbol("mv")   # non-radiative data marker
sig_field = eps * u ** 2 * (1 - u) ** 2 * z ** 2 / (1 + z * zb) ** 2
m_field = eps * mv * u * (1 - u)
sigbar = sigma(sig_field)
eth2_sigbar = ethn(sigbar, -2, 2)
ImPart = sp.simplify((eth2_sigbar - sigma(eth2_sigbar)) / (2 * I))  # Im[eth^2 barsigma], sigma-real
rep("M6 Im[eth^2 barsigma] is sigma-real", sp.simplify(sigma(ImPart) - ImPart) == 0)
rep("M6 ImPart nonzero", ImPart != 0)
Frad = sp.simplify(-3 * I * sp.diff(sig_field * ImPart, u))
Fnon = sp.simplify(-3 * sp.diff(m_field * sig_field, u))
F20 = sp.simplify(-3 * sig_field ** 2 * sp.diff(sigbar, u))
for nm, fx, deg in [("Frad", Frad, 2), ("Fnonrad", Fnon, 2), ("F20", F20, 3)]:
    fe = sp.expand(fx)
    low_vanish = all(sp.simplify(fe.coeff(eps, k)) == 0 for k in range(deg))
    lead = sp.simplify(fe.coeff(eps, deg))
    rep(f"M6 {nm}: eps^{{0..{deg - 1}}}=0, eps^{deg} != 0", low_vanish and lead != 0)
# radiative vs non-radiative content (G24 text after (3.16))
rep("M6 Fnonrad vanishes without m", sp.simplify(Fnon.subs(mv, 0)) == 0)
rep("M6 Frad independent of m and nonzero",
    sp.simplify(Frad.subs(mv, 0) - Frad) == 0 and Frad != 0)
# total-derivative structure of the F_{2,1} fluxes: burst integral collapses to
# boundary values, which vanish for the compact-support witness shear
rep("M6 int_0^1 Frad = 0 (total derivative)",
    sp.simplify(sp.integrate(Frad, (u, 0, 1))) == 0)
rep("M6 int_0^1 Fnonrad = -3 [m sigma]_0^1 = 0 (total derivative)",
    sp.simplify(sp.integrate(Fnon, (u, 0, 1))) == 0)

print(f"\n{sum(ok)}/{len(ok)} scratch checks passed")
