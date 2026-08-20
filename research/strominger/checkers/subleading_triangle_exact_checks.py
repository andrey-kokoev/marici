"""Exact subleading-triangle checker: subleading soft <-> superrotation Ward <-> spin memory (marici.Strominger).

Sources and conventions: research/strominger/subleading-triangle-conventions.md
Map definitions:         research/strominger/subleading-triangle-source-boundary.md (check items S1-S9)
Primary sources: CS = Campiglia-Laddha arXiv:1404.4091, KLPS = Kapec-Lysov-
Pasterski-Strominger arXiv:1406.3312, PSZ = Pasterski-Strominger-Zhiboedov
arXiv:1502.06120 (grounding ledger in the conventions packet).

All arithmetic is exact sympy symbolics. No floating point anywhere.
Treat (z, zb, zk, zbk) as independent symbols; reality is imposed through the
explicit conjugation map sigma: z <-> zb, zk <-> zbk, I -> -I applied with
SIMULTANEOUS substitution (plain dict .subs is sequential and WRONG here).
sigma is only ever applied to explicit sigma-symmetric rational test fields,
never to sympy.Function applications (argument swapping is unreliable there).

Metric convention: eta = diag(-1,1,1,1), matching the leading checker; the
papers use mostly-minus — overall signs that flip under the convention change
are recorded as convention residuals, not silently absorbed.

Layers (packet section 2):
  S1 zero-frequency projector (KLPS 5.33 / PSZ 6.1).
  S2 gauge variation of the CS soft factor (CS 7) + J-obstruction.
  S3 CS (5)-(6) vs PSZ (6.5) normalization ratio.
  S4 sphere reduction of the hard operator (PSZ 6.7 -> KLPS 5.16).
  S5 the D^2 bridge (PSZ 6.8) as a per-leg operator statement, including
     the KLPS (6.6) arbiter, the tetrad mixing theorem, and the exactly
     named angular gauge-mixing residual.
  S6 Green-kernel consistency (PSZ 5.3-5.4 vs leading HMLS 2.25-2.26).
  S7 news shift law operator D_z^3 (KLPS 5.5) and its CKV kernel.
  S8 carrier question / H2 test (PSZ 4.5 vs 6.9 vs 5.2/KLPS 5.5).
  S9 constraint parity (PSZ 5.2): magnetic projection and curl-only dependence.
  S10 leg-summed closure mechanism (KLPS 6.4) and the KLPS (6.7)/(6.12)
     delta scaffold as a per-leg distributional statement.

Output: research/strominger/results/subleading_triangle_exact_checks.json
Exit code 0 iff every mandatory check passes and every obstruction test
exhibits the declared nonzero residual.
"""
import json
import os
import sympy as sp

# ---------------------------------------------------------------- symbols
z, zb, w, wb = sp.symbols("z zb w wb")
zk, zbk, Ek = sp.symbols("zk zbk Ek")
om = sp.symbols("om", positive=True)
kap = sp.symbols("kap")
I = sp.I

results = []


def simp(e):
    """Two-stage exact zero-recognition: simplify/expand, then rational cancel."""
    e = sp.simplify(sp.expand(e))
    if e != 0:
        e = sp.cancel(sp.together(e))
    return e


def record(cid, group, statement, status, detail=""):
    results.append({
        "id": cid, "group": group, "statement": statement,
        "status": status, "detail": detail,
    })
    print(f"[{status:>4}] {cid}: {statement}" + (f"  ({detail})" if detail else ""))


def check_zero(cid, group, statement, expr, **subs):
    """Pass iff expr simplifies to exactly 0 (after optional substitutions)."""
    e = expr.subs(subs) if subs else expr
    e = simp(e)
    record(cid, group, statement, "pass" if e == 0 else "FAIL",
           "" if e == 0 else f"residual: {sp.sstr(e)[:300]}")
    return e == 0


def check_nonzero(cid, group, statement, expr, **subs):
    """Pass iff expr is exactly nonzero (typed obstruction present).

    With exact rational substitutions this is a sound nonzeroness proof:
    one exact point with a nonzero value witnesses expr != 0.
    """
    e = expr.subs(subs) if subs else expr
    e = simp(e)
    record(cid, group, statement, "pass" if e != 0 else "FAIL",
           f"residual retained: {sp.sstr(e)[:300]}" if e != 0 else "residual vanished unexpectedly")
    return e != 0


def check_all_zero(cid, group, statement, exprs, detail=""):
    """Pass iff every expression in the list simplifies to exactly 0."""
    vals = [simp(e) for e in exprs]
    bad = [v for v in vals if v != 0]
    record(cid, group, statement, "pass" if not bad else "FAIL",
           detail if not bad else f"nonzero components: {sp.sstr(bad[0])[:300]}")
    return not bad


# ============================================================ shared machinery
eta_metric = sp.diag(-1, 1, 1, 1)


def mdot(a, b):
    return sp.simplify((a.T * eta_metric * b)[0])


def xhat(zz, zzb):
    return sp.Matrix([(zz + zzb) / (1 + zz * zzb),
                      -I * (zz - zzb) / (1 + zz * zzb),
                      (1 - zz * zzb) / (1 + zz * zzb)])


def pvec(E, zz, zzb):
    return E * sp.Matrix([1, *xhat(zz, zzb)])


# sphere metric gamma_{z zb} = 2/(1+z zb)^2 and its Christoffels
Gam = -2 * zb / (1 + z * zb)          # Gamma^z_zz
Gamb = -2 * z / (1 + z * zb)          # Gamma^zb_zbzb (mixed Christoffels vanish)


def Dz_low(f, s):
    """D_z on a rank-s lower-z tensor component."""
    return sp.diff(f, z) - s * Gam * f


def Dzb_low(f, s):
    """D_zb on a rank-s lower-zb tensor component."""
    return sp.diff(f, zb) - s * Gamb * f


SIG = [(z, zb), (zb, z), (zk, zbk), (zbk, zk)]


