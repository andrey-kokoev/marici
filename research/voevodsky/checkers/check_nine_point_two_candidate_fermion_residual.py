"""Can the fixed-coefficient history 9 leave a single R*R fermion tensor?"""
import contextlib,io,json,random
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_four_mass_rank_six_Y0_regular_witness as witness
 import check_four_mass_complete_component_companion_trace as psi
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
prior=json.loads((OUT/'nine-point-four-mass-vs-single-history-fermion-rank.json').read_text());assert prior['passed']
D,variables=witness.D,witness.variables
x=s.symbols('x')
def fibre(z):
 H=z[4:8,:];assert H.det()!=0
 w=H.T.inv()*s.Matrix([1,x,0,0]);V=(w[0]*z[4,:]+w[1]*z[5,:]).T;W=(w[2]*z[6,:]+w[3]*z[7,:]).T
 P=s.Poly(s.cancel(V[0]*W[1]-V[1]*W[0]),x)
 assert P.degree()==2
 roots=s.solve(P.as_expr(),x);assert len(roots)==2 and all(r.is_Rational for r in roots)
 for root in roots:
  weights=w.subs(x,root);vv=V.subs(x,root);ww=W.subs(x,root)
  denom=s.factor(vv[2]*ww[0]-ww[2]*vv[0]);assert denom!=0
  tv=s.factor(-ww[0]/denom);uv=s.factor(vv[0]/denom)
  point=dict(zip(variables,(root,s.factor(-tv*vv[3]-uv*ww[3]),*weights,tv,uv)))
  assert D.subs(point)*z==s.zeros(2,4)
  yield point
rows=[]
for row_index,row in enumerate(json.loads((OUT/'nine-point-paired-two-sheet-trace.json').read_text())['rows']):
 initial=dict(zip(variables,[s.Rational(v) for v in row['weights']]+[s.Rational(row['t']),s.Rational(row['u'])]))
 C=D.subs(initial);null=s.Matrix.hstack(*C.nullspace());assert null.shape==(8,6)
 rng=random.Random(803+row_index)
 # Random rational external four-vectors in the EXACT nullspace of the
 # chosen positive four-pair source point. Gauge first four to I4.
 for attempt in range(200):
  mix=s.Matrix(6,4,[rng.randint(-3,3) for _ in range(24)])
  trial=null*mix
  if trial[:4,:].det()==0:continue
  z=trial*trial[:4,:].inv()
  if z[4:8,:].det()==0:continue
  def br(i,j,k,l):return z[[i-1,j-1,k-1,l-1],:].det(method='domain-ge')
  outer=(8,1,2,3,4);inner=(8,4,5,6,7)
  def denom(seq):return s.prod(br(*(seq[(offset+j)%5] for j in range(4))) for offset in range(5))
  d=denom(outer)*denom(inner)
  if d==0:continue
  try:points=list(fibre(z))
  except (AssertionError,ZeroDivisionError):continue
  break
 else:raise AssertionError('no_generic_rational_nullspace_witness')
 assert C*z==s.zeros(2,4) and any(D.subs(p)==C for p in points)
 terms=[]
 for point in points:
  Ci=D.subs(point)
  cols=[]
  for v in variables:
   diff=D.diff(v).subs(point)*z
   cols.append(s.Matrix([diff[i,j] for i in range(2) for j in range(4)]))
  J=s.Matrix.hstack(*cols).det(method='domain-ge');assert J!=0
  source=-s.S.One/(s.prod(point[v] for v in variables[:6])*point[variables[7]]*(point[variables[6]]-point[variables[7]]))
  pairX=s.Matrix.hstack(Ci[:,0],Ci[:,4]).det()
  pairY=s.Matrix.hstack(Ci[:,1],Ci[:,5]).det()
  terms.append((source/J,pairX,pairY))
 Fx=s.factor(sum(weight*px**4 for weight,px,py in terms))
 Fy=s.factor(sum(weight*py**4 for weight,px,py in terms))
 Fxy=s.factor(sum(weight*px**2*py**2 for weight,px,py in terms))
 sourced,_=psi.complete_component(br)
 assert Fx==sourced
 nx=br(2,3,4,8)*br(6,7,8,4)
 ny=br(3,4,8,1)*br(7,8,4,5)
 Kx=nx**4/d;Ky=ny**4/d;Kxy=nx**2*ny**2/d
 assert Kx*Ky-Kxy**2==0
 crossing=s.factor(Fx*Ky+Fy*Kx-2*Fxy*Kxy)
 assert crossing!=0
 only_possible_lambda=s.factor((Fx*Fy-Fxy**2)/crossing)
 defects={}
 for coefficient in (1,-1):
  defect=s.factor((Fx-coefficient*Kx)*(Fy-coefficient*Ky)-(Fxy-coefficient*Kxy)**2)
  defects[str(coefficient)]=str(defect)
  assert defect!=0
 rows.append({'source_weights':row['weights'],'random_attempt':attempt,
  'independent_generic_z_rank':z.rank(),'history9_denominator_nonzero':True,
  'full_source_XX_matches_independent_psi':True,
  'residual_rank_one_defect_after_plus_history9':defects['1'],
  'residual_rank_one_defect_after_minus_history9':defects['-1'],
  'only_rank_one_restoring_history9_coefficient':str(only_possible_lambda),
  'both_fixed_signs_excluded':True})
assert rows[0]['only_rank_one_restoring_history9_coefficient']!=rows[1]['only_rank_one_restoring_history9_coefficient']
report={'schema':'marici.nima.nine-point-two-candidate-fermion-residual.v1','passed':True,
 'source_candidates':'History 9 ordinary [8,1,2,3,4][8,4,5,6,7] and history 27 transported xi=(9,8,2).',
 'test':'On independently generated GENERIC exact rational z in the four-pair source nullspace, reconstruct both sheets, compute F_XXXX,F_YYYY,F_XXYY and subtract history9 fixed ±1 ordinary-product coefficients. If the remainder were a single generalized-R product its rank-one minor would vanish. Both signs yield nonzero minors at two exact inputs.',
 'witnesses':rows,
 'rank_one_restoring_history9_coefficient_is_kinematic_dependent':True,
 'conclusion':'The complete starred four-mass invariant is not a fixed-sign sum of ONLY endpoint candidates 9 and 27, if 27 is one sourced generalized-R delta4*delta4 product. This does not exclude rational kinematic coefficients, other histories with explicit label 3 whose dependence cancels in a sum, or identities involving more than two authored terms.',
 'orientation_boundary':'Both ±1 source-form sign choices were tested; published generalized-R overall convention remains independent.'}
(OUT/'nine-point-two-candidate-fermion-residual.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'witnesses':len(rows),'fixed_plus_minus_two_candidate_sum_excluded':True},indent=2))
