#!/usr/bin/env python3
"""Transport fixed theta wall/odd norms to the relative three-port quotient."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_three_port_theta_normalization_certificate_20260908.json');args=p.parse_args();checks=0
 r=s.Matrix([1,1,1]);u=s.Matrix([1,1,-2]);v=s.Matrix([1,-1,0])
 Pi=s.Matrix([[1,0,-1],[0,1,-1]])
 w=s.Matrix([s.Rational(1,2),s.Rational(1,2)]);j=s.Matrix([s.Rational(1,4),-s.Rational(1,4)])
 assert Pi*r==s.zeros(2,1);checks+=1
 assert Pi*(u/6)==w;checks+=1
 assert Pi*(v/4)==j;checks+=1
 metric=2*s.eye(2)
 even_norm=(w.T*metric*w)[0];odd_norm=(j.T*metric*j)[0]
 assert even_norm==1 and odd_norm==s.Rational(1,4);checks+=2
 # If u and v are orthogonal quotient eigenvectors, these source norms force
 # lambda_even and lambda_odd from q(u/6)=1, q(v/4)=1/4.
 le=s.solve(s.Eq(6*s.Symbol('le')/36,even_norm),s.Symbol('le'))[0]
 lo=s.solve(s.Eq(2*s.Symbol('lo')/16,odd_norm),s.Symbol('lo'))[0]
 assert (le,lo)==(6,2);checks+=1
 G=s.Matrix([[2,0,-2],[0,2,-2],[-2,-2,4]])
 assert G*r==s.zeros(3,1) and G*u==le*u and G*v==lo*v;checks+=1
 assert G==Pi.T*metric*Pi;checks+=1
 out={'schema':'marici.rh.three-port-theta-normalization.v1','status':'unique_reciprocal_even_green_form_under_quotient_coordinate','checks':checks,'quotient_coordinate':'Pi(a,b,c)=(a-c,b-c)','normalized_even':'u/6 maps to w_theta=(1/2,1/2)','normalized_odd':'v/4 maps to j_theta=(1/4,-1/4)','endpoint_metric':'2I','lambda_even':6,'lambda_odd':2,'green_matrix':[[int(G[i,j]) for j in range(3)] for i in range(3)],'factorization':'G=Pi^T (2I) Pi','claim':'the fixed theta wall and odd norms determine the reciprocal-even real-symmetric part once Pi is the source-authorized quotient coordinate','boundary':'a Hermitian reciprocal-oriented form may also have an imaginary polarization invisible to these norms; the complete Green form is not unique until that seam current is derived'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'lambda_even':6,'lambda_odd':2}))
if __name__=='__main__':main()
