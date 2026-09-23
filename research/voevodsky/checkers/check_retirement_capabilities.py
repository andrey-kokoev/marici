"""Explicit capabilities on a verified singleton public-image migration."""
from dataclasses import dataclass,replace
from fractions import Fraction as Q
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
def observe(x):return sum(x),sum(v*Q(1,128**j) for j,v in enumerate(x))
def admitted(x):return len(x)==3 and all(0<=v<=100+2*j for j,v in enumerate(x))
@dataclass(frozen=True)
class Fine:
 moments:tuple
 frames:tuple=()
 def member(self,x):
  return admitted(x) and observe(x)==self.moments and all(sum(a*b for a,b in zip(n,self.moments))<=b for n,b in self.frames)
@dataclass(frozen=True)
class Retired:
 public:tuple
 frames:tuple=()
 section:tuple|None=None
 archive:Fine|None=None
 def nonempty(self):return all(sum(a*b for a,b in zip(n,self.public))<=b for n,b in self.frames)
 def member(self,y):
  if len(y)!=2:raise ValueError('UNDECLARED_OBSERVABLE')
  return self.nonempty() and tuple(y)==self.public
 def threshold(self,axis,h):
  if axis not in (0,1):raise ValueError('UNDECLARED_OBSERVABLE')
  if not self.nonempty():return 'INCONSISTENT'
  return 'FORCED_TRUE' if self.public[axis]<=h else 'FORCED_FALSE'
 def refine(self,normal,upper):
  if len(normal)!=2:raise ValueError('NONLOCAL_REFINEMENT')
  return replace(self,frames=self.frames+((tuple(map(Q,normal)),Q(upper)),))
 def lift(self):
  if self.section is None:raise PermissionError('NO_FINE_LIFT_CAPABILITY')
  if not self.nonempty():raise ValueError('EMPTY_PUBLIC_STATE')
  assert admitted(self.section) and observe(self.section)==self.public
  return self.section
 def reexpose(self):
  if self.archive is None:raise PermissionError('NO_FINE_RELATION_ARCHIVE')
  return replace(self.archive,frames=self.archive.frames+self.frames)
def size(obj):return len(json.dumps(obj,separators=(',',':')).encode())
def main():
 x=(Q(50),Q(51),Q(52));y=observe(x);old=Fine(y)
 other=tuple(a+b for a,b in zip(x,(Q(-1,128),Q(129,128),Q(-1))))
 assert old.member(x) and old.member(other) and x!=other
 answer=Retired(y);lift=Retired(y,section=x);archive=Retired(y,section=x,archive=old)
 rejected=0
 for state,operation in [(answer,'lift'),(answer,'reexpose'),(lift,'reexpose')]:
  try:getattr(state,operation)()
  except PermissionError:rejected+=1
  else:raise AssertionError('unsupported capability accepted')
 for state in (answer,lift,archive):
  assert state.member(y) and state.threshold(0,153)=='FORCED_TRUE'
  assert state.refine((1,0),153).member(y)
  assert not state.refine((1,0),152).member(y)
  assert state.refine((1,0),152).threshold(0,153)=='INCONSISTENT'
  try:state.refine((0,0,1),1)
  except ValueError:rejected+=1
  else:raise AssertionError('hidden refinement accepted')
 assert lift.lift()==x
 reopened=archive.reexpose();assert reopened.member(x) and reopened.member(other)
 empty=archive.refine((1,0),152)
 assert not empty.reexpose().member(x) and not empty.reexpose().member(other)
 try:empty.lift()
 except ValueError:rejected+=1
 else:raise AssertionError('empty state produced witness')
 assert archive.member(y) # prior snapshot unchanged
 report={'passed':True,'capability_rejections':rejected,'distinct_old_compatible_witnesses':[list(map(str,x)),list(map(str,other))],
 'ledger':{'public_payload_bytes':size({'moments':list(map(str,y)),'frames':[]}),
 'optional_lift_payload_bytes':size(list(map(str,x))),
 'optional_fine_archive_payload_bytes':size({'source':'tail-box-m3','moment_equalities':list(map(str,y)),'frames':[]})},
 'scope':'Fixture-bound migration and API capability checks, not a general independently verified migration format or confidentiality mechanism.'}
 (OUT/'retirement-capabilities.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
