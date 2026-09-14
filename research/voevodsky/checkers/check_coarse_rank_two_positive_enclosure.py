#!/usr/bin/env python3
"""Coarse analytic error budget for one positive two-translate source sample."""
import cmath,json,math
from pathlib import Path

B2=(1/6,-1/30,1/42,-1/30,5/66,-691/2730,7/6,-3617/510)
def digamma(z):
 s=0j
 while abs(z)<12:s-=1/z;z+=1
 out=s+cmath.log(z)-1/(2*z);power=z*z
 for k,b in enumerate(B2,1):out-=b/(2*k*power);power*=z*z
 return out

def midpoint_gamma(sigma,d,U,panels):
 t=2*sigma;h=U/panels;s=0.0
 for k in range(panels):
  u=(k+.5)*h
  s+=math.exp(-t*u*u)*digamma(.25+.5j*u).real*(1-math.cos(d*u))
 return h*s/(2*math.pi)

def main():
 sigma=.005;d=.25;t=2*sigma;U=math.sqrt(35/t);panels=600000;h=U/panels
 # On Re(z)=1/4: |Re psi(z)| <= 21+2U and |d/du Re psi(z)| <= 10,
 # from the convergent digamma/trigamma series.
 A=21+2*U;Aprime=10
 # Derivative bound for exp(-tu^2) A(u)(1-cos(du))/(2pi), using |1-cos|<=2.
 M=(4*t*U*A+2*Aprime+A*d)/(2*math.pi)
 midpoint_error=M*U*h/4
 scout=json.loads((Path(__file__).parents[1]/'results'/'two_translate_weil_deficit_scout.json').read_text())
 row=next(r for r in scout['rows'] if r['sigma']==sigma and r['d']==d)
 scout_value=row['K0_minus_Kd']
 gamma_midpoint=midpoint_gamma(sigma,d,U,panels)
 value=sum(v for k,v in row['parts'].items() if k!='gamma_integral')+gamma_midpoint
 prime_tail=json.loads((Path(__file__).parents[1]/'results'/'two_translate_prime_tail_bound.json').read_text())
 pt_raw=next(r['absolute_prime_tail_bound'] for r in prime_tail['rows'] if r['sigma']==sigma and r['d']==d)
 pt=max(pt_raw,1e-100) # avoid reporting floating underflow as an exact zero
 gamma_tail=json.loads((Path(__file__).parents[1]/'results'/'two_translate_gamma_tail_bound.json').read_text())
 gt=next(r['absolute_gamma_tail_bound'] for r in gamma_tail['rows'] if r['sigma']==sigma and r['d']==d)
 # Deliberately generous allowance for finite special-function and floating evaluation.
 evaluation_allowance=1e-6
 lower=value-midpoint_error-pt-gt-evaluation_allowance
 assert lower>0
 result={'schema':'marici.voevodsky.coarse-rank-two-positive-enclosure.v1','sigma':sigma,'d':d,'scouted_simpson_value':scout_value,'midpoint_gamma_value':gamma_midpoint,'midpoint_centered_deficit':value,'digamma_absolute_bound':A,'digamma_derivative_bound':Aprime,'integrand_lipschitz_bound':M,'midpoint_panels_required':panels,'midpoint_error_bound':midpoint_error,'prime_tail_bound':pt,'gamma_tail_bound':gt,'finite_evaluation_allowance':evaluation_allowance,'coarse_lower_bound':lower,'strictly_positive':True,'certification_level':'analytic error budget conditional on correctly rounded elementary/special-function finite evaluations','publication_interval_certificate':False,'conclusion':'The source-side antisymmetric rank-two inequality is robustly positive at this one parameter point.'}
 out=Path(__file__).parents[1]/'results'/'coarse_rank_two_positive_enclosure.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
