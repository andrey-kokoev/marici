"""Test uniform capacity inequalities on every 33-edge residual: if six compatible ports exist, their disjoint footprints can be partitioned into blocks of k=1,2,3. Measure minimum total footprint of one such compatible block."""
import sys,json,gzip,itertools,collections
from pathlib import Path
root=Path(__file__).resolve().parents[2];p=root/'chatgpt/ramsey';sys.path.insert(0,str(p));from ramsey_r37_recursive_proof_verify import graph6,independent_fives
rows=[]
for line in gzip.open(p/'r36_16.g6.gz','rb'):
 A=graph6(line)
 if sum(n.bit_count() for n in A)!=66:continue
 F=independent_fives(A);D=[sum(1<<i for i,f in enumerate(F) if not f&t) for t in F];assert min(D)>0;blocks=[(i,d) for i,d in enumerate(D)];bounds=[]
 for k in (1,2,3):
  bounds.append(min((d.bit_count() for _,d in blocks),default=len(F)+1));
  if k<3:blocks=[(j,d|D[j]) for i,d in blocks for j in range(i+1,len(D)) if not d&D[j]]
 rows.append(dict(graph=line.decode().strip(),capacity=len(F),blockMin=bounds,excluded=[6//k*b>len(F) for k,b in enumerate(bounds,1)]))
print(collections.Counter(tuple(r['excluded']) for r in rows));print(rows[:3]);(root/'voevodsky/results/ramsey_37_group_capacity.json').write_text(json.dumps(rows,indent=2)+'\n');
