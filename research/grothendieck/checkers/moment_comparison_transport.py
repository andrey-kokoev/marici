"""Exact fixed-query transport between append-only fine-edge presentations.

The caller supplies an already verified head and independently authorized destination
path. This module proves semantic equality; it does not authorize either path.
"""
from collections import defaultdict, deque
from fractions import Fraction as Q
from verify_moment_fine_rebase import data, successor, flow_check, mixed_result, digest
from moment_column_checkpoints import encode
from verify_active_cap_moment_master import admitted
import json
from threading import RLock


def row_key(edge):
 return (edge['block'], -1 if edge['tail'] is None else edge['tail'], -1 if edge['head'] is None else edge['head'], Q(edge['upper']))


def replay(base, operations):
 state=base
 for op in operations:state=successor(state,op)
 return state


def transport(head, base, source_operations, destination_operations):
 """Reindex dual flows; retain a previously certified optimum or contradiction.

 Preconditions: head was checked from base via source_operations; destination
 operations were authorized for the same base by an external owner. Comparing
 digests here is a consistency check, NOT an authority check.
 """
 source=replay(base,source_operations);destination=replay(base,destination_operations)
 assert head['state']==source
 assert len(source_operations)==len(destination_operations)
 assert sorted(map(row_key,source_operations))==sorted(map(row_key,destination_operations))
 old=data(source);new=data(destination);assert len(old)==len(new)
 bounds=[]
 for b,(o,n,prior) in enumerate(zip(old,new,head['bounds'])):
  assert o[:2]==n[:2]
  buckets=defaultdict(deque)
  for i,row in enumerate(n[2]):buckets[row].append(i)
  reordered=[Q(0)]*len(n[2])
  for row,weight in zip(o[2],map(Q,prior['flow'])):
   assert buckets[row];reordered[buckets[row].popleft()]=weight
  assert all(not indices for indices in buckets.values())
  current={**prior,'flow':list(map(str,reordered))}
  flow_check(o,prior);flow_check(n,current);bounds.append(current)
 for column in head['columns']:
  b=column['block'];admitted(new[b],tuple(map(Q,column['potential'])),True)
 result=head['result']
 if result['status']=='OPTIMUM':
  # The retained allocation must still be admitted; the old verified global
  # optimality transfers because the *entire* source relation is identical.
  assert mixed_result(destination,head['columns'],head['weights'],result['value'])==result
 else:assert result=={'status':'INCONSISTENT'}
 return {'state':destination,'result':json.loads(encode(result)),'columns':json.loads(encode(head['columns'])),
         'weights':json.loads(encode(head['weights'])),'bounds':bounds}

class ComparisonSession:
 """Owner approval is external; detachment disables comparison but not replay."""
 def __init__(self,head,base,operations,authorize):
  assert head['state']==replay(base,operations)
  self._raw=encode(head);self._base=json.loads(encode(base));self._path=json.loads(encode(operations))
  self._authorize=authorize;self._event=object();self._handle=object();self._lock=RLock()
 @property
 def event(self):return self._event
 @property
 def handle(self):return self._handle
 def snapshot(self,handle):
  with self._lock:
   assert handle is self._handle
   return json.loads(self._raw)
 def detach(self,handle):
  with self._lock:
   assert handle is self._handle
   self._authorize=None;self._handle=object();return self._handle
 def compare(self,handle,expected_path,destination,grant):
  with self._lock:
   assert handle is self._handle and encode(expected_path)==encode(self._path)
   assert self._authorize is not None
   path=json.loads(encode(destination))
   assert self._authorize(self._event,json.loads(encode(self._base)),json.loads(encode(self._path)),path,grant) is True
   successor_head=transport(json.loads(self._raw),self._base,self._path,path)
   self._raw=encode(successor_head);self._path=path;self._handle=object()
   return self._handle
