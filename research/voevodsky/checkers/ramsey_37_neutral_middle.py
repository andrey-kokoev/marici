"""Centered end stars and fixed middle addresses for the five conjugate pole-swapping reflections. A red four-leaf star here is induced, not the center's full red neighborhood."""
from pathlib import Path
import json
from itertools import combinations
D=Path(__file__).resolve().parents[1]/'results';w=json.loads((D/'ramsey_37_dual_stars.json').read_text());E=set(map(tuple,w['red_edges']));edge=lambda a,b:tuple(sorted((a,b))) in E
s=w['reflection'];X=set(w['stars'][0][0])|{w['rows'][0][0]};Y=set(w['stars'][1][0])|{w['rows'][3][0]};assert {s[v] for v in X}==Y and not X&Y
for z,S in [(1,X),(11,Y)]:assert all(edge(z,v) for v in S-{z}) and not any(edge(*p) for p in combinations(S-{z},2))
r=list(range(22));
for row in w['rows']:
    for i,u in enumerate(row):r[u]=row[(i+1)%5]
recs=[]
for _ in range(5):
    M=set(range(22))-X-Y;fixed=[v for v in sorted(M) if s[v]==v];pairs=[(v,s[v]) for v in sorted(M) if v<s[v]];assert len(fixed)==2 and len(pairs)==5
    ends={v:[sorted(u for u in S if edge(v,u)) for S in (X,Y)] for v in fixed};assert all(len(a)==len(b)==1 and s[a[0]]==b[0] for a,b in ends.values());recs.append(dict(left=sorted(X),right=sorted(Y),fixed=ends,moving_middle=pairs));X={r[v] for v in X};Y={r[v] for v in Y};s=[r[s[r.index(v)]] for v in range(22)]
print(recs[0]);(D/'ramsey_37_neutral_middle.json').write_text(json.dumps(recs,indent=2)+'\n')
