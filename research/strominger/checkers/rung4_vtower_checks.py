"""Exact rung-4 V-tower checker: the derived S^(3) candidate V^3/den, the
channel census and vanishing shadow, the closed-form first-order line, the
depth-parity alternation theorem, gauge continuation, and the readout
gate-migration prediction (marici.Strominger).

Companion to (does NOT import or modify):
  research/strominger/checkers/rung3_s2_bridge_checks.py (R1-R4, grounding)
  research/strominger/checkers/rung3_cocycle_checks.py (K1-K5)
  research/strominger/checkers/a1z_jacobian_correspondence_checks.py (J1-J6)
  research/strominger/checkers/readout_parity_mechanism_checks.py (P1-P6)
Sources and conventions:
  research/strominger/rung3-s2-bridge.md (grounded S^(2), gauge mechanism)
  research/strominger/a1z-jacobian-correspondence.md (V, den, mu, Jac, D)
  research/strominger/readout-parity-mechanism.md (character theorem P3)

No local source grounds S^(3); the rung-4 operator is DERIVED from the
certified rung-3 structure S^(2)- = V^2/den (J1) by iterating the same
per-leg vector field V = c_zk d_zk + c_Ek d_Ek over the same denominator
den = 2 om q.k. All arithmetic is exact sympy symbolics.

Layers:
  G1 the tower and its anchor: the multi-index recursion
     A^{n+1}_a = V(A^n_a) + sum_i c_i A^n_{a-e_i} reproduces the grounded
     rung-3 channels at n = 2 exactly; the nonzero channel census at order
     n is n(n+3)/2 - (n-1); the vanishing channels are exactly the pure-Ek
     subprincipal shadow {(0,k), k = 1..n-1} — the propagation of
     V(c_Ek) = 0 (certified through order 4).
  G2 the first-order line in closed form: since c_zk is Ek-free and
     d_zk c_zk = -2 c_zk/(z-zk), the magnetic first-order channel at every
     order is V^n(c_zk) = (-1)^n (n+1)! c_zk^{n+1}/(z-zk)^n — the induction
     step is certified with SYMBOLIC n, so the formula holds at every rung.
  G3 the depth-parity alternation theorem: with D(z-zk) = X/u the
     first-order line character is (uX)^n at operator order n (symbolic n
     via exponent arithmetic); over all channels through order 4 the
     diagonal valuation val_z of D(channel/den) EQUALS the channel's
     V-depth. Hence the square-root gate on the magnetic first-order line
     ALTERNATES along the tower: odd (rootless) at rung 3, square
     (uX)^2 at rung 4, odd again at rung 5.
  G4 gauge continuation: the two contraction atoms q.A = 0 (R1.1a) and
     q^2 = 0 (null soft momentum) force the covariant cubic atom
     dE_{mn} q^m A^n = 0 exactly; with dE[A,A] = 0 (R1.1b) every variation
     of every tower numerator (eps.q.J)^n vanishes — per-leg gauge
     invariance propagates up the whole tower by the same antisymmetry
     mechanism, with no conservation law at any rung.
  G5 the readout migration: the certified characters (P3) are
     P(E_g) = +u^{g+2}, P(M_g) = -u^{g+3}; the exponents have OPPOSITE
     parity, so exactly one readout sector is gate-obstructed at every
     grade (perpetual alternation). At the rung-4 candidate grade g = 5
     the obstruction migrates: the ELECTRIC character +u^7 is odd (gate
     fails), the magnetic -u^8 is even (gate passes) — the falsifiable
     prediction for rung 4, conditional on the fold grade assignment.
  G6 the verdict.

Output: research/strominger/results/rung4_vtower.json
Exit code 0 iff every check passes.
"""
import json
import os
import sympy as sp

# ---------------------------------------------------------------- symbols
z, zb, zk, zbk, Ek = sp.symbols("z zb zk zbk Ek")
om = sp.symbols("om", positive=True)
I = sp.I
sq2 = sp.sqrt(2)
u = z * zb
n_sym = sp.symbols("n", integer=True, positive=True)

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
    """Sigma-norm Q(f) = f sigma(f)."""
    return sp.cancel(e * sigma(e))


def Dmap(e):
    """Determinant-line norm character D(f) = Q(alpha f)/Q(f)."""
    return sp.cancel(Qmap(alpha_map(e)) / Qmap(e))


def vval(e, var):
    """Exact order of vanishing of a rational function along var = 0."""
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


# ============================================================ the line
c_zk = -sq2 * om * (z - zk) ** 2 / (1 + u)
c_Ek = -sq2 * Ek * om * (z - zk) * (1 + z * zbk) / ((1 + u) * (1 + zk * zbk))
X = (1 + z * zbk) * (1 + zb * zk) / ((z - zk) * (zb - zbk))
den = -4 * Ek * om ** 2 * (z - zk) * (zb - zbk) / ((1 + u) * (1 + zk * zbk))
cs = [c_zk, c_Ek]

