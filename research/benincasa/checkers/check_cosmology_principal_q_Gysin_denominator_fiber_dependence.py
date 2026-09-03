#!/usr/bin/env python3
"""Exact expansion of the q-based Gysin denominator on p=0."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
prior=json.loads((R/'cosmology_principal_q_to_s_support_falsifier.json').read_text());assert prior['passed']
# Sparse polynomials in independent affine fiber functions A=q_g1, B=q_g2.
def add(x,y):
 z=dict(x)
 for e,c in y.items():z[e]=z.get(e,0)+c
 return {e:c for e,c in z.items() if c}
def scale(x,c):return {e:c*v for e,v in x.items() if c*v}
def mul(x,y):
 z={}
 for (i,j),a in x.items():
  for (k,l),b in y.items():z[(i+k,j+l)]=z.get((i+k,j+l),0)+a*b
 return {e:c for e,c in z.items() if c}
A={(1,0):1};B={(0,1):1};C=add(A,B)
Lambda=add(add(add(mul(A,A),mul(B,B)),mul(C,C)),add(add(scale(mul(A,B),-2),scale(mul(A,C),-2)),scale(mul(B,C),-2)))
assert Lambda=={(1,1):-4}
den=mul(mul(mul(A,B),C),Lambda);assert den=={(3,2):-4,(2,3):-4}
out={'schema':'marici.benincasa.cosmology-principal-q-Gysin-denominator-fiber-dependence.v1','conjecture':'imposing q_g3=q_g1+q_g2 makes the q-based Gysin denominator independent of fiber coordinates','p_relation':'q_g3=q_g1+q_g2','pulled_Lambda_P':'-4*q_g1*q_g2','pulled_denominator':'-4*q_g1^2*q_g2^2*(q_g1+q_g2)','fiber_total_degree':5,'nonconstant_monomials':{'q_g1^3*q_g2^2':-4,'q_g1^2*q_g2^3':-4},'fiber_independent':False,'conjecture_disposition':'falsified by exact expansion','consequence':'the only sourced principal relation sharpens rather than cancels the fiber support, so this route cannot define a divisor on the u base','next_conjecture':'a nonzero rational diagonal rescaling s1=a*q_g1, s2=b*q_g2, s3=c*q_g3 can cancel the fiber dependence','next_falsifier':'classify the quadratic coefficients of Lambda_P after q_g3=q_g1+q_g2 and prove whether any nonzero a,b,c make the denominator base-only','passed':True};(R/'cosmology_principal_q_Gysin_denominator_fiber_dependence.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
