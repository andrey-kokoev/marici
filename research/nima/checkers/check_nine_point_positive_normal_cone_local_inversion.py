"""Certify B,D normal cones each locally invertible, yet disjoint over two positive face targets."""
import contextlib,io,json,itertools
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_slope_face_exact_fibre_normal_match as prior
 import check_nine_point_positive_slope_face_normal_cones as separation
 import check_nine_point_four_mass_loop_embedding as loop
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
A,vars=loop.D,loop.variables
w2,w4,w5,w6,w7,w8,t,u=vars
B=A.copy();B[0,3]=-w4/t
D=B.copy();D[1,5]=w6*u
external=loop.Z8six*loop.Z8six[:6,:].inv()
points=[('first',('1','1','1','1','1','1','2','2'),s.Rational(-14,55),s.Rational(7,11)),
        ('second',('2','3','3','2','1','4','3','3'),s.Rational(-1213,645),s.oo)]
lam=s.symbols('lambda',real=True);checks=[]
for idx,(name,raw,lower,upper) in enumerate(points):
 p=dict(zip(vars,[s.Rational(q) for q in raw]));Y=B.subs(p)*external
 fixed=next(pair for pair in itertools.combinations(range(6),2) if Y[:,list(pair)].det()!=0)
 free=tuple(i for i in range(6) if i not in fixed)
 def jac(cell,point):
  Y0=cell.subs(point)*external;H=Y0[:,list(fixed)];target=H.inv()*Y0[:,list(free)]
  cols=[]
  for var in vars:
   delta=cell.diff(var).subs(point)*external
   cols.append(s.Matrix(list(H.inv()*(delta[:,list(free)]-delta[:,list(fixed)]*target))))
  return s.Matrix.hstack(*cols)
 J=jac(B,p)
 tangent=s.Matrix.hstack(*(J[:,i] for i in (0,2,3,4,5)),J[:,6]+J[:,7]);assert tangent.rank()==6
 L=s.Matrix.vstack(*(z.T for z in tangent.T.nullspace()))
 r=[s.Rational(z) for z in prior.checks[idx]['source_fibre_direction']]
 q={var:p[var]+lam*r[i] for i,var in enumerate(vars)}
 cell_results={}
 for label,cell in [('B',B),('D',D)]:
  n=s.simplify(L*jac(cell,q)[:,6])
  radial=s.factor(s.det(s.Matrix.hstack(n,n.diff(lam))))
  assert radial!=0
  numer,denom=s.fraction(radial)
  real_roots=[z for z in s.solve(numer,lam) if z.is_real]
  assert all(not(lower<z<upper) for z in real_roots)
  midpoint=(lower+upper)/2 if upper!=s.oo else s.S.Zero
  sign=s.sign(radial.subs(lam,midpoint));assert sign in (s.S.One,-s.S.One)
  # Exact normal leading map eta=v*n(lambda) has Jacobian
  # det(d eta / d(v,lambda))=v*det(n,n'). Thus for positive v,
  # each source cone is locally an open target wedge whenever radial!=0.
  cell_results[label]={'n_components':[str(s.factor(z)) for z in n],
   'det_n_nprime':str(radial),'sign_on_entire_positive_fibre':int(sign),
   'zero_of_normal_jacobian_inside_positive_interval':False}
 assert separation.checks[idx]['nonparallel_for_every_pair_of_positive_face_preimages']
 checks.append({'point':name,'positive_fibre_interval':[str(lower),str(upper)],
  'normal_families_disjoint_in_common_target_quotient':True,
  'each_normal_cone_has_regular_two_dimensional_interior':True,
  'cell_normal_inversion':cell_results})
report={'schema':'marici.nima.nine-point-positive-normal-cone-local-inversion.v1','passed':True,
 'exact_face_targets':checks,
 'consequence':'At two tested positive target planes, B and D have disjoint positive first-order target-normal ray families; each family has a nonvanishing radial derivative over its entire positive fibre, so each cell supplies a locally invertible two-dimensional normal cone sector in its leading blow-down model. A B-sector normal ray cannot receive a competing D source from this same face fibre in a sufficiently small regular neighborhood.',
 'scope':'First-order local cone statement near two target planes only. Does not exclude other positive cells, other preimages, or evaluate actual singular pushed eight-form residues/canonical form.'}
(OUT/'nine-point-positive-normal-cone-local-inversion.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'positive_target_planes':len(checks),
 'each_normal_cone_locally_invertible':True,'B_D_positive_normal_cones_disjoint':True},indent=2))