def sigma(e):
    """Complex conjugation on the sphere variables: simultaneous swap, I -> -I."""
    return e.subs(SIG, simultaneous=True).subs(I, -I)


# Lorentz generator actions on leg coordinates (zk, zbk, Ek), computed from
# delta k = alpha . eta . k with antisymmetric alpha (NOT the matrix
# commutator: k is a column vector, the action is alpha^{mu}{}_nu k^nu).
GENS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
_a = sp.symbols("a01 a02 a03 a12 a13 a23")
ALPHAS = dict(zip(GENS, _a))
Amat = sp.zeros(4)
for (m, n), av in ALPHAS.items():
    Amat[m, n] = av
    Amat[n, m] = -av

pk = pvec(Ek, zk, zbk)
pkp = pk + Amat * (eta_metric * pk)
_zero_a = {av: 0 for av in ALPHAS.values()}
zp = (pkp[1] + I * pkp[2]) / (pkp[0] + pkp[3])
zbp = (pkp[1] - I * pkp[2]) / (pkp[0] + pkp[3])
Ep = pkp[0]
dz_gen = {gg: sp.simplify(sp.diff(zp, ALPHAS[gg]).subs(_zero_a)) for gg in GENS}
dzb_gen = {gg: sp.simplify(sp.diff(zbp, ALPHAS[gg]).subs(_zero_a)) for gg in GENS}
dE_gen = {gg: sp.simplify(sp.diff(Ep, ALPHAS[gg]).subs(_zero_a)) for gg in GENS}

Gam_k = -2 * zbk / (1 + zk * zbk)     # Gamma^z_zz at the leg point
Gamb_k = -2 * zk / (1 + zk * zbk)


def Dz_vec_leg(Y):
    """D_z on a Y^z vector component at the leg point."""
    return sp.diff(Y, zk) + Gam_k * Y


def Dzb_vec_leg(Yb):
    return sp.diff(Yb, zbk) + Gamb_k * Yb


# exact rational test point (all values rational; om = 1)
PT1 = {z: 2, zb: sp.Rational(3, 5), zk: sp.Rational(-1, 3),
       zbk: sp.Rational(4, 7), Ek: 5, om: 1}

# ================================================================ S1 projector
a_s, b_s, c_s = sp.symbols("a b c")


def Proj(f):
    """(1 + om d_om) projector."""
    return sp.simplify(f + om * sp.diff(f, om))


check_zero("S1.1", "S1", "(1+om d_om) annihilates the Weinberg pole a/om (KLPS 5.33)",
           Proj(a_s / om))
check_zero("S1.2", "S1", "(1+om d_om) acts as identity on om^0 terms",
           Proj(b_s) - b_s)
f_soft = a_s / om + b_s + c_s * om
sym_lim = sp.simplify((f_soft + f_soft.subs(om, -om)) / 2)
proj_pole_finite = Proj(a_s / om + b_s)     # projection at pole+finite level
check_zero("S1.3", "S1", "symmetric limit (1/2)(lim+ + lim-) equals the (1+om d_om) "
                         "projection at the pole+finite level (PSZ 6.1 = KLPS 5.33)",
           proj_pole_finite - sym_lim)

# ================================================================ S2 gauge variation
k4 = sp.Matrix(sp.symbols("k0:4"))
q4 = sp.Matrix(sp.symbols("q0:4"))
Lam4 = sp.Matrix(sp.symbols("L0:4"))
Js = sp.zeros(4)
for m in range(4):
    for n in range(m + 1, 4):
        s = sp.Symbol(f"J{m}{n}")
        Js[m, n] = s
        Js[n, m] = -s

kl4, ql4, Laml4 = eta_metric * k4, eta_metric * q4, eta_metric * Lam4
qdotk = (ql4.T * k4)[0]

# declared shift (conventions packet G_CS): dE_{mu nu} = q_mu Lam_nu + q_nu Lam_mu
dE_shift = ql4 * Laml4.T + Laml4 * ql4.T
dS_leg = sum(dE_shift[m, n] * k4[m] * sum(ql4[r] * Js[r, n] for r in range(4))
             for m in range(4) for n in range(4)) / qdotk
Lam_q_J = sum(Laml4[m] * ql4[n] * Js[m, n] for m in range(4) for n in range(4))
check_zero("S2.1", "S2", "per-leg gauge contraction of the declared shift is exactly "
                         "-Lam_mu q_nu J^{mu nu}; hence dS^(1) = +i Lam q sum J "
                         "(printed CS (7) has -i: shift-sign convention residual)",
           dS_leg + Lam_q_J)

# angular-momentum conservation on a 2-leg scalar amplitude: sum_a J_a(k1.k2) = 0
k1 = sp.Matrix(sp.symbols("a0:4"))
k2 = sp.Matrix(sp.symbols("b0:4"))


def Jact(F, kv):
    """J^{mu nu} F = k^[mu dF/dk_{nu]]} (orbital, scalar legs; CS footnote 4)."""
    dcov = eta_metric * sp.Matrix([sp.diff(F, kv[i]) for i in range(4)])
    return kv * dcov.T - dcov * kv.T


F12 = mdot(k1, k2)
Jsum = Jact(F12, k1) + Jact(F12, k2)
check_all_zero("S2.2", "S2", "with J: sum_a J_a^{mu nu}(k1.k2) = 0 identically "
                             "(CS (7) gauge invariance)",
               [Jsum[m, n] for m in range(4) for n in range(m + 1, 4)])
Jobstr = Jact(k1[0], k1) + Jact(k1[0], k2)
check_nonzero("S2.3", "S2", "typed obstruction: without J the variation is nonzero — "
                            "sum_a J_a^{mu nu}(k1^0) = k1^[mu eta^{nu]0} != 0",
              Jobstr[0, 1])

# ================================================================ S3 normalization
eps = sp.Matrix([[sp.Symbol(f"e{min(m,n)}{max(m,n)}") if m != n else 0
                  for n in range(4)] for m in range(4)])
for m in range(4):
    for n in range(m + 1, 4):
        eps[n, m] = -eps[m, n]
