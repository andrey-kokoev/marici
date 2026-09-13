#!/usr/bin/env python3
"""Exact Green determinant and skew Pfaffian transitions under two-point insertion."""

import json, random
from fractions import Fraction
from pathlib import Path

def green_det(gaps):
 z=Fraction(1)
 for r in gaps:z*=1-r*r
 return z
def skew_pf(gaps):
 z=Fraction(1)
 for r in gaps[0::2]:z*=r
 return z
def main():
 rng=random.Random(20260920);rows=[]
 for parity in (0,1):
  for _ in range(50):
   left=[Fraction(rng.randrange(1,9),10) for _ in range(parity+2)]
   i=parity
   old=left[:]
   alpha=Fraction(rng.randrange(1,9),10);gamma=Fraction(rng.randrange(1,9),10);beta=Fraction(rng.randrange(1,9),10)
   rho=alpha*gamma*beta;old[i]=rho;new=old[:i]+[alpha,gamma,beta]+old[i+1:]
   pf_ratio=skew_pf(new)/skew_pf(old);expected=(alpha*beta/rho if i%2==0 else gamma)
   det_ratio=green_det(new)/green_det(old);expected_det=(1-alpha*alpha)*(1-gamma*gamma)*(1-beta*beta)/(1-rho*rho)
   assert pf_ratio==expected and det_ratio==expected_det
   rows.append({'replaced_gap_parity':'even' if i%2==0 else 'odd','pfaffian_ratio':str(pf_ratio),'green_determinant_ratio':str(det_ratio)})
 result={'schema':'marici.coherence.paired-refinement-line-transitions.v1','cases':len(rows),'all_exact':True,'pfaffian_transition_selected_gap':'alpha*beta/rho = gamma^-1','pfaffian_transition_unselected_gap':'gamma','green_transition':'(1-alpha^2)(1-gamma^2)(1-beta^2)/(1-rho^2)','conclusion':'paired refinement preserves even parity but acts differently on Green and Pfaffian lines'}
 Path(__file__).with_name('paired-refinement-line-transitions.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
