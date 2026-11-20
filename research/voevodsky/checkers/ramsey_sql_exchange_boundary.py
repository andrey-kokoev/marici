"""Boundary antijoin for matching exchanges. Input partial edges only; full completions used separately as oracle."""
from ramsey_sql_matching_exchange import SQL
from itertools import combinations
from collections import defaultdict,Counter
import sqlite3,json
from pathlib import Path

RISKS='''WITH sides(side,val) AS (VALUES (0,:x),(1,:y)),
 residual AS MATERIALIZED (
 SELECT side,bad,sites,edges,edges & ~:prefix AS needed FROM sides CROSS JOIN pattern
 WHERE (edges & :prefix & CASE bad WHEN 1 THEN ~val ELSE val END)=0)
 SELECT p.side,p.bad,p.sites & ~:inside AS outside,p.needed,p.sites
 FROM residual p WHERE (p.edges & :flip)<>0 AND NOT EXISTS (
 SELECT 1 FROM residual q WHERE q.side<>p.side AND
 (q.needed=0 OR (q.bad=p.bad AND (p.needed & q.needed)=q.needed)))
 ORDER BY p.side,p.bad,p.sites'''

def run(n,k):
    db=sqlite3.connect(':memory:');E=[(i,j) for j in range(n) for i in range(j)];m=len(E);db.execute('create table edge(id integer,ends integer)');db.executemany('insert into edge values (?,?)',enumerate((1<<i)|(1<<j) for i,j in E));moves=list(db.execute(SQL));db.execute('create table pattern(bad,sites,edges)');pats=[(bad,sum(1<<i for i in s),sum(1<<E.index(e) for e in combinations(s,2))) for size,bad in [(3,1),(k,0)] for s in combinations(range(n),size)];db.executemany('insert into pattern values(?,?,?)',pats)
    def valid(v):return all((v&e!=e if b else v&e!=0) for b,_,e in pats)
    models=[v for v in range(1<<m) if valid(v)];ct=Counter();demo=[]
    for cut in range(1,m):
        cap=1<<cut;prefix=cap-1;F=defaultdict(set)
        for v in models:F[v&prefix].add(v>>cut)
        seen=set()
        for start in F:
            for a,b in moves:
                flip=a|b
                if flip>=cap or (start&flip) not in (a,b):continue
                x,y=sorted((start,start^flip));key=x,y
                if key in seen:continue
                seen.add(key);inside=sum(1<<i for i in {w for j,e in enumerate(E) if flip>>j&1 for w in e})
                risks=db.execute(RISKS,dict(x=x,y=y,prefix=prefix,flip=flip,inside=inside)).fetchall();safe=F.get(x,set())==F.get(y,set());ct['tested']+=1;ct['exact_safe']+=int(safe);ct['certified']+=int(not risks);assert risks or safe
                if (n,k,cut,x,y)==(5,4,5,12,18):
                    for side,bad,outside,need,sites in risks:
                        vx,vy=(x,y) if side else (y,x);w=next((s for s in sorted(F.get(vx,())) if (((s<<cut)&need)==need if bad else ((s<<cut)&need)==0)),None)
                        demo.append(dict(bad_on='after' if side else 'before',color='red' if bad else 'blue',vertices=[i for i in range(n) if sites>>i&1],outside=[i for i in range(n) if outside>>i&1],needed=[e for j,e in enumerate(E) if need>>j&1],legal_opposite_suffix=w))
    db.close();return dict(n=n,k=k,counts=ct,demo=demo)
if __name__=='__main__':
    report=[run(n,k) for n,k in [(5,3),(5,4),(6,4)]];print(json.dumps(report,indent=1));(Path(__file__).resolve().parents[1]/'results/ramsey_sql_exchange_boundary.json').write_text(json.dumps(report,indent=1)+'\n')
