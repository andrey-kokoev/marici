#!/usr/bin/env python3
"""Exact audit of all-rank positivity reframed as universal rung-4 Schwarz squares."""
import json
from fractions import Fraction
from pathlib import Path

def q(G,c):return sum(c[i]*G[i][j]*c[j] for i in range(len(c)) for j in range(len(c)))
def main():
 # Hermitian functional fixture: L(1)=1 and composite primitive p with L(p)=2,L(p*p)=1.
 L1=Fraction(1);Lp=Fraction(2);Lpp=Fraction(1);det=L1*Lpp-Lp*Lp;assert det<0
 # A negative arbitrary-rank Gram witness becomes one composite primitive p=sum c_j e_j.
 G=[[Fraction(1),Fraction(-3,5),Fraction(-3,5)],[Fraction(-3,5),Fraction(1),Fraction(-3,5)],[Fraction(-3,5),Fraction(-3,5),Fraction(1)]];c=[1,1,1];Lpp2=q(G,c);assert Lpp2<0
 # Regardless of L(p), L(1)L(p*p)-|L(p)|^2 is then negative.
 arbitrary_Lp=Fraction(0);det2=L1*Lpp2-arbitrary_Lp**2;assert det2<0
 result={'schema':'marici.voevodsky.universal-rung4-schwarz-reframing.v1','local_square':'[[L(1),L(p)],[L(p*) ,L(p*p)]]','local_gate':'L(1)L(p*p)-|L(p)|^2 >= 0','scalar_hostile':{'L1':str(L1),'Lp':str(Lp),'Lpp':str(Lpp),'determinant':str(det)},'rank_three_to_composite_primitive':{'coefficients':c,'L_of_p_star_p':str(Lpp2),'rung4_determinant_with_Lp_zero':str(det2)},'theorem':'For Hermitian L with L(1)>0, universal rung-4 Schwarz positivity for every admitted p implies L(p*p)>=0 for every p, hence positivity. Conversely a positive functional satisfies every Schwarz square and all matrix amplifications.','closure_requirement':'The primitive phase must admit every finite linear combination of Gaussian translate channels and survive completion. Testing only the generating translate is insufficient.','rh_bridge':'Under source identity and Gaussian density, RH is equivalent to universal rung-4 Schwarz positivity over the composite-primitive closure.'}
 out=Path(__file__).parents[1]/'results'/'universal_rung4_schwarz_reframing.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
