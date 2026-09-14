#!/usr/bin/env python3
"""Exact radial-three-dimensional Green/Dirichlet identity for the theta Gaussian."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_radial_dirichlet_green_form_certificate_20260908.json');args=p.parse_args();r=s.symbols('r',positive=True);checks=0
 phi=s.exp(-s.pi*r*r);lap=s.diff(phi,r,2)+2*s.diff(phi,r)/r
 X=s.pi*r*r
 assert s.simplify(r*r*lap-(4*X*X-6*X)*phi)==0;checks+=1
 dirichlet=s.integrate(s.diff(phi,r)**2*r*r,(r,0,s.oo))
 green=s.integrate(-phi*lap*r*r,(r,0,s.oo))
 assert s.simplify(dirichlet-green)==0;checks+=1
 expected=3*s.sqrt(2)/16
 assert s.simplify(dirichlet-expected)==0;checks+=1
 assert dirichlet.is_positive;checks+=1
 boundary0=s.limit(phi*s.diff(phi,r)*r*r,r,0,dir='+');boundaryInf=s.limit(phi*s.diff(phi,r)*r*r,r,s.oo)
 assert boundary0==0 and boundaryInf==0;checks+=2
 # The signed pointwise Green image integrates to the positive Dirichlet form
 # only after multiplication by -phi and the radial measure.
 signed=s.integrate(-phi*(4*X*X-6*X)*phi,(r,0,s.oo))
 assert s.simplify(signed-dirichlet)==0;checks+=1
 out={'schema':'marici.rh.radial-dirichlet-green-form.v1','status':'positive_radial_form_exact','checks':checks,'source':'phi(r)=exp(-pi r^2)','operator':'Delta_3=d_r^2+(2/r)d_r','identity':'r^2 Delta_3 phi=(4X^2-6X)phi, X=pi r^2','dirichlet_value':'3*sqrt(2)/16','boundary_at_zero':'0','boundary_at_infinity':'0','claim':'the sign-indefinite pointwise theta Green image yields a strictly positive integrated radial Dirichlet form','boundary':'single Gaussian radial source only; modular reciprocal sewing, labelled theta summation, cross terms, and identification with D_bw remain unproved'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'dirichlet_value':out['dirichlet_value']}))
if __name__=='__main__':main()
