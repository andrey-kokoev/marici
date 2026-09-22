"""Exact independent replay of persistent-frame, primal/dual and Farkas packets.
No optimizer or producer module is imported.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,copy
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(obj):return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()
c=load(R/'coherent-tail-refinement-contract.json');context=digest(c['context'])
def verify_stage(stage):
 state=stage['state'];result=stage['result'];assert state['context']==context
 prefix={'context':context,'frames':[]}
 rows=[]
 for frame in state['frames']:
  assert frame['context']==context and frame['parent']==digest(prefix)
  rows+=frame['rows'];prefix={'context':context,'frames':prefix['frames']+[frame]}
 assert digest(state)==result['state_digest']
 m=max([1]+[int(n) for row in rows for n in row['coefficients']]);assert m==result['horizon']
 A=[[Q(int(i==j)) for j in range(m)] for i in range(m)];b=[Q(1)]*m
 for row in rows:
  assert all(int(n)>=1 for n in row['coefficients'])
  A.append([Q(row['coefficients'].get(str(j+1),'0')) for j in range(m)]);b.append(Q(row['upper']))
 if result['status']=='EVIDENCE_CONSISTENCY_FAILURE':
  y=list(map(Q,result['farkas']));assert len(y)==len(b) and all(t>=0 for t in y)
  assert all(sum(A[i][j]*y[i] for i in range(len(b)))>=0 for j in range(m))
  assert sum(a*z for a,z in zip(b,y))<0
  return
 x=list(map(Q,result['primal']));y=list(map(Q,result['dual']));assert len(x)==m and len(y)==len(b)
 assert all(t>=0 for t in x+y)
 assert all(sum(a*z for a,z in zip(row,x))<=bound for row,bound in zip(A,b))
 assert all(sum(A[i][j]*y[i] for i in range(len(b)))>=Q(1,2**(j+1)) for j in range(m))
 value=-sum(t/2**(j+1) for j,t in enumerate(x));assert value==-sum(a*z for a,z in zip(b,y))==Q(result['finite_optimum'])
 eps=Q(1,2**m);assert eps==Q(result['tail_error']) and result['infinite_primal_tail']==1
 # Frame supports are <=m; the constant-one suffix satisfies the entire
 # infinite ambient box and exactly contributes -eps by the geometric sum.
 infimum=value-eps;assert infimum==Q(result['infinite_optimum'])
 status='UNIVERSAL_THRESHOLD_SEPARATION' if infimum>Q(result['threshold']) else 'ADMITTED_COUNTEREXAMPLE'
 assert status==result['status']
def verify_chain(stages,expected=None):
 for i,s in enumerate(stages):
  verify_stage(s)
  if i:
   assert s['state']['frames'][:-1]==stages[i-1]['state']['frames']
   if expected is not None:assert s['state']['frames'][-1]['rows']==expected[i-1]
   old=stages[i-1]['result'];new=s['result']
   if old['status']!='EVIDENCE_CONSISTENCY_FAILURE' and new['status']!='EVIDENCE_CONSISTENCY_FAILURE':assert Q(old['infinite_optimum'])<=Q(new['infinite_optimum'])
r=load(R/'coherent-tail-refinement.json');assert r['contract_sha256']==sha(R/'coherent-tail-refinement-contract.json')
for p,h in r['bindings'].items():assert sha(Path(p))==h
for name,stages in r['scenarios'].items():verify_chain(stages,c['scenarios'][name])
for s in r['isolated_switch_frames']:verify_stage(s);assert s['result']['status']!='EVIDENCE_CONSISTENCY_FAILURE'
assert r['scenarios']['witness_switching'][-1]['result']['status']=='EVIDENCE_CONSISTENCY_FAILURE'
assert r['scenarios']['separation'][-1]['result']['status']=='UNIVERSAL_THRESHOLD_SEPARATION'
verify_chain(r['equality_boundary'])
for n,s in enumerate(r['equality_boundary'],1):assert Q(s['result']['infinite_optimum'])==-Q(1,2**n)<0
verify_stage(r['reverse_separation']);assert r['reverse_separation']['result']['infinite_optimum']==r['scenarios']['separation'][-1]['result']['infinite_optimum']
# Explicitly demonstrate that a current minimizing point need not persist:
# preserving the feasible set is different from committing to its optimizer.
a,b=r['scenarios']['noncommitted_optimizer'][1:]
assert a['result']['primal'][0]=='1' and b['result']['primal'][0]=='0'
# Corrupt a Farkas packet; an empty claim without a certificate must fail.
bad=copy.deepcopy(r['scenarios']['witness_switching'][-1]);bad['result']['farkas']=['0']*len(bad['result']['farkas'])
try:verify_stage(bad)
except AssertionError:pass
else:raise AssertionError('false inconsistency certificate accepted')
# Dropping a frame is detectable relative to the supplied prior state even
# if local envelope digests are recomputed. Hashes alone do not prove history.
verify_stage(r['reset_second_frame'])  # individually valid, including new digests and LP packet
badchain=copy.deepcopy(r['scenarios']['separation']);badchain[-1]=r['reset_second_frame']
try:verify_chain(badchain,c['scenarios']['separation'])
except AssertionError:pass
else:raise AssertionError('reset evidence fiber accepted')
assert set(r['rejected_frames'])=={'foreign','stale_parent'}
print('PASS: persistent conjunctions, primal/dual separation, Farkas inconsistency, separately admitted switching control, equality boundary, optimizer noncommitment, and corruption controls')
