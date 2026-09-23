"""Prove a rank bound along the ENTIRE slope face of B,D for arbitrary rank-six external data."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_four_mass_loop_embedding as loop
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
A,vars=loop.D,loop.variables
w2,w4,w5,w6,w7,w8,t,u=vars
B=A.copy();B[0,3]=-w4/t
D=B.copy();D[1,5]=w6*u
assert B.subs(t,u)==D.subs(t,u)
Z=s.Matrix(8,6,lambda i,j:s.Symbol(f'Z{i+1}_{j+1}'))
face=B.subs(t,u);Y=face*Z
# The five independently positive weights act through ONE 6-vector T:
# S=Y_row0=Z1+w2 Z2-T, Q=Y_row1+u Y_row0=Z4+u(Z1+w2 Z2).
T=w4*Z[3,:]/u+sum((v*Z[index,:] for v,index in
                    ((w5,4),(w6,5),(w7,6),(w8,7))),s.zeros(1,6))
S=Z[0,:]+w2*Z[1,:]-T
Q=Z[2,:]+u*(Z[0,:]+w2*Z[1,:])
assert all(s.factor(z)==0 for z in (Y[0,:]-S))
assert all(s.factor(z)==0 for z in (Y[1,:]+u*Y[0,:]-Q))
assert all(s.factor(z)==0 for z in Q.diff(w4))
assert all(s.factor(z)==0 for z in Q.diff(w5))
# Under variation of the five weights (w4,...,w8), Q stays fixed.
# The other generator S moves in 6-space, but only its class in
# k^6/span{S,Q} (dimension FOUR) changes the 2-plane. Therefore
# FIVE weight-parameter derivatives have rank <=4 for arbitrary Z.
# This gives a kernel with dt=du=dw2=0, so full Jacobian rank<=7.
external=loop.Z8six*loop.Z8six[:6,:].inv()
points=[('positive_slope_face_w4_one',('1','1','1','1','1','1','2','2')),
        ('positive_slope_face_w4_three',('2','3','3','2','1','4','3','3'))]
checks=[];eps=s.symbols('eps')
for name,raw in points:
 p=dict(zip(vars,[s.Rational(z) for z in raw]))
 assert p[w4]>0 and p[t]==p[u]>0
 shared=B.subs(p)*external
 fixed=next(pair for pair in __import__('itertools').combinations(range(6),2)
            if shared[:,list(pair)].det()!=0)
 free=tuple(j for j in range(6) if j not in fixed)
 def jac(cell,point):
  Y0=cell.subs(point)*external
  H=Y0[:,list(fixed)];target=H.inv()*Y0[:,list(free)]
  cols=[]
  for variable in vars:
   dY=cell.diff(variable).subs(point)*external
   cols.append(s.Matrix(list(H.inv()*(dY[:,list(free)]-dY[:,list(fixed)]*target))))
  return s.Matrix.hstack(*cols)
 assert B.subs(p)==D.subs(p)
 ranks={};pairings={}
 for label,cell in [('B',B),('D',D)]:
  J=jac(cell,p)
  assert J[:,1:6].rank()==4
  assert J.rank()==7
  r,l=J.nullspace()[0],J.T.nullspace()[0]
  assert r[0]==r[6]==r[7]==0 and r[1]!=0
  moving=dict(p);moving[t]=p[u]+eps
  J1=jac(cell,moving).diff(eps).subs(eps,0)
  assert jac(cell,moving).subs(eps,0)==J
  pairing=s.factor((l.T*J1*r)[0]);assert pairing!=0
  ranks[label]=7;pairings[label]=str(pairing)
 checks.append({'point':name,'source_w4':str(p[w4]),'rank':ranks,
  'five_weight_tangent_rank':4,'transverse_first_order_pairing':pairings})
report={'schema':'marici.nima.nine-point-slope-face-structural-blowdown.v1','passed':True,
 'arbitrary_Z6_identity':{
  'row0':'Z1+w2*Z2-T','row1_plus_u_row0':'Z4+u*(Z1+w2*Z2)',
  'T':'(w4/u)*Z5+w5*Z6+w6*Z7+w7*Z8+w8*Z9',
  'consequence':'Five weight deformations map into a four-dimensional quotient k^6/span(Y); full rank at most seven on the ENTIRE t=u face where span(Y) has dimension two.'},
 'exact_positive_interior_slope_face_controls':checks,
 'genericity':'The nonzero transverse first-order pairings at positive exact witnesses show a simple Jacobian determinant zero on a nonempty Zariski-open of the slope face for the tested strictly positive rank-six external configuration; by algebraic nonvanishing this persists on a nonempty open of external/source data. Rank at most seven is universal for arbitrary rank-six external data on this face.',
 'boundary':'This structural tangent-collapse theorem does not compute singular pushed-image residues, image-face multiplicities or the full nine-point canonical form.'}
(OUT/'nine-point-slope-face-structural-blowdown.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'universal_slope_face_rank_bound':7,
 'positive_w4_interior_controls':len(checks),'simple_transverse_unfolding':True},indent=2))
