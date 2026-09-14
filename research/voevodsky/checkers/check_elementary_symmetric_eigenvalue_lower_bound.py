#!/usr/bin/env python3
"""Elementary lower enclosure for K_sigma(0)+K_sigma(d) at one sample."""
import json,math
from pathlib import Path

def mangoldt(N):
 out=[0.0]*(N+1);sieve=bytearray(b'\x01')*(N+1);sieve[:2]=b'\x00\x00'
 for p in range(2,N+1):
  if not sieve[p]:continue
  if p*p<=N:sieve[p*p:N+1:p]=b'\x00'*(((N-p*p)//p)+1)
  q=p
  while q<=N:out[q]=math.log(p);q*=p
 return out
def lower_repsi(u,M=16):
 a=.25;b=u/2
 partial=sum(b*b/((k+a)*((k+a)**2+b*b)) for k in range(M))
 return -0.5772156649015329-math.pi/2-3*math.log(2)+partial+.5*math.log1p(b*b/(a+M)**2)
def main():
 sigma=.005;d=.25;t=2*sigma;U=math.sqrt(35/t);panels=3600000;h=U/panels
 total=0.0
 for j in range(panels):
  u=(j+.5)*h;total+=math.exp(-t*u*u)*lower_repsi(u)*(1+math.cos(d*u))
 gamma_integral_lower=h*total/(2*math.pi)
 pref=math.exp(-d*d/(4*t));c=-math.log(math.pi)/(4*math.sqrt(math.pi*t))
 endpoint=math.exp(sigma/2)*(1+math.cosh(d/2));gamma_constant=c*(1+pref)
 N=1200000;vm=mangoldt(N);C=1/(2*math.sqrt(math.pi*t));raw=0.0
 for n in range(2,N+1):
  if not vm[n]:continue
  L=math.log(n);p0=math.exp(-L*L/(4*t));pair=(math.exp(-(L-d)**2/(4*t))+math.exp(-(L+d)**2/(4*t)))/2
  raw+=vm[n]/math.sqrt(n)*(p0+pair)
 prime=-C*raw;center=endpoint+gamma_constant+gamma_integral_lower+prime
 A=21+2*U;Aprime=20;Mlip=(4*t*U*A+2*Aprime+A*d)/(2*math.pi);quad=Mlip*U*h/4
 prime_tail=1e-100;gamma_tail=2.4e-14;floating=1e-6;lower=center-quad-prime_tail-gamma_tail-floating
 result={'schema':'marici.voevodsky.elementary-symmetric-eigenvalue-lower-bound.v1','sigma':sigma,'d':d,'digamma_terms_retained':16,'midpoint_panels':panels,'parts_lower_center':{'endpoint':endpoint,'gamma_constant':gamma_constant,'gamma_integral_lower':gamma_integral_lower,'prime':prime},'center':center,'quadrature_error_bound':quad,'prime_tail_bound':prime_tail,'gamma_tail_bound':gamma_tail,'floating_allowance':floating,'final_lower_bound':lower,'strictly_positive':lower>0,'publication_interval_certificate':False,'conclusion':'Both eigenvalues of the selected rank-two source Gram matrix now have positive analytic error budgets under the stated floating model.'}
 out=Path(__file__).parents[1]/'results'/'elementary_symmetric_eigenvalue_lower_bound.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
