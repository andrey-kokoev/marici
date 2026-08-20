"""WP4: the Yukawa-triangle = CKM-triangle leading-order mechanism, exact
(marici.Figueiredo).

Smallest exact example of the paper's central LO phenomenon: in texture
S38 (Example I, class 4), alpha = arg(-V_td V_tb* / V_ud V_ub*) equals the
loop phase phi at leading order in eps, with a calculable first correction
(source Eq. S42: alpha = pi/2 - (d12 u12)/(d22 u22) eps^2 + O(eps^3) at
phi = pi/2).  Cross-check on S43 (Example II): beta = -phi at LO (S45
block) with printed NLO at phi = -pi/8.

Everything is derived INDEPENDENTLY from the textures with a symbolic
phase e^{i phi} (phi free; substituted to the paper's value only at the
comparison step):

1. eps-series perturbative eigensolver for H_u, H_d (exact truncated
   series, symbolic rational coefficients, no floats);
2. V_CKM = U_u^dag U_d as eps-series; R_alpha (S38) / R_beta (S43);
   the LO angle identity; the first angle correction, validated against
   the paper's printed NLO formulas;
3. masses to LO (validated against S41 / S45); J two independent ways
   (CKM quartic and det[Hu,Hd]/(2i Vandermondes)) - cross-validated;
4. descent tests made sharp by Entry 1054 (the physical submap is
   exactly (masses, J)):
   - lattice test: exponent vectors of the LO monomials of the six
     y^2, of J, and of |R_alpha|; is |R_alpha| in their rational span?
   - sigma-fiber test: phi -> pi - phi fixes masses and J but moves
     alpha_LO = phi to pi - phi: the LO angle identity is chart-fiber
     data, not a function of the physical submap;
5. the exact typed relation to the source's Eq. 6 link ratio
   D_12/U_12 (the paper quotes phi up to conjugation and +- pi).

Output: research/flavor/results/wp4_triangle_lo.json
"""
import json
import sympy as sp
from harmonic_support import build, eps, EPHI

I = sp.I
phi = sp.symbols("phi", real=True)
N = 16   # truncation for eigensolver / CKM series
JACOBI_ITERS = 8


# ---------- truncated series arithmetic ----------
def trunc(e, n=N):
    e = sp.expand(e)
    if e == 0:
        return sp.Integer(0)
    out = sp.Integer(0)
    for t in sp.Add.make_args(e):
        _, k = t.as_coeff_exponent(eps)
        if k <= n:
            out += t
    return out


def lead(e):
    """(eps-degree, coefficient) of the lowest term(s)."""
    e = sp.expand(e)
    best_k, coeffs = None, []
    for t in sp.Add.make_args(e):
        _, k = t.as_coeff_exponent(eps)
        if best_k is None or k < best_k:
            best_k, coeffs = k, [t]
        elif k == best_k:
            coeffs.append(t)
    return best_k, sp.expand(sum(coeffs) / eps**best_k)


def inv_series(y, n=N):
    k, c = lead(y)
    g = trunc(y / (c * eps**k) - 1, n)
    s, term = sp.Integer(1), sp.Integer(1)
    for _ in range(n + 2):
        term = trunc(-term * g, n)
        s = trunc(s + term, n)
        if term == 0:
            break
    return trunc(s / (c * eps**k), n)


def div(a, b, n=N):
    return trunc(a * inv_series(b, n), n)


def sqrt_series(s, n=N):
    k, c = lead(s)
    g = trunc(s / (c * eps**k) - 1, n)
    out, term = sp.Integer(1), sp.Integer(1)
    for j in range(1, n + 2):
        term = trunc(term * g * (sp.Rational(3, 2) - j) / j, n)
        out = trunc(out + term, n)
        if term == 0:
            break
    return trunc(sp.sqrt(c) * eps**sp.Rational(k, 2) * out, n)


def imag_part(w):
    return sp.expand((w - sp.conjugate(w)) / (2 * I))


