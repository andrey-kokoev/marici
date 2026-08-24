"""Exact Bregman form and differential identities for the source offset."""

import sympy as sp

p, q = sp.symbols("p q", real=True)
a, b = sp.atanh(p), sp.atanh(q)
delta = sp.Rational(1, 2)*(p*(a-b)-sp.log(sp.cosh(a))+sp.log(sp.cosh(b)))

print("Delta=", delta)
print("Delta_p_reserve=", sp.simplify(sp.diff(delta,p)-(a-b)/2))
print("Delta_q_reserve=", sp.simplify(
    sp.diff(delta,q)+(p-q)/(2*(1-q**2))
))
print("Delta_qq=", sp.factor(sp.diff(delta,q,2)))
print("Delta_pq=", sp.factor(sp.diff(delta,p,q)))
print("Delta_pp=", sp.factor(sp.diff(delta,p,2)))
