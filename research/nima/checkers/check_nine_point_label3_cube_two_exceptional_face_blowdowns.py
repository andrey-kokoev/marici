"""Certify codimension-two image blowdowns on both exceptional label3 cube slope faces."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_label3_oriented_eight_cell_cube as cube
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
vars=cube.vars;w2,w4,w5,w6,w7,w8,t,u=vars
v=s.symbols('v');lam=s.symbols('lambda',real=True)
coordinates=vars[:6]+(v,u);Z=cube.Z
checks=[]
for first,second in (('E_B','E_D'),('F_B','F_D')):
 CA=cube.E[first].subs(t,u+v) if first[0]=='E' else cube.F[first].subs(t,u+v)
 CB=cube.E[second].subs(t,u+v) if second[0]=='E' else cube.F[second].subs(t,u+v)
 for raw in [(1,1,1,1,1,1,0,2),
             (2,3,3,2,1,4,0,3)]:
  p=dict(zip(coordinates,map(s.Rational,raw)))
  assert CA.subs(p)==CB.subs(p)
  Y=CA.subs(p)*Z
  fixed=next(pair for pair in __import__('itertools').combinations(range(6),2) if Y[:,list(pair)].det()!=0)
  free=tuple(j for j in range(6) if j not in fixed)
  def chart(C,point):
   Y0=C.subs(point)*Z
   return Y0[:,list(fixed)].inv()*Y0[:,list(free)]
  B=chart(CA,p)
  H=Y[:,list(fixed)]
  def jac(C):
   return s.Matrix.hstack(*[s.Matrix(list(H.inv()*(delta[:,list(free)]-
                         delta[:,list(fixed)]*B))) for delta in
                         (C.diff(param).subs(p)*Z for param in coordinates)])
  JA,JB=jac(CA),jac(CB)
  assert JA.rank()==JB.rank()==7
  assert all(JA[:,j]==JB[:,j] for j in range(8) if j!=6)
  tangent=JA[:,[0,1,2,3,4,5,7]]
  assert tangent.rank()==6
  r=JA.nullspace()[0]
  assert r[6]==0 and JA*r==JB*r==s.zeros(8,1)
  p_lambda={variable:p[variable]+lam*r[i] for i,variable in enumerate(coordinates)}
  assert all(s.cancel(z)==0 for z in chart(CA,p_lambda)-B)
  assert all(s.cancel(z)==0 for z in chart(CB,p_lambda)-B)
  L=s.Matrix.vstack(*(x.T for x in tangent.T.nullspace()))
  assert L.shape==(2,8)
  wedge=s.factor(s.det(s.Matrix.hstack(L*JA[:,6],L*JB[:,6])))
  assert wedge!=0
  checks.append({'exceptional_edge':first+'/'+second,
                 'point_w2_w4_u':[str(p[x]) for x in (w2,w4,u)],
                 'source_to_target_ranks':[7,7],
                 'face_tangent_rank':6,'face_fibre_dimension':1,
                 'exact_face_target_constant_along_fibre_for_both_cells':True,
                 'target_normal_quotient_dimension':2,
                 'distinct_transverse_normal_rays_at_same_positive_source':True,
                 'normal_wedge':str(wedge)})
report={'schema':'marici.nima.nine-point-label3-cube-two-exceptional-face-blowdowns.v1',
 'passed':True,'positive_face_controls':checks,
 'consequence':'Both exceptional t-u faces E_B/E_D and F_B/F_D have rank-six target FACE images from seven-dimensional source faces: one exact source fibre direction is collapsed and each two-cell pair has two independent transverse target-normal directions at the same positive boundary point. The face image is codimension TWO in eight-dimensional target space, so opposite source residues cannot be interpreted as ordinary common codimension-one pushed form residues.',
 'scope':'Two exact positive boundary controls per exceptional edge; not exhaustive positive normal-cone pairing over all face fibres/targets, complete source-boundary-current cancellation or full nine-point canonical form.'}
(OUT/'nine-point-label3-cube-two-exceptional-face-blowdowns.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'exceptional_faces':2,'positive_controls':len(checks),
 'each_target_face_codimension':2},indent=2))
