#!/usr/bin/env python3
"""Compute the exact finite symbolic endpoint readout of the log-prime four-cup."""

import json, math
from collections import defaultdict
from pathlib import Path

PRIMES=(2,3,5,7); A=tuple(math.log(p) for p in PRIMES); ZERO=(0,0,0,0); TOL=1e-12
def val(n): return sum(x*a for x,a in zip(n,A))
def move(n,i,s):
 m=list(n);m[i]+=s;return tuple(m)
def add_expr(*signed):
 out=defaultdict(int)
 for sign,e in signed:
  for k,v in e.items():out[k]+=sign*v
 return {k:v for k,v in out.items() if v}
def identity_at(x): return {x:1}
def R(i,op,x): return op(move(x,i,1))
def S(i,op,x): return {} if val(x)<A[i]-TOL else op(move(x,i,-1))
def rawK(q,p,op,x): return add_expr((1,R(q,lambda y:S(p,op,y),x)),(-1,S(p,lambda y:R(q,op,y),x)))
def F(i,j,op,x): return add_expr((1,rawK(j,i,op,x)),(-1,rawK(i,j,op,x)))
def composeF(i,j,k,l,op,x): return F(i,j,lambda y:F(k,l,op,y),x)
def anti(i,j,k,l,op,x): return add_expr((1,composeF(i,j,k,l,op,x)),(1,composeF(k,l,i,j,op,x)))
def Q(op,x): return add_expr((1,anti(0,1,2,3,op,x)),(-1,anti(0,2,1,3,op,x)),(1,anti(0,3,1,2,op,x)))
def main():
 e=Q(identity_at,ZERO)
 assert e
 assert all(val(n)>=-TOL and sum(abs(x) for x in n)<=4 for n in e)
 terms=[{'valuation_word':n,'point':val(n),'coefficient':c,'multiplicative_label':f"2^{n[0]} 3^{n[1]} 5^{n[2]} 7^{n[3]}"} for n,c in sorted(e.items(),key=lambda z:val(z[0]))]
 result={'schema':'marici.coherence.log-prime-p4-endpoint-readout.v1','formula':'rho_0(Q4)f=(Q4 f)(0)','nonzero':True,'term_count':len(terms),'all_terms_in_Gamma4_plus':True,'terms':terms}
 target=Path(__file__).with_name('log-prime-p4-endpoint-readout.v1.json');target.write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
