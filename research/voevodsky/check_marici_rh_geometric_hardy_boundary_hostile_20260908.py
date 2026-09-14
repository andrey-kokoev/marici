#!/usr/bin/env python3
"""Exact Hardy-H2 boundary hostile for geometric cutoff presentations."""
import argparse,json
from pathlib import Path

def square_coefficients(n):
 # coefficients of (1+q+...+q^n)^2
 return [k+1 if k<=n else 2*n-k+1 for k in range(2*n+1)]
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_geometric_hardy_boundary_hostile_certificate_20260908.json');a=p.parse_args();rows=[];checks=0;previous_g=previous_square=-1
 for n in (2,3,5,10,20,40):
  g_h2_squared=n+1
  coeffs=square_coefficients(n);square_h2_squared=sum(c*c for c in coeffs)
  closed=(n+1)*(2*n*n+4*n+3)//3
  assert square_h2_squared==closed;checks+=1
  assert g_h2_squared>previous_g and square_h2_squared>previous_square;checks+=2
  previous_g,previous_square=g_h2_squared,square_h2_squared
  rows.append({'depth':n,'g_h2_norm_squared':g_h2_squared,'square_h2_norm_squared':square_h2_squared,'square_formula':f'({n+1})*(2*{n}^2+4*{n}+3)/3'})
 out={'schema':'marici.rh.geometric-hardy-boundary-hostile.v1','status':'not_hardy_h2_cauchy','checks':checks,'rows':rows,'claim':'geometric cutoff carriers and their square presentations have unbounded H2 boundary norms','residual':'g_n has H2 norm squared n+1; g_n squared has norm squared (n+1)(2n^2+4n+3)/3','disposition':'the unrenormalized geometric presentation cannot supply the seam completion; retain only its interior compact-disk theorem','boundary':'does not test the determinant-three-renormalized operator carrier or a different source-derived rigging'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'max_depth':rows[-1]['depth']}))
if __name__=='__main__':main()
