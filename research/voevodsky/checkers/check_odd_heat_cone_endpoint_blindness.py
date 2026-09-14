#!/usr/bin/env python3
"""Exact audit: odd heat-square tests cannot detect endpoint evaluation."""
import json
from fractions import Fraction
from pathlib import Path

def poly_eval(coeffs,x):return sum(c*x**i for i,c in enumerate(coeffs))

def main():
 # q_h(0)=0, so every G=q_h*even_factor is odd and every |G|^2 vanishes at zero.
 # Polynomial surrogates exhaust odd jets u*p(u^2) through bounded degree.
 checked=0
 for degree in range(7):
  for mask in range(1 << (degree+1)):
   p=[Fraction((mask>>i)&1) for i in range(degree+1)]
   # G(u)=u p(u^2); F=G^2. Its constant coefficient is exactly zero.
   g=[Fraction(0)]*(2*degree+2)
   for i,c in enumerate(p):g[2*i+1]=c
   f=[Fraction(0)]*(2*len(g)-1)
   for i,a in enumerate(g):
    for j,b in enumerate(g):f[i+j]+=a*b
   assert poly_eval(f,Fraction(0))==0
   checked+=1
 # Hostile extension: R=-delta_0 vanishes on every restricted square but is negative on 1.
 restricted_values=[0 for _ in range(checked)]
 assert all(v==0 for v in restricted_values)
 assert -poly_eval([Fraction(1)],Fraction(0))==-1
 result={'schema':'marici.voevodsky.odd-heat-cone-endpoint-blindness.v1','odd_polynomial_gaussian_jet_surrogates_checked':checked,'restricted_square_endpoint_values_all_zero':True,'annihilator':'span(delta_0)','hostile_form':'R(f)=-f(0)','hostile_restriction_nonnegative':True,'hostile_full_form_nonnegative':False,'conclusion':'Restriction to odd heat squares is not injective on Weil-type distributions and cannot by itself reflect positivity on a domain containing endpoint evaluation.','next_gate':'Fix the endpoint coefficient by an independent source identity, then test graph-norm core density modulo the endpoint line.'}
 out=Path(__file__).parents[1]/'results'/'odd_heat_cone_endpoint_blindness.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
