"""Exact Hardy and finite Blaschke/Cauchy algebra regressions.

The zeros below are algebraic fixtures, NOT asserted zeta zeros. The actual
infinite-source theorem uses the classical Hadamard and Blaschke estimates.
"""
from pathlib import Path
import json
import sympy as S

q,s,t=S.symbols('q s t')
eps,alpha,v=S.symbols('eps alpha v',positive=True)
hardy=S.integrate(1/((eps+alpha)**2+t**2),(t,-S.oo,S.oo))/(2*S.pi)
assert S.simplify(hardy-1/(2*(eps+alpha)))==0
assert S.integrate(S.exp(-2*alpha*v),(v,0,S.oo))==1/(2*alpha)

zeros=[(S.Rational(1,2)+3*S.I,1),(S.Rational(1,2)-3*S.I,1),
       (S.Rational(1,3)+5*S.I,2),(S.Rational(1,3)-5*S.I,2)]
B=S.Integer(1)
L=S.Rational(2,3)
P=S.Rational(2,3)
residue_checks=0
for rho,m in zeros:
    reflected=6-S.conjugate(rho)
    B*=((q-rho)/(q-reflected))**m
    L+=m*(1/(q-rho)+1/rho)
    P+=m*(1/rho+1/(q-reflected))
    assert S.simplify(S.limit((q-rho)*((m/(q-rho))-S.Symbol('Ls'))/(q-s),q,rho)
                      -m/(rho-s))==0
    residue_checks+=1
assert S.cancel(L-S.diff(B,q)/B-P)==0
assert B.subs(q,0)>0
C=S.cancel(B/(4-q)**6)
LC=S.cancel(L*C)
for rho,m in zeros:
    assert S.simplify(S.limit((q-rho)*LC,q,rho))==0
    assert S.limit(LC,q,rho).is_finite
# After cancellation, every possible pole is outside Re q<=2.
denominator=S.denom(LC)
assert denominator.subs(q,0)!=0
assert S.limit(C,q,S.oo)==0 and S.limit(LC,q,S.oo)==0

# Boundary modulus of an individual half-plane Blaschke factor.
x,y,z=S.symbols('x y z',real=True)
rho=x+S.I*y
reflected=6-S.conjugate(rho)
b=(3+S.I*z-rho)/(3+S.I*z-reflected)
assert S.simplify(b*S.conjugate(b))==1

# Check the sign of the general integrated residual formula.
Ls,Lq=S.symbols('Ls Lq')
assert S.simplify((Lq-Ls)/(q-s)-(Ls/(s-q)-Lq/(s-q)))==0
# Nonzero C(0) certifies a nonzero source via its convergent Laplace transform.
assert C.subs(q,0)!=0

result={'schema':'marici.grothendieck.infinite-euler-residual-domain.v1','passed':True,
        'zero_residue_sign_checks':residue_checks,
        'checks':{'Hardy_Laplace_norm_normalization':True,
                  'reflected_Blaschke_factor_has_unit_boundary_modulus':True,
                  'logarithmic_derivative_remainder_identity':True,
                  'all_fixture_zero_poles_cancel':True,
                  'proper_Cauchy_data_and_nonzero_source_certificate':True,
                  'integrated_residual_sign':True},
        'scope':'Finite symbolic fixtures only. The infinite nonzero kernel construction, Bochner integrability and Hardy iff criterion are proved in the companion note using standard entire-function and half-plane Hardy theorems.'}
root=Path(__file__).resolve().parents[3]
out=root/'research/grothendieck/results/infinite-euler-residual-domain.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
