#!/usr/bin/env python3
"""Compute the full framed equalizer defect for reciprocal residual transport."""

import json
from fractions import Fraction
from pathlib import Path

def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def sub(A,B):return [[A[i][j]-B[i][j] for j in range(2)] for i in range(2)]
def neg(A):return [[-x for x in row] for row in A]
def det(A):return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def rank(A):return 0 if all(x==0 for r in A for x in r) else (1 if det(A)==0 else 2)
def main():
 R=[[Fraction(0),Fraction(1)],[Fraction(1),Fraction(0)]];I=[[Fraction(1),0],[0,Fraction(1)]];rows=[]
 for z in sorted(set(Fraction(n,d) for n in range(1,10) for d in range(1,10))):
  T=[[z,0],[0,1/z]];rec=mm(R,mm(T,R));D=sub(T,rec);s=z-1/z
  assert mm(R,mm(D,R))==neg(D)
  assert mm(D,D)==[[s*s,0],[0,s*s]]
  fixed=z*z==1;assert (rank(D)==0)==fixed and (det(D)==0)==fixed
  rows.append({'z':str(z),'fixed':fixed,'defect_rank':rank(D),'defect_determinant':str(det(D))})
 result={'schema':'marici.coherence.framed-reciprocal-equalizer-defect.v1','cases':len(rows),'defect':'Delta(z)=T(z)-R T(z) R','identities':['R Delta R=-Delta','Delta^2=(z-z^-1)^2 I','det Delta=-(z-z^-1)^2'],'kernel_nonzero_exactly_on_fixed_locus':True,'positive_fixed_locus':'z=1','conclusion':'the full framed defect, not orbit equivalence, detects reciprocal fixed points'}
 Path(__file__).with_name('framed-reciprocal-equalizer-defect.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ('cases','defect','identities','kernel_nonzero_exactly_on_fixed_locus','positive_fixed_locus')},indent=2))
if __name__=='__main__':main()
