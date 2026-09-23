"""Compile all 50 authored n9 fermionic rows and rank-filter label-3 cancellation."""
import contextlib,io,json,random,sys,itertools,os
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/nima'))
with contextlib.redirect_stdout(io.StringIO()):
 import check_nine_point_history27_transported_pair_ratio as calibrated
 import check_nine_point_two_candidate_fermion_residual as prior_checker
from nnmhv_coherence_paths import compile_nnmhv_histories
OUT=ROOT/'research/nima/results'
screen=json.loads((OUT/'nine-point-authored-four-pair-history-screen.json').read_text());assert screen['passed']
D,variables=prior_checker.D,prior_checker.variables
witness_index=int(os.environ.get('NIMA_LABEL3_WITNESS_INDEX','0'))
assert witness_index in (0,1)
row=json.loads((OUT/'nine-point-paired-two-sheet-trace.json').read_text())['rows'][witness_index]
init=dict(zip(variables,[s.Rational(v) for v in row['weights']]+[s.Rational(row['t']),s.Rational(row['u'])]))
C=D.subs(init);null=s.Matrix.hstack(*C.nullspace())
rng=random.Random(803+witness_index);mix=s.Matrix(6,4,[rng.randint(-3,3) for _ in range(24)])
trial=null*mix;z=trial*trial[:4,:].inv();assert C*z==s.zeros(2,4)
rng2=random.Random(931+witness_index)
for attempt in range(300):
 P=s.Matrix(4,4,[rng2.randint(-4,4) for _ in range(16)])
 if P.det()==0:continue
 zz=z*P;phys=[None,zz[0,:],zz[1,:],s.Matrix([[3,7,11,17]])*P]
 phys.extend(zz[j,:] for j in range(2,8))
 def lam(i):return phys[i][:,0:2].T
 if all(s.Matrix.hstack(lam(i-1 if i>1 else 9),lam(i)).det()!=0 for i in range(1,10)):break
else:raise AssertionError('generic_spintwistor_presentation')
def lam(i):return phys[i][:,0:2].T
def mu(i):return phys[i][:,2:4].T
def x(i):
 j=i-1 if i>1 else 9
 return s.Matrix.hstack(mu(j),mu(i))*s.Matrix.hstack(lam(j),lam(i)).inv()
def br(*seq):return s.Matrix.vstack(*(phys[i] for i in seq)).det(method='domain-ge')
X={i:x(i) for i in range(1,10)};epsilon=s.Matrix([[0,1],[-1,0]])
def add_theta(row,i,L):
 j=i-1 if i>1 else 9
 inv=s.Matrix.vstack(lam(j).T,lam(i).T).inv()
 row[j]+=s.factor((L*inv[:,0])[0]);row[i]+=s.factor((L*inv[:,1])[0])
def rows_for_history(h):
 a1,b1=h.outer_pair;a,b=h.inner_pair
 outer={i:s.S.Zero for i in range(1,10)}
 seq=(9,a1-1,a1,b1-1,b1)
 for k,p in enumerate(seq):outer[p]=br(*(seq[(k+j)%5] for j in range(1,5)))
 inner={i:s.S.Zero for i in range(1,10)}
 if h.branch=='left-nested':
  anchor=a1
  xi=lam(9).T*(X[9]-X[b1]).T*epsilon*(X[b1]-X[a1])
  def factor(a,b):return xi*epsilon*(X[anchor]-X[a]).T*epsilon*(X[a]-X[b])*epsilon
 else:
  anchor=9
  def factor(a,b):return lam(9).T*(X[9]-X[a]).T*epsilon*(X[a]-X[b])*epsilon
 L1,L2=factor(a,b),factor(b,a)
 add_theta(inner,b,L1);add_theta(inner,a,L2);add_theta(inner,anchor,-L1-L2)
 return outer,inner
def pair(A,B,p,q):return s.factor(A[p]*B[q]-A[q]*B[p])
hist=compile_nnmhv_histories(9);assert len(hist)==50
rowdata=[];active={};zero=[];fermionic_rows={}
for index,h in enumerate(hist):
 A,B=rows_for_history(h);fermionic_rows[index]=(A,B)
 vector=tuple(pair(A,B,3,p) for p in (1,2,4,5,6,7,8,9))
 if all(v==0 for v in vector):zero.append(index);continue
 pivot=next(v for v in vector if v!=0)
 normalized=tuple(s.factor(v/pivot) for v in vector)
 active.setdefault(normalized,[]).append(index)
 rowdata.append({'history_index':index,'first_nonzero_label3_partner':next(p for p,v in zip((1,2,4,5,6,7,8,9),vector) if v!=0),
                 'normalized_label3_pair_vector':[str(v) for v in normalized]})
