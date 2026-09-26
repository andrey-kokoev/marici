"""Check oriented four-cell square at intersecting w4=0 and t-u=0 source facets."""
import contextlib,io,itertools,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_loop_canonical_residue as top
 import check_nine_point_four_mass_loop_embedding as loop
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
A,vars=loop.D,loop.variables
w2,w4,w5,w6,w7,w8,t,u=vars;v=t-u
B=A.copy();B[0,3]=-w4/t # exchange cyclic pole (45) -> (56)
C=A.copy();C[1,5]=w6*u # exchange cyclic pole (67) -> (78)
D=B.copy();D[1,5]=w6*u # simultaneous two-pole exchange
cells={'A':A,'B':B,'C':C,'D':D}
assert B.subs(w4,0)==A.subs(w4,0)
assert s.simplify(C.subs(t,u)-A.subs(t,u))==s.zeros(2,8)
assert D.subs(w4,0)==C.subs(w4,0)
assert s.simplify(D.subs(t,u)-B.subs(t,u))==s.zeros(2,8)
assert s.simplify(D.subs({w4:0,t:u})-A.subs({w4:0,t:u}))==s.zeros(2,8)
positive_counts={};slope=s.symbols('slope',positive=True)
for label,cell in cells.items():
 N9=s.Matrix.hstack(cell[:,:2],s.zeros(2,1),cell[:,2:]);positive=zero=0
 for i,j in itertools.combinations(range(9),2):
  minor=s.factor(s.det(s.Matrix.hstack(N9[:,i],N9[:,j])))
  numerator,denominator=s.fraction(s.cancel(minor.subs(t,u+slope)))
  assert all(z>=0 for z in s.Poly(numerator,w2,w4,w5,w6,w7,w8,u,slope).coeffs()),(label,i,j,minor)
  assert all(z>=0 for z in s.Poly(denominator,w2,w4,w5,w6,w7,w8,u,slope).coeffs())
  if minor==0:zero+=1
  else:positive+=1
  assert (positive,zero)!=(0,36)
 positive_counts[label]={'positive':positive,'zero':zero}
 assert (positive,zero)==((24,12) if label=='A' else (23,13)),(label,positive,zero)
# The new D cell is the simultaneous replacement (45)->(56) and
# (67)->(78). In the SAME ambient top measure, set
# h=(w4-g/w5)/t, e=t-u-k/(w6*w7). Both normal changes have a minus sign.
g,k=s.symbols('g k')
change={top.h:(w4-g/w5)/t,top.e:t-u-k/(w6*w7)}
Dtop=top.C.subs(change)
assert Dtop.subs(dict.fromkeys(top.normals[:3],0)).subs({g:0,k:0,top.f:0})==s.Matrix.hstack(D[:,:2],s.zeros(2,1),D[:,2:])
J_D=s.factor(top.J/(w5*t*w6*w7))
leading=w2*w7*w8 # (12),(23),(34),(56),(78),(89)
remaining=(w4/t)*(w5*w6*(t-u))*(-w8*u) # (45),(67),(91)
rho_D=s.factor(J_D/(leading*remaining))
assert s.factor(rho_D-top.source_density)==0
rho={'A':top.source_density,'B':-top.source_density,
     'C':-top.source_density,'D':rho_D}
assert s.factor(sum(rho.values()))==0
# At the codim-two source corner all four matrices and all numerator
# components agree; both residue orders can be evaluated exactly.
corner={w4:0,t:u};corner_coefficient={}
for label,density in rho.items():
 coefficient=s.factor((density*w4*(t-u)).subs(corner))
 corner_coefficient[label]=coefficient
assert corner_coefficient['A']==corner_coefficient['D']
assert corner_coefficient['B']==corner_coefficient['C']==-corner_coefficient['A']
assert s.factor(sum(corner_coefficient.values()))==0
# Check whether standard target charts remain regular on the corner;
# only report exact rank, not an unjustified pushed-corner cancellation.
external=loop.Z8six*loop.Z8six[:6,:].inv()
points=[('first',('1','0','1','1','1','1','2','2')),
        ('second',('2','0','3','2','1','4','3','3'))]
corner_rank=[]
for name,raw in points:
 point=dict(zip(vars,[s.Rational(z) for z in raw]))
 assert point[w4]==0 and point[t]==point[u]>0 and all(point[z]>0 for z in (w2,w5,w6,w7,w8))
 Y=A.subs(point)*external
 fixed=next(pair for pair in itertools.combinations(range(6),2) if Y[:,list(pair)].det()!=0)
 free=tuple(i for i in range(6) if i not in fixed)
 H=Y[:,list(fixed)];target=H.inv()*Y[:,list(free)]
 ranks={}
 for label,cell in cells.items():
  cols=[]
  for parameter in vars:
   dY=cell.diff(parameter).subs(point)*external
   cols.append(s.Matrix(list(H.inv()*(dY[:,list(free)]-dY[:,list(fixed)]*target))))
  jac=s.Matrix.hstack(*cols)
  ranks[label]=jac.rank()
 assert all(r>=6 for r in ranks.values())
 corner_rank.append({'point':name,'target_frame':list(fixed),'source_to_target_jacobian_ranks':ranks})
report={'schema':'marici.nima.nine-point-w4-slope-intersection-square.v1','passed':True,
 'positive_eight_cells_ordered_minors':positive_counts,
 'square':{'A_B':'w4=0','A_C':'t-u=0','B_D':'t-u=0','C_D':'w4=0'},
 'new_diagonal_cell_D_top_measure_normal_jacobian':str(J_D),
 'new_diagonal_cell_D_sixfold_source_residue':str(rho_D),
 'oriented_source_densities':{label:str(density) for label,density in rho.items()},
 'signed_common_corner_coefficients':{label:str(value) for label,value in corner_coefficient.items()},
 'corner_target_rank_controls':corner_rank,
 'scope':'An exact positive oriented source-cell square and common codimension-two corner relation. This does not prove global image coverage, exhaust corner pushforward or other intersections.'}
(OUT/'nine-point-w4-slope-intersection-square.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'four_cell_corner_signs':'A:+ B:- C:- D:+ relative to A',
 'corner_target_ranks':corner_rank},indent=2))
