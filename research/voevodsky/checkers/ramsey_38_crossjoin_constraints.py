"""Exhaustive K8 truth-table comparison, in 2^18-coloring bit-parallel blocks."""
import sqlite3,json
from itertools import combinations,product
from pathlib import Path
P=Path(__file__).resolve().parents[1];V=range(8);E=list(combinations(V,2));db=sqlite3.connect(':memory:');db.execute('create table rels(u,v,side,response)');db.executemany('insert into rels values(?,?,?,?)',[(u,v,s,t) for u,v in E for s,t in product(('buyer','seller'),('positive','negative'))]);rows=[(json.loads(v),s) for v,s in db.execute((P/'sql/ramsey_38_crossjoin_constraints.sql').read_text())];assert len(rows)==57
# Bit h denotes the h-th assignment of the low 18 edges. Remaining 10 edges fixed per block.
W=1<<18;allbits=(1<<W)-1;low=[(allbits//((1<<(1<<j))+1))<<(1<<j) for j in range(18)];legal=0
for hi in range(1<<10):
    cols=dict(zip(E,low+[allbits if hi>>j&1 else 0 for j in range(10)]));reject=0
    for vs,s in rows:
        hits=allbits
        for e in combinations(vs,2):hits &= cols[e] if s=='+' else ~cols[e]
        reject |= hits
    # Direct graph test independent of emitted records. Check common plus neighbors
    # of each plus edge. On K8 a minus eight-clique is precisely absence of plus edges.
    any_plus=tri=0
    for (i,j),col in cols.items():
        any_plus |= col
        for k in range(j+1,8):tri |= col & cols[i,k] & cols[j,k]
    direct=tri|(allbits^any_plus);assert reject==direct
    legal+=W-reject.bit_count()
print('112 input rows; 57 constraints;',legal,'legal;', (1<<28)-legal,'illegal; no mismatches')
