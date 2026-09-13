#!/usr/bin/env python3
"""Measure first-order bulk leakage from a nonlocal metric perturbation."""
import json
from fractions import Fraction
from pathlib import Path
import check_constrained_green_anomaly_lift as lin

def kernel(n,rho,p):return [[rho**(abs(i-j) if p==1 else (i-j)**2) for j in range(n)] for i in range(n)]
def main():
 n=9;S=list(range(1,n-1));rho=Fraction(1,2);K=kernel(n,rho,1);G=kernel(n,rho,2);A=[[K[-1][j] for j in S],[K[0][j] for j in S]];d=[Fraction(1),Fraction(0)];rows=[]
 for power in range(1,7):
  eps=Fraction(1,10**power);W=[[K[i][j]+eps*G[i][j] for j in S] for i in S];Wi=lin.inv(W);R=lin.mm(Wi,lin.tr(A));u=lin.mv(R,lin.mv(lin.inv(lin.mm(A,R)),d));assert lin.mv(A,u)==d
  bulk=u[1:-1];mx=max(abs(x) for x in bulk);assert mx>0
  rows.append({'epsilon':str(eps),'max_strict_bulk_coefficient':float(mx),'bulk_over_epsilon':float(mx/eps),'all_strict_bulk_nonzero':all(x!=0 for x in bulk)})
 ratios=[r['bulk_over_epsilon'] for r in rows]
 assert max(ratios[-3:])/min(ratios[-3:])<1.01
 result={'schema':'marici.coherence.small-nonlocal-metric-perturbation.v1','contexts':n,'allowed_sites':S,'metric':'Markov K + epsilon squared-exponential G','rows':rows,'exact_localization_survives_for_epsilon_nonzero':False,'first_order_leakage':True,'conclusion':'arbitrarily small nonlocal metric coupling populates the entire admissible bulk, with coefficients linear in epsilon to first order'}
 Path(__file__).with_name('small-nonlocal-metric-perturbation.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
