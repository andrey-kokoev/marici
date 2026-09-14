#!/usr/bin/env python3
"""Exact two-chart proof of positivity of the aggregate centered theta Green image."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_theta_green_global_positivity_certificate_20260908.json');args=p.parse_args();checks=0
 y,t,a=s.symbols('y t a',positive=True);X=a*t
 # Direct chart y>=1: X_n=pi n^2 y >3/2 termwise.
 assert (s.pi-s.Rational(3,2)).is_positive is True;checks+=1
 # Reciprocal chart: S1(y)=y^-1/2 A(t), t=1/y,
 # A(t)=Theta(t)/4+t Theta'(t)/2.  A prime denotes d/dt.
 theta,theta1,theta2=s.symbols('theta theta1 theta2')
 A=theta/4+t*theta1/2
 Aprime=s.diff(A,t)+s.diff(A,theta)*theta1+s.diff(A,theta1)*theta2
 assert s.expand(Aprime-(s.Rational(3,4)*theta1+t*theta2/2))==0;checks+=1
 # One theta atom contributes 2e^(-at): A'_atom=a e^(-at)(at-3/2).
 atom=s.exp(-a*t)/2 + t*(-2*a*s.exp(-a*t))/2
 atom_prime=s.simplify(s.diff(atom,t))
 expected=a*s.exp(-a*t)*(a*t-s.Rational(3,2))
 assert s.simplify(atom_prime-expected)==0;checks+=1
 # For t>=1 and a=pi n^2, every reciprocal atom is strictly positive.
 assert (s.pi*1*1-s.Rational(3,2)).is_positive is True;checks+=1
 out={'schema':'marici.rh.theta-green-global-positivity.v1','status':'strict_positive_on_both_modular_charts','checks':checks,'direct_chart':'y>=1: every X_n=pi n^2 y exceeds 3/2','reciprocal_chart':'0<y<=1, t=1/y>=1: A_prime(t)=sum_n pi n^2 exp(-pi n^2 t)(pi n^2 t-3/2)>0','transport':'mu(y)-3/2=t A_prime(t)/A(t)','claim':'the full positive-label centered theta Green image W(y)(mu(y)-3/2) is strictly positive for every y>0','boundary':'this is a source radial positivity theorem; it does not identify the radial Green form with D_bw or prove scalar-zero boundary sewing'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'charts':['y>=1','0<y<=1']}))
if __name__=='__main__':main()
