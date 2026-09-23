"""Full rank-one domain coverage bound to a real verified migration."""
from fractions import Fraction as Q
from uuid import uuid4
import json
from migration_section_checkpoint import SectionSession,check_section
from checked_retirement_interface import freeze,source,dec

def segment_targets(a,b):
 v=tuple(y-x for x,y in zip(a,b));pivot=next(i for i,x in enumerate(v) if x)
 d=len(a);unit=tuple(Q(int(i==pivot))/v[pivot] for i in range(d))
 targets=[(tuple(-x for x in unit),-a[pivot]/v[pivot]),(unit,1+a[pivot]/v[pivot])]
 for j in range(d):
  if j==pivot:continue
  ratio=v[j]/v[pivot];n=tuple(Q(int(i==j))-ratio*int(i==pivot) for i in range(d));h=a[j]-ratio*a[pivot]
  targets.extend([(n,h),(tuple(-x for x in n),-h)])
 return pivot,targets

def coverage_rows(state):
 r=json.loads(state.runtime_json);base,*_=source(r['m'],r['audits'])
 return base+list(map(dec,r['frames']))+list(state.public_frames)

def verify_full_segment(state,expected_vertices,packet):
 assert set(packet)=={'migration_binding','vertices','source_lifts','coverage_weights'}
 assert packet['vertices']==expected_vertices and packet['migration_binding']==state.migration_binding
 vertices=[tuple(map(Q,v)) for v in expected_vertices];assert len(vertices)>=2
 d=2+len(json.loads(state.runtime_json)['audits']);assert all(len(v)==d for v in vertices)
 a,b=vertices[0],vertices[-1];pivot,targets=segment_targets(a,b)
 knots=[(v[pivot]-a[pivot])/(b[pivot]-a[pivot]) for v in vertices]
 assert knots[0]==0 and knots[-1]==1 and all(x<y for x,y in zip(knots,knots[1:]))
 assert all(v==tuple(x+t*(y-x) for x,y in zip(a,b)) for t,v in zip(knots,vertices))
 assert len(packet['source_lifts'])==len(vertices)
 # Each unique vertex checks original fine evidence once. Shared endpoints
 # use one source-lift array, establishing coherence without duplicate claims.
 for v,t in zip(expected_vertices,packet['source_lifts']):
  check_section(state,[v],{'migration_binding':state.migration_binding,'vertices':[v],'source_lifts':[t]})
 rows=coverage_rows(state);assert len(packet['coverage_weights'])==len(targets)
 for raw,(normal,bound) in zip(packet['coverage_weights'],targets):
  weights=list(map(Q,raw));assert len(weights)==len(rows) and all(w>=0 for w in weights)
  assert tuple(sum(w*n[j] for w,(n,h) in zip(weights,rows)) for j in range(d))==normal
  assert sum(w*h for w,(n,h) in zip(weights,rows))<=bound
 # Domain subset segment follows from those Farkas implications. Reverse
 # inclusion follows from admitted endpoints + convexity. Knots cover it.
 return {'vertex_checks':len(vertices),'coverage_implications':len(targets),'cells':len(vertices)-1}

class FullSegmentSession(SectionSession):
 def __init__(self):super().__init__();self._covers={}
 def _receipt(self):
  result=super()._receipt();result['bytes']['full_segment_encodings']=sum(len(s.encode()) for s in self._covers.values());return result
 def attach_full_segment(self,handle,expected_before,expected_vertices,packet):
  with self._lock:
   self._current(handle);assert expected_before==self._state.descriptor()
   proof=json.loads(freeze(packet));vertices=json.loads(freeze(expected_vertices))
   work=verify_full_segment(self._state,vertices,proof)
   sid=uuid4().hex;self._covers[sid]=freeze(proof);self._handle=uuid4().hex
   self._section_work['vertex_checks']+=work['vertex_checks']
   result=self._receipt();result.update({'section_id':sid,'coverage':'full-current-domain','attachment_work':work});return result
 def covered_lift(self,handle,section_id,point):
  with self._lock:
   self._current(handle)
   if section_id not in self._covers:raise ValueError('UNKNOWN_COVER')
   proof=json.loads(self._covers[section_id]);assert proof['migration_binding']==self._state.migration_binding
   vertices=[tuple(map(Q,v)) for v in proof['vertices']];a,b=vertices[0],vertices[-1];p=tuple(map(Q,point))
   if len(p)!=len(a):raise ValueError('NONPUBLIC_POINT')
   pivot,_=segment_targets(a,b);t=(p[pivot]-a[pivot])/(b[pivot]-a[pivot])
   if not 0<=t<=1 or p!=tuple(x+t*(y-x) for x,y in zip(a,b)):raise ValueError('OUTSIDE_COVER')
   if not all(sum(x*y for x,y in zip(n,p))<=h for n,h in coverage_rows(self._state)):raise ValueError('EXCLUDED_POINT')
   knots=[(v[pivot]-a[pivot])/(b[pivot]-a[pivot]) for v in vertices]
   i=next(i for i in range(len(knots)-1) if knots[i]<=t<=knots[i+1]);w=(t-knots[i])/(knots[i+1]-knots[i])
   x,y=[tuple(map(Q,v)) for v in proof['source_lifts'][i:i+2]]
   self._section_work['interpolated_lifts']+=1
   return [str((1-w)*u+w*v) for u,v in zip(x,y)]
