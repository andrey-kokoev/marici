#!/usr/bin/env python3
"""Exact centered-Green action and sign audit on one completed theta label."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_completed_theta_green_source_certificate_20260908.json');args=p.parse_args();u,a=s.symbols('u a', real=True, positive=True);X=s.symbols('X',positive=True);checks=0
 phi=s.exp(u/2)*s.exp(-a*s.exp(2*u));Lphi=s.simplify(s.diff(phi,u,2)-phi/4)
 expected=s.exp(u/2)*(4*(a*s.exp(2*u))**2-6*a*s.exp(2*u))*s.exp(-a*s.exp(2*u))
 assert s.simplify(Lphi-expected)==0;checks+=1
 polynomial=s.factor(4*X**2-6*X);assert polynomial==2*X*(2*X-3);checks+=1
 assert polynomial.subs(X,s.Rational(1,1))<0;checks+=1
 assert polynomial.subs(X,s.Rational(2,1))>0;checks+=1
 assert s.solve(polynomial,X)==[s.Rational(3,2)];checks+=1
 out={'schema':'marici.rh.completed-theta-green-source.v1','status':'exact_factorization_sign_indefinite','checks':checks,'theta_label':'phi_n(u)=exp(u/2) exp(-a exp(2u)), a=pi n^2','green_operator':'L=d_u^2-1/4','factor':'4X^2-6X=2X(2X-3), X=a exp(2u)','positive_root':'3/2','sign':'negative for 0<X<3/2; positive for X>3/2','claim':'the centered Green image of each completed theta label is exact but not pointwise one-signed','consequence':'boundary conservation cannot be obtained from pointwise positivity of L phi_n; it must use the integrated modularly sewn packet or another factorization','boundary':'does not determine the sign of the fully summed and reciprocally sewn Hermitian form'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'root':'3/2'}))
if __name__=='__main__':main()
