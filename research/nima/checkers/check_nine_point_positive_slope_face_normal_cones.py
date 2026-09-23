"""Compare entire positive B,D slope-face target-normal ray families at two exact targets."""
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
D=B.copy();D[1,5]=w6*u
external=loop.Z8six*loop.Z8six[:6,:].inv()
points=[('first',('1','1','1','1','1','1','2','2'),s.Rational(-14,55),s.Rational(7,11)),
        ('second',('2','3','3','2','1','4','3','3'),s.Rational(-1213,645),s.oo)]
lambda_B,lambda_D=s.symbols('lambda_B lambda_D',real=True)
checks=[]
for name,raw,lower,upper in points:
 p=dict(zip(vars,[s.Rational(z) for z in raw]));Y=B.subs(p)*external
 fixed=next(pair for pair in itertools.combinations(range(6),2) if Y[:,list(pair)].det()!=0)
 free=tuple(j for j in range(6) if j not in fixed)
 def jac(cell,point):
  Y0=cell.subs(point)*external;H=Y0[:,list(fixed)];target=H.inv()*Y0[:,list(free)]
  cols=[]
  for variable in vars:
   delta=cell.diff(variable).subs(point)*external
   cols.append(s.Matrix(list(H.inv()*(delta[:,list(free)]-delta[:,list(fixed)]*target))))
  return s.Matrix.hstack(*cols)
 J0=jac(B,p);r=s.Matrix([s.Rational(z) for z in prior.checks[len(checks)]['source_fibre_direction']])
 assert J0*r==s.zeros(8,1)
 tangent=s.Matrix.hstack(*(J0[:,j] for j in (0,2,3,4,5)),J0[:,6]+J0[:,7]);assert tangent.rank()==6
 L=s.Matrix.vstack(*(null.T for null in tangent.T.nullspace()))
 pB={v:p[v]+lambda_B*r[i] for i,v in enumerate(vars)}
 pD={v:p[v]+lambda_D*r[i] for i,v in enumerate(vars)}
 nB=s.simplify(L*jac(B,pB)[:,6]);nD=s.simplify(L*jac(D,pD)[:,6])
 wedge=s.factor(s.det(s.Matrix.hstack(nB,nD)))
 numerator,denominator=s.fraction(wedge)
 assert s.Poly(numerator,lambda_B,lambda_D).total_degree()<=2
 # Exhibit a strictly positive polynomial after shifting BOTH fibre
 # variables to their exact positivity lower bounds. No finite sampling
 # is used to infer the uniform nonintersection statement.
 x,y=s.symbols('x y',positive=True)
 shifted=s.Poly(s.expand((-numerator).subs({lambda_B:lower+x,
                                            lambda_D:lower+y})),x,y)
 assert all(coefficient>0 for coefficient in shifted.coeffs()),shifted
 assert shifted.coeff_monomial(1)>0
 eq=s.solve(numerator,lambda_D)
 samples=[]
 for z in (s.S.Zero,(lower+upper)/2 if upper!=s.oo else s.S.One,
           (lower+upper)/3 if upper!=s.oo else s.S(3)):
  if not lower<z<upper:continue
  matches=[s.factor(m.subs(lambda_B,z)) for m in eq]
  samples.append({'B_fibre_lambda':str(z),'D_parallelism_lambdas':[str(m) for m in matches],
                  'D_match_inside_positive_interval':[bool(lower<m<upper) for m in matches]})
 checks.append({'point':name,'positive_lambda_interval':[str(lower),str(upper)],
  'wedge_numerator':str(s.factor(numerator)),'wedge_denominator':str(s.factor(denominator)),
  'strictly_positive_shifted_negative_numerator':str(shifted.as_expr()),
  'nonparallel_for_every_pair_of_positive_face_preimages':True,
  'D_parallelism_solution':[str(e) for e in eq],
  'exact_B_fibre_samples':samples})
report={'schema':'marici.nima.nine-point-positive-slope-face-normal-cones.v1',
 'passed':True,'controls':checks,
 'scope':'An exact polynomial-positive certificate proves the B/D transverse target-normal rays never coincide for ANY pair of positive face preimages over EACH of these two fixed target planes. This excludes first-order B/D normal pairing only at those targets, not other cells, other targets, nonlinear images, surviving poles or full n9 form.'}
(OUT/'nine-point-positive-slope-face-normal-cones.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'controls':[{'point':x['point'],'wedge':x['wedge_numerator'],
 'samples':x['exact_B_fibre_samples']} for x in checks]},indent=2))
