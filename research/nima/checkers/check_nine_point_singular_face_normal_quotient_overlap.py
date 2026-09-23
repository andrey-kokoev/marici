"""Compute two-dimensional common TARGET normal quotient of singular B,D slope face."""
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
external=loop.Z8six*loop.Z8six[:6,:].inv()
points=[('first',('1','1','1','1','1','1','2','2')),
        ('second',('2','3','3','2','1','4','3','3'))]
eps=s.symbols('eps');checks=[]
for name,raw in points:
 p=dict(zip(vars,[s.Rational(z) for z in raw]))
 Y=B.subs(p)*external
 fixed=next(pair for pair in itertools.combinations(range(6),2) if Y[:,list(pair)].det()!=0)
 free=tuple(j for j in range(6) if j not in fixed)
 def jac(cell,point):
  Y0=cell.subs(point)*external
  H=Y0[:,list(fixed)];target=H.inv()*Y0[:,list(free)]
  cols=[]
  for variable in vars:
   delta=cell.diff(variable).subs(point)*external
   cols.append(s.Matrix(list(H.inv()*(delta[:,list(free)]-delta[:,list(fixed)]*target))))
  return s.Matrix.hstack(*cols)
 JB,JD=jac(B,p),jac(D,p)
 assert JB.rank()==JD.rank()==7
 tangent_B=s.Matrix.hstack(*(JB[:,i] for i in (0,2,3,4,5)),JB[:,6]+JB[:,7])
 tangent_D=s.Matrix.hstack(*(JD[:,i] for i in (0,2,3,4,5)),JD[:,6]+JD[:,7])
 assert tangent_B==tangent_D and tangent_B.rank()==6
 left=tangent_B.T.nullspace()
 assert len(left)==2
 L=s.Matrix.vstack(*(l.T for l in left))
 kernel=s.Matrix([*JB.nullspace()[0]])
 assert JD*kernel==s.zeros(8,1) and kernel[6]==kernel[7]==0
 normals={};slopes={}
 for label,cell,J in [('B',B,JB),('D',D,JD)]:
  moving=dict(p);moving[t]=p[u]+eps
  J1=jac(cell,moving).diff(eps).subs(eps,0)
  # Differentiate the image of a common infinitesimal collapsed weight
  # direction as the slope-gap normal opens.
  n=L*J[:,6]
  m=L*J1*kernel
  frame=s.Matrix.hstack(n,m)
  assert frame.det()!=0
  normals[label]=frame
  slopes[label]={'n':[str(s.factor(z)) for z in n],
                 'm':[str(s.factor(z)) for z in m],
                 'normal_frame_determinant':str(s.factor(frame.det()))}
 # In shared TARGET normal coordinates, express the B normal jet in
 # the D normal frame; this is NOT a complete common-target inverse map.
 bd=normals['D'].inv()*normals['B'][:,0]
 db=normals['B'].inv()*normals['D'][:,0]
 checks.append({'point':name,'common_face_target_tangent_rank':6,
  'common_collapsed_weight_kernel':True,'normal_frames':slopes,
  'B_normal_jet_in_D_frame':[str(s.factor(z)) for z in bd],
  'D_normal_jet_in_B_frame':[str(s.factor(z)) for z in db],
  'positive_B_to_D_normal_scale':bool(bd[0]>0),
  'positive_D_to_B_normal_scale':bool(db[0]>0)})
report={'schema':'marici.nima.nine-point-singular-face-normal-quotient-overlap.v1','passed':True,
 'exact_positive_face_controls':checks,
 'method':'Quotient eight target chart directions by the common rank-six slope-face tangent image; project each cell slope-gap normal jet n and first-order unfolding m of its common collapsed weight-kernel direction. Both 2x2 normal frames invert exactly.',
 'scope':'First-order target normal-plane comparison at two positive face points. The coefficients of m depend on kernel normalization, and first-order normal overlap does not solve nonlinear common-target inverse branches, positivity intervals, singular fermionic pushforward or global canonical form.'}
(OUT/'nine-point-singular-face-normal-quotient-overlap.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'normal_matching':[{'point':z['point'],
 'B_in_D':z['B_normal_jet_in_D_frame'],
 'positive_B_to_D_scale':z['positive_B_to_D_normal_scale']} for z in checks]},indent=2))
