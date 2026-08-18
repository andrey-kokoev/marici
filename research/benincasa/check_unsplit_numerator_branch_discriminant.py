"""Test whether the literal unsplit occurrence numerator produces the source quartic."""

import json
from pathlib import Path
import sympy as sp

a,b,x,y,z=sp.symbols("a b x y z")
E=x+y+z
h=x**2+y**2-z**2
K=(
 x**2*a**4-h*a**2*b**2+y**2*b**4
 +(x**2*(x**2-y**2-z**2)+E**2*(y**2-x**2-z**2))*a**2
 +(y**2*(y**2-x**2-z**2)+E**2*(x**2-y**2-z**2))*b**2
 +z**2*E**4+E**2*z**2*(z**2-x**2-y**2)+z**2*x**2*y**2
)
ell1=x-y-z
ell2=x-y+z
ell3=x+y-z
ell4=E
A=ell1*ell2
B=ell3*ell4
Q=sp.expand(4*A*B-(A+B-E**2)**2)
Q_audit=-16*(x*y)**2-8*x*y*E**2+8*(x+y)*E**3-5*E**4
assert sp.expand(Q-Q_audit)==0
N=a+b-x-y
restriction=sp.factor(K.subs(b,x+y-a))
disc=sp.factor(sp.discriminant(restriction,a))
disc_poly=sp.Poly(disc,x,y,z)
q_poly=sp.Poly(Q,x,y,z)
gcd=sp.factor(sp.gcd(disc_poly,q_poly).as_expr())
quo,rem=sp.div(disc_poly,q_poly)
residual=sp.factor(disc / (-16*ell1**2*ell2**2*ell3**4*ell4**7))
result={
 "schema":"marici.unsplit-numerator-branch-discriminant.v1",
 "source_numerator":"a+b-x-y",
 "restriction_degree_in_a":int(sp.degree(restriction,a)),
 "discriminant_factorization":str(disc),
 "energy_letter_factor":"-16*ell1^2*ell2^2*ell3^4*ell4^7",
 "residual_degree":int(sp.total_degree(residual)),
 "residual_term_count":len(sp.Poly(residual,x,y,z).terms()),
 "quartic":str(sp.factor(Q)),
 "quartic_gcd_with_discriminant":str(gcd),
 "quartic_divides_discriminant":rem.is_zero,
 "classification":"coefficient_support" if rem.is_zero else "not_generated_by_unsplit_zero_divisor"
}
out=Path(__file__).with_name("unsplit-numerator-branch-discriminant.json")
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,sort_keys=True))
