#!/usr/bin/env python3
"""Hostile: compact-disk geometric bounds do not extend uniformly to |q|=1."""
import argparse,json
from fractions import Fraction
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_carrier_boundary_nonuniformity_certificate_20260908.json');a=p.parse_args();rows=[];checks=0
 for n in (2,5,10):
  bounds=[]
  for m in (2,4,8,16,32):
   r=Fraction(m-1,m);tail=r**(n+1)/(1-r);square=2*tail/(1-r)
   bounds.append(square);rows.append({'depth':n,'radius':f'{m-1}/{m}','square_error_bound':f'{square.numerator}/{square.denominator}'})
  assert bounds[-1]>bounds[0];checks+=1
  # At fixed cutoff the bound diverges as r approaches one; compact convergence
  # supplies no cutoff uniform over the whole open disk.
  assert bounds[-1]>n;checks+=1
 out={'schema':'marici.rh.carrier-boundary-nonuniformity.v1','status':'compact_only','checks':checks,'rows':rows,'claim':'the proved geometric convergence is locally uniform on compact subdisks but not uniform as the radius approaches one','residual':'boundary/seam control requires a different source norm or boundary theorem','boundary':'growth of this bound alone does not prove that every alternative norm or renormalized presentation fails'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'depths':[2,5,10]}))
if __name__=='__main__':main()
