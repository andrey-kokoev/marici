"""One-audit elimination: checked compaction and quadratic facet obstruction."""
from pathlib import Path
from fractions import Fraction as Q
import json,gzip,hashlib
from joint_audit_tail_interface import JointAuditModel,dot
from audit_elimination import compile_projection,extend
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def enc(a,b):return {'normal':list(map(str,a)),'upper':str(b)}
def size(x):return len(json.dumps(x,separators=(',',':')).encode())
plans=[{'name':'forced-zero-tail','m':3,'audits':[0],'retire':0,'frames':[enc((Q(1),Q(0),Q(-1)),Q(0)),enc((Q(-1),Q(0),Q(1)),Q(0)),enc((Q(0),Q(0),Q(1)),Q(1))]},
 {'name':'one-sided-audit-evidence','m':3,'audits':[0],'retire':0,'frames':[enc((Q(0),Q(0),Q(1)),Q(v)) for v in (30,20,10)]},
 {'name':'coupled-surviving-audit','m':4,'audits':[0,1],'retire':0,'frames':[enc((Q(1),Q(0),Q(-1),Q(-1)),Q(4)),enc((Q(0),Q(1),Q(1),Q(-1)),Q(2)),enc((Q(0),Q(0),Q(-1),Q(0)),Q(-1))]}]
plans += [{'name':'all-audits-lower-dimensional','m':2,'audits':[0,1],'retire':0,'frames':[enc((Q(0),Q(0),Q(1),Q(1)),Q(3)),enc((Q(0),Q(0),Q(-1),Q(0)),Q(-1))]}, {'name':'inconsistent-history','m':3,'audits':[0],'retire':0,'frames':[enc((Q(0),Q(0),Q(0)),Q(-1))]}]
contract={'schema':'audit-elimination-contract.v1','plans':plans,'expansion_n':[2,3,4,8,16],'source_binding':sha(HERE/'joint_audit_tail_interface.py'),'scope':'one exact existential audit elimination; linear evidence on owning relaxed source; public source generator retained'}
cp=R/'audit-elimination-contract.json';cp.write_text(json.dumps(contract,indent=2)+'\n');results=[]
for plan in plans:
 fine=JointAuditModel(plan['m'],plan['audits']);index=2+fine.audits.index(plan['retire']);rows=[]
 for j in range(fine.d):
  for sign in (-1,1):
   a=tuple(Q(sign if k==j else 0) for k in range(fine.d));rows.append((a,fine.bound(a)))
 rows+=list(dict(fine.cuts()).values());rows += [(tuple(map(Q,f['normal'])),Q(f['upper'])) for f in plan['frames']]
 answer=compile_projection(rows,index)
 coarse=JointAuditModel(plan['m'],[j for j in fine.audits if j!=plan['retire']]);summary=[];base=[]
 for i,row in enumerate(answer['rows']):
  a=tuple(map(Q,row['normal']));b=Q(row['upper']);support=coarse.bound(a)
  if support<=b:base.append({'row':i,'source_support':str(support)})
  else:summary.append(enc(a,b))
 runtime={'m':plan['m'],'audits':list(coarse.audits),'frames':summary,'source_binding':contract['source_binding']}
 original={k:plan[k] for k in ('m','audits','frames')};original['source_binding']=contract['source_binding']
 queries=[]
 for j in range(coarse.d):
  c=tuple(Q(int(k==j)) for k in range(coarse.d));old_c=c[:index]+(Q(0),)+c[index:]
  old=fine.maximize(tuple((tuple(map(Q,f['normal'])),Q(f['upper'])) for f in plan['frames']),old_c)
  new=coarse.maximize(tuple((tuple(map(Q,f['normal'])),Q(f['upper'])) for f in summary),c)
  assert old['status']==new['status']
  if new['status']=='INCONSISTENT':
   queries.append({'objective':list(map(str,c)),'status':'INCONSISTENT','fine_certificate':old,'coarse_certificate':new});continue
  assert old['value']==new['value']
  public=tuple(map(Q,new['point']));extended,interval=extend(rows,index,public);lift=fine.source_lift(extended);assert lift is not None
  queries.append({'objective':list(map(str,c)),'value':old['value'],'public':list(map(str,public)),'extension_interval':list(map(str,interval)),'fine_point':list(map(str,extended)),'source_lift':list(map(str,lift)),'fine_certificate':old,'coarse_certificate':new})
 result={'name':plan['name'],'projection':answer,'runtime':runtime,'base_implied_rows':base,'queries':queries,'ledger':{'fine_materialized_rows':len(rows),'fine_frame_rows':len(plan['frames']),'runtime_frame_rows':len(summary),'old_runtime_bytes':size(original),'new_runtime_bytes':size(runtime),'projection_proof_bytes':size(answer)}}
 results.append(result)
# A four-dimensional inner box of the owning m=4, audits={0,1} image.
# Fine normalized variables are (x,y,H,z); retire H (atom 0), keep z (atom 1).
model=JointAuditModel(4,(0,1));center=model.observe(tuple(b/2 for b in model.caps));delta=Q(1,128**4)
from itertools import product
corners=[]
for local in product((-1,1),(-1,1),(-4,4),(-4,4)):
 joint=tuple(a+delta*b for a,b in zip(center,local));t=model.source_lift(joint);assert t is not None
 corners.append({'local':list(map(str,local)),'joint':list(map(str,joint)),'source_lift':list(map(str,t))})
expansions=[]
for n in contract['expansion_n']:
 knots=[Q(2*i+1-n,n) for i in range(n)];facets=[];witnesses=[]
 for i,a in enumerate(knots):
  for j,b in enumerate(knots):
   facets.append(enc((2*a,2*b,Q(-1)),a*a+b*b))
   # Strictly violates only this pair facet; all box walls remain strict.
   gap=Q(2,n*n);p=(a,b,a*a+b*b-gap)
   assert dot((2*a,2*b,Q(-1)),p)>a*a+b*b
   witnesses.append(list(map(str,p)))
 for i,p in enumerate(witnesses):
  point=tuple(map(Q,p))
  assert all(dot(tuple(map(Q,f['normal'])),point)<=Q(f['upper']) for j,f in enumerate(facets) if i!=j)
  assert -1<point[0]<1 and -1<point[1]<1 and -4<point[2]<4
 expansions.append({'n':n,'knots':list(map(str,knots)),'projected_pair_facets':facets,'exclusive_violation_witnesses':witnesses,'fine_evidence_rows':2*n+8,'projected_facets':n*n+5})
out={'schema':'audit-elimination-result.v1','contract_sha256':sha(cp),'compactions':results,'expansion':{'m':4,'audits':[0,1],'retire':0,'center':list(map(str,center)),'delta':str(delta),'inner_box_corners':corners,'families':expansions},'bindings':{str(p):sha(p) for p in (Path(__file__),HERE/'audit_elimination.py',HERE/'joint_audit_tail_interface.py',cp)},'status':'ONE_AUDIT_EXACT_PROJECTION_WITH_CHECKABLE_COMPACTION_AND_QUADRATIC_FACET_OBSTRUCTION'}
(R/'audit-elimination.json.gz').write_bytes(gzip.compress(json.dumps(out,separators=(',',':')).encode(),mtime=0))
for case in results:print(case['name'],case['ledger'])
print('quadratic families',[(e['n'],e['projected_facets']) for e in expansions])