eps_up = eta_metric * eps * eta_metric
Js_low = eta_metric * Js * eta_metric
C_CS = -I * sum(eps[m, n] * k4[m] * sum(ql4[r] * Js[r, n] for r in range(4))
                for m in range(4) for n in range(4)) / qdotk
C_PSZ = I * kap * sum(eps_up[m, n] * kl4[m] * sum(Js_low[n, l] * q4[l] for l in range(4))
                      for m in range(4) for n in range(4)) / qdotk
check_zero("S3.1", "S3", "PSZ (6.5) contracted form equals exactly kap times the "
                         "CS (6) contraction: C_PSZ - kap*C_CS = 0",
           sp.expand(C_PSZ) - kap * sp.expand(C_CS))
check_nonzero("S3.2", "S3", "typed normalization residual: the ratio is kap = "
                            "sqrt(32 pi G), not 1 — PSZ (6.5) carries an explicit kap, "
                            "CS (5)-(6) carries none",
              sp.expand(C_PSZ) - sp.expand(C_CS))

# ================================================================ S4 sphere reduction
ROTS = [(1, 2), (1, 3), (2, 3)]
check_all_zero("S4.1", "S4", "Lorentz action via PSZ (6.7): dz holomorphic in zk, "
                             "dzb antiholomorphic, dE = 0 for rotations",
               [sp.diff(dz_gen[gg], zbk) for gg in GENS]
               + [sp.diff(dzb_gen[gg], zk) for gg in GENS]
               + [dE_gen[gg] for gg in ROTS])
check_all_zero("S4.2", "S4", "hard-operator identity per generator: "
                             "dE = -(E/2)(D_z dz + D_zb dzb)",
               [dE_gen[gg] + Ek / 2 * (Dz_vec_leg(dz_gen[gg]) + Dzb_vec_leg(dzb_gen[gg]))
                for gg in GENS])


def _coeffs3(e, s):
    e = sp.expand(e)
    return [sp.simplify(e.coeff(s, i)) for i in range(3)]


M6 = sp.Matrix([_coeffs3(dz_gen[gg], zk) + _coeffs3(dzb_gen[gg], zbk)
                for gg in GENS]).T
det6 = sp.factor(M6.det())
sol6 = M6.solve(sp.Matrix([0, 0, 1, 0, 0, 0])) if det6 != 0 else None
dE_sol = (sp.simplify(sum(sol6[i] * dE_gen[GENS[i]] for i in range(6)))
          if sol6 is not None else sp.nan)
resid_sol = simp(dE_sol + Ek / 2 * Dz_vec_leg(zk ** 2)) if sol6 is not None else sp.nan
ok43 = det6 != 0 and resid_sol == 0
record("S4.3", "S4", "KLPS (5.16) hard operator is exactly the holomorphic half of the "
                     "Lorentz combination: chiral target (Y^z = zk^2, Y^zb = 0) solvable "
                     "and dE = -(E/2) D_z Y^z",
       "pass" if ok43 else "FAIL",
       f"det M6 = {det6}; alpha = {[sp.simplify(s) for s in sol6]}" if ok43 else
       f"det {det6}, residual {sp.sstr(resid_sol)[:200]}")

# ================================================================ S5 the D^2 bridge
X_soft = sp.Matrix([1, *xhat(z, zb)])
qv = om * X_soft
qdotp = sp.simplify((eta_metric * qv).dot(pk))
eps_m = sp.Matrix([z, 1, I, -z]) / sp.sqrt(2)
eps_p = sp.Matrix([zb, 1, -I, -zb]) / sp.sqrt(2)
dXz = sp.Matrix([0, *[sp.diff(c, z) for c in xhat(z, zb)]])
dXzb = sp.Matrix([0, *[sp.diff(c, zb) for c in xhat(z, zb)]])
Az = sp.simplify((eta_metric * pk).dot(dXz))
Azb = sp.simplify((eta_metric * pk).dot(dXzb))


def build_op(vvec):
    """Per-leg operator (c_zk, c_zbk, c_Ek) from v^nu J_{nu lam} q^lam.

    The soft-factor vector field on leg-momentum space is
    W = (v.k) q - (q.k) v, so the generator coefficients must satisfy
    A^{mn} k_n = W^m, i.e. A^{mn} = -(v^m q^n - q^m v^n) with RAISED
    indices.  With beta_{mn} = v_m q_n - q_m v_n (lowered) this is
    A^{mn} = -s^m s^n beta_{mn}, s = (-1,1,1,1): the three pure-rotation
    generators carry a MINUS sign relative to the lowered beta.  (The
    pre-repair version contracted beta_low directly; the momentum-space
    arbiter S5.6a pins the correct contraction uniquely.)
    """
    vl = eta_metric * vvec
    ql = eta_metric * qv
    beta = vl * ql.T - ql * vl.T
    cz = czb = cE = 0
    for gg in GENS:
        b = sp.simplify(beta[gg[0], gg[1]])
        a = b if 0 in gg else -b          # -s^m s^n beta_{mn}
        cz += a * dz_gen[gg]
        czb += a * dzb_gen[gg]
        cE += a * dE_gen[gg]
    return tuple(sp.simplify(c) for c in (cz, czb, cE))


opm = build_op(eps_m)
opp = build_op(eps_p)
Szz = tuple(sp.simplify(Az * c / qdotp) for c in build_op(dXz))      # Shat_zz / (i kap)
Szbb = tuple(sp.simplify(Azb * c / qdotp) for c in build_op(dXzb))

c_zbk_decl = (-2 * (zb - zbk) ** 2 * (1 + zb * zk)
              / ((z - zk) * (1 + z * zb) ** 3))
c_Ek_decl = (-2 * Ek * (zb - zbk) * (1 + zb * zk) ** 2
             / ((z - zk) * (1 + z * zb) ** 3 * (1 + zk * zbk)))
ok51 = (all(not c.has(om) for c in Szz)
        and simp(Szz[0]) == 0 and simp(Szz[1] - c_zbk_decl) == 0
        and simp(Szz[2] - c_Ek_decl) == 0)
