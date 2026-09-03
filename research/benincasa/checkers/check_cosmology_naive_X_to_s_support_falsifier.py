#!/usr/bin/env python3
"""Exact deliberate-failure test of the unauthorized assignment s_i=X_i."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
prior=json.loads((R/'cosmology_p_locus_to_Gysin_base_map.json').read_text());assert prior['passed']
def trim(a):
 while len(a)>1 and a[-1]==0:a.pop()
 return a
def add(a,b):
 c=[F(0)]*max(len(a),len(b))
 for i,x in enumerate(a):c[i]+=x
 for i,x in enumerate(b):c[i]+=x
 return trim(c)
def scale(a,q):return trim([q*x for x in a])
def mul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return trim(c)
def rem(a,b):
 a=a[:]
 while len(a)>=len(b) and a!=[0]:
  q=a[-1]/b[-1];d=len(a)-len(b)
  for i,x in enumerate(b):a[i+d]-=q*x
  trim(a)
 return a
def gcd(a,b):
 while b!=[0]:a,b=b,rem(a,b)
 return scale(a,F(1,a[-1]))
one=[F(1)];u=[F(0),F(1)];s1=one;s2=[F(-1),F(3,2)];s3=[F(0),F(-1,2)]
Lambda=add(add(add(mul(s1,s1),mul(s2,s2)),mul(s3,s3)),add(add(scale(mul(s1,s2),-2),scale(mul(s1,s3),-2)),scale(mul(s2,s3),-2)))
assert Lambda==[F(4),F(-6),F(4)]
candidate=mul(mul(mul(s1,s2),s3),Lambda);D=[F(4),F(-12),F(1),F(12),F(-4)];norm=mul(mul(mul(u,add(u,[-1])),add(u,[-2])),D)
assert gcd(candidate,norm)==u
out={'schema':'marici.benincasa.cosmology-naive-X-to-s-support-falsifier.v1','conjecture':'the deliberate assignment (s1,s2,s3)=(X1,X2,X3), X1=1, has support compatible with the norm residual','assignment':{'s1':'1','s2':'3u/2-1','s3':'-u/2'},'pulled_Lambda_P':'2*(2u^2-3u+2)','pulled_Gysin_denominator':'-u*(3u-2)*(2u^2-3u+2)/2','norm_denominator':'u*(u-1)*(u-2)*D','support_gcd':'u','candidate_only_components':['3u-2','2u^2-3u+2'],'norm_only_components':['u-1','u-2','D'],'supports_equal':False,'conjecture_disposition':'falsified by exact factor comparison','assignment_source_authorized':False,'consequence':'even the tempting coordinate-name identification cannot repair the missing typed base map or relate the parity obstructions','next_conjecture':'the principal wall functions q_g1,q_g2,q_g3 provide a better candidate assignment to s1,s2,s3 on p=0','next_falsifier':'specialize the three sourced q_g functions to the radial p chart, pull back the Gysin denominator, and compare supports exactly','passed':True};(R/'cosmology_naive_X_to_s_support_falsifier.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
