"""Prefix-only C5 inference. Enumerate subgroups on six labels, not Hall matchings. A subgroup survives if the rotational orbit of the observed flags has no repeated left or right endpoint with different mates. No residual fill, mark count or closure label in the predictor. Completed strips used only as test cases."""
from itertools import combinations,permutations
from pathlib import Path
from collections import Counter
import json
D=list(combinations(range(6),2));M=[t for t in combinations(D,3) if len(set(sum(t,())))==6]
def action(p):
 d=lambda x:tuple(sorted(p[i] for i in x));return [D.index(d(x)) for x in D]+[15+M.index(tuple(sorted(map(d,t)))) for t in M]
G=[]
for hub in range(6):
 v=sorted(set(range(6))-{hub})
 for tail in permutations(v[1:]):
    cyc=(v[0],)+tail;p=list(range(6))
    for i,j in zip(cyc,cyc[1:]+cyc[:1]):p[i]=j
    pw=tuple(range(6));powers=[]
    for _ in range(4):pw=tuple(p[x] for x in pw);powers.append(pw)
    if tuple(p)==min(powers):G.append([action(q) for q in [tuple(range(6)),*powers]])
assert len(G)==36
X=list(combinations(range(4),2));swap=(0,2,1,3);r=action([X.index(tuple(sorted(swap[i] for i in x))) for x in X]);flag=lambda a,b:tuple(sorted((a,b)))
def infer(obs):
 ans=[]
 for n,group in enumerate(G):
    forced={(p[i],p[j]) for i,j in obs for p in group}
    if len(forced)==len({i for i,j in forced})==len({j for i,j in forced}):ans.append((n,len(forced)))
 return ans
rows=json.loads(Path(__file__).with_name('ramsey_strip_closure_control.json').read_text());hist=Counter();closed_ids=set();control=Counter();sizes=Counter()
for z in rows:
 p=z['path'];
 if (p[0],p[-1])!=(0,29):continue
 for parity in range(2):
    obs=[];first=None;trace=[]
    for i,(v,w) in enumerate(zip(p,p[1:])):
        obs.append(flag(v,w) if i%2==parity else flag(r[v],r[w]));ans=infer(obs);trace.append(len(ans))
        if len(ans)==1 and first is None:first=i+1
        if i==6:sizes[z['closes'],ans[0][1]]+=1
    control[z['closes'],len(ans)]+=1
    if z['closes']:
        assert len(ans)==1 and ans[0][1]==15;closed_ids.add(ans[0][0]);hist[first]+=1
    print('closed',z['closes'],'parity',parity,'candidates',trace)
print('first unique on successful strips',hist,'distinct groups',len(closed_ids),'final survivor counts',control,'step 7 orbit sizes',sizes)
