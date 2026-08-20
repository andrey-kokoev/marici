"""Compare pipeline V elements vs the paper's printed S45/S47 expansions
for S43 at eps=1e-3, phi=-pi/8, declared rational edges (same assignment
as wp4_numeric_angle.py)."""
import mpmath as mp
import sympy as sp
from harmonic_support import build, eps, EPHI

mp.mp.dps = 60

EDGE_VALUES = [sp.Rational(11, 7), sp.Rational(5, 3), sp.Rational(13, 9),
               sp.Rational(7, 5), sp.Rational(17, 11), sp.Rational(3, 2),
               sp.Rational(19, 13), sp.Rational(2, 1), sp.Rational(23, 17)]

Yu, Yd = build("S43")
syms = sorted({s for M in (Yu, Yd) for e in M for s in e.free_symbols
               if s not in (eps, EPHI) and str(s) != "phi"}, key=str)
subs = dict(zip(syms, EDGE_VALUES))
subs[eps] = sp.Rational(1, 1000)
subs[EPHI] = sp.exp(-sp.I * sp.pi / 8)
Yu, Yd = Yu.subs(subs), Yd.subs(subs)

v = {str(s): mp.mpf(str(val)) for s, val in zip(syms, EDGE_VALUES)}
e = mp.mpf(10)**-3
phi = -mp.pi / 8
ephi = mp.exp(1j * phi)


def to_mp(H):
    return mp.matrix([[mp.mpc(complex(sp.N(H[i, j], 60)))
                       for j in range(3)] for i in range(3)])


def eigh_asc(Hm):
    E, ER = mp.eigh(Hm)
    order = sorted(range(3), key=lambda i: mp.re(E[i]))
    return [[ER[k, j] for k in range(3)] for j in order]


Uu = eigh_asc(to_mp(Yu * Yu.H))
Ud = eigh_asc(to_mp(Yd * Yd.H))
V = [[sum(mp.conj(Uu[i][k]) * Ud[j][k] for k in range(3))
      for j in range(3)] for i in range(3)]

d13, d23, d32, d33 = v["d13"], v["d23"], v["d32"], v["d33"]
u13, u33 = v["u13"], v["u33"]
Dn = d32**2 + d33**2

paper = {
    "V_cb": (-d23 * d33 / Dn * ephi * e
             + d23**3 * d33 * (2 * d32**2 - d33**2) / (2 * Dn**3)
             * ephi * e**3),
    "V_cd": (-d13 / d23 * e
             + (d13**3 / (2 * d23**3) - d13 * d23 * d33**2 / (2 * Dn**2))
             * e**3),
    "V_td": (u13 / u33 * e**2
             + (d13 * d23**2 * d33 / Dn**2 * mp.conj(ephi)
                - u13 * d13**2 / (2 * u33 * d23**2)) * e**4),
    "V_tb": 1 - d23**2 * d33**2 / (2 * Dn**2) * e**2,
    "V_us": d13 / d23 * e,
}
mine = {"V_cb": V[1][2], "V_cd": V[1][0], "V_td": V[2][0],
        "V_tb": V[2][2], "V_us": V[0][1]}

for k in paper:
    diff = abs(paper[k] - mine[k])
    print(f"{k}: paper={mp.nstr(paper[k], 12)}")
    print(f"      mine ={mp.nstr(mine[k], 12)}   |diff|={mp.nstr(diff, 3)}")

R_paper = -(paper["V_cd"] * mp.conj(paper["V_cb"])) / \
          (paper["V_td"] * mp.conj(paper["V_tb"]))
R_mine = -(mine["V_cd"] * mp.conj(mine["V_cb"])) / \
         (mine["V_td"] * mp.conj(mine["V_tb"]))
print("arg(R) paper-elements:", mp.nstr(mp.arg(R_paper), 20),
      " vs -phi =", mp.nstr(-phi, 20))
print("arg(R) mine          :", mp.nstr(mp.arg(R_mine), 20),
      " vs +phi =", mp.nstr(phi, 20))
