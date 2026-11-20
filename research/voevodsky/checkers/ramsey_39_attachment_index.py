"""Frozen cut: hide label 34. Customer proposes signs to 0..16, product to
17..33; (+)-neighbor masks disjoint. Two dispositions on the ordered pair
are computed from prefix-only blocker tables. No unknowns on a proposed star.
Implicit SQL view: do not materialize 2**34 proposal pairs. Independent oracle
uses maximal (-)-cliques of the old graph. Source: McKay's r39_35.g6."""
from pathlib import Path
from itertools import combinations
import json, sqlite3
G='bsaCCA?O?O_aC??`c@O@b?RcHQ?DcA@H?PC_@QO@@Q?DA@MP?RgKADoH?aR?KCbOC_JE?xO@AALC@AJPG?__V?_K@ROO_A@dOG@?_'
U=(1<<34)-1; H=(1<<17)-1
bits=''.join(f'{ord(c)-63:06b}' for c in G[1:]);assert ord(G[0])-63==35
edges=[(i,j) for j in range(35) for i in range(j) if bits[j*(j-1)//2+i]=='1'];old=[(i,j) for i,j in edges if j<34];held=sum(1<<i for i,j in edges if j==34)
P=[0]*34
for i,j in old:P[i]|=1<<j;P[j]|=1<<i
M=[U^p^(1<<i) for i,p in enumerate(P)]
assert not any(P[i]&P[j] for i,j in old)
# Enumerate all plus-independent neighborhoods, including the empty one.
def independent(c,s=0):
    yield s
    while c:
        v=c&-c;c^=v;yield from independent(c&~P[v.bit_length()-1],s|v)
sets=list(independent(U));assert max(s.bit_count() for s in sets)==8
db=sqlite3.connect(':memory:');db.executescript('create table plus2(m integer primary key);create table minus8(m integer primary key);');db.executemany('insert into plus2 values (?)',[(1<<i|1<<j,) for i,j in old]);db.executemany('insert into minus8 values (?)',[(s,) for s in sets if s.bit_count()==8]);
# Exhaust all neighborhoods not rejected by the plus blocker. Split and rejoin by the two proposal fields in SQL.
db.execute('create table proposals(customer integer,product integer,primary key(customer,product)) without rowid');db.executemany('insert into proposals values (?,?)',[(s&H,s>>17) for s in sets]);
q='''with stars as (select customer | (product << 17) as s from proposals) select s from stars where not exists(select 1 from plus2 where (s&m)=m) and not exists(select 1 from minus8 where (s&m)=0)''';got={s for s, in db.execute(q)}
# Independent Bron-Kerbosch maximal-clique oracle, pivoting; never consult SQL or the plus-independent list.
def maximal(r,p,x):
    if not(p|x):yield r;return
    t=p|x;u=(t&-t).bit_length()-1;c=p&~M[u]
    while c:
        v=c&-c;c^=v;i=v.bit_length()-1;yield from maximal(r|v,p&M[i],x&M[i]);p^=v;x|=v
maxs=list(maximal(0,U,0));oracle=set();checked=set()
for clique in maxs:
    s=clique
    while s:
        if s not in checked:
            checked.add(s)
            if all((c&~s).bit_count()<8 for c in maxs):oracle.add(s)
        s=(s-1)&clique
assert max(m.bit_count() for m in maxs)==8 and set(sets)==checked|{0} and held in got and got==oracle
out=dict(source='https://users.cecs.anu.edu.au/~bdm/data/r39_35.g6',hidden_vertex=34,total_stars=1<<34,plus_blocked=(1<<34)-len(sets),plus_pass=len(sets),minus_blocked_after_plus=len(sets)-len(got),plus2=len(old),minus8=sum(s.bit_count()==8 for s in sets),legal=len(got),legal_plus_neighbors=[[i for i in range(34) if s>>i&1] for s in sorted(got)],held_plus_neighbors=[i for i in range(34) if held>>i&1]);print(out);(Path(__file__).resolve().parents[1]/'results/ramsey_39_attachment_index.json').write_text(json.dumps(out,indent=2)+'\n')
