#!/usr/bin/env python3
"""Exact realified seam/conormal model for reciprocal RH boundary work."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_realified_seam_conormal_certificate_20260908.json');args=p.parse_args();x,y,B=s.symbols('x y B',real=True);checks=0
 # z=s-1/2=x+iy; Real reciprocal reflection is z -> -conj? In coordinates
 # s -> 1-conj(s), hence (x,y)->(-x,y).
 sigma=lambda f:s.expand(f.subs({x:-x},simultaneous=True))
 assert sigma(x)==-x and sigma(y)==y;checks+=2
 dbw=-2*x*B
 assert sigma(dbw)==2*x*B;checks+=1
 assert s.rem(dbw,s.Poly(x,x).as_expr(),x)==0;checks+=1
 conormal_coefficient=s.simplify(dbw/x);assert conormal_coefficient==-2*B;checks+=1
 # The complex polar endpoints s=0,1 become real points (-1/2,0),(1/2,0),
 # exchanged by the involution and disjoint from the seam x=0.
 poles=[(s.Rational(-1,2),0),(s.Rational(1,2),0)]
 assert [(-px,py) for px,py in poles]==list(reversed(poles));checks+=1
 assert all(px!=0 for px,_ in poles);checks+=1
 out={'schema':'marici.rh.realified-seam-conormal.v1','status':'real_seam_conormal_typed','checks':checks,'base':'Spec R[x,y] as the realification of z=s-1/2','reciprocal_involution':'(x,y)->(-x,y)','fixed_seam':'Z=V(x)','conormal_generator':'x mod x^2','boundary_work':'D_bw=-2xB','conormal_coefficient':'-2B','polar_points':['(-1/2,0)','(1/2,0)'],'claim':'D_bw is an involution-odd first-order conormal section supported relative to the Real fixed seam, while the polar points form a separate exchanged locus','consequence':'a complex Zariski seam is the wrong DAG base; the candidate localization must use the realified parameter space or an equivariant/derived-analytic enhancement','boundary':'typing the coordinate and first-order divisibility does not realize Xi or the completed operator packet as IndCoh on this base'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'seam':'x=0','dbw':out['boundary_work']}))
if __name__=='__main__':main()
