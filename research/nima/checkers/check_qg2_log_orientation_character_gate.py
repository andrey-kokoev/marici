"""Character obstruction between trivial conductor line and odd log primitive."""
import json
import sympy as s
t=s.symbols('t');solution=s.solve(s.Eq(t,-t),t)
assert solution==[0]
out={'schema':'marici.nima.qg2-log-orientation-character-gate.v1','status':'nonzero_equivariant_identification_obstructed',
'conductor_character':'+1 (normalized-wall Kummer trivial)','log_primitive_character':'-1 (reflection odd)',
'intertwiner_equation':'t=-t','characteristic':'0','solutions':['t=0'],
'consequence':'matching primitive scalar normalizations does not identify the orientation lines',
'repair':'tensor the conductor line with a source-derived sign/orientation local system carried by the relative cut chain'}
open('research/nima/results/qg2-log-orientation-character-gate.json','w').write(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
