"""Can forced colors discharge SQL boundary warnings? Independent completion oracle used only to audit guards. No recursive SAT search in the guard."""
from collections import Counter,defaultdict
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import sqlite3,json
from ramsey_sql_matching_exchange import SQL

def probe(n,k,order):
    E=sorted(combinations(range(n),2), key=(lambda e:e[::-1]) if order=='colex' else (lambda e:e)); m=len(E);full=(1<<m)-1
    def mask(t):return sum(1<<E.index(e) for e in combinations(t,2))
    pats=[(bad,mask(t)) for bad,r in [(1,3),(0,k)] for t in combinations(range(n),r)]
    @lru_cache(maxsize=131072)
    def forced(R,B):
        rounds=0
        while True:
            nr=nb=0
            for bad,p in pats:
                if p&(B if bad else R):continue
                u=p&~(R|B)
                if not u:return True,rounds
                if u&(u-1)==0:
                    if bad:nb|=u
                    else:nr|=u
            if nr&nb:return True,rounds+1
            if not (nr|nb):return False,rounds
            R|=nr;B|=nb;rounds+=1
    @lru_cache(maxsize=None)
    def residual(pref,val):return frozenset((b,p&~pref) for b,p in pats if not(p&((pref^val) if b else val)))
    with sqlite3.connect(':memory:') as db:
        db.execute('create table edge(id,ends)');db.executemany('insert into edge values(?,?)',enumerate((1<<i)|(1<<j) for i,j in E));moves=list(db.execute(SQL))
    oracle=[v for v in range(full+1) if all((v&p!=p if b else v&p!=0) for b,p in pats)];cnt=Counter();dist=Counter();example=None
    for cut in range(1,m):
        pref=(1<<cut)-1;F=defaultdict(set)
        for v in oracle:F[v&pref].add(v>>cut)
        seen=set()
        for start in F:
            for a,b in moves:
                u=a|b
                if u>pref or start&u not in (a,b):continue
                x,y=sorted((start,start^u));key=x,y
                if key in seen:continue
                seen.add(key);safe=F.get(x,set())==F.get(y,set());cnt['tested']+=1;cnt['safe']+=safe;threats=[]
                for dest,src in ((x,y),(y,x)):
                    d=residual(pref,dest);s=residual(pref,src)
                    for bad,p in sorted(d-s):
                        if any(q==0 or (bb==bad and p&q==q) for bb,q in s):continue
                        R=src|(p if bad else 0);B=(pref^src)|(0 if bad else p);threats.append((R,B,bad,p))
                if not threats:assert safe;cnt['original_certified']+=1;continue
                checks=[forced(R,B) for R,B,_,_ in threats]
                if all(v for v,_ in checks):
                    assert safe;cnt['forced_extra']+=1;dist[max(h for _,h in checks)]+=1
                    if example is None:example=dict(cut=cut,x=x,y=y,threats=threats,rounds=checks)
                elif safe:cnt['safe_unresolved']+=1
    return dict(n=n,k=k,order=order,counts=dict(cnt),rounds_for_extra=dict(dist),example=example)
if __name__=='__main__':
    r=[probe(n,k,order) for order in ('colex','lex') for n,k in ((5,3),(5,4),(6,4))];print(json.dumps(r,indent=1));(Path(__file__).resolve().parents[1]/'results/ramsey_exchange_warning_probe.json').write_text(json.dumps(r,indent=1)+'\n')
