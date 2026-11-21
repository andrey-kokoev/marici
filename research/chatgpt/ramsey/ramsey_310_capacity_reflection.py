"""Two-deletion blocker capacities and the proposed P5 fringe reversal."""
import csv,json
from itertools import combinations
from pathlib import Path
from ramsey_mutual_repair_conjecture import sevens
D=Path(__file__).parent
A=[sum(1<<z for z in {(v+s*d)%38 for s in (1,-1) for d in (1,3,5,12,19)}) for v in range(38)];I=list(sevens(A,k=9));rows=[]
for d in range(1,20):
    m=1|1<<d;cap,t=min(((t&A[0]).bit_count()+(t&A[d]).bit_count(),t) for t in I if not t&m);rows.append((d,cap,[i for i in range(38) if t>>i&1]))
print('capacity minima',[r[1] for r in rows]);print(rows[0]);(D/'ramsey_310_capacity_minima.json').write_text(json.dumps(rows,indent=2)+'\n')
B=[sum(int(x)<<j for j,x in enumerate(row)) for row in csv.reader((D/'ramsey_3_10_witness_39.csv').read_text().splitlines()) if row];path=[(12,38),(9,37),(13,37),(21,33),(33,35)];print('endpoint degree pairs',[sorted(B[i].bit_count() for i in e) for e in path]);print('successive shared endpoints',[set(e)&set(f) for e,f in zip(path,path[1:])]);assert len(set(path[0])&set(path[1]))!=len(set(path[-1])&set(path[-2]))
