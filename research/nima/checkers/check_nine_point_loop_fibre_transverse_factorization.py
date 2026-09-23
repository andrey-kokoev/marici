"""Four exact source sheets: factor the local 14x14 top-cell chart into target and fibre normals."""
import contextlib,io,itertools,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):import check_nine_point_four_mass_loop_image_interior as previous
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
D,vars,D9,Z8,Z9=previous.previous.D,previous.vars,previous.D9,previous.previous.Z8six,previous.Z9
K=s.Matrix.vstack(*(x.T for x in Z9.T.nullspace()))
assert K.shape==(3,9) and K*Z9==s.zeros(3,6)
parameters=s.symbols('t0:6');T=s.Matrix(2,3,parameters)
assert D9[:,[0,3]]==s.eye(2)
# The gauge-normal coordinates vanish IDENTICALLY along the eight-source
# sheet. They are transverse to it in the 14-dimensional top chart.
assert D9[:,2]==s.zeros(2,1)
for i,j in ((0,1),(3,4),(5,6),(7,8)):
 assert s.det(s.Matrix.hstack(D9[:,i],D9[:,j]))==0
rows=[]
for index,input_row in enumerate(json.loads((OUT/'nine-point-paired-two-sheet-trace.json').read_text())['rows']):
 point0=dict(zip(vars,[s.Rational(x) for x in input_row['weights']]+[s.Rational(input_row['t']),s.Rational(input_row['u'])]))
 C0=D.subs(point0);Y=C0*Z8
 kernel=Y.nullspace();right=Y.T*(Y*Y.T).inv()
 G=s.Matrix.hstack(*kernel,*[right[:,j] for j in range(2)])
 G[:,0]=G[:,0]/G.det();assert G.det()==1
 ext=Z9*G
 assert K*ext==s.zeros(3,6)
 sheets=list(previous.previous.rank_six.fibre(C0));assert len(sheets)==2
 for root,point in sheets:
  C=D9.subs(point);mapped=C*ext
  assert mapped[:,:4]==s.zeros(2,4)
  H=mapped[:,4:6];assert H.det()!=0
  tangent=[]
  for parameter in vars:
   derivative=D9.diff(parameter).subs(point)*ext
   tangent.append(s.Matrix(list(H.inv()*derivative[:,:4])))
  J=s.Matrix.hstack(*tangent)
  detJ=J.det(method='domain-ge');assert detJ!=0
  normal_derivative=[]
  E=T*K
  normal_derivative.extend((E[0,2],E[1,2]))
  for i,j in ((0,1),(3,4),(5,6),(7,8)):
   normal_derivative.append(s.det(s.Matrix.hstack(E[:,i],C[:,j]))+
                            s.det(s.Matrix.hstack(C[:,i],E[:,j])))
  M,rhs=s.linear_eq_to_matrix(normal_derivative,parameters)
  assert rhs==s.zeros(6,1)
  detM=M.det(method='domain-ge');assert detM!=0
  # d(target)/d(T)=0 EXACT because K*external=0;
  # d(normals)/d(source)=0 IDENTICALLY along loop/parallel cell.
  block=s.diag(J,M)
  determinant=block.det(method='domain-ge')
  assert determinant==detJ*detM and determinant!=0
  rows.append({'witness_index':index,'kernel_area':str(root),
   'positive_source_sheet':root==0,'source_target_jacobian_nonzero':True,
   'kernel_fibre_transverse_normal_jacobian_nonzero':True,
   'fourteen_by_fourteen_block_diagonal_determinant_nonzero':True,
   'target_and_fibre_dimensions':[8,6],
   'source_target_jacobian_sign':int(s.sign(detJ)),
   'fibre_normal_jacobian_sign':int(s.sign(detM))})
report={'schema':'marici.nima.nine-point-loop-fibre-transverse-factorization.v1','passed':True,
 'source_sheet_tests':rows,
 'local_identity':'In gauge C[:,phys(1,4)]=I2, use eight sourced positive-cell coordinates and six left-kernel coordinates T. Take eight Gr(2,6) target-chart coordinates and six normals (both zero-column entries and four parallel-pair minors). At every tested source sheet, d(target)/dT=0 as K*Z9=0; d(normals)/dsource=0 identically; diagonal 8x8 and 6x6 blocks have nonzero determinants. Thus the 14x14 local coordinate Jacobian factors exactly.',
 'interpretation':'The sourced eight-dimensional loop cell is a transverse discrete intersection (two complex/rational sheets in these examples) of a six-dimensional full n9 source fibre; its two-sheet form is a localized boundary-source contour, not by itself an image-boundary residue.',
 'boundary':'Four exact sheets over two positive rank6 external witnesses. Factorization is local where both determinants stay nonzero; no canonical top-cell form orientation, global residue theorem, full image-form trace or coverage is established.'}
(OUT/'nine-point-loop-fibre-transverse-factorization.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'sheet_checks':len(rows),'full_local_jacobian_rank':14,
 'positive_sheet_count':sum(x['positive_source_sheet'] for x in rows)},indent=2))