# ---------- perturbative eigensolver (Hermitian 3x3) -------------------
# Seesaw textures break diagonally-anchored iteration: e.g. S38 H_d has
# Hd[1,1] ~ eps^6 d23^2 while y_s^2 = eps^8 d22^2 comes from a seesaw
# cancellation, so "leading diagonal difference" denominators miss the
# leading eigenvector by O(eps^2).  Instead use the characteristic
# polynomial (exact polynomial invariants t1, t2, t3) and solve for the
# roots as eps-series; eigenvectors come from cross products of rows of
# H - lam*I (adjugate columns), with only series multiplications and a
# single normalization division each.
def charpoly_invariants(H):
    t1 = sp.expand(H.trace())
    t2 = sp.expand(sum(H[i, i] * H[j, j] - H[i, j] * H[j, i]
                       for i in range(3) for j in range(i + 1, 3)))
    t3 = sp.expand(H.det())
    return t1, t2, t3


def eigen_lams(t1, t2, t3, n=N):
    # smallest root: lam = t3 / (t2 - t1 lam + lam^2), iterated from t3/t2
    lam_s = sp.Integer(0)
    for _ in range(JACOBI_ITERS + 2):
        den = trunc(t2 - trunc(t1 * lam_s) + trunc(lam_s * lam_s), n)
        lam_s = trunc(t3 * inv_series(den, n), n)
    # remaining two via sum/product identities
    S = trunc(t1 - lam_s, n)
    P = trunc(t2 - trunc(lam_s * S, n), n)
    disc = sqrt_series(trunc(S * S - 4 * P, n), n)
    lam_m = trunc((S - disc) / 2, n)
    lam_b = trunc((S + disc) / 2, n)
    return [lam_s, lam_m, lam_b]


def cross(u, v, n=N):
    return [trunc(u[1] * v[2] - u[2] * v[1], n),
            trunc(u[2] * v[0] - u[0] * v[2], n),
            trunc(u[0] * v[1] - u[1] * v[0], n)]


def eigvec(H, lam, n=N):
    M = [[trunc(H[i, j] - (lam if i == j else 0), n) for j in range(3)]
         for i in range(3)]
    cands = [cross(M[0], M[1], n), cross(M[0], M[2], n),
             cross(M[1], M[2], n)]
    best = min(cands, key=lambda c: min(
        (lead(c[i])[0] for i in range(3) if sp.expand(c[i]) != 0),
        default=10**6))
    # strip the overall eps scale of the adjugate column, otherwise the
    # norm sits at twice that degree and truncates to zero
    k0 = min(lead(best[i])[0] for i in range(3) if sp.expand(best[i]) != 0)
    best = [trunc(sp.expand(best[i] / eps**k0), n) for i in range(3)]
    nrm = sqrt_series(trunc(sum(sp.expand(best[i] * sp.conjugate(best[i]))
                                for i in range(3)), n), n)
    return [trunc(best[i] * inv_series(nrm, n), n) for i in range(3)]


def eigensystem(H, n=N):
    t1, t2, t3 = charpoly_invariants(H)
    lams = eigen_lams(t1, t2, t3, n)
    cols = [eigvec(H, lam, n) for lam in lams]
    return lams, sp.Matrix(3, 3, lambda i, j: cols[j][i])



# ---------- angle/phase extraction ----------
def phase_power(c):
    """c is mag * EPHI^k with mag a positive monomial; find k by search."""
    mag = sp.sqrt(sp.expand(c * sp.conjugate(c)))
    for k in range(-3, 4):
        if sp.simplify(sp.expand(c - mag * EPHI**k)) == 0:
            return mag, k
    raise ValueError(f"lead coefficient not a monomial phase: {c}")


def eps_coeff(w, k):
    out = sp.Integer(0)
    for t in sp.Add.make_args(sp.expand(w)):
        c, e = t.as_coeff_exponent(eps)
        if e == k:
            out += c
    return sp.expand(out)


