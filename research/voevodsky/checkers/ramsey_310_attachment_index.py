"""Leave out vertex 38 of the stored (3,10;39) witness. Exact one-star SQL index vs maximal-clique oracle."""
import csv, json, sqlite3
from pathlib import Path
HOME=Path(__file__).resolve().parents[1]
source=HOME.parent/'chatgpt/ramsey/ramsey_3_10_witness_39.csv'
A=[list(map(int,r)) for r in csv.reader(source.open()) if r];n=38;u=(1<<n)-1
assert len(A)==39 and all(len(r)==39 for r in A)
assert all(A[i][j]==A[j][i] in (0,1) for i in range(39) for j in range(39)) and not any(A[i][i] for i in range(39))
plus=[sum(b<<j for j,b in enumerate(row[:n])) for row in A[:n]];minus=[u^p^(1<<i) for i,p in enumerate(plus)];held=sum(b<<j for j,b in enumerate(A[n][:n]))
edges=[(1<<i)|(1<<j) for i in range(n) for j in range(i) if A[i][j]];assert not any(plus[i]&plus[j] for i in range(n) for j in range(i) if A[i][j])
def independent(avail,s=0):
    yield s
    while avail:
        v=avail&-avail;avail^=v;yield from independent(avail&~plus[v.bit_length()-1],s|v)
sets=list(independent(u));assert max(map(int.bit_count,sets))==9
nine=[s for s in sets if s.bit_count()==9];db=sqlite3.connect(':memory:');db.executescript('create table plus2(m integer primary key);create table minus9(m integer primary key);create table proposals(c integer,p integer,primary key(c,p)) without rowid;');db.executemany('insert into plus2 values (?)',((s,) for s in edges));db.executemany('insert into minus9 values (?)',((s,) for s in nine));db.executemany('insert into proposals values (?,?)',((s&((1<<19)-1),s>>19) for s in sets));got={s for s, in db.execute('with stars as (select c|(p<<19) as s from proposals) select s from stars where not exists(select 1 from plus2 where (s&m)=m) and not exists(select 1 from minus9 where (s&m)=0)')}
# Independently enumerate maximal minus cliques, then their subsets. A star
# fails the minus test precisely if some old maximal clique retains >=9 vertices.
def maximal(r,p,x):
    if not(p|x):yield r;return
    t=p|x;c=p&~minus[(t&-t).bit_length()-1]
    while c:
        v=c&-c;c^=v;i=v.bit_length()-1;yield from maximal(r|v,p&minus[i],x&minus[i]);p^=v;x|=v
mx=list(maximal(0,u,0));assert max(map(int.bit_count,mx))==9
cand={0}
for m in mx:
    s=m
    while s:cand.add(s);s=(s-1)&m
big=[m for m in mx if m.bit_count()>=9];oracle={s for s in cand if all((m&~s).bit_count()<9 for m in big)};assert cand==set(sets) and got==oracle and held in got
out=dict(source=source.name,hidden=n,total=1<<n,plus_edges=len(edges),minus_nines=len(nine),plus_pass=len(sets),legal=len(got),held_plus=[i for i in range(n) if held>>i&1],legal_masks=sorted(got));print(json.dumps(out));(HOME/'results/ramsey_310_attachment_index.json').write_text(json.dumps(out,indent=2)+'\n')
