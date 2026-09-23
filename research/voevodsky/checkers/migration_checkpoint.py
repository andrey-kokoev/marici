"""Owning migration-gated process-local retirement sessions.
Point-witness reuse, not a certified domain-wide section cache.
"""
from threading import RLock
from uuid import uuid4
from fractions import Fraction as Q
import json
from checked_retirement_interface import migrate,freeze,verify_answer,source,dec

class Session:
 def __init__(self):
  self._lock=RLock();self._state=None;self._handle=None;self._witnesses={}
  self._work={'migration_checks':0,'answer_checks':0,'fine_witness_checks':0,'fine_witness_hits':0}
 def _current(self,handle):
  if self._state is None or handle!=self._handle:raise ValueError('STALE_OR_FOREIGN')
 def _receipt(self):
  state=self._state
  return {'handle':self._handle,'state':state.descriptor(),'work':dict(self._work),
   'bytes':{'live_descriptor':len(freeze(state.descriptor()).encode()),
    'lift_context':len((state.lift_json or '').encode()),'archive':len((state.archive_json or '').encode()),
    'cached_point_witnesses':sum(len(freeze([p,t]).encode()) for p,t in self._witnesses.items())}}
 def bootstrap(self,expected_plan,case,*,retain_lift=False,retain_archive=False):
  with self._lock:
   if self._state is not None:raise ValueError('ALREADY_BOOTSTRAPPED')
   # Caller snapshots precede checking and publication. Failure publishes nothing.
   plan=json.loads(freeze(expected_plan));packet=json.loads(freeze(case))
   state=migrate(plan,packet,retain_lift=retain_lift,retain_archive=retain_archive)
   self._state=state;self._handle=uuid4().hex;self._work['migration_checks']+=1
   return self._receipt()
 def advance(self,handle,expected_before,operation,expected_objective,answer):
  with self._lock:
   self._current(handle);assert expected_before==self._state.descriptor()
   op=json.loads(freeze(operation));packet=json.loads(freeze(answer))
   if set(op)!={'kind','normal','upper'} or op['kind']!='append-public':raise PermissionError('PUBLIC_ONLY')
   state=self._state.refine(op['normal'],op['upper'])
   objective=list(map(str,map(Q,expected_objective)))
   verify_answer(state.descriptor(),objective,packet)
   self._state=state;self._handle=uuid4().hex;self._work['answer_checks']+=1
   # Fine history/source do not change under public-only refinement. Cached
   # witnesses remain locally true, but eligibility MUST be checked per call.
   return self._receipt()
 def fine_lift(self,handle,point):
  with self._lock:
   self._current(handle);state=self._state
   if state.lift_json is None:raise PermissionError('NO_FINE_LIFT_CAPABILITY')
   p=tuple(map(Q,point));runtime=json.loads(state.runtime_json)
   if len(p)!=2+len(runtime['audits']):raise ValueError('NONPUBLIC_POINT')
   frames=list(map(dec,runtime['frames']))+list(state.public_frames)
   if not all(sum(a*x for a,x in zip(n,p))<=b for n,b in frames):raise ValueError('EXCLUDED_POINT')
   key=tuple(map(str,p))
   if key in self._witnesses:
    self._work['fine_witness_hits']+=1;return list(self._witnesses[key])
   t=tuple(state.fine_lift(p));context=json.loads(state.lift_json);plan=context['plan']
   _,_,observe,caps=source(plan['m'],plan['audits']);joint=observe(t)
   assert len(t)==plan['m'] and all(0<=v<=b for v,b in zip(t,caps))
   k=2+plan['audits'].index(plan['retire']);assert joint[:k]+joint[k+1:]==p
   assert all(sum(a*x for a,x in zip(n,joint))<=b for n,b in map(dec,plan['frames']))
   encoded=tuple(map(str,t));self._witnesses[key]=encoded;self._work['fine_witness_checks']+=1
   return list(encoded)
 def reexpose(self,handle):
  with self._lock:self._current(handle);return self._state.reexpose()
