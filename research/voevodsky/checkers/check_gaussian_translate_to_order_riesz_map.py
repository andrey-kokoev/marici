#!/usr/bin/env python3
"""Audit the Fourier-restriction map from Gaussian translates to order Riesz rows."""
import json,math
from pathlib import Path

def dual_bound(sigma,a):
 # Half the integral on [0,infinity] of |d/dlambda exp(-sigma lambda^2-ia lambda)|^2.
 return math.sqrt(math.pi)*math.sqrt(sigma)/(2**2.5) + a*a*math.sqrt(math.pi)/(4*math.sqrt(2*sigma))
def numerical_integral(sigma,a,R=12.0,N=200000):
 h=R/N;s=0.0
 for k in range(N+1):
  x=k*h;y=(4*sigma*sigma*x*x+a*a)*math.exp(-2*sigma*x*x)
  s+=(0.5 if k in (0,N) else 1.0)*y
 return 0.5*h*s
def main():
 cases=[]
 for sigma in (0.25,0.5,1.0,2.0,4.0):
  for a in (-3.0,-1.0,0.0,1.0,3.0):
   exact=dual_bound(sigma,a);numeric=numerical_integral(sigma,a)
   assert abs(exact-numeric)<2e-8
   cases.append({'sigma':sigma,'a':a,'dual_norm_bound_squared':exact})
 result={'schema':'marici.voevodsky.gaussian-translate-to-order-riesz-map.v1','source_probe':'g_(sigma,a)(x)=exp(-(x-a)^2/(4 sigma))','arithmetic_evaluation_row':'constant times exp(-sigma lambda^2) exp(-i a lambda)','boundedness_method':'adjacent-gap Cauchy-Schwarz controlled by one-half integral of |F prime| squared','parameter_cases_checked':len(cases),'cases':cases,'riesz_map_exists':True,'map_target':'complexified order completion H_ord tensor C','form_descent_proved':False,'remaining_gate':'Show every finite linear relation among Riesz images lies in the radical of the polarized source kernel, then apply the kernel closability criterion.'}
 out=Path(__file__).parents[1]/'results'/'gaussian_translate_to_order_riesz_map.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
