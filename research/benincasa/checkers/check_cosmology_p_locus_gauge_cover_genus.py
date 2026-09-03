#!/usr/bin/env python3
"""Classify the quadratic gauge cover y^2=D(u)."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
prior=json.loads((R/'cosmology_p_locus_quadratic_gauge_source.json').read_text());assert prior['passed']
# Ascending coefficients D=4-12u+u^2+12u^3-4u^4.
D=[Fraction(4),-12,1,12,-4]
def trim(A):
 while len(A)>1 and A[-1]==0:A.pop()
 return A
def divrem(A,B):
 A=A[:];B=trim(B[:]);Q=[Fraction(0)]*max(1,len(A)-len(B)+1)
 while len(A)>=len(B) and any(A):
  k=len(A)-len(B);c=A[-1]/B[-1];Q[k]=c
  for j,b in enumerate(B):A[j+k]-=c*b
  trim(A)
 return trim(Q),trim(A)
def gcd(A,B):
 while any(B):_,r=divrem(A,B);A,B=B,r
 lead=A[-1];return [x/lead for x in A]
Dp=[Fraction(i)*D[i] for i in range(1,len(D))];g=gcd(D,Dp);assert g==[1]
a,b,c,d,e=-4,12,1,-12,4
I=12*a*e-3*b*d+c*c;J=72*a*c*e+9*b*c*d-27*a*d*d-27*b*b*e-2*c**3
delta_binary=4*I**3-J**2;assert (I,J,delta_binary)==(241,-2450,49987584)
out={'schema':'marici.benincasa.cosmology-p-locus-gauge-cover-genus.v1','conjecture':'the minimal cover y^2=D is smooth of genus one','D':'-4u^4+12u^3+u^2-12u+4','gcd_D_Dprime':'1','squarefree':True,'geometric_branch_points_finite':4,'branch_at_infinity':False,'riemann_hurwitz':'2g-2=2*(-2)+4=0','geometric_genus':1,'rational_point':{'u':0,'y':2},'elliptic_curve_over_Q':True,'binary_quartic_invariants':{'I':I,'J':J,'4I3_minus_J2':delta_binary},'conjecture_disposition':'retained by exact test','rational_source_extension':False,'research_consequence':'removing the p-locus residual requires passage to an elliptic function field, not a rational chart gauge','source_authorized':False,'next_conjecture':'this elliptic curve is isomorphic over Q to an existing source elliptic cover','next_falsifier':'compare binary-quartic invariants or j-invariant and require a typed base-compatible isomorphism','passed':True};(R/'cosmology_p_locus_gauge_cover_genus.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
