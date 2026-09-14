#!/usr/bin/env python3
"""Explicit elementary upper bound for the omitted prime-power deficit tail."""
import json,math
from pathlib import Path

def component_tail(N,sigma,d):
 # Sum_{n>N} log(n)/sqrt(n) exp(-(log(n)-d)^2/(8 sigma)).
 # Bound by f(N)+integral_N^infty f(x) dx once f is decreasing.
 x0=math.log(N);mu=d+2*sigma;A=8*sigma
 assert x0>mu and x0*(x0-d)>4*sigma # derivative negativity in n-coordinate
 fN=x0/math.sqrt(N)*math.exp(-(x0-d)**2/A)
 z=(x0-mu)/math.sqrt(A)
 integ=math.exp(d/2+sigma/2)*(mu*math.sqrt(math.pi*A)/2*math.erfc(z)+A/2*math.exp(-z*z))
 return fN+integ
def deficit_tail(N,sigma,d):
 # |pair-p0| <= pair+p0, including the explicit-formula coefficient.
 raw=.5*component_tail(N,sigma,d)+.5*component_tail(N,sigma,-d)+component_tail(N,sigma,0)
 return raw/(2*math.sqrt(math.pi*2*sigma))
def main():
 N=1200000;rows=[]
 for sigma in (0.005,0.01,0.02,0.05,0.1):
  for d in (0.1,0.25,0.5,1.0,2.0,3.0):rows.append({'sigma':sigma,'d':d,'absolute_prime_tail_bound':deficit_tail(N,sigma,d)})
 worst=max(rows,key=lambda r:r['absolute_prime_tail_bound'])
 result={'schema':'marici.voevodsky.two-translate-prime-tail-bound.v1','cutoff':N,'inequality':'Lambda(n)<=log(n)','method':'decreasing summand bounded by first omitted term plus exact Gaussian integral','rows':rows,'worst_case':worst,'narrow_width_sigma_at_most_0.05_worst':max((r for r in rows if r['sigma']<=.05),key=lambda r:r['absolute_prime_tail_bound']),'certifies_full_deficit':False,'remaining_errors':['digamma asymptotic remainder','quadrature error','floating roundoff in cancellation'],'conclusion':'Prime truncation is negligible in the narrow-width scout region relative to its reported positive margins.'}
 out=Path(__file__).parents[1]/'results'/'two_translate_prime_tail_bound.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'worst_case':worst,'narrow_width_worst':result['narrow_width_sigma_at_most_0.05_worst']},indent=2))
if __name__=='__main__':main()
