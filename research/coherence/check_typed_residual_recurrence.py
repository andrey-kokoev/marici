#!/usr/bin/env python3
"""Verify that an odd block retypes to two boundary charges closed under sewing."""

import json, random
from fractions import Fraction
from pathlib import Path


def pf(A):
 n=len(A)
 if n==0:return Fraction(1)
 return sum((1 if j%2 else -1)*A[0][j]*pf([[A[r][c] for c in range(n) if c not in (0,j)] for r in range(n) if r not in (0,j)]) for j in range(1,n))
def matrix(y):
 n=len(y);A=[[Fraction(0) for _ in range(n)] for _ in range(n)]
 for i in range(n):
  for j in range(i+1,n):A[i][j]=y[j]/y[i];A[j][i]=-A[i][j]
 return A
def cof(A):return [(-1 if i%2 else 1)*pf([[A[r][c] for c in range(len(A)) if c!=i] for r in range(len(A)) if r!=i]) for i in range(len(A))]
def typed(y):
 u=cof(matrix(y));return u,sum(u[i]/y[i] for i in range(len(y))),sum(u[i]*y[i] for i in range(len(y)))
def main():
 rng=random.Random(20260912);rows=[]
 for ln,rn in ((1,1),(1,3),(3,1),(3,3),(3,5),(5,3),(5,5),(5,7)):
  for trial in range(12):
   gaps=[Fraction(rng.randrange(1,9),rng.randrange(9,18)) for _ in range(ln+rn-1)];y=[Fraction(1)]
   for g in gaps:y.append(y[-1]*g)
   yl,yr=y[:ln],y[ln:];ul,out_l,in_l=typed(yl);ur,out_r,in_r=typed(yr)
   B=[[yr[j]/yl[i] for j in range(rn)] for i in range(ln)]
   direct=sum(ul[i]*B[i][j]*ur[j] for i in range(ln) for j in range(rn));retyped=out_l*in_r
   assert direct==retyped==pf(matrix(y))
   rows.append({'left_size':ln,'right_size':rn,'trial':trial,'typed_pairing_exact':True})
 result={'schema':'marici.coherence.typed-residual-recurrence.v1','cases':len(rows),'all_typed_pairings_exact':True,'residual_type':'(null line, outgoing charge sum u_i/y_i, incoming charge sum u_i y_i, parity, orientation)','sewing':'outgoing(left)*incoming(right)','rows':rows}
 Path(__file__).with_name('typed-residual-recurrence.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ('cases','all_typed_pairings_exact','residual_type','sewing')},indent=2))
if __name__=='__main__':main()
