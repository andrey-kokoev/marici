#!/usr/bin/env python3
"""Exact finite Gram audit for labelled radial theta Gaussians."""
import argparse,json
from pathlib import Path
import sympy as s

def entry(n,m):return s.Rational(3,2)*n*n*m*m/s.Pow(n*n+m*m,s.Rational(5,2))
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_labelled_theta_dirichlet_gram_certificate_20260908.json');args=p.parse_args();r=s.symbols('r',positive=True);checks=0;rows=[]
 for n,m in ((1,1),(1,2),(2,3),(3,4)):
  pn=s.exp(-s.pi*n*n*r*r);pm=s.exp(-s.pi*m*m*r*r)
  integral=s.integrate(s.diff(pn,r)*s.diff(pm,r)*r*r,(r,0,s.oo))
  assert s.simplify(integral-entry(n,m))==0;checks+=1
 for size in (1,2,3,4):
  G=s.Matrix(size,size,lambda i,j:entry(i+1,j+1));det=s.simplify(G.det())
  assert det.is_positive is True;checks+=1
  rows.append({'size':size,'determinant':str(det),'positive':True})
 out={'schema':'marici.rh.labelled-theta-dirichlet-gram.v1','status':'finite_labelled_gram_positive','checks':checks,'entry_formula':'G_nm=(3/2)n^2m^2/(n^2+m^2)^(5/2)','principal_minors':rows,'claim':'the radial Dirichlet form is positive definite on the tested spans of the first four labelled theta Gaussians','boundary':'finite labelled spans only; no uniform lower frame bound, infinite completion, reciprocal sewing, or identification with D_bw is claimed'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'max_size':4}))
if __name__=='__main__':main()
