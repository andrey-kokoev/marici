#!/usr/bin/env python3
"""Classify affine lines with constant Gysin denominator."""
import itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
prior=json.loads((R/'cosmology_principal_q_affine_leading_degree_no_go.json').read_text());assert prior['passed']
def trim(a):
 while len(a)>1 and a[-1]==0:a.pop()
 return a
def add(a,b):
 c=[0]*max(len(a),len(b))
 for i,x in enumerate(a):c[i]+=x
 for i,x in enumerate(b):c[i]+=x
 return trim(c)
def scale(a,q):return trim([q*x for x in a])
def mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return trim(c)
def F(c,d):
 ss=[[c[i],d[i]] for i in range(3)]
 L=add(add(add(mul(ss[0],ss[0]),mul(ss[1],ss[1])),mul(ss[2],ss[2])),add(add(scale(mul(ss[0],ss[1]),-2),scale(mul(ss[0],ss[2]),-2)),scale(mul(ss[1],ss[2]),-2)))
 return mul(mul(mul(ss[0],ss[1]),ss[2]),L)
tested=zero_lines=0
for vals in itertools.product(range(-2,3),repeat=6):
 c=vals[:3];d=vals[3:]
 if d==(0,0,0):continue
 f=F(c,d);tested+=1
 if f==[0]:zero_lines+=1
 assert not (len(f)==1 and f[0]!=0)
out={'schema':'marici.benincasa.cosmology-rank-one-affine-Gysin-constant-line.v1','conjecture':'a nonconstant affine line can pull the Gysin denominator back to a nonzero base constant','line':'s_i(t)=c_i+d_i*t','unit_argument':'if s1*s2*s3*Lambda_P is a nonzero constant in Q[t], every factor is a unit, hence every s_i is constant','nonconstant_line_with_nonzero_constant_pullback_exists':False,'constant_zero_lines':'contained in the Gysin divisor and therefore degenerate','bounded_nonconstant_lines_tested':tested,'bounded_zero_pullbacks':zero_lines,'bounded_nonzero_constant_pullbacks':0,'conjecture_disposition':'falsified for all affine lines over Q','rank_class_consequence':'rank one cannot repair the base-map obstruction; rank zero has no fiber comparison','next_conjecture':'the accumulated base-map and parity results establish the strongest obstruction under the active source envelope','next_falsifier':'synthesize the typed gates and search for any surviving source-authorized primitive integral route','passed':True};(R/'cosmology_rank_one_affine_Gysin_constant_line.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
