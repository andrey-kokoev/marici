"""Generate switches in SQL from endpoints alone; audit alternating-color guard against exact futures."""
import sqlite3,json
from collections import defaultdict,Counter
from itertools import combinations
from pathlib import Path

SQL='''WITH matching AS (
 SELECT (1<<a.id)|(1<<b.id) AS bits,a.ends|b.ends AS vertices FROM edge a JOIN edge b
 ON a.id<b.id AND (a.ends & b.ends)=0
) SELECT a.bits,b.bits FROM matching a JOIN matching b
ON a.vertices=b.vertices AND a.bits<b.bits ORDER BY a.bits,b.bits'''

def run(n,k):
    edges=[(i,j) for j in range(n) for i in range(j)];m=len(edges)
    with sqlite3.connect(':memory:') as db:
        db.execute('create table edge(id integer primary key,ends integer)');db.executemany('insert into edge values(?,?)',[(i,(1<<a)|(1<<b)) for i,(a,b) in enumerate(edges)]);moves=list(db.execute(SQL))
    assert len(moves)==3*len(list(combinations(range(n),4)))
    # Reference uses monochromatic subset tests only; has no access to candidate moves.
    pats=[(bad,sum(1<<edges.index(e) for e in combinations(t,2))) for size,bad in ((3,1),(k,0)) for t in combinations(range(n),size)];models=[v for v in range(1<<m) if all((v&p!=p if bad else v&p!=0) for bad,p in pats)]
    count=Counter();counterexample=None
    for cut in range(1,m):
        cap=1<<cut;future=defaultdict(set)
        for v in models:future[v%cap].add(v>>cut)
        parent={x:x for x in future}
        def root(x):
            while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
            return x
        seen=set()
        for x in future:
            for a,b in moves:
                s=a|b
                if s>=cap or (x&s) not in (a,b):continue
                y=x^s;pair=tuple(sorted((x,y)))
                if pair in seen:continue
                seen.add(pair);fx=future[x];fy=future.get(y,set());count['guarded']+=1
                if fx==fy:count['safe']+=1;parent[root(x)]=root(y)
                elif counterexample is None:
                    z=min(fx^fy);counterexample=dict(cut=cut,x=x,y=y,flip=[edges[i] for i in range(m) if s>>i&1],suffix=z,valid='x' if z in fx else 'y')
        groups=defaultdict(list)
        for x,f in future.items():groups[frozenset(f)].append(x)
        for g in groups.values():
            if len(g)>1:
                count['nontrivial_classes']+=1;count['connected_by_safe_generated_moves']+=int(len({root(x) for x in g})==1)
    return dict(n=n,k=k,supports=len(moves),**count,counterexample=counterexample)
if __name__=='__main__':
    res=[run(n,k) for n,k in ((5,3),(5,4),(6,4))];print(json.dumps(res,indent=1));(Path(__file__).resolve().parents[1]/'results/ramsey_sql_matching_exchange.json').write_text(json.dumps(res,indent=1)+'\n')