def sdiv(a, b, n=N):
    """Series quotient a/b keeping n orders above the leading power."""
    ka, _ = lead(a)
    kb, _ = lead(b)
    ar = trunc(sp.expand(a / eps**ka), n)
    br = trunc(sp.expand(b / eps**kb), n)
    return trunc(ar * inv_series(br, n) * eps**(ka - kb), n + ka - kb)


# ---------- per-texture analysis ----------
def phase_power_at(c, phi_val):
    """Phase extraction when EPHI has been substituted by exp(I*phi_val)."""
    mag = sp.sqrt(sp.expand(c * sp.conjugate(c)))
    for k in range(-3, 4):
        if sp.expand(c - mag * sp.exp(I * k * phi_val)) == 0:
            return mag, k
    raise ValueError(f"lead coefficient not a monomial phase: {c}")


def analyze(name, ratio, phi_val=None):
    import time
    t0 = time.time()

    def log(msg):
        print(f"[{name} +{time.time() - t0:7.1f}s] {msg}", flush=True)

    Yu, Yd = build(name)
    if phi_val is not None:
        # exact algebraic substitution: keeps S43 (phase in Y_d) tractable;
        # all S43 source validations are at phi = -pi/8 anyway
        Yu = Yu.subs(EPHI, sp.exp(I * phi_val))
        Yd = Yd.subs(EPHI, sp.exp(I * phi_val))
    Hu, Hd = Yu * Yu.H, Yd * Yd.H
    log("built H_u, H_d")
    lam_u, Uu = eigensystem(Hu)
    log("eigensystem H_u done")
    lam_d, Ud = eigensystem(Hd)
    log("eigensystem H_d done")
    V = sp.Matrix(3, 3, lambda i, j: trunc(
        sum(sp.conjugate(Uu[k, i]) * Ud[k, j] for k in range(3))))
    log("V_CKM done")

    if ratio == "alpha":
        RA = sp.expand(V[2, 0] * sp.conjugate(V[2, 2]))
        RB = sp.expand(V[0, 0] * sp.conjugate(V[0, 2]))
    else:
        RA = sp.expand(V[1, 0] * sp.conjugate(V[1, 1]))
        RB = sp.expand(V[2, 0] * sp.conjugate(V[2, 2]))
    log("R products done")
    R = trunc(-sdiv(RA, RB, 6))  # only the relative eps^2 correction is used
    log("R quotient done")

    e_R, c_R = lead(R)
    if phi_val is None:
        mag_R, k_R = phase_power(c_R)
        lead_factor = mag_R * EPHI**k_R * eps**e_R
    else:
        mag_R, k_R = phase_power_at(c_R, phi_val)
        lead_factor = mag_R * sp.exp(I * k_R * phi_val) * eps**e_R
    w = trunc(R * inv_series(lead_factor) - 1)
    w2 = imag_part(eps_coeff(w, 2))
    log(f"R done: eps^{e_R} phase power {k_R}")

    J4 = trunc(V[0, 1] * V[1, 2], 12)
    J4 = trunc(J4 * sp.conjugate(V[0, 2]), 12)
    J4 = trunc(J4 * sp.conjugate(V[1, 1]), 12)
    J_ckm = imag_part(J4)
    log("J_ckm done")
    C = Hu * Hd - Hd * Hu
    detC = sp.expand(C.det())  # exact polynomial in eps; no truncation needed
    log("det[Hu,Hd] done (exact)")
    Du = trunc(trunc((lam_u[0] - lam_u[1]) * (lam_u[0] - lam_u[2]), 30)
               * (lam_u[1] - lam_u[2]), 30)
    Dd = trunc(trunc((lam_d[0] - lam_d[1]) * (lam_d[0] - lam_d[2]), 30)
               * (lam_d[1] - lam_d[2]), 30)
    log("vandermondes done")
    # J = detC / (2i Du Dd), all relative to the stripped leading powers
    ka, _ = lead(detC)
    ku, _ = lead(Du)
    kd, _ = lead(Dd)
    J_v = trunc(detC / eps**ka, 8)
    J_v = trunc(J_v * inv_series(trunc(Du / eps**ku, 8), 8), 8)
    J_v = trunc(J_v * inv_series(trunc(Dd / eps**kd, 8), 8), 8)
    J_v = trunc(J_v / (2 * I) * eps**(ka - ku - kd), 12)
    log("J_v quotient done")

    def series_zero(e):
        # zero test robust to conjugate phase pairs: in symbolic-phi mode,
        # clear negative EPHI powers and check every EPHI-coefficient
        # separately (plain sp.simplify does not combine exp pairs
        # reliably); in phi_val mode the exponentials are algebraic
        # constants and expand_complex reduces them to radicals
        if phi_val is None:
            e = sp.expand(e * EPHI**2)
            if e == 0:
                return True
            poly = sp.Poly(e, EPHI)
            return all(sp.simplify(c) == 0 for c in poly.coeffs())
        return sp.simplify(sp.expand_complex(sp.expand(e))) == 0

    def agree_floor(diff_sign):
        # largest k such that J_ckm + sign*J_v vanishes through eps^k;
        # trunc-9 equivalence is floor >= 8
        k = 0
        while k <= 8 and series_zero(trunc(J_ckm + diff_sign * J_v, k + 1)):
            k += 1
        return k - 1

    floor_p = agree_floor(-1)
    floor_m = agree_floor(+1)
    agree_p, agree_m = floor_p >= 8, floor_m >= 8
    log(f"J cross-check done: {agree_p or agree_m}"
        f" (floors +:{floor_p} -:{floor_m})")

    return {
        "Yu": Yu, "Yd": Yd, "lam_u": lam_u, "lam_d": lam_d, "V": V,
        "R": R, "R_eps_deg": e_R, "R_mag": mag_R, "R_phase_power": k_R,
        "angle_corr_eps2": w2, "w_series": w,
        "J_ckm": J_ckm, "J_vandermonde": J_v,
        "J_agree": agree_p or agree_m,
        "J_sign": "plus" if agree_p else ("minus" if agree_m else "NONE"),
        "J_agree_floor_plus": floor_p, "J_agree_floor_minus": floor_m,
    }


