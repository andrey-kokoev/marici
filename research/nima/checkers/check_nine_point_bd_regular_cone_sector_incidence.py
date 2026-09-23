"""Place B/D positive blow-down sectors relative to regular A/C corner normal cones."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_positive_square_corner_normal_fan as fan
 import check_nine_point_positive_normal_cone_local_inversion as cones
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
lam,x=s.symbols('ell x',positive=True)
controls=[]
for index,(fc,cn) in enumerate(zip(fan.checks,cones.checks)):
 rays=fc['corner_target_normal_rays']
 Rw=s.Matrix([s.Rational(z) for z in rays['shared_regular_w4_ray']])
 Ra=s.Matrix([s.Rational(z) for z in rays['A_and_B_slope_gap_boundary_ray']])
 Rc=s.Matrix([s.Rational(z) for z in rays['C_and_D_slope_gap_boundary_ray']])
 FA=s.Matrix.hstack(Rw,Ra);FC=s.Matrix.hstack(Rw,Rc)
 assert FA.det()!=0 and FC.det()!=0
 L=s.Rational(cn['positive_fibre_interval'][0])
 U=s.oo if cn['positive_fibre_interval'][1]=='oo' else s.Rational(cn['positive_fibre_interval'][1])
 def vector(label):
  return s.Matrix([s.sympify(z.replace('lambda','ell'),locals={'ell':lam})
                   for z in cn['cell_normal_inversion'][label]['n_components']])
 nB,nD=vector('B'),vector('D')
 assert nB.subs(lam,L)==Ra and nD.subs(lam,L)==Rc
 coeff_B=s.simplify(FA.inv()*nB.subs(lam,L+x))
 coeff_D=s.simplify(FC.inv()*nD.subs(lam,L+x))
 assert coeff_B[0].coeff(x)<0 and coeff_B[1].subs(x,0)==1
 assert coeff_D[0].coeff(x)>0 and coeff_D[1].subs(x,0)==1
 # Linear coefficients are strictly signed on the entire indicated
 # positive interval (including unbounded interval by checking slopes).
 if U!=s.oo:
  assert coeff_D[1].subs(x,U-L)>=0
 else:
  assert coeff_D[1].coeff(x)>=0
 assert coeff_D[1].subs(x,(U-L)/2 if U!=s.oo else s.S.One)>0
 controls.append({'point':fc['point'],'positive_fibre_interval':[str(L),str(U)],
  'B_ray_A_cone_coefficients_at_lambda_lower_plus_x':[str(s.factor(z)) for z in coeff_B],
  'D_ray_C_cone_coefficients_at_lambda_lower_plus_x':[str(s.factor(z)) for z in coeff_D],
  'B_cone_outside_A_regular_cone_except_shared_boundary_ray':True,
  'D_cone_inside_C_regular_cone_for_all_positive_fibre_points':True,
  'D_upper_ray_meets_shared_w4_ray':bool(U!=s.oo and coeff_D[1].subs(x,U-L)==0)})
report={'schema':'marici.nima.nine-point-bd-regular-cone-sector-incidence.v1',
 'passed':True,'exact_positive_target_controls':controls,
 'consequence':'At both tested target planes, the entire positive B normal sector is outside A regular normal cone apart from their common slope boundary ray, whereas the entire positive D normal sector lies within C regular normal cone. At the first target the D sector reaches the regular common w4 ray at its other fibre endpoint.',
 'scope':'Exact linearized sector incidence at two fixed target planes. Overlap with C does not by itself determine oriented pushed-density cancellation; other cells and global form unresolved.'}
(OUT/'nine-point-bd-regular-cone-sector-incidence.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'two_target_sectors':[{'point':q['point'],
 'B_outside_A':q['B_cone_outside_A_regular_cone_except_shared_boundary_ray'],
 'D_inside_C':q['D_cone_inside_C_regular_cone_for_all_positive_fibre_points'],
 'D_upper_meets_w4_ray':q['D_upper_ray_meets_shared_w4_ray']}
 for q in controls]},indent=2))