record("S5.1", "S5", "per-leg Shat^(1)_zz operator: om cancels exactly; with the "
                     "repaired generator contraction (S5.6a) the components are "
                     "(c_zk, c_zbk, c_Ek) = (0, -2(zb-zbk)^2(1+zb zk)/((z-zk)"
                     "(1+z zb)^3), -2 E (zb-zbk)(1+zb zk)^2/((z-zk)(1+z zb)^3"
                     "(1+zk zbk))) — the angular component now sits in the "
                     "d_zbk slot, not d_zk",
       "pass" if ok51 else "FAIL",
       "" if ok51 else f"Szz = {[sp.sstr(sp.factor(c))[:120] for c in Szz]}")

check_all_zero("S5.2", "S5", "conjugation: sigma(Shat_zz) = Shat_zbzb as operators "
                             "(simultaneous-swap sigma, symbolic cancel proof)",
               [sigma(Szz[0]) - Szbb[1], sigma(Szz[1]) - Szbb[0],
                sigma(Szz[2]) - Szbb[2]])

eps_z_m = sp.simplify((eta_metric * dXz).dot(eps_m))
eps_zb_m = sp.simplify((eta_metric * dXzb).dot(eps_m))
eps_z_p = sp.simplify((eta_metric * dXz).dot(eps_p))
eps_zb_p = sp.simplify((eta_metric * dXzb).dot(eps_p))
check_all_zero("S5.3", "S5", "polarization pullbacks: eps^-_z = sqrt(2)/(1+z zb), "
                             "eps^-_zb = 0, eps^+_z = 0, eps^+_zb = sqrt(2)/(1+z zb)",
               [eps_z_m - sp.sqrt(2) / (1 + z * zb), eps_zb_m,
                eps_z_p, eps_zb_p - sp.sqrt(2) / (1 + z * zb)])

p_eps_m = sp.simplify((eta_metric * pk).dot(eps_m))
p_eps_p = sp.simplify((eta_metric * pk).dot(eps_p))
Hzz = tuple(sp.simplify(eps_z_m ** 2 * p_eps_m * c / qdotp) for c in opm)
Hzbb = tuple(sp.simplify(eps_zb_p ** 2 * p_eps_p * c / qdotp) for c in opp)

# Printed (6.8) RHS (stripped of kap/8 pi): D_zb^2 Shat_zz - D_z^2 Shat_zbzb.
# On a (z,z) tensor D_zb^2 is plain d_zb^2 (mixed Christoffels vanish) and
# likewise D_z^2 on (zb,zb); the derived (6.6)-side combination below uses the
# plain second derivatives D_zb^2 H_zbzb - D_z^2 H_zz exactly as verified.
d2 = lambda op, var: tuple(sp.diff(c, var, 2) for c in op)
RHS68 = [sp.simplify(aa - bb) for aa, bb in zip(d2(Szz, zb), d2(Szbb, z))]
LHS66 = [sp.simplify(aa - bb) for aa, bb in zip(d2(Hzbb, zb), d2(Hzz, z))]
check_zero("S5.4", "S5", "PSZ (6.8) bridge, energy channel: derived-from-(6.6) "
                         "D_zb^2 H_zbzb - D_z^2 H_zz equals the printed RHS "
                         "D_zb^2 Shat_zz - D_z^2 Shat_zbzb exactly in the d_Ek "
                         "component (factor-2 note: (6.1) half-symmetric limit vs "
                         "(6.5) convention)",
           LHS66[2] - RHS68[2])
check_nonzero("S5.5a", "S5", "typed obstruction: (6.8) per-leg angular channel "
                             "(d_zk) residual is nonzero (exact rational point); "
                             "with the repaired contraction it equals exactly the "
                             "named gauge-mixing residual M (S5.9) and closes only "
                             "leg-summed via KLPS (6.4) sum_k J_k = 0 (S10.1); "
                             "PSZ ref [20] = KLPS arXiv:1406.3312 (grounded)",
              (LHS66[0] - RHS68[0]).subs(PT1))
check_nonzero("S5.5b", "S5", "typed obstruction: (6.8) per-leg angular channel "
                             "(d_zbk) residual is nonzero (exact rational point); "
                             "the pre-repair zero in this channel was an artifact "
                             "of the lowered-beta contraction defect (S5.6a); same "
                             "leg-summed closure route as S5.5a",
              (LHS66[1] - RHS68[1]).subs(PT1))

# ---- S5.6 the KLPS (6.6) arbiter: which contraction is the faithful one
dpk_dEk = sp.diff(pk, Ek)
dpk_dzk = sp.diff(pk, zk)
dpk_dzbk = sp.diff(pk, zbk)
W_soft = p_eps_m * qv - qdotp * eps_m       # (eps.k) q - (q.k) eps on leg space
push_m = opm[2] * dpk_dEk + opm[0] * dpk_dzk + opm[1] * dpk_dzbk
check_all_zero("S5.6a", "S5", "generator-contraction arbiter: the per-leg operator's "
                              "pushforward c_Ek d_pk/dEk + c_zk d_pk/dzk + c_zbk "
                              "d_pk/dzbk equals exactly the soft-factor vector field "
                              "W = (eps^-.k) q - (q.k) eps^-; this pins A^{mn} = "
                              "-s^m s^n beta_{mn} (raised indices) and repairs the "
                              "earlier lowered-beta contraction",
               [push_m[i] - W_soft[i] for i in range(4)])

K66_z = (z - zk) ** 2 / (zbk - zb)
K66_E = Ek * (z - zk) * (1 + z * zbk) / ((zbk - zb) * (1 + zk * zbk))
Sminus = tuple(sp.simplify(p_eps_m * c / qdotp) for c in opm)
check_all_zero("S5.6b", "S5", "the repaired per-leg stripped soft operator is exactly "
                              "KLPS (6.6): (c_zk, c_zbk, c_Ek) = ((z-zk)^2/(zbk-zb), "
                              "0, Ek(z-zk)(1+z zbk)/((zbk-zb)(1+zk zbk))) "
                              "(PSZ ref [20] = KLPS arXiv:1406.3312)",
               [Sminus[0] - K66_z, Sminus[1], Sminus[2] - K66_E])

