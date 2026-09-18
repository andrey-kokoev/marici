#!/usr/bin/env python3
"""Cyclic interval rank tables for the six certified rank-two positroid cells."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];src=json.loads((ROOT/'research/nima/results/seven-point-positroid-compiler.json').read_text());n=7;rows=[]
for c in src['cells']:
 omitted=[]
 for name in c['vanishing_cyclic_minors']:omitted.append(int(name.split('(')[1].split(',')[0]))
 parent=list(range(n+1))
 def find(a):
  while parent[a]!=a:parent[a]=parent[parent[a]];a=parent[a]
  return a
 def union(a,b):
  a,b=find(a),find(b)
  if a!=b:parent[b]=a
 for i in omitted:union(i,1 if i==n else i+1)
 table=[]
 for a in range(1,n+1):
  interval=[]
  for length in range(1,n+1):
   interval.append((a+length-2)%n+1);rank=min(2,len({find(j) for j in interval}));table.append({'start':a,'length':length,'end':interval[-1],'rank':rank})
 # Recover necklace as first cyclic pair having rank two.
 necklace=[]
 for a in range(1,n+1):
  order=[(a+j-1)%n+1 for j in range(n)];pair=next((order[i],order[j]) for i in range(n) for j in range(i+1,n) if find(order[i])!=find(order[j]));necklace.append(list(pair))
 rows.append({'history_index':c['history_index'],'bounded_affine_permutation':c['bounded_affine_permutation'],'cyclic_rank_table':table,'recovered_grassmann_necklace':necklace,'parallel_column_classes':[sorted([j for j in range(1,n+1) if find(j)==r]) for r in sorted({find(j) for j in range(1,n+1)})]})
checks={'six_rank_tables':len(rows)==6,'all_necklaces_recovered':all(r['recovered_grassmann_necklace']==src['cells'][i]['grassmann_necklace'] for i,r in enumerate(rows)),'all_full_intervals_rank_two':all(all(e['rank']==2 for e in r['cyclic_rank_table'] if e['length']==n) for r in rows),'rank_tables_distinct':len({tuple(e['rank'] for e in r['cyclic_rank_table']) for r in rows})==6}
out={'schema':'marici.nima.seven-point-positroid-rank-tables.v1','cells':rows,'checks':checks,'passed':all(checks.values()),'meaning':'The cyclic interval rank table is gauge-independent data equivalent to the decorated permutation and determines each positroid cell without choosing a plabic graph.'};p=ROOT/'research/nima/results/seven-point-positroid-rank-tables.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'schema':out['schema'],'checks':checks,'passed':out['passed']},indent=2));raise SystemExit(0 if out['passed'] else 1)
