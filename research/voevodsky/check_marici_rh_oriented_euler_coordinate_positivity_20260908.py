#!/usr/bin/env python3
"""Check positivity margin for source-declared strict/all-grade Euler odd coordinates."""
import argparse,json,math
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_oriented_euler_coordinate_positivity_certificate_20260908.json');args=p.parse_args();u=s.symbols('u',positive=True);checks=0
 hall=2*u/(s.exp(u)-1) # L=2u, r=e^-u
 derivative=s.factor(s.diff(hall,u))
 assert s.simplify(derivative-2*(s.exp(u)*(1-u)-1)/(s.exp(u)-1)**2)==0;checks+=1
 # phi=e^u(1-u)-1 has phi(0)=0 and phi'=-u e^u<0, so hall decreases from 2.
 phi=s.exp(u)*(1-u)-1
 assert s.simplify(s.diff(phi,u)+u*s.exp(u))==0;checks+=1
 hstrict=2*u*(s.exp(-u)+s.exp(-2*u))
 assert s.simplify((hall-hstrict)-2*u*s.exp(-2*u)/(s.exp(u)-1))==0;checks+=1
 samples=[]
 for prime in (2,3,5,7,11,101,1009):
  L=math.log(prime);hs=L*(prime**-.5+prime**-1);ha=L*prime**-.5/(1-prime**-.5)
  assert 0<hs<ha<2;checks+=1;samples.append({'p':prime,'h_strict':hs,'h_all_grade':ha,'det_margin_all_grade':4-ha*ha})
 out={'schema':'marici.rh.oriented-euler-coordinate-positivity.v1','status':'euler_odd_coordinate_inside_positive_cone','checks':checks,'strict_coordinate':'h_p=L(p^-1/2+p^-1)','all_grade_coordinate':'h_p=L p^-1/2/(1-p^-1/2)','proof':'with u=L/2, h_all=2u/(e^u-1) decreases strictly from 2 because d/du[e^u(1-u)-1]=-u e^u<0; h_strict<h_all','consequence':'for every p>1, 0<h_strict<h_all<2, so H_h=[[2,ih],[-ih,2]] is positive definite','samples':samples,'boundary':'the Euler scalar and sign are source-declared, but identifying it with the imaginary entry of the three-port theta Green representation still requires quadratic functoriality'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'p2_all_grade':samples[0]['h_all_grade']}))
if __name__=='__main__':main()
