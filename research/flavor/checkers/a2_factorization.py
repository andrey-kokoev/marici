"""Rank-one factorization of the second-harmonic coefficient a_2.

Ledger 1048 left open: does connected b1 = 1 force a_2 = 0 in
det[Hu, Hd] = sum_m a_m (z^m - z^{-m})?  The toggle map
(m2_toggle_map.py) gave exact data but no criterion.

Derivation (phase in one entry of the up sector; the down-sector case
is symmetric).  Write Yu(z) = Y0 + zB, B = b E_{pq} the single
phase-carrying entry.  Then

    Hu(z) = H0 + zA + z^{-1} A^dag,   A = B Y0^dag = u v^dag,

with u = e_p, v = b * (column q of Y0); v^dag u = b (Y0)_{pq} ... note
A^2 = u (v^dag u) v^dag is NOT zero a priori: A^2 = (v^dag u) A.
[Nilpotency holds only when (Y0)_{pq} = 0, i.e. the phase entry is the
ONLY nonzero in its slot -- true here since the phase edge replaces the
real entry, so column q of Y0 has zero in row p.  The checker VERIFIES
A^2 = 0 rather than assuming it.]

C = [Hu, Hd] is traceless, so det C = (1/3) tr C^3 and

    a_2 = tr(C0 Y^2),   Y = [A, Hd],   C0 = [H0, Hd].

With A^2 = 0:  Y^2 = (v^dag Hd u) {A, Hd} - (v^dag Hd^2 u) A, hence

    a_2 = (v^dag Hd u)(v^dag {C0, Hd} u) - (v^dag Hd^2 u)(v^dag C0 u).

For phase in the DOWN sector, swap roles: Hd(z) = H0 + zA + z^-1 A^dag,
C0 = [Hu, H0], Y = [Hu, A] = -[A, Hu], and

    a_2 = (v^dag Hu u)(v^dag {C0, Hu} u) - (v^dag Hu^2 u)(v^dag C0 u),

with u = e_p, v = b * (column q of D0) for the phase entry b E_{pq} of
Yd.

This checker verifies the factorization EXACTLY (symbolic) against the
directly computed a_2 polynomials stored in results/m2_toggle_map.json
(all 18 toggle rows) and against fresh direct computations for the four
baselines.  It also reports which of the four sandwich factors vanish
identically per row -- the empirical seed of a graph criterion.

Output: research/flavor/results/a2_factorization.json
"""
import json
import sympy as sp
from harmonic_support import build, laurent_coeffs, eps, EPHI

x = sp.symbols("x", positive=True, real=True)


def split_phase(Y, phase_pos):
    """Split Y(z) = Y0 + z B at the phase position (p, q) 0-based."""
    p, q = phase_pos
    Y0 = Y.copy()
    entry = Y0[p, q]
    Y0[p, q] = 0
    b = sp.simplify(entry / EPHI)
    return Y0, p, q, b


def sandwiches(Yu0, Yd0, phase_sector, p, q, b):
    """Return dict of the four sandwich scalars and A^2 check."""
    Hu0 = Yu0 * Yu0.H
    Hd0 = Yd0 * Yd0.H
    u = sp.Matrix.zeros(3, 1)
    u[p] = 1
    src = Yu0 if phase_sector == "u" else Yd0
    v = b * src[:, q]
    A = u * v.H
    A2_zero = sp.simplify(A * A) == sp.Matrix.zeros(3)
    if phase_sector == "u":
        Hs, Ho = Hu0, Hd0      # Hs = z-carrying sector's H0; Ho = other
    else:
        Hs, Ho = Hd0, Hu0
    C0 = Hu0 * Hd0 - Hd0 * Hu0
    vd = v.H
    out = {
        "A2_is_zero": A2_zero == True or A2_zero,
        "vHo_u": sp.expand((vd * Ho * u)[0]),
        "vHo2_u": sp.expand((vd * Ho * Ho * u)[0]),
        "vC0_u": sp.expand((vd * C0 * u)[0]),
        "vC0Ho_HoC0_u": sp.expand((vd * (C0 * Ho + Ho * C0) * u)[0]),
    }
    out["a2_factored"] = sp.expand(
        out["vHo_u"] * out["vC0Ho_HoC0_u"] - out["vHo2_u"] * out["vC0_u"])
    return out


def direct_a2(Yu, Yd):
    Hu, Hd = Yu * Yu.H, Yd * Yd.H
    C = Hu * Hd - Hd * Hu
    return sp.expand(laurent_coeffs(C.det()).get(2, 0))


PHASE_POS = {"S38": ("u", (0, 1)), "S43": ("d", (2, 2)),
             "S48": ("d", (0, 1)), "S53": ("d", (1, 1))}


def check_row(name, sec_added=None, pos_added=None):
    Yu, Yd = build(name)
    if sec_added:
        (Yu if sec_added == "u" else Yd)[pos_added[0], pos_added[1]] = x
    sec, (p, q) = PHASE_POS[name]
    Yu0, Yd0 = Yu.copy(), Yd.copy()
    if sec == "u":
        Y0mat, pp, qq, b = split_phase(Yu0, (p, q))
        sw = sandwiches(Y0mat, Yd0, "u", pp, qq, b)
    else:
        Y0mat, pp, qq, b = split_phase(Yd0, (p, q))
        sw = sandwiches(Yu0, Y0mat, "d", pp, qq, b)
    a2_direct = direct_a2(Yu, Yd)
    diff = sp.simplify(sw["a2_factored"] - a2_direct)
    zero = lambda e: sp.simplify(e) == 0
    return {
        "A2_is_zero": bool(sw["A2_is_zero"]),
        "factorization_exact": diff == 0,
        "a2_zero": zero(a2_direct),
        "vHo_u_zero": zero(sw["vHo_u"]),
        "vHo2_u_zero": zero(sw["vHo2_u"]),
        "vC0_u_zero": zero(sw["vC0_u"]),
        "vC0Ho_HoC0_u_zero": zero(sw["vC0Ho_HoC0_u"]),
    }


def main():
    toggles = json.load(open("results/m2_toggle_map.json"))
    out = {"purpose": "verify a_2 = (vHo u)(v{C0,Ho}u) - (vHo^2 u)(vC0 u) "
                      "against direct computation; record which sandwich "
                      "factors vanish per row",
           "rows": {}}
    for name in ("S38", "S43", "S48", "S53"):
        key = f"{name} baseline"
        out["rows"][key] = check_row(name)
        print(key, out["rows"][key], flush=True)
    for name in ("S38", "S43"):
        for t in toggles["textures"][name]["toggles"]:
            sec, i, j = t["added_edge"]
            key = f"{name} +{sec}{i}{j}"
            out["rows"][key] = check_row(name, sec, (i - 1, j - 1))
            print(key, out["rows"][key], flush=True)
    with open("results/a2_factorization.json", "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    bad = [k for k, r in out["rows"].items() if not r["factorization_exact"]]
    print("factorization failures:", bad or "none")


if __name__ == "__main__":
    main()