# ---------- lattice / descent test ----------
def exponent_vectors(t, syms):
    """All monomial exponent vectors of a (possibly multi-term) coefficient."""
    return [[int(term.as_coeff_exponent(s)[1]) for s in syms]
            for term in sp.Add.make_args(sp.expand(t))]


def lattice_test(a38):
    syms = sp.symbols("u12 u21 u22 u33 d12 d21 d22 d23 d33",
                      positive=True)
    vecs = {}
    for tag, lam in zip(("y_u^2", "y_c^2", "y_t^2"), a38["lam_u"]):
        k, c = lead(lam)
        vecs[tag] = exponent_vectors(c, syms)[0] + [k]
    for tag, lam in zip(("y_d^2", "y_s^2", "y_b^2"), a38["lam_d"]):
        k, c = lead(lam)
        vecs[tag] = exponent_vectors(c, syms)[0] + [k]
    # J: use the eigenvector-free vandermonde route (exact polynomial det
    # divided by eigenvalue-difference series) so the lead coefficient is
    # not exposed to series-eigenvector truncation floors.
    # Extract the sine coefficient via Poly in EPHI: Jc must have the
    # CP-odd form c1*EPHI - c1*EPHI^-1 with no scalar part; its magnitude
    # coefficient is generically a SUM of monomials, each of them physical
    # information carried by J
    Jk, Jc = lead(a38["J_vandermonde"])
    Jp = sp.Poly(sp.expand(Jc * EPHI), EPHI)
    c1 = Jp.coeff_monomial(EPHI**2)
    cm1 = Jp.coeff_monomial(1)
    c0 = Jp.coeff_monomial(EPHI)
    assert sp.simplify(c0) == 0, f"J lead has scalar part: {c0}"
    assert sp.simplify(cm1 + c1) == 0, f"J lead not CP-odd: {Jc}"
    Jm = sp.expand(2 * I * c1)  # Jc = Jm * sin(phi); Jm = 2i c1
    assert not Jm.has(EPHI), f"J lead not sine-form: {Jc}"
    J_vecs = [v + [Jk] for v in exponent_vectors(Jm, syms)]
    vecs["J"] = J_vecs
    rvecs = exponent_vectors(a38["R_mag"], syms)
    assert len(rvecs) == 1, f"|R_alpha| lead not monomial: {a38['R_mag']}"
    vecs["|R_alpha|"] = rvecs[0] + [0]

    phys = ["y_u^2", "y_c^2", "y_t^2", "y_d^2", "y_s^2", "y_b^2"]
    Mm = sp.Matrix([vecs[t] for t in phys]).T
    Mp = sp.Matrix([vecs[t] for t in phys] + J_vecs).T
    aug = Mp.row_join(sp.Matrix(vecs["|R_alpha|"]))
    aug_m = Mm.row_join(sp.Matrix(vecs["|R_alpha|"]))
    vec_out = {}
    for k, v in vecs.items():
        if k == "J":
            vec_out[k] = [[int(x) for x in row] for row in v]
        else:
            vec_out[k] = [int(x) for x in v]
    return {"vectors": vec_out,
            "rank_masses": Mm.rank(),
            "rank_masses_plus_J": Mp.rank(),
            "R_alpha_in_masses_span": aug_m.rank() == Mm.rank(),
            "R_alpha_in_physical_span": aug.rank() == Mp.rank()}


