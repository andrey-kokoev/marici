#!/usr/bin/env python3
"""Exact modular transport law for the first positive theta heat moment."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_first_theta_moment_modular_transport_certificate_20260908.json');args=p.parse_args();y=s.symbols('y',positive=True);thetaDual,thetaDualPrime,Sdual=s.symbols('thetaDual thetaDualPrime Sdual');checks=0
 # Differentiating y^(-1/2)Theta(1/y) gives this first-moment expression.
 S1_from_modular=(y*thetaDual+2*thetaDualPrime)/(4*y**s.Rational(3,2))
 # S1(1/y)=-(1/(2y))Theta'(1/y), hence Theta'(1/y)=-2y Sdual.
 transported=s.simplify(S1_from_modular.subs(thetaDualPrime,-2*y*Sdual))
 expected=y**s.Rational(-1,2)*(thetaDual/4-Sdual)
 assert s.simplify(transported-expected)==0;checks+=1
 # At the self-reciprocal point this forces S1(1)=Theta(1)/8.
 S,thetaOne=s.symbols('S thetaOne');fixed=s.solve(s.Eq(S,thetaOne/4-S),S)
 assert fixed==[thetaOne/8];checks+=1
 out={'schema':'marici.rh.first-theta-moment-modular-transport.v1','status':'exact_modular_transport','checks':checks,'theta_law':'Theta(y)=y^(-1/2)Theta(1/y)','moment':'S1(y)=-y Theta_prime(y)/2','transport':'S1(y)=y^(-1/2)(Theta(1/y)/4-S1(1/y))','self_reciprocal_value':'S1(1)=Theta(1)/8','claim':'the first theta heat moment transforms affinely, not as a pure modular weight','consequence':'its log-curvature proof must retain the inhomogeneous theta term; treating S1 as a modular eigenfunction would be invalid','boundary':'does not prove strict logarithmic concavity'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'fixed_value':'Theta(1)/8'}))
if __name__=='__main__':main()
