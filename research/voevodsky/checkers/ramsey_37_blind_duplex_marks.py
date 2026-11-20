"""Blind mark selection within the two candidate three-star partitions. For each, try every end leaf independently and every middle leaf touching P. Reflect the triple and require a unique *outside* common decoder; test when neither single view suffices. No apex label used in scoring."""
import json
from itertools import product,combinations
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results';load=lambda f:json.loads((D/(f+'.json')).read_text());g=load('ramsey_37_dual_stars');N={v:set() for v in range(22)}
for u,v in g['red_edges']:N[u].add(v);N[v].add(u)
s=g['reflection'];rot=list(range(22))
for row in g['rows']:
    for i,u in enumerate(row):rot[u]=row[(i+1)%5]
def decode(t):return set.intersection(*(N[v] for v in t))
out=[]
for rec in load('ramsey_37_three_stars_apex'):
    results=[]
    for c in rec['choices']:
        L,R=set(rec['left']),set(rec['right']);lc,=[v for v in L if len(N[v]&L)==4];rc,=[v for v in R if len(N[v]&R)==4];leaves=set(c['leaves']);inside=L|R|leaves|{c['center']};cnt=0;hits=[]
        for a,m,b in product(sorted(L-{lc}),sorted(leaves&N[0]),sorted(R-{rc})):
            cnt+=1;T=(a,m,b);S=tuple(map(s.__getitem__,T));x,y=decode(T),decode(S);joint=x&y
            if len(joint)!=1 or joint&inside:continue
            h,=joint;marks=set(T+S);mins=[t for k in range(1,len(marks)+1) for t in combinations(sorted(marks),k) if decode(t)==joint and all(len(decode(set(t)-{v}))>1 for v in t if len(t)>1)]
            hits.append(dict(mark=T,reflected=S,decoded=h,views=[sorted(x),sorted(y)],minimal_mark_sets=mins,needs_both=len(x)>1 and len(y)>1))
        assert cnt==32 and len(hits)==1;results.append(dict(center=c['center'],tested=cnt,hits=hits))
    assert sum(r['hits'][0]['needs_both'] for r in results)==1;out.append(results);s=[rot[s[rot.index(v)]] for v in range(22)]
print(out[0]);(D/'ramsey_37_blind_duplex_marks.json').write_text(json.dumps(out,indent=2)+'\n')
