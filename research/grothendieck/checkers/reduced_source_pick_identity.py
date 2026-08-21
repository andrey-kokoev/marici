"""Exact endpoint reduction and conditional Pick-sign regression."""
import json
from fractions import Fraction as Q
from pathlib import Path

# Rational complex arithmetic as (real,imag).
def add(z,w):return z[0]+w[0],z[1]+w[1]
def mul(z,w):return z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0]
def inv(z):
    d=z[0]*z[0]+z[1]*z[1];return z[0]/d,-z[1]/d
def div(z,w):return mul(z,inv(w))

# Verify 4s(s-1)/(2s-1) * (1/s+1/(s-1)) = 4 off poles.
s=(Q(7,5),Q(3,7));one=(Q(1),Q(0))
sm1=add(s,(-1,0));two_s_minus_one=add(mul((2,0),s),(-1,0))
prefactor=div(mul((4,0),mul(s,sm1)),two_s_minus_one)
endpoint=add(inv(s),inv(sm1))
assert mul(prefactor,endpoint)==(Q(4),Q(0))

# Positive spectral atoms make F(t)=4M-sum c/(t+lambda) a Pick function.
atoms=[(Q(2,3),1),(Q(7,5),2),(Q(11,2),1)];t=(Q(2,5),Q(3,7))
F=(Q(0),Q(0))
for lam,mass in atoms:
    coefficient=Q(mass)*(1+4*lam)
    F=add(F,mul((-coefficient,0),inv(add(t,(lam,0)))))
assert F[1]>0
# A negative Gram weight reverses its rank-one Pick contribution.
bad_lambda=Q(-1,2);bad_coefficient=1+4*bad_lambda
bad=mul((-bad_coefficient,0),inv(add(t,(bad_lambda,0))))
assert bad[1]<0
result={'endpoint_poles_reduce_exactly_to_constant_four':True,'positive_spectral_pick_imaginary_part':str(F[1]),'negative_weight_pick_falsifier_imaginary_part':str(bad[1]),'coupled_pick_target':'Im F(t) >= 0 for Im(t) > 0','zero_locations_used':False}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'reduced-source-pick-identity.json';output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
