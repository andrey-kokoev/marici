#!/usr/bin/env python3
"""Enumerate endpoint four-cup readouts under all 24 prime-frame orderings."""

import json, math
from collections import defaultdict, Counter
from itertools import permutations
from fractions import Fraction
from pathlib import Path

PRIMES=(2,3,5,7); TOL=1e-12; ZERO=(0,0,0,0)
def add(*signed):
 o=defaultdict(int)
 for s,e in signed:
  for k,v in e.items():o[k]+=s*v
 return {k:v for k,v in o.items() if v}
def move(x,i,s):
 y=list(x);y[i]+=s;return tuple(y)
def run(frame):
 A=tuple(math.log(p) for p in frame)
 def val(x):return sum(n*a for n,a in zip(x,A))
 def I(x):return {x:1}
 def R(i,op,x):return op(move(x,i,1))
 def S(i,op,x):return {} if val(x)<A[i]-TOL else op(move(x,i,-1))
 def K(q,p,op,x):return add((1,R(q,lambda y:S(p,op,y),x)),(-1,S(p,lambda y:R(q,op,y),x)))
 def F(i,j,op,x):return add((1,K(j,i,op,x)),(-1,K(i,j,op,x)))
 def comp(i,j,k,l,op,x):return F(i,j,lambda y:F(k,l,op,y),x)
 def anti(i,j,k,l,op,x):return add((1,comp(i,j,k,l,op,x)),(1,comp(k,l,i,j,op,x)))
 out=add((1,anti(0,1,2,3,I,ZERO)),(-1,anti(0,2,1,3,I,ZERO)),(1,anti(0,3,1,2,I,ZERO)))
 terms=[]
 for n,c in out.items():
  ratio=Fraction(1,1)
  for p,e in zip(frame,n):ratio*=Fraction(p)**e
  terms.append((n,c,ratio))
 return terms

def parity(perm):
 inv=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4));return -1 if inv%2 else 1

def main():
 rows=[]; forms=Counter()
 for frame in permutations(PRIMES):
  terms=run(frame); idx=tuple(PRIMES.index(p) for p in frame)
  signature=tuple((str(r),c) for _,c,r in terms);forms[signature]+=1
  rows.append({'frame':frame,'permutation_parity':parity(idx),'term_count':len(terms),'terms':[{'word':n,'coefficient':c,'ratio':str(r)} for n,c,r in terms]})
 result={'schema':'marici.coherence.p4-permutation-covariance.v1','ordering_count':24,'distinct_endpoint_forms':len(forms),'form_multiplicities':{str(k):v for k,v in forms.items()},'rows':rows}
 Path(__file__).with_name('p4-permutation-covariance.v1.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'ordering_count':24,'distinct_endpoint_forms':len(forms),'form_multiplicities':result['form_multiplicities']},indent=2))
if __name__=='__main__':main()
