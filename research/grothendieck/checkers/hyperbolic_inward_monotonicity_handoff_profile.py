"""High-precision profile of the compact-to-tail proof handoff."""

from __future__ import annotations
import mpmath as mp
import sympy as sp
from hyperbolic_inward_monotonicity_symbolic import generate,k,l,t


def main()->None:
    mp.mp.dps=80;_,_,q,m=generate();qp=sp.Poly(q,l);q2=qp.coeff_monomial(l**2);q1=qp.coeff_monomial(l);delta=sp.discriminant(q,l)
    _,rem=sp.div(sp.Poly(m,l,domain=sp.QQ.frac_field(t,k)),sp.Poly(q,l,domain=sp.QQ.frac_field(t,k)))
    numerator,_=sp.fraction(sp.cancel(rem.as_expr()));s=sp.cancel(-numerator/((1-t)**2*(1+t)**2));a=sp.diff(s,l);b=s.subs(l,0);c=sp.expand(-a*q1+2*q2*b);h=sp.factor(c*c-a*a*delta)
    p=sp.cancel(h/((t-1)*(t+1)*t**6*(3*t-1)**6*(3*t+1)**6));fq=sp.lambdify((t,l,k),q,"mpmath");fa=sp.lambdify((t,k),a,"mpmath");fc=sp.lambdify((t,k),c,"mpmath");fp=sp.lambdify((t,k),p,"mpmath")
    guess=mp.mpf("0.714")
    for zs in ("0.1","0.095","0.09","0.085","0.08","0.075"):
        z=mp.mpf(zs);kv=z**-2-1;fun=lambda holding:fq((mp.exp(holding)-z)/(mp.exp(holding)+z),holding,kv)
        holding=mp.findroot(fun,(guess*mp.mpf("0.98"),guess*mp.mpf("1.02")));guess=holding;e=mp.exp(holding);tv=(e-z)/(e+z);w=fp(tv,kv)*z**13*(e+z)**48/e**39
        print(zs,mp.nstr(kv,12),mp.nstr(fa(tv,kv),14),mp.nstr(fc(tv,kv),14),mp.nstr(w,14))


if __name__=="__main__":main()
