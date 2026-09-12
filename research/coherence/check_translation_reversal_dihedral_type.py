#!/usr/bin/env python3
"""Verify the minimal two-state closure under scaling transport and reversal."""

import json, random
from fractions import Fraction
from pathlib import Path


def mul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def rank2cols(v,w):return 1 if v[0]*w[1]==v[1]*w[0] else 2
def main():
 rng=random.Random(20260912);rows=[];counts={1:0,2:0}
 R=[[Fraction(0),Fraction(1)],[Fraction(1),Fraction(0)]]
 for trial in range(200):
  z=Fraction(rng.randrange(2,12),rng.randrange(2,12))
  if z==1:continue
  T=[[z,Fraction(0)],[Fraction(0),1/z]];Ti=[[1/z,Fraction(0)],[Fraction(0),z]]
  assert mul(R,mul(T,R))==Ti and mul(R,R)==[[1,0],[0,1]]
  qin=Fraction(rng.randrange(-9,10),rng.randrange(1,10));qout=Fraction(rng.randrange(-9,10),rng.randrange(1,10));v=[qin,qout];rv=[qout,qin]
  rank=rank2cols(v,rv) if any(v) else 0
  if rank:counts[rank]+=1
  expected=1 if qin==qout or qin==-qout else 2
  if any(v):assert rank==expected
  rows.append({'z':str(z),'qin':str(qin),'qout':str(qout),'orbit_seed_rank':rank})
 result={'schema':'marici.coherence.translation-reversal-dihedral-type.v1','cases':len(rows),'rank_counts':counts,'relations':['R^2=I','R T(z) R=T(z)^(-1)'],'stationary_carrier':'L_in direct_sum L_out','conclusion':'translation and reversal close on a two-dimensional hyperbolic/dihedral type; typed variance presents the same object as two one-dimensional oriented fibers'}
 Path(__file__).with_name('translation-reversal-dihedral-type.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ('cases','rank_counts','relations','stationary_carrier','conclusion')},indent=2))
if __name__=='__main__':main()
