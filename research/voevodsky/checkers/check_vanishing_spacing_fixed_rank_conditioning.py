#!/usr/bin/env python3
"""Exact/numerical audit of fixed-rank conditioning as spacing tends to zero."""
import json,math,cmath
from pathlib import Path

def main():
 # Signed hostile 2 delta_0-delta_x, x=1: k0=1, k1=2-exp(-ih).
 rows=[]
 for h in (.5,.25,.125,.0625,.03125,.015625):
  k1=2-cmath.exp(-1j*h);det=1-abs(k1)**2
  exact=4*(math.cos(h)-1)
  assert abs(det-exact)<1e-14
  rows.append({'h':h,'rank_two_determinant':det,'determinant_over_h_squared':det/(h*h)})
 assert all(abs(r['determinant_over_h_squared']+2)<.05 for r in rows[-3:])
 result={'schema':'marici.voevodsky.vanishing-spacing-fixed-rank-conditioning.v1','signed_source':'2 delta_0-delta_1','rows':rows,'exact_determinant':'4(cos(h)-1)','small_h_asymptotic':'-2h^2+O(h^4)','conclusion':'A fixed-rank test can detect the negative atom for every nonzero h, but its margin collapses quadratically as h tends to zero.','computational_requirement':'Coefficient error must shrink at least on the h^2 scale at fixed rank, or rank/precision must grow during refinement.','correction':'Finite positivity through rank thirteen at three decreasing spacings is evidence at three scales, not a numerically uniform de-aliasing sequence.'}
 out=Path(__file__).parents[1]/'results'/'vanishing_spacing_fixed_rank_conditioning.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
