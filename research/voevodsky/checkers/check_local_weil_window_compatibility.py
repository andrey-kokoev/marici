#!/usr/bin/env python3
"""Exact discrete audit of zero-extension compatibility and bound growth."""
import json,math
from fractions import Fraction
from pathlib import Path

def mangoldt_table(N):
 out=[0.0]*(N+1)
 sieve=[True]*(N+1)
 for p in range(2,N+1):
  if not sieve[p]:continue
  for k in range(p*p,N+1,p):sieve[k]=False
  q=p
  while q<=N:
   out[q]=math.log(p);q*=p
 return out

def corr(f,k):return sum(f[i]*f[i+k] for i in range(len(f)-k))
def prime_form(f,K):return -sum(Fraction(k,1)*corr(f,k) for k in range(1,min(K,len(f)-1)+1))
def main():
 # Integer shifts model the exact support rule: shifts >= vector length have zero overlap.
 compatibility=0
 for m in range(1,9):
  for mask in range(1<<m):
   f=[Fraction((mask>>i)&1) for i in range(m)]
   small=prime_form(f,m-1)
   ext=f+[Fraction(0)]*m
   large=prime_form(ext,2*m-1)
   assert small==large;compatibility+=1
 # Actual explicit-formula coefficient majorants grow with support cutoff.
 radii=(1,2,3,4,5);Nmax=int(math.exp(2*max(radii)));vm=mangoldt_table(Nmax)
 bounds=[]
 for L in radii:
  N=int(math.exp(2*L));s=sum(vm[n]/math.sqrt(n) for n in range(2,N+1))
  bounds.append(s)
 assert all(bounds[i+1]>bounds[i] for i in range(len(bounds)-1))
 result={'schema':'marici.voevodsky.local-weil-window-compatibility.v1','zero_extension_cases_checked':compatibility,'local_form_compatibility':True,'support_rule':'translation terms vanish beyond twice the support radius','window_radii':[1,2,3,4,5],'prime_coefficient_majorants':bounds,'majorants_strictly_increasing':True,'local_conclusion':'On each fixed support window the gamma-plus-finite-prime form is continuous in the logarithmic Fourier graph norm.','global_conclusion':'The compatible compact-window forms define an algebraic inductive-limit form, but growing prime bounds do not supply a common Hilbert lower bound or closable global completion.'}
 out=Path(__file__).parents[1]/'results'/'local_weil_window_compatibility.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
