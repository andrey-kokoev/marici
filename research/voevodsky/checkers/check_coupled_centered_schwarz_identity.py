#!/usr/bin/env python3
"""Exact audit of the cancellation-preserving centered Schwarz identity."""
import json
from fractions import Fraction
from pathlib import Path

def q(G,c):return sum(c[i]*G[i][j]*c[j] for i in range(len(c)) for j in range(len(c)))
def main():
 # L(1)=G00; L(p)=e0^T G c; L(p*p)=c^T G c.
 G=[[Fraction(2),Fraction(1),Fraction(-1)],[Fraction(1),Fraction(3),Fraction(1,2)],[Fraction(-1),Fraction(1,2),Fraction(1)]];c=[Fraction(1),Fraction(2),Fraction(-1)]
 m=G[0][0];Lp=sum(G[0][j]*c[j] for j in range(3));Lpp=q(G,c);D=m*Lpp-Lp*Lp
 centered=c[:];centered[0]-=Lp/m
 assert sum(G[0][j]*centered[j] for j in range(3))==0
 rhs=m*q(G,centered);assert D==rhs
 # Negative hostile from earlier, centered all-ones direction remains a Schwarz failure.
 H=[[Fraction(1),Fraction(-3,5),Fraction(-3,5)],[Fraction(-3,5),Fraction(1),Fraction(-3,5)],[Fraction(-3,5),Fraction(-3,5),Fraction(1)]];v=[Fraction(1)]*3
 hm=H[0][0];hp=sum(H[0][j]*v[j] for j in range(3));hv=v[:];hv[0]-=hp/hm;hD=hm*q(H,v)-hp*hp;assert hD==hm*q(H,hv) and hD<0
 result={'schema':'marici.voevodsky.coupled-centered-schwarz-identity.v1','identity':'L(1)L(p*p)-|L(p)|^2 = L(1)L((p-L(p)/L(1))*(p-L(p)/L(1)))','centering_condition':'L(p-L(p)/L(1))=0','exact_fixture':{'determinant':str(D),'centered_square_times_mass':str(rhs)},'negative_hostile':{'centered_coefficients':[str(x) for x in hv],'determinant':str(hD)},'source_use':'Apply endpoint, gamma, and prime source terms only after forming the centered square; do not demand sectorwise Schwarz inequalities.','remaining_gate':'The fully coupled source functional is nonnegative on every square in ker L.'}
 out=Path(__file__).parents[1]/'results'/'coupled_centered_schwarz_identity.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
