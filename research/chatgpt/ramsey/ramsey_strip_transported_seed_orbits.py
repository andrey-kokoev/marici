"""Group transported ordered seed flags under six-label symmetries of the fixed longest matching. Distinguish arbitrary phase from distinct seed classes."""
from itertools import permutations
from collections import Counter
from ramsey_strip_short_long_all_transports import long,r,P,T,moved,selected,allms,I,comp,order
stabilizer=[];records=[]
for p in permutations(range(6)):
 tr=lambda d:tuple(sorted(p[x] for x in d));H=tuple([P.index(tr(d)) for d in P]+[15+T.index(tuple(sorted(map(tr,t)))) for t in T])
 if moved(long,H)==long:stabilizer.append(H)
 for n,pair in enumerate(selected,1):
  for orient,j in enumerate(pair):
   if moved(allms[j],H)==long:records.append((n,orient,tuple(H[v] for v in (0,16,7,29))))
print('long matching six-label stabilizer size',len(stabilizer),'orders',Counter(map(order,stabilizer)))
seeds={z for _,_,z in records};todo=set(seeds);orbits=[]
while todo:
 seed=min(todo);orb={tuple(g[v] for v in seed) for g in stabilizer};assert orb<=seeds;todo-=orb;orbits.append(orb)
print('transported ordered seeds',len(seeds),'orbits',list(map(len,orbits)))
for k,orb in enumerate(orbits,1):print('seed orbit',k,'source fillings/orientations',sorted({(n,o) for n,o,z in records if z in orb}),'pole images',sorted({(z[0],z[3]) for z in orb}))
assert len(stabilizer)==5 and all(len(o)==5 for o in orbits)