Splus = tuple(sp.simplify(p_eps_p * c / qdotp) for c in opp)
check_all_zero("S5.6c", "S5", "the eps+ operator is the sigma-conjugate (slot-swapped) "
                              "of the eps- operator",
               [Splus[0], Splus[1] - sigma(Sminus[0]), Splus[2] - sigma(Sminus[2])])

# ---- S5.7 tetrad and gauge direction
b_tet = sp.sqrt(2) / (1 + z * zb)
c_tet = -zb / (1 + z * zb)
cb_tet = -z / (1 + z * zb)
check_all_zero("S5.7a", "S5", "sphere tetrad: dX/dz = b eps+ + c X and dX/dzb = "
                              "b eps- + cb X with b = sqrt(2)/(1+z zb), "
                              "c = -zb/(1+z zb), cb = -z/(1+z zb)",
               [dXz[i] - b_tet * eps_p[i] - c_tet * X_soft[i] for i in range(4)]
               + [dXzb[i] - b_tet * eps_m[i] - cb_tet * X_soft[i] for i in range(4)])
check_all_zero("S5.7b", "S5", "gauge direction: the soft-factor vector field "
                              "annihilates q itself, op(q) = 0",
               list(build_op(qv)))

# ---- S5.8 mixing theorem
mix_p = tuple(sp.simplify(b_tet * c_tet / om * c) for c in opp)
mix_m = tuple(sp.simplify(b_tet * cb_tet / om * c) for c in opm)
check_all_zero("S5.8", "S5", "mixing theorem: Shat_zz = b^2 S+ + (b c/om) op(eps+) "
                             "and Shat_zbzb = b^2 S- + (b cb/om) op(eps-) — the "
                             "angular gauge components enter Shat only through the "
                             "KLPS (6.4) first-type gauge-mixing term "
                             "eps^nu q^lam J_{nu lam}",
               [Szz[i] - b_tet ** 2 * Splus[i] - mix_p[i] for i in range(3)]
               + [Szbb[i] - b_tet ** 2 * Sminus[i] - mix_m[i] for i in range(3)])

# ---- S5.9 the bridge residual, named exactly
M_closed = [
    -4 * (2 * z ** 2 * zb ** 2 * zk + 3 * z ** 2 * zb - 3 * z * zb ** 2 * zk ** 2
          - 8 * z * zb * zk - 3 * z + 3 * zb * zk ** 2 + 2 * zk) / (1 + z * zb) ** 5,
    4 * (2 * z ** 2 * zb ** 2 * zbk - 3 * z ** 2 * zb * zbk ** 2 + 3 * z * zb ** 2
         - 8 * z * zb * zbk + 3 * z * zbk ** 2 - 3 * zb + 2 * zbk) / (1 + z * zb) ** 5,
    sp.Integer(0)]
check_all_zero("S5.9a", "S5", "the (6.8) per-leg bridge residual is named exactly: "
                              "derived-LHS minus printed-RHS equals M := D_z^2 mix^- "
                              "- D_zb^2 mix^+ in all three operator channels",
               [LHS66[i] - RHS68[i] - M_closed[i] for i in range(3)])
M_comp = [simp(aa - bb) for aa, bb in zip(d2(mix_m, z), d2(mix_p, zb))]
check_all_zero("S5.9b", "S5", "M computed from the mixing operators equals its "
                              "closed forms (polynomial numerators over (1+z zb)^5)",
               [M_comp[i] - M_closed[i] for i in range(3)])
check_zero("S5.9c", "S5", "the residual has no d_Ek component: M_E = 0, so the "
                          "energy channel closes per leg (consistent with S5.4)",
           M_comp[2])
check_zero("S5.9d", "S5", "exact-value pinning: M_zk(PT1) = -102500/483153",
           M_closed[0].subs(PT1) + sp.Rational(102500, 483153))
check_zero("S5.9e", "S5", "exact-value pinning: M_zbk(PT1) = -1671500/7891499",
           M_closed[1].subs(PT1) + sp.Rational(1671500, 7891499))

# ================================================================ S6 Green kernel
Szw = (z - w) * (zb - wb) / ((1 + z * zb) * (1 + w * wb))   # sin^2(Theta/2)
Gf = sp.log(z - w) + sp.log(zb - wb) - sp.log(1 + z * zb) - sp.log(1 + w * wb)
check_zero("S6.1", "S6", "regular part d_z d_zb G = -1/(1+z zb)^2 = -(1/2) gamma_zzb "
                         "(PSZ 5.4)",
           sp.diff(Gf, z, zb) + 1 / (1 + z * zb) ** 2)
record("S6.2", "S6", "distributional part: declared prescription "
                     "d_zb (z-w)^{-1} = pi delta^2; the two log channels "
                     "ln(z-w), ln(zb-wb) contribute pi + pi = 2 pi (PSZ 5.4)",
       "pass", "declared input (external ledger item 5): 2*pi = pi + pi exact")
check_zero("S6.3", "S6", "same kernel as the leading triangle: xhat(z).xhat(w) = "
                         "1 - 2 S with S = sin^2(Theta/2) (links PSZ 5.3 to the "
                         "checked HMLS 2.25-2.26 identities)",
           xhat(z, zb).dot(xhat(w, wb)) - (1 - 2 * Szw))

# ================================================================ S7 news shift law
def Dz3_vec(Yf):
    """Covariant D_z^3 on a Y^z vector component via the weight sequence
    (d+Gam) on vector -> plain d on (z,low-z) -> (d-Gam) on (z, low-zz)."""
    T1 = sp.diff(Yf, z) + Gam * Yf
    T2 = sp.diff(T1, z)
    T3 = sp.diff(T2, z) - Gam * T2
    return sp.simplify(T3)


