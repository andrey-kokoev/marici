#!/usr/bin/env python3
"""Equal Green determinants with distinct ordered skew Pfaffian torsions."""

import json
from fractions import Fraction
from pathlib import Path

def det(A):
 M=[r[:] for r in A];d=Fraction(1)
 for j in range(len(M)):
  p=next(i for i in range(j,len(M)) if M[i][j]);
  if p!=j:M[j],M[p]=M[p],M[j];d=-d
  q=M[j][j];d*=q
  for i in range(j+1,len(M)):
   a=M[i][j]/q
   for k in range(j+1,len(M)):M[i][k]-=a*M[j][k]
 return d
def gram(rs):
 n=len(rs)+1
 def k(i,j):
  z=Fraction(1)
  for r in rs[min(i,j):max(i,j)]:z*=r
  return z
 return [[k(i,j) for j in range(n)] for i in range(n)]
def skew(rs):
 K=gram(rs);n=len(K)
 return [[Fraction(0) if i==j else (K[i][j] if i<j else -K[i][j]) for j in range(n)] for i in range(n)]
def pf4(M):return M[0][1]*M[2][3]-M[0][2]*M[1][3]+M[0][3]*M[1][2]
def main():
 A=[Fraction(1,2),Fraction(1,3),Fraction(1,4)];B=[Fraction(1,3),Fraction(1,2),Fraction(1,4)]
 KA,KB=gram(A),gram(B);MA,MB=skew(A),skew(B)
 assert det(KA)==det(KB) and pf4(MA)!=pf4(MB)
 assert det(MA)==pf4(MA)**2 and det(MB)==pf4(MB)**2
 result={'schema':'marici.coherence.green-determinant-vs-skew-pfaffian-hostile.v1','green_determinant_A':str(det(KA)),'green_determinant_B':str(det(KB)),'skew_pfaffian_A':str(pf4(MA)),'skew_pfaffian_B':str(pf4(MB)),'equal_green_determinants':True,'distinct_pfaffian_torsions':True,'conclusion':'the positive Green determinant line does not determine ordered skew Pfaffian torsion'}
 Path(__file__).with_name('green-determinant-vs-skew-pfaffian-hostile.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
