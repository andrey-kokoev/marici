"""Process-local checkpoints for the fixed owning square-section contract.
Not a migration issuer, generic triangulator, or hostile-process boundary.
"""
from fractions import Fraction as Q
from threading import RLock
from uuid import uuid4
import json,hashlib
if not __debug__:raise RuntimeError('Assertions required')
def encode(x):return json.dumps(x,sort_keys=True,separators=(',',':'))
def digest(x):return hashlib.sha256(encode(x).encode()).hexdigest()
def snapshot(x):return json.loads(encode(x))
ROWS=[((-1,0,0,0),0),((1,0,0,0),1),((0,-1,0,0),0),((0,1,0,0),1),((0,0,-1,0),0),((0,0,1,0),1),((0,0,0,-1),0),((0,0,0,1),1),((1,0,-1,0),0),((0,1,-1,0),0),((-1,-1,1,0),0)]
def initial_state():return {'contract':'owning-square-section-v1','frames':[], 'capabilities':{'answer':True,'lift':True,'archive':False}}
def local_check(public,raw):
 x=tuple(map(Q,raw));assert len(x)==4 and all(0<=v<=100+2*j for j,v in enumerate(x))
 r=[Q(1,128**j) for j in range(4)];center=[50,51,52,53];delta=Q(1,128**4)
 z=((sum(x)-206)/delta,(sum(a*b for a,b in zip(x,r))-sum(a*b for a,b in zip(center,r)))/delta,(x[0]-50)/delta,(x[1]-51)/delta)
 assert z[:2]==tuple(map(Q,public))
 assert all(sum(Q(a)*v for a,v in zip(n,z))<=b for n,b in ROWS)
 return raw

def verify(state,packet,old=None):
 assert state['contract']=='owning-square-section-v1'
 assert state['capabilities']==initial_state()['capabilities']
 assert set(state)==set(initial_state())
 for row in state['frames']:
  assert set(row)=={'normal','upper'} and len(row['normal'])==2
  list(map(Q,row['normal']));Q(row['upper'])
 assert packet['public_vertices']==[['0','0'],['1','0'],['1','1'],['0','1']]
 assert packet['triangles']==[[0,1,2],[0,2,3]]
 assert packet['fine_rows']==[{'normal':list(map(str,a)),'upper':str(b)} for a,b in ROWS]
 assert len(packet['vertex_source_lifts'])==4
 stats={'local_checks':0,'local_hits':0,'fresh_cover_checks':1,'hashed_local_bytes':0};cache={}
 for v,x in zip(packet['public_vertices'],packet['vertex_source_lifts']):
  dep={'epoch':'square-vertex-v1','contract':state['contract'],'capabilities':state['capabilities'],'rows':packet['fine_rows'],'vertex':v,'lift':x}
  key=digest(dep);stats['hashed_local_bytes']+=len(encode(dep).encode())
  if old is not None and key in old:stats['local_hits']+=1
  else:local_check(v,x);stats['local_checks']+=1
  cache[key]=encode(x)
 # Fixed diagonal triangulation covers the full square with barycentric
 # weights (1-p,p-q,q) or (1-q,p,q-p). One shared vertex array guarantees
 # diagonal agreement. New domain is its intersection with public frames,
 # so restriction inherits cover and coherence, including the empty case.
 # Topology/schema and all frame syntax above are checked on every call.
 return cache,stats

class Session:
 def __init__(self):self._head=None;self._lock=RLock()
 def _publish(self,state,packet,cache,stats):
  handle=uuid4().hex;self._head=(handle,encode(state),encode(packet),dict(cache))
  return {'handle':handle,'state':snapshot(state),'work':dict(stats),
   'bytes':{'live_state':len(encode(state).encode()),'section':len(encode(packet).encode()),
    'checkpoint':len(encode(self._head).encode()),'archive':0}}
 def bootstrap(self,expected,packet):
  with self._lock:
   if self._head is not None:raise ValueError('ALREADY_BOOTSTRAPPED')
   state=snapshot(expected);proof=snapshot(packet);assert state==initial_state()
   cache,stats=verify(state,proof);return self._publish(state,proof,cache,stats)
 def advance(self,handle,expected_before,operation,candidate):
  with self._lock:
   if self._head is None or self._head[0]!=handle:raise ValueError('STALE_OR_FOREIGN')
   _,encoded,proof,old=self._head;before=json.loads(encoded);assert before==expected_before
   op=snapshot(operation);c=snapshot(candidate)
   if set(op)!={'kind','row'} or op['kind']!='append-public':raise PermissionError('PUBLIC_ONLY')
   after=snapshot(before);after['frames'].append(op['row']);assert c['state']==after
   cache,stats=verify(after,c['section'],old)
   return self._publish(after,c['section'],cache,stats)
 def lift(self,handle,point):
  with self._lock:
   if self._head is None or self._head[0]!=handle:raise ValueError('STALE_OR_FOREIGN')
   state=json.loads(self._head[1]);proof=json.loads(self._head[2]);p,q=map(Q,point)
   if not (0<=p<=1 and 0<=q<=1):raise ValueError('OUTSIDE_DOMAIN')
   if not all(Q(row['normal'][0])*p+Q(row['normal'][1])*q<=Q(row['upper']) for row in state['frames']):raise ValueError('EXCLUDED_POINT')
   ids,w=([0,1,2],(1-p,p-q,q)) if q<=p else ([0,2,3],(1-q,p,q-p))
   return [str(sum(a*Q(proof['vertex_source_lifts'][i][j]) for i,a in zip(ids,w))) for j in range(4)]
 def reexpose(self,handle):
  with self._lock:
   if self._head is None or self._head[0]!=handle:raise ValueError('STALE_OR_FOREIGN')
   raise PermissionError('SECTION_IS_NOT_AN_ARCHIVE')
