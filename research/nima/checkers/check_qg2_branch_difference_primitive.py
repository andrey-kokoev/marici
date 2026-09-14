"""Normalize the exact odd branch difference to the selected primitive line."""
import json
import sympy as s
A,d=s.symbols('A d',nonzero=True);B=s.symbols('B')
plus=(-B+d)/(2*A);minus=(-B-d)/(2*A);difference=s.simplify(plus-minus)
assert difference==d/A
normalized=s.simplify((A/d)*difference);assert normalized==1
out={'schema':'marici.nima.qg2-branch-difference-primitive.v1','status':'odd_branch_difference_normalized_to_selected_unit',
'branch_difference':'xi_plus-xi_minus=d/A','normalizing_unit':'A/d','normalized_value':str(normalized),
'deck_character':-1,'selected_log_generator':'gamma has primitive coordinate 1','selected_L2_generator':'v has rho0(v)=1',
'consequence':'there is a unique generator-preserving map of the three selected free rank-one lines',
'boundary':'physical descent, occurrence labels, and equality with raw physical Cech defect remain open'}
open('research/nima/results/qg2-branch-difference-primitive.json','w').write(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
