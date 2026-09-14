#!/usr/bin/env python3
"""Exact grade decomposition of the completed Euler odd orientation coordinate."""
import argparse,json,math
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_euler_odd_connected_tail_decomposition_certificate_20260908.json');args=p.parse_args();r,L=s.symbols('r L',positive=True);checks=0
 h1=L*r;h2=L*r**2;hconn=L*r**3/(1-r);hall=L*r/(1-r)
 assert s.simplify(h1+h2+hconn-hall)==0;checks+=1
 assert s.simplify(hall-(h1+h2)-hconn)==0;checks+=1
 # For r=p^-1/2, the connected tail is bounded by a constant times log(p)p^-3/2.
 # Since p>=2 gives 1/(1-r)<=1/(1-2^-1/2), comparison with all integers converges.
 C=1/(1-2**-.5);samples=[];partial=0.0
 for prime in (2,3,5,7,11,101,1009):
  rr=prime**-.5;tail=math.log(prime)*rr**3/(1-rr);major=C*math.log(prime)*prime**-1.5
  assert 0<tail<=major*(1+1e-14);checks+=1
  partial+=tail;samples.append({'p':prime,'connected_tail':tail,'majorant':major})
 # Exact truncation residual after grade K.
 K=s.symbols('K',integer=True,positive=True)
 residual=L*r**(K+1)/(1-r)
 assert s.simplify(hall-L*sum(r**k for k in range(1,6))-residual.subs(K,5))==0;checks+=1
 out={'schema':'marici.rh.euler-odd-connected-tail-decomposition.v1','status':'connected_tail_exact_and_absolutely_summable','checks':checks,'primitive':'L r','square':'L r^2','connected':'L r^3/(1-r)','completed':'L r/(1-r)','identity':'completed=primitive+square+connected','grade_K_residual':'L r^(K+1)/(1-r)','prime_majorant':'C log(p) p^-3/2, C=(1-2^-1/2)^-1','claim':'the difference between the all-grade and strict odd coordinates is exactly the grade>=3 reservoir, not a fitted correction','consequence':'the all-grade imaginary Green entry may be used only when the connected reservoir is retained','samples':samples,'boundary':'absolute scalar summability does not by itself prove the labelled Schur-return representation or quadratic functoriality'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'sample_tail_sum':partial}))
if __name__=='__main__':main()
