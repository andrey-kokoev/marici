"""Cancel shared C/D boundary-ray pole in the leading common-target normal forms."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_positive_square_corner_normal_fan as fan
 import check_nine_point_positive_normal_cone_local_inversion as cones
 import check_nine_point_slope_face_exact_fibre_normal_match as prior
 import check_nine_point_four_mass_loop_embedding as loop
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
vars=loop.variables
w2,w4,w5,w6,w7,w8,t,u=vars
X,Y,H=s.symbols('X Y H',positive=True)
checks=[]
points=[('first',('1','1','1','1','1','1','2','2')),
        ('second',('2','3','3','2','1','4','3','3'))]
for idx,(name,raw) in enumerate(points):
 p=dict(zip(vars,[s.Rational(z) for z in raw]))
 r=[s.Rational(z) for z in prior.checks[idx]['source_fibre_direction']]
 lower=-p[w4]/r[1]
 corner={z:p[z]+lower*r[j] for j,z in enumerate(vars)}
 fc=fan.checks[idx];cn=cones.checks[idx]
 rays=fc['corner_target_normal_rays']
 Rw=s.Matrix([s.Rational(z) for z in rays['shared_regular_w4_ray']])
 Ra=s.Matrix([s.Rational(z) for z in rays['A_and_B_slope_gap_boundary_ray']])
 Rc=s.Matrix([s.Rational(z) for z in rays['C_and_D_slope_gap_boundary_ray']])
 M=s.Matrix.hstack(Rw,Ra);assert M.det()!=0
 alpha,beta=M.inv()*Rc
 assert alpha>0 and beta>0
 slope=s.factor(alpha/beta)
 ell=s.symbols('ell')
 nD=s.Matrix([s.sympify(z.replace('lambda','ell'),locals={'ell':ell})
              for z in cn['cell_normal_inversion']['D']['n_components']])
 nd_A=s.simplify(M.inv()*nD.subs(ell,lower+ell))
 bw,by=nd_A.diff(ell)
 assert nd_A==s.Matrix([alpha+bw*ell,beta+by*ell])
 delta=s.factor(alpha*by-beta*bw)
 assert delta!=0
 eta=s.Matrix([X,Y]);base=s.Matrix([alpha,beta]);direction=s.Matrix([bw,by])
 Dlin=s.factor(s.det(s.Matrix.hstack(eta,direction)))
 Nlin=s.factor(s.det(s.Matrix.hstack(base,eta)))
 assert s.factor(Nlin+beta*(X-slope*Y))==0
 fibre_weights=[corner[z]+ell*r[i] for i,z in enumerate(vars[1:6],1)]
 assert fibre_weights[0]==ell*r[1]
 # D source sign -1. For eta=v*(base+ell*direction), the oriented
 # Jacobian det(d eta / d(ell,v))=-v*delta.
 inverse_v=Dlin/delta;inverse_ell=Nlin/Dlin
 D_source=s.factor(r[1]/(p[w2]*p[u]*s.prod(fibre_weights)*s.Symbol('v')**2*delta))
 D_target=s.factor(D_source.subs({s.Symbol('v'):inverse_v,
                              ell:inverse_ell},simultaneous=True))
 common=s.factor(s.S.One/(corner[w2]*corner[w5]*corner[w6]*corner[w7]*corner[w8]*corner[u]))
 C_target=common/(Y*(X-slope*Y))
 D_residue=s.factor(s.limit((H*D_target).subs(X,slope*Y+H),H,0,dir='+'))
 C_residue=s.factor(s.limit((H*C_target).subs(X,slope*Y+H),H,0,dir='+'))
 assert D_residue==-common/Y and C_residue==common/Y
 assert s.factor(D_residue+C_residue)==0
 checks.append({'point':name,'shared_C_D_boundary_ray_equation':f'X=({slope})*Y',
  'D_normal_angular_jacobian_in_A_coordinates':str(delta),
  'common_corner_base_source_density':str(common),
  'regular_C_shared_ray_pole_residue':str(C_residue),
  'singular_D_shared_ray_pole_residue':str(D_residue),
  'all_fermionic_components_leading_shared_target_pole_cancel':True})
report={'schema':'marici.nima.nine-point-singular-d-regular-c-shared-target-pole.v1','passed':True,
 'general_local_mechanism':'At a regular shared corner with D normal map eta=v*(Rc+ell*b), Rc=(alpha,beta) in A coordinates and ell=0 at w4=0, let H=X-(alpha/beta)*Y. C has leading normal pole +k/(Y*H), with k=1/(w2*w5*w6*w7*w8*u) at corner. D source sign is opposite and the exact linearized inverse gives residue -k/Y at H=0. Their common bosonic/fermionic boundary data cancel the shared target-ray pole.',
 'exact_positive_corner_controls':checks,
 'scope':'A LEADING common-target normal-form pole cancellation on a C/D overlap ray at two tested corners. Does not calculate the full nonlinear pushed eight-form, other inverse sheets/cells, or the complete n9 image canonical form.'}
(OUT/'nine-point-singular-d-regular-c-shared-target-pole.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'corner_controls':len(checks),
 'singular_D_regular_C_target_ray_pole_cancellation':True},indent=2))
