"""Fixed-chart fine rebase with external owner authorization and atomic heads."""
from fractions import Fraction as Q
from threading import RLock
import json
from active_cap_moment_master import Block,query
from active_cap_network_support import support
from moment_column_checkpoints import compact,encode
from verify_moment_fine_rebase import successor,digest,from_answer,verify_rebase

def blocks(state):
 return [Block(*interval,[e for e in state.get('fine_edges',[]) if e['block']==b]) for b,interval in enumerate(state['intervals'])]
def solve(state,seeds=None):
 return query(blocks(state),[(tuple(map(Q,f['normal'])),Q(f['upper'])) for f in state['frames']],tuple(map(Q,state['objective'])),point=None if 'point' not in state else tuple(map(Q,state['point'])),local_frames=[(f['block'],tuple(map(Q,f['normal'])),Q(f['upper'])) for f in state.get('local_frames',[])],initial_columns=seeds)
def compress(state,answer):return compact(state['intervals'],answer['columns'],answer['trace'][-1]['master']['point'][:len(answer['columns'])])

def propose(head,operation):
 after=successor(head['state'],operation);old=blocks(head['state']);new=blocks(after);kept=[];labels=[]
 for column in head['columns']:
  b=column['block'];p=(Q(0),*map(Q,column['potential']));survives=all(p[v]-p[u]<=w for u,v,w in new[b].edges[len(old[b].edges):]);labels.append('KEEP' if survives else 'DROP')
  if survives:kept.append(column)
 bounds=[]
 for b,prior in enumerate(head['bounds']):
  a=tuple(map(Q,prior['objective']));witness=None
  choices=[prior['witness']]+[['0']+c['potential'] for c in kept if c['block']==b]
  for candidate in choices:
   if candidate is None:continue
   p=tuple(map(Q,candidate))
   if all(p[v]-p[u]<=w for u,v,w in new[b].edges) and sum(x*y for x,y in zip(a,new[b].observe(p[1:])))==Q(prior['upper']):witness=candidate;break
  bounds.append({'objective':prior['objective'],'flow':prior['flow']+['0']*(len(new[b].edges)-len(old[b].edges)),'upper':prior['upper'],'witness':witness})
 packet={'before_digest':digest(head),'after_digest':digest(after),'operation':operation,'column_status':labels,'bounds':bounds}
 if head['result']['status']=='INCONSISTENT':return {**packet,'mode':'INHERITED_INCONSISTENCY','result':{'status':'INCONSISTENT'}}
 if len(kept)==len(head['columns']):
  lifts=[]
  for b,block in enumerate(new):
   t=[Q(0)]*block.m
   for c,w in zip(head['columns'],map(Q,head['weights'])):
    if c['block']==b:
     for i,z in enumerate(map(Q,c['potential'])):t[i]+=w*block.s[i]*z
   lifts.append(t)
  glued=lifts[0]+[v for t in lifts[1:] for v in t[1:]]
  result={'status':'OPTIMUM','value':str(Q(head['result']['value'])),'source_lift':list(map(str,glued)),'block_lifts':[list(map(str,t)) for t in lifts]}
  return {**packet,'mode':'RETAINED_OPTIMUM','result':result}
 seeds=list(kept);reseed=[]
 for b,block in enumerate(new):
  if any(c['block']==b for c in kept):continue
  certificate=support(block.edges,(Q(0),)*(block.m+1))
  if certificate['status']=='INCONSISTENT':return {**packet,'mode':'LOCAL_NEGATIVE_CYCLE','empty_block':b,'cycle_edges':certificate['cycle_edges']}
  reseed.append({'block':b,'certificate':certificate});seeds.append({'block':b,'potential':certificate['potential'][1:]})
 answer=solve(after,seeds)
 return {**packet,'mode':'REPAIRED','seeds':seeds,'reseed':reseed,'answer':answer,'compact':compress(after,answer)}

class RebaseSession:
 """The injected authorize callback is an external trusted-owner boundary.
 It is not selected by a proof packet and does not infer actual history.
 """
 def __init__(self,expected_state,answer,compaction,authorize=None):
  state=json.loads(encode(expected_state));answer=json.loads(encode(answer));compaction=json.loads(encode(compaction))
  self._raw=encode(from_answer(state,answer,compaction));self._head=object();self._initial=self._head;self._event=object();self._authorize=authorize;self._lock=RLock()
 @property
 def event(self):return self._event
 @property
 def initial_handle(self):return self._initial
 def snapshot(self,handle):
  with self._lock:
   assert handle is self._head;return json.loads(self._raw)
 def advance(self,handle,expected_before,expected_operation,authorization,candidate):
  with self._lock:
   assert handle is self._head
   old=json.loads(self._raw);assert encode(expected_before)==encode(old['state']);operation=json.loads(encode(expected_operation));after=successor(old['state'],operation)
   context=json.loads(encode([old['state'],operation,after]))
   assert self._authorize is not None and self._authorize(self._event,*context,authorization) is True
   candidate=json.loads(encode(candidate));new=verify_rebase(old,operation,candidate)
   raw=encode(new);token=object();receipt={'mode':candidate['mode'],'status':new['result']['status'],'retained_columns':len(new['columns']),'head_bytes':len(raw),'new_master_solves':len(candidate.get('answer',{}).get('trace',[])),'source_rule':'fixed-chart/grid-six/append-only','capability':'fixed-query result under authorized fine successor; no archive re-exposure'}
   self._raw=raw;self._head=token
   return token,receipt
