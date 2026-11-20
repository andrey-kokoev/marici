"""Held-out n=7, (3,4). Same boundary-subsumption and round convention as ramsey_exchange_warning_probe.py. Stop each edge order at first safe missed exchange."""
from collections import defaultdict
from functools import lru_cache
from itertools import combinations
import sqlite3,json
from pathlib import Path
from ramsey_sql_matching_exchange import SQL

def probe(order):
    E=sorted(combinations(range(7),2),key=lambda e:e[::-1] if order=='colex' else e);m=len(E)
    def mask(t):return sum(1<<E.index(e) for e in combinations(t,2))
    P=[(bad,mask(t)) for bad,r in [(1,3),(0,4)] for t in combinations(range(7),r)];last=[[p for p in P if p[1].bit_length()==i+1] for i in range(m)]
    def extend(x,i):
        if i==m:yield x;return
        for y in (x,x|1<<i):
            if all((y&p!=p if b else y&p!=0) for b,p in last[i]):yield from extend(y,i+1)
    oracle=list(extend(0,0));db=sqlite3.connect(':memory:');db.execute('create table edge(id,ends)');db.executemany('insert into edge values(?,?)',enumerate((1<<a)|(1<<b) for a,b in E));moves=list(db.execute(SQL));db.close()
    def contradiction(R,B):
        trace=[]
        while True:
            nr=nb=0
            for bad,p in P:
                if p&(B if bad else R):continue
                u=p&~(R|B)
                if not u:return len(trace),trace
                if u.bit_count()==1:
                    if bad:nb|=u
                    else:nr|=u
            if not nr|nb:return None,trace
            trace.append([nr,nb]);
            if nr&nb:return len(trace),trace
            R|=nr;B|=nb
    for c in range(1,m):
        pref=(1<<c)-1;F=defaultdict(list)
        for z in oracle:F[z&pref].append(z>>c)
        @lru_cache(None)
        def residual(x):return {(b,p&~pref) for b,p in P if not p&((pref^x) if b else x)}
        for x in sorted(F):
            for a,b in moves:
                u=a|b;y=x^u
                if u>pref or x>=y or x&u not in (a,b) or y not in F or F[x]!=F[y]:continue
                for dest,src in ((x,y),(y,x)):
                    s=residual(src)
                    for bad,p in sorted(residual(dest)-s):
                        if any(q==0 or (bb==bad and p&q==q) for bb,q in s):continue
                        R=src|(p if bad else 0);B=(pref^src)|(0 if bad else p);rnd,trace=contradiction(R,B)
                        if rnd is None or rnd>1:
                            def direct(z):return all((z&t!=t if b else z&t!=0) for b,t in P)
                            futures=[[v for v in range(1<<(m-c)) if direct((v<<c)|h)] for h in (x,y)];assert futures[0]==futures[1] and set(futures[0])==set(F[x]) and F[x]
                            return dict(order=order,models=len(oracle),cut=c,edges=E,prefixes=[x,y],toggle=[e for i,e in enumerate(E) if u>>i&1],suffixes=futures[0],warning=dict(src=src,dest=dest,bad=bad,mask=p,rounds=rnd,trace=trace))
    return dict(order=order,models=len(oracle),counterexample=None)
if __name__=='__main__':
    out=[probe(o) for o in ('colex','lex')];print(json.dumps(out));(Path(__file__).resolve().parents[1]/'results/ramsey_one_round_seven.json').write_text(json.dumps(out,indent=1)+'\n')
