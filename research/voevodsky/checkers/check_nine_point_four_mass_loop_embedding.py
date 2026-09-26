"""Exact positive-Grassmannian zero-column embedding of sourced 8-point four-mass cell."""
import contextlib,io,json,itertools,random
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_two_candidate_fermion_residual as previous
 import check_four_mass_rank_six_Y0_regular_witness as rank_six
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
D,variables=previous.D,previous.variables
w2,w4,w5,w6,w7,w8,t,u=variables
D9=s.Matrix.hstack(D[:,:2],s.zeros(2,1),D[:,2:])
assert D9.shape==(2,9) and D9[:,2]==s.zeros(2,1)
assert s.Matrix.hstack(D9[:,0:2],D9[:,3:9])==D
v=s.symbols('v',positive=True)
nonzero=zero=0
for i,j in itertools.combinations(range(9),2):
 minor=s.factor(s.det(s.Matrix.hstack(D9[:,i],D9[:,j])))
 polynomial=s.Poly(s.expand(minor.subs(t,u+v)),w2,w4,w5,w6,w7,w8,u,v)
 assert all(coef>=0 for coef in polynomial.coeffs()),(i,j,minor)
 if minor==0:zero+=1
 else:nonzero+=1
assert nonzero+zero==36 and zero>=8
# Source chart and fermion pushforward are IDENTICALLY the same as the
# eight-point source for ANY ninth twistor and ANY chi3 values.
Z8=s.Matrix(8,4,lambda i,j:s.Symbol(f'z{i+1}_{j}'))
z3=s.Matrix(1,4,lambda _,j:s.Symbol(f'z3_{j}'))
Z9=s.Matrix.vstack(Z8[:2,:],z3,Z8[2:,:])
assert D9*Z9==D*Z8
for parameter in variables:assert D9.diff(parameter)*Z9==D.diff(parameter)*Z8
chi8=s.Matrix(8,1,lambda i,_:s.Symbol(f'chi{i+1}'))
chi3=s.symbols('chi3')
chi9=s.Matrix.vstack(chi8[:2,:],s.Matrix([[chi3]]),chi8[2:,:])
assert D9*chi9==D*chi8
source=-s.S.One/(w2*w4*w5*w6*w7*w8*u*(t-u))
assert s.factor(source.subs(t,u+v)*w2*w4*w5*w6*w7*w8*u*v)==-1
# Validate generic twice-covered target after embedding using source's
# previously independent exact two-sheet fibre reconstruction.
samples=[]
for index,row in enumerate(json.loads((OUT/'nine-point-paired-two-sheet-trace.json').read_text())['rows']):
 init=dict(zip(variables,[s.Rational(x) for x in row['weights']]+[s.Rational(row['t']),s.Rational(row['u'])]))
 C=D.subs(init);kernel=s.Matrix.hstack(*C.nullspace())
 rng=random.Random(803+index);mix=s.Matrix(6,4,[rng.randint(-3,3) for _ in range(24)])
 raw=kernel*mix;z8=raw*raw[:4,:].inv();assert C*z8==s.zeros(2,4)
 z9=s.Matrix.vstack(z8[:2,:],s.Matrix([[3,7,11,17]]),z8[2:,:])
 altered=s.Matrix.vstack(z8[:2,:],s.Matrix([[11,13,17,19]]),z8[2:,:])
 assert D9*z9==D*z8==D9*altered
 sheets=list(previous.fibre(z8));assert len(sheets)==2
 jacobians=[]
 for point in sheets:
  assert D9.subs(point)*z9==D.subs(point)*z8==s.zeros(2,4)
  assert D9.subs(point)*altered==s.zeros(2,4)
  cols=[];cols9=[]
  for parameter in variables:
   d=D.diff(parameter).subs(point)*z8
   d9=D9.diff(parameter).subs(point)*z9
   assert d==d9
   cols.append(s.Matrix(list(d)));cols9.append(s.Matrix(list(d9)))
  J=s.Matrix.hstack(*cols).det(method='domain-ge')
  assert J!=0 and J==s.Matrix.hstack(*cols9).det(method='domain-ge')
  jacobians.append(str(J))
 samples.append({'source_weights':row['weights'],'generic_fibre_sheet_count':2,
                 'both_sheet_jacobians_nonzero_and_embedding_equal':True,
                 'physical_label3_bosonic_and_fermionic_independence':True,
                 'eight_point_jacobians':jacobians})
