"""Exact tail-identity and trace checks; finite prime-discrepancy illustrations."""
from pathlib import Path
import json
import math
import sympy as S

xi=S.symbols('xi',real=True,nonzero=True)
a=S.symbols('a',positive=True)
# Signed fixture 3 delta_a - exp(-t/2)dt; its mass discrepancy is one.
left=3*S.exp(S.I*xi*a)-1/(S.Rational(1,2)-S.I*xi)
tail_integral=3*(S.exp(S.I*xi*a)-1)/(S.I*xi)-2/(S.Rational(1,2)-S.I*xi)
assert S.simplify(left-(1+S.I*xi*tail_integral))==0
assert 3-2==1
x,r=S.symbols('x r',positive=True)
assert S.simplify(S.diff(x**(1-2*r)/(1-2*r),x)-x**(-2*r))==0
assert S.integrate(x**(-S.Rational(1,2)),(x,0,1))==2
assert S.integrate(1/x,(x,0,1))==S.oo
ell=S.symbols('ell',positive=True)
assert S.integrate(S.exp(-a/2),(a,ell/2,S.oo))==2*S.exp(-ell/4)
C,K=S.symbols('C K',positive=True)
# Endpoints of the interpolation expression.
assert (C**(1-r)*K**r).subs(r,0)==C
assert (C**(1-r)*K**r).subs(r,1)==K

# Integrate the absolute discrepancy exactly on each real step interval,
# using elementary primitives in floating point (not certified enclosures).
def step_integral(w,lo,hi):
    def primitive(z):
        return w*math.log(z)-4*math.sqrt(z)
    root=(w/2)**2
    cuts=[lo]+([root] if lo<root<hi else [])+[hi]
    return sum(abs(primitive(v)-primitive(u)) for u,v in zip(cuts,cuts[1:]))
rows=[]
for cutoff in [1000,10000,100000]:
    primes=list(S.primerange(2,cutoff+1))
    integral=4*math.sqrt(2) # x in (0,2), where W=0
    w=0.
    for index,p in enumerate(primes):
        w+=math.log(p)/math.sqrt(p)
        stop=primes[index+1] if index+1<len(primes) else cutoff
        if stop>p:
            integral+=step_integral(w,p,stop)
    discrepancy=abs(w/math.sqrt(cutoff)-2)+integral/math.sqrt(cutoff)
    assert math.isfinite(discrepancy) and discrepancy>0
    rows.append({'cutoff':cutoff,'K_P_approximate':discrepancy,
                 'first_prime_L2_operator_lower_bound':2*w/math.sqrt(cutoff)})
result={'schema':'marici.grothendieck.fractional-uniform-escape.v1','passed':True,
        'checks':{'tail_identity_includes_mass':True,'interpolation_endpoints':True,
                  'PNT_tail_split':True,'zero_extension_fractional_threshold':True},
        'numerical_rows':rows,
        'scope':'Finite discrepancy numbers are illustrative, not certified bounds. Uniform convergence uses Sobolev interpolation and PNT; zero-regularity failure uses simultaneous recurrence.'}
root=Path(__file__).resolve().parents[3]
p=root/'research/grothendieck/results/fractional-uniform-escape.json'
p.parent.mkdir(parents=True,exist_ok=True)
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
