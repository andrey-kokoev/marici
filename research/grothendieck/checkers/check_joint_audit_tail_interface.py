"""Frozen variable-audit refinement tests on the owning tail family."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import json,hashlib,subprocess,sys,gzip
from joint_audit_tail_interface import JointAuditModel,dot
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
subprocess.run([sys.executable,str(HERE/'verify_two_moment_tail_complexity.py')],check=True)
subprocess.run([sys.executable,str(HERE.parents[1]/'nima/checkers/verify_audited_tail_section.py')],check=True)
schemas=[(m,tuple(j for j in range(m) if mask>>j&1)) for m in (2,3) for mask in range(2**m)]
schemas += [(4,a) for a in ((),(0,),(0,3),(0,1,2),(0,1,2,3))]+[(8,(0,4,7)),(16,(0,15))]
def encrow(a,b):return {'normal':list(map(str,a)),'upper':str(b)}
plans=[]
for m,audits in schemas:
 model=JointAuditModel(m,audits);d=model.d;center=model.observe(tuple(v/2 for v in model.caps));total=sum(model.caps)
 unit=lambda j,sign=1:tuple(Q(sign if i==j else 0) for i in range(d))
 coupled=tuple(Q(int(i==1)+int(bool(audits) and i==2)) for i in range(d))
 f1=(unit(0),total/2);f2=(coupled,dot(coupled,center));f3=(unit(0,-1),-3*total/4)
 objective=tuple(Q(-int(i==0)+2*int(i==1)+3*int(bool(audits) and i==2)) for i in range(d))
 # All plans and thresholds are specified before optimization.
 plans.append({'m':m,'audits':list(audits),'queries':[{'frames':[],'objective':list(map(str,unit(1)))},{'frames':[encrow(*f1)],'objective':list(map(str,objective))},{'frames':[encrow(*f1),encrow(*f2)],'objective':list(map(str,objective))},{'frames':[encrow(*f1),encrow(*f2),encrow(*f3)],'objective':list(map(str,unit(1)))}]})
contract={'schema':'joint-audit-tail-interface-contract.v1','plans':plans,'source_sha256':sha(R/'two-moment-tail-complexity.json'),'frames':'arbitrary rational joint moment/audit halfspaces; pin values are variable coordinates unless constrained by frames','backend':'finite streamed shear dictionary, exact bounded outer LP, independently checked primal/dual or Farkas certificates','scope':'Prototype for the owning relaxed boxes; no authenticated evidence admission, noisy-source inference or physical action authorization.'}
cp=R/'joint-audit-tail-interface-contract.json';cp.write_text(json.dumps(contract,indent=2)+'\n')
results=[];membership=[];state_membership=[]
for si,plan in enumerate(plans):
 model=JointAuditModel(plan['m'],plan['audits']);D=dict(model.cuts());q=len(model.free);k=len(model.audits)
 assert len(D)==model.dictionary_size()<=2*model.m+4
 for qi,query in enumerate(plan['queries']):
  frames=tuple((tuple(map(Q,f['normal'])),Q(f['upper'])) for f in query['frames']);objective=tuple(map(Q,query['objective']))
  result=model.maximize(frames,objective)
  if qi==3:assert result['status']=='INCONSISTENT'
  else:assert result['status']=='OPTIMUM'
  results.append({'schema_index':si,'query_index':qi,'answer':result})
  for source_point in (tuple(Q(0) for _ in model.caps),tuple(v/2 for v in model.caps),tuple(model.caps)):
   point=model.observe(source_point)
   state_membership.append({'schema_index':si,'query_index':qi,'point':list(map(str,point)),'answer':model.member(frames,point)})
 # Every supplied joint point is checked with one schema-specific dictionary.
 samples=[tuple(v/3 for v in model.caps),tuple(Q(0) for _ in model.caps),tuple(model.caps)]
 if model.m<=4:samples+=list(product(*[(Q(0),v) for v in model.caps]))
 for t in samples:
  point=model.observe(t);answer=model.oracle(point);assert 'lift' in answer
  membership.append({'schema_index':si,'point':list(map(str,point)),'answer':answer})
 outside=[tuple([Q(0),Q(1)]+[Q(0)]*k),tuple([Q(-1),Q(0)]+[Q(0)]*k)]
 if k:outside.append(tuple([Q(0),Q(0),model.caps[model.audits[0]]+1]+[Q(0)]*(k-1)))
 for point in outside:
  answer=model.oracle(point);assert 'cut' in answer;membership.append({'schema_index':si,'point':list(map(str,point)),'answer':answer})
# Persistent conjunction versus resetting: the last mass lower bound alone
# is feasible, whereas its complete independently specified prefix is empty.
reset=[]
for si,plan in enumerate(plans):
 model=JointAuditModel(plan['m'],plan['audits']);query=plan['queries'][-1];f=query['frames'][-1]
 answer=model.maximize(((tuple(map(Q,f['normal'])),Q(f['upper'])),),tuple(map(Q,query['objective'])))
 assert answer['status']=='OPTIMUM';reset.append({'schema_index':si,'answer':answer})
out={'schema':'joint-audit-tail-interface-result.v1','contract_sha256':sha(cp),'queries':results,'membership':membership,'state_membership':state_membership,'reset_controls':reset,'bindings':{str(p):sha(p) for p in (Path(__file__),HERE/'joint_audit_tail_interface.py',cp,R/'two-moment-tail-complexity.json')},'counts':{'schemas':len(plans),'refined_queries':len(results),'membership':len(membership),'reset_controls':len(reset),'state_membership':len(state_membership),'max_cut_additions':max(len(r['answer']['trace']) for r in results)}}
(R/'joint-audit-tail-interface.json.gz').write_bytes(gzip.compress(json.dumps(out,separators=(',',':')).encode(),mtime=0));print(json.dumps(out['counts'],indent=2))
