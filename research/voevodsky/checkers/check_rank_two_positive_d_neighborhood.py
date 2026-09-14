#!/usr/bin/env python3
"""Extend the enclosed rank-two sample to an open separation interval."""
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
def main():
 sigma=.005;t=2*sigma;d0=.25;radius=2e-5;dmax=d0+radius
 anti=json.loads((Path(__file__).parents[1]/'results'/'elementary_digamma_lower_bound_deficit.json').read_text())['final_lower_bound']
 sym=json.loads((Path(__file__).parents[1]/'results'/'elementary_symmetric_eigenvalue_lower_bound.json').read_text())['final_lower_bound']
 endpoint=math.exp(sigma/2)*.5*math.sinh(dmax/2)
 c=abs(-math.log(math.pi)/(4*math.sqrt(math.pi*t)));pref=math.exp(-(d0-radius)**2/(4*t));gamma_constant=c*dmax/(2*t)*pref
 # |Re psi|<=21+2u; integrate u(21+2u)e^{-tu^2} on the half-line.
 gamma_integral=(21/(2*t)+math.sqrt(math.pi)/(2*t**1.5))/(2*math.pi)
 N=1200000;vm=mangoldt(N);C=1/(2*math.sqrt(math.pi*t));prime=0.0
 for n in range(2,N+1):
  if not vm[n]:continue
  L=math.log(n)
  dmin=d0-radius
  deriv=(abs(L-dmax)*math.exp(-(L-dmax)**2/(4*t))+abs(L+dmin)*math.exp(-(L+dmin)**2/(4*t)))/(4*t)
  prime+=vm[n]/math.sqrt(n)*deriv
 prime*=C
 lipschitz=endpoint+gamma_constant+gamma_integral+prime
 loss=lipschitz*radius
 anti_box=anti-loss;sym_box=sym-loss
 assert anti_box>0 and sym_box>0
 result={'schema':'marici.voevodsky.rank-two-positive-d-neighborhood.v1','sigma':sigma,'center_d':d0,'radius':radius,'d_interval':[d0-radius,d0+radius],'derivative_bounds':{'endpoint':endpoint,'gamma_constant':gamma_constant,'gamma_integral':gamma_integral,'finite_prime':prime},'total_lipschitz_bound':lipschitz,'maximum_transport_loss':loss,'center_lower_bounds':{'antisymmetric':anti,'symmetric':sym},'interval_lower_bounds':{'antisymmetric':anti_box,'symmetric':sym_box},'positive_definite_throughout_interval':True,'claim_boundary':'Fixed sigma only; inherits the elementary-function rounding assumptions of the center enclosures.'}
 out=Path(__file__).parents[1]/'results'/'rank_two_positive_d_neighborhood.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
