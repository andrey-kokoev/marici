#!/usr/bin/env python3
"""Exact minimum-energy lift of a rank-two boundary anomaly."""
import json, random
from fractions import Fraction
from pathlib import Path

def inv2(A):
 d=A[0][0]*A[1][1]-A[0][1]*A[1][0];assert d
 return [[A[1][1]/d,-A[0][1]/d],[-A[1][0]/d,A[0][0]/d]]
def mv(A,v):return [sum(a*x for a,x in zip(r,v)) for r in A]
def main():
 rng=random.Random(20261002);rho=Fraction(3,5);cases=0
 for n in range(2,16):
  A=[[rho**(n-1-i) for i in range(n)],[rho**i for i in range(n)]]
  G=[[sum(A[r][i]*A[s][i] for i in range(n)) for s in range(2)] for r in range(2)];Gi=inv2(G)
  for _ in range(25):
   d=[Fraction(rng.randrange(-7,8),rng.randrange(1,8)) for _ in range(2)];lam=mv(Gi,d);w=[sum(A[r][i]*lam[r] for r in range(2)) for i in range(n)];assert mv(A,w)==d
   e=sum(x*x for x in w)
   if n>=3:
    # Cross product on three columns gives a boundary-invisible perturbation.
    ids=(0,n//2,n-1);cols=[[A[r][i] for i in ids] for r in range(2)];h3=[cols[0][1]*cols[1][2]-cols[0][2]*cols[1][1],cols[0][2]*cols[1][0]-cols[0][0]*cols[1][2],cols[0][0]*cols[1][1]-cols[0][1]*cols[1][0]];h=[Fraction(0)]*n
    for i,x in zip(ids,h3):h[i]=x
    assert mv(A,h)==[0,0] and sum(w[i]*h[i] for i in range(n))==0
    assert sum((w[i]+h[i])**2 for i in range(n))>=e
   cases+=1
 result={'schema':'marici.coherence.minimum-energy-boundary-anomaly-lift.v1','rho':str(rho),'cases':cases,'all_exact':True,'lift':'omega*=A^T(AA^T)^-1 boundary_anomaly','orthogonality':'minimum lift is orthogonal to the two-moment kernel','general_solution':'omega=omega*+h with h in kernel(A)','interpretation':'boundary anomaly selects one canonical global frustration only after an energy metric is chosen'}
 Path(__file__).with_name('minimum-energy-boundary-anomaly-lift.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
