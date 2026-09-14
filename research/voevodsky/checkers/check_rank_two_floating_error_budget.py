#!/usr/bin/env python3
"""Forward-error budget for finite gamma and prime accumulations at one sample."""
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
 sigma=.005;d=.25;t=2*sigma;N=1200000;vm=mangoldt(N);terms=[]
 for n in range(2,N+1):
  if not vm[n]:continue
  L=math.log(n);p0=math.exp(-L*L/(4*t));pair=(math.exp(-(L-d)**2/(4*t))+math.exp(-(L+d)**2/(4*t)))/2
  terms.append(vm[n]/math.sqrt(n)*(pair-p0))
 C=1/(2*math.sqrt(math.pi*t));absolute_prime_accumulation=C*sum(abs(x) for x in terms)
 eps=2**-53;ops=50*N;prime_round=(ops*eps)/(1-ops*eps)*absolute_prime_accumulation
 gamma=json.loads((Path(__file__).parents[1]/'results'/'elementary_digamma_lower_bound_deficit.json').read_text())
 gamma_round=gamma['standard_rounding_bound'];reserve=1e-6
 assert 100*(prime_round+gamma_round)<reserve
 result={'schema':'marici.voevodsky.rank-two-floating-error-budget.v1','sigma':sigma,'d':d,'prime_terms_nonzero':len(terms),'absolute_prime_accumulation':absolute_prime_accumulation,'prime_standard_rounding_bound':prime_round,'gamma_standard_rounding_bound':gamma_round,'combined_bound':prime_round+gamma_round,'declared_reserve':reserve,'reserve_factor':reserve/(prime_round+gamma_round),'reserve_exceeds_100x_standard_bound':True,'libm_caveat':'The bound assumes each elementary transcendental evaluation is within a small fixed number of ulps; Python does not contractually guarantee directed enclosures.','conclusion':'The 1e-6 finite-evaluation reserve is quantitatively conservative under the stated IEEE/libm assumption.'}
 out=Path(__file__).parents[1]/'results'/'rank_two_floating_error_budget.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
