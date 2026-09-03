from fractions import Fraction as F
from math import factorial, comb
from pathlib import Path
import json


def exp_neg_upper(z, terms=160):
    s=sum((F(z)**k)/factorial(k) for k in range(terms+1))
    return 1/s


def bell_bounds(m, x=6):
    l1=F(m*x+4); l2=F(2*m*x+9); l3=F(4*m*x+50); l4=F(8*m*x+420)
    return [F(1),l1,l1*l1+l2,l1**3+3*l1*l2+l3,l1**4+6*l1*l1*l2+3*l2*l2+4*l1*l3+l4]

# A=sum_{n>=3} R_n and its first four derivative envelopes at x=6.
A=[F(0) for _ in range(5)]
for n in range(3,21):
    m=n*n-1
    R=2*n**4*exp_neg_upper(3*m)
    B=bell_bounds(m)
    for k in range(5): A[k]+=R*B[k]
# Terms n>=21 have ratio far below 1/2; twice n=21 is a rigorous coarse cap.
n=21; m=n*n-1; R=2*n**4*exp_neg_upper(3*m); B=bell_bounds(m)
for k in range(5): A[k]+=2*R*B[k]

# R2 derivative envelopes, using R2<1/200 and m=3 bounds.
RB=[F(1,200)*v for v in bell_bounds(3)]
S=[F(1),RB[1],RB[2]+2*RB[1]**2,
   RB[3]+6*RB[1]*RB[2]+6*RB[1]**3,
   RB[4]+8*RB[1]*RB[3]+6*RB[2]**2+36*RB[1]**2*RB[2]+24*RB[1]**4]
# r=A/(1+R2): Leibniz envelopes for A times reciprocal.
r=[sum(F(comb(k,j))*A[j]*S[k-j] for j in range(k+1)) for k in range(5)]
h2=r[2]+r[1]**2
h4=r[4]+4*r[1]*r[3]+3*r[2]**2+12*r[1]**2*r[2]+6*r[1]**4
transfer=h4+F(192)*h2
unsafe=F(2000)*transfer
result={
 "schema":"marici.theta-tail-transfer-bound.v1",
 "arithmetic":"exact Fraction; decimals are reporting projections",
 "h2_upper_decimal":float(h2),
 "h4_upper_decimal":float(h4),
 "transfer_upper_decimal":float(transfer),
 "margin":112,
 "passed":transfer<F(112),
 "deliberate_failure_scaled_tail_decimal":float(unsafe),
 "deliberate_failure_exhibited":unsafe>F(112)
}
result['passed']=result['passed'] and result['deliberate_failure_exhibited']
Path('research/grothendieck/results/theta_tail_transfer_bound.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
if not result['passed']: raise SystemExit(1)
