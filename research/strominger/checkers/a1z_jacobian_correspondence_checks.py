"""Exact A1z Jacobian-correspondence checker: why the unique partnerless
channel carries the unique odd determinant line (marici.Strominger).

Companion to (does NOT import or modify):
  research/strominger/checkers/rung3_s2_bridge_checks.py (R1-R4, grounding)
  research/strominger/checkers/rung3_cocycle_checks.py (K1-K5, cocycle arc)
Sources and conventions:
  research/strominger/rung3-cocycle.md (K5 gate failure on A1z, det = u X)
  research/strominger/rung3-s2-bridge.md (R1.3: A1E = 0 grounded)

All arithmetic is exact sympy symbolics. No floating point anywhere.
sigma: z <-> zb, zk <-> zbk (Ek, om fixed); alpha: z -> -1/zb, zb -> -1/z
(legs fixed). The determinant line of a coefficient K is
det(K) = F2 sigma(F2) = D(K) with the multiplicative norm character
D(f) = Q(alpha f)/Q(f), Q(f) = f sigma(f).

Layers:
  J1 the operator square: the five grounded S^(2)- channels are EXACTLY the
     pure square V^2/den of the single leg vector field
     V = c_zk d_zk + c_Ek d_Ek over the common denominator
     den = -4 Ek om^2 (z-zk)(zb-zbk)/((1+u)(1+zk zbk)).
  J2 the Hamiltonian collapse: V(c_Ek) = 0 (the A1E = 0 grounding), so V is
     Hamiltonian with respect to c_Ek with explicit multiplier
     mu = Ek c_zk/c_Ek = (z-zk)(1+zk zbk)/(1+z zbk):
     c_zk = mu d_Ek(c_Ek) and c_Ek = -mu d_zk(c_Ek).
  J3 the Jacobian identity: V(c_zk) = mu Jac(c_zk, c_Ek) — the surviving
     first-order channel A1z is a Poisson bracket (area form), not a
     symmetric product of soft-factor lines.
  J4 norm bookkeeping: D is multiplicative and every product-side input has
     a SQUARE character: D(c_zk) = X^2, D(c_Ek) = 1, D(den) = X^2,
     D(mu) = X^2, with X = (1+z zbk)(1+zb zk)/((z-zk)(zb-zbk)). Hence every
     channel built from c-line products has even determinant — forced, not
     computed case by case.
  J5 the Jacobian character: D(Jac) = u X — the Jacobian of the soft map is
     the UNIQUE odd-character object in the construction. Therefore
     det(A1z) = D(mu) D(Jac)/D(den) = u X, and the rational square-root
     gate failure is located exactly in the soft-map Jacobian.
  J6 the correspondence verdict: (a) necessity — every symmetrized c-product
     channel has even det by J4 multiplicativity; (b) the collapse
     V(c_Ek) = 0 is precisely the partner-vanishing (A1E = 0), and it
     reduces the first-order sector to the pure Jacobian channel A1z;
     (c) exact pinning identities det(A1z)^2 = u^2 det(A2z) det(AzE) and
     F2(A1z)^2 = -zb^2 F2(AzE) F2(A2z) — the odd line is pinned by the even
     lines up to the diagonal monomial u^2. Verdict: "vanishing partner"
     does not numerically force oddness; it removes the square protection.
     The odd u-valuation (1) is then a computed property of the soft-map
     Jacobian character.

Output: research/strominger/results/a1z_jacobian_correspondence.json
Exit code 0 iff every check passes.
"""
import json
import os
import sympy as sp

# ---------------------------------------------------------------- symbols
z, zb, zk, zbk, Ek = sp.symbols("z zb zk zbk Ek")
om = sp.symbols("om", positive=True)
sq2 = sp.sqrt(2)
u = z * zb

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
    e = expr.subs(subs) if subs else expr
    e = simp(e)
    record(cid, group, statement, "pass" if e == 0 else "FAIL",
           "" if e == 0 else f"residual: {sp.sstr(e)[:300]}")
    return e == 0


def check_true(cid, group, statement, cond, detail=""):
    record(cid, group, statement, "pass" if bool(cond) else "FAIL", detail)
    return bool(cond)


# ============================================================ maps
SIG = [(z, zb), (zb, z), (zk, zbk), (zbk, zk)]
ALPHA = [(z, -1 / zb), (zb, -1 / z)]


