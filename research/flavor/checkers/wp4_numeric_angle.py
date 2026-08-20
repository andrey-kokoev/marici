"""WP4 high-precision numeric cross-check for the LO triangle mechanism.

The exact symbolic pipeline (wp4_triangle_lo.py) proves alpha_LO = phi for
S38 and validates its NLO coefficient against the paper's S42 formula.
Symbolic S43 is intractable for that pipeline (seesaw scales eps^10 with
16th-root-of-unity radicals), so here we certify BOTH textures
numerically at 60 digits:

  angle(R) = s * phi + eps^2 * w2 + O(eps^4),   s = +1 (S38 alpha),
                                                    s = -1 (S43 beta)
with w2 compared against the paper's printed NLO formulas:
  S38 at phi = pi/2  (S42):  w2 = -(d12 u12)/(d22 u22)
  S43 at phi = -pi/8 (S45):  w2 = -(1/2) sqrt(2 - sqrt(2))
                                    d13 d23^2 d33 u33
                                    / ((d32^2 + d33^2)^2 u13)

Method: exact-texture build, then numeric substitution of declared
rational edge values and two epsilon values (eps, eps/2); Hermitian
eigensystems via mpmath; the angle of the rephasing-invariant ratio
R (quartic in V, so eigenvector-phase independent); Richardson
extraction w2_est = (4 f(eps/2) - f(eps))/3 cancels the O(eps^4)
remainder, where f(eps) = (angle(R) - s*phi)/eps^2.

Inputs, precision, and digit agreement are printed for the ledger.
"""
import mpmath as mp
import sympy as sp
from harmonic_support import build, eps, EPHI

mp.mp.dps = 60

# fixed declared edge assignment (order-1 rationals, all distinct,
# avoiding accidental degeneracies); sorted symbol names map in order
EDGE_VALUES = [sp.Rational(11, 7), sp.Rational(5, 3), sp.Rational(13, 9),
               sp.Rational(7, 5), sp.Rational(17, 11), sp.Rational(3, 2),
               sp.Rational(19, 13), sp.Rational(2, 1), sp.Rational(23, 17),
               sp.Rational(29, 19), sp.Rational(31, 23), sp.Rational(37, 29)]


def paper_w2(name, vals):
    d = vals
    if name == "S38":  # phi = pi/2, S42
        return -(d["d12"] * d["u12"]) / (d["d22"] * d["u22"])
    if name == "S43":  # phi = -pi/8, S45 printed block
        return (-sp.Rational(1, 2) * sp.sqrt(2 - sp.sqrt(2))
                * d["d13"] * d["d23"]**2 * d["d33"] * d["u33"]
                / ((d["d32"]**2 + d["d33"]**2)**2 * d["u13"]))
    raise KeyError(name)


def numeric_angle(name, phi_val, eps_val):
    Yu, Yd = build(name)
    syms = sorted({s for M in (Yu, Yd) for e in M for s in e.free_symbols
                   if s not in (eps, EPHI) and str(s) != "phi"}, key=str)
    vals = dict(zip([str(s) for s in syms], EDGE_VALUES))
    subs = {s: v for s, v in zip(syms, EDGE_VALUES)}
    subs[eps] = eps_val
    subs[EPHI] = sp.exp(sp.I * phi_val)
    Yu = Yu.subs(subs)
    Yd = Yd.subs(subs)
    Hu = Yu * Yu.H
    Hd = Yd * Yd.H

    def to_mp(H):
        return mp.matrix([[mp.mpc(complex(sp.N(H[i, j], 60)))
                           for j in range(3)] for i in range(3)])

    def eigh_asc(Hm):
        E, ER = mp.eigh(Hm)
        order = sorted(range(3), key=lambda i: mp.re(E[i]))
        vecs = [[ER[k, j] for k in range(3)] for j in order]
        return vecs  # vecs[j] = eigenvector (list of 3) for j-th smallest

    Uu = eigh_asc(to_mp(Hu))
    Ud = eigh_asc(to_mp(Hd))
    V = [[sum(mp.conj(Uu[i][k]) * Ud[j][k] for k in range(3))
          for j in range(3)] for i in range(3)]

    if name == "S38":  # alpha: R = -(V_td conj(V_tb))/(V_ud conj(V_ub))
        R = -(V[2][0] * mp.conj(V[2][2])) / (V[0][0] * mp.conj(V[0][2]))
    else:              # beta:  R = -(V_cd conj(V_cb))/(V_td conj(V_tb))
        R = -(V[1][0] * mp.conj(V[1][2])) / (V[2][0] * mp.conj(V[2][2]))
        return -mp.arg(R), vals  # beta_LO = -arg(R) = -phi for S43
    return mp.arg(R), vals


def run_case(name, phi_val, sign):
    e1 = sp.Rational(1, 1000)
    out = {"texture": name, "phi": str(phi_val), "sign": sign,
           "epsilons": [str(e1), str(e1 / 2)], "dps": mp.mp.dps}
    a1, vals = numeric_angle(name, phi_val, e1)
    a2, _ = numeric_angle(name, phi_val, e1 / 2)
    phi_mp = mp.mpf(str(phi_val.evalf(60)))
    e1m, e2m = mp.mpf(10)**-3, mp.mpf(10)**-3 / 2
    g1, g2 = a1 - sign * phi_mp, a2 - sign * phi_mp
    f1, f2 = g1 / e1m**2, g2 / e2m**2
    w2_est = (4 * f2 - f1) / 3
    w2_paper = mp.mpf(str(paper_w2(name, vals).evalf(60)))
    out["edge_assignment"] = {k: str(v) for k, v in vals.items()}
    out["angle_minus_LO_at_eps"] = mp.nstr(g1, 25)
    out["angle_minus_LO_at_eps_half"] = mp.nstr(g2, 25)
    out["LO_rate_ratio(expect 4)"] = mp.nstr(g1 / g2, 25)
    out["w2_richardson"] = mp.nstr(w2_est, 30)
    out["w2_paper"] = mp.nstr(w2_paper, 30)
    out["abs_diff"] = mp.nstr(abs(w2_est - w2_paper), 5)
    out["digits_agree"] = int(-mp.log10(abs(w2_est - w2_paper)
                                        / abs(w2_paper)))
    for k, v in out.items():
        print(f"  {k}: {v}")
    return out


if __name__ == "__main__":
    import json
    res = {}
    print("S38 (alpha, phi=pi/2):")
    res["S38"] = run_case("S38", sp.pi / 2, +1)
    print("S43 (beta, phi=-pi/8):")
    res["S43"] = run_case("S43", -sp.pi / 8, -1)
    with open("results/wp4_numeric_angle.json", "w",
              encoding="utf-8") as fh:
        json.dump(res, fh, indent=2, default=str)
    print("written results/wp4_numeric_angle.json")
