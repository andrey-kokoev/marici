"""Research integration of owning migration certificates and capability checks.
Importing the owning research verifier replays its frozen artifact checks.
This is not a hardened API or a security boundary.
"""
from pathlib import Path
from fractions import Fraction as Q
from dataclasses import dataclass,replace
import sys,json,hashlib
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/grothendieck/checkers'))
from verify_audit_elimination import verify_case,verify_lp,source,dec
from joint_audit_tail_interface import JointAuditModel

def freeze(x):return json.dumps(x,sort_keys=True,separators=(',',':'))
def digest(x):return hashlib.sha256(freeze(x).encode()).hexdigest()
@dataclass(frozen=True)
class RetiredState:
 runtime_json:str
 migration_binding:str
 public_frames:tuple=()
 lift_json:str|None=None
 archive_json:str|None=None
 def descriptor(self):
  return {'runtime':json.loads(self.runtime_json),'migration_binding':self.migration_binding,
   'public_frames':[{'normal':list(map(str,a)),'upper':str(b)} for a,b in self.public_frames],
   'capabilities':{'lift':self.lift_json is not None,'reexpose':self.archive_json is not None}}
 def refine(self,a,b):
  d=2+len(json.loads(self.runtime_json)['audits'])
  if len(a)!=d:raise ValueError('NONPUBLIC_FRAME')
  return replace(self,public_frames=self.public_frames+((tuple(map(Q,a)),Q(b)),))
 def maximize(self,a):
  expected=self.descriptor();runtime=expected['runtime'];a=tuple(map(Q,a))
  if len(a)!=2+len(runtime['audits']):raise ValueError('NONPUBLIC_QUERY')
  frames=list(map(dec,runtime['frames']))+list(self.public_frames)
  proof=JointAuditModel(runtime['m'],runtime['audits']).maximize(frames,a)
  packet={'state':expected,'objective':list(map(str,a)),'proof':proof}
  verify_answer(expected,list(map(str,a)),packet)
  return packet
 def fine_lift(self,point):
  if self.lift_json is None:raise PermissionError('NO_FINE_LIFT_CAPABILITY')
  context=json.loads(self.lift_json);plan=context['plan'];fine=[dec(r) for r in context['rows']]
  runtime=json.loads(self.runtime_json);point=tuple(map(Q,point));d=2+len(runtime['audits'])
  if len(point)!=d:raise ValueError('NONPUBLIC_POINT')
  if not all(sum(a*x for a,x in zip(n,point))<=b for n,b in list(map(dec,runtime['frames']))+list(self.public_frames)):raise ValueError('EXCLUDED_PUBLIC_POINT')
  if JointAuditModel(runtime['m'],runtime['audits']).source_lift(point) is None:raise ValueError('OUTSIDE_SOURCE')
  k=2+plan['audits'].index(plan['retire'])
  lo=[];hi=[]
  for a,b in fine:
   rhs=b-sum(v*x for v,x in zip(a[:k]+a[k+1:],point))
   if a[k]<0:lo.append(rhs/a[k])
   elif a[k]>0:hi.append(rhs/a[k])
   elif rhs<0:raise ValueError('EMPTY_FINE_FIBER')
  lower,upper=max(lo),min(hi);assert lower<=upper
  joint=point[:k]+((lower+upper)/2,)+point[k:]
  t=JointAuditModel(plan['m'],plan['audits']).source_lift(joint);assert t is not None
  assert all(sum(v*x for v,x in zip(a,joint))<=b for a,b in fine)
  return t
 def reexpose(self):
  if self.archive_json is None:raise PermissionError('NO_FINE_ARCHIVE')
  plan=json.loads(self.archive_json);k=2+plan['audits'].index(plan['retire'])
  for a,b in self.public_frames:plan['frames'].append({'normal':list(map(str,a[:k]+(Q(0),)+a[k:])),'upper':str(b)})
  return plan

def migrate(expected_plan,case,*,retain_lift=False,retain_archive=False):
 # Verify before constructing any runtime object; copy inputs by serialization.
 verify_case(expected_plan,case)
 plan=json.loads(freeze(expected_plan));lift=None
 if retain_lift:
  base,*_=source(plan['m'],plan['audits']);rows=base+list(map(dec,plan['frames']))
  lift=freeze({'plan':plan,'rows':[{'normal':list(map(str,a)),'upper':str(b)} for a,b in rows]})
 return RetiredState(freeze(case['runtime']),digest({'expected':plan,'case':case}),
  lift_json=lift,archive_json=freeze(plan) if retain_archive else None)
def verify_answer(expected_state,expected_objective,packet):
 assert packet['state']==expected_state and packet['objective']==expected_objective
 r=expected_state['runtime'];frames=list(map(dec,r['frames']))+list(map(dec,expected_state['public_frames']))
 c=tuple(map(Q,expected_objective));assert len(c)==2+len(r['audits'])
 verify_lp(r['m'],r['audits'],frames,c,packet['proof'])
