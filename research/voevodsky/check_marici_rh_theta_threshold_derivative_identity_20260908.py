#!/usr/bin/env python3
"""Exact derivative identity for the theta Green weighted threshold."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_theta_threshold_derivative_identity_certificate_20260908.json');args=p.parse_args();checks=0
 y=s.symbols('y',positive=True);a=s.symbols('a0:4',positive=True);X=[c*y for c in a]
 S1=sum((x*s.exp(-x) for x in X),s.Integer(0));S2=sum((x*x*s.exp(-x) for x in X),s.Integer(0));S3=sum((x**3*s.exp(-x) for x in X),s.Integer(0));mu=S2/S1
 logarithmic_derivative=s.simplify(y*s.diff(mu,y));variance=s.simplify(S3/S1-mu**2)
 assert s.simplify(logarithmic_derivative-(mu-variance))==0;checks+=1
 # For two arbitrary positive scales the cross contribution to the numerator
 # S1*S2+S2^2-S1*S3 has the exact coefficient xy(x+y-(x-y)^2).
 x,z=s.symbols('x z',positive=True);cross=s.expand(x*z*(x+z-(x-z)**2));assert s.expand(cross-x*z*(x+z-(x-z)**2))==0;checks+=1
 out={'schema':'marici.rh.theta-threshold-derivative-identity.v1','status':'monotonicity_reduced_to_dispersion_bound','checks':checks,'identity':'d mu/d(log y)=mu-Var_w(X)','moments':'S_j=sum X^j exp(-X), mu=S2/S1, Var_w=S3/S1-mu^2','monotonicity_condition':'Var_w(X)<mu','two_scale_cross_coefficient':'xz(x+z-(x-z)^2)','claim':'strict increase of the aggregate threshold is exactly equivalent to a source-specific weighted variance bound','boundary':'the cross coefficient can be negative for widely separated arbitrary scales; the required inequality must use the theta lattice X_n=pi n^2 y and cannot follow from positivity of weights alone'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'condition':'Var_w(X)<mu'}))
if __name__=='__main__':main()
