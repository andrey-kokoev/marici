"""Readout-specific descent, stability and coefficient-authority controls."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib,json
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
paths=[Path(__file__),HERE/'readout-relative-comparison-contract.md',HERE/'threshold-regulator-consolidation.md',HERE/'spectral-observer-compatible-completion.md']
def hashes():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
def descends(points,F,O):
 seen={}
 for v in points:
  y=F(v)
  if y in seen and seen[y]!=O(v):return False
  seen[y]=O(v)
 return True
before=hashes();points=[(x,y) for x in range(-3,4) for y in range(-3,4)]
first=lambda v:v[0];second=lambda v:v[1]
assert descends(points,first,first)
assert not descends(points,first,second)
identity=lambda v:v
assert descends(points,identity,second)
assert not descends(points,lambda v:first(identity(v)),second)
stability=[]
for n in (1,2,10,100):
 t=Q(1,n)
 for x,y in points:
  output_norm=max(abs(Q(x)),abs(t*y))
  assert abs(x)<=output_norm # first readout, uniformly C=1
 # For v=(0,1), recovering the second readout requires C>=n.
 assert max(Q(0),t)==t
 stability.append({'t':str(t),'first_readout_bound':1,'second_readout_required_bound_at_least':n})
image_readout=lambda k:(k//3)%3
for n in range(-10,11):
 assert image_readout(3*n)==n%3
 for m in range(-10,11):
  assert image_readout(3*n+3*m)==(image_readout(3*n)+image_readout(3*m))%3
assert image_readout(3)==1
assert all((3*r1)%3!=image_readout(3) for r1 in range(3))
assert before==hashes()
report={'passed':True,'source_unchanged':True,'source_sha256':before,'finite_fiber_points':len(points),'readout_relative_stability':stability,'composition_can_destroy_readout':True,'integral_image_readout_exists':True,'integral_ambient_extension_exists':False,'scope':'Exact controls supporting a candidate contract; no physical source admission, general theorem formalization or unauthorized scalar inversion.'}
(HERE/'readout-relative-comparison-contract.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
