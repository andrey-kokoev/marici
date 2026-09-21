"""Exact escape-profile checks; PNT and operator estimates are proved in note."""
from pathlib import Path
import json
import math
import sympy as S

x,t=S.symbols('x t',positive=True)
# Endpoint-zero exponential fixture; NOT an asserted arithmetic kernel source.
f=S.exp(-2*x)*(S.Rational(8,15)-S.Rational(32,15)*x+x*x)
assert S.integrate(S.exp(x/2)*f,(x,0,S.oo))==0
assert S.integrate(S.exp(-x/2)*f,(x,0,S.oo))==0
hm=S.simplify(S.exp(-t/2)*S.integrate(S.exp(x/2)*f,(x,0,t)))
hp=S.simplify(S.exp(t/2)*S.integrate(S.exp(-x/2)*f,(x,t,S.oo)))
assert S.simplify(hm+S.exp(-t/2)*S.integrate(S.exp(x/2)*f,(x,t,S.oo)))==0
assert S.simplify(hp+S.exp(t/2)*S.integrate(S.exp(-x/2)*f,(x,0,t)))==0
assert S.simplify(S.diff(hm,t)+hm/2-f.subs(x,t))==0
assert S.simplify(S.diff(hp,t)-hp/2+f.subs(x,t))==0
assert hm!=0 and hp!=0

P=S.symbols('P',positive=True)
gamma,sigma=S.symbols('gamma sigma',real=True)
alpha=sigma-S.Rational(1,2)
assert S.simplify(alpha-S.Rational(1,2)+1-2*sigma)==-sigma
assert S.simplify(-alpha-S.Rational(1,2)+1-sigma)==1-2*sigma
for sign in [-1,1]:
    log_weight=-2*gamma*(S.log(P)+sign*t)
    assert S.expand(S.log(P)+log_weight-(1-2*gamma)*S.log(P)+2*gamma*sign*t)==0
z=S.symbols('z')
assert S.factor(1/(1-z)-1-z-z*z/(1-z))==0

ff=S.lambdify(x,f,'math')
mf=S.lambdify(t,hm,'math');pf=S.lambdify(t,hp,'math')
rows=[]
for cutoff in [1000,10000,100000]:
    primes=list(S.primerange(2,cutoff+1))
    for tt in [.5,1.,2.]:
        minus=0.;plus=0.
        for p in primes:
            ratio=math.log(p/cutoff)
            coefficient=math.log(p)/math.sqrt(p*cutoff)
            if tt+ratio>=0:
                minus+=coefficient*ff(tt+ratio)
            plus+=coefficient*ff(tt-ratio)
        rows.append({'cutoff':cutoff,'t':tt,
                     'negative_first_prime_profile_error':abs(minus-mf(tt)),
                     'positive_first_prime_profile_error':abs(plus-pf(tt))})
assert max(max(row['negative_first_prime_profile_error'],row['positive_first_prime_profile_error'])
           for row in rows if row['cutoff']==100000)<.03
result={'schema':'marici.grothendieck.kernel-cutoff-escape.v1','passed':True,
        'checks':{'zero_endpoint_fixture':True,'profile_tail_and_initial_integral_signs':True,
                  'profile_ODEs_certify_nontriviality':True,'omitted_power_exponents':True,
                  'two_sided_weight_scaling':True,'first_prime_numerical_regression':True},
        'numerical_rows':rows,
        'scope':'Fixture is not an xi-kernel source. Numerical prime sums illustrate only the first-prime profiles. Actual kernel escape, uniform limits, and norm orders use the PNT, Bochner bounds, and unchanged weighted-dual operator in the companion proof.'}
root=Path(__file__).resolve().parents[3]
path=root/'research/grothendieck/results/kernel-cutoff-escape.json'
path.parent.mkdir(parents=True,exist_ok=True)
path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
