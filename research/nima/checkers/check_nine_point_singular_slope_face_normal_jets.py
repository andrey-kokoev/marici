"""Compare first-order target jets and Jacobian determinants of B,D across collapsed slope face."""
import contextlib,io,json,itertools
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_four_mass_loop_embedding as loop
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
A,vars=loop.D,loop.variables
w2,w4,w5,w6,w7,w8,t,u=vars
B=A.copy();B[0,3]=-w4/t
D=B.copy();D[1,5]=w6*u
Z=s.Matrix(8,6,lambda i,j:s.Symbol(f'Z{i+1}_{j+1}'))
v=t-u
T=(w4/t)*Z[3,:]+w5*Z[4,:]+w6*Z[5,:]+w7*Z[6,:]+w8*Z[7,:]
Q=Z[2,:]+t*(Z[0,:]+w2*Z[1,:])
R_B=w7*Z[6,:]+w8*Z[7,:]
R_D=w6*Z[5,:]+R_B
for name,cell,R in [('B',B,R_B),('D',D,R_D)]:
 Y=cell*Z
 assert all(s.factor(q)==0 for q in Y[0,:]-(Z[0,:]+w2*Z[1,:]-T))
 assert all(s.factor(q)==0 for q in Y[1,:]+t*Y[0,:]-(Q-v*R))
assert s.simplify(D-B+s.Matrix([[0]*8,[0,0,0,0,0,w6*v,0,0]]))==s.zeros(2,8)
external=loop.Z8six*loop.Z8six[:6,:].inv()
points=[('first_positive_slope_face',('1','1','1','1','1','1','2','2')),
        ('second_positive_slope_face',('2','3','3','2','1','4','3','3'))]
controls=[];eps=s.symbols('eps')
for name,raw in points:
 p=dict(zip(vars,[s.Rational(z) for z in raw]))
 Y=B.subs(p)*external
 fixed=next(pair for pair in itertools.combinations(range(6),2) if Y[:,list(pair)].det()!=0)
 free=tuple(j for j in range(6) if j not in fixed)
 def chart(cell,point):
  Y0=cell.subs(point)*external
  H=Y0[:,list(fixed)];return H.inv()*Y0[:,list(free)]
 def jac(cell,point):
  Y0=cell.subs(point)*external;H=Y0[:,list(fixed)];target=H.inv()*Y0[:,list(free)]
  return s.Matrix.hstack(*(s.Matrix(list(H.inv()*(delta[:,list(free)]-
   delta[:,list(fixed)]*target))) for delta in
   (cell.diff(parameter).subs(point)*external for parameter in vars)))
 assert B.subs(p)==D.subs(p)
 slope_normal_B=jac(B,p)[:,6]-jac(B,p)[:,7]
 slope_normal_D=jac(D,p)[:,6]-jac(D,p)[:,7]
 # The actual path t=u+eps uses partial_t. Its first target jet differs.
 jet_B=jac(B,p)[:,6];jet_D=jac(D,p)[:,6]
 assert jet_B!=jet_D
 results={}
 for label,cell in (('B',B),('D',D)):
  J0=jac(cell,p);assert J0.rank()==7
  r,l=J0.nullspace()[0],J0.T.nullspace()[0]
  moving=dict(p);moving[t]=p[u]+eps
  J1=jac(cell,moving).diff(eps).subs(eps,0)
  alpha=None
  for row in range(8):
   if l[row]==0:continue
   for column in range(8):
    if r[column]==0:continue
    minor=J0.minor_submatrix(row,column).det(method='domain-ge')
    if minor!=0:
     alpha=s.factor((-1)**(row+column)*minor/(l[row]*r[column]))
     break
   if alpha is not None:break
  assert alpha is not None
  first=s.factor(alpha*(l.T*J1*r)[0]);assert first!=0
  results[label]={'jacobian_determinant_linear_coefficient':str(first),
                  'rank_on_face':7}
 first_B=s.Rational(results['B']['jacobian_determinant_linear_coefficient'])
 first_D=s.Rational(results['D']['jacobian_determinant_linear_coefficient'])
 ratio=s.factor(first_B/first_D)
 controls.append({'point':name,'target_frame':list(fixed),
   'normal_target_jets_differ':jet_B!=jet_D,
   'jacobian_linear_coefficients':results,'coefficient_ratio_B_over_D':str(ratio),
   'naive_same_source_parameter_leading_push_coefficients_cancel':ratio==1})
report={'schema':'marici.nima.nine-point-singular-slope-face-normal-jets.v1','passed':True,
 'arbitrary_external_target_plane_jet':{
  'first_generator':'Z1+w2*Z2-T with T=(w4/t)*Z5+w5*Z6+w6*Z7+w7*Z8+w8*Z9',
  'second_B':'Z4+t*(Z1+w2*Z2)-(t-u)*(w7*Z8+w8*Z9)',
  'second_D':'Z4+t*(Z1+w2*Z2)-(t-u)*(w6*Z7+w7*Z8+w8*Z9)',
  'difference':'D-B has lower physical-column7 entry -w6*(t-u)'},
 'exact_positive_face_controls':controls,
 'scope':'A first-order target-jet distinction and exact simple determinant coefficients are not a pushed target-form comparison at common TARGET coordinates; B,D parameter paths need not coincide off the collapsed face. Do not interpret naive coefficients alone as canonical-form poles or cancellation.'}
(OUT/'nine-point-singular-slope-face-normal-jets.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'controls':[{'point':q['point'],
 'coefficient_ratio_B_over_D':q['coefficient_ratio_B_over_D'],
 'naive_cancel':q['naive_same_source_parameter_leading_push_coefficients_cancel']}
 for q in controls]},indent=2))
