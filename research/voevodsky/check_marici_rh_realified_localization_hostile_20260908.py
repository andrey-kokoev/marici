#!/usr/bin/env python3
"""Hostile: Real reciprocal equivariance does not support the zero locus on the seam."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_realified_localization_hostile_certificate_20260908.json');args=p.parse_args();x,y=s.symbols('x y',real=True);checks=0
 sigma=lambda f:s.expand(f.subs({x:-x},simultaneous=True))
 section=x*x+y*y-1
 assert sigma(section)==section;checks+=1
 point={x:1,y:0};assert section.subs(point)==0;checks+=1
 assert point[x]!=0;checks+=1
 B=s.Integer(1);dbw=-2*x*B;assert dbw.subs(point)==-2;checks+=1
 # The section is square-free and has no x factor, so its divisor is not
 # supported on the seam ideal (x).
 assert s.gcd(section,x)==1;checks+=1
 out={'schema':'marici.rh.realified-localization-hostile.v1','status':'equivariance_insufficient_for_seam_support','checks':checks,'section':'F=x^2+y^2-1','reciprocal_invariance':'F(-x,y)=F(x,y)','off_seam_zero':'(x,y)=(1,0)','boundary_work_at_zero':'-2 for B=1','gcd_with_seam_generator':'1','claim':'Real reciprocal invariance and conormal typing of D_bw do not imply that zeros of a distinguished section are supported on the fixed seam','consequence':'the IndCoh localization fibre is seam-supported only after a source-specific support/transversality theorem; assuming that support would restate RH','boundary':'this polynomial is a structural hostile, not a model of the theta section'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'off_seam_zero':'(1,0)'}))
if __name__=='__main__':main()