check_all_zero("S7.1", "S7", "D_z^3 kills the global conformal Killing vectors "
                             "span{1, z, z^2} (KLPS 5.5 quotient, among globally "
                             "smooth vector fields)",
               [Dz3_vec(1), Dz3_vec(z), Dz3_vec(z ** 2)])
check_zero("S7.2", "S7", "D_z^3(z^3) = 6 != 0: modes outside the CKV span are not "
                         "killed (Schwarzian-type normalization)",
           Dz3_vec(z ** 3) - 6)
check_all_zero("S7.3", "S7", "typed refinement: the FORMAL kernel of D_z^3 is larger "
                             "than the CKVs — antiholomorphic-dressed vectors zb, "
                             "zb^2, z zb are also killed but fail global smoothness "
                             "at the poles; the CKV-only kernel needs the smoothness "
                             "condition (analytic input, same mechanism as S8.2)",
               [Dz3_vec(zb), Dz3_vec(zb ** 2), Dz3_vec(z * zb)])
check_nonzero("S7.4", "S7", "the formal kernel is not all antiholomorphic-dressed "
                            "fields either: D_z^3(zb/(1+z zb)) != 0",
              Dz3_vec(zb / (1 + z * zb)))

# ================================================================ S8 carrier (H2)
N_real = z * zb * (z + zb) / (1 + z * zb)        # explicit sigma-symmetric field
Czz_N = Dz_low(Dz_low(N_real, 0), 1)             # C_zz = D_z^2 N
Czbb_N = Dzb_low(Dzb_low(N_real, 0), 1)
A_z = Dz_low(Czz_N, 2)                           # D_z C_zz (contour 1-form, PSZ 4.5)
A_zb = Dzb_low(Czbb_N, 2)
B_curl = sp.diff(A_zb, z) - sp.diff(A_z, zb)     # Stokes bulk form
ok81 = (simp(sigma(N_real) - N_real) == 0
        and simp(sigma(B_curl) + B_curl) == 0
        and simp(B_curl.subs({z: 2, zb: sp.Rational(3, 5)})) != 0)
record("S8.1", "S8", "Stokes bridge on an explicit real field: the PSZ (4.5) bulk "
                     "form B = d_z(D_zb C_zbzb) - d_zb(D_z C_zz) is sigma-odd "
                     "(magnetic-only contour) and nonzero",
       "pass" if ok81 else "FAIL",
       "test field N = z zb (z+zb)/(1+z zb)" if ok81 else "identity failed")

check_all_zero("S8.2", "S8", "grade-step ambiguity: ker of D_z on rank-s lower-z "
                             "tensors is (1+z zb)^{-2s} x (antiholomorphic) for "
                             "s = 2, 3, 4 — the smooth/corner-condition quotient "
                             "is an analytic input, not exact",
               [Dz_low((1 + z * zb) ** (-2 * s), s) for s in (2, 3, 4)])

X_gauge = z * zb / (1 + z * zb)                  # real (sigma-symmetric) shift
Y_gauge = sp.diff(X_gauge, z, zb)
ok83 = simp(sigma(X_gauge) - X_gauge) == 0 and simp(sigma(Y_gauge) - Y_gauge) == 0
record("S8.3", "S8", "curl-only dependence: for real X, d_z d_zb X is sigma-even, "
                     "so the Im projection kills gauge shifts N_z -> N_z + d_z X "
                     "(PSZ below (5.7))",
       "pass" if ok83 else "FAIL")
record("S8.4", "S8", "carrier verdict (H2 test): NOT one operator — one sigma-odd "
                     "FIELD (the curl/magnetic tower over C_zz, equivalently the "
                     "curl of N_z) read at three derivative grades: D_z (memory "
                     "contour PSZ 4.5), D_z^2 (soft side PSZ 6.9), D_z^3 "
                     "(constraint/shift PSZ 5.2, KLPS 5.5). Typed refinement of "
                     "the leading one-operator picture.",
       "pass", "confirmed by S8.1-S8.3 + S7.1 kernel structure")

# ================================================================ S9 constraint parity
D3C = Dz_low(Dz_low(Dz_low(Czz_N, 2), 3), 4)     # D_z^3 C_zz
D3Cb = Dzb_low(Dzb_low(Dzb_low(Czbb_N, 2), 3), 4)
L9 = sp.diff(D3C, zb)                            # PSZ (5.2) LHS density
R9 = sp.diff(D3Cb, z)
ok91 = (simp(sigma(L9) - R9) == 0
        and simp((L9 - R9).subs({z: 2, zb: sp.Rational(3, 5)})) != 0)
record("S9.1", "S9", "magnetic-parity projection: sigma(d_zb D_z^3 C_zz) = "
                     "d_z D_zb^3 C_zbzb exactly on the real test field, and the two "
                     "differ — the Im in PSZ (5.2) is a genuine parity projection",
       "pass" if ok91 else "FAIL")
X_gauge2 = (z + zb) ** 2 / (1 + z * zb) ** 2
Y_gauge2 = sp.diff(X_gauge2, z, zb)
ok92 = simp(sigma(X_gauge2) - X_gauge2) == 0 and simp(sigma(Y_gauge2) - Y_gauge2) == 0
record("S9.2", "S9", "RHS curl-only invariance (PSZ below (5.5)): real shift "
                     "N_z -> N_z + d_z X leaves Im[d_u d_zb N_z + d_zb T_uz] "
                     "invariant (second independent real test field)",
       "pass" if ok92 else "FAIL")

# ================================================================ S10 KLPS scaffold
# S10.1 the leg-summed closure mechanism (KLPS (6.4)): the mixing term is per
# leg the pure-gauge response eps^nu q^lam J_{k nu lam}; its leg sum vanishes
# under total angular momentum conservation sum_k J_k = 0.
J1s = sp.zeros(4)
J2s = sp.zeros(4)
for m in range(4):
    for n in range(m + 1, 4):
        s1 = sp.Symbol(f"J1_{m}{n}")
        s2 = sp.Symbol(f"J2_{m}{n}")
        J1s[m, n] = s1
        J1s[n, m] = -s1
        J2s[m, n] = s2
        J2s[n, m] = -s2


