"""Exact fermionic tensor-rank obstruction to a single authored R*R history."""
import contextlib,io,json
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):import check_four_mass_rank_six_Y0_regular_witness as witness
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
prior=json.loads((OUT/'nine-point-authored-four-pair-history-screen.json').read_text());assert prior['passed']
assert [x['history_index'] for x in prior['exact_eight_label_endpoint_candidates']]==[9,27]
src=(ROOT/'research/sources/nima/papers/n2mhv-tree/0808.2475/newrecursionv6.tex').read_text()
assert r'R_{n;a_1b_1}^{0;0}' in src and r'R_{n;b_1a_1;a_2b_2}^{0;a_1b_1}' in src
Z,D,variables=witness.Z,witness.D,witness.variables
results=[]
for row in json.loads((OUT/'nine-point-paired-two-sheet-trace.json').read_text())['rows']:
 initial=dict(zip(variables,[s.Rational(x) for x in row['weights']]+[s.Rational(row['t']),s.Rational(row['u'])]))
 C=D.subs(initial);Y=C*Z
 kernel=Y.nullspace();right=Y.T*(Y*Y.T).inv()
 G=s.Matrix.hstack(*kernel,*[right[:,j] for j in range(2)]);G[:,0]=G[:,0]/G.det()
 z=(Z*G)[:,0:4]
 terms=[]
 for root,point in witness.fibre(C):
  Ci=D.subs(point);assert Ci*z==s.zeros(2,4)
  cols=[]
  for variable in variables:
   diff=D.diff(variable).subs(point)*z
   cols.append(s.Matrix([diff[i,j] for i in range(2) for j in range(4)]))
  Jz=s.Matrix.hstack(*cols).det(method='domain-ge');assert Jz!=0
  source=-s.S.One/(s.prod(point[v] for v in variables[:6])*point[variables[7]]*(point[variables[6]]-point[variables[7]]))
  weight=source/Jz
  # Two disjoint external eta-pairs in the local retained-eight order.
  # X=(1,5), Y=(2,6); flavor-by-flavor coefficient is their Pluecker minor.
  dx=s.Matrix.hstack(Ci[:,0],Ci[:,4]).det()
  dy=s.Matrix.hstack(Ci[:,1],Ci[:,5]).det()
  assert dx!=0 and dy!=0 and weight!=0
  terms.append((s.factor(weight),s.factor(dx),s.factor(dy)))
 assert len(terms)==2
 xx=s.factor(sum(w*dx**4 for w,dx,dy in terms))
 yy=s.factor(sum(w*dy**4 for w,dx,dy in terms))
 xy=s.factor(sum(w*dx**2*dy**2 for w,dx,dy in terms))
 defect=s.factor(xx*yy-xy**2)
 (w1,x1,y1),(w2,x2,y2)=terms
 factor=s.factor(w1*w2*(x1*x1*y2*y2-x2*x2*y1*y1)**2)
 assert defect==factor and defect!=0
 # Any ONE sourced R*generalized-R history has two degree-four fermion
 # delta factors and yields a rank-one flavor tensor: xx*yy=xy^2.
 results.append({'source_weights':row['weights'],'two_branch_fermionic_rank_one_minor':str(defect),
                 'rank_one_violated':True,'exact_two_sheet_factorization':True,
                 'pair_X_local_labels':[1,5],'pair_Y_local_labels':[2,6]})
report={'schema':'marici.nima.nine-point-four-mass-vs-single-history-fermion-rank.v1','passed':True,
 'four_mass_complete_fermion_tensor_test':'F_XXXX F_YYYY - F_XXYY^2 where F_XXXX=sum_i weight_i*Delta_i(1,5)^4, F_YYYY=sum_i weight_i*Delta_i(2,6)^4, F_XXYY=sum_i weight_i*Delta_i(1,5)^2*Delta_i(2,6)^2.',
 'identity':'The defect equals w1*w2*(Delta1(X)^2*Delta2(Y)^2-Delta2(X)^2*Delta1(Y)^2)^2 and is nonzero at both exact witnesses.',
 'witnesses':results,
 'conclusion':'The complete two-branch starred four-mass fermionic polynomial cannot equal ANY SINGLE authored nine-point product R*generalized-R term, including transported-spinor candidate 27, for generic kinematics: each such term is a single product of two flavor-blind fermionic degree-four deltas and has rank-one tensor. A sum of histories or different on-shell decomposition is not excluded.',
 'claim_boundary':'Exact generic nonidentity via two rational kinematic witnesses, not a proof that the full authored n=9 SUM lacks this invariant or that the four-pair cell is a BCFW tree cell; orientations and global image coverage remain separate.'}
(OUT/'nine-point-four-mass-vs-single-history-fermion-rank.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'witnesses':len(results),'single_history_identity_possible':False,
                  'history27_standalone_excluded':True},indent=2))
