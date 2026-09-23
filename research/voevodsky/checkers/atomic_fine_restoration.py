"""Atomic fixed-family restoration across Nima ambiguity and owner archive.
Owner-supplied pre-retirement identity is trusted, not authenticated observation.
"""
from pathlib import Path
from fractions import Fraction as Q
from threading import RLock
from uuid import uuid4
import json,sys
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/nima/checkers'))
from capability_request_checkpoint import CapabilitySession,freeze,digest,snapshot
from verify_scalar_envelope_band import cross
from verify_fine_successor import expected_archive,verify
from approximate_section_checkpoint import source,source_gate

class Vault:
 def __init__(self):self._records={};self._lock=RLock()
 def _admit(self,event,context,n,history):
  archive=expected_archive(n,history)
  with self._lock:
   token=uuid4().hex;self._records[token]=freeze({'event':event,'context':context,'archive':archive});return token
 def _authorize(self,token,event,context,request_digest):
  with self._lock:
   if not isinstance(token,str) or token not in self._records:raise PermissionError('NO_ARCHIVE_AUTHORITY')
   r=json.loads(self._records[token])
   if (r['event'],r['context'])!=(event,context):raise PermissionError('FOREIGN_ARCHIVE')
   return {'archive':r['archive'],'request_digest':request_digest,'event':event}
 def revoke(self,token):
  with self._lock:del self._records[token]
 def bytes(self):
  with self._lock:return len(freeze(self._records).encode())

class Session:
 def __init__(self,vault):
  self._lock=RLock();self._vault=vault;self._handle=None;self._state=None;self._coarse=None
  self._coarse_handle=None;self._ambiguity=None;self._fine=None;self._event=None;self._context=None
 def _current(self,handle,expected):
  if self._handle is None or handle!=self._handle:raise ValueError('STALE_OR_FOREIGN')
  assert expected==self._state
 def receipt(self):
  return {'handle':self._handle,'state':snapshot(self._state),'retirement_event':self._event,
   'bytes':{'live_state':len(freeze(self._state).encode()),
    'ambiguity':len(freeze(self._ambiguity).encode()) if self._ambiguity else 0,
    'fine_successor':len(freeze(self._fine).encode()) if self._fine else 0}}
 def retire(self,expected,section,*,owner_history=None):
  with self._lock:
   if self._handle is not None:raise ValueError('ALREADY_RETIRED')
   if owner_history not in (None,'A','B'):raise ValueError('UNKNOWN_HISTORY')
   service=CapabilitySession();receipt=service.bootstrap(expected,section);source_gate()
   event=uuid4().hex;context=digest({'expected':expected,'section':section})
   token=self._vault._admit(event,context,expected['n'],owner_history) if owner_history else None
   self._coarse=service;self._coarse_handle=receipt['handle'];self._state=receipt['state']
   self._event=event;self._context=context;self._handle=uuid4().hex
   r=self.receipt();r['archive_reference']=token;return r
 def request_fine(self,handle,expected,operation,point,proof):
  with self._lock:
   self._current(handle,expected)
   if self._coarse is None:raise PermissionError('ALREADY_FINE')
   a=self._coarse.request_fine(self._coarse_handle,self._state,operation,point,proof)
   self._ambiguity=snapshot(a);return snapshot(a)
 def restore(self,handle,expected,request_digest,token,candidate):
  with self._lock:
   self._current(handle,expected)
   if self._coarse is None or self._ambiguity is None:raise ValueError('NO_LIVE_AMBIGUITY')
   if request_digest!=self._ambiguity['request_digest']:raise ValueError('STALE_REQUEST')
   grant=self._vault._authorize(token,self._event,self._context,request_digest)
   assert grant['request_digest']==request_digest and grant['event']==self._event
   successor=snapshot(candidate)
   verify(grant['archive'],self._event,self._ambiguity,successor)
   # No fallible verification remains after this point. Old service is removed;
   # published capabilities and runtime share exactly this successor snapshot.
   self._fine=successor;self._state=successor;self._coarse=None;self._coarse_handle=None
   self._ambiguity=None;self._handle=uuid4().hex;return self.receipt()
 def query_point(self,handle,expected,point):
  with self._lock:
   self._current(handle,expected)
   if self._fine is None:raise PermissionError('FINE_AUTHORITY_REQUIRED')
   p=tuple(map(Q,point));assert len(p)==2
   poly=[tuple(map(Q,v)) for v in self._fine['public_polygon']]
   if not all(cross(a,b,p)>=0 for a,b in zip(poly,poly[1:]+poly[:1])):return {'admitted':False,'reason':'outside-original-public-domain'}
   lows=[];highs=[]
   for row in self._fine['fine_rows']:
    a,b,c=map(Q,row['normal']);rhs=Q(row['upper'])-a*p[0]-b*p[1]
    if c>0:highs.append(rhs/c)
    elif c<0:lows.append(rhs/c)
    elif rhs<0:return {'admitted':False,'reason':'public-row'}
   lo,hi=max(lows),min(highs)
   if lo>hi:return {'admitted':False,'interval':[str(lo),str(hi)]}
   h=(lo+hi)/2;t=source(*p,h)
   assert all(0<=v<=100+2*j for j,v in enumerate(t))
   assert all(sum(a*x for a,x in zip(map(Q,row['normal']),(*p,h)))<=Q(row['upper']) for row in self._fine['fine_rows'])
   return {'admitted':True,'interval':[str(lo),str(hi)],'source_lift':list(map(str,t))}
 def reexpose(self,handle,expected):
  with self._lock:self._current(handle,expected);raise PermissionError('NO_ARCHIVE_REEXPOSURE_CAPABILITY')
