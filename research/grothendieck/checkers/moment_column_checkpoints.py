"""Bounded warm columns, exact allocation compaction, verifier-owned lineage.
Optional local flow-result reuse; all global master/gluing checks remain fresh.
"""
from fractions import Fraction as Q
from threading import RLock
import json,hashlib
from pathlib import Path
if not __debug__:raise RuntimeError('Assertions required')
def encode(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def observe(interval,z):
 ids=range(interval[0],interval[1]+1);t=[Q(1+j%3)*v for j,v in zip(ids,z)]
 return (t[0],t[-1],sum(t),sum(Q(1,128**j)*v for j,v in zip(ids,t)))
def dependency(vectors):
 # Columns are (1,left,right,U,V); find a rational kernel vector.
 A=[list(row) for row in zip(*vectors)];pivots=[];r=0;n=len(vectors)
 for j in range(n):
  p=next((i for i in range(r,len(A)) if A[i][j]),None)
  if p is None:continue
  A[r],A[p]=A[p],A[r];v=A[r][j];A[r]=[x/v for x in A[r]]
  for i in range(len(A)):
   if i!=r:
    v=A[i][j];A[i]=[x-v*y for x,y in zip(A[i],A[r])]
  pivots.append(j);r+=1
  if r==len(A):break
 free=next(j for j in range(n) if j not in pivots);out=[Q(0)]*n;out[free]=Q(1)
 for i,j in enumerate(pivots):out[j]=-A[i][free]
 assert all(sum(row[j]*out[j] for j in range(n))==0 for row in zip(*vectors))
 return out

def compact(intervals,columns,weights):
 weights=list(map(Q,weights));assert len(weights)==len(columns);result=[]
 for b,interval in enumerate(intervals):
  active=[i for i,c in enumerate(columns) if c['block']==b and weights[i]>0]
  while len(active)>5:
   mu=dependency([(Q(1),*observe(interval,tuple(map(Q,columns[i]['potential'])))) for i in active])
   theta=min(weights[i]/v for i,v in zip(active,mu) if v>0)
   for i,v in zip(active,mu):weights[i]-=theta*v
   active=[i for i in active if weights[i]>0]
  result.extend({'index':i,'weight':str(weights[i])} for i in active)
 return result

def verify_compaction(spec,answer,packet):
 columns=answer['columns'];weights=tuple(map(Q,answer['trace'][-1]['master']['point'][:len(columns)]));indices=[p['index'] for p in packet]
 assert len(set(indices))==len(indices) and all(type(i)==int and 0<=i<len(columns) for i in indices)
 retained=tuple(Q(p['weight']) for p in packet);assert all(v>0 for v in retained)
 # Reconstruct all five affine coordinates directly in raw source atoms.
 for b,(left,right) in enumerate(spec['intervals']):
  def v(i):
   col=columns[i];z=tuple(map(Q,col['potential']));assert len(z)==right-left+1
   raw=[Q(1+j%3)*z[j-left] for j in range(left,right+1)]
   return (Q(1),raw[0],raw[-1],sum(raw),sum(Q(1,128**j)*raw[j-left] for j in range(left,right+1)))
  old=[i for i,c in enumerate(columns) if c['block']==b];new=[(i,w) for i,w in zip(indices,retained) if columns[i]['block']==b]
  assert 1<=len(new)<=5
  target=tuple(sum(weights[i]*v(i)[j] for i in old) for j in range(5));actual=tuple(sum(w*v(i)[j] for i,w in new) for j in range(5))
  assert target[0]==1 and actual==target
 return [columns[i] for i in indices]

class VerifierSession:
 def __init__(self,full_verifier,local_verifier=None):
  self._verify=full_verifier;self._local=local_verifier;self._head=None;self._lock=RLock();self._cache={}
  self._rule_path=Path(local_verifier.__code__.co_filename) if local_verifier else None
  self._epoch=hashlib.sha256(self._rule_path.read_bytes()).hexdigest() if local_verifier else None
 def _replay(self,state,answer,seeds=None,bootstrap=False):
  staged={};stats={'local_checks':0,'local_hits':0,'predecessor_hits':0,'within_candidate_hits':0}
  if self._local is None:
   self._verify(state,answer,seeds);stats['local_checks']=sum(len(t['pricing']) for t in answer['trace']);return staged,stats
  assert hashlib.sha256(self._rule_path.read_bytes()).hexdigest()==self._epoch
  def local(data,q,certificate):
   ids,s,edges=data;key=tuple(ids)
   dependency=encode({'epoch':self._epoch,'ids':ids,'scales':list(map(str,s)),'edges':[(u,v,str(w)) for u,v,w in edges],'objective':list(map(str,q))})
   proof=encode(certificate);entry=None
   if not bootstrap:
    for origin,candidate in (('within_candidate_hits',staged.get(key)),('predecessor_hits',self._cache.get(key))):
     if candidate is not None and candidate[:2]==(dependency,proof):entry=candidate;stats[origin]+=1;break
   if entry is None:
    p,upper=self._local(data,q,certificate);entry=(dependency,proof,encode({'potential':list(map(str,p)),'upper':str(upper)}));stats['local_checks']+=1
   else:stats['local_hits']+=1
   staged[key]=entry;result=json.loads(entry[2]);return tuple(map(Q,result['potential'])),Q(result['upper'])
  self._verify(state,answer,seeds,pricing_checker=local)
  return staged,stats
 def _check_state(self,state):
  assert set(state)<= {'intervals','objective','frames','local_frames','point'}
  assert len(state['objective'])==4 and state['intervals']
  assert all(set(f)=={'normal','upper'} and len(f['normal'])==4 for f in state['frames'])
  assert all(set(f)=={'block','normal','upper'} and len(f['normal'])==4 and 0<=f['block']<len(state['intervals']) for f in state.get('local_frames',[]))
  if 'point' in state:assert len(state['point'])==4
 def _publish(self,state,answer,compact_packet,seeds,cache,stats):
  payload={'state':state,'seeds':seeds,'weights':[p['weight'] for p in compact_packet],'status':answer['status'],'proof_digest':hashlib.sha256(encode(answer)).hexdigest(),'rule':'active-cap-chain/global-chart/endpoint-U-V/v1'}
  assert len(cache)<=len(state['intervals'])
  payload['checked_local']=[{'nodes':ids,'dependency':entry[0].decode(),'proof':entry[1].decode(),'result':entry[2].decode()} for ids,entry in cache.items()]
  raw=encode(payload);token=object();receipt={'retained_columns':len(seeds),'checkpoint_bytes':len(raw),'source_coordinates':sum(len(c['potential']) for c in seeds),'full_master_checks':len(answer['trace']),'pricing_proofs_presented':sum(len(t['pricing']) for t in answer['trace'])}
  receipt.update(stats);receipt['cached_local_entries']=len(cache)
  self._payload=raw;self._cache=dict(cache);self._head=token
  return token,receipt
 def bootstrap(self,expected_state,answer,compact_packet):
  with self._lock:
   assert self._head is None;state=json.loads(encode(expected_state));self._check_state(state);answer=json.loads(encode(answer));compact_packet=json.loads(encode(compact_packet))
   cache,stats=self._replay(state,answer,bootstrap=True);seeds=verify_compaction(state,answer,compact_packet)
   return self._publish(state,answer,compact_packet,seeds,cache,stats)
 def snapshot(self,handle):
  with self._lock:
   assert handle is self._head and handle is not None
   return json.loads(self._payload)
 def advance(self,handle,expected_before,expected_frame,answer,compact_packet):
  with self._lock:
   assert handle is self._head and handle is not None
   previous=json.loads(self._payload);assert encode(expected_before)==encode(previous['state'])
   state=previous['state'];state['frames'].append(json.loads(encode(expected_frame)));self._check_state(state)
   answer=json.loads(encode(answer));compact_packet=json.loads(encode(compact_packet))
   cache,stats=self._replay(state,answer,previous['seeds']);seeds=verify_compaction(state,answer,compact_packet)
   return self._publish(state,answer,compact_packet,seeds,cache,stats)
