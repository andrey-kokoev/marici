#!/usr/bin/env python3
"""Exact endpoint-supported lift selected by the Green coefficient metric."""
import json, random
from fractions import Fraction
from pathlib import Path

def mv(A,v):return [sum(a*x for a,x in zip(r,v)) for r in A]
def quad(u,K,v):return sum(u[i]*sum(K[i][j]*v[j] for j in range(len(v))) for i in range(len(u)))
def main():
 rng=random.Random(20261003);rho=Fraction(3,5);cases=0
 for n in range(2,18):
  K=[[rho**abs(i-j) for j in range(n)] for i in range(n)];A=[K[-1],K[0]];r=rho**(n-1);den=1-r*r
  for _ in range(30):
   dR=Fraction(rng.randrange(-8,9),rng.randrange(1,9));dL=Fraction(rng.randrange(-8,9),rng.randrange(1,9))
   u0=(dL-r*dR)/den;uN=(dR-r*dL)/den;u=[Fraction(0)]*n;u[0]=u0;u[-1]=uN;assert mv(A,u)==[dR,dL]
   if n>=3:
    ids=(0,n//2,n-1);C=[[A[q][i] for i in ids] for q in range(2)];z=[C[0][1]*C[1][2]-C[0][2]*C[1][1],C[0][2]*C[1][0]-C[0][0]*C[1][2],C[0][0]*C[1][1]-C[0][1]*C[1][0]];h=[Fraction(0)]*n
    for i,x in zip(ids,z):h[i]=x
    assert mv(A,h)==[0,0] and quad(u,K,h)==0
    assert quad([u[i]+h[i] for i in range(n)],K,[u[i]+h[i] for i in range(n)])==quad(u,K,u)+quad(h,K,h)
   cases+=1
 result={'schema':'marici.coherence.green-energy-boundary-lift.v1','rho':str(rho),'cases':cases,'all_exact':True,'lift_support':'first and last event only','endpoint_coefficients':['u_0=(d_L-rho^(n-1)d_R)/(1-rho^(2n-2))','u_(n-1)=(d_R-rho^(n-1)d_L)/(1-rho^(2n-2))'],'orthogonality':'Green-metric lift is orthogonal to the two-moment kernel','conclusion':'the natural Green coefficient norm chooses an endpoint-supported anomaly lift, unlike the delocalized Euclidean lift'}
 Path(__file__).with_name('green-energy-boundary-lift.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
