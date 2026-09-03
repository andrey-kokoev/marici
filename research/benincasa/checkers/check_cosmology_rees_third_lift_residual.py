#!/usr/bin/env python3
"""Compute the exact full residual after lifts through third normal order."""
import json
from fractions import Fraction as F
from pathlib import Path
def add(*ps):
 r={}
 for p in ps:
  for k,v in p.items():r[k]=r.get(k,F(0))+v
 return {k:v for k,v in r.items() if v}
def sc(p,c):return {k:c*v for k,v in p.items() if c*v}
def mul(a,b):
 r={}
 for (i,j),u in a.items():
  for (k,l),v in b.items():r[i+k,j+l]=r.get((i+k,j+l),F(0))+u*v
 return {k:v for k,v in r.items() if v}
def der(p,z):
 r={}
 for (i,j),v in p.items():
  n=i if z==0 else j
  if n:r[(i-1,j) if z==0 else (i,j-1)]=n*v
 return r
X={(1,0):F(1)};s={(0,1):F(1)};one={(0,0):F(1)}
R=mul(mul(X,add(X,s)),add(X,{(0,0):F(-6)}));Q=mul(mul(s,s),R)
H=add(sc(mul(X,X),3),sc(mul(s,s),-6),sc(s,-36));K=mul(H,H);K0={(4,0):F(9)}
def L1(f,z):return add(mul(Q,der(f,z)),sc(mul(der(Q,z),f),-1))
def L0(f,z):return add(mul(K,L1(f,z)),sc(mul(mul(Q,der(K,z)),f),F(-1,2)))
target=sc(mul(K,Q),3)
b=sc(mul(K0,s),-3);a=mul(s,{(4,0):F(171,2),(3,0):F(-648)});c=sc(s,F(5,2))
res=add(target,sc(L1(b,1),-1),sc(L1(a,0),-1),sc(L0(c,0),-1));order=min(j for i,j in res);coef={i:v for (i,j),v in res.items() if j==order}
out={'schema':'marici.benincasa.cosmology-rees-third-lift-residual.v1','problem':'test whether explicit lifts through third normal order cancel scalar tau exactly','bold_conjecture':'the order-three lift is an exact polynomial preimage','named_rivals':['exact cancellation','a higher normal residue remains'],'risky_consequences':['the full residual polynomial must vanish','no coefficient at normal order four or higher may survive'],'strongest_falsification_attempt':{'inputs':['boundary y=-3K0s','boundary x=s((171/2)X4-648X3)','lower x=(5/2)s'],'residual_term_count':len(res),'first_nonzero_s_order':order,'first_coefficient':{str(i):str(v) for i,v in sorted(coef.items())},'exact_residual_zero':not res},'disposition':'the third-order lift is not exact; the first surviving normal coefficient is recorded exactly','surviving_scope':'tau is matched through order three only','next_test':'characterize the constrained image at the recorded next normal order and test this coefficient','passed':bool(res) and order>=4};assert out['passed'];Rout=Path(__file__).resolve().parents[1]/'results';(Rout/'cosmology_rees_third_lift_residual.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
