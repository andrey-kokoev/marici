"""Generate the exact denominator-free inward monotonicity polynomial.

This is a symbolic discovery checker.  It reconstructs the epsilon expansion
without logarithms by using tanh addition around the limiting coordinate t.
"""

from __future__ import annotations

import sympy as sp


e,t,l,k=sp.symbols("e t l k")


def truncate(expression:sp.Expr,order:int=4)->sp.Expr:
    return sp.series(expression,e,0,order).removeO().expand()


def shifted_tanh(y:sp.Expr)->sp.Expr:
    """Series for tanh(atanh(t)+y), where y=O(e)."""
    z=truncate(y-y**3/3)
    return truncate((t+z)*sp.series(1/(1+t*z),e,0,4).removeO())


def flow(expression:sp.Expr)->sp.Expr:
    return sp.diff(expression,l)+(1-t*t)*sp.diff(expression,t)/2


def generate()->tuple[sp.Expr,sp.Expr,sp.Expr,sp.Expr]:
    d=sum((((1+k)**n-1)/(sp.Integer(2)*n*2**n))*e**n for n in range(1,4))
    tt=shifted_tanh(d/2)
    rr=shifted_tanh(-d/2-e*l/2)
    p=1-e;q=1-(1+k)*e
    n=tt**4+tt**2*p*q-tt*(p+q)*rr+(1-2*tt**2-tt**2*p*q)*rr**2+tt*(p+q)*rr**3
    series=sp.Poly(truncate(n),e)
    phi=sp.factor(series.coeff_monomial(e**2))
    psi=sp.factor(series.coeff_monomial(e**3))
    qpoly=sp.cancel(flow(phi)/(1-t*t))
    p2=flow(flow(phi));b=flow(psi);c=flow(b);d3=flow(p2)
    reserve=sp.expand(p2*c-b*d3+3*p2*p2)
    margin=sp.expand(sp.diff(reserve,k)*flow(qpoly)-flow(reserve)*sp.diff(qpoly,k))
    return phi,psi,sp.factor(qpoly),margin


def main()->None:
    phi,psi,qpoly,margin=generate()
    poly=sp.Poly(margin,t,l,k)
    # The critical equation is quadratic in the holding L.  Divide in L over
    # QQ(t,k), rather than using a multivariate monomial order, so the exact
    # restriction to Q=0 becomes affine in L.
    quotient_l,remainder_l=sp.div(sp.Poly(margin,l,domain=sp.QQ.frac_field(t,k)),sp.Poly(qpoly,l,domain=sp.QQ.frac_field(t,k)))
    remainder=sp.cancel(remainder_l.as_expr())
    numerator,denominator=sp.fraction(remainder)
    remainder_poly=sp.Poly(numerator,t,l,k)
    print(f"phi_terms={len(sp.Poly(phi,t,l,k).terms())}")
    print(f"psi_terms={len(sp.Poly(psi,t,l,k).terms())}")
    print(f"Q_terms={len(sp.Poly(qpoly,t,l,k).terms())}")
    print(f"M_terms={len(poly.terms())}")
    print(f"M_degrees={(poly.degree(t),poly.degree(l),poly.degree(k))}")
    print(f"M_mod_Q_numerator_terms={len(remainder_poly.terms())}")
    print(f"M_mod_Q_numerator_degrees={(remainder_poly.degree(t),remainder_poly.degree(l),remainder_poly.degree(k))}")
    print(f"M_mod_Q_denominator_terms={len(sp.Poly(denominator,t,k).terms())}")
    print(f"M_mod_Q_denominator_factor={sp.factor(denominator)}")
    stripped=sp.cancel(-numerator/((1-t)**2*(1+t)**2))
    stripped_poly=sp.Poly(stripped,l)
    assert stripped_poly.degree()==1
    a=sp.Poly(stripped_poly.coeff_monomial(l),t,k)
    b=sp.Poly(stripped_poly.coeff_monomial(1),t,k)
    print("M_mod_Q_structure=-(1-t^2)^2*(A(t,k)*L+B(t,k))/denominator")
    print(f"A_terms={len(a.terms())}; A_degrees={(a.degree(t),a.degree(k))}")
    print(f"B_terms={len(b.terms())}; B_degrees={(b.degree(t),b.degree(k))}")
    assert sp.cancel(margin-quotient_l.as_expr()*qpoly-remainder)==0


if __name__=="__main__":main()