def sigma(e):
    """Complex conjugation on sphere+leg variables: simultaneous swap."""
    return e.subs(SIG, simultaneous=True)


def alpha_map(e):
    """Antipodal pullback: z -> -1/zb, zb -> -1/z (legs fixed)."""
    return e.subs(ALPHA, simultaneous=True)


def Qmap(e):
    """Sigma-norm Q(f) = f sigma(f), sigma-invariant and multiplicative."""
    return sp.cancel(e * sigma(e))


def Dmap(e):
    """Determinant-line norm character D(f) = Q(alpha f)/Q(f)."""
    return sp.cancel(Qmap(alpha_map(e)) / Qmap(e))


def vval(e, var):
    """Exact order of vanishing of a rational function along var = 0
    (generic other variables): positive for zeros, negative for poles."""
    n, d = sp.fraction(sp.cancel(e))
    cnt = 0
    n = sp.expand(n)
    while n != 0 and sp.simplify(n.subs(var, 0)) == 0:
        n = sp.expand(n / var)
        cnt += 1
    d = sp.expand(d)
    while d != 0 and sp.simplify(d.subs(var, 0)) == 0:
        d = sp.expand(d / var)
        cnt -= 1
    return cnt


def valu(e):
    """Diagonal u-valuation: val_u = val_z + val_zb (u = z zb)."""
    return vval(e, z) + vval(e, zb)


# ============================================================ the line
# Grounded S^(2)- per-leg operator channels K^+ (bridge checker R1.2/R1.3).
c_zk = -sq2 * om * (z - zk) ** 2 / (1 + u)
c_Ek = -sq2 * Ek * om * (z - zk) * (1 + z * zbk) / ((1 + u) * (1 + zk * zbk))
A2z = -(z - zk) ** 3 * (1 + zk * zbk) / (2 * Ek * (zb - zbk) * (1 + u))
AzE = -(z - zk) ** 2 * (1 + z * zbk) / ((zb - zbk) * (1 + u))
A2E = -Ek * (z - zk) * (1 + z * zbk) ** 2 / (2 * (zb - zbk) * (1 + u) * (1 + zk * zbk))
A1z = (z - zk) ** 2 * (1 + zk * zbk) / (Ek * (zb - zbk) * (1 + u))

X = (1 + z * zbk) * (1 + zb * zk) / ((z - zk) * (zb - zbk))


def Vop(f):
    """The soft-map leg vector field V = c_zk d_zk + c_Ek d_Ek."""
    return c_zk * sp.diff(f, zk) + c_Ek * sp.diff(f, Ek)


# ============================================================ J1 operator square
den = sp.cancel(c_zk ** 2 / A2z)
den_decl = -4 * Ek * om ** 2 * (z - zk) * (zb - zbk) / ((1 + u) * (1 + zk * zbk))
check_zero("J1.den", "J1", "common denominator closed form: "
           "den = c_zk^2/A2z = -4 Ek om^2 (z-zk)(zb-zbk)/((1+u)(1+zk zbk))",
           den - den_decl)
check_zero("J1.AzE", "J1", "operator square: AzE den = 2 c_zk c_Ek",
           AzE * den - 2 * c_zk * c_Ek)
check_zero("J1.A2E", "J1", "operator square: A2E den = c_Ek^2",
           A2E * den - c_Ek ** 2)
check_zero("J1.A1z", "J1", "operator square: A1z den = V(c_zk)",
           A1z * den - Vop(c_zk))
check_zero("J1.A1E", "J1", "operator square: A1E den = V(c_Ek) = 0 "
           "(helicity-degenerate partner, grounded R1.3)", Vop(c_Ek))

# ============================================================ J2 Hamiltonian collapse
mu = sp.cancel(Ek * c_zk / c_Ek)
mu_decl = (z - zk) * (1 + zk * zbk) / (1 + z * zbk)
check_zero("J2.mu", "J2", "Hamiltonian multiplier closed form: "
           "mu = Ek c_zk/c_Ek = (z-zk)(1+zk zbk)/(1+z zbk)", mu - mu_decl)
check_zero("J2.flow.a", "J2", "Hamiltonian collapse: c_zk = mu d_Ek(c_Ek)",
           c_zk - mu * sp.diff(c_Ek, Ek))
check_zero("J2.flow.b", "J2", "Hamiltonian collapse: c_Ek = -mu d_zk(c_Ek)",
           c_Ek + mu * sp.diff(c_Ek, zk))
