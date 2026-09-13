#!/usr/bin/env python3
"""Verify the derivative of a constrained minimum-energy lift under metric perturbation."""
import json
from fractions import Fraction
from pathlib import Path
import check_constrained_green_anomaly_lift as lin

def add(A,B,s=1):return [[A[i][j]+s*B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def subvec(a,b):return [x-y for x,y in zip(a,b)]
def scalevec(a,s):return [s*x for x in a]
def lift(W,A,d):
 X=lin.inv(W);R=lin.mm(X,lin.tr(A));return lin.mv(R,lin.mv(lin.inv(lin.mm(A,R)),d))
def main():
 n=9;S=list(range(1,n-1));rho=Fraction(1,2)
 fullK=[[rho**abs(i-j) for j in range(n)] for i in range(n)];fullG=[[rho**((i-j)**2) for j in range(n)] for i in range(n)];K=[[fullK[i][j] for j in S] for i in S];G=[[fullG[i][j] for j in S] for i in S];A=[[fullK[-1][j] for j in S],[fullK[0][j] for j in S]];d=[Fraction(1),Fraction(0)];X=lin.inv(K);u0=lift(K,A,d);H=lin.mm(lin.mm(A,X),lin.tr(A));P=lin.mm(lin.mm(X,lin.tr(A)),lin.mm(lin.inv(H),A));xgu=lin.mv(X,lin.mv(G,u0));du=[-xgu[i]+lin.mv(P,xgu)[i] for i in range(len(S))]
 assert lin.mv(A,du)==[0,0]
 rows=[]
 for power in range(1,7):
  eps=Fraction(1,10**power);ue=lift(add(K,G,eps),A,d);dq=scalevec(subvec(ue,u0),1/eps);err=max(abs(x-y) for x,y in zip(dq,du));rows.append({'epsilon':str(eps),'max_derivative_error':float(err)})
 assert rows[-1]['max_derivative_error']<rows[0]['max_derivative_error']/10000
 result={'schema':'marici.coherence.first-order-nonlocal-leakage-formula.v1','formula':'u_prime=-(I-P) K^-1 G u_0','projection':'P=K^-1 A^T(A K^-1 A^T)^-1 A','boundary_derivative_zero':True,'rows':rows,'conclusion':'first-order bulk leakage is the boundary-invisible component of the nonlocal forcing K^-1 G u_0'}
 Path(__file__).with_name('first-order-nonlocal-leakage-formula.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
