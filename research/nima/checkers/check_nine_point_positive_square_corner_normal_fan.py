"""Compute exact A/C regular corner rays and their B/D blow-down boundary rays."""
import contextlib,io,json,itertools
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_slope_face_exact_fibre_normal_match as prior
 import check_nine_point_four_mass_loop_embedding as loop
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
A,vars=loop.D,loop.variables
w2,w4,w5,w6,w7,w8,t,u=vars
B=A.copy();B[0,3]=-w4/t
C=A.copy();C[1,5]=w6*u
D=B.copy();D[1,5]=w6*u
external=loop.Z8six*loop.Z8six[:6,:].inv()
points=[('first',('1','1','1','1','1','1','2','2')),
        ('second',('2','3','3','2','1','4','3','3'))]
checks=[]
for name,raw,old in zip(('first','second'),points,prior.checks):
 _,raw=raw;p=dict(zip(vars,[s.Rational(z) for z in raw]))
 r=[s.Rational(z) for z in old['source_fibre_direction']]
 lam=-p[w4]/r[1];corner={z:p[z]+lam*r[i] for i,z in enumerate(vars)}
 Y=A.subs(corner)*external
 fixed=next(pair for pair in itertools.combinations(range(6),2) if Y[:,list(pair)].det()!=0)
 free=tuple(i for i in range(6) if i not in fixed)
 def jac(cell):
  Y0=cell.subs(corner)*external;H=Y0[:,list(fixed)];target=H.inv()*Y0[:,list(free)]
  cols=[]
  for parameter in vars:
   delta=cell.diff(parameter).subs(corner)*external
   cols.append(s.Matrix(list(H.inv()*(delta[:,list(free)]-delta[:,list(fixed)]*target))))
  return s.Matrix.hstack(*cols)
 JA,JB,JC,JD=[jac(x) for x in (A,B,C,D)]
 tangent=s.Matrix.hstack(*(JA[:,i] for i in (0,2,3,4,5)),JA[:,6]+JA[:,7]);assert tangent.rank()==6
 assert all(s.Matrix.hstack(*(J[:,i] for i in (0,2,3,4,5)),J[:,6]+J[:,7])==tangent
            for J in (JB,JC,JD))
 L=s.Matrix.vstack(*(z.T for z in tangent.T.nullspace()))
 Rw=L*JA[:,1];Ra=L*JA[:,6];Rc=L*JC[:,6]
 assert L*JC[:,1]==Rw
 assert L*JB[:,6]==Ra and L*JD[:,6]==Rc
 assert L*JB[:,1]==s.zeros(2,1) and L*JD[:,1]==s.zeros(2,1)
 detA=s.factor(s.det(s.Matrix.hstack(Rw,Ra)))
 detC=s.factor(s.det(s.Matrix.hstack(Rw,Rc)))
 detAC=s.factor(s.det(s.Matrix.hstack(Ra,Rc)))
 assert detA>0 and detC>0 and detAC<0
 interior_coeff=s.Matrix.hstack(Rw,Ra).inv()*Rc
 assert all(z>0 for z in interior_coeff)
 checks.append({'point':name,'corner_target_normal_rays':{
  'shared_regular_w4_ray':[str(s.factor(z)) for z in Rw],
  'A_and_B_slope_gap_boundary_ray':[str(s.factor(z)) for z in Ra],
  'C_and_D_slope_gap_boundary_ray':[str(s.factor(z)) for z in Rc]},
  'regular_A_target_normal_determinant':str(detA),
  'regular_C_target_normal_determinant':str(detC),
  'slope_gap_boundary_rays_wedge':str(detAC),
  'A_C_cones_on_opposite_sides_of_common_w4_ray':False,
  'C_slope_ray_positive_coordinates_inside_A_normal_cone':
   [str(s.factor(z)) for z in interior_coeff],
  'B_D_w4_normal_projected_to_zero_at_corner':True})
report={'schema':'marici.nima.nine-point-positive-square-corner-normal-fan.v1','passed':True,
 'exact_positive_corner_controls':checks,
 'meaning':'At each certified shared corner, A/C regular target normal cones have the same w4 ray, with the C slope-gap ray strictly INSIDE A cone (both positive coefficients). The B blow-down slope-gap ray equals A, and D equals C, while B/D w4 derivative is tangent to the six-dimensional corner image. These are exact linearized ray/incidence relations, not an image-form assembly.',
 'scope':'Two corners only. Whether all normal sectors, other cells and pushed forms assemble to the full positive-image canonical form remains unresolved.'}
(OUT/'nine-point-positive-square-corner-normal-fan.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'controls':[{'point':c['point'],
 'regular_normal_determinants':[c['regular_A_target_normal_determinant'],
 c['regular_C_target_normal_determinant']],
 'opposite_sides':c['A_C_cones_on_opposite_sides_of_common_w4_ray']} for c in checks]},indent=2))
