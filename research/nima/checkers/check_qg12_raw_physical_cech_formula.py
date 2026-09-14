"""Define and verify the local raw qG12 physical Cech defect from source Leray frames."""
import json
import sympy as s
X1,X2,X3,v,xi,k=s.symbols('X1 X2 X3 v xi k',nonzero=True)
n12=-s.Rational(1,2)/(X1*X2);n31=-s.Rational(1,2)/(X3*X1)
transition=s.factor(n12/n31)
chart={X1:1,X2:(v-2)/2,X3:-v/2};edge=s.factor(transition.subs(chart))
raw_v=s.factor(s.diff(s.log(edge),v));v_xi=2*(xi+1)/(1-k)
raw_xi=s.factor(raw_v.subs(v,v_xi)*s.diff(v_xi,xi))
road=s.factor(1/(xi+1)-1/(xi+k))
assert transition==X3/X2
assert s.simplify(edge+v/(v-2))==0
assert s.simplify(raw_xi-road)==0
out={'schema':'marici.nima.qg12-raw-physical-cech-formula.v1','status':'local_raw_physical_Cech_defined_and_matched',
'source_definition':'dlog(n12/n31)','source_frames':{'n12':'-1/(2 X1 X2)','n31':'-1/(2 X3 X1)'},
'labelled_transition':'G31_to_G12 = X3/X2','qG12_chart_transition':'-v/(v-2)',
'qg2_coordinate':'v=2(xi+1)/(1-kappa)','raw_defect':'dlog((xi+1)/(xi+kappa))',
'road_boundary':'dlog((xi+1)/(xi+kappa))','equality':'exact rational one-form identity',
'scope':'one occurrence-labelled qG12 wall sector; no unsupported global three-cut Cech cover'}
open('research/nima/results/qg12-raw-physical-cech-formula.json','w').write(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
