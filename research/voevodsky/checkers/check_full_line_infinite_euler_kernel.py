"""Positive transform, reflection, and endpoint-killing Cauchy fixtures."""
from pathlib import Path
import json
import sympy as s
q,z=s.symbols('q z')
Ps,Pq,ds,dq,lp=s.symbols('Ps Pq ds dq lp')
Lz=1/z+1/(z-1)-lp/2+ds/2-Ps
Lq=1/q+1/(q-1)-lp/2+dq/2-Pq
positive=(Ps+Pq+lp-(ds+dq)/2)/(z+q-1)-1/(z*(q-1))-1/((z-1)*q)
assert s.factor(positive+(Lz+Lq)/(z+q-1))==0
# Functional-equation reflection of the one-state negative transform.
reflected_negative=(-Lq-Lz)/(1-q-z)
assert s.factor(positive+reflected_negative)==0
# A conjugate-paired toy zero set, NOT a claim about actual zeta zeros.
rho=s.Rational(1,2)+s.I
roots=(rho,s.conjugate(rho))
B=s.prod((q-r)/(q-(6-s.conjugate(r))) for r in roots)
C=s.factor(q*(q-1)*B/(4-q)**8)
Ltoy=sum(1/(q-r) for r in roots)
assert s.simplify(Ltoy.subs(q,1-q)+Ltoy)==0
assert C.subs(q,0)==0 and C.subs(q,1)==0
assert C.subs(q,-1)!=0
LC=s.cancel(Ltoy*C)
for r in roots:
    assert s.residue(LC,q,r)==0
# Proper rational C and LC have all their poles to the right of sigma=2.
for f in (C,LC):
    num,den=s.fraction(s.cancel(f))
    assert s.degree(num,q)<s.degree(den,q)-2
    assert all(s.re(r)>2 for r in s.solve(den,q))
result={'passed':True,'checks':{'positive_source_transform_sign':True,
 'functional_equation_reflection':True,'both_source_endpoints_zero':True,
 'nonzero_source_cauchy_certificate':True,'zero_poles_cancel_in_LC':True,
 'proper_left_analytic_Cauchy_data':True},
 'scope':'Exact algebra and finite toy-zero fixtures only. The actual infinite-dimensional kernel uses the supplied xi Blaschke construction, polynomial endpoint factors, Cauchy integration and Laplace uniqueness. No ordinary L2 convergence of finite-place responses is tested or claimed.'}
ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/voevodsky/results/full-line-infinite-euler-kernel.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
