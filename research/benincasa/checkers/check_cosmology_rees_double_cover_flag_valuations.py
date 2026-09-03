#!/usr/bin/env python3
"""Compute exact K valuations on the two moving split flags."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
def add(a,b):
 n=max(len(a),len(b));return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n)]
def neg(a):return [-x for x in a]
def mul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c
def pw(a,n):
 r=[F(1)]
 for _ in range(n):r=mul(r,a)
 return r
def scale(a,c):return [c*x for x in a]
def trim(a):
 while len(a)>1 and not a[-1]:a.pop()
 return a
E=[F(0),F(1)];z=[F(-3),F(1)];e=[F(6),F(1)];z2=pw(z,2);e2=pw(e,2)
c22=add(z2,[F(-45)]);c20=add(scale(add([F(-27)],neg(z2)),9),mul(e2,add([F(27)],neg(z2))));c02=add(scale(add([F(27)],neg(z2)),36),mul(e2,add([F(-27)],neg(z2))));c00=add(add(mul(z2,pw(e,4)),mul(mul(e2,z2),add(z2,[F(-45)]))),scale(z2,324))
def kval(X,Y):return trim(add(add(add(add(scale(pw(X,4),9),mul(c22,mul(pw(X,2),pw(Y,2)))),scale(pw(Y,4),36)),mul(c20,pw(X,2))),add(mul(c02,pw(Y,2)),c00)))
A=kval(E,[F(3),F(1)]);B=kval(E,[F(3)]);va=next(i for i,x in enumerate(A) if x);vb=next(i for i,x in enumerate(B) if x)
out={'schema':'marici.benincasa.cosmology-rees-double-cover-flag-valuations.v1','K_on_q1_q2_flag':[str(x) for x in A],'K_on_q23_q2_flag':[str(x) for x in B],'K_valuations':{'flag_A':va,'flag_B':vb},'leading_coefficients':{'flag_A':str(A[va]),'flag_B':str(B[vb])},'w_valuations':{'flag_A':f'{va}/2','flag_B':f'{vb}/2'},'passed':True};(R/'cosmology_rees_double_cover_flag_valuations.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
