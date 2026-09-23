"""Invert the two B/D blow-down normal maps and derive their exact leading rational two-forms."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_positive_normal_cone_local_inversion as cone
 import check_nine_point_slope_face_exact_fibre_normal_match as prior
 import check_nine_point_four_mass_loop_embedding as loop
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
vars=loop.variables
w2,w4,w5,w6,w7,w8,t,u=vars
X,Y=s.symbols('X Y',real=True);eta=s.Matrix([X,Y]);lam,v=s.symbols('lambda v',real=True)
points=[('first',('1','1','1','1','1','1','2','2')),
        ('second',('2','3','3','2','1','4','3','3'))]
checks=[]
for idx,(name,raw) in enumerate(points):
 p=dict(zip(vars,[s.Rational(z) for z in raw]))
 r=[s.Rational(z) for z in prior.checks[idx]['source_fibre_direction']]
 fibre_weights=[p[z]+lam*r[i] for i,z in enumerate(vars[1:6],1)]
 frames=cone.checks[idx]['cell_normal_inversion']
 items={}
 for label,sign in [('B',s.S.One),('D',-s.S.One)]:
  n=s.Matrix([s.sympify(z.replace('lambda','ell'),locals={'ell':lam})
              for z in frames[label]['n_components']])
  a=n.subs(lam,0);b=n.diff(lam)
  assert n==a+lam*b
  delta=s.factor(s.det(s.Matrix.hstack(a,b)))
  assert delta==s.Rational(frames[label]['det_n_nprime']) and delta!=0
  denom_ray=s.factor(s.det(s.Matrix.hstack(eta,b)))
  numer_ray=s.factor(s.det(s.Matrix.hstack(a,eta)))
  # Inverse of eta=v*(a+lambda*b): v=D/delta, lambda=N/D.
  assert s.factor(denom_ray.subs({X:v*n[0],Y:v*n[1]})-v*delta)==0
  assert s.factor(numer_ray.subs({X:v*n[0],Y:v*n[1]})-v*lam*delta)==0
  linear_weights=[s.factor(p[z]*denom_ray+r[i]*numer_ray)
                  for i,z in enumerate(vars[1:6],1)]
  target_density=s.factor(-sign*r[1]*delta*denom_ray**3/
           (p[w2]*p[u]*s.prod(linear_weights)))
  # Source differential order base6^dlambda^dv; normal Jacobian
  # det(d eta / d(lambda,v))=-v*delta, rho_source=sign*r4/(prod*v).
  expected=s.factor(-sign*r[1]/(p[w2]*p[u]*s.prod(fibre_weights)*v**2*delta))
  assert s.factor(target_density.subs({X:v*n[0],Y:v*n[1]})-expected)==0
  trial=s.factor(expected.subs({lam:0,v:s.Rational(1,10)}));assert trial!=0
  items[label]={'normal_ray_n_lambda':[str(s.factor(z)) for z in n],
   'nonzero_normal_angular_jacobian':str(delta),
   'inverse_v':str(s.factor(denom_ray/delta)),
   'inverse_lambda':str(s.factor(numer_ray/denom_ray)),
   'leading_target_normal_rational_density':str(target_density),
   'rational_density_homogeneity':-2,
   'nonzero_sample_at_lambda_zero_v_one_tenth':str(trial)}
 checks.append({'point':name,'cell_form_models':items,
  'B_D_positive_first_order_normal_supports_disjoint':True})
report={'schema':'marici.nima.nine-point-singular-bd-leading-target-normal-forms.v1','passed':True,
 'general_formula':'For n_i(lambda)=a_i+lambda*b_i and delta_i=det(a_i,b_i), let D_i=det(eta,b_i), N_i=det(a_i,eta). The leading pushed normal two-form coefficient from source sign sigma_i (B:+1,D:-1) is -sigma_i*r4*delta_i*D_i^3/[w2*u*product_over_j(p_j*D_i+r_j*N_i)] in the common six-dimensional base/normal-chart convention; eta=v*n_i(lambda), v=D_i/delta_i, lambda=N_i/D_i.',
 'exact_positive_face_targets':checks,
 'scope':'Exact rational forms of the LEADING LINEARIZED NORMAL MAP at two target-face points, on each individual locally regular positive normal sector. A common six-dimensional corner base factor and full fermionic numerator must be restored. Does NOT calculate nonlinear pushed eight-form, other sheets/cells, or full image canonical form.'}
(OUT/'nine-point-singular-bd-leading-target-normal-forms.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'target_planes':len(checks),
 'positive_B_D_leading_sector_densities_nonzero':True,
 'normal_degree':-2},indent=2))
