"""At exactly 3 marks among 10 visits, retain their complete order under BOTH readings on BOTH paths. Compare closure without assuming the return is a reflected copy."""
from ramsey_strip_unmirrored_holdout import groups,rules,dist,br,full,s,t,fill,combinations,Counter
from collections import defaultdict
ps=groups[11,(3,3)];words={p:tuple(tuple(i for i,x in enumerate(p,1) if tuple(dist[x][j] for j in br) in rule) for rule in rules) for p in ps};bins=defaultdict(Counter)
for p,q in combinations(ps,2):
    if not set(p).isdisjoint(q):continue
    key=tuple(sorted((words[p],words[q])));ok=fill(frozenset(full-{s,t}-set(p)-set(q)));bins[key][ok]+=1
print('distinct word pairs',len(bins),'mixed',sum(len(h)==2 for h in bins.values()),'total',sum(bins.values(),Counter()));print('first mixed:',next(((k,h) for k,h in bins.items() if len(h)==2),None))
