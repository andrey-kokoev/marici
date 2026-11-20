"""Recover the fixed ground label from the C5 stabilizer. Determine exactly which one-label marks anchor its phase."""
from collections import Counter
from itertools import permutations
from ramsey_strip_transported_seed_orbits import stabilizer,long,P,T,moved,selected,allms
stars=[{i for i,d in enumerate(P) if x in d} for x in range(6)]
actions=[]
for H in stabilizer:actions.append(tuple(stars.index({H[i] for i in s}) for s in stars))
hub,=[x for x in range(6) if all(a[x]==x for a in actions)];assert sorted({a[x] for a in actions}.__len__() for x in range(6))==[1,5,5,5,5,5]
print('target fixed ground label (zero-based)',hub,'stabilizer sizes after marking each label',[sum(a[x]==x for a in actions) for x in range(6)])
sourcehubs={};transport_records=[]
for p in permutations(range(6)):
 tr=lambda d:tuple(sorted(p[x] for x in d));H=tuple([P.index(tr(d)) for d in P]+[15+T.index(tuple(sorted(map(tr,t)))) for t in T])
 for n,pair in enumerate(selected,1):
  for o,j in enumerate(pair):
   if moved(allms[j],H)==long:sourcehubs.setdefault((n,o),set()).add(p.index(hub));transport_records.append((n,o,p))
print('source fixed labels by filling/orientation',sourcehubs)
for key,hs in sourcehubs.items():
 h,=hs
 for x in set(range(6))-{h}:
  counts=Counter(p[x] for n,o,p in transport_records if (n,o)==key);assert len(counts)==5 and set(counts.values())=={1}
print('prescribing image of one nonfixed source label chooses exactly one of five transports within each source class')
