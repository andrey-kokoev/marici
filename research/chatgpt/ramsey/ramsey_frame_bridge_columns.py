"""Build a spanning tree on pair readings, with at most two bridges per witness."""
import csv, json, random
from pathlib import Path
from itertools import combinations
from collections import defaultdict
root=Path(__file__).parent

def tests(order):
    for i,w in enumerate(order):
        for d in range(1,10+1):
            yield w,tuple(sorted((w,order[(i-d)%20]))),tuple(sorted((w,order[(i+d)%20])))

def select():
    v=list(range(20));s=v.copy();random.Random(37).shuffle(s);perm=v.copy()
    for i in range(0,20,4):
        block=s[i:i+4]
        for j,x in enumerate(block):perm[x]=block[(j+1)%4]
    for attempt in range(1000):
        parent={p:p for p in combinations(v,2)}
        def find(p):
            while parent[p]!=p:p=parent[p]
            return p
        def join(a,b):
            x,y=find(a),find(b)
            if x==y:return False
            parent[x]=y;return True
        first=[(w,a,b) for w,a,b in tests(v) if join(a,b)];assert len(first)==159
        pending=list(tests(perm));random.Random(attempt).shuffle(pending);added=[];by=defaultdict(int)
        for w,a,b in pending:
            if by[w]<2 and join(a,b):added.append((w,a,b));by[w]+=1
        if len(added)==30:return first,added,attempt
    raise ValueError('no schedule found')

if __name__=='__main__':
    with (root/'ramsey_balanced_order_20.csv').open(newline='') as f:h,*data=csv.reader(f)
    labels=list(map(int,h[1:]));M=[list(map(int,r[1:])) for r in data];value=lambda e:M[e[0]][e[1]]
    first,added,trial=select();adj=defaultdict(list);cols=[[None,None] for _ in labels];report=[]
    for w,a,b in first+added:
        bit=value(a)^value(b);adj[a].append((b,bit));adj[b].append((a,bit))
    for w,a,b in added:
        slot=cols[w].index(None);cols[w][slot]=value(a)^value(b)
        report.append(dict(witness=labels[w],column=21+slot,pairs=[[labels[j] for j in e] for e in (a,b)],bit=cols[w][slot]))
    for anchor in adj:
        seen={anchor:value(anchor)};stack=[anchor]
        while stack:
            a=stack.pop()
            for b,bit in adj[a]:
                if b not in seen:seen[b]=seen[a]^bit;stack.append(b)
        assert len(seen)==190 and all(v==value(p) for p,v in seen.items())
    (root/'ramsey_frame_bridge_columns.json').write_text(json.dumps(dict(order=labels,trial=trial,columns=cols,bridges=report),indent=2)+'\n');print('trial',trial,'records per column',[sum(r[i]!=None for r in cols) for i in (0,1)],'first',report[0])
