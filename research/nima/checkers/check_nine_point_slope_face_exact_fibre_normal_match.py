"""Solve exact positive face fibres and first-order common-target normal-jet matching."""
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
lam=s.symbols('lambda',real=True);checks=[]
for name,raw in points:
 p=dict(zip(vars,[s.Rational(z) for z in raw]))
 Y=B.subs(p)*external
 fixed=next(pair for pair in itertools.combinations(range(6),2) if Y[:,list(pair)].det()!=0)
 free=tuple(j for j in range(6) if j not in fixed)
 def chart(cell,point):
  Y0=cell.subs(point)*external;H=Y0[:,list(fixed)]
  return H.inv()*Y0[:,list(free)]
 def jac(cell,point):
  Y0=cell.subs(point)*external;H=Y0[:,list(fixed)];target=H.inv()*Y0[:,list(free)]
  cols=[]
  for variable in vars:
   delta=cell.diff(variable).subs(point)*external
   cols.append(s.Matrix(list(H.inv()*(delta[:,list(free)]-delta[:,list(fixed)]*target))))
  return s.Matrix.hstack(*cols)
 JB=jac(B,p);r=JB.nullspace()[0]
 assert r[0]==r[6]==r[7]==0 and r[1]!=0
 q={var:p[var]+lam*r[i] for i,var in enumerate(vars)}
 assert all(s.factor(z)==0 for z in chart(B,q)-chart(B,p))
 assert all(s.factor(z)==0 for z in chart(D,q)-chart(B,p))
 tangent=s.Matrix.hstack(*(JB[:,i] for i in (0,2,3,4,5)),JB[:,6]+JB[:,7]);assert tangent.rank()==6
 L=s.Matrix.vstack(*(left.T for left in tangent.T.nullspace()))
 nB=L*JB[:,6]
 JD_q=jac(D,q)
 nD=s.simplify(L*JD_q[:,6])
 wedge=s.factor(s.det(s.Matrix.hstack(nB,nD)))
 numerator,denominator=s.fraction(wedge)
 roots=s.solve(numerator,lam)
 cert=[]
 for root in roots:
  if root.is_real is False:continue
  candidate={var:s.factor(q[var].subs(lam,root)) for var in vars}
  if any(z.has(s.I) for z in candidate.values()):continue
  positive=all(candidate[z]>0 for z in vars[:6]) and candidate[t]==candidate[u]>0
  nd=s.simplify(nD.subs(lam,root))
  scale=next((s.factor(nB[i]/nd[i]) for i in range(2) if nd[i]!=0),None)
  assert scale is not None
  assert s.simplify(nB-scale*nd)==s.zeros(2,1)
  cert.append({'lambda':str(root),'candidate_weights':[str(candidate[z]) for z in vars],
               'all_weights_positive':bool(positive),
               'positive_D_slope_gap_scale':bool(scale>0),
               'required_D_slope_gap_scale':str(scale)})
 checks.append({'point':name,'source_fibre_direction':[str(s.factor(z)) for z in r],
                'exact_constancy_of_target_along_face_fibre':True,
                'normal_jet_parallelism_numerator':str(s.factor(numerator)),
                'matching_candidates':cert})
report={'schema':'marici.nima.nine-point-slope-face-exact-fibre-normal-match.v1',
 'passed':True,'controls':checks,
 'scope':'Exact face-target fibre and first-order common-target normal-jet matching. A positive matched first-order jet, if found, does not solve nonlinear off-face inverse branches or pushed canonical forms.'}
(OUT/'nine-point-slope-face-exact-fibre-normal-match.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'controls':[{'point':z['point'],
 'candidates':z['matching_candidates']} for z in checks]},indent=2))
