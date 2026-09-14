#!/usr/bin/env python3
"""Discriminant obstruction to identifying the conductor A2 with pyramid A1^2."""
import json
from fractions import Fraction
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[3]
A2=s.Matrix([[-2,1],[1,-2]]);P=-2*s.eye(2)
dA=abs(int(A2.det()));dP=abs(int(P.det()));ratio=s.Rational(dA,dP)
# A rational isometry M would force det(M)^2=det(A2)/det(P)=3/4.
num,den=s.fraction(ratio)
def square(n):return int(s.integer_nthroot(int(n),2)[0])**2==int(n)
checks={'A2_discriminant_three':dA==3,'pyramid_discriminant_four':dP==4,'no_integral_isometry':dA!=dP,'determinant_ratio':ratio==s.Rational(3,4),'ratio_not_rational_square':not(square(num) and square(den))}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.A2-pyramid-return-no-go.v1','passed':True,'conductor_Gram':A2.tolist(),'pyramid_complement_Gram':[[int(P[i,j]) for j in range(2)] for i in range(2)],'absolute_discriminants':{'A2':dA,'A1_squared':dP},'determinant_square_ratio':str(ratio),'integral_isometry':False,'rational_isometry':False,'decision':'the primitive E1-E2 conductor incidence cannot label the pyramid sum/difference kernel without an explicit non-isometric correspondence','checks':checks}
# convert A2 list
out['conductor_Gram']=[[int(A2[i,j]) for j in range(2)] for i in range(2)]
p=ROOT/'research/voevodsky/results/A2_pyramid_return_no_go.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'discriminants':[dA,dP],'rational_isometry':False}))
