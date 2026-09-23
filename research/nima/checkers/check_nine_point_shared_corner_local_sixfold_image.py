"""Verify common corner rank six and local face-to-corner quotient near two exact positive targets."""
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
C=A.copy();C[1,5]=w6*u
D=B.copy();D[1,5]=w6*u
cells={'A':A,'B':B,'C':C,'D':D}
external=loop.Z8six*loop.Z8six[:6,:].inv()
points=[('first',('1','1','1','1','1','1','2','2')),
        ('second',('2','3','3','2','1','4','3','3'))]
controls=[]
for name,raw,old in zip(('first','second'),points,prior.checks):
 _,raw=raw
 p=dict(zip(vars,[s.Rational(z) for z in raw]))
 r=[s.Rational(z) for z in old['source_fibre_direction']]
 lam=-p[w4]/r[1]
 corner={var:s.factor(p[var]+lam*r[i]) for i,var in enumerate(vars)}
 assert corner[w4]==0 and corner[t]==corner[u]>0
 assert all(corner[z]>0 for z in (w2,w5,w6,w7,w8))
 Y=A.subs(corner)*external
 fixed=next(pair for pair in itertools.combinations(range(6),2) if Y[:,list(pair)].det()!=0)
 free=tuple(j for j in range(6) if j not in fixed)
 def jac(cell,point):
  Y0=cell.subs(point)*external;H=Y0[:,list(fixed)];target=H.inv()*Y0[:,list(free)]
  cols=[]
  for variable in vars:
   delta=cell.diff(variable).subs(point)*external
   cols.append(s.Matrix(list(H.inv()*(delta[:,list(free)]-delta[:,list(fixed)]*target))))
  return s.Matrix.hstack(*cols)
 ranks={};boundary=None;full={}
 for label,cell in cells.items():
  J=jac(cell,corner)
  corner_columns=s.Matrix.hstack(*(J[:,j] for j in (0,2,3,4,5)),J[:,6]+J[:,7])
  assert corner_columns.rank()==6
  if boundary is None:boundary=corner_columns
  else:assert corner_columns==boundary
  ranks[label]=J.rank()
  full[label]=str(s.factor(J.det(method='domain-ge')))
 assert ranks=={'A':8,'B':7,'C':8,'D':7}
 # Pick one exact 6x6 target minor of the common-corner map.
 image_rows=next(rows for rows in itertools.combinations(range(8),6)
                 if boundary[list(rows),:].det()!=0)
 sixminor=s.factor(boundary[list(image_rows),:].det())
 assert sixminor!=0
 # The same target is represented by p on the B/D face and by the
 # positive-six-weight corner preimage.
 def chart(cell,point):
  Y0=cell.subs(point)*external;return Y0[:,list(fixed)].inv()*Y0[:,list(free)]
 assert chart(B,p)==chart(A,corner)==chart(C,corner)==chart(D,p)
 # B/D source face has rank6; its collapsed kernel is transverse to
 # the w4=0 corner boundary, because its w4 component is nonzero.
 for label,cell in (('B',B),('D',D)):
  J=jac(cell,corner)
  face=s.Matrix.hstack(*(J[:,j] for j in range(6)),J[:,6]+J[:,7])
  assert face.rank()==6
  kernel=face.nullspace();assert len(kernel)==1 and kernel[0][1]!=0
  assert face.columnspace() and s.Matrix.hstack(boundary,face).rank()==6
 controls.append({'point':name,'corner_source_weights':[str(corner[z]) for z in vars],
  'full_target_jacobian_ranks':ranks,'common_corner_target_rank':6,
  'nonzero_common_corner_target_six_minor':str(sixminor),
  'exact_same_target_positive_B_D_face_and_positive_corner':True,
  'collapsed_face_kernel_transverse_to_corner':True})
report={'schema':'marici.nima.nine-point-shared-corner-local-sixfold-image.v1','passed':True,
 'exact_controls':controls,
 'local_consequence':'At each exact positive corner witness, the six free corner coordinates immerse into the rank-six target and the B/D seven-dimensional slope face has the SAME six-dimensional tangent image with kernel transverse to the corner. By the constant-rank and inverse function theorems on this regular local locus, the corner gives local target coordinates for the nearby B/D face image; no singular pushed density is inferred.',
 'scope':'Two regular positive corner neighborhoods only. Not a global surjectivity/multiplicity or full image canonical form theorem.'}
(OUT/'nine-point-shared-corner-local-sixfold-image.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'regular_positive_shared_corner_controls':len(controls),
 'full_cell_ranks':controls[0]['full_target_jacobian_ranks']},indent=2))
