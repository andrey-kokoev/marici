#!/usr/bin/env python3
"""Exact audit of the universal double cover of a real Schwarz square."""
import json
from fractions import Fraction
from pathlib import Path

def case(a,b,c):
 C=a+c;D=a*c-b*b;Delta=C*C-4*D
 # Delta=(a-c)^2+4b^2; rational-square fixtures chosen below.
 y=Fraction(int(Delta.numerator**0.5),int(Delta.denominator**0.5));assert y*y==Delta
 xp=(C+y)/2;xm=(C-y)/2
 assert xp+xm==C and xp*xm==D
 return {'a':str(a),'b':str(b),'c':str(c),'trace_C13':str(C),'determinant':str(D),'discriminant':str(Delta),'cover_coordinate_y':str(y),'X13':str(xp),'X24':str(xm),'deck_exchange':'y -> -y swaps X13 and X24','both_channels_positive':xp>=0 and xm>=0}
def main():
 rows=[case(Fraction(2),Fraction(0),Fraction(1)),case(Fraction(1),Fraction(2),Fraction(1))]
 assert rows[0]['both_channels_positive'] and not rows[1]['both_channels_positive']
 result={'schema':'marici.voevodsky.universal-Schwarz-spectral-cover.v1','cover_equation':'y^2=C13^2-4D=(a-c)^2+4|b|^2','channels':['X13=(C13+y)/2','X24=(C13-y)/2'],'deck_action':'y -> -y','incidence':['X13+X24=C13','X13*X24=D'],'rows':rows,'orientation_problem_solved':True,'positivity_forced':False,'positivity_gate':'C13>=|y|, equivalently D>=0 when C13>=0','comparison_to_existing_C13_cover':'A map from y_source^2=g(m) requires the pulled-back Schwarz discriminant to equal g(m) up to an invertible square factor.'}
 out=Path(__file__).parents[1]/'results'/'universal_Schwarz_spectral_cover.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
