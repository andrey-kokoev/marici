#!/usr/bin/env python3
"""Elementary absolute bound for the omitted digamma-integral tail."""
import json,math
from pathlib import Path

def tail_bound(sigma,d):
 t=2*sigma;U=max(12.0,math.sqrt(35/t))
 # From the convergent digamma series at a=1/4: |Re psi| <= C+2u, deliberately coarse.
 C=21.0
 # |1-cos(du)|<=2; erfc tail <= exp(-tU^2)/(sqrt(pi*t)*U), simplified further below.
 e=math.exp(-t*U*U)
 integral_const=C*e/(2*t*U) # integral_U inf exp(-t u^2) du <= e/(2tU)
 integral_linear=e/t         # integral 2u exp(-t u^2) du = e/t
 return (integral_const+integral_linear)/math.pi,U

def main():
 rows=[]
 for sigma in (.005,.01,.02,.05,.1):
  for d in (.1,.25,.5,1,2,3):
   b,U=tail_bound(sigma,d);rows.append({'sigma':sigma,'d':d,'cutoff':U,'absolute_gamma_tail_bound':b})
 worst=max(rows,key=lambda r:r['absolute_gamma_tail_bound'])
 result={'schema':'marici.voevodsky.two-translate-gamma-tail-bound.v1','digamma_majorant':'|Re psi(1/4+iu/2)| <= 21+2u','oscillation_majorant':'|1-cos(du)| <= 2','gaussian_cutoff_rule':'2 sigma U^2 >= 35','rows':rows,'worst_case':worst,'all_bounds_below_1e-12':all(r['absolute_gamma_tail_bound']<1e-12 for r in rows),'certifies_quadrature':False,'conclusion':'The omitted infinite gamma tail is below 1e-12 throughout the scout; only finite-interval quadrature and digamma evaluation remain uncertified.'}
 out=Path(__file__).parents[1]/'results'/'two_translate_gamma_tail_bound.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'worst_case':worst,'all_bounds_below_1e-12':result['all_bounds_below_1e-12']},indent=2))
if __name__=='__main__':main()