# Independently calibrated ordinary history9 and transported history27.
A9,B9=rows_for_history(hist[9]); A27,B27=rows_for_history(hist[27])
local=(1,2,4,5,6,7,8,9)
def r(A,B):return s.factor(pair(A,B,local[1],local[5])/pair(A,B,local[0],local[4]))
def localbr(*seq):return z[[i-1 for i in seq],:].det(method='domain-ge')
ordinary_ratio=localbr(3,4,8,1)*localbr(7,8,4,5)/(localbr(2,3,4,8)*localbr(6,7,8,4))
assert r(A9,B9)==ordinary_ratio
assert r(A27,B27)==s.Rational(calibrated.rows[witness_index]['transported_pair_ratio'])
assert all(3 not in screen['all_history_records'][i]['explicit_endpoint_envelope'] for i in zero)
groups=[indices for indices in active.values() if len(indices)>1]
singletons=[indices[0] for indices in active.values() if len(indices)==1]
# The chi3^4 sector is (sum_p beta_(3,p) chi_p)^4 in the four SU(4)
# flavors. Certify independence of ALL distinct fourth powers via an
# 18x18 nonzero minor of their Sym^4(8) coefficient matrix mod prime.
prime=1000003
rays=list(active)
def residue(r):
 r=s.Rational(r);den=int(s.denom(r))%prime
 assert den!=0
 return int(s.numer(r))%prime*pow(den,-1,prime)%prime
vectors=[[residue(v) for v in ray] for ray in rays]
basis={};chosen=[]
for monomial in itertools.combinations_with_replacement(range(8),4):
 column=[s.prod(vector[j] for j in monomial)%prime for vector in vectors]
 for pivot,old in sorted(basis.items()):
  if column[pivot]:
   coeff=column[pivot]
   column=[(w-coeff*u)%prime for w,u in zip(column,old)]
 pivot=next((j for j,v in enumerate(column) if v),None)
 if pivot is None:continue
 inverse=pow(int(column[pivot]),-1,prime)
 basis[pivot]=[(v*inverse)%prime for v in column]
 chosen.append(monomial)
 if len(basis)==len(rays):break
assert len(basis)==len(rays)==18
if witness_index:
 first=json.loads((OUT/'nine-point-label3-history-cancellation-rank.json').read_text())
 assert first['repeated_label3_pair_rays']==groups
 assert first['singleton_label3_ray_history_indices']==singletons
report={'schema':'marici.nima.nine-point-label3-history-cancellation-rank.v1','passed':True,
 'witness_index':witness_index,
 'authored_history_count':len(hist),'label3_inactive_history_indices':zero,
 'label3_active_history_count':len(rowdata),
 'distinct_label3_fourth_power_rays':len(active),
 'repeated_label3_pair_rays':groups,'singleton_label3_ray_history_indices':singletons,
 'fourth_power_independence_certificate':{'prime':prime,'rank':len(basis),
  'selected_monomial_column_indices':[list(t) for t in chosen],
  'meaning':'Nonzero 18x18 minor modulo prime certifies rational independence of 18 distinct chi3^4 rays.'},
 'calibration_history9_ordinary_and_history27_transported_pair_ratios':True,
 'two_witness_grouping_consistency_control':True if witness_index else 'rerun with NIMA_LABEL3_WITNESS_INDEX=1',
 'claim':'At this exact generic witness, all 41 label3-active histories occupy only 18 rays in the chi3^4 sector, and these 18 fourth-power rays are linearly INDEPENDENT over Q by a modular minor certificate. Hence any scalar-weighted combination cancelling ALL chi3 dependence must first have zero net coefficient independently within EACH ray group. Twelve singleton-ray histories individually have zero coefficient in such a combination; each of six repeated-ray groups is a necessary potential cancellation block, but its full mixed-chi3 tensor may not cancel.',
 'claim_boundary':'One exact rational witness plus ordinary history9 and corrected transported history27 calibrations; generic exclusion of singleton histories assumes scalar weights regular at this witness (a rational identity can be checked at additional generic witnesses). Grouping is only a necessary chi3^4 condition, not a found full-flavor cancellation, bosonic normalization, or full amplitude equality.'}
filename='nine-point-label3-history-cancellation-rank'+('-witness2' if witness_index else '')+'.json'
(OUT/filename).write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'active':len(rowdata),'inactive':len(zero),
 'distinct_rays':len(active),'repeat_groups':groups},indent=2))
