"""Independent exact audit-design replay, with no section-engine import."""
from pathlib import Path
from fractions import Fraction as Q
from bisect import bisect_right
import json,hashlib,copy
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
r=load(R/'audit-conditioning-design.json');contract=load(R/'audit-conditioning-design-contract.json')
for p,h in r['bindings'].items():assert sha(Path(p))==h
assert sha(R/'audit-conditioning-design-contract.json')==r['contract_sha256']
def setup(free):
 b=[Q(100+2*j) for j in free];w=[Q(1,128**j) for j in free];C=[Q(0)]
 for cap in b:C.append(C[-1]+cap)
 def high(U):
  k=bisect_right(C,U)-1;remainder=U-C[k]
  v=[cap if i<k else remainder if i==k else Q(0) for i,cap in enumerate(b)]
  return v,sum(a*z for a,z in zip(w,v))
 return b,w,C,high
def check_record(record):
 m=record['m'];mask=record['audit_mask'];free=[j for j in range(m) if mask&(1<<j)==0];assert free==record['free'] and m-len(free)==record['audit_count']
 b,w,C,high=setup(free);T=C[-1];q=len(free)
 if q==0:lo=hi=Q(0);where=None
 elif q==1:lo=hi=1/(1+w[0]);where=None
 else:
  values=[(2/(w[0]-w[-1]),Q(0))];weighted=sum(a*z for a,z in zip(b,w))
  for U in sorted(set(C)|{T-z for z in C}):
   if not 0<U<T:continue
   upper,H=high(U);comp,V=high(T-U);lower=[a-z for a,z in zip(b,comp)];L=weighted-V
   assert H>L
   values.append((sum(abs(a-z) for a,z in zip(upper,lower))/(H-L),U))
  lo,where=max(values);hi=max(lo,1+w[0]*lo)
  if q==2:
   assert lo==2/(w[0]-w[1]);hi=lo
  if free[0]>0:assert hi==lo
 assert Q(record['unavoidable_lower'])==lo and Q(record['greedy_upper'])==hi
 assert record['maximizing_mass_or_tip']==(None if where is None else str(where))
for record in r['records']:check_record(record)
for m in contract['m_values']:
 rows=[s for s in r['records'] if s['m']==m];assert {s['audit_mask'] for s in rows}==set(range(2**m)) and len(rows)==2**m
for summary in r['budgets']:
 m=summary['m'];k=summary['audit_count'];ids=[i for i,s in enumerate(r['records']) if s['m']==m and s['audit_count']==k]
 best=min(ids,key=lambda i:(Q(r['records'][i]['unavoidable_lower']),r['records'][i]['free']));worst=max(ids,key=lambda i:Q(r['records'][i]['unavoidable_lower']))
 assert best==summary['best_record'] and worst==summary['worst_record']
 rec=r['records'][best];assert rec['unavoidable_lower']==summary['design_lower'] and rec['greedy_upper']==summary['design_upper']
 assert Q(summary['design_upper'])<=Q(summary['design_lower'])+1
 if m-k==2:
  assert rec['free']==[0,m-1] and Q(rec['unavoidable_lower'])==2/(1-Q(1,128**(m-1)))
  bad=r['records'][worst];assert bad['free']==[m-2,m-1]
  assert Q(bad['unavoidable_lower'])/Q(rec['unavoidable_lower'])==Q(128**(m-1)-1,127)
for case in r['runtime_controls']:
 rec=r['records'][case['record']];m=rec['m'];free=rec['free'];section=case['section'];point=tuple(map(Q,case['point']));lift=list(map(Q,case['source_lift']))
 pins={j:Q(h) for j,h in section['pins']};assert set(pins)==set(range(m))-set(free)
 assert all(h==Q(100+2*j,3) for j,h in pins.items())
 assert all(0<=v<=100+2*j for j,v in enumerate(lift)) and all(lift[j]==h for j,h in pins.items())
 assert sum(lift)==point[0] and sum(v*Q(1,128**j) for j,v in enumerate(lift))==point[1]
 offset=(sum(pins.values()),sum(h*Q(1,128**j) for j,h in pins.items()));assert tuple(map(Q,section['offset']))==offset
 residual=(point[0]-offset[0],point[1]-offset[1]);assert tuple(map(Q,section['residual_point']))==residual
 b,w,C,high=setup(free);upper,H=high(residual[0]);comp,V=high(C[-1]-residual[0]);lower=[a-z for a,z in zip(b,comp)];L=sum(a*z for a,z in zip(b,w))-V
 answer=section['residual_membership'];assert answer['admitted'] and tuple(map(Q,answer['vertical_bounds']))==(L,H)
 theta=(residual[1]-L)/(H-L) if H!=L else Q(0);assert Q(answer['lift']['theta'])==theta
 assert [lift[j] for j in free]==[(1-theta)*a+theta*z for a,z in zip(lower,upper)]
control=r['nonmonotonicity'];before=r['records'][control['before_record']];after=r['records'][control['after_record']]
assert before['m']==after['m']==3 and before['audit_mask']==0 and after['audit_mask']==1
assert Q(after['unavoidable_lower'])>Q(before['greedy_upper'])
assert Q(control['strict_ratio_lower'])==Q(after['unavoidable_lower'])/Q(before['greedy_upper'])
bad=copy.deepcopy(after);bad['unavoidable_lower']=str(Q(bad['unavoidable_lower'])/2)
try:check_record(bad)
except AssertionError:pass
else:raise AssertionError('understated unavoidable conditioning accepted')
print('PASS:',len(r['records']),'audit sets,',len(r['budgets']),'optimal vertical designs,',len(r['runtime_controls']),'actual conditional lifts; nonmonotonicity and closed two-free optimum')
