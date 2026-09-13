#!/usr/bin/env python3
"""Exact Green-energy lift on arbitrary allowed interior support sets."""
import json, random
from fractions import Fraction
from pathlib import Path

def inv(A):
 n=len(A);M=[r[:]+[Fraction(i==j) for j in range(n)] for i,r in enumerate(A)]
 for j in range(n):
  p=next(i for i in range(j,n) if M[i][j]);M[j],M[p]=M[p],M[j];q=M[j][j];M[j]=[x/q for x in M[j]]
  for i in range(n):
   if i!=j:
    q=M[i][j];M[i]=[x-q*y for x,y in zip(M[i],M[j])]
 return [r[n:] for r in M]
def mv(A,v):return [sum(a*x for a,x in zip(r,v)) for r in A]
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def tr(A):return [list(x) for x in zip(*A)]
def main():
 rng=random.Random(20261004);rho=Fraction(3,5);n=15;K=[[rho**abs(i-j) for j in range(n)] for i in range(n)];cases=[]
 for _ in range(100):
  S=sorted(rng.sample(range(1,n-1),rng.randrange(2,n-2)));KS=[[K[i][j] for j in S] for i in S];AS=[[K[n-1][j] for j in S],[K[0][j] for j in S]];Ki=inv(KS);R=mm(Ki,tr(AS))
  # Each Riesz representer is supported at one extreme allowed site.
  assert all(R[i][0]==0 for i in range(len(S)-1)) and all(R[i][1]==0 for i in range(1,len(S)))
  G=mm(AS,R);Gi=inv(G);d=[Fraction(rng.randrange(-7,8),rng.randrange(1,8)) for _ in range(2)];u=mv(R,mv(Gi,d));assert mv(AS,u)==d
  assert all(u[i]==0 for i in range(1,len(S)-1))
  cases.append({'allowed_sites':S,'lift_support':[S[0],S[-1]]})
 result={'schema':'marici.coherence.constrained-green-anomaly-lift.v1','cases':len(cases),'all_exact':True,'constraint':'endpoint sites forbidden; arbitrary allowed interior subset S','lift_support':'min(S) and max(S) only','principle':'Green minimum energy moves anomaly to the boundary of the allowed region','cases_detail':cases}
 Path(__file__).with_name('constrained-green-anomaly-lift.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ('cases','all_exact','constraint','lift_support','principle')},indent=2))
if __name__=='__main__':main()
