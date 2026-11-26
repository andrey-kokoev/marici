"""Enumerate all optimal one-step sides inside the saved optimal (4,4) endpoint."""
import json,itertools,collections
from ramsey_retention_slice import D,decode,check,has
r=json.loads(D.read_text())[-1];a=decode(r['graph6']);P=r['seed17'];vertices=[i for i in range(len(a)) if P>>i&1];assert len(vertices)==17 and check(a,P,4,4)
L=[];R=[];c=[~x for x in a]
for t in itertools.combinations(vertices,8):
 m=sum(1<<i for i in t)
 if not has(a,m,3):L.append(m)
 if not has(c,m,3):R.append(m)
h=collections.Counter();example=None;strong=collections.Counter()
for l,r in itertools.product(L,R):
 n=(l&r).bit_count();h[n]+=1
 if n==5:
  assert check(a,l&r,3,3);outside=P&~(l|r);assert outside.bit_count()==6
  joint=[i for i in vertices if outside>>i&1 and not check(a,l|1<<i,3,4) and not check(a,r|1<<i,4,3)];strong[len(joint)]+=1
  if example is None:example=dict(left=l,right=r,seed=l&r,joint=joint)
out=dict(endpoint=P,sides34=len(L),sides43=len(R),overlap_hist=dict(h),joint_hist=dict(strong),example=example);print(out);(D.parent/'ramsey_maximum_square_33.json').write_text(json.dumps(out,indent=1)+'\n')
