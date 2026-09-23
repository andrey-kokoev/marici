"""Project full four-mass tensor to monomials using all eight retained labels."""
import contextlib,io,json,random
from pathlib import Path
import sympy as s
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_two_candidate_fermion_residual as previous
 import check_nine_point_history27_transported_pair_ratio as transported
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/nima/results'
screen=json.loads((OUT/'nine-point-authored-four-pair-history-screen.json').read_text())
assert screen['exact_eight_label_endpoint_candidate_count']==2
D,variables=previous.D,previous.variables
physical_labels=(1,2,4,5,6,7,8,9)
matchings=[((1,3),(2,5),(4,7),(6,8)),
           ((1,3),(2,6),(4,8),(5,7)),
           ((1,3),(2,7),(4,6),(5,8))]
assert all(sorted(i for pair in pairs for i in pair)==list(range(1,9)) for pairs in matchings)
records=[]
for index,row in enumerate(json.loads((OUT/'nine-point-paired-two-sheet-trace.json').read_text())['rows']):
 init=dict(zip(variables,[s.Rational(v) for v in row['weights']]+[s.Rational(row['t']),s.Rational(row['u'])]))
 C=D.subs(init);null=s.Matrix.hstack(*C.nullspace())
 rng=random.Random(803+index)
 mix=s.Matrix(6,4,[rng.randint(-3,3) for _ in range(24)])
 trial=null*mix;z=trial*trial[:4,:].inv();assert C*z==s.zeros(2,4)
 sheets=[]
 for point in previous.fibre(z):
  Ci=D.subs(point);cols=[]
  for v in variables:
   deriv=D.diff(v).subs(point)*z
   cols.append(s.Matrix([deriv[i,j] for i in range(2) for j in range(4)]))
  J=s.Matrix.hstack(*cols).det(method='domain-ge');assert J!=0
  source=-s.S.One/(s.prod(point[v] for v in variables[:6])*point[variables[7]]*(point[variables[6]]-point[variables[7]]))
  sheets.append((source/J,Ci))
 F=[]
 for pairs in matchings:
  F.append(s.factor(sum(weight*s.prod(s.Matrix.hstack(Ci[:,p-1],Ci[:,q-1]).det() for p,q in pairs) for weight,Ci in sheets)))
 assert any(v!=0 for v in F)
 # Reproduce the calibrated generic bosonic presentation from the
 # standalone transported-spinor checker (seed and candidate filter).
 rng2=random.Random(931+index)
 for attempt in range(300):
  P=s.Matrix(4,4,[rng2.randint(-4,4) for _ in range(16)])
  if P.det()==0:continue
  zz=z*P
  physical=[None,zz[0,:],zz[1,:],s.Matrix([[3,7,11,17]])*P]
  physical.extend(zz[j,:] for j in range(2,8))
  def lam(i):return physical[i][:,0:2].T
  if all(s.Matrix.hstack(lam(i-1 if i>1 else 9),lam(i)).det()!=0 for i in range(1,10)):break
 else:raise AssertionError('nondegenerate presentation not found')
 def lam(i):return physical[i][:,0:2].T
 def mu(i):return physical[i][:,2:4].T
 def x(i):
  j=i-1 if i>1 else 9
  return s.Matrix.hstack(mu(j),mu(i))*s.Matrix.hstack(lam(j),lam(i)).inv()
 def br(*seq):return s.Matrix.vstack(*(physical[i] for i in seq)).det(method='domain-ge')
 X={i:x(i) for i in (2,5,7,8,9)};eps2=s.Matrix([[0,1],[-1,0]])
 xi=lam(9).T*(X[9]-X[8]).T*eps2*(X[8]-X[2])
 def inner_term(a,b):return xi*eps2*(X[2]-X[a]).T*eps2*(X[a]-X[b])*eps2
 L1,L2=inner_term(5,7),inner_term(7,5)
 inner={i:s.S.Zero for i in range(1,10)}
 for i,L in ((7,L1),(5,L2),(2,-L1-L2)):
  inverse=s.Matrix.vstack(lam(i-1).T,lam(i).T).inv()
  inner[i-1]+=s.factor((L*inverse[:,0])[0]);inner[i]+=s.factor((L*inverse[:,1])[0])
 outer={i:s.S.Zero for i in range(1,10)}
 seq=(9,1,2,7,8)
 for k,p in enumerate(seq):outer[p]=br(*(seq[(k+j)%5] for j in range(1,5)))
 def beta(p,q):
  p,q=physical_labels[p-1],physical_labels[q-1]
  return s.factor(outer[p]*inner[q]-outer[q]*inner[p])
 # Exact calibration of the extended B row against the already
 # sourced and ordinary-R-controlled history27 X/Y ratio.
 observed=s.factor(beta(2,6)/beta(1,5))
 expected=s.Rational(transported.rows[index]['transported_pair_ratio'])
 assert observed==expected
 K=[s.factor(s.prod(beta(p,q) for p,q in pairs)) for pairs in matchings]
 # History9 has only outer support on local labels 1 and 3: its
 # per-flavor Pluecker coefficient for the shared (1,3) pair vanishes.
 history9_outer={8,1,2,3,4};history9_inner={8,4,5,6,7}
 assert {1,3}<=history9_outer-history9_inner
 assert all(v!=0 for v in K)
 ratios=[s.factor(F[j]/K[j]) for j in range(len(F))]
 assert len(set(ratios))>1
 records.append({'source_weights':row['weights'],
  'complete_fourmass_all_eight_label_coefficients':[str(v) for v in F],
  'history27_all_eight_label_coefficients_up_to_common_prefactor':[str(v) for v in K],
  'fourmass_to_history27_monomial_ratios':[str(v) for v in ratios],
  'ratios_not_constant':True})
report={'schema':'marici.nima.nine-point-all-eight-label-fermion-projection.v1','passed':True,
 'three_flavorwise_perfect_matchings':[list(map(list,m)) for m in matchings],
 'screen':'Exactly two authored histories have the full explicit eight-label envelope. The other seven individually label3-free histories have at most seven explicit labels; they vanish on every all-eight-label monomial. History9 also vanishes because pair (1,3) lies entirely in its outer-exclusive support.',
 'witnesses':records,
 'conclusion':'The complete starred fourmass fermionic polynomial does not agree with any scalar multiple of transported history27 on three distinct all-eight-label monomials at either of two generic z inputs. Consequently a sum of only the nine individually label3-free endpoint-screened histories cannot equal the fourmass invariant, assuming their endpoint envelope bounds actual momentum-twistor fermion support. Any authored representation must use additional histories with individual label3 dependence cancelling in the sum, or a different non-BCFW presentation.',
 'boundary':'All-eight support reasoning uses source theta-to-momentum-twistor endpoint incidence and the calibrated transported-spinor convention. This does not construct the additional cancellation combination, the global n9 amplitude form, or image coverage.'}
(OUT/'nine-point-all-eight-label-fermion-projection.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'witnesses':len(records),'three_monomial_ratios_constant':False},indent=2))
