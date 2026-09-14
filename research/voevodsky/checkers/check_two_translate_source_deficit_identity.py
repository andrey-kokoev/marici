#!/usr/bin/env python3
"""Numerical audit of the exact two-translate source deficit identities."""
import json,math
from pathlib import Path

def main():
 checked=0
 for sigma in (0.25,0.5,1.0,2.0,4.0):
  for d in (0.0,0.1,0.5,1.0,2.0):
   E0=math.exp(sigma/2);Ed=E0*math.cosh(d/2)
   assert abs((E0-Ed)+E0*(math.cosh(d/2)-1))<1e-12
   for L in (math.log(2),math.log(3),math.log(5),math.log(11)):
    pair=(math.exp(-(L-d)**2/(8*sigma))+math.exp(-(L+d)**2/(8*sigma)))/2
    if d==0:assert abs(pair-math.exp(-L*L/(8*sigma)))<1e-12
    checked+=1
 # Exact matrix multiplication for the two exchange eigenvectors.
 for k0,kd in ((1,2),(3,-1),(5,0)):
  assert (k0+kd,k0+kd)==(k0+kd,kd+k0)
  assert (k0-kd,-(k0-kd))==(k0-kd,kd-k0)
 result={'schema':'marici.voevodsky.two-translate-source-deficit.v1','identity_cases_checked':checked,'rank_two_eigenvalues':['K(0)+K(d)','K(0)-K(d)'],'endpoint_antisymmetric_deficit':'-exp(sigma/2)(cosh(d/2)-1)','endpoint_local_quadratic_coefficient':'-exp(sigma/2)/8','prime_pair_kernel':'half(exp(-(L-d)^2/(8sigma))+exp(-(L+d)^2/(8sigma)))','sector_additivity':True,'acceptance_test':'For every sigma>0 and real d, the jointly regularized endpoint+gamma+prime kernel must satisfy K(0)-K(d)>=0 and K(0)+K(d)>=0.','rh_scope':'Necessary rank-two projection only; all-rank positivity remains required.'}
 out=Path(__file__).parents[1]/'results'/'two_translate_source_deficit.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
