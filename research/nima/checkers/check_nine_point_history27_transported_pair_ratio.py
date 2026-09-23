"""Conventions-aware attempted spinor-transport test of history 27 against two sheets."""
import contextlib,io,json,random
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):import check_nine_point_two_candidate_fermion_residual as previous
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
src=(ROOT/'research/sources/nima/papers/n2mhv-tree/0808.2475/newrecursionv6.tex').read_text()
assert r'\l< \xi | = \l<n | x_{nb_1}x_{b_1 a_1}' in src
assert r'\l< \xi | x_{a_r a}x_{ab} | \theta_{ba_r}' in src
source_twistors=(ROOT/'research/sources/nima/papers/six-point-nmhv/1312.2007/amplituhedron.tex').read_text()
assert r'z_a = \left(\begin{array}{c} \lambda_a \\ \mu_a' in source_twistors
D,variables=previous.D,previous.variables
rows=[]
for index,row in enumerate(json.loads((OUT/'nine-point-paired-two-sheet-trace.json').read_text())['rows']):
 init=dict(zip(variables,[s.Rational(v) for v in row['weights']]+[s.Rational(row['t']),s.Rational(row['u'])]))
 C=D.subs(init);null=s.Matrix.hstack(*C.nullspace())
 rng=random.Random(803+index)
 mix=s.Matrix(6,4,[rng.randint(-3,3) for _ in range(24)])
 raw=null*mix;z=raw*raw[:4,:].inv();assert C*z==s.zeros(2,4)
 # The first-four-to-I gauge makes some lambda pairs degenerate.
 # Restore a generic SL4 presentation and retain source zero column 3.
 rng2=random.Random(931+index)
 for attempt in range(300):
  P=s.Matrix(4,4,[rng2.randint(-4,4) for _ in range(16)])
  if P.det()==0:continue
  zz=z*P
  physical=[None,zz[0,:],zz[1,:],s.Matrix([[3,7,11,17]])*P]
  physical.extend(zz[j,:] for j in range(2,8))
  assert len(physical)==10
  def lam(i):return physical[i][:,0:2].T
  if any(s.det(s.Matrix.hstack(lam(i-1 if i>1 else 9),lam(i)))==0 for i in range(1,10)):continue
  break
 else:raise AssertionError('no_nondegenerate_momentum_twistor_presentation')
 def ratio(physical):
  def lambda_(i):return physical[i][:,0:2].T
  def mu(i):return physical[i][:,2:4].T
  def x(i):
   j=i-1 if i>1 else 9
   return s.Matrix.hstack(mu(j),mu(i))*s.Matrix.hstack(lambda_(j),lambda_(i)).inv()
  def bracket(*seq):return s.Matrix.vstack(*(physical[i] for i in seq)).det(method='domain-ge')
  X={i:x(i) for i in (2,5,7,8,9)}
  eps2=s.Matrix([[0,1],[-1,0]])
  xi=lambda_(9).T*(X[9]-X[8]).T*eps2*(X[8]-X[2])
  L=xi*eps2*(X[2]-X[5]).T*eps2*(X[5]-X[7])*eps2
  L2=xi*eps2*(X[2]-X[7]).T*eps2*(X[7]-X[5])*eps2
  pair=s.Matrix.vstack(lambda_(6).T,lambda_(7).T).inv()
  c6=(L*pair[:,0])[0];c7=(L*pair[:,1])[0]
  assert c6!=0 and c7!=0
  # Independent calibration of the SAME x25 x57 spinor contraction
  # pattern against the ordinary R_{9;5,7} five-bracket [9,4,5,6,7].
  plain=lambda_(9).T*(X[9]-X[5]).T*eps2*(X[5]-X[7])*eps2
  plain_ratio=s.factor((plain*pair[:,1])[0]/(plain*pair[:,0])[0])
  assert plain_ratio==bracket(9,4,5,6)/bracket(7,9,4,5)
  outer=bracket(7,8,9,1)/bracket(2,7,8,9)
  theta2=s.Matrix.vstack(lambda_(1).T,lambda_(2).T).inv()
  transported_outer=s.factor((xi*eps2*theta2[:,1])[0]/(xi*eps2*theta2[:,0])[0])
  assert transported_outer==outer, ('ordinary_R_outer_calibration',transported_outer,outer)
  # Outer chi7 is nonzero, and the generalized inner delta ALSO has
  # chi2 through theta2. This crossed contribution is essential for Y.
  b2=((-L-L2)*theta2[:,1])[0]
  a1=bracket(2,7,8,9);a2=bracket(7,8,9,1);a7=bracket(8,9,1,2)
  return s.factor((a2*c7-a7*b2)/(a1*c6))
 r27=ratio(physical)
 scale=s.diag(2,3,5,7)
 scale[0,2]=1;scale[1,3]=-2
 again=[None]+[p*scale for p in physical[1:]]
 assert ratio(again)==r27
 changed_three=[None]+list(physical[1:])
 changed_three[3]=s.Matrix([[11,13,17,19]])*P
 assert ratio(changed_three)==r27
 sheets=list(previous.fibre(z))
 rp=[]
 for point in sheets:
  Ci=D.subs(point)
  dx=s.Matrix.hstack(Ci[:,0],Ci[:,4]).det()
  dy=s.Matrix.hstack(Ci[:,1],Ci[:,5]).det()
  assert dx!=0 and dy!=0
  rp.append(s.factor(dy/dx))
 assert len(rp)==2 and rp[0]!=rp[1]
 # Ratios of Pluecker minors are unchanged under the z->zP gauge.
 assert r27 not in rp
 rows.append({'source_weights':row['weights'],'transported_pair_ratio':str(r27),
              'two_four_mass_branch_pair_ratios':[str(v) for v in rp],
              'upper_parabolic_GL4_covariance_control':True,
              'physical_label_three_deformation_invariant':True,
              'two_independent_ordinary_R_five_bracket_calibrations':True,
              'candidate27_ratio_differs_from_both_branches':True})
report={'schema':'marici.nima.nine-point-history27-transported-pair-ratio.v1','passed':True,'witnesses':rows,
 'translation_convention':'Incidence mu_i=x_i lambda_i solved from adjacent momentum twistors; theta_i lambda_(i-1/i)=chi_(i-1/i); epsilon-raised alternating x spinor indices. ξ=<9|x98 x82; the FULL pair ratio is (A2*B7-A7*B2)/(A1*B6), including the crossed outer-chi7/inner-chi2 term from both theta72 and theta52.',
 'supersedes_shortcut':'An earlier expression dropped -A7*B2 and is invalid; the present corrected two-witness result and ordinary-R calibrations pass.',
 'boundary':'Exact two-kinematic witness for candidate27 per-flavor pair ratio using primary-source generalized xi, momentum-twistor incidence and two ordinary-R five-bracket calibrations. Nontrivial upper-parabolic GL4 and deleted-label-3 invariances are checked. This is a necessary two-term secant exclusion, not a full history27 bosonic prefactor or any three-or-more-term identity.'}
(OUT/'nine-point-history27-transported-pair-ratio.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'witnesses':len(rows),'r27_equals_fourmass_branch':False},indent=2))
