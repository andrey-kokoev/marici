"""Migration-bound simplex sections. Coverage is ONLY the declared simplex."""
from fractions import Fraction as Q
from uuid import uuid4
import json
from migration_checkpoint import Session
from checked_retirement_interface import freeze,source,dec

def rank(rows):
 a=[list(row) for row in rows];r=0
 if not a:return 0
 for j in range(len(a[0])):
  pivot=next((i for i in range(r,len(a)) if a[i][j]),None)
  if pivot is None:continue
  a[r],a[pivot]=a[pivot],a[r];v=a[r][j];a[r]=[x/v for x in a[r]]
  for i in range(r+1,len(a)):
   v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[r])]
  r+=1
  if r==len(a):break
 return r

def check_section(state,expected_vertices,packet):
 if state.lift_json is None:raise PermissionError('NO_FINE_LIFT_CAPABILITY')
 assert set(packet)=={'migration_binding','vertices','source_lifts'}
 assert packet['migration_binding']==state.migration_binding
 assert packet['vertices']==expected_vertices
 vertices=[tuple(map(Q,v)) for v in expected_vertices];runtime=json.loads(state.runtime_json)
 d=2+len(runtime['audits']);assert 1<=len(vertices)<=d+1 and all(len(v)==d for v in vertices)
 assert rank([tuple(x-y for x,y in zip(v,vertices[0])) for v in vertices[1:]])==len(vertices)-1
 lifts=[tuple(map(Q,t)) for t in packet['source_lifts']];assert len(lifts)==len(vertices)
 context=json.loads(state.lift_json);plan=context['plan'];_,_,observe,caps=source(plan['m'],plan['audits'])
 k=2+plan['audits'].index(plan['retire']);frames=list(map(dec,runtime['frames']))+list(state.public_frames)
 for p,t in zip(vertices,lifts):
  assert len(t)==plan['m'] and all(0<=v<=b for v,b in zip(t,caps))
  joint=observe(t);assert joint[:k]+joint[k+1:]==p
  assert all(sum(a*x for a,x in zip(n,joint))<=b for n,b in map(dec,plan['frames']))
  assert all(sum(a*x for a,x in zip(n,p))<=b for n,b in frames)
 return len(vertices)

class SectionSession(Session):
 def __init__(self):
  super().__init__();self._sections={};self._section_work={'vertex_checks':0,'interpolated_lifts':0}
 def _receipt(self):
  result=super()._receipt();result['section_work']=dict(self._section_work)
  result['bytes']['section_encodings']=sum(len(v.encode()) for v in self._sections.values())
  return result
 def attach(self,handle,expected_before,expected_vertices,packet):
  with self._lock:
   self._current(handle);assert expected_before==self._state.descriptor()
   proof=json.loads(freeze(packet));vertices=json.loads(freeze(expected_vertices))
   count=check_section(self._state,vertices,proof)
   sid=uuid4().hex;self._sections[sid]=freeze(proof);self._section_work['vertex_checks']+=count
   self._handle=uuid4().hex;receipt=self._receipt();receipt['section_id']=sid
   receipt['coverage']='declared-simplex-only';return receipt
 def section_lift(self,handle,section_id,point,weights):
  with self._lock:
   self._current(handle)
   if section_id not in self._sections:raise ValueError('UNKNOWN_SECTION')
   proof=json.loads(self._sections[section_id]);assert proof['migration_binding']==self._state.migration_binding
   vertices=[tuple(map(Q,v)) for v in proof['vertices']];w=tuple(map(Q,weights));p=tuple(map(Q,point))
   assert len(w)==len(vertices) and all(v>=0 for v in w) and sum(w)==1
   assert len(p)==len(vertices[0]) and p==tuple(sum(a*v[j] for a,v in zip(w,vertices)) for j in range(len(p)))
   runtime=json.loads(self._state.runtime_json);frames=list(map(dec,runtime['frames']))+list(self._state.public_frames)
   if not all(sum(a*x for a,x in zip(n,p))<=b for n,b in frames):raise ValueError('EXCLUDED_POINT')
   lifts=[tuple(map(Q,t)) for t in proof['source_lifts']]
   t=tuple(sum(a*v[j] for a,v in zip(w,lifts)) for j in range(len(lifts[0])))
   self._section_work['interpolated_lifts']+=1
   return {'source_lift':list(map(str,t)),'point':list(map(str,p)),
    'section_id':section_id,'state':self._state.descriptor(),'coverage':'declared-simplex-only'}
