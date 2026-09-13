#!/usr/bin/env python3
"""Exact hostile for thresholding small Green innovations."""

import json
from fractions import Fraction
from pathlib import Path

def main():
 rows=[]
 for m in (2,3,4,5,6):
  rho=1-Fraction(1,10**m);d=1-rho*rho
  # r=k_new-rho*k_old has norm^2 d. Scaling by 1/d gives squared
  # norm 1/d, showing coefficient amplification; unit normalization always
  # leaves relative projection error one when this line is discarded.
  rows.append({'rho':str(rho),'raw_innovation_norm_squared':str(d),'inverse_variance':str(1/d),'discarded_unit_relative_error':'1'})
 result={'schema':'marici.coherence.innovation-threshold-uniform-no-go.v1','rows':rows,'all_exact':True,'operator_norm_error_of_any_proper_orthogonal_stage_projection':'1','reason':'a normalized vector in any discarded innovation line is a unit hostile','authorization_needed':['source coefficient bound','probability prior','noise floor','restricted context family']}
 Path(__file__).with_name('innovation-threshold-uniform-no-go.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
