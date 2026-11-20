"""SQLite anti-join guard for edge 01 at the seven-edge cut, (3,4) on five roles."""
import sqlite3
from itertools import combinations

SQL='''SELECT c.id FROM context c WHERE NOT EXISTS (
 SELECT 1 FROM pattern p WHERE NOT EXISTS (
  SELECT 1 FROM member m JOIN fact f ON f.edge=m.edge
  WHERE m.pattern=p.id AND f.context=c.id AND f.red<>p.bad
 )) ORDER BY c.id'''

def main():
    E=[(i,j) for j in range(5) for i in range(j)]
    patterns=[(bad,tuple(E.index(e) for e in combinations(t,2))) for size,bad in ((3,1),(4,0)) for t in combinations(range(5),size)]
    def suffixes(prefix):
        return {s for s in range(8) if all(any(((prefix|(s<<7))>>i)&1!=bad for i in edges) for bad,edges in patterns)}
    contexts=range(0,128,2);safe={c for c in contexts if suffixes(c)==suffixes(c^1)};live={c for c in safe if suffixes(c)}
    db=sqlite3.connect(':memory:');db.executescript('CREATE TABLE context(id PRIMARY KEY);CREATE TABLE pattern(id PRIMARY KEY,bad);CREATE TABLE member(pattern,edge);CREATE TABLE fact(context,edge,red,PRIMARY KEY(context,edge));')
    for j,(bad,edges) in enumerate(patterns):
        if 0 in edges:
            db.execute('insert into pattern values(?,?)',(j,bad));db.executemany('insert into member values(?,?)',[(j,i) for i in edges if i!=0])
    for c in contexts:
        db.execute('insert into context values(?)',(c,));db.executemany('insert into fact values(?,?,?)',[(c,i,c>>i&1) for i in range(1,7)])
    accepted={c for c, in db.execute(SQL)};assert accepted<=safe and 20 in accepted and 32 not in accepted
    # Minimum conjunction of fixed labeled colors, matching context 20 and sound on every context.
    for k in range(7):
        mins=[S for S in combinations(range(1,7),k) if all(c in safe for c in contexts if all(((c^20)>>i)&1==0 for i in S))];
        if mins:break
    print('SQL accepts:',sorted(accepted),'live:',sorted(accepted&live));print('all safe live:',sorted(live),'safe including dead:',len(safe));print('minimal sound conjunctions at 20:',[[(E[i],20>>i&1) for i in S] for S in mins]);print('suffixes:',{c:sorted(suffixes(c)) for c in (20,21,32,33)})
if __name__=='__main__':main()
