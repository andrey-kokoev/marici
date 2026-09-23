"""Unique two-summand quartic decomposition excludes ordinary history 9 at any weight."""
import contextlib,io,json,random
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):import check_nine_point_two_candidate_fermion_residual as previous
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
prior=json.loads((OUT/'nine-point-two-candidate-fermion-residual.json').read_text());assert prior['passed']
D,variables=previous.D,previous.variables
out=[]
for index,row in enumerate(json.loads((OUT/'nine-point-paired-two-sheet-trace.json').read_text())['rows']):
 init=dict(zip(variables,[s.Rational(v) for v in row['weights']]+[s.Rational(row['t']),s.Rational(row['u'])]))
 C=D.subs(init);null=s.Matrix.hstack(*C.nullspace())
 rng=random.Random(803+index)
 mix=s.Matrix(6,4,[rng.randint(-3,3) for _ in range(24)])
 trial=null*mix;assert trial[:4,:].det()!=0
 z=trial*trial[:4,:].inv();assert z[4:8,:].det()!=0
 assert C*z==s.zeros(2,4)
 def br(i,j,k,l):return z[[i-1,j-1,k-1,l-1],:].det(method='domain-ge')
 points=list(previous.fibre(z));assert len(points)==2
 sheets=[]
 for point in points:
  Ci=D.subs(point)
  columns=[]
  for v in variables:
   derivative=D.diff(v).subs(point)*z
   columns.append(s.Matrix([derivative[i,j] for i in range(2) for j in range(4)]))
  J=s.Matrix.hstack(*columns).det(method='domain-ge');assert J!=0
  source=-s.S.One/(s.prod(point[v] for v in variables[:6])*point[variables[7]]*(point[variables[6]]-point[variables[7]]))
  px=s.Matrix.hstack(Ci[:,0],Ci[:,4]).det()
  py=s.Matrix.hstack(Ci[:,1],Ci[:,5]).det()
  assert px!=0 and py!=0
  sheets.append((source/J,px,py))
 moment=[s.factor(sum(weight*px**(4-j)*py**j for weight,px,py in sheets)) for j in range(5)]
 hankel=s.Matrix(3,3,lambda i,j:moment[i+j])
 assert hankel.rank()==2 and hankel.det()==0
 (w1,x1,y1),(w2,x2,y2)=sheets
 r1=s.factor(y1/x1);r2=s.factor(y2/x2)
 assert r1!=r2
 kernel=s.Matrix([r1*r2,-r1-r2,1])
 assert hankel*kernel==s.zeros(3,1)
 # History 9 = [8,1,2,3,4][8,4,5,6,7]. Per-flavor pair
 # amplitudes for X=(1,5) and Y=(2,6), including cyclic numerator
 # order, are nx and ny; a common denominator does not change ny/nx.
 nx=br(2,3,4,8)*br(6,7,8,4)
 ny=br(3,4,8,1)*br(7,8,4,5)
 assert nx!=0 and ny!=0
 rk=s.factor(ny/nx)
 obstruction=s.factor(rk*rk-(r1+r2)*rk+r1*r2)
 assert obstruction==s.factor((rk-r1)*(rk-r2)) and obstruction!=0
 out.append({'source_weights':row['weights'],'two_branch_pair_ratios':[str(r1),str(r2)],
  'ordinary_history9_pair_ratio':str(rk),
  'rank_two_quartic_Hankel_kernel':[str(v) for v in kernel],
  'history9_root_polynomial_obstruction':str(obstruction),
  'history9_cannot_be_any_one_of_two_summands':True})
report={'schema':'marici.nima.nine-point-four-mass-secant-uniqueness.v1','passed':True,
 'test':'For X=(1,5),Y=(2,6), use all five flavor-selected coefficients F_j=sum_i weight_i x_i^(4-j)y_i^j. The 3x3 Hankel matrix H_(ab)=F_(a+b) has rank two and unique kernel polynomial (r-r1)(r-r2). Any decomposition into TWO flavor-blind delta4*delta4 terms must have exactly these two pair ratios. History9 has a different ratio at two independent generic z witnesses, regardless of its scalar coefficient.',
 'witnesses':out,
 'conclusion':'The complete four-mass invariant cannot be a sum of history9 with ANY one other single R*R history, including candidate27, even if the coefficient of history9 is allowed to be kinematic dependent. This rules out any TWO-term representation containing ordinary history9 on the tested generic open set; at least three decomposable terms would be required if history9 participates with nonzero coefficient.',
 'boundary':'Two-variable flavor restriction yields a necessary obstruction for a two-term global identity; it does not rule out three or more authored histories, nor prove tree-image coverage or a full-amplitude equality.'}
(OUT/'nine-point-four-mass-secant-uniqueness.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'witnesses':len(out),'history9_in_any_two_term_decomposition':False},indent=2))
