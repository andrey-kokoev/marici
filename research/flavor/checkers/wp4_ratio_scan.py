"""Exploratory: args of all nine row-pair unitarity-triangle ratios for a
texture at one epsilon, to locate which quartet carries the LO phase."""
import sys
import mpmath as mp
import sympy as sp
from harmonic_support import build, eps, EPHI

mp.mp.dps = 60

EDGE_VALUES = [sp.Rational(11, 7), sp.Rational(5, 3), sp.Rational(13, 9),
               sp.Rational(7, 5), sp.Rational(17, 11), sp.Rational(3, 2),
               sp.Rational(19, 13), sp.Rational(2, 1), sp.Rational(23, 17),
               sp.Rational(29, 19), sp.Rational(31, 23), sp.Rational(37, 29)]

name = sys.argv[1] if len(sys.argv) > 1 else "S43"
phi_val = sp.Rational(sys.argv[2]) * sp.pi if len(sys.argv) > 2 else -sp.pi / 8
eps_val = sp.Rational(1, 1000)

Yu, Yd = build(name)
syms = sorted({s for M in (Yu, Yd) for e in M for s in e.free_symbols
               if s not in (eps, EPHI) and str(s) != "phi"}, key=str)
subs = dict(zip(syms, EDGE_VALUES))
subs[eps] = eps_val
subs[EPHI] = sp.exp(sp.I * phi_val)
Yu, Yd = Yu.subs(subs), Yd.subs(subs)
Hu, Hd = Yu * Yu.H, Yd * Yd.H


def to_mp(H):
    return mp.matrix([[mp.mpc(complex(sp.N(H[i, j], 60)))
                       for j in range(3)] for i in range(3)])


def eigh_asc(Hm):
    E, ER = mp.eigh(Hm)
    order = sorted(range(3), key=lambda i: mp.re(E[i]))
    return [[ER[k, j] for k in range(3)] for j in order]


Uu, Ud = eigh_asc(to_mp(Hu)), eigh_asc(to_mp(Hd))
V = [[sum(mp.conj(Uu[i][k]) * Ud[j][k] for k in range(3))
      for j in range(3)] for i in range(3)]

target = float(sp.N(phi_val, 20))
print(f"{name} at eps={eps_val}, phi={phi_val} ({target})")
for i, j in ((0, 1), (0, 2), (1, 2)):
    for a, b in ((0, 1), (0, 2), (1, 2)):
        R = -(V[i][a] * mp.conj(V[i][b])) / (V[j][a] * mp.conj(V[j][b]))
        arg = float(mp.arg(R))
        mark = "  <== ~phi" if abs(abs(arg) - abs(target)) < 1e-6 else ""
        print(f"rows({i},{j}) cols({a},{b}): arg={arg:+.12f}{mark}")
