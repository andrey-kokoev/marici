"""Compare cubic label3 zeros against bosonic poles at two internal E_B support walls."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_label3_EB_positive_overlap_chamber as chamber
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
trace=chamber.trace;D,vars=trace.D,trace.vars
w2,w4,w5,w6,w7,w8,t,u=vars
e=chamber.e
EB=chamber.EB
point={v:chamber.parse(EB['inverse_source_parameters'][str(v)]) for v in vars}
cell=trace.bir.square.source['E_B'];z=chamber.z;h=chamber.h
J=s.factor(s.Matrix.hstack(*[s.Matrix(list(cell.diff(v).subs(point)*z)) for v in vars]).det(method='domain-ge'))
A=s.factor((cell.subs(point)*h).det())
other=s.factor(point[w5]*point[w6]*point[w7]*point[w8]*point[u]*(point[t]-point[u]))
assert J!=0 and A!=0
assert s.factor(s.det(cell[:,[0,3]])-w4)==0
assert s.factor(s.det(cell[:,[1,2]])-w2)==0
bosonic=s.factor(-A**4/(point[w2]*point[w4]*other*J))
fermionic=s.factor(bosonic*(point[w2]*point[w4])**4)
def order_at(expr,root):
 num,den=s.fraction(s.factor(expr))
 line=s.Poly(e-root,e)
 def count(poly):
  poly=s.Poly(poly,e);degree=0
  while poly.rem(line)==0:
   poly=poly.quo(line);degree+=1
  return degree
 return count(num)-count(den)
checks=[]
for label,root,source_pole in [('lower_w2',chamber.threshold_low,'w2'),
                                ('upper_w4',chamber.threshold_high,'w4')]:
 assert J.subs(e,root)!=0 and A.subs(e,root)!=0 and other.subs(e,root)!=0
 assert order_at(bosonic,root)==-1
 assert order_at(fermionic,root)==3
 surviving_pair_component=s.factor(bosonic*(point[w4] if label=='lower_w2' else point[w2])**4)
 assert order_at(surviving_pair_component,root)==-1
 assert chamber.J_E.subs(e,root)!=0
 checks.append({'wall':label,'E_positive_e':str(root),
  'EB_source_facet':source_pole+'=0',
  'E_and_EB_target_jacobians_nonzero':True,
  'EB_target_frame_and_other_source_factors_nonzero':True,
  'EB_bosonic_target_form_order':-1,
  'EB_chi3_power4_chi5_power4_target_component_order':3,
  'surviving_fermionic_pole_component':('chi1^4 chi5^4' if label=='lower_w2' else 'chi3^4 chi4^4'),
  'surviving_fermionic_component_order':-1})
report={'schema':'marici.nima.nine-point-EB-internal-support-walls-fermionic-vanishing.v1',
 'passed':True,'E_B_target_Jacobian_on_E_family':str(J),
 'E_B_target_frame_determinant':str(A),
 'E_B_oriented_bosonic_coefficient':str(bosonic),
 'E_B_chi3_power4_chi5_power4_coefficient':str(fermionic),
 'exact_positive_internal_walls':checks,
 'consequence':'Both E_B support-wall images lie inside regular strictly positive E image. At each, E_B has a genuine simple pole in a SUPERFORM component: chi1^4 chi5^4 at the lower w2 wall and chi1^4 chi3^4 at the upper w4 wall. Its distinguished chi3^4 chi5^4 component instead has a CUBIC zero at each, because det(C3,C5)^4=(w2*w4)^4 kills the source logarithmic pole. Additional cell contributions are necessary if the global form must be regular at these internal positive-image loci.',
 'scope':'Exact first-pivot moment-curve target family, only E_B versus E local forms. Other fermionic coefficients and cells remain unresolved.'}
(OUT/'nine-point-EB-internal-support-walls-fermionic-vanishing.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'internal_walls':checks},indent=2))
