#!/usr/bin/env python3
"""Attach conservative order-1..3 tails to rank-two remainder point determinants."""
import json,math,re
from pathlib import Path
R=Path(__file__).parents[1]/'results';src=json.loads((R/'remainder_rank_two_finite_core.json').read_text())
U=100.;N=200000.;V=math.log(N)
def center(s):return float(re.match(r'\[([^ ]+)',s).group(1))
def gamma_tail(t,k):
 # |Re psi|<=u^2 for u>=100. Bound I_m recursively from I0.
 e=math.exp(-t*U*U);I=e/(2*t*U)
 for m in range(2,2*k+3,2):I=U**(m-1)*e/(2*t)+(m-1)*I/(2*t)
 return I/(2*math.pi)
def prime_tail(t,k):
 # For k<=3, |L_k^-1/2(y)|<=10(1+y)^k.
 y=V*V/(4*t);single=10*V/math.sqrt(N)*math.exp(-y)*(1+y)**k
 # after x=e^v, logarithmic growth <=(2k+1)/V
 g=10*V*(1+y)**k;base=math.exp(V/2-y);rate=(V-t)/(2*t)-(2*k+1)/V
 integ=g*base/rate
 return math.factorial(k)*(single+integ)/(2*math.sqrt(math.pi)*t**(k+.5))
rows=[]
for x in src['rows']:
 t=float(x['t']);c=[center(x[f'c{i}']) for i in range(3)];e=[gamma_tail(t,k+1)+prime_tail(t,k+1) for k in range(3)]
 err=abs(c[2])*e[0]+abs(c[0])*e[2]+2*abs(c[1])*e[1]+e[0]*e[2]+e[1]*e[1]
 d=x['lower'];lb=d-err;rows.append({'t':t,'finite_core_det_lower':d,'moment_tail_bounds':e,'determinant_error_bound':err,'complete_det_lower':lb,'certified_positive':lb>0})
out={'schema':'marici.voevodsky.remainder-rank-two-point-tails.v1','rows':rows,
 'lemmas':['|Re psi(1/4+iu/2)|<=u^2 for u>=100','Lambda(n)<=log n','|L_k^-1/2(y)|<=10(1+y)^k for k=1,2,3','decreasing log-Gaussian sum <= first term plus transformed integral'],
 'all_complete_point_determinants_positive':all(x['certified_positive'] for x in rows),'passed':all(x['certified_positive'] for x in rows),'rh_proved':False,
 'scope':'Nine complete point determinants only; no interval or all-rank theorem.'}
p=R/'remainder_rank_two_point_tails.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
