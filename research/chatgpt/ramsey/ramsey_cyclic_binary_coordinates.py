"""Binary coordinates on the eight quotient constructions, with doubling action derived explicitly. Coordinates do not assert that every bit change is a local cage move."""
from collections import Counter
from ramsey_cyclic_quotient_constructor import outputs,P,T,L,R,hubrow
# A Gray labeling of the four nonzero field values.
gray={1:(0,0),2:(1,0),4:(1,1),3:(0,1)};codes={};classes=Counter()
for m in outputs:
 steps=set()
 for i,j in m:
  x,y=P[i]
  if 5 in (x,y):continue
  p,=[p for p in T[j-15] if 5 in p];z,=set(p)-{5}
  if (x+y-2*z)%5==0:continue
  if (2*y-x-z)%5:x,y=y,x
  assert (2*y-x-z)%5==0;steps.add((y-x)%5)
 family=len(steps)-1;assert family in (0,1)
 if family:a,=[a for a in steps if 3*a%5 in steps]
 else:a,=steps
 code=(family,*gray[a]);assert code not in codes;codes[code]=m
 j,=[j for i,j in m if P[i]==(0,5)];col,=[k for k,t in enumerate(R) if j in t];classes[family,col]+=1
p=(0,2,4,1,3,5);tr=lambda d:tuple(sorted(p[x] for x in d));H=[P.index(tr(d)) for d in P]+[15+T.index(tuple(sorted(map(tr,t)))) for t in T]
for (f,x,y),m in codes.items():
 image=frozenset((H[i],H[j]) for i,j in m);assert image==codes[f,1-y,x]
print('family bit versus hub destination orbit counts',dict(sorted(classes.items())));print('eight binary codes',sorted(codes));print('doubling action (family,x,y) -> (family,1-y,x); square complements x,y; fourth iterate identity')
