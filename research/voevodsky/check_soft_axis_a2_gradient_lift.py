"""Verify the three-gradient lift of the even a^2 commutator."""

import importlib.util
from fractions import Fraction as Q
from pathlib import Path

source = Path(__file__).with_name("check_soft_axis_deck_orbit_completion.py")
spec = importlib.util.spec_from_file_location("deck", source)
d = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d)

Ka = d.add(
    d.scale(d.power(d.a, 3), 4),
    d.scale(d.mul(d.u, d.a), 2),
    d.scale(d.mul(d.u, d.a, d.power(d.b, 2)), -2),
)
Ku = d.add(
    d.power(d.a, 2),
    d.scale(d.mul(d.power(d.a, 2), d.power(d.b, 2)), -1),
)

# The global Euler bridge from the principal differential to the retained
# deformation-gradient differential.
assert d.add(
    d.mul(d.scale(d.a, Q(1, 4)), Ka),
    d.mul(d.scale(d.u, Q(1, 2)), Ku),
) == d.K

sectors = ((1, 1), (1, 0), (0, 1), (0, 0))
for conjugate in (False, True):
    l2 = d.L2_plus if conjugate else d.L2_minus
    for sa, sb in sectors:
        ea, eb = 2 - sa, 2 - sb
        base = d.mul(d.power(d.L1, ea), d.power(l2, eb))
        for ai in range(4):
            for bi in range(4):
                f = d.mul(d.power(d.a, ai), d.power(d.b, bi))
                h = d.scale(d.mul(d.a, f, base), 2)
                Ha = d.mul(h, d.scale(d.a, Q(1, 4)))
                Hu = d.mul(h, d.scale(d.u, Q(1, 2)))
                lifted_boundary = d.add(d.mul(Ha, Ka), d.mul(Hu, Ku))
                commutator = d.scale(d.mul(d.a, f, base, d.K), 2)
                assert lifted_boundary == commutator

                # The lift is polynomial at a=0, b=0, and both incidence
                # endpoints; no division or chartwise certificate occurs.
                assert all(mon[0] >= 0 and mon[1] >= 0 and mon[2] >= 0
                           for mon in (*Ha.keys(), *Hu.keys()))

print("K=(a/4)K_a+(u/2)K_u: verified modulo u^2")
print("[q,a^2](f)=d_grad(h a/4, 0, h u/2)")
print("h=2 a f L1^ea L2^eb in every sector and deck lattice")
print("lift coefficients: H_a=(a^2/2)f base, H_u=u a f base")
print("verdict: Entry 504's commutator is nullhomotopic in the retained three-gradient complex")
