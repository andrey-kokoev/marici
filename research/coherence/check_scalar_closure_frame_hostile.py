#!/usr/bin/env python3
"""Exhibit equal scalar closures separated by the retained Green metric."""

import json
from fractions import Fraction
from pathlib import Path

def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def tr(A):return [list(x) for x in zip(*A)]
def add(A,B):return [[A[i][j]+B[i][j] for j in range(2)] for i in range(2)]
def neg(A):return [[-x for x in r] for r in A]
def det(A):return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def main():
 I=[[Fraction(1),0],[0,Fraction(1)]];R=[[0,Fraction(1)],[Fraction(1),0]];H=R
 D0=[[Fraction(1),0],[0,Fraction(-1)]]
 D1=[[Fraction(5,3),Fraction(4,3)],[Fraction(-4,3),Fraction(-5,3)]]
 assert D0!=D1
 for D in (D0,D1):
  assert mm(D,D)==I and det(D)==-1 and mm(R,mm(D,R))==neg(D)
 green0=add(mm(tr(D0),H),mm(H,D0))
 green1=add(mm(tr(D1),H),mm(H,D1))
 assert green0==[[0,0],[0,0]] and green1!=green0
 result={'schema':'marici.coherence.scalar-closure-frame-hostile.v1','shared_data':['Delta^2=I','det Delta=-1','R Delta R=-Delta'],'operators_distinct':True,'canonical_defect_green_skew':True,'hostile_defect_green_skew':False,'conclusion':'central square, determinant, and reversal parity do not determine the framed defect; Green-metric typing removes this hostile'}
 Path(__file__).with_name('scalar-closure-frame-hostile.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
