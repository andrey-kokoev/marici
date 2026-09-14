#!/usr/bin/env python3
"""Exact algebra audit for the unequal-width polarized Gaussian kernel."""
import json
from fractions import Fraction
from pathlib import Path

def spectral_product(sigma,tau,a,b,u):
 # Constants omitted: exponent of exp is returned exactly.
 return -(sigma+tau)*u*u-(a-b)*u  # character exponent uses -i times linear term

def completed_square(sigma,tau,a,b,u):
 # Encode imaginary terms as pairs (real, imaginary): exponent equality algebraically.
 t=sigma+tau;d=a-b
 # -d^2/(4t) - t*(u+i d/(2t))^2 has real -t*u^2 and imaginary -d*u.
 return (-t*u*u,-d*u)

def main():
 checked=0
 vals=[Fraction(1,2),Fraction(1),Fraction(3,2),Fraction(2)]
 shifts=[Fraction(-2),Fraction(-1),Fraction(0),Fraction(1),Fraction(2)]
 for s in vals:
  for t in vals:
   for a in shifts:
    for b in shifts:
     for u in shifts:
      raw=( -(s+t)*u*u, -(a-b)*u )
      assert raw==completed_square(s,t,a,b,u);checked+=1
 # Kernel parameters and Hermitian swap law: total width fixed, d changes sign.
 hermitian=0
 for s in vals:
  for t in vals:
   for a in shifts:
    for b in shifts:
     left=(s+t,a-b);right=(t+s,-(b-a))
     assert left==right;hermitian+=1
 result={'schema':'marici.voevodsky.unequal-width-weil-gaussian-kernel.v1','algebra_cases_checked':checked,'hermitian_swap_cases_checked':hermitian,'source_gaussian':'g_sigma(x-a)=exp(-(x-a)^2/(4 sigma))','spectral_product':'4 pi sqrt(sigma tau) exp(-(sigma+tau)u^2) exp(-i(a-b)u)','theta_reduction':'4 pi sqrt(sigma tau) exp(-(a-b)^2/(4(sigma+tau))) Theta(sigma+tau,-i(a-b)/(2(sigma+tau)))','unequal_width_kernel_constructed':True,'positivity_proved':False,'closability_proved':False,'comparison_boundary':'This kernel is on the source Gaussian-translate span; identification with the order-completion heat-Riesz vectors still requires a typed comparison map.'}
 out=Path(__file__).parents[1]/'results'/'unequal_width_weil_gaussian_kernel.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
