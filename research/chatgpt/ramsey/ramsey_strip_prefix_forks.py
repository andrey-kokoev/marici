"""Explain the prefix threshold by trie forks and exact Hall completions, with no rotation assumption in the second test. All 40 reflected 11-step routes; one row numbering per pole pair as in the census."""
from collections import defaultdict,Counter
from functools import lru_cache
from ramsey_strip_prefix_rotation import rows,D,M,G,r,flag,infer
N=[tuple(j+15 for j,m in enumerate(M) if d in m) for d in D]
def count(obs):
 used={x:y for x,y in obs};assert len(used)==len(obs)==len(set(used.values()))
 @lru_cache(None)
 def fill(i,taken):
    if i==15:return 1
    options=[used[i]] if i in used else N[i];return sum(fill(i+1,taken|(1<<(j-15))) for j in options if not taken&(1<<(j-15)))
 return fill(0,0)
summary=Counter();forks=defaultdict(list);facts={}
for z in rows:
 p=z['path'];key=(p[0],p[-1]);k=facts.get(key,0)+1;facts[key]=k
 for parity in (0,1):
    obs=[flag(v,w) if i%2==parity else flag(r[v],r[w]) for i,(v,w) in enumerate(zip(p,p[1:]))];n,sz=infer(obs[:7])[0];group=G[n];seen=set();first_three=None
    for i,(x,y) in enumerate(obs[:7],1):
        seen|={a[x] for a in group}
        if len(seen)==15 and first_three is None:first_three=i
    counts=tuple(count(obs[:i]) for i in (5,6,7,8));summary[z['closes'],first_three,counts]+=1
    assert counts[2]==1 and counts[3]==int(z['closes']);
    left=set(range(15))-{i for i,j in obs[:7]};right=set(range(15,30))-{j for i,j in obs[:7]};forced=set(obs[:7]);
    while left:
        options={(i,j) for i in left for j in N[i] if j in right};pair=next(((i,j) for i,j in sorted(options) if sum(x==i for x,y in options)==1 or sum(y==j for x,y in options)==1),None);assert pair;forced.add(pair);left.remove(pair[0]);right.remove(pair[1])
    assert (obs[7] in forced)==z['closes']
    if key==(0,29) and parity==0:forks[tuple(p[:8])].append((k,z['closes'],first_three,counts))
print('prefix forks, literal poles:');print(list(forks.values()));print('all 40 x two alternations:',summary)
