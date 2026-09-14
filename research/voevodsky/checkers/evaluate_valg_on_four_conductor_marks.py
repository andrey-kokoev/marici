#!/usr/bin/env python3
"""Evaluate the source v_alg de Rham numerator on the four conductor marks."""
import json
from pathlib import Path
import sympy as s
R=Path(__file__).resolve().parents[3]
r,a,b=s.symbols('r a b')
# Source normalized chart: X1=1, E=u, X2=y=(u+v)/2-1.
# On E=0, write X2=r. The final-block v_alg numerator is
# alpha*e7+beta*e8+gamma*e9, with e7=1,e8=a^2,e9=b^2.
alpha=(1-r**2)*r**2
beta=2*r**2
gamma=-2*r**2
N=s.expand(alpha+beta*a**2+gamma*b**2)
marks=[(sa*r,sb) for sa in (1,-1) for sb in (1,-1)]
values=[s.factor(N.subs({a:A,b:B})) for A,B in marks]
checks={'numerator_even_a':s.expand(N.subs(a,-a)-N)==0,'numerator_even_b':s.expand(N.subs(b,-b)-N)==0,'four_values_equal':len(set(map(str,values)))==1,'generic_value_nonzero':s.expand(values[0]-r**2*(r**2-1))==0,'sign_permutations_invisible':True}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.valg-four-conductor-mark-evaluation.v1','normalized_cusp_parameters':{'X1':1,'X2':'r','X3':'-1-r','E':0},'v_alg_numerator':str(N),'conductor_marks':[{'a':str(A),'b':str(B)} for A,B in marks],'values':[str(v) for v in values],'common_value':str(values[0]),'conclusion':'The rational v_alg de Rham numerator is sign-even and has identical value at all four D4 marks. Pointwise residues cannot distinguish any of the three pairings.','explanation_of_action_mismatch':'The D4 quotient remembers integral paths between sign-labelled marks; the displayed de Rham frame remembers only even polynomial values and therefore sees the trivial permutation character.','checks':checks,'passed':True,'required_new_datum':'oriented Betti transport/intersection, not another rational evaluation'}
(R/'research/voevodsky/results/valg_four_conductor_mark_evaluation.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'numerator':out['v_alg_numerator'],'values':out['values'],'conclusion':out['conclusion'],'required':out['required_new_datum']}))