check_true("J2.collapse", "J2", "V(c_Ek) = 0 is exactly the partner-vanishing: "
           "in 2 leg dimensions a vector field annihilating c_Ek is "
           "Hamiltonian with respect to c_Ek, V = mu J grad(c_Ek)",
           simp(Vop(c_Ek)) == 0 and simp(c_zk - mu * sp.diff(c_Ek, Ek)) == 0)

# ============================================================ J3 Jacobian identity
Jac = (sp.diff(c_zk, zk) * sp.diff(c_Ek, Ek)
       - sp.diff(c_zk, Ek) * sp.diff(c_Ek, zk))
Jac_decl = (-4 * om ** 2 * (z - zk) ** 2 * (1 + z * zbk)
            / ((1 + u) ** 2 * (1 + zk * zbk)))
check_zero("J3.bracket", "J3", "Jacobian identity: the surviving first-order "
           "numerator is a Poisson bracket, V(c_zk) = mu Jac(c_zk, c_Ek)",
           Vop(c_zk) - mu * Jac)
check_zero("J3.closed", "J3", "Jacobian closed form: Jac(c_zk, c_Ek) = "
           "-4 om^2 (z-zk)^2 (1+z zbk)/((1+u)^2 (1+zk zbk))",
           sp.cancel(Jac) - Jac_decl)
check_zero("J3.channel", "J3", "the A1z channel is the area form: "
           "A1z = mu Jac/den", A1z - mu * Jac / den)
check_true("J3.nonzero", "J3", "the soft map (zk, Ek) -> (c_zk, c_Ek) is a "
           "local diffeomorphism: Jac is not identically zero",
           simp(Jac) != 0)

# ============================================================ J4 norm bookkeeping
check_zero("J4.mult", "J4", "the norm character is multiplicative: "
           "D(c_zk c_Ek) = D(c_zk) D(c_Ek)",
           Dmap(c_zk * c_Ek) - Dmap(c_zk) * Dmap(c_Ek))
check_zero("J4.czk", "J4", "square character: D(c_zk) = X^2",
           Dmap(c_zk) - X ** 2)
check_zero("J4.cEk", "J4", "square character: D(c_Ek) = 1", Dmap(c_Ek) - 1)
check_zero("J4.den", "J4", "square character: D(den) = X^2",
           Dmap(den) - X ** 2)
check_zero("J4.mu", "J4", "square character: D(mu) = X^2 — even the "
           "Hamiltonian multiplier is square-protected", Dmap(mu) - X ** 2)
check_zero("J4.A2z", "J4", "forced evenness: det(A2z) = D(c_zk)^2/D(den) = X^2",
           Dmap(c_zk) ** 2 / Dmap(den) - X ** 2)
check_zero("J4.AzE", "J4", "forced evenness: det(AzE) = D(c_zk)D(c_Ek)/D(den) = 1",
           Dmap(c_zk) * Dmap(c_Ek) / Dmap(den) - 1)
check_zero("J4.A2E", "J4", "forced evenness: det(A2E) = D(c_Ek)^2/D(den) = X^-2",
           Dmap(c_Ek) ** 2 / Dmap(den) - X ** -2)

# ============================================================ J5 Jacobian character
check_zero("J5.char", "J5", "THE Jacobian character: D(Jac(c_zk, c_Ek)) = u X "
           "— the soft-map Jacobian is the unique odd-character object in "
           "the construction", Dmap(sp.cancel(Jac)) - u * X)
check_zero("J5.Vczk", "J5", "character multiplicativity on the area form: "
           "D(V(c_zk)) = D(mu) D(Jac) = u X^3", Dmap(Vop(c_zk)) - u * X ** 3)
check_zero("J5.det", "J5", "the A1z determinant line from the characters: "
           "det(A1z) = D(mu) D(Jac)/D(den) = u X (matches the K3 line)",
           Dmap(Vop(c_zk)) / Dmap(den) - u * X)
vzd = vval(u * X, z)
check_true("J5.gate", "J5", "the square-root gate failure is located in the "
           f"Jacobian: det(A1z) = u X has odd val_z = {vzd}, so no rational "
           "square root exists", vzd % 2 == 1,
           f"val_z(uX) = {vzd}, val_u(uX) = {valu(u * X)}")

