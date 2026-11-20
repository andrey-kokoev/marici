"""Distinguish one globally reused frame transformation from stepwise choosing among transformations. No immediate repeat at a marked port fixes the former, but need not make the latter deterministic."""
from collections import Counter
from ramsey_strip_mixed_cube_exchange import ans,r,U,V
allowed=[a for a in ans if a[16]==7];quarter,=[a for a in allowed if a[a[16]]==r[16]];reflection,=[a for a in allowed if a[a[16]]==16]
assert all(quarter[quarter[x]]!=x for x in quarter);cycles=[];seen=set()
for x in quarter:
 if x in seen:continue
 c=[x]
 for _ in range(3):c.append(quarter[c[-1]])
 assert quarter[c[-1]]==x and len(set(c))==4;seen.update(c);cycles.append(c)
hist=Counter();amb=[]
for x in quarter:
 y=quarter[x];nexts={a[y] for a in allowed}-{x};hist[len(nexts)]+=1
 if len(nexts)>1:amb.append((x,y,sorted(nexts)))
print('one global nonreturning map: four-cycles',cycles);print('locally chosen maps after a quarter-turn edge: continuation counts',dict(hist),'ambiguous examples',amb)
assert len(cycles)==4
