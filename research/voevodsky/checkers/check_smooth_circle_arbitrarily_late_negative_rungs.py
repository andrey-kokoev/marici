#!/usr/bin/env python3
"""Exact smooth-circle realization of arbitrarily late minimal Toeplitz failures."""
import json
from fractions import Fraction
from pathlib import Path

def main():
 rows=[]
 for n in range(3,11):
  r=-(Fraction(1,n-2)+Fraction(1,n-1))/2
  # Smooth density w(theta)=1+2r sum_{m=1}^{n-1} cos(m theta) has moments k0=1,k_m=r.
  proper=1+(n-2)*r;full=1+(n-1)*r;allones_q=n*full
  assert proper>0 and full<0
  rows.append({'n':n,'r':str(r),'density':f'1 + 2({r}) sum_(m=1)^{n-1} cos(m theta)','moments_through_n_minus_1':'k0=1, k_m=r','largest_proper_minimum_eigenvalue':str(proper),'full_minimum_eigenvalue':str(full),'all_ones_quadratic_value':str(allones_q)})
 result={'schema':'marici.voevodsky.smooth-circle-arbitrarily-late-negative-rungs.v1','rows':rows,'all_densities':'real, even, C-infinity trigonometric polynomials','all_moment_packets':'Hermitian Toeplitz, reversal invariant, and compatible under principal restriction','theorem':'For every n>=3, a smooth signed circle distribution can have every Toeplitz rank below n positive definite and fail first at rank n.','consequence':'No argument using only smoothness, stationarity, reversal, circle incidence, or finite-rung coherence can force RH positivity. The coupled arithmetic source values must enter a quantitative inequality.'}
 out=Path(__file__).parents[1]/'results'/'smooth_circle_arbitrarily_late_negative_rungs.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'ranks':[3,10],'smooth_toeplitz_hostiles':len(rows)},indent=2))
if __name__=='__main__':main()