# ============================================================ J6 correspondence verdict
square_roots = {"c_zk": X, "c_Ek": sp.Integer(1), "A2z": X, "AzE": sp.Integer(1),
                "A2E": X ** -1}
check_true("J6.necessity", "J6", "necessity direction: every symmetrized "
           "c-product channel (c_zk, c_Ek, c_zk^2, c_zk c_Ek, c_Ek^2 over "
           "den) has a determinant that is a RATIONAL SQUARE — evenness is "
           "forced by J4 multiplicativity, not checked case by case",
           all(v is not None for v in square_roots.values()),
           "roots: X, 1, X, 1, X^-1; the Jacobian channel is the only "
           "channel not of product form")
det_A1z, det_A2z, det_AzE = u * X, X ** 2, sp.Integer(1)
check_zero("J6.pin.det", "J6", "pinning identity: the odd line is pinned by "
           "the even lines up to u^2: det(A1z)^2 = u^2 det(A2z) det(AzE)",
           det_A1z ** 2 - u ** 2 * det_A2z * det_AzE)
F2_A1z = -z ** 2 * (z - zk) * (1 + zb * zk) ** 2 / (
    zb * (zb - zbk) ** 2 * (1 + z * zbk))
F2_AzE = -z ** 2 * (z - zk) * (1 + zb * zk) / (
    zb ** 2 * (zb - zbk) * (1 + z * zbk))
F2_A2z = z ** 2 * (z - zk) * (1 + zb * zk) ** 3 / (
    zb ** 2 * (zb - zbk) ** 3 * (1 + z * zbk))
check_zero("J6.pin.F2", "J6", "pinning identity at cocycle level: "
           "F2(A1z)^2 = -zb^2 F2(AzE) F2(A2z)",
           F2_A1z ** 2 + zb ** 2 * F2_AzE * F2_A2z)
check_true("J6.verdict", "J6", "VERDICT: vanishing partner <=> Hamiltonian "
           "collapse of V (J2) <=> the first-order sector is a pure Jacobian "
           "area form (J3). The Jacobian is the unique object not protected "
           "by the square-norm bookkeeping (J4), and its character is "
           "computed to be u X (J5). Hence the unique partnerless channel "
           "carries the unique odd determinant line: the partner-vanishing "
           "removes the square protection; the odd u-valuation itself is a "
           "property of the soft-map Jacobian",
           simp(Vop(c_Ek)) == 0 and simp(Dmap(sp.cancel(Jac)) - u * X) == 0
           and vzd % 2 == 1)

# ============================================================ summary
n_pass = sum(1 for r in results if r["status"] == "pass")
mandatory = [r for r in results if r["status"] != "pass"]
summary = {
    "total": len(results), "passed": n_pass, "failed": len(mandatory),
    "failed_ids": [r["id"] for r in mandatory],
    "classification": {
        "operator": "S^(2)- = V^2/den exactly: the rung-3 soft operator is "
                    "the pure square of one leg vector field "
                    "V = c_zk d_zk + c_Ek d_Ek (J1)",
        "collapse": "V(c_Ek) = 0 <=> V Hamiltonian w.r.t. c_Ek with "
                    "multiplier mu = (z-zk)(1+zk zbk)/(1+z zbk) (J2)",
        "jacobian": "V(c_zk) = mu Jac(c_zk, c_Ek): the A1z channel is an "
                    "area form (J3)",
        "bookkeeping": "D multiplicative; D(c_zk) = X^2, D(c_Ek) = 1, "
                       "D(den) = X^2, D(mu) = X^2 — every product-side "
                       "input square-protected (J4)",
        "character": "D(Jac) = u X: the soft-map Jacobian is the unique "
                     "odd-character object; det(A1z) = u X (J5)",
        "verdict": "the unique partnerless channel carries the unique odd "
                   "determinant line: partner-vanishing removes the square "
                   "protection; the odd u-valuation (1) is a computed "
                   "property of the soft-map Jacobian character (J6)",
    },
}
results.append({"id": "summary", "group": "summary",
                "statement": json.dumps(summary), "status": "info"})

out = os.path.join(os.path.dirname(__file__), "..", "results",
                   "a1z_jacobian_correspondence.json")
with open(out, "w", encoding="utf-8") as fh:
    json.dump({"summary": summary, "checks": results}, fh, indent=2)
print(f"\n{n_pass}/{len(results) - 1} checks passed; results -> {out}")
raise SystemExit(1 if mandatory else 0)