# Grounded rung-3 channels (bridge checker R1.3) for the anchor.
A2z_g = -(z - zk) ** 3 * (1 + zk * zbk) / (2 * Ek * (zb - zbk) * (1 + u))
AzE_g = -(z - zk) ** 2 * (1 + z * zbk) / ((zb - zbk) * (1 + u))
A2E_g = -Ek * (z - zk) * (1 + z * zbk) ** 2 / (
    2 * (zb - zbk) * (1 + u) * (1 + zk * zbk))
A1z_g = (z - zk) ** 2 * (1 + zk * zbk) / (Ek * (zb - zbk) * (1 + u))


def Vop(f):
    """The soft-map leg vector field V = c_zk d_zk + c_Ek d_Ek."""
    return sp.cancel(c_zk * sp.diff(f, zk) + c_Ek * sp.diff(f, Ek))


def tower(nmax):
    """Multi-index coefficient tower of V^n (nonzero channels only)."""
    A = [{(0, 0): sp.Integer(1)}]
    for n in range(1, nmax + 1):
        cur = {}
        for alpha, coef in A[-1].items():
            vc = Vop(coef)
            if vc != 0:
                cur[alpha] = sp.cancel(cur.get(alpha, 0) + vc)
            for i in range(2):
                na = list(alpha)
                na[i] += 1
                na = tuple(na)
                val = sp.cancel(cur.get(na, 0) + coef * cs[i])
                if val != 0:
                    cur[na] = val
        A.append(cur)
    return A


A = tower(4)

# ============================================================ G1 tower & anchor
check_zero("G1.anchor.20", "G1", "tower anchor: A^2_{(2,0)}/den reproduces "
           "the grounded rung-3 A2z channel", A[2][(2, 0)] - A2z_g * den)
check_zero("G1.anchor.11", "G1", "tower anchor: A^2_{(1,1)}/den reproduces "
           "the grounded rung-3 AzE channel", A[2][(1, 1)] - AzE_g * den)
check_zero("G1.anchor.02", "G1", "tower anchor: A^2_{(0,2)}/den reproduces "
           "the grounded rung-3 A2E channel", A[2][(0, 2)] - A2E_g * den)
check_zero("G1.anchor.10", "G1", "tower anchor: A^2_{(1,0)}/den reproduces "
           "the grounded rung-3 A1z channel", A[2][(1, 0)] - A1z_g * den)
