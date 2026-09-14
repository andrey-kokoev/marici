#!/usr/bin/env python3
"""Exact adjacent-label hostile to the natural diagonal Dirichlet weight."""
import argparse,json
from pathlib import Path
import sympy as s

def gram(n,m):return s.Rational(3,2)*n*n*m*m/(n*n+m*m)**s.Rational(5,2)
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_diagonal_weight_margin_hostile_certificate_20260908.json');args=p.parse_args();n=s.symbols('n',positive=True);checks=0
 energy=s.simplify(gram(n,n)+gram(n+1,n+1)-2*gram(n,n+1))
 weight=s.simplify(1/n+1/(n+1))
 quotient=s.simplify(energy/weight)
 assert s.limit(quotient,n,s.oo)==0;checks+=1
 scaled=s.limit(n*n*quotient,n,s.oo)
 assert s.simplify(scaled-33*s.sqrt(2)/128)==0;checks+=1
 rows=[]
 for k in (2,4,8,16,32,64):
  q=s.simplify(quotient.subs(n,k));assert q.is_positive is True;checks+=1
  rows.append({'adjacent_labels':[k,k+1],'exact_rayleigh':str(q)})
 out={'schema':'marici.rh.diagonal-weight-margin-hostile.v1','status':'diagonal_weight_not_uniformly_coercive','checks':checks,'test_vector':'e_n-e_(n+1)','coefficient_weight':'sum |c_n|^2/n','rayleigh_limit':'0','scaled_limit':'lim n^2 R_n=33*sqrt(2)/128','rows':rows,'claim':'weighting by the exact diagonal decay repairs individual label norms but not near-collinearity of adjacent high labels','disposition':'a viable completion must control label derivatives/separation or quotient the asymptotically redundant direction; a diagonal weight alone is insufficient','boundary':'does not refute a graph norm with label-difference control or another source-derived quotient'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'scaled_limit':out['scaled_limit']}))
if __name__=='__main__':main()
