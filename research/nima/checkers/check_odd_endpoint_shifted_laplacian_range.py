"""Exact shifted-Laplacian endpoint range test and Dirichlet comparison.

This is a comparison energy, not identification with the semilocal two-space
bulk operator. The endpoint coefficient c is retained as an external source
input, not chosen by this checker.
"""
import json
from pathlib import Path
import sympy as s


def zero(expr):
    return s.simplify(s.expand_trig(expr.rewrite(s.exp)))==0


def main():
    x=s.symbols('x',real=True)
    L=s.symbols('L',positive=True)
    h=s.sinh(x/2)
    delta=s.sinh(L)-L
    H=lambda f:-s.diff(f,x,2)+f/4
    # H_D w=h, w(+/-L)=0, obtained by solving the resonant ODE.
    w=L*s.coth(L/2)*s.sinh(x/2)-x*s.cosh(x/2)
    N=L*s.coth(L/2)*delta-(L*s.cosh(L)-s.sinh(L))
    ell=N/delta
    margin=L*(L*s.coth(L/2)-2)/delta
    h2=s.integrate(h*h,(x,-L,L))
    mixed=s.integrate(x*s.sinh(x/2)*s.cosh(x/2),(x,-L,L))
    # The bare second-order residual kills the endpoint mode, but the
    # differentiated Dirichlet Green form need not kill its dual functional.
    checks={
        'odd_endpoint_is_bare_residual_kernel':zero(H(h)),
        'endpoint_norm_exact':zero(h2-delta),
        'resonant_green_solution':zero(H(w)-h),
        'right_dirichlet_boundary':zero(w.subs(x,L)),
        'left_dirichlet_boundary':zero(w.subs(x,-L)),
        'mixed_integral_exact':zero(mixed-(L*s.cosh(L)-s.sinh(L))),
        'leverage_numerator_exact':zero(L*s.coth(L/2)*h2-mixed-N),
        'unit_coefficient_margin_identity':zero(1-ell-margin),
        'source_endpoint_squared_norm':zero(s.integrate(2*h*h,(x,-L,L))-2*delta),
        'small_interval_leverage':s.limit(ell/L**2,L,0,dir='+')==s.Rational(1,15),
        'large_interval_leverage':s.limit(ell,L,s.oo)==1,
        'unnormalized_endpoint_leverage_diverges':s.limit(2*N,L,s.oo)==s.oo,
    }
    assert all(checks.values()),checks
    result={
        'schema':'marici.nima.odd-endpoint-shifted-laplacian-range.v1',
        'strength':'exact_comparison_domain_theorem_not_semilocal_identification',
        'checks':checks,
        'domain_hostile':'On an unrestricted H2 interval domain, h=sinh(x/2) has zero ||P h||^2 and nonzero endpoint overlap.',
        'dirichlet_energy':'integral(|f_prime|^2+|f|^2/4), domain H_0^1(-L,L)',
        'normalized_endpoint':'v=sinh(x/2)/sqrt(sinh(L)-L)',
        'leverage':'ell_D=1-L*(L*coth(L/2)-2)/(sinh(L)-L)',
        'sharp_gate':'H_D >= c*v*v^* iff c*ell_D <= 1, for c>=0',
        'unit_coefficient_result':'0<ell_D<1 for every finite L>0; ell_D tends to 1',
        'unnormalized_endpoint_result':'b=sqrt(2)*sinh(x/2) has leverage 2*(sinh(L)-L)*ell_D, unbounded as L grows',
        'missing_source_arrow':'A boundary-domain-compatible comparison from the differentiated canonical/dual bulk energy to H_D, transporting the actual endpoint coefficient c_k.',
        'physical_schur_gate_proved':False,
    }
    out=Path(__file__).resolve().parents[1]/'results/odd-endpoint-shifted-laplacian-range.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
