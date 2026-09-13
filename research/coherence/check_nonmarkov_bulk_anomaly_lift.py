#!/usr/bin/env python3
"""Compare constrained anomaly lifts for Markov and non-Markov kernels."""
import json
from fractions import Fraction
from pathlib import Path
import check_constrained_green_anomaly_lift as lin

def kernel(n,rho,power):return [[rho**(abs(i-j) if power==1 else (i-j)**2) for j in range(n)] for i in range(n)]
def lift(K,S,d):
 n=len(K);KS=[[K[i][j] for j in S] for i in S];A=[[K[n-1][j] for j in S],[K[0][j] for j in S]];R=lin.mm(lin.inv(KS),lin.tr(A));G=lin.mm(A,R);return lin.mv(R,lin.mv(lin.inv(G),d)),R
def main():
 n=9;S=list(range(1,n-1));rho=Fraction(1,2);d=[Fraction(1),Fraction(0)]
 markov,Rm=lift(kernel(n,rho,1),S,d);gaussian,Rg=lift(kernel(n,rho,2),S,d)
 markov_support=[S[i] for i,x in enumerate(markov) if x];gaussian_support=[S[i] for i,x in enumerate(gaussian) if x]
 assert markov_support==[S[0],S[-1]] and gaussian_support==S
 assert all(Rm[i][0]==0 for i in range(len(S)-1)) and all(Rm[i][1]==0 for i in range(1,len(S)))
 assert sum(any(Rg[i][j] for j in range(2)) for i in range(len(S)))==len(S)
 result={'schema':'marici.coherence.nonmarkov-bulk-anomaly-lift.v1','contexts':n,'allowed_sites':S,'rho':str(rho),'boundary_target':['1','0'],'markov_kernel':'rho^abs(i-j)','markov_lift_support':markov_support,'nonmarkov_kernel':'rho^((i-j)^2)','nonmarkov_lift_support':gaussian_support,'nonmarkov_coefficients':[str(x) for x in gaussian],'conclusion':'boundary localization is a Markov-kernel theorem; a non-Markov positive kernel generically spreads the minimum-energy lift through the bulk'}
 Path(__file__).with_name('nonmarkov-bulk-anomaly-lift.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
