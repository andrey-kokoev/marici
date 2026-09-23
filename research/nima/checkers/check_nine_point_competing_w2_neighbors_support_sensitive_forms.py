"""Distinguish supported target-normal forms for two alternative positive w2 neighbors."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_two_composite_neighbors_target_sides as sides
 import check_nine_point_loop_canonical_residue as top
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
h,k,nA,nV,nE,w=s.symbols('h k nA nV nE w',nonzero=True,real=True)
sign={'A':-1,'V':1,'E':1}
# The same oriented boundary seven-form K and the same target tangent
# chart multiply each one-dimensional source normal density sigma*K/w.
# With h=n_cell*w to first order, each MEROMORPHIC pushed germ is
# sigma*K/h. Positive cell support is h/n_cell>0, not all h.
for label in sign:
 n={'A':nA,'V':nV,'E':nE}[label]
 jac=s.diff(n*w,w)
 assert s.factor((sign[label]*k/w)/jac-sign[label]*k/h).subs(h,n*w)==0
assert sign['A']+sign['E']==0
assert sign['A']+sign['V']==0
k_source=1/(sides.w4*sides.w5*sides.w6*sides.w7*sides.w8*sides.u*(sides.t-sides.u))
assert s.factor(sides.w2*top.source_density+k_source)==0
checks=[]
for item in sides.checks:
 normals={label:s.Rational(value) for label,value in item['target_normal_quotient_scalars'].items()}
 assert normals['A']*normals['E']>0 and normals['A']*normals['V']<0
 checks.append({'point':item['point'],
  'A_E_positive_source_images_same_target_normal_half_space':True,
  'A_V_positive_source_images_opposite_target_normal_half_spaces':True,
  'A_plus_E_leading_meromorphic_density_in_common_positive_half_space':'-K/h+K/h=0',
  'A_plus_V_supported_local_model':'A alone on A-side; V alone on opposite side',
  'source_pole_orientation_signs':sign})
report={'schema':'marici.nima.nine-point-competing-w2-neighbors-support-sensitive-forms.v1',
 'passed':True,'exact_positive_boundary_controls':checks,
 'universal_one_normal_dimensional_model':'For source parameter w>0, target normal h=n_cell*w, and oriented intrinsic normal pole sigma_cell*K*dw/w, the meromorphic pushed normal germ is sigma_cell*K*dh/h. It is physically supported only for h/n_cell>0. A sign -, V/E sign +.',
 'consequence':'On the A-side, A+E has a supported leading 1/h cancellation, while A+V has ONLY A supported there and V supported on the opposite side. Both pairs have algebraically opposite meromorphic residues, but they are different target-supported local chains.',
 'scope':'First-order supported normal-form analysis near three positive regular boundary points; other inverse sheets/cells, exact nonlinear full densities and globally valid canonical contour are not selected.'}
(OUT/'nine-point-competing-w2-neighbors-support-sensitive-forms.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'exact_boundary_controls':len(checks),
 'same_side_A_E_leading_pole_cancel':True,
 'opposite_side_A_V_locally_glue':True},indent=2))