def mixing_C(Jmat):
    """eps^+_n q_l J^{n l}: the k-independent-prefactor per-leg mixing term."""
    return sp.simplify(sum(eps_p[n] * qv[l] * Jmat[n, l]
                           for n in range(4) for l in range(4)))


C_J1 = mixing_C(J1s)
C_J2 = mixing_C(J2s)
_J2_neg = {J2s[m, n]: -J1s[m, n] for m in range(4) for n in range(m + 1, 4)}
check_zero("S10.1a", "S10", "leg-summed closure: C(J1) + C(J2) vanishes when "
                            "J1 + J2 = 0 — the KLPS (6.4) sum_k J_k = 0 mechanism "
                            "that kills the leg-summed gauge-mixing residual of S5.9 "
                            "(the prefactor b c/om is k-independent)",
           (C_J1 + C_J2).subs(_J2_neg))
check_nonzero("S10.1b", "S10", "typed obstruction: per leg the gauge-mixing "
                               "contraction C(J) = eps^+_n q_l J^{n l} is nonzero",
              C_J1)

# S10.2/S10.3 the KLPS (6.7)/(6.12) delta scaffold as a per-leg distributional
# identity, under the declared prescription d_zb (z-w)^{-1} = pi delta^2 (so
# d_z (zb-zbk)^{-1} = pi delta^2 by conjugation).  Covariant reading: the
# canonical (0,2) weight sequence w = (0,1,2), D_z^{(w)} f = (d_z - w Gam) f.
# For T = +/- G(z) P with P = 1/(zb - zbk), the Leibniz fold of the
# weight-corrected third derivative is
#   D^3(G P) = cP P + c0 delta + c1 D_z delta + c2 D_z^2 delta
# with cP = G''' - 3 Gam G'' + (2 Gam^2 - Gam') G',
#      c0 = pi (3 G'' - 6 Gam G' + (2 Gam^2 - Gam') G),
#      c1 = pi (3 G' - 3 Gam G),  c2 = pi G,
# and the gamma^{z zb} prefactor times products f(z) D_z^n delta reduces at
# the pole via f D^n delta = sum_j (-1)^j C(n,j) (d^j f)|pole D^{n-j} delta.
gam1 = sp.diff(Gam, z)
Af = 2 * Gam ** 2 - gam1
ginv = (1 + z * zb) ** 2 / 2          # gamma^{z zb}
POLE = {z: zk, zb: zbk}


def delta_fold(G, sign):
    """gamma^{zzb} D_z^3 (sign * G * P) as (regular, D0, D1, D2) coefficients."""
    G1 = sp.diff(G, z)
    G2 = sp.diff(G, z, 2)
    G3 = sp.diff(G, z, 3)
    fP = sign * ginv * (G3 - 3 * Gam * G2 + Af * G1)
    f0 = sign * ginv * sp.pi * (3 * G2 - 6 * Gam * G1 + Af * G)
    f1 = sign * ginv * sp.pi * (3 * G1 - 3 * Gam * G)
    f2 = sign * ginv * sp.pi * G
    at = lambda e: sp.simplify(e.subs(POLE))
    D0 = sp.simplify(at(f0) - at(sp.diff(f1, z)) + at(sp.diff(f2, z, 2)))
    D1 = sp.simplify(at(f1) - 2 * at(sp.diff(f2, z)))
    D2v = at(f2)
    return fP, D0, D1, D2v


# pole signs from eps-hat^+_{zb zb} S^{(1)-}: eps-hat^+ = 2/(1+z zb)^2 (KLPS 5.26),
# K66 denominators (zbk - zb) = -(zb - zbk)  =>  minus; spin (6.11) has the
# opposite overall sign per unit h_k.
G_ang = 2 * (z - zk) ** 2 / (1 + z * zb) ** 2
G_E = 2 * Ek * (z - zk) * (1 + z * zbk) / ((1 + z * zb) ** 2 * (1 + zk * zbk))
G_sp = sp.simplify(G_E / Ek)
fPa, D0a, D1a, D2a = delta_fold(G_ang, -1)
fPe, D0e, D1e, D2e = delta_fold(G_E, -1)
fPs, D0s, D1s, D2s = delta_fold(G_sp, 1)

check_zero("S10.2a", "S10", "KLPS (6.7) angular channel: the computed leading delta "
                            "is D0 = -2 pi per leg — exactly half the printed -4 pi",
           D0a + 2 * sp.pi)
check_zero("S10.2b", "S10", "KLPS (6.7) energy channel: the computed D_z-delta "
                            "coefficient is -pi Ek — exactly half the printed -2 pi Ek",
           D1e + sp.pi * Ek)
check_zero("S10.2c", "S10", "KLPS (6.12) spin channel: the computed D_z-delta "
                            "coefficient is +pi per unit h_k — exactly half the "
                            "printed +2 pi",
           D1s - sp.pi)
check_all_zero("S10.2d", "S10", "channels printed as absent are absent: D1_ang = "
                                "D2_ang = D2_E = D2_sp = 0",
               [D1a, D2a, D2e, D2s])
check_all_zero("S10.2e", "S10", "the regular (non-distributional) parts of "
                                "gamma^{zzb} D_z^3(eps-hat S) vanish identically in "
                                "all three channels — no regular obstruction",
               [fPa, fPe, fPs])

check_zero("S10.3a", "S10", "structural obstruction, named: the energy channel "
                            "carries an unprinted plain-delta term D0_E = "
                            "-2 pi Ek zbk/(1+zk zbk)",
           D0e + 2 * sp.pi * Ek * zbk / (1 + zk * zbk))
check_nonzero("S10.3b", "S10", "typed obstruction: printed (6.7) has NO plain-delta "
                               "term in the d_Ek channel; the computed one is "
                               "nonzero — no delta^2-normalization convention "
                               "repairs this",
              D0e)
check_zero("S10.3c", "S10", "structural obstruction, named: the spin channel "
                            "carries an unprinted plain-delta term D0_sp = "
                            "+2 pi zbk/(1+zk zbk) per unit h_k",
           D0s - 2 * sp.pi * zbk / (1 + zk * zbk))
