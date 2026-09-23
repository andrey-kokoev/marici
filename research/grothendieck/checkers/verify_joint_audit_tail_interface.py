"""Independent expected-state/query and exact certificate replay.
Imports neither the joint engine, a greedy constructor, nor an optimizer.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,gzip,hashlib,copy
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dot(a,b):return sum(x*y for x,y in zip(a,b))
r=json.loads(gzip.decompress((R/'joint-audit-tail-interface.json.gz').read_bytes()));cp=R/'joint-audit-tail-interface-contract.json';contract=load(cp)
for p,h in r['bindings'].items():assert sha(Path(p))==h
assert sha(cp)==r['contract_sha256'] and sha(R/'two-moment-tail-complexity.json')==contract['source_sha256']

def schema(index):
 plan=contract['plans'][index];m=plan['m'];audits=plan['audits'];d=2+len(audits);free=[j for j in range(m) if j not in audits]
 caps=[Q(100+2*j) for j in range(m)];slopes=[Q(1,128**j) for j in range(m)]
 def pull(a):return [a[0]+a[1]*slopes[j]+(a[2+audits.index(j)] if j in audits else 0) for j in range(m)]
 def bound(a):return sum(b*max(Q(0),v) for b,v in zip(caps,pull(a)))
 def shear(a,b):return tuple([a,b]+[-a-b*slopes[j] for j in audits])
 D={}
 for k,j in enumerate(audits):
  for sign in (-1,1):
   a=tuple(Q(sign if i==k+2 else 0) for i in range(d));D[f'audit:{j}:{sign}']=(a,bound(a))
 if len(free)>=2:
  for j in free:
   for sign in (-1,1):
    a=shear(-sign*slopes[j],Q(sign));D[f'edge:{j}:{sign}']=(a,bound(a))
 if free:
  for sign in (-1,1):
   a=shear(Q(sign),Q(0));D[f'mass:{sign}']=(a,bound(a))
 if len(free)==1:
  for sign in (-1,1):D[f'equality:{sign}']=(shear(-sign*slopes[free[0]],Q(sign)),Q(0))
 elif not free:
  for j in (0,1):
   for sign in (-1,1):D[f'equality:{j}:{sign}']=(shear(Q(sign if j==0 else 0),Q(sign if j==1 else 0)),Q(0))
 assert len(D)==2*m+(4 if not free else 2)
 return plan,m,audits,d,caps,slopes,bound,D

def lift(point,raw,m,audits,caps,slopes):
 t=tuple(map(Q,raw));assert len(t)==m and all(0<=a<=b for a,b in zip(t,caps))
 assert point==(sum(t),dot(slopes,t),*[t[j] for j in audits])

def verify_answer(si,qi,answer,reset=False):
 plan,m,audits,d,caps,slopes,bound,D=schema(si);query=plan['queries'][qi];frames=[(tuple(map(Q,f['normal'])),Q(f['upper'])) for f in query['frames']]
 if reset:frames=frames[-1:]
 objective=tuple(map(Q,query['objective']));expected=[]
 for j in range(d):
  for sign in (-1,1):
   a=tuple(Q(sign if i==j else 0) for i in range(d));expected.append((a,bound(a),f'box:{j}:{sign}'))
 expected += [(a,b,f'frame:{i}') for i,(a,b) in enumerate(frames)]
 used=set()
 for step in answer['trace']:
  p=tuple(map(Q,step['candidate']));name=step['cut'];assert len(p)==d and all(v>=0 for v in p)
  assert all(dot(a,p)<=b for a,b,label in expected)
  assert name in D and name not in used;a,b=D[name];assert dot(a,p)>b;used.add(name);expected.append((a,b,name))
 if answer['rows'][-1]['label']=='support:objective':expected.append((objective,bound(objective),'support:objective'))
 rows=[(tuple(map(Q,f['normal'])),Q(f['upper']),f['label']) for f in answer['rows']];assert rows==expected
 assert answer['dictionary_size']==len(D) and len(used)<=len(D)
 y=list(map(Q,answer['multipliers']));assert len(y)==len(rows) and all(a>=0 for a in y)
 normal=tuple(sum(y[i]*rows[i][0][j] for i in range(len(rows))) for j in range(d));rhs=sum(y[i]*rows[i][1] for i in range(len(rows)))
 if answer['status']=='INCONSISTENT':assert all(v>=0 for v in normal) and rhs<0
 else:
  assert answer['status']=='OPTIMUM';p=tuple(map(Q,answer['point']));assert all(v>=0 for v in p)
  lift(p,answer['source_lift'],m,audits,caps,slopes)
  assert all(dot(a,p)<=b for a,b in frames) and all(a>=b for a,b in zip(normal,objective))
  assert rhs==dot(objective,p)==Q(answer['value'])

expected_queries={(si,qi) for si,p in enumerate(contract['plans']) for qi in range(len(p['queries']))}
assert len(r['queries'])==len(expected_queries) and {(c['schema_index'],c['query_index']) for c in r['queries']}==expected_queries
assert len(r['reset_controls'])==len(contract['plans']) and {c['schema_index'] for c in r['reset_controls']}==set(range(len(contract['plans'])))
assert len(r['state_membership'])==3*len(expected_queries)
for case in r['queries']:
 verify_answer(case['schema_index'],case['query_index'],case['answer'])
 assert (case['answer']['status']=='INCONSISTENT')==(case['query_index']==3)
for case in r['reset_controls']:
 verify_answer(case['schema_index'],3,case['answer'],True);assert case['answer']['status']=='OPTIMUM'
for case in r['membership']:
 plan,m,audits,d,caps,slopes,bound,D=schema(case['schema_index']);p=tuple(map(Q,case['point']));a=case['answer']
 if 'lift' in a:lift(p,a['lift'],m,audits,caps,slopes)
 else:n,b=D[a['cut']];assert dot(n,p)>b
for case in r['state_membership']:
 plan,m,audits,d,caps,slopes,bound,D=schema(case['schema_index']);p=tuple(map(Q,case['point']));a=case['answer'];frames=[(tuple(map(Q,f['normal'])),Q(f['upper'])) for f in plan['queries'][case['query_index']]['frames']]
 if a['status']=='EXCLUDED_FRAME':n,b=frames[a['frame_index']];assert dot(n,p)>b
 else:
  assert all(dot(n,p)<=b for n,b in frames)
  if a['status']=='ADMITTED_POINT':lift(p,a['lift'],m,audits,caps,slopes)
  else:assert a['status']=='EXCLUDED_SOURCE';n,b=D[a['cut']];assert dot(n,p)>b
# Expected states come from the frozen contract, not the response. A valid
# certificate for a reset history is not acceptable for the original prefix.
case=r['reset_controls'][0]
try:verify_answer(case['schema_index'],3,case['answer'],False)
except AssertionError:pass
else:raise AssertionError('dropped prior frames accepted')
case=r['queries'][0];bad=copy.deepcopy(case['answer']);bad['source_lift'][0]='-1'
try:verify_answer(case['schema_index'],case['query_index'],bad)
except AssertionError:pass
else:raise AssertionError('corrupted source lift accepted')
def rejects(si,qi,answer):
 try:verify_answer(si,qi,answer)
 except (AssertionError,KeyError,IndexError):return
 raise AssertionError('invalid statement/certificate accepted')
# Same point/packet under another independently expected schema or query.
rejects(1,0,r['queries'][0]['answer'])
rejects(0,1,r['queries'][0]['answer'])
bad=copy.deepcopy(r['queries'][0]['answer']);bad['value']=str(Q(bad['value'])+1);rejects(0,0,bad)
bad=copy.deepcopy(r['queries'][0]['answer']);bad['multipliers'][-1]='-1';rejects(0,0,bad)
case=next(c for c in r['queries'] if c['answer']['trace']);bad=copy.deepcopy(case['answer'])
label=bad['trace'][0]['cut'];row=next(row for row in bad['rows'] if row['label']==label);row['normal'][0]=str(Q(row['normal'][0])+1)
rejects(case['schema_index'],case['query_index'],bad)
print('PASS: variable-audit dictionaries, finite cut progress, expected-history binding, exact primal/dual/Farkas certificates, 499 base/state membership checks and seven reset/corruption controls')
