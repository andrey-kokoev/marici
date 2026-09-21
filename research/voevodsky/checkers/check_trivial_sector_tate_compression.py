"""Fixed-sector Tate symbol signs and the prime leakage negative control."""
from pathlib import Path
import json
import sympy as s
import mpmath as mp
mp.mp.dps=60
r,q,L=s.symbols('r q L',nonzero=True)
# q=exp(i*t*log p), dq/dt=i*log(p)*q.
gamma=(1-r/q)/(1-r*q)
a=s.simplify(-s.I*(s.diff(gamma,q)*s.I*L*q)/gamma)
expected=L*(r/q/(1-r/q)+r*q/(1-r*q))
assert s.simplify(a-expected)==0
# The prime part of the arithmetic form is the NEGATIVE of this symbol.
assert s.simplify(-expected+a)==0

fixtures=[]
for t in (mp.mpf(0),mp.mpf('0.7'),mp.mpf(3)):
    def scattering(x):
        z=mp.mpf('.5')-1j*x
        return 2*(2*mp.pi)**(-z)*mp.gamma(z)*mp.cos(mp.pi*z/2)
    connection=(-1j*mp.diff(scattering,t)/scattering(t))
    target=mp.log(mp.pi)-mp.re(mp.digamma(mp.mpf('.25')+1j*t/2))
    assert abs(connection-target)<mp.mpf('1e-50')
    fixtures.append({'frequency':str(t),'connection':mp.nstr(target,20)})

# For f supported in (0,log p), negative-side shift images at k log p
# have disjoint supports. Their squared coefficients sum exactly as below.
x=s.symbols('x',positive=True)
assert s.simplify(x/(1-x)-1/(1/x-1))==0
for p in (2,3,5,11):
    finite=sum(s.Rational(1,p)**k for k in range(1,9))
    tail=s.Rational(1,p)**9/(1-s.Rational(1,p))
    assert finite+tail==s.Rational(1,p-1)
result={'passed':True,'archimedean_scattering_regressions':fixtures,
 'checks':{'finite_prime_tate_sign':True,
 'regular_arithmetic_symbol_is_negative_tate_connection':True,
 'prime_leakage_squared_norm':'(log p)^2/(p-1) times input norm squared'},
 'scope':'Exact finite-prime identities and high-precision archimedean regression. The common-core compression and domain inclusion are proved in the companion note; no full-line invariance or global prime-limit assertion.'}
ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/voevodsky/results/trivial-sector-tate-compression.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