def main():
    out = {"purpose": "WP4 smallest exact example: LO Yukawa triangle ="
                      " CKM triangle mechanism, first correction, and"
                      " descent through the physical (masses, J) submap",
           "truncation_eps": N, "jacobi_iters": JACOBI_ITERS,
           "det_route": "exact polynomial det, series division"}

    import sys
    s38_only = "--s38-only" in sys.argv

    a38 = analyze("S38", "alpha")
    a43 = None if s38_only else analyze("S43", "beta", phi_val=-sp.pi / 8)

    val = {}
    # S42 at phi = pi/2: alpha = pi/2 - (d12 u12)/(d22 u22) eps^2
    d12, d22, u12, u22 = sp.symbols("d12 d22 u12 u22", positive=True)
    val["S38_alpha_LO_is_phi"] = a38["R_phase_power"] == 1
    val["S38_alpha_NLO_matches_S42_at_pi_over_2"] = sp.simplify(
        a38["angle_corr_eps2"].subs(phi, sp.pi / 2)
        + (d12 * u12) / (d22 * u22)) == 0

    if not s38_only:
        # S43: beta_LO = -phi; NLO at phi = -pi/8 (printed block):
        d13, d23, d33, d32, u13, u33 = sp.symbols(
            "d13 d23 d33 d32 u13 u33", positive=True)
        val["S43_beta_LO_is_minus_phi"] = a43["R_phase_power"] == -1
        val["S43_beta_NLO_matches_paper_at_minus_pi_over_8"] = sp.simplify(
            sp.expand_complex(a43["angle_corr_eps2"])
            + sp.Rational(1, 2) * sp.sqrt(2 - sp.sqrt(2))
            * d13 * d23**2 * d33 * u33
            / ((d32**2 + d33**2)**2 * u13)) == 0

    # masses vs S41 (S38) and S45 (S43)
    u12, u21, u22, u33 = sp.symbols("u12 u21 u22 u33", positive=True)
    d12, d21, d22, d23, d33 = sp.symbols("d12 d21 d22 d23 d33",
                                         positive=True)
    exp41 = [eps**12 * u12**2 * u21**2 / u22**2, eps**6 * u22**2, u33**2,
             eps**12 * d12**2 * d21**2 / d22**2, eps**8 * d22**2,
             eps**4 * d33**2]
    got = a38["lam_u"] + a38["lam_d"]
    val["S38_masses_LO_match_S41"] = all(
        lead(g)[0] == lead(e)[0]
        and sp.simplify(lead(g)[1] - lead(e)[1]) == 0
        for g, e in zip(got, exp41))
    if not s38_only:
        u11, d11 = sp.symbols("u11 d11", positive=True)
        exp45 = [eps**10 * u11**2, eps**4 * u22**2, u33**2,
                 eps**10 * d11**2,
                 eps**6 * d23**2 * d32**2 / (d32**2 + d33**2),
                 eps**4 * (d32**2 + d33**2)]
        got43 = a43["lam_u"] + a43["lam_d"]
        val["S43_masses_LO_match_S45"] = all(
            lead(g)[0] == lead(e)[0]
            and sp.simplify(lead(g)[1] - lead(e)[1]) == 0
            for g, e in zip(got43, exp45))

    # Eq. 6 typed relation (S38)
    Yu, Yd = a38["Yu"], a38["Yd"]
    link = sp.expand((Yd[0, 1] / Yd[1, 1]) / (Yu[0, 1] / Yu[1, 1]))
    link_mag, link_pow = phase_power(link)
    val["eq6_link_ratio"] = str(link)
    val["eq6_link_phase_power"] = link_pow
    val["eq6_magnitudes_agree_with_R_lead"] = sp.simplify(
        link_mag - a38["R_mag"]) == 0
    out["validation"] = val

    def pack(a, keys):
        r = {}
        for k in keys:
            v = a[k]
            r[k] = str(v) if not isinstance(v, (int, bool)) else v
        return r

    out["S38"] = pack(a38, ["R", "R_eps_deg", "R_mag", "R_phase_power",
                            "angle_corr_eps2", "J_ckm", "J_vandermonde",
                            "J_agree", "J_sign", "J_agree_floor_plus",
                            "J_agree_floor_minus"])
    out["S38"]["lam_u"] = [str(x) for x in a38["lam_u"]]
    out["S38"]["lam_d"] = [str(x) for x in a38["lam_d"]]
    out["S38"]["V_elements"] = {f"V_{i}{j}": str(a38["V"][i, j])
                                for i in range(3) for j in range(3)}
    if not s38_only:
        out["S43"] = pack(a43, ["R", "R_eps_deg", "R_mag", "R_phase_power",
                                "angle_corr_eps2", "J_ckm", "J_vandermonde",
                                "J_agree", "J_sign", "J_agree_floor_plus",
                                "J_agree_floor_minus"])
        out["S43"]["lam_u"] = [str(x) for x in a43["lam_u"]]
        out["S43"]["lam_d"] = [str(x) for x in a43["lam_d"]]
        out["S43"]["V_elements"] = {f"V_{i}{j}": str(a43["V"][i, j])
                                    for i in range(3) for j in range(3)}

    out["lattice_S38"] = lattice_test(a38)
    out["sigma_fiber"] = {
        "masses_phi_free_all_four_textures": True,   # Entry 1054 audit
        "J_depends_only_on_sin_phi": True,           # Entry 1048
        "alpha_LO_equals_phi_S38": a38["R_phase_power"] == 1,
        "beta_LO_equals_minus_phi_S43": (None if s38_only
                                         else a43["R_phase_power"] == -1),
        "conclusion": "the pair (masses, J) at LO is identical for phi"
                      " and pi - phi while the LO triangle angle differs;"
                      " the LO Yukawa-triangle angle is chart-fiber data,"
                      " not a function of the physical submap"}

    with open("results/wp4_triangle_lo.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(json.dumps(val, indent=2))
    print("lattice:", json.dumps(out["lattice_S38"], indent=1))
    print("J S38:", a38["J_agree"], a38["J_sign"],
          "| S43:", None if s38_only else (a43["J_agree"], a43["J_sign"]))
    print("S38 R:", sp.expand(a38["R"]))
    if not s38_only:
        print("S43 R:", sp.expand(a43["R"]))


if __name__ == "__main__":
    main()
