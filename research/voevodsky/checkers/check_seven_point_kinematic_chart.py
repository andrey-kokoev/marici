"""Verify six independent projective moduli, and the two-parameter slice."""
from pathlib import Path
import itertools,json
import sympy as s
root=Path(__file__).resolve().parents[1]
a,b,c,d,e,f,u,v=s.symbols('a b c d e f u v')
frame=s.Matrix([(1,t,t*t,t**3) for t in range(1,5)])
fifth=s.Matrix([[1,5,25,125]])*frame.inv();assert all(x!=0 for x in fifth)
def invariants(row):
 coords=s.Matrix([row])*frame.inv()
 return [s.factor(coords[i]*fifth[0]/(coords[0]*fifth[i])) for i in (1,2,3)]
r6=invariants((1,a,b,c));r7=invariants((1,d,e,f))
moduli=s.Matrix(r6+r7);variables=(a,b,c,d,e,f)
jac=s.factor(moduli.jacobian(variables).det());assert jac!=0
slice_values=s.Matrix(invariants((1,7,u,v)));slice_jac=slice_values.jacobian((u,v));minor=None
for indices in itertools.combinations(range(3),2):
 value=s.factor(slice_jac[list(indices),:].det())
 if value!=0:minor={'invariant_rows':indices,'determinant':str(value)};break
assert minor
report={'passed':True,'generic_twistor_rows':[[str(x) for x in row] for row in [(1,t,t*t,t**3) for t in range(1,6)]+[(1,a,b,c),(1,d,e,f)]],'projective_frame':'First five twistors fixed in general linear position. Their stabilizer in PGL(4) is trivial; remaining two projective points carry six moduli.','normalized_projective_invariants':list(map(str,moduli)),'six_modulus_jacobian':str(jac),'symbolic_surface_rank_two_minor':minor,'scope':'Nonzero symbolic Jacobians certify independent local kinematic moduli, not an amplitude identity. Generic chart valid on its regular affine/frame open.'}
(root/'results/seven-point-kinematic-chart.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':True,'generic_chart_dimension':6,'proved_surface_dimension':2}))
