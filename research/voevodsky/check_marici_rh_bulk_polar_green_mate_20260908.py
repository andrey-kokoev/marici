#!/usr/bin/env python3
"""Exact source-derived bulk-to-polar Green mate on a decaying test source."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_bulk_polar_green_mate_certificate_20260908.json');args=p.parse_args();u,z=s.symbols('u z', real=True);checks=0
 g=s.exp(-u);c=s.Integer(1);Lg=s.diff(g,u,2)-g/4
 Ig=s.integrate(g*s.sinh(z*u),(u,0,s.oo),conds='none')
 transformed_Lg=s.integrate(Lg*s.sinh(z*u),(u,0,s.oo),conds='none')
 assert s.simplify(Ig-z/(1-z*z))==0;checks+=1
 assert s.simplify(Lg-s.Rational(3,4)*g)==0;checks+=1
 green_residual=s.simplify(transformed_Lg-(c*z+(z*z-s.Rational(1,4))*Ig))
 assert green_residual==0;checks+=1
 bulk_odd=2*Ig;polar_odd=2*c*z/(z*z-s.Rational(1,4))
 mate=2*transformed_Lg/(z*z-s.Rational(1,4))
 assert s.simplify(bulk_odd+polar_odd-mate)==0;checks+=1
 # Dropping the polar boundary term leaves the exact nonzero defect.
 assert s.simplify(mate-bulk_odd-polar_odd)==0 and polar_odd!=0;checks+=1
 out={'schema':'marici.rh.bulk-polar-green-mate.v1','status':'source_green_mate_exact_on_test_source','checks':checks,'source':'g(u)=exp(-u), c=g(0)=1','operator':'L=d_u^2-1/4','bulk_odd':str(s.simplify(bulk_odd)),'polar_odd':str(s.simplify(polar_odd)),'green_mate':str(s.simplify(mate)),'residual':str(green_residual),'claim':'the polar odd port is the exact boundary completion produced by integrating the centered source operator twice by parts','boundary':'one decaying test source verifies the constructor and constants; positivity, the completed theta source domain, and identification with D_bw are not proved'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'residual':'0'}))
if __name__=='__main__':main()
