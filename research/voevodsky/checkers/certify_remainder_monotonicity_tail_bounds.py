#!/usr/bin/env python3
"""Attach conservative analytic tails to the Arb finite-core monotonicity values."""
import json,math
from pathlib import Path
R=Path(__file__).parents[1]/"results";core=json.loads((R/"remainder_monotonicity_finite_core.json").read_text())
U=40.0;N=200000.0;V=math.log(N)
def gaussian_moment_tail_even4(t,U):
 # I_m=integral_U^inf u^m exp(-t u^2)du;
 # I_m=U^(m-1)e^-tU2/(2t)+(m-1)I_(m-2)/(2t), with I0 bounded by e^-tU2/(2tU).
 e=math.exp(-t*U*U);I0=e/(2*t*U);I2=U*e/(2*t)+I0/(2*t);I4=U**3*e/(2*t)+3*I2/(2*t);return I4
def gamma_tail(t):
 # For u>=40, the standard digamma series/remainder estimate gives
 # |Re psi(1/4+iu/2)| <= u^2. This intentionally crude bound is ample.
 return gaussian_moment_tail_even4(t,U)/(2*math.pi)
def prime_tail(t):
 # Lambda(n)<=log n and |L_1^-1/2(y)|=|1/2-y|<=y+1/2.
 # Integral test after x=e^v. For g(v)=v(v^2/(4t)+1/2),
 # g(V+s)<=g(V)e^(3s/V), while the Gaussian exponent drops at least
 # exp(-(V-t)s/(2t)).
 y=V*V/(4*t);single=V/math.sqrt(N)*math.exp(-y)*(y+.5)
 g=V*(y+.5);base=math.exp(V/2-y);rate=(V-t)/(2*t)-3/V
 integral=g*base/rate
 return (single+integral)/(2*math.sqrt(math.pi)*t**1.5)
rows=[]
for x in core['rows']:
 t=float(x['t']);gt=gamma_tail(t);pt=prime_tail(t);total=gt+pt;lb=x['lower_bound']-total
 rows.append({'t':t,'finite_core_lower':x['lower_bound'],'digamma_tail_absolute_bound':gt,'prime_tail_absolute_bound':pt,'full_lower_bound':lb,'certified_positive':lb>0})
out={'schema':'marici.voevodsky.remainder-monotonicity-tail-bounds.v1','tail_lemmas':[
 'For u>=40, |Re psi(1/4+iu/2)|<=u^2, from the standard digamma series with its integral remainder.',
 'Lambda(n)<=log(n).',
 'For y>=0, |L_1^(-1/2)(y)|=|1/2-y|<=y+1/2.',
 'Beyond N=200000 on the listed t range, the resulting log-Gaussian majorant is decreasing; the sum is bounded by its first term plus its integral.'
 ],'rows':rows,'all_listed_complete_values_certified_positive':all(x['certified_positive'] for x in rows),
 'coverage':'The listed heat times only; this is not a compact-interval or all-t theorem.','passed':all(x['certified_positive'] for x in rows),'rh_proved':False}
p=R/'remainder_monotonicity_tail_bounds.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
