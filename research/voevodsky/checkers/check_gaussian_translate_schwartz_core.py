#!/usr/bin/env python3
"""Exact moment audit for finite-difference generation of Gaussian derivatives."""
import json,math
from pathlib import Path

def binom(n,k):return math.comb(n,k)
def main():
 audits=[]
 # Forward n-th differences annihilate monomials below n and select n! at n.
 for n in range(9):
  weights=[(-1)**(n-k)*binom(n,k) for k in range(n+1)]
  moments=[]
  for m in range(n+2):moments.append(sum(weights[k]*k**m for k in range(n+1)))
  assert all(moments[m]==0 for m in range(n))
  assert moments[n]==math.factorial(n)
  audits.append({'derivative_order':n,'translation_weights':weights,'moments':moments})
 result={'schema':'marici.voevodsky.gaussian-translate-schwartz-core.v1','orders_checked':'0..8','finite_difference_moment_identities':audits,'analytic_steps':['translation finite differences converge to Gaussian derivatives in every Schwartz seminorm','Gaussian derivatives are Hermite polynomial times Gaussian','finite Hermite expansions are dense in Schwartz space'],'conclusion':'The linear span of translates of one Gaussian is Schwartz-dense.','positivity_consequence':'For a continuous Hermitian Weil form, PSD of every finite Gaussian-translate Gram matrix is equivalent to positivity on Schwartz space.','rh_boundary':'Equivalence with RH additionally invokes the standard Weil positivity criterion and exact source-form normalization.'}
 out=Path(__file__).parents[1]/'results'/'gaussian_translate_schwartz_core.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
