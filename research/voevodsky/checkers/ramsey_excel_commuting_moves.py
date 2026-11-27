from itertools import combinations
from hashlib import sha256
from collections import defaultdict
from pathlib import Path
import json

D=Path(__file__).resolve().parents[1]/'results'

def check(k):
    rows=[r for r in combinations(range(1,k+1),3) if min(r[1]-r[0],r[2]-r[1])>=2];adj=[set() for _ in rows];edges=[]
    for i,j in combinations(range(len(rows)),2):
        if sum(abs(x-y) for x,y in zip(rows[i],rows[j]))==1:
            adj[i].add(j);adj[j].add(i);edges.append((i,j))
    parent={e:e for e in edges}
    def root(e):
        while e!=parent[e]:e=parent[e]
        return e
    def join(a,b,c,d):parent[root(tuple(sorted((a,b))))]=root(tuple(sorted((c,d))))
    squares=0
    for i in range(len(rows)):
        for j,l in combinations(sorted(x for x in adj[i] if x>i),2):
            for h in adj[j]&adj[l]:
                if h<=i:continue
                squares+=1;join(i,j,l,h);join(i,l,j,h)
    groups=defaultdict(list)
    for e in edges:groups[root(e)].append(e)
    classes={}
    for es in groups.values():
        labels=set()
        for i,j in es:
            r=next(r for r in range(3) if rows[i][r]!=rows[j][r]);labels.add((r+1,rows[i][r]-2*r))
        assert len(labels)==1;key=labels.pop();assert key not in classes;classes[key]=[[rows[i],rows[j]] for i,j in es]
    assert set(classes)=={(r,b) for r in (1,2,3) for b in range(1,k-4)}
    return dict(width=k,rows=len(rows),moves=len(edges),squares=squares,reversible=len(classes),directed=2*len(classes),classes={f'{r}:{b}':v for (r,b),v in sorted(classes.items())})

if __name__=='__main__':
    charts=[check(k) for k in (6,7,8)];prefix='ramsey_excel_commuting_moves';out=dict(charts=charts,protocol_sha=sha256((D/(prefix+'_protocol.md')).read_bytes()).hexdigest());(D/(prefix+'.json')).write_text(json.dumps(out,indent=2)+'\n');print([{k:v for k,v in c.items() if k!='classes'} for c in charts])