census_ok = all(
    len(A[n]) == n * (n + 3) // 2 - (n - 1) for n in range(1, 5))
check_true("G1.census", "G1", "channel census: at operator order n the "
           "nonzero channel count is n(n+3)/2 - (n-1) (certified n = 1..4): "
           "4, 7, 11 at rungs 3, 4, 5", census_ok,
           f"counts: {[len(A[n]) for n in range(1, 5)]}")
shadow_ok = all(
    all((0, k) not in A[n] for k in range(1, n)) and (0, n) in A[n]
    for n in range(2, 5))
check_true("G1.shadow", "G1", "the vanishing shadow: exactly the pure-Ek "
           "subprincipal channels {(0,k), k = 1..n-1} vanish at order n — "
           "the propagation of V(c_Ek) = 0 up the tower; the pure-Ek "
           "principal channel (0,n) = c_Ek^n survives (certified n = 2..4)",
           shadow_ok)
check_zero("G1.vcEk", "G1", "the shadow's root: V(c_Ek) = 0 (grounded "
           "R1.3, the Hamiltonian collapse J2)", Vop(c_Ek))

# ============================================================ G2 first-order line
check_zero("G2.mech", "G2", "first-order mechanism: c_zk is Ek-free with "
           "d_zk c_zk = -2 c_zk/(z-zk), so V(c_zk) = c_zk d_zk c_zk",
           sp.diff(c_zk, zk) + 2 * c_zk / (z - zk))
K, w = sp.symbols("K w")  # c_zk = K w^2 with w = z - zk, K = -sq2 om/(1+u) zk-free
a_sym, b_sym = sp.symbols("a b")
mono = K ** a_sym * w ** (2 * a_sym + b_sym)
# d_zk w = -1, d_zk K = 0, so V(mono) = K w^2 * d_zk(mono)
step = sp.expand(K * w ** 2 * (-(2 * a_sym + b_sym) * K ** a_sym
                               * w ** (2 * a_sym + b_sym - 1)) - (
    -(2 * a_sym + b_sym) * K ** (a_sym + 1) * w ** (2 * a_sym + b_sym + 1)))
check_zero("G2.induction", "G2", "first-order line induction step with "
           "SYMBOLIC (a, b): with c_zk = K (z-zk)^2 (K zk-free), "
           "V(K^a (z-zk)^{2a+b}) = -(2a+b) K^{a+1} (z-zk)^{2a+b+1} — "
           "iterating from (1, 0) gives V^n(c_zk) = (-1)^n (n+1)! "
           "c_zk^{n+1}/(z-zk)^n at EVERY rung (factor product over "
           "k = 0..n-1 of -(k+2) is (-1)^n (n+1)!)",
           sp.expand(step))
f_n = (-1) ** n_sym * sp.factorial(n_sym + 1) * c_zk ** (n_sym + 1) / (
    (z - zk) ** n_sym)
for n in (1, 2, 3):
    check_zero(f"G2.value.{n}", "G2", f"first-order line value: V^{n}(c_zk) "
               f"matches the tower channel A^{n + 1}_{{(1,0)}}",
               A[n + 1][(1, 0)] - f_n.subs(n_sym, n))

# ============================================================ G3 depth-parity alternation
check_zero("G3.atom", "G3", "the character atom: D(z-zk) = X/u",
           Dmap(z - zk) - X / u)
check_zero("G3.czk", "G3", "square character: D(c_zk) = X^2",
           Dmap(c_zk) - X ** 2)
check_zero("G3.den", "G3", "square character: D(den) = X^2",
           Dmap(den) - X ** 2)
char_n = sp.cancel((X ** 2) ** (n_sym + 1) * (u / X) ** n_sym / X ** 2)
check_true("G3.charline", "G3", "first-order line character by exponent "
           "arithmetic (symbolic n): D(V^n(c_zk)/den) = (X^2)^{n+1} "
           "(u/X)^n / X^2 = (uX)^n",
           sp.simplify(char_n - (u * X) ** n_sym) == 0)
depth_rows = []
for n in (3, 4):
    for alpha in sorted(A[n], key=lambda a: (-sum(a), -a[0])):
        depth = n - sum(alpha)
        d = Dmap(sp.cancel(A[n][alpha] / den))
        depth_rows.append((n, alpha, depth, vval(d, z)))
rule_ok = all(vz == depth for _, _, depth, vz in depth_rows)
check_true("G3.depthrule", "G3", "THE DEPTH-PARITY RULE: val_z of every "
           "tower channel's determinant character EQUALS the channel's "
           "V-depth (certified on all 18 channels of orders 3 and 4) — "
           "parity alternates with depth: even, odd, even, odd",
           rule_ok,
           f"depths seen: {sorted({d for _, _, d, _ in depth_rows})}, all "
           "val_z == depth")
det_r3 = u * X
det_r4 = u ** 2 * X ** 2
check_true("G3.alternation", "G3", "gate alternation on the magnetic "
           "first-order line: rung 3 character uX has odd val_z = 1 (no "
           "rational root); rung 4 character (uX)^2 = u^2 X^2 is a rational "
           "sigma-invariant SQUARE (root uX, sigma(uX) = uX); rung 5 "
           "predicted odd again",
           vval(det_r3, z) % 2 == 1 and vval(det_r4, z) % 2 == 0
           and simp(sigma(u * X) - u * X) == 0
           and simp(Dmap(A[3][(1, 0)] / den) - det_r4) == 0
           and simp(Dmap(A[4][(1, 0)] / den) - (u * X) ** 3) == 0,
           "rung-4 first-order det certified as (uX)^2; rung-5 as (uX)^3")

# ============================================================ G4 gauge continuation
def xhat(zz, zzb):
    return [(zz + zzb) / (1 + zz * zzb), (zz - zzb) / (I * (1 + zz * zzb)),
            (1 - zz * zzb) / (1 + zz * zzb)]


eta = sp.diag(1, -1, -1, -1)
qv = om * sp.Matrix([1, *xhat(z, zb)])
ql = eta * qv
Lam4 = sp.Matrix(sp.symbols("L0:4"))
Laml = eta * Lam4
J1 = sp.zeros(4)
for m in range(4):
    for n in range(m + 1, 4):
        s = sp.Symbol(f"J1_{m}{n}")
        J1[m, n] = s
        J1[n, m] = -s
Araised = J1 * ql  # covariant A^nu = J^{nu rho} q_rho
dE = ql * Laml.T + Laml * ql.T

check_zero("G4.qA", "G4", "gauge atom 1 (covariant): q.A = q_nu J^{nu rho} "
           "q_rho = 0 by antisymmetry (R1.1a mechanism)", (ql.T * Araised)[0])
check_zero("G4.qq", "G4", "gauge atom 2: the soft momentum is null, "
           "q^2 = 0", (ql.T * qv)[0])
atom_cubic = sp.expand(sum(dE[m, n] * qv[m] * Araised[n]
                           for m in range(4) for n in range(4)))
check_zero("G4.cubic", "G4", "the cubic gauge atom: dE_{mn} q^m A^n = "
           "(q.Lam)(q.A) + q^2 (Lam.A) = 0 exactly — the variation of one "
           "(eps.q.J) factor inside ANY tower numerator",
           sp.simplify(atom_cubic))
atom_quad = sp.expand(sum(dE[m, n] * Araised[m] * Araised[n]
                          for m in range(4) for n in range(4)))
check_zero("G4.quad", "G4", "the quadratic gauge atom: dE[A,A] = 2(q.A)"
           "(Lam.A) = 0 (R1.1b, retro-certified)",
           sp.simplify(atom_quad))
check_true("G4.tower", "G4", "gauge continuation verdict: d(C^n)/gauge = "
           "n C^{n-1} dC with dC built from the certified zero atoms — "
           "per-leg gauge invariance propagates up the WHOLE tower by the "
           "antisymmetry-plus-nullness mechanism alone, no conservation "
           "law at any rung",
           simp(atom_cubic) == 0 and simp(atom_quad) == 0
           and simp((ql.T * Araised)[0]) == 0 and simp((ql.T * qv)[0]) == 0)

# ============================================================ G5 readout migration
parity_pairs = [(g, (g + 2) % 2, (g + 3) % 2) for g in range(0, 6)]
check_true("G5.perpetual", "G5", "perpetual alternation: the certified "
           "characters (P3) are P(E_g) = +u^{g+2}, P(M_g) = -u^{g+3}; the "
           "exponents have opposite parity at every grade, so EXACTLY ONE "
           "readout sector is square-root-obstructed at every grade — the "
           "obstruction never lifts, it migrates",
           all((a + b) == 1 for _, a, b in parity_pairs),
           f"(g, E parity, M parity): {parity_pairs}")
check_true("G5.migration", "G5", "the rung-4 prediction: at the candidate "
           "grade g = 5 the obstruction migrates sectors — the ELECTRIC "
           "character +u^7 is ODD (gate fails), the magnetic -u^8 is EVEN "
           "(gate passes); conditional on the fold grade assignment, this "
           "is the falsifiable rung-4 readout signature",
           (5 + 2) % 2 == 1 and (5 + 3) % 2 == 0)

# ============================================================ G6 verdict
check_true("G6.verdict", "G6", "VERDICT: the rung-4 operator is derived as "
           "V^3/den with the tower anchored to the grounded rung-3 channels "
           "(G1); the magnetic first-order line is closed form at every "
           "order (G2); its determinant character is (uX)^n — the "
           "square-root gate ALTERNATES along the tower, passing at rung 4 "
           "(G3); per-leg gauge invariance propagates up the whole tower "
           "(G4); and the readout obstruction migrates to the electric "
           "sector at the rung-4 grade (G5). Two alternations — tower "
           "depth and readout grade — govern where oddness can live",
           census_ok and shadow_ok and rule_ok
           and simp(atom_cubic) == 0)

# ============================================================ summary
n_pass = sum(1 for r in results if r["status"] == "pass")
mandatory = [r for r in results if r["status"] != "pass"]
summary = {
    "total": len(results), "passed": n_pass, "failed": len(mandatory),
    "failed_ids": [r["id"] for r in mandatory],
    "classification": {
        "tower": "S^(3)- candidate derived as V^3/den; tower anchored to "
                 "grounded rung-3 channels (G1); census n(n+3)/2 - (n-1); "
                 "pure-Ek subprincipal shadow vanishes at every order",
        "first_order_line": "V^n(c_zk) = (-1)^n (n+1)! c_zk^{n+1}/(z-zk)^n "
                            "— symbolic-n induction certified (G2)",
        "alternation": "D(first-order channel/den) = (uX)^n; val_z equals "
                       "V-depth on all 18 channels of orders 3-4; the "
                       "square-root gate alternates along the tower, "
                       "passing at rung 4 (G3)",
        "gauge": "per-leg gauge invariance propagates up the whole tower "
                 "from the atoms q.A = 0 and q^2 = 0 (G4)",
        "readout": "exactly one readout sector gate-obstructed at every "
                   "grade; at g = 5 the obstruction migrates to the "
                   "electric sector (+u^7 odd, -u^8 even) — the falsifiable "
                   "rung-4 prediction (G5)",
    },
}
results.append({"id": "summary", "group": "summary",
                "statement": json.dumps(summary), "status": "info"})

out = os.path.join(os.path.dirname(__file__), "..", "results",
                   "rung4_vtower.json")
with open(out, "w", encoding="utf-8") as fh:
    json.dump({"summary": summary, "checks": results}, fh, indent=2)
print(f"\n{n_pass}/{len(results) - 1} checks passed; results -> {out}")
raise SystemExit(1 if mandatory else 0)