# Extend to strictly positive n=9 rank-six external data: insert row 3
# into the totally-positive eight-row moment curve and apply the SAME
# SL(6) change that puts the sourced target in the regular Y0 chart.
positive_rank_six=[]
Z8six=rank_six.Z
Z9six=s.Matrix([[j**d for d in range(6)] for j in range(1,10)])
assert Z9six[:2,:]==Z8six[:2,:] and Z9six[3:,:]==Z8six[2:,:]
for index,row in enumerate(json.loads((OUT/'nine-point-paired-two-sheet-trace.json').read_text())['rows']):
 point=dict(zip(variables,[s.Rational(x) for x in row['weights']]+[s.Rational(row['t']),s.Rational(row['u'])]))
 C=D.subs(point);Y=C*Z8six
 kernel=Y.nullspace();right=Y.T*(Y*Y.T).inv()
 G=s.Matrix.hstack(*kernel,*[right[:,j] for j in range(2)])
 G[:,0]=G[:,0]/G.det();assert G.det()==1
 ext9=Z9six*G;ext8=Z8six*G
 for chosen in itertools.combinations(range(9),6):
  # Vandermonde's strictly positive ordered minor is preserved by SL(6).
  expected=s.prod(b-a for a,b in itertools.combinations((i+1 for i in chosen),2))
  assert expected>0
  assert ext9[list(chosen),:].det(method='domain-ge')==expected
 assert D9*ext9==D*ext8
 target=D9.subs(point)*ext9
 assert target[:,:4]==s.zeros(2,4) and target[:,4:6].det()!=0
 roots=list(rank_six.fibre(C));assert len(roots)==2
 for root,other in roots:
  mapped=D9.subs(other)*ext9
  assert mapped[:,:4]==s.zeros(2,4) and mapped[:,4:6].det()!=0
  assert mapped==mapped[:,4:6]*target[:,4:6].inv()*target
  cols=[]
  for parameter in variables:
   d=D9.diff(parameter).subs(other)*ext9
   assert d==D.diff(parameter).subs(other)*ext8
   cols.append(s.Matrix(list(d[:,:4])))
  assert s.Matrix.hstack(*cols).det(method='domain-ge')!=0
 positive_rank_six.append({'source_weights':row['weights'],'all_84_nine_point_external_six_minors_positive':True,
  'same_rank_six_Y0_target_has_two_regular_source_sheets':True})
report={'schema':'marici.nima.nine-point-four-mass-loop-embedding.v1','passed':True,
 'exact_positive_ordered_minor_count':nonzero,'identically_zero_minor_count':zero,
 'symbolic_image_identity':'C9 Z9 = C8 Z8 for arbitrary inserted Z3 and every source point',
 'symbolic_fermionic_identity':'C9 chi9=C8 chi8 for arbitrary inserted chi3 and every SU4 flavor',
 'symbolic_jacobian_identity':'Every source parameter derivative of C9 Z9 equals the C8 Z8 derivative, so two-sheet pushforward Jacobians and dlog measure are unchanged wherever regular.',
 'source_orientation':'-dw2/w2 ^ dw4/w4 ^ dw5/w5 ^ dw6/w6 ^ dw7/w7 ^ dw8/w8 ^ dv/v ^ du/u, with v=t-u>0 and source orientation inherited.',
 'source_region':'w2,w4,w5,w6,w7,w8,u,v positive; C9 is a positive-boundary loop-column positroid cell (physical col3 zero), not an interior n9 BCFW history.',
 'generic_exact_controls':samples,
 'strictly_positive_nine_point_rank_six_external_Y0_controls':positive_rank_six,
 'boundary':'This is a source-authorized alternative eight-point four-mass contour embedded as an n9 positive boundary and its same two-sheet invariant; it does not prove equality to the full n9 tree amplitude or full amplituhedron image coverage.'}
(OUT/'nine-point-four-mass-loop-embedding.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'positive_minors':nonzero,'zero_minors':zero,'two_sheet_witnesses':len(samples)},indent=2))
