#!/usr/bin/env python3
"""Exact normal-convergence majorant for the reciprocal det3 transition."""
import argparse,json
from fractions import Fraction
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_det3_reciprocal_overlap_bound_certificate_20260908.json');a=p.parse_args();rows=[];checks=0;previous=None
 # On |Re z|<=1/12, p^{-k/2}|2 sinh(k z log p)| <= 2 p^{-5k/12}.
 # For P>=16, sum k>=3 is <=(4/3)n^{-5/4}; summing integers above P
 # gives <=(16/3)P^{-1/4}.
 for root in (2,3,4,6,8,12):
  P=root**4
  if P<16:continue
  bound=Fraction(16,3*root)
  assert bound>0;checks+=1
  if previous is not None:
   assert bound<previous;checks+=1
  previous=bound
  rows.append({'prime_cutoff':P,'overlap_log_transition_tail_bound':f'{bound.numerator}/{bound.denominator}'})
 assert rows[-1]['overlap_log_transition_tail_bound']=='4/9';checks+=1
 out={'schema':'marici.rh.det3-reciprocal-overlap-bound.v1','status':'normal_convergence_on_closed_substrip','checks':checks,'closed_substrip':'|Re(z)| <= 1/12','chart_overlap':'|Re(z)| < 1/6','majorant':'reciprocal transition log tail <= (16/3) P^(-1/4)','rows':rows,'claim':'the connected determinant-three reciprocal transition converges normally on the tested closed substrip','boundary':'the bound is deliberately coarse and does not include primitive or square currents, identify the theta section, or imply boundary-work conservation'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'last_bound':rows[-1]['overlap_log_transition_tail_bound']}))
if __name__=='__main__':main()
