"""Independent atom-metric answer checking; no checkpoint/adapter import."""
from pathlib import Path
from fractions import Fraction as Q
import sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/nima/checkers'))
from verify_scalar_envelope_band import domain,envelopes,cross,value
if not __debug__:raise RuntimeError('Assertions required')
def verify(expected,point,answer):
 assert answer['state']==expected and answer['point']==point
 assert expected['family']=='owning-m4-moment-curve-two-history-v1'
 assert expected['capabilities']=={'approximate_lift':True,'exact_lift':False,'archive':False}
 delta=Q(1,128**4);eps=Q(expected['epsilon']);assert eps==16513*delta*Q(expected['request']['eta']) and eps>=0
 p=tuple(map(Q,point));assert len(p)==2;polygon=domain(expected['request']['n'])
 assert all(cross(a,b,p)>=0 for a,b in zip(polygon,polygon[1:]+polygon[:1]))
 assert all(sum(a*x for a,x in zip(map(Q,row['normal']),p))<=Q(row['upper']) for row in expected['frames'])
 r=[Q(1,128**j) for j in range(4)];U=206+delta*p[0];V=sum(x*y for x,y in zip((50,51,52,53),r))+delta*p[1]
 def admitted(raw):
  x=tuple(map(Q,raw));assert len(x)==4 and all(0<=v<=100+2*j for j,v in enumerate(x))
  assert sum(x)==U and sum(a*b for a,b in zip(x,r))==V
  return x
 t=admitted(answer['source_lift']);assert len(answer['history_witnesses'])==2
 lower,upper=envelopes(expected['request']['n']);f=max(value(a,p) for a in lower);g=min(value(a,p) for a in upper)
 for i,raw in enumerate(answer['history_witnesses']):
  x=admitted(raw);h=(x[0]-50)/delta;assert x[1]==51 and 0<=h<=1
  assert (h>=f if i==0 else h<=g)
  assert max(abs(a-b) for a,b in zip(t,x))<=eps
 return True
