"""Nima scalar certificates composed with an owning source-metric contract.
Trusted process-local reuse under public restriction only; no migration claim.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from threading import RLock
from uuid import uuid4
import sys,json,hashlib
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/nima/checkers'))
from verify_scalar_envelope_band import check,domain,envelopes,cross,value
if not __debug__:raise RuntimeError('Assertions required')
D=Q(1,128**4);M=16513*D;R=[Q(1,128**j) for j in range(4)]
def encode(x):return json.dumps(x,sort_keys=True,separators=(',',':'))
def digest(x):return hashlib.sha256(encode(x).encode()).hexdigest()
def copy(x):return json.loads(encode(x))
def source(p,q,h):
 c=[50,51,52,53];a=50+D*h;b=Q(51);u=sum(c)+D*p-a-b
 v=sum(x*r for x,r in zip(c,R))+D*q-a-R[1]*b
 z=(v-R[3]*u)/(R[2]-R[3]);return (a,b,z,u-z)
def source_gate():
 for p,q,h in product((Q(0),Q(1)),repeat=3):
  x=source(p,q,h);assert all(0<=v<=100+2*j for j,v in enumerate(x))
  assert sum(x)==206+D*p and sum(v*r for v,r in zip(x,R))==sum(v*r for v,r in zip((50,51,52,53),R))+D*q
 a=source(0,0,0);b=source(0,0,1)
 assert tuple(y-x for x,y in zip(a,b))==(D,0,-M,16512*D)

def initial(request):return {'family':'owning-m4-moment-curve-two-history-v1','request':copy(request),
 'epsilon':str(M*Q(request['eta'])),'frames':[],
 'capabilities':{'approximate_lift':True,'exact_lift':False,'archive':False}}
class Session:
 def __init__(self):self._lock=RLock();self._state=None;self._proof=None;self._handle=None;self._metrics=None
 def current(self,h):
  if self._state is None or h!=self._handle:raise ValueError('STALE_OR_FOREIGN')
 def receipt(self):return {'handle':self._handle,'state':copy(self._state),'checked_section':digest(self._proof),
  'bytes':{'live_state':len(encode(self._state).encode()),'section':len(encode(self._proof).encode())}}
 def bootstrap(self,expected,packet):
  with self._lock:
   if self._state is not None:raise ValueError('ALREADY_BOOTSTRAPPED')
   state=copy(expected);proof=copy(packet);assert state==initial(state['request'])
   metrics=check(state['request'],proof);source_gate()
   self._state=state;self._proof=proof;self._metrics=metrics;self._handle=uuid4().hex
   result=self.receipt();result['verification']=metrics;return result
 def restrict(self,handle,expected_before,operation):
  with self._lock:
   self.current(handle);assert expected_before==self._state
   op=copy(operation)
   if set(op)!={'kind','normal','upper'} or op['kind']!='append-public':raise PermissionError('PUBLIC_RESTRICTIONS_ONLY')
   if len(op['normal'])!=2:raise ValueError('NONPUBLIC_FRAME')
   n=list(map(Q,op['normal']));b=Q(op['upper'])
   after=copy(self._state);after['frames'].append({'normal':list(map(str,n)),'upper':str(b)})
   self._state=after;self._handle=uuid4().hex;result=self.receipt()
   result['reuse']={'verified_cells_retained':self._metrics['cells'],'fresh_plane_vertex_checks':0,
    'justification':'Public intersection restricts the same verified cover and coherent section.'}
   return result
 def lift(self,handle,point):
  with self._lock:
   self.current(handle);p=tuple(map(Q,point))
   if len(p)!=2:raise ValueError('NONPUBLIC_POINT')
   polygon=domain(self._state['request']['n'])
   if not all(cross(a,b,p)>=0 for a,b in zip(polygon,polygon[1:]+polygon[:1])):raise ValueError('OUTSIDE_DOMAIN')
   if not all(sum(a*x for a,x in zip(map(Q,row['normal']),p))<=Q(row['upper']) for row in self._state['frames']):raise ValueError('EXCLUDED_POINT')
   found=[]
   for cell in self._proof['cells']:
    vs=[tuple(map(Q,v)) for v in cell['vertices']]
    if all(cross(a,b,p)>=0 for a,b in zip(vs,vs[1:]+vs[:1])):found.append(value(tuple(map(Q,cell['formula'])),p))
   assert found and len(set(found))==1
   h=min(Q(1),max(Q(0),found[0]));lo,up=envelopes(self._state['request']['n'])
   f=max(value(a,p) for a in lo);g=min(value(a,p) for a in up)
   return {'state':copy(self._state),'point':list(map(str,p)),'source_lift':list(map(str,source(*p,h))),
    'history_witnesses':[list(map(str,source(*p,max(h,f)))),list(map(str,source(*p,min(h,g))))]}
 def reexpose(self,handle):
  with self._lock:self.current(handle);raise PermissionError('APPROXIMATE_SECTION_IS_NOT_ARCHIVE')
