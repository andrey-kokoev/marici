#!/usr/bin/env python3
"""Verify Lorentz and Clifford structure of the stationary residual double."""

import json, random
from fractions import Fraction
from pathlib import Path

def tr(A):return [list(x) for x in zip(*A)]
def mul(A,B):return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def main():
 I=[[Fraction(1),0],[0,Fraction(1)]];H=[[0,Fraction(1)],[Fraction(1),0]];A=[[Fraction(1),0],[0,Fraction(-1)]];R=[[0,Fraction(1)],[Fraction(1),0]]
 assert mul(A,A)==I and mul(R,R)==I and [[x+y for x,y in zip(a,b)] for a,b in zip(mul(A,R),mul(R,A))]==[[0,0],[0,0]]
 rng=random.Random(20260912);cases=0
 for _ in range(200):
  z=Fraction(rng.randrange(1,20),rng.randrange(1,20));M=[[z,0],[0,1/z]]
  assert mul(tr(M),mul(H,M))==H and mul(R,mul(M,R))==[[1/z,0],[0,z]] and mul(tr(R),mul(H,R))==H;cases+=1
 result={'schema':'marici.coherence.residual-double-clifford-lorentz.v1','cases':cases,'lorentz_metric':'H=[[0,1],[1,0]]','identities':['M(z)^T H M(z)=H','R^T H R=H','A^2=R^2=I','AR+RA=0'],'classification':'the stationary incoming/outgoing double is an O(1,1) module and A,R generate Cl(1,1)'}
 Path(__file__).with_name('residual-double-clifford-lorentz.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