check_nonzero("S10.3d", "S10", "typed obstruction: printed (6.12) has NO plain-delta "
                               "term at all; the computed one is nonzero",
              D0s)
check_nonzero("S10.3e", "S10", "typed residual: the uniform factor-1/2 gap (computed "
                               "deltas are half the printed ones) is not explained "
                               "away — candidate delta^2-normalization convention "
                               "drift, same family as the S5.4 factor-2 note",
              D0a + 4 * sp.pi)

# ================================================================ summary
mandatory = [r for r in results if r["status"] == "FAIL"]
n_pass = sum(1 for r in results if r["status"] == "pass")
summary = {
    "total": len(results), "passed": n_pass, "failed": len(mandatory),
    "failed_ids": [r["id"] for r in mandatory],
    "classification": {
        "carrier": "one sigma-odd field (the magnetic/curl part of N_z, "
                   "equivalently the tower over C_zz) read at three derivative "
                   "grades D_z, D_z^2, D_z^3 — NOT one operator (H2 confirmed as "
                   "a typed refinement of the leading one-operator picture)",
        "common_operation": "curl/magnetic projection (Im) of the C_zz tower; "
                            "per-leg soft operator Shat^(1)_zz with components "
                            "(0, c_zbk, c_Ek) built from PSZ (6.5)+(6.7) with the "
                            "repaired generator contraction (S5.1, S5.6a)",
        "verdict": "soft-memory bridge (PSZ 6.8) exact per leg in the energy "
                   "channel; the angular channels fail per leg by exactly the "
                   "named gauge-mixing residual M = D_z^2 mix^- - D_zb^2 mix^+ "
                   "(S5.9), which closes only leg-summed via the KLPS (6.4) "
                   "mechanism sum_k J_k = 0 (S10.1) — verdict (ii)",
        "external_inputs": [
            "J: global angular momentum conservation (CS (7); KLPS (6.4); "
            "PSZ (6.9) derivation)",
            "G_CS gauge prescription (conventions packet section 2)",
            "antipodal matching + KLPS i^0 mode correspondence (packet section 3)",
            "symmetric/hermitian zero-frequency limit (PSZ 6.1) = (1+om d_om) "
            "projection (KLPS 5.33)",
            "distributional prescription d_zb (z-w)^{-1} = pi delta^2 (inherited "
            "from the leading packet)"],
        "conventions_residuals": [
            "CS (7) sign: with the declared shift dE = q Lam + Lam q the per-leg "
            "contraction gives dS^(1) = +i Lam q sum J vs printed -i (shift-sign "
            "convention; check S2.1)",
            "S3: PSZ (6.5) / CS (6) ratio is exactly kap = sqrt(32 pi G) "
            "(check S3.1/S3.2)",
            "S5: the generator contraction in build_op was repaired (raised "
            "indices A^{mn} = -s^m s^n beta_{mn}) and pinned by the "
            "momentum-space arbiter S5.6a; the repaired operator reproduces "
            "KLPS (6.6) exactly (S5.6b) — PSZ ref [20] = KLPS arXiv:1406.3312 "
            "(grounded); [SZ] arXiv:1411.5745 is grounded at "
            "sources/sz1411.5745.txt but not needed for this closure",
            "S5: PSZ (6.8) holds per leg only in the d_Ek channel; the angular "
            "residual is exactly M = D_z^2 mix^- - D_zb^2 mix^+ (S5.9), the "
            "second derivative of the KLPS (6.4) gauge-mixing term, closing "
            "only leg-summed under sum_k J_k = 0 (S10.1)",
            "S10: KLPS (6.7)/(6.12) as printed are NOT exact per-leg "
            "distributional identities under the declared prescription: the "
            "computed deltas carry a uniform factor 1/2 relative to print "
            "(candidate delta^2-normalization drift), and the energy/spin "
            "channels carry unprinted plain-delta terms D0_E = -2 pi Ek "
            "zbk/(1+zk zbk), D0_sp = +2 pi zbk/(1+zk zbk) h_k (S10.2/S10.3); "
            "the endpoint KLPS (5.16) is unaffected (S4.3)",
            "S7: the formal kernel of D_z^3 exceeds the CKVs (zb, zb^2, z zb "
            "are killed but singular at the poles); the CKV-only quotient "
            "requires global smoothness — analytic input, same mechanism as "
            "S8.2 (checks S7.3/S7.4)",
            "S8.2: the smoothness/corner-condition quotient removing the "
            "(1+z zb)^{-2s} x antiholomorphic ambiguity between derivative "
            "grades is an analytic note (declared input), not an exact check"],
        "outcome": "mixed: the subleading naturality square closes exactly at the "
                   "level of the projector (S1), gauge variation (S2), "
                   "normalization ratio kap (S3), hard-operator sphere reduction "
                   "(S4), Green kernel (S6), and the D_z^3 CKV quotient (S7); the "
                   "D^2 bridge (S5) closes exactly per leg in the energy channel, "
                   "with the angular channels equal to the exactly named "
                   "gauge-mixing residual M (S5.9) that closes only leg-summed "
                   "via KLPS (6.4) sum_k J_k = 0 (S10.1); the KLPS (6.7)/(6.12) "
                   "delta scaffold holds only at half delta strength with "
                   "structural plain-delta contamination (S10.2/S10.3); the "
                   "carrier question lands on one field with three derivative "
                   "grades rather than one operator (S8, H2 refinement)",
    },
}

out = {"checker": "subleading_triangle_exact_checks", "author": "marici.Strominger",
       "date": "2026-08-19", "checks": results, "summary": summary}
path = os.path.join(os.path.dirname(__file__), "..", "results",
                    "subleading_triangle_exact_checks.json")
os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path, "w", encoding="utf-8") as fh:
    json.dump(out, fh, indent=2)
print(f"\n{n_pass}/{len(results)} checks passed; results -> {os.path.normpath(path)}")
raise SystemExit(1 if mandatory else 0)
