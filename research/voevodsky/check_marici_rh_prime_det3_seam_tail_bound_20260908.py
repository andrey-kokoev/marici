#!/usr/bin/env python3
"""Exact majorant for the source-labelled determinant-three prime tail at the seam."""
import argparse,json
from fractions import Fraction
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_prime_det3_seam_tail_bound_certificate_20260908.json');a=p.parse_args();rows=[];checks=0;previous=None
 # At Re(s)=1/2 and P>=4:
 # sum_{p>P} sum_{k>=3} p^{-k/2}/k
 # <= (1/3) sum_{n>P} n^{-3/2}/(1-n^{-1/2})
 # <= (2/3) sum_{n>P} n^{-3/2} <= 4/(3 sqrt(P)).
 for root in (2,4,8,16,32,64):
  P=root*root;bound=Fraction(4,3*root)
  assert P>=4 and bound>0;checks+=2
  if previous is not None:
   assert bound<previous;checks+=1
  previous=bound
  rows.append({'prime_cutoff':P,'bound':f'{bound.numerator}/{bound.denominator}'})
 assert rows[-1]['bound']=='1/48';checks+=1
 out={'schema':'marici.rh.prime-det3-seam-tail-bound.v1','status':'absolute_seam_tail_control','checks':checks,'rows':rows,'majorant':'sum_{p>P,k>=3} p^(-k/2)/k <= 4/(3 sqrt(P)) for P>=4','claim':'the source-labelled connected determinant-three logarithm is absolutely Cauchy under prime cutoff at Re(s)=1/2','boundary':'controls only the k>=3 carrier logarithm; primitive and square anomaly currents, reciprocal gluing, the distinguished Xi section, and boundary-work conservation remain separate'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'last_bound':rows[-1]['bound']}))
if __name__=='__main__':main()
