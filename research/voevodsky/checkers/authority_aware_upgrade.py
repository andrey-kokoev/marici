"""Trusted-process authority prototype for a fixed two-history retirement.
The owner supplies actual history BEFORE retirement. No serialized provenance
import, observation authentication, or general migration-compiler claim.
"""
from threading import RLock
from uuid import uuid4
import json
from approximate_section_checkpoint import Session,copy,encode,digest,domain,cross
from fractions import Fraction as Q
from verify_fine_refinement_obstruction import verify

class ArchiveAuthority:
 """Owner-controlled process-local vault, separate from live semantic state.
 Registers independently supplied original-history identity, never inferred
 from a common section. Possession of a valid reference is required to read.
 """
 def __init__(self):self._records={};self._lock=RLock()
 def _admit(self,event,context,history):
  with self._lock:
   if history not in ('A','B'):raise ValueError('UNKNOWN_HISTORY')
   token=uuid4().hex
   self._records[token]=encode({'event':event,'context':context,'history':history})
   return token
 def _resolve(self,token,event,context):
  with self._lock:
   if not isinstance(token,str) or token not in self._records:raise PermissionError('NO_ARCHIVE_AUTHORITY')
   record=json.loads(self._records[token])
   if record['event']!=event or record['context']!=context:raise PermissionError('FOREIGN_RETIREMENT_ARCHIVE')
   return record['history']
 def revoke(self,token):
  with self._lock:
   if token not in self._records:raise PermissionError('UNKNOWN_ARCHIVE')
   del self._records[token]
 def encoded_bytes(self):
  with self._lock:return len(encode(self._records).encode())

class UpgradeSession(Session):
 def __init__(self,authority):
  super().__init__();self._authority=authority;self._event=None;self._context=None;self._resolution=None
 def retire(self,expected,section,*,owner_history,retain_identity=True):
  with self._lock:
   if owner_history not in ('A','B'):raise ValueError('UNKNOWN_HISTORY')
   # Full scalar/source bootstrap must succeed before any archive publication.
   receipt=self.bootstrap(expected,section)
   self._event=uuid4().hex
   self._context=digest({'expected':expected,'section':section})
   if retain_identity:
    receipt['archive_reference']=self._authority._admit(self._event,self._context,owner_history)
   else:receipt['archive_reference']=None
   receipt['retirement_event']=self._event
   receipt['scope']='fixed-family retirement, not an owning projection-compiler migration'
   return receipt
 def _obstruction(self,operation,packet):
  if self._event is None:raise PermissionError('OWNER_RETIREMENT_REQUIRED')
  op=copy(operation)
  if set(op)!={'kind','h_upper','point'} or op['kind']!='fine-upper-point-admission':raise ValueError('UNSUPPORTED_UPGRADE')
  point=tuple(map(Q,op['point']))
  if len(point)!=2:raise ValueError('NONPUBLIC_POINT')
  if not all(sum(a*x for a,x in zip(map(Q,row['normal']),point))<=Q(row['upper']) for row in self._state['frames']):raise ValueError('OBSTRUCTION_POINT_EXCLUDED')
  expected={'family':self._state['family'],'n':self._state['request']['n'],
   'continuation':'append-fine-upper-then-exact-point-admission','h_upper':str(Q(op['h_upper']))}
  proof=copy(packet);assert proof['public_point']==list(map(str,point))
  result=verify(expected,proof)
  return op,result
 def request_upgrade(self,handle,expected_before,operation,obstruction):
  with self._lock:
   self.current(handle);assert expected_before==self._state
   op,result=self._obstruction(operation,obstruction)
   # Reporting ambiguity is NOT a state transition or permission escalation.
   return {'status':'AMBIGUOUS','retirement_event':self._event,'operation':op,
    'alternatives':{'A':result['A_admits_point'],'B':result['B_admits_point']},
    'requires':'event-bound original-history authority','head_unchanged':True}
 def resolve(self,handle,expected_before,operation,obstruction,archive_reference):
  with self._lock:
   self.current(handle);assert expected_before==self._state
   op,result=self._obstruction(operation,obstruction)
   history=self._authority._resolve(archive_reference,self._event,self._context)
   resolved={'status':'RESOLVED','retirement_event':self._event,'operation':op,
    'history':history,'admits_point':result[history+'_admits_point'],
    'scope':'this exact admission request only; no general fine-update capability'}
   # Publish only after semantic verification AND authority validation.
   self._resolution=encode(resolved);self._handle=uuid4().hex
   answer=self.receipt();answer['resolution']=copy(resolved);return answer
