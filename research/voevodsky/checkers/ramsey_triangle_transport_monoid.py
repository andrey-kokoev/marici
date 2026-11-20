"""Test if the map from a history to its reachable reader state already determines its action from EVERY start state. Canonical shortest histories are transition words; omission of a generator extension is certified by equality of full transformations. This proves closure inductively for arbitrary length."""
from pathlib import Path
from collections import deque,Counter
from array import array
import json
D=Path(__file__).resolve().parents[1]/'results';a=json.loads((D/'ramsey_triangle_transport_memory.json').read_text())['full'];t=a['transition'];n=len(t);e=a['initial'];word={e:()};queue=deque([e]);acts={e:array('H',range(n))}
while queue:
    s=queue.popleft()
    for k,u in enumerate(t[s]):
        f=array('H',(t[v][k] for v in acts[s]));
        if u in acts:assert acts[u]==f
        else:acts[u]=f;word[u]=word[s]+(k,);queue.append(u)
def run(w):
    s=e
    for k in w:s=t[s][k]
    return s
rev=[run(word[s][::-1]) for s in range(n)];mul=lambda s,u:acts[u][s]
assert all(rev[rev[s]]==s and all(rev[t[s][k]]==mul(t[e][k],rev[s]) for k in range(8)) for s in range(n));assert all(acts[s][e]==s for s in range(n));ranks=Counter();powers=Counter();idem=Counter();h3=Counter();example=None
for s in range(n):
    rank=len(set(acts[s]));ranks[rank]+=1;idem[mul(s,s)==s]+=1
    visited={};u=e;i=0
    while u not in visited:visited[u]=i;u=mul(u,s);i+=1
    powers[(visited[u],i-visited[u])]+=1
    if len(word[s])==3:h3[(rank,mul(s,s)==s)]+=1
    if example is None and len(word[s])==3 and rev[s]!=s and mul(s,rev[s])!=mul(rev[s],s):example=dict(word=word[s],rev=word[rev[s]],forward_then_reverse=word[mul(s,rev[s])],reverse_then_forward=word[mul(rev[s],s)])
out=dict(states=n,units=ranks[n],idempotents=idem[True],power_types={str(k):v for k,v in sorted(powers.items())},depth3_rank_idempotent={str(k):v for k,v in sorted(h3.items())},example=example);print(out);(D/'ramsey_triangle_transport_monoid.json').write_text(json.dumps(out,indent=2)+'\n')
