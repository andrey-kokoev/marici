"""Enumerate every simple ten-cycle of the full incidence cage, independent of row swap, poles, or matchings. Classify distance partitions and cross-layer degrees."""
from itertools import combinations
from collections import Counter,deque
P=list(combinations(range(6),2));T=[m for m in combinations(P,3) if len(set(sum(m,())))==6];N=[set() for _ in range(30)]
for i,p in enumerate(P):
 for j,t in enumerate(T,15):
  if p in t:N[i].add(j);N[j].add(i)
cycles=[]
def walk(p):
 if len(p)==10:
  if p[0] in N[p[-1]] and p[1]<p[-1]:cycles.append(tuple(p))
  return
 for v in N[p[-1]]-set(p):
  if v>p[0]:walk(p+[v])
for s in range(30):walk([s])
hist=Counter();components=Counter()
for p in cycles:
 d={v:0 for v in p};q=deque(p)
 while q:
  x=q.popleft()
  for y in N[x]-d.keys():d[y]=d[x]+1;q.append(y)
 sizes=tuple(sum(k==i for k in d.values()) for i in range(max(d.values())+1));degrees=tuple(sorted(Counter(sum(d[w]>0 and d[w]!=d[v] for w in N[v]) for v in d if d[v]>0).items()));hist[sizes,degrees]+=1
 for layer in (1,2):
  inside={v for v in d if d[v]==layer};components[layer,tuple(sorted(Counter(len(N[v]&inside) for v in inside).items()))]+=1
print('simple ten-cycles',len(cycles),'distance sizes and cross degrees',hist);print('within-layer degree distributions',components)
assert len(cycles)==72 and hist==Counter({((10,10,10),((1,20),)):72})
for p in cycles:
 assert all(len(N[v]&set(p))==2 for v in p)
