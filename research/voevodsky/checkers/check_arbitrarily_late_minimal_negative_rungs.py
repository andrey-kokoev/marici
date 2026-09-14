#!/usr/bin/env python3
"""Exact family: first positivity failure can occur at any prescribed rank."""
import json
from fractions import Fraction
from pathlib import Path

def main():
 rows=[]
 for n in range(3,13):
  # Midpoint between -1/(n-2) and -1/(n-1).
  r=-(Fraction(1,n-2)+Fraction(1,n-1))/2
  full=1+(n-1)*r
  proper=1+(n-2)*r
  transverse=1-r
  assert full<0 and proper>0 and transverse>0
  rows.append({'first_failing_rank':n,'off_diagonal':str(r),'full_all_ones_eigenvalue':str(full),'largest_proper_all_ones_eigenvalue':str(proper),'transverse_eigenvalue':str(transverse)})
 result={'schema':'marici.voevodsky.arbitrarily-late-minimal-negative-rungs.v1','family':'G_n has diagonal 1 and constant off-diagonal r_n','rows':rows,'theorem':'For every n>=3 there is a reversal- and permutation-invariant Hermitian packet whose every proper principal subpacket is positive definite while the full rank-n packet is indefinite.','branching_consequence':'No ancestry reduction using only proper coordinate subpackets is jointly conservative for negative squares, even with complete reversal/permutation coherence.','required_escape':'A branch must retain a mixed all-channel correlation. Such a branch compresses dimension but preserves composite ancestry, so its terminal positivity is not primitive base positivity.'}
 out=Path(__file__).parents[1]/'results'/'arbitrarily_late_minimal_negative_rungs.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'ranks_checked':[3,12],'all_exact_hostiles':True},indent=2))
if __name__=='__main__':main()
